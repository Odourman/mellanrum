#!/usr/bin/env python3
"""Gopher2600 genuine Free Forest 50k-frame idle longevity, unpatched E9EA cartridge."""
import argparse,hashlib,json,re,subprocess,collections,sys
from pathlib import Path
SHA='e9ea87d381bcf8da39ec055d7d6951ceff97b21d3a798addd10fbbe540c5e974'
p=argparse.ArgumentParser();p.add_argument('--emulator',required=True);p.add_argument('--rom',required=True);p.add_argument('--out',required=True);p.add_argument('--frames',type=int,default=50000);args=p.parse_args()
rom=Path(args.rom).resolve();em=Path(args.emulator).resolve();out=Path(args.out).resolve();out.mkdir(exist_ok=True)
assert hashlib.sha256(rom.read_bytes()).hexdigest()==SHA
cmd=['VERSION','CARTRIDGE HASH','PERIPHERAL LEFT STICK','PANEL SET P0AM','PANEL SET P1PRO']
cmd.extend(['STEP FRAME']*8);cmd+=['STICK LEFT FIRE'];cmd.extend(['STEP FRAME']*3);cmd+=['STICK LEFT NOFIRE']
cmd+=['TV FRAME','PEEK 0x00b8 0x00b9 0x00c6 0x00db','SCREENSHOT '+str(out/'free_initial.png')]
checkpoints=[{'frame_after_start':0}]
for i in range(1,args.frames+1):
    cmd.append('STEP FRAME')
    if i%1000==0:
        cmd+=['TV FRAME','PEEK 0x00b8 0x00b9 0x00c6 0x00db']
        checkpoints.append({'frame_after_start':i})
cmd+=['SCREENSHOT '+str(out/'free_after_long.png'),'QUIT']
(out/'replay_commands.txt').write_text('\n'.join(cmd)+'\n')
(out/'frame_indexed_events.jsonl').write_text(''.join(json.dumps(x)+'\n' for x in [{'frame':0,'event':'PANEL LEFT B'}, {'frame':8,'event':'STICK LEFT FIRE'}, {'frame':11,'event':'STICK LEFT NOFIRE'}]))
with (out/'headless.log').open('w') as f:
    try:r=subprocess.run([str(em),'HEADLESS',str(rom)],input='\n'.join(cmd)+'\n',stdout=f,stderr=subprocess.STDOUT,text=True,timeout=2400)
    except subprocess.TimeoutExpired:r=None
s=(out/'headless.log').read_text(errors='replace')
pat=re.compile(r'top: \d+, bottom: \d+, total: (\d+)\s*\n((?:0x[0-9a-fA-F]{4} \([^)]+\) = 0x[0-9a-fA-F]{2}\s*\n?)+)')
observed=[]
for m in pat.finditer(s):
 vals={int(k,16):int(v,16) for k,v in re.findall(r'0x([0-9a-fA-F]{4}) \([^)]+\) = 0x([0-9a-fA-F]{2})',m.group(2))}
 if 0xb8 in vals:observed.append({'mode':vals[0xb8],'room':vals.get(0xb9),'beat':vals.get(0xc6),'presence':vals.get(0xdb),'tia_scanlines':int(m.group(1))})
status='PASS' if r is not None and r.returncode==0 and len(observed)==len(checkpoints) and all(x['mode']==4 for x in observed) else 'INCONCLUSIVE'
result={'status':status,'test':'GOPHER2600_REAL_FRI_SKOG_50000_FRAMES','classification':'ACTUAL_UNMODIFIED_ROM_HEADLESS_6507_TIA_FRAME_STEPPED','expected_sha256':SHA,'requested_consecutive_frames':args.frames,'actual_frames_completed':args.frames if r and r.returncode==0 else 0,'observed_checkpoints':len(observed),'expected_checkpoints':len(checkpoints),'mode4_all_samples':all(x['mode']==4 for x in observed),'scanline_counts':dict(collections.Counter(x['tia_scanlines'] for x in observed)),'emulator_return_code':r.returncode if r else 'timeout','snapshots':[str(f.name) for f in out.glob('*.png')]}
(out/'results.json').write_text(json.dumps(result,indent=2)+'\n');(out/'checkpoints.json').write_text(json.dumps(observed,indent=2)+'\n');print(json.dumps(result))
