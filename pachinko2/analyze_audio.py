#!/usr/bin/env python3
"""Objective WAV metrics for genuine Gopher2600 TIA -wav output, not judgement of art."""
import wave,struct,math,json,hashlib,os,sys
from pathlib import Path
root=Path(sys.argv[1] if len(sys.argv)>1 else 'build/pachinko/real-audio').resolve()
rows=[]
for wav in root.rglob('*.wav'):
 d={'file':str(wav.relative_to(root)),'size':wav.stat().st_size,'sha256':hashlib.sha256(wav.read_bytes()).hexdigest(),'classification':'GOPHER2600_NATIVE_TIA_AUDIO_WAV_OUTPUT_GUI_PLATFORM_60HZ_FALLBACK'}
 try:
  with wave.open(str(wav),'rb') as w:
   d.update({'channels':w.getnchannels(),'rate':w.getframerate(),'samples':w.getnframes(),'width':w.getsampwidth(),'seconds':w.getnframes()/w.getframerate()})
   raw=w.readframes(min(w.getnframes(),int(w.getframerate()*60)))
  width=d['width'];count=len(raw)//width
  if width==1: v=[(a-128)/128 for a in raw]
  elif width==2:v=[x/32768 for x in struct.unpack('<'+str(count)+'h',raw)]
  elif width==4:v=[x/2147483648 for x in struct.unpack('<'+str(count)+'i',raw)]
  else:raise RuntimeError(f'unsupported PCM depth {width}')
  d.update({'rms':round(math.sqrt(sum(x*x for x in v)/len(v)),7) if v else 0,'peak':round(max(abs(x) for x in v),7) if v else 0,'clipped_fraction':round(sum(abs(x)>=0.999 for x in v)/len(v),6) if v else 0,'numeric_nonzero':any(x!=0 for x in v),'status':'PASS' if len(v)>10000 and any(x!=0 for x in v) and d['seconds']>2 else 'INCONCLUSIVE'})
 except Exception as e:d.update({'status':'INCONCLUSIVE','error':str(e)})
 rows.append(d)
res={'audio_capture_status':'PASS' if rows and all(x['status']=='PASS' for x in rows) else 'INCONCLUSIVE','real_wavs':len(rows),'tracks':rows,'human_listen_review':'PENDING','artistic_sound_verdict':'NOT_RUN','test_platform':'Pinned Gopher2600 74c544 + GUI refresh fallback only, not changed 6507/TIA core'}
(root/'metrics.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res,indent=2))
