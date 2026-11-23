#!/usr/bin/env python3
"""Native Gopher per-frame TV total across title, FIRE, room, SELECT, RESET (no POKE)."""
from pathlib import Path
import subprocess,json,re,collections,hashlib
base=Path(__file__).resolve().parents[2];rom=(base/'build/candidate.bin').resolve();emu=(base/'build/gopher/gopher2600').resolve();out=base/'build/issue15_raster_transitions';out.mkdir(exist_ok=True)
cmd=['PERIPHERAL LEFT STICK','PANEL SET P0PRO'];events={40:['STICK LEFT FIRE'],44:['STICK LEFT NOFIRE'],100:['PANEL HOLD SELECT'],104:['PANEL RELEASE SELECT'],180:['PANEL HOLD RESET'],184:['PANEL RELEASE RESET'],220:['STICK LEFT FIRE'],224:['STICK LEFT NOFIRE']}
for i in range(300):
 cmd.extend(events.get(i,[]));cmd.extend(['STEP FRAME','TV FRAME']);
 if i in (39,45,95,105,179,189,225,299):cmd.extend(['PEEK 0x00b8 0x00b9 0x00cc 0x00cd'])
cmd.append('QUIT');(out/'commands.txt').write_text('\n'.join(cmd)+'\n')
with (out/'stdout.log').open('w') as f:r=subprocess.run([str(emu),'HEADLESS',str(rom)],input='\n'.join(cmd)+'\n',text=True,stdout=f,stderr=subprocess.STDOUT,timeout=160)
s=(out/'stdout.log').read_text(errors='replace');lines=[int(v) for v in re.findall(r'total:\s*(\d+)',s)];nonboot=lines[1:];count=dict(collections.Counter(nonboot));res={'status':'PASS' if r.returncode==0 and len(lines)==300 and count=={262:299} else 'FAIL','count':len(lines),'nonboot_histogram':count,'boot_scanlines':lines[0] if lines else None,'frame_events':events,'native_rom_sha':hashlib.sha256(rom.read_bytes()).hexdigest(),'method':'Gopher2600 real TV FRAME every frame; no POKE'};(out/'result.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps({k:v for k,v in res.items() if k!='frame_events'}))
