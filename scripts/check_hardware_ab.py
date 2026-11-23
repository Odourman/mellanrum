#!/usr/bin/env python3
"""REAL 6507 compiled instruction execution in a developmental CPU/RIOT model.
The UI/control acceptance cases are replayed at frame boundaries; no Stella claim.
"""
from pathlib import Path
from cpu_trace import load
ROOT=Path(__file__).resolve().parents[1]
ROM=str(ROOT/'build/mellanrum_ntsc.bin');SYM=str(ROOT/'build/mellanrum_ntsc.sym')
def step(c,n=3):c.run_to_frame(c.frames+n,instr_cap=3000000)
def init(swchb=0xff):
 c=load(ROM,SYM);c.input_swchb=swchb;step(c,5)
 assert c.ram('mode')==0
 return c
def start(c,kind,room=None):
 c.input_fire=True;step(c,2)
 assert c.ram('mode')==kind,(kind,c.ram('mode'))
 if room is not None:assert c.ram('room')==room,(kind,room,c.ram('room'))
 c.input_fire=False;step(c,2)
 return c
# True left switch polarity, independent of right switch and title SELECT.
for leftA in [True,False]:
 for rightA in [True,False]:
  sb=(0x3f | (0x40 if leftA else 0) | (0x80 if rightA else 0))
  c=init(sb)
  assert c.read(0x282)==sb
  start(c,1 if leftA else 4,0 if leftA else None)
  if not leftA:assert 10<=c.ram('room')<=13
  # Moving left difficulty or right difficulty while playing cannot change mode.
  c.input_swchb^=0xc0;step(c,5)
  assert c.ram('mode')==(1 if leftA else 4)
  # SELECT room restart must not change mode even if the difficulty moved.
  c.input_swchb&=0xfd;step(c,2)
  assert c.ram('mode')==(1 if leftA else 4)
  c.input_swchb|=2;step(c,1)
  # RESET returns to title; new title FIRE must honor NEW switch setting.
  c.input_swchb&=0xfe;step(c,2)
  assert c.ram('mode')==0
  c.input_swchb|=1;step(c,2)
  start(c,4 if leftA else 1,0 if not leftA else None)
# Title SELECT, all joystick directions, right A/B do not select.
for swcha in [0xef,0xdf,0xbf,0x7f,0x00]:
 c=init(0xff);c.input_swcha=swcha;c.input_swchb=0xfd;step(c,8)
 assert c.ram('mode')==0
 c.input_swchb=0x7f;step(c,3)
 start(c,1,0)
# Title A->B and B->A before FIRE, distinct from in-game latching.
for initial,target in [(0xff,0xbf),(0xbf,0xff)]:
 c=init(initial);c.input_swchb=target;step(c,4)
 start(c,1 if target&0x40 else 4,0 if target&0x40 else None)
# Held FIRE one shot; title must NOT recur, mode stays latched, R01 start once.
for left in [0xff,0xbf]:
 c=init(left);c.input_fire=True;step(c,18)
 assert c.ram('mode')==(1 if left&0x40 else 4)
 assert c.ram('introFrames')>0
 c.input_swchb^=0x40;step(c,18)
 assert c.ram('mode')==(1 if left&0x40 else 4)
print('HARDWARE_AB_CPU_PASS: 4 LEFT/RIGHT combos, title toggles, SELECT, joystick, FIRE one-shot, mode latch, RESET re-latch')
