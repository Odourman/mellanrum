#!/usr/bin/env python3
"""Native Gopher2600 TIA WAV recording with ONLY HEADLESS -wav CLI flag exposed.
WavWriter and entire TIA/CPU emulator core are unchanged from pinned upstream.
"""
import argparse,hashlib,json,subprocess,sys
from pathlib import Path
SHA='e9ea87d381bcf8da39ec055d7d6951ceff97b21d3a798addd10fbbe540c5e974'
p=argparse.ArgumentParser();p.add_argument('--emulator',required=True);p.add_argument('--rom',required=True);p.add_argument('--out',required=True);args=p.parse_args()
em=Path(args.emulator).resolve();rom=Path(args.rom).resolve();out=Path(args.out).resolve();out.mkdir(parents=True,exist_ok=True)
assert hashlib.sha256(rom.read_bytes()).hexdigest()==SHA
for kind in ('CAMPAIGN','FRI_SKOG','TITLE_IDLE'):
    d=out/kind;d.mkdir(parents=True,exist_ok=True)
    if kind=='CAMPAIGN':
        proc=subprocess.run([sys.executable,str(Path(__file__).resolve().parent/'campaign_attempt.py'),'--generate-only','--emulator',str(em),'--rom',str(rom),'--rooms',str(Path('reference/rooms.json').resolve()),'--out',str(d)],capture_output=True,text=True,timeout=30)
        assert proc.returncode==0,proc.stdout+proc.stderr
        commands=(d/'commands.txt').read_text()
    else:
        seq=['VERSION','CARTRIDGE HASH','PERIPHERAL LEFT STICK','PANEL SET P0AM' if kind=='FRI_SKOG' else 'PANEL SET P0PRO','PANEL SET P1PRO']
        for i in range(30):seq.append('STEP FRAME')
        if kind=='FRI_SKOG':
            seq+=['STICK LEFT FIRE'];seq+=['STEP FRAME']*4;seq+=['STICK LEFT NOFIRE']
        for f in range(1100 if kind=='FRI_SKOG' else 450):
            if kind=='FRI_SKOG' and f%200==0:seq+=['STICK LEFT RIGHT']
            if kind=='FRI_SKOG' and f%200==4:seq+=['STICK LEFT NORIGHT','STICK LEFT FIRE']
            if kind=='FRI_SKOG' and f%200==7:seq+=['STICK LEFT NOFIRE']
            seq+=['STEP FRAME']
            if f%150==0:seq+=['TV FRAME','AUDIO','PEEK 0x00b8 0x00b9 0x00c6 0x00db']
        seq+=['SCREENSHOT '+str(d/'last_frame.png'),'QUIT']
        commands='\n'.join(seq)+'\n';(d/'commands.txt').write_text(commands)
    with (d/'gopher_stdout.log').open('w') as log:
        try:r=subprocess.run([str(em),'HEADLESS','-wav',str(rom)],input=commands,text=True,cwd=d,stdout=log,stderr=subprocess.STDOUT,timeout=660)
        except subprocess.TimeoutExpired:r=None
    wavs=list(d.glob('*.wav'))
    data={'kind':kind,'rom_sha256':SHA,'emulator_exit':r.returncode if r is not None else 'timeout','command_lines':commands.count('\n'),'real_wav_count':len(wavs),'wav_bytes':[x.stat().st_size for x in wavs],'status':'WAV_CAPTURED' if wavs and r is not None and r.returncode==0 else 'INCONCLUSIVE','provenance':'Pinned real Gopher TIA output, CLI-only addition to expose upstream native opts.Wav in HEADLESS'}
    (d/'capture_result.json').write_text(json.dumps(data,indent=2)+'\n');print(json.dumps(data))
