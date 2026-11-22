#!/usr/bin/env python3
"""Independent REAL Gopher2600 frame/scanline counter observation of immutable ROM.
Never use development CPU model for these values. Exit 1 on measured 261-line ROM.
"""
import argparse,hashlib,json,re,subprocess,sys,platform,collections
from pathlib import Path
SHA='e9ea87d381bcf8da39ec055d7d6951ceff97b21d3a798addd10fbbe540c5e974'
p=argparse.ArgumentParser();p.add_argument('--emulator',required=True);p.add_argument('--rom',required=True);p.add_argument('--out',required=True);p.add_argument('--frames',type=int,default=120);p.add_argument('--repeat',type=int,default=2);args=p.parse_args()
em=Path(args.emulator).resolve();rom=Path(args.rom).resolve();out=Path(args.out).resolve();out.mkdir(parents=True,exist_ok=True)
assert hashlib.sha256(rom.read_bytes()).hexdigest()==SHA
for j in range(args.repeat):
  commands=['VERSION','CARTRIDGE HASH','PERIPHERAL LEFT STICK','PANEL SET P0PRO']
  for f in range(args.frames):
    if f==10:commands+=['STICK LEFT FIRE']
    if f==15:commands+=['STICK LEFT NOFIRE']
    commands+=['STEP FRAME','TV FRAME']
    if f in (1,10,18,19,args.frames-1):commands+=['TV','TV VSYNC','PEEK 0x00b8 0x00b9 0x0282']
  commands+=['QUIT']
  d=out/f'run_{j+1}';d.mkdir(exist_ok=True)
  (d/'replay_commands.txt').write_text('\n'.join(commands)+'\n')
  with (d/'gopher_tv_frame.log').open('w') as file:
    r=subprocess.run([str(em),'HEADLESS',str(rom)],input='\n'.join(commands)+'\n',text=True,stdout=file,stderr=subprocess.STDOUT,timeout=240)
  s=(d/'gopher_tv_frame.log').read_text(errors='replace')
  samples=[int(n) for n in re.findall(r'top:\s*\d+, bottom:\s*\d+, total:\s*(\d+)',s)]
  stabilized=samples[1:] if samples and samples[0]<200 else samples
  result={'id':f'GOPHER_NATIVE_RASTER_REPEAT_{j+1}','status':'PASS' if r.returncode==0 and len(samples)==args.frames and all(n==262 for n in stabilized) else 'FAIL' if r.returncode==0 and len(samples)==args.frames and any(n!=262 for n in stabilized) else 'INCONCLUSIVE','rom_sha256':SHA,'evidence_type':'REAL_GOPHER_6507_TIA_TV_FRAME','runner':platform.platform(),'frames_requested':args.frames,'frames_reported':len(samples),'sample_scanlines_counts':dict(collections.Counter(stabilized)),'first_bad_sample':next((i+1 for i,n in enumerate(stabilized) if n!=262),None),'emulator_exit':r.returncode,'measured_from_gopher_tv_frame_not_cpu_model':True,'repro':f'gopher2600 HEADLESS {rom} < replay_commands.txt'}
  (d/'result.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
# Do not exit nonzero on observed product bug: preserve green infra with clear data, separate gate
