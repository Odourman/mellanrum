#!/usr/bin/env python3
"""Issue15 candidate raster/per-room ORIGINAL Gopher emulator screenshots.
POKE is used ONLY in a diagnostic test to select 15 source rooms (not gameplay evidence).
Leaves frozen production ROM entirely untouched.
"""
import subprocess,json,hashlib,os,re,sys
from pathlib import Path
base=Path(__file__).resolve().parents[2]
rom=(base/'build/candidate.bin').resolve();emu=(base/'build/gopher/gopher2600').resolve();out=base/'build/issue15_gopher_15';out.mkdir(parents=True,exist_ok=True)
r=json.loads((base/'reference/rooms.json').read_text());cmd=['VERSION','CARTRIDGE HASH','PERIPHERAL LEFT STICK','PANEL SET P0PRO']
def sf(n):cmd.extend(['STEP FRAME']*n)
sf(20);cmd+=['STICK LEFT FIRE'];sf(3);cmd+=['STICK LEFT NOFIRE'];sf(10)
rows=[]
for i,rec in enumerate(r):
    cmd += [f'POKE 0x00b9 {i}','PANEL HOLD SELECT'];sf(3)
    cmd += ['PANEL RELEASE SELECT'];sf(3)
    cmd += ['TV FRAME','PEEK 0x00b8 0x00b9 0x00bc 0x00bd 0x00bf 0x00c0 0x00c1 0x00c2 0x00cc 0x00cd',f'SCREENSHOT {out/("room_%02d.png"%i)}']
    rows.append({'i':i,'id':rec['id'],'sameY':rec['stone'][1]==rec['exit'][1]})
# Four diagnostic feedback states, measured at THE SAME x/y; these are forced
# machine variables, not evidence that each gameplay action reaches the state.
for idx in range(4):
    cmd += ['POKE 0x00cc 5','POKE 0x00cd 3',f'POKE 0x00d5 {20 if idx>0 else 0}',f'POKE 0x00d6 {idx}'];sf(2)
    cmd += ['TV FRAME',f'SCREENSHOT {out/("marker_%02d.png"%idx)}']
# Real frame-indexed joystick cursor movement: move right one cell through ReadInput
cmd += ['POKE 0x00cc 5','POKE 0x00cd 3','POKE 0x00d5 0','POKE 0x00d6 0','STICK LEFT RIGHT'];sf(24)
cmd += ['STICK LEFT NORIGHT','TV FRAME','PEEK 0x00cc 0x00cd',f'SCREENSHOT {out/"marker_real_joystick_right.png"}']
# Second axis: real hardware joystick UP and actual RAM cursor coordinate readout.
cmd += ['POKE 0x00cc 5','POKE 0x00cd 3','STICK LEFT UP'];sf(24)
cmd += ['STICK LEFT NOUP','TV FRAME','PEEK 0x00cc 0x00cd',f'SCREENSHOT {out/"marker_real_joystick_up.png"}']
# Adversarial hardware object overlaps, separate from four feedback snapshots.
for name,x in [('owl',1),('symbol_A',4),('symbol_B',8)]:
    cmd += [f'POKE 0x00cc {x}','POKE 0x00cd 3','POKE 0x00d5 20','POKE 0x00d6 3'];sf(2)
    cmd += ['TV FRAME',f'SCREENSHOT {out/("overlap_"+name+".png")}']
# actIII presence & phase synthetic deterministic visual state, room14
cmd+=['POKE 0x00db 2'];sf(2)
cmd+=['TV FRAME',f'SCREENSHOT {out/"presence_active.png"}']
cmd+=['POKE 0x00db 0'];sf(2)
cmd+=['TV FRAME',f'SCREENSHOT {out/"presence_off.png"}']
# A diagnostic phase toggle does not change room geometry; it uses existing game palette rules.
cmd += ['POKE 0x00c4 1'];sf(2)
cmd += ['TV FRAME',f'SCREENSHOT {out/"phase1.png"}']
cmd += ['POKE 0x00c4 0'];sf(2)
cmd += ['TV FRAME',f'SCREENSHOT {out/"phase0.png"}']
cmd+=['QUIT']
(out/'replay.txt').write_text('\n'.join(cmd)+'\n')
with (out/'stdout.log').open('w') as f:proc=subprocess.run([str(emu),'HEADLESS',str(rom)],input='\n'.join(cmd)+'\n',stdout=f,stderr=subprocess.STDOUT,text=True,timeout=180)
log=(out/'stdout.log').read_text(errors='replace')
found=re.findall(r'top: (\d+), bottom: (\d+), total: (\d+)',log)
print(json.dumps({'returncode':proc.returncode,'totalFrames':len(found),'scanlines':sorted(set(int(x[2]) for x in found)),'screenshotCount':len(list(out.glob('*.png'))),'sha':hashlib.sha256(rom.read_bytes()).hexdigest()}))
(out/'metadata.json').write_text(json.dumps({'rom_sha':hashlib.sha256(rom.read_bytes()).hexdigest(),'emulator':'Gopher2600 unreleased pinned','status':'DIAGNOSTIC_FORCED_ROOM_SELECT_NOT_REAL_PLAYTHROUGH','room_geometry':rows,'scanline_counts':{k:sum(x[2]==k for x in found) for _,_,k in found}},indent=2)+'\n')
if proc.returncode or len(list(out.glob('room_*.png')))!=15:sys.exit(1)
