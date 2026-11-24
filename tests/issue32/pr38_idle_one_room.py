#!/usr/bin/env python3
"""Exactly one 600s idle test in actual libretro Stella, controller-reached room.
READ-ONLY RIOT snapshots and real emulator serialization, never RAM writes."""
import argparse,ctypes as C,hashlib,json,pathlib,sys,time
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]/'issue15'))
from libretro_stella_capture import Core,mapping_for,VIDEO,AUDIO,BATCH
p=argparse.ArgumentParser()
for name in ('core','rom','events','out'):p.add_argument('--'+name,required=True)
p.add_argument('--room',type=int,required=True)
a=p.parse_args()
assert 0<=a.room<15
out=pathlib.Path(a.out);out.mkdir(parents=True,exist_ok=True)
rom=pathlib.Path(a.rom);rb=rom.read_bytes()
sha=hashlib.sha256(rb).hexdigest()
trace=json.loads(pathlib.Path(a.events).read_text())
assert len(rb)==16384 and trace['rom_sha256']==sha,(sha,trace.get('rom_sha256'))
core=Core(a.core,str(rom),str(out),0);mp=mapping_for(core.desc)
@VIDEO
def video(ptr,w,h,pitch):core.counters['video']+=1
@AUDIO
def audio(l,r):core.counters['audio_samples']+=1
@BATCH
def batch(ptr,n):core.counters['audio_samples']+=n;return n
core.refs.extend([video,audio,batch])
core.lib.retro_set_video_refresh(video)
core.lib.retro_set_audio_sample(audio)
core.lib.retro_set_audio_sample_batch(batch)
core.lib.retro_serialize_size.argtypes=[];core.lib.retro_serialize_size.restype=C.c_size_t
core.lib.retro_serialize.argtypes=[C.c_void_p,C.c_size_t];core.lib.retro_serialize.restype=C.c_bool
core.lib.retro_unserialize.argtypes=[C.c_void_p,C.c_size_t];core.lib.retro_unserialize.restype=C.c_bool
n=core.lib.retro_serialize_size();assert 0<n<1024*1024,n
buf=C.create_string_buffer(n)
events=trace['events'];idx=0;capture_frame=None;state=None;before=time.monotonic()
for f in range(20000):
 while idx+1<len(events) and f>=events[idx]['end']:idx+=1
 event=events[idx];buttons=event['buttons'] if event['start']<=f<event['end'] else []
 core.run({mp[x] for x in buttons},f)
 raw=core.memory();assert raw and len(raw)>=128
 if raw[0x38]==1 and raw[0x39]==a.room:
  assert core.lib.retro_serialize(buf,n)
  state=bytes(buf.raw);capture_frame=f;break
assert state is not None,(a.room,'CONTROLLER_REACHED_ROOM_NOT_FOUND')
assert core.lib.retro_unserialize(C.create_string_buffer(state),n)
unexpected=None
for step in range(36000):
 core.run(set(),step)
 if step%4==0:
  raw=core.memory()
  if raw[0x38]!=1 or raw[0x39]!=a.room:
   unexpected={'frame':step,'mode':raw[0x38],'room':raw[0x39]};break
result={'status':'PASS' if unexpected is None else 'FAIL',
 'evidence':'REAL_STELLA_CONTROLLER_REACHED_SAVESTATE_36000_FRAMES_NO_INPUT',
 'rom_sha256':sha,'stella_core_sha256':hashlib.sha256(pathlib.Path(a.core).read_bytes()).hexdigest(),
 'room':a.room+1,'controller_reached_frame':capture_frame,
 'savestate_sha256':hashlib.sha256(state).hexdigest(),
 'idle_frames':36000,'sample_every_frames':4,
 'unexpected_mode_change':unexpected,'wall_seconds':round(time.monotonic()-before,2)}
(out/'result.json').write_text(json.dumps(result,indent=2)+'\n')
print('PR38_REAL_STELLA_IDLE',json.dumps(result),flush=True)
core.close()
if result['status']!='PASS':raise SystemExit(2)
