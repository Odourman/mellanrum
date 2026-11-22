#!/usr/bin/env python3
"""Native Gopher diagnostic snapshots: M0 widths, true joystick 2D and PF Presence.
POKE-based feedback images are hardware feasibility evidence, not ordinary game actions.
"""
from pathlib import Path
from PIL import Image,ImageChops
import json,re,sys
base=Path(__file__).resolve().parents[1];out=base/'build/gopher_15'
widths=[]
for i in range(4):
 im=Image.open(out/f'marker_{i:02d}.png').convert('RGB')
 xs=[x for x in range(530,630) if any(im.getpixel((x,y))==(6,6,6) for y in range(280,345))]
 widths.append(max(xs)-min(xs)+1 if xs else 0)
assert widths==[7,13,26,52],('marker widths',widths)
raw=(out/'stdout.log').read_text(errors='replace')
xs=[int(s,16) for s in re.findall(r'0x00cc (?:\([^)]*\) )?\(RAM\) = 0x([0-9a-fA-F]{2})',raw)]
ys=[int(s,16) for s in re.findall(r'0x00cd (?:\([^)]*\) )?\(RAM\) = 0x([0-9a-fA-F]{2})',raw)]
assert xs[-2:]==[8,5],xs[-2:]
assert ys[-2:]==[3,0],ys[-2:]
def changed(a,b):
 im=ImageChops.difference(Image.open(out/a).convert('RGB'),Image.open(out/b).convert('RGB'))
 return sum(1 for rgb in im.getdata() if rgb!=(0,0,0))
pres=changed('presence_active.png','presence_off.png');phase=changed('phase0.png','phase1.png')
assert pres>1000 and phase>1000,(pres,phase)
res={'test':'GOPHER_REAL_DIAG_M0_CURSOR_AND_PF_EFFECTS','status':'PASS','hardware_M0_width_pixels':widths,'real_joystick_RIGHT_24_frames_x':xs[-2],'real_joystick_UP_24_frames_y':ys[-1],'presence_on_off_changed_screen_pixels':pres,'phase0_phase1_changed_screen_pixels':phase,'scope':'M0 feedback forced via RAM in disposable diagnostics; ordinary gameplay status transitions are NOT independently verified'}
(out/'marker_presence_audit.json').write_text(json.dumps(res,indent=2)+'\n')
print(json.dumps(res))
