#!/usr/bin/env python3
"""Instruction-cycle sanity under several timing states (NOT a certified TIA test)."""
from cpu_trace import load
from check_rom_vs_model import call
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

counts=[]
for i in range(15):
 c=load(str(ROOT/'build/mellanrum_ntsc.bin'),str(ROOT/'build/mellanrum_ntsc.sym'))
 c.pc=c.syms['Frame'];c.sp=255;c.write(c.syms['room'],i);c.write(c.syms['mode'],1)
 call(c,'LoadRoom')
 c.write(c.syms['introFrames'],1)
 c.write(c.syms['beatFrames'],1)
 c.input_swcha=0xef
 c.input_fire=True
 c.run_to_frame(65,instr_cap=5000000)
 lengths=[n for n,_,_ in c.frame_samples][1:]
 if any(n!=19988 for n in lengths):
  print('FRAME_MISMATCH',i,sorted(set(lengths)),[(j,n) for j,n in enumerate(lengths) if n!=19988][:10]);raise SystemExit(1)
 counts.append((i,len(lengths),c.max_stack,c.wsync_missed,c.ram('beat')))
print('FRAME_BUDGET_MODEL_263_EXPECTED_VS_REAL_GOPHER262: 15 rooms x 64 sampled frames, model only; samples',sum(i[1] for i in counts),'lowest_sp',hex(min(i[2] for i in counts)))
print('CAVEAT: custom CPU/RIOT/WSYNC model has +1 scanline systematic bias vs actual native Gopher; native 262 measured separately; not a native 263 violation.')
