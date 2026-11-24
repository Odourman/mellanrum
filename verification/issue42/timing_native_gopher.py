#!/usr/bin/env python3
"""Issue #42: genuine Gopher2600 CPU/TV/TIA instruction traces on unchanged BFDEB.
Diagnostic POKE changes only emulator RIOT RAM, never product ROM.
Outputs exact commands, raw console logs, parsed per-scanline evidence.
Requires original Gopher2600 binary and exact 16KiB F6 ROM as CLI arguments.
"""
import argparse,collections,concurrent.futures,hashlib,json,pathlib,re,subprocess,time
p=argparse.ArgumentParser()
p.add_argument("--gopher",required=True)
p.add_argument("--rom",required=True)
p.add_argument("--out",required=True)
a=p.parse_args()
rom=pathlib.Path(a.rom);exe=pathlib.Path(a.gopher);out=pathlib.Path(a.out);out.mkdir(parents=True,exist_ok=True)
ROM_SHA="bfdeb5308dcecc526e802cd95886b94e0ce4953628e7bc7190c5d49231deac06"
GOPHER_SHA="7b12dff57fcb73154122d2477f35d9c8ae8b344649bc0faa8ff6f5663c70470b"
assert hashlib.sha256(rom.read_bytes()).hexdigest()==ROM_SHA
assert len(rom.read_bytes())==16384
assert hashlib.sha256(exe.read_bytes()).hexdigest()==GOPHER_SHA
base=["VERSION","CARTRIDGE HASH","CARTRIDGE MAPPER","PERIPHERAL LEFT STICK","PANEL SET P0PRO"]+["STEP FRAME"]*16+["STICK LEFT FIRE","STEP FRAME","STEP FRAME","STICK LEFT NOFIRE"]+["STEP FRAME"]*4
def roomstart(room):
 return base+[f"POKE 0x00b9 {room}","PANEL HOLD SELECT","STEP FRAME","STEP FRAME","PANEL RELEASE SELECT"]+["STEP FRAME"]*110
r=roomstart(12)
cases={
"ACTIII_BASELINE":r,
"ACTIII_ACTIVE_LATE":r+["POKE 0x00db 2"],
"ACTIII_SHADOW_ACTIVE":r+["POKE 0x00db 2","POKE 0x00f0 0"],
"ACTIII_SHADOW_FIRE":r+["POKE 0x00db 2","POKE 0x00f0 0","STICK LEFT FIRE"],
"ACTIII_SHADOW_PHASE":r+["POKE 0x00db 2","POKE 0x00f0 0","POKE 0x00c4 1"],
"ACTIII_SHADOW_ECHO":r+["POKE 0x00db 2","POKE 0x00f0 0","POKE 0x00d7 8","POKE 0x00d8 0","POKE 0x00d9 9","POKE 0x00da 0","POKE 0x00d2 1","POKE 0x00d3 9","POKE 0x00d4 1","STICK LEFT FIRE"],
"TITLE_NATIVE":["VERSION","CARTRIDGE HASH","CARTRIDGE MAPPER","PERIPHERAL LEFT STICK","PANEL SET P0PRO"]+["STEP FRAME"]*64,
"FRI_CONTROLLER":["VERSION","CARTRIDGE HASH","CARTRIDGE MAPPER","PERIPHERAL LEFT STICK","PANEL SET P0AM"]+["STEP FRAME"]*16+["STICK LEFT FIRE","STEP FRAME","STEP FRAME","STICK LEFT NOFIRE"]+["STEP FRAME"]*126+["STICK LEFT FIRE"]
}
pat=re.compile(r"FR=(\d+) SL=(\d+) CL=(-?\d+)\n[^\n]+\nPC=([0-9a-f]{4}) A=([0-9a-f]{2}) X=([0-9a-f]{2}) Y=([0-9a-f]{2}) SP=([0-9a-f]{2})",re.I)
WSYNC={0xf68c,0xf7c7,0xf7d6,0xf7f8,0xf83c,0xf87a,0xf89b,0xf8b7,0xf8b9,0xf8da,0xf8dc,0xf8de,0xf8e0,0xf90e,0xf963,0xf98e,0xf9ac,0xf9c6,0xf9cf,0xfa0a}
def run(case,prelude):
 target=out/case;target.mkdir(exist_ok=True)
 commands=prelude+["TV FRAME","QUANTUM INSTRUCTION","ONSTEP TV,TIA,CPU","ONSTEP ON","STEP FRAME","ONSTEP OFF","TV FRAME","QUIT"]
 (target/"commands.txt").write_text("\n".join(commands)+"\n")
 with (target/"stdout.log").open("w") as stream:
  process=subprocess.run([str(exe),"HEADLESS",str(rom)],input="\n".join(commands)+"\n",text=True,stdout=stream,stderr=subprocess.STDOUT,timeout=120)
 logs=(target/"stdout.log").read_text(errors="replace")
 matches=[(int(fr),int(sl),int(cl),int(pc,16)) for fr,sl,cl,pc,*_ in pat.findall(logs)]
 bysite=collections.defaultdict(list);late=[];positions=collections.defaultdict(list)
 for i,(fr,sl,cl,pc) in enumerate(matches):
  if pc in (0xf7c7,0xf7d6,0xf7f8,0xf83c,0xf87a,0xf89b,0xf90e,0xf963,0xf98e,0xf9cf):positions[f"{pc:04X}"].append(sl)
  if pc in WSYNC and i+1<len(matches):
   nxt=matches[i+1];diff=(nxt[0]-fr)*262+nxt[1]-sl
   row={"pc":f"{pc:04X}","scanline":sl,"cpu_cycle":(cl+68)//3,"delta_scanlines":diff}
   bysite[f"{pc:04X}"].append(row)
   if diff!=1:late.append(row)
 total=[int(s) for s in re.findall(r"top: \d+, bottom: \d+, total: (\d+)",logs)]
 report={"case":case,"rom_sha256":ROM_SHA,"type":"CONTROLLER_TITLE_FRI" if case in ("TITLE_NATIVE","FRI_CONTROLLER") else "FORCED_RAM_DIAGNOSTIC","exit_code":process.returncode,"cpu_instructions":len(matches),"frame_lines":total,"wsync_count":sum(map(len,bysite.values())),"late_wsync":late,"late_visible_wsync":[x for x in late if 51<=x["scanline"]<=226],"renderer_absolute_scanlines":dict(positions),"max_start_cycle_per_wsync":{k:max(x["cpu_cycle"] for x in v) for k,v in bysite.items()},"status":"PASS_BOUNDED" if process.returncode==0 and total[-1]==262 and not [x for x in late if 51<=x["scanline"]<=226] else "FAIL_OR_INCONCLUSIVE"}
 (target/"result.json").write_text(json.dumps(report,indent=2)+"\n")
 return report
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
 results=list(pool.map(lambda c:run(*c),cases.items()))
checks={}
z={r["case"]:r for r in results}
for pc in ("F7C7","F7D6","F7F8","F83C","F87A","F89B","F90E","F963","F98E"):
 checks[pc]=z["ACTIII_BASELINE"]["renderer_absolute_scanlines"].get(pc,[])==z["ACTIII_ACTIVE_LATE"]["renderer_absolute_scanlines"].get(pc,[])
summary={"rom_sha256":ROM_SHA,"gopher_sha256":GOPHER_SHA,"test_cases":len(results),"all_262":all(r["frame_lines"][-1]==262 for r in results),"all_exit0":all(r["exit_code"]==0 for r in results),"cpu_instructions":sum(r["cpu_instructions"] for r in results),"wsync_events":sum(r["wsync_count"] for r in results),"visible_skipped_wsync":sum(len(r["late_visible_wsync"]) for r in results),"normal_active_absolute_kernel_alignment":checks,"cases":results,"scope":"Actual 6507/NTSC single-frame instruction traces; RAM forcing explicitly DIAGNOSTIC; only title/FRI control-only."}
(out/"summary.json").write_text(json.dumps(summary,indent=2)+"\n")
with (out/"SHA256SUMS").open("w") as f:
 for path in sorted(out.rglob("*")):
  if path.is_file() and path.name!="SHA256SUMS":f.write(hashlib.sha256(path.read_bytes()).hexdigest()+"  "+str(path.relative_to(out))+"\n")
print(json.dumps({k:v for k,v in summary.items() if k!="cases"},indent=2))
if not (summary["all_262"] and summary["all_exit0"] and summary["visible_skipped_wsync"]==0 and all(checks.values())):raise SystemExit(2)
