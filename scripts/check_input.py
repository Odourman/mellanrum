#!/usr/bin/env python3
"""Joystick/console-switch frame semantics on real ROM instructions in developmental CPU model."""
from cpu_trace import load
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
rom=str(ROOT/'build/mellanrum_ntsc.bin');sym=str(ROOT/'build/mellanrum_ntsc.sym')
def progress(c,n):c.run_to_frame(c.frames+n,instr_cap=3000000)
def reset():
 c=load(rom,sym);progress(c,5);assert c.ram('mode')==0;return c
c=reset(); c.input_swchb=0xbd;progress(c,4);assert c.ram('mode')==0, 'SELECT changed mode on title'
progress(c,4);assert c.ram('mode')==0, 'held SELECT changed mode on title'
c.input_swchb=0xbf;progress(c,3);c.input_fire=True;progress(c,4)
assert c.ram('mode')==4,('FRI SKOG missing',c.ram('mode'))
assert 10<=c.ram('room')<=13, 'deterministically seeded original Act III room missing'
c.input_fire=False;progress(c,3)
start=(c.ram('cursorX'),c.ram('cursorY'));c.input_swcha=0xf7 # right on bit7? actually $80 => 0x7f
c.input_swcha=0x7f; progress(c,1); assert c.ram('cursorX')==min(start[0]+1,9),(start,c.ram('cursorX'))
progress(c,13);assert c.ram('cursorX')==min(start[0]+2,9),('repeat 200ms',start,c.ram('cursorX'))
c.input_swcha=0xff;progress(c,2)
c.input_swchb=0xfd;progress(c,2);assert c.ram('beat')==0 and c.ram('introFrames')>=106,'SELECT did not restart all room timers'
c.input_swchb=0xfe;progress(c,4);assert c.ram('mode')==0,'RESET did not go to title'
# Campaign, edge-trigger FIRE once per tick and no repeated held fire
c=reset();c.input_fire=True;progress(c,3);assert c.ram('mode')==1 and c.ram('room')==0
c.input_fire=False;progress(c,2)
# Navigate from (1,3) right to editable T at (2,3)
c.input_swcha=0x7f;progress(c,1);c.input_swcha=0xff;progress(c,2)
assert c.ram('cursorX')==2 and c.ram('cursorY')==3
c.input_fire=True;progress(c,2);assert c.ram('pending')==1
progress(c,110);assert c.ram('pending')==0 and c.ram('usedFire')==0
# Held FIRE must not automatically schedule new action
before=c.ram('mapRows')+3;got=c.read(before)
progress(c,90); assert c.read(before)==got, 'held fire unexpectedly repeated'
print('INPUT_FRAME_SEMANTICS_PASS: title SELECT no-op, left B FRI seed, FIRE start, joystick repeat, SELECT same-room restart, RESET title, one-shot FIRE')
