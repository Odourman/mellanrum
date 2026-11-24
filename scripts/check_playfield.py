#!/usr/bin/env python3
"""Verify emitted PF register bytes for all source-preserving dynamic tree toggles."""
import pathlib,json,sys
ROOT=pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from check_rom_vs_model import new_room,call
from generate_rom_data import pfpack
rooms=json.loads((ROOT/'reference/rooms.json').read_text())
shape={'#':('1111','0110'),'.':('0000','0000'),'T':('1011','0110'),'t':('0001','0000')}
count=0
for g in range(5):
 state=[list(s) for s in rooms[g]['half_rows']]
 c=new_room(g)
 for y in range(8):
  for x in range(5):
   if state[y][x] not in 'Tt':continue
   c.write(c.syms['workKey'],y*5+x)
   call(c,'ToggleTree')
   state[y][x]=('t' if state[y][x]=='T' else 'T')
   expected=[]
   for row in state:
    for band in (0,1):expected.extend(pfpack(''.join(shape[ch][band] for ch in row)))
   found=list(c.mem[c.syms['pfbuf']:c.syms['pfbuf']+48]);assert found==expected,(g,x,y,[(i,a,b) for i,(a,b) in enumerate(zip(found,expected)) if a!=b])
   count+=1
 print('GEOMETRY',g,'mutable groups',sum(ch in 'Tt' for row in state for ch in row),'PF register bytes checked')
print('DYNAMIC_PLAYFIELD_PASS',count,'edit operations: 48 bytes checked after every operation for five source maps')
