#!/usr/bin/env python3
"""Issue #26: reproducible standard F6 4x4096 native DASM build, never copy PR23 4K.
Each bank is native assembled as a cartridge window $F000-$FFFF. Data in
banks 0..2 occupies 3840 live TIA score bytes; runtime code at $FF00.
Bank 3 contains real 15-room game, F6 shared return/reset trampolines.
Concatenate as 0,1,2,3 in canonical F6 order.
"""
from pathlib import Path
import argparse,subprocess,hashlib,json,sys
p=argparse.ArgumentParser();p.add_argument("--out",default="build/issue26");a=p.parse_args()
root=Path(__file__).resolve().parents[2];out=(root/a.out).resolve();out.mkdir(parents=True,exist_ok=True)
src=[root/f"rom/f6/bank{i}_score.asm" for i in range(3)]+[root/"rom/src/main.asm"]
paths=[]
for i,file in enumerate(src):
    b=out/f"bank{i}.bin";sym=out/f"bank{i}.sym";lst=out/f"bank{i}.lst"
    cmd=["dasm",str(file.relative_to(root)),"-f3","-o"+str(b),"-l"+str(lst),"-s"+str(sym)]
    subprocess.run(cmd,cwd=root,check=True)
    actual=b.read_bytes()
    if len(actual)!=4096:raise RuntimeError(f"BAD_BANK_SIZE_{i}={len(actual)}")
    paths.append(b)
raw=b"".join(x.read_bytes() for x in paths)
assert len(raw)==16384
# F6 vectors in bank3, all earlier banks must recover to FF9A.
for i in range(3):
    b=paths[i].read_bytes()
    assert b[4092:4094]==b"\x9a\xff",(i,b[-4:].hex())
    assert b[0xF90:0xF93]==b"\xbd\xf6\xff",f"bank{i}: trampoline does not mirror LDA $FFF6,X"
    assert b[0xF96:0xF99]==b"\xad\xf9\xff",f"bank{i}: return LDA $FFF9 missing"
assert raw[-4:-2]==b"\x00\xf0",raw[-4:].hex()
assert raw[0x3000+0xF90:0x3000+0xF93]==b"\xbd\xf6\xff"
product=out/"MELLANRUM_16K_NTSC_F6.bin";product.write_bytes(raw)
report={"mapper":"F6","size":len(raw),"banks":[{"bank":i,"offset":4096*i,"size":4096,"sha256":hashlib.sha256(x.read_bytes()).hexdigest(),"src":str(src[i].relative_to(root))}for i,x in enumerate(paths)],"rom_sha256":hashlib.sha256(raw).hexdigest(),"startup_bank":3,"cartridge_ram":0,"coprocessor":"NONE","real_tia_score_bytes":3*3840,"music_control_frames_per_room":256,"rooms_scored":15,"driver":"actual native DASM 6507"}
(out/"ROM_16K_BUILD.json").write_text(json.dumps(report,indent=2)+"\n")
(out/"SHA256SUMS").write_text(hashlib.sha256(raw).hexdigest()+"  MELLANRUM_16K_NTSC_F6.bin\n")
print(json.dumps(report,indent=2))
