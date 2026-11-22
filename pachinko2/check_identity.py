#!/usr/bin/env python3
"""Immutable ROM identity gate. No game source or oracle writes."""
import hashlib,json,pathlib,sys
ROM_SHA='e9ea87d381bcf8da39ec055d7d6951ceff97b21d3a798addd10fbbe540c5e974'
COMMIT='49eb168b17d0254d06cf50d87c60e8fb6016db6e'
p=pathlib.Path(sys.argv[1]);rom=p.read_bytes();ok=len(rom)==4096 and hashlib.sha256(rom).hexdigest()==ROM_SHA
result={'case':'native_dasm_freeze','status':'PASS' if ok else 'FAIL','source_commit':COMMIT,'rom_sha_expected':ROM_SHA,'rom_sha_measured':hashlib.sha256(rom).hexdigest(),'rom_size':len(rom),'evidence':'REAL_DASM_NATIVE_ASSEMBLY'}
print(json.dumps(result));sys.exit(0 if ok else 2)
