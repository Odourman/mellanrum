#!/usr/bin/env python3
"""Qualification only: authentic Gopher2600 HEADLESS 6507/TIA frame stepping.
This does NOT assert full campaign completion or analogue audio acceptance.
"""
import argparse,hashlib,json,platform,subprocess,time,re
from pathlib import Path
EXPECTED='e9ea87d381bcf8da39ec055d7d6951ceff97b21d3a798addd10fbbe540c5e974'
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
p=argparse.ArgumentParser();p.add_argument('--emulator',required=True);p.add_argument('--rom',required=True);p.add_argument('--out',default='build/pachinko/qualification');args=p.parse_args()
rom=Path(args.rom).resolve();em=Path(args.emulator).resolve();out=Path(args.out).resolve();out.mkdir(parents=True,exist_ok=True)
assert len(rom.read_bytes())==4096 and sha(rom)==EXPECTED, 'WRONG FROZEN ROM'
start=time.monotonic();results=[]
for left in ('A','B'):
    steps=[];events=[];frame=0
    def command(c):steps.append(c)
    def advance(n):
        global frame
        for i in range(n):command('STEP FRAME');frame+=1
    def event(c):events.append(dict(frame=frame,cmd=c));command(c)
    command('VERSION');command('CARTRIDGE HASH');command('PERIPHERAL LEFT STICK')
    event('PANEL SET P0PRO' if left=='A' else 'PANEL SET P0AM');event('PANEL SET P1PRO')
    command('TV FRAME');command('RIOT PORTS');command('PEEK 0x00b8 0x00ba 0x0282')
    advance(5)
    command('TV FRAME');command('PEEK 0x00b8 0x00ba 0x0282')
    event('STICK LEFT FIRE');advance(4);event('STICK LEFT NOFIRE');advance(8)
    command('TV FRAME');command('RIOT PORTS');command('PEEK 0x00b8 0x00ba 0x0282');command('AUDIO')
    command('SCREENSHOT '+str(out/('gopher_'+left+'.png')))
    command('QUIT')
    (out/f'commands_{left}.txt').write_text('\n'.join(steps)+'\n')
    with (out/f'events_{left}.jsonl').open('w') as f:
        for e in events:f.write(json.dumps(e)+'\n')
    with (out/f'headless_{left}.log').open('w') as f:
        proc=subprocess.run([str(em),'HEADLESS',str(rom)],input='\n'.join(steps)+'\n',text=True,stdout=f,stderr=subprocess.STDOUT,timeout=150,cwd=str(out))
    log=(out/f'headless_{left}.log').read_text(errors='replace')
    result=dict(test=f'GOPHER_HEADLESS_LEFT_{left}',classification='REAL_6507_TIA_EMULATION_FRAME_STEPPED',requested_frames=frame,emulator=str(em),rom_sha=EXPECTED,tool_exit=proc.returncode,command_count=len(steps),screenshots=[x.name for x in out.glob('gopher_'+left+'*')],log_tail=log[-1400:],duration_wall_seconds=round(time.monotonic()-start,3))
    result['status']='PASS' if proc.returncode==0 and len(result['screenshots'])>0 and 'error in HEADLESS' not in log else 'INCONCLUSIVE'
    results.append(result)
(out/'qualification_results.json').write_text(json.dumps(results,indent=2)+'\n')
for r in results: print(json.dumps({k:v for k,v in r.items() if k!='log_tail'}));print(r['log_tail'][-800:])
if any(r['status']!='PASS' for r in results):raise SystemExit('HEADLESS_QUALIFICATION_INCONCLUSIVE: review real logs and correct interface')
print('FRAME_STEPPED_GOPHER_REAL_EMULATOR_PROBE_PASS; does NOT certify 262-line count without TV parse')
