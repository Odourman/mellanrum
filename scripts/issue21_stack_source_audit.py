#!/usr/bin/env python3
"""Conservative JSR-only source call-graph stack bound for unbanked 6507 code.
NOT a dynamic CPU-SP trace. Fail on recursion, unrecognized stack op, or RAM overlap.
"""
from collections import defaultdict
from pathlib import Path
import json,re,sys

source=Path("rom/src/main.asm").read_text()
code=source.split("\n        include \"rom/src/data.inc\"")[0]
lines=code.splitlines()
jsrs=set(re.findall(r"(?m)^\s+jsr\s+(\w+)",code,re.IGNORECASE))
entries=jsrs | {"Frame","Reset"}
edges=defaultdict(set)
current="(setup)"
for line in lines:
 clean=line.split(";",1)[0]
 label=re.match(r"^([A-Za-z_][A-Za-z_0-9]*):\s*$",clean)
 if label and label.group(1) in entries: current=label.group(1)
 m=re.match(r"^\s+jsr\s+(\w+)",clean,re.IGNORECASE)
 if m:edges[current].add(m.group(1))
unresolved=jsrs-{re.match(r"^([A-Za-z_][A-Za-z_0-9]*):",x).group(1) for x in lines if re.match(r"^([A-Za-z_][A-Za-z_0-9]*):",x)}
assert not unresolved,("JSR_TARGETS_MISSING",sorted(unresolved))
prohibited=[(i+1,line.strip()) for i,line in enumerate(lines) if re.match(r"^\s+(pha|php|phx|phy|pla|plp|plx|ply|brk)\b",line,re.IGNORECASE)]
assert not prohibited,("UNACCOUNTED_STACK_PUSH_POP",prohibited)
assert len(re.findall(r"(?im)^\s+txs\b",code))==1, "TXS reset contract changed"
assert "        sei" in code, "interrupt masking contract changed"

def longest(node,route):
 if node in route:raise AssertionError(("RECURSIVE_JSR",route,node))
 nroute=route+(node,)
 follow=[longest(child,nroute) for child in edges[node]]
 return max(follow,key=len) if follow else nroute
chains=[longest(name,()) for name in ("Frame","Reset")]
critical=max(chains,key=len)
depth=len(critical)-1
bytes_required=depth*2
sym=Path(sys.argv[1] if len(sys.argv)>1 else "build/issue21/mellanrum_vnext.sym")
pairs={}
for line in sym.read_text().splitlines():
 m=re.match(r"^([A-Za-z_]\w*)\s+([0-9A-Fa-f]{4})\s+\(R\s*\)",line)
 if m:pairs[m.group(1)]=int(m.group(2),16)
assert pairs.get("shadowOn")==0xF1,("RAM_TOP_CHANGED",pairs.get("shadowOn"))
assert pairs.get("mapRows")==0xB0,("COLLISION_RAM_ADDRESS_CHANGED",pairs.get("mapRows"))
stack_available=0xFF-pairs["shadowOn"]
assert bytes_required<=stack_available,("STACK_AND_ZP_OVERLAP",critical,bytes_required,stack_available)
r={"status":"PASS","class":"CONSERVATIVE_SOURCE_JSR_GRAPH_NOT_DYNAMIC_STACK_INSTRUMENTATION",
 "longest_jsr_chain":critical,"nested_jsrs":depth,
 "stack_push_bytes_from_jsr":bytes_required,
 "ram_highest_symbol":"shadowOn","ram_highest_address":pairs["shadowOn"],
 "stack_bytes_available":stack_available,
 "margin_bytes":stack_available-bytes_required,
 "assumptions":"No stack-based CPU tricks or interrupts; 6507 SEI, JSR/RTS only; source-scanned straight-line maximum across all control branches, not proof of actual emulator SP high-water",
 "new_ROM_SHA":"READ_FROM_NATIVE_ARTIFACT"}
out=Path("build/issue21/stack_source_audit.json");out.parent.mkdir(exist_ok=True,parents=True)
out.write_text(json.dumps(r,indent=2)+"\n")
print("ISSUE21_STATIC_STACK_BOUND",json.dumps(r))
