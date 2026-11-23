#!/usr/bin/env python3
"""Frame-exact execution of an actual libretro Stella core, not a CPU model."""
import argparse,ctypes as C,hashlib,json,os,pathlib,random,struct,time,wave,zlib
# Issue #21: exact new candidate is supplied by CI and logged with evidence.
# Never silently relabel the immutable PR #16 hash as the new candidate.
COMMIT=os.environ.get("GITHUB_SHA","SOURCE_SHA_NOT_PROVIDED")
ROM_SHA=os.environ.get("MELLANRUM_ROM_SHA","HASH_NOT_PROVIDED")
class Info(C.Structure):
 _fields_=[("library_name",C.c_char_p),("library_version",C.c_char_p),("valid_extensions",C.c_char_p),("need_fullpath",C.c_bool),("block_extract",C.c_bool)]
class Geometry(C.Structure):
 _fields_=[("base_width",C.c_uint),("base_height",C.c_uint),("max_width",C.c_uint),("max_height",C.c_uint),("aspect_ratio",C.c_float)]
class Timing(C.Structure):
 _fields_=[("fps",C.c_double),("sample_rate",C.c_double)]
class AV(C.Structure):
 _fields_=[("geometry",Geometry),("timing",Timing)]
class Game(C.Structure):
 _fields_=[("path",C.c_char_p),("data",C.c_void_p),("size",C.c_size_t),("meta",C.c_char_p)]
class Descriptor(C.Structure):
 _fields_=[("port",C.c_uint),("device",C.c_uint),("index",C.c_uint),("id",C.c_uint),("description",C.c_char_p)]
ENV=C.CFUNCTYPE(C.c_bool,C.c_uint,C.c_void_p)
VIDEO=C.CFUNCTYPE(None,C.c_void_p,C.c_uint,C.c_uint,C.c_size_t)
AUDIO=C.CFUNCTYPE(None,C.c_int16,C.c_int16)
BATCH=C.CFUNCTYPE(C.c_size_t,C.POINTER(C.c_int16),C.c_size_t)
POLL=C.CFUNCTYPE(None)
INPUT=C.CFUNCTYPE(C.c_int16,C.c_uint,C.c_uint,C.c_uint,C.c_uint)
def write_png(file,w,h,pitch,pixels,fmt):
 raw=bytearray()
 for y in range(h):
  raw.append(0);row=pixels[y*pitch:(y+1)*pitch]
  if fmt==1:raw.extend(b"".join(bytes((row[i+2],row[i+1],row[i])) for i in range(0,w*4,4)))
  else:
   for v in struct.unpack_from("<"+str(w)+"H",row):
    if fmt==2:r,g,b=((v>>11)&31)*255//31,((v>>5)&63)*255//63,(v&31)*255//31
    else:r,g,b=((v>>10)&31)*255//31,((v>>5)&31)*255//31,(v&31)*255//31
    raw.extend((r,g,b))
 def ck(k,v):return struct.pack(">I",len(v))+k+v+struct.pack(">I",zlib.crc32(k+v)&0xffffffff)
 pathlib.Path(file).write_bytes(b"\x89PNG\r\n\x1a\n"+ck(b"IHDR",struct.pack(">IIBBBBB",w,h,8,2,0,0,0))+ck(b"IDAT",zlib.compress(raw,6))+ck(b"IEND",b""))
class Core:
 def __init__(self,so,rom,out,audio_frames):
  self.lib=C.CDLL(so);self.out=pathlib.Path(out);self.pixels=None;self.width=0;self.height=0;self.pitch=0;self.pixfmt=0
  self.pressed=set();self.desc=[];self.counters={"video":0,"audio_samples":0,"input_polls":0};self.frame=0;self.audio_frames=audio_frames
  for n,args,ret in [("retro_set_environment",[ENV],None),("retro_set_video_refresh",[VIDEO],None),("retro_set_audio_sample",[AUDIO],None),("retro_set_audio_sample_batch",[BATCH],None),("retro_set_input_poll",[POLL],None),("retro_set_input_state",[INPUT],None),("retro_init",[],None),("retro_deinit",[],None),("retro_get_system_info",[C.POINTER(Info)],None),("retro_get_system_av_info",[C.POINTER(AV)],None),("retro_load_game",[C.POINTER(Game)],C.c_bool),("retro_unload_game",[],None),("retro_run",[],None),("retro_set_controller_port_device",[C.c_uint,C.c_uint],None),("retro_get_memory_data",[C.c_uint],C.c_void_p),("retro_get_memory_size",[C.c_uint],C.c_size_t)]:
   f=getattr(self.lib,n);f.argtypes=args;f.restype=ret
  self.sd=C.create_string_buffer(os.fsencode(str(self.out.resolve())))
  @ENV
  def env(cmd,p):
   if cmd==10:self.pixfmt=C.cast(p,C.POINTER(C.c_int))[0];return True
   if cmd==3:C.cast(p,C.POINTER(C.c_bool))[0]=True;return True
   if cmd==11:
    d=C.cast(p,C.POINTER(Descriptor))
    for i in range(128):
     row=d[i]
     if not row.description:break
     self.desc.append({"port":row.port,"device":row.device,"id":row.id,"name":row.description.decode("utf-8","replace")})
    return True
   if cmd in (9,30,31):C.cast(p,C.POINTER(C.c_char_p))[0]=C.cast(self.sd,C.c_char_p);return True
   if cmd==39:C.cast(p,C.POINTER(C.c_uint))[0]=0;return True
   if cmd==17:C.cast(p,C.POINTER(C.c_bool))[0]=False;return True
   return False
  @VIDEO
  def video(ptr,w,h,pitch):
   self.counters["video"]+=1
   if ptr:self.width=w;self.height=h;self.pitch=pitch;self.pixels=C.string_at(ptr,pitch*h)
  @AUDIO
  def audio(l,r):
   self.counters["audio_samples"]+=1
   if self.wav and self.frame<self.audio_frames:self.wav.writeframesraw(struct.pack("<hh",l,r))
  @BATCH
  def batch(ptr,n):
   self.counters["audio_samples"]+=n
   if self.wav and self.frame<self.audio_frames:self.wav.writeframesraw(C.string_at(ptr,n*4))
   return n
  @POLL
  def poll():self.counters["input_polls"]+=1
  @INPUT
  def inp(port,device,index,id):return int(port==0 and device==1 and index==0 and id in self.pressed)
  self.refs=[env,video,audio,batch,poll,inp]
  self.lib.retro_set_environment(env);self.lib.retro_set_video_refresh(video);self.lib.retro_set_audio_sample(audio);self.lib.retro_set_audio_sample_batch(batch);self.lib.retro_set_input_poll(poll);self.lib.retro_set_input_state(inp)
  self.lib.retro_init();inf=Info();self.lib.retro_get_system_info(C.byref(inf))
  self.info={"name":inf.library_name.decode() if inf.library_name else "", "version":inf.library_version.decode() if inf.library_version else "","core_sha256":hashlib.sha256(pathlib.Path(so).read_bytes()).hexdigest(),"need_fullpath":bool(inf.need_fullpath)}
  self.lib.retro_set_controller_port_device(0,1)
  self.rombytes=pathlib.Path(rom).read_bytes();self.buf=C.create_string_buffer(self.rombytes);self.game=Game(os.fsencode(os.path.abspath(rom)),C.cast(self.buf,C.c_void_p),len(self.rombytes),None)
  if not self.lib.retro_load_game(C.byref(self.game)):raise RuntimeError("LIBRETRO_ROM_LOAD_FAILED")
  av=AV();self.lib.retro_get_system_av_info(C.byref(av))
  self.info.update({"fps":av.timing.fps,"sample_rate":av.timing.sample_rate,"geometry":[av.geometry.base_width,av.geometry.base_height],"pixel_format":self.pixfmt,"rom_sha256":hashlib.sha256(self.rombytes).hexdigest(),"reported_ram_bytes":self.lib.retro_get_memory_size(2)})
  self.wav=wave.open(str(self.out/"tia_audio.wav"),"wb") if audio_frames else None
  if self.wav:self.wav.setnchannels(2);self.wav.setsampwidth(2);self.wav.setframerate(round(av.timing.sample_rate))
 def memory(self):
  sz=self.lib.retro_get_memory_size(2);p=self.lib.retro_get_memory_data(2)
  return C.string_at(p,min(sz,8192)) if p and sz else None
 def run(self,buttons,frame):
  self.pressed=set(buttons);self.frame=frame;self.lib.retro_run()
 def snapshot(self,frame):
  if self.pixels is None:return None
  file=self.out/("frame_%07d.png"%frame);write_png(file,self.width,self.height,self.pitch,self.pixels,self.pixfmt);return file.name
 def close(self):
  if self.wav:self.wav.close()
  self.lib.retro_unload_game();self.lib.retro_deinit()
def mapping_for(desc):
 m={"Fire":0,"Select":2,"Reset":3,"Up":4,"Down":5,"Left":6,"Right":7}
 for d in desc:
  if d["port"]!=0 or d["device"]!=1:continue
  s=d["name"].lower().strip()
  for name in ["Fire","Select","Reset","Up","Down","Left","Right","Left Difficulty A","Left Difficulty B","Right Difficulty A","Right Difficulty B","Color","Black/White"]:
   if s==name.lower():m[name]=d["id"]
 return m
def policy(profile,frame,seed,left):
 if frame<3:return {"Left Difficulty "+left}
 if 18<=frame<21:return {"Fire"}
 if frame<142:return set()
 n=frame-142;r=random.Random((seed+47)*1000003+(n//13)*961748941)
 if profile=="IDLE":return set()
 if profile=="CLOG":return {"Fire"} if n%17<13 else {"Right"} if n%17==13 else set()
 if profile=="TILT_FIRE":return {"Fire"} if n%11==0 else {["Up","Down","Left","Right"][n//16%4]} if n%11<5 else set()
 if profile=="TILT_STONE":return {"Right"} if n%31<9 else {"Down"} if n%31<18 else {"Fire"} if n%31==18 else set()
 if profile=="BOG":return {"Fire","Right"} if n%73 in (0,1) else {"Up","Fire"} if n%73==2 else {"Left","Down"} if n%73 in (17,18) else set()
 if n%41==0:return {"Fire"}
 if n%19<8:return {r.choice(["Up","Down","Left","Right"])}
 return set()
def main():
 p=argparse.ArgumentParser()
 for name in ("core","rom","out"):p.add_argument("--"+name,required=True)
 p.add_argument("--frames",type=int,default=480);p.add_argument("--seed",type=int,default=2600);p.add_argument("--profile",default="RAIN");p.add_argument("--left",choices=["A","B"],default="A");p.add_argument("--snap-every",type=int,default=120);p.add_argument("--audio-frames",type=int,default=480);p.add_argument("--sample-every",type=int,default=30);p.add_argument("--replay")
 a=p.parse_args();out=pathlib.Path(a.out);out.mkdir(parents=True,exist_ok=True)
 data=pathlib.Path(a.rom).read_bytes();assert len(data)==4096 and hashlib.sha256(data).hexdigest()==ROM_SHA,"FROZEN_SHA_MISMATCH"
 core=Core(a.core,a.rom,out,a.audio_frames);m=mapping_for(core.desc)
 print("QUALIFIED_CORE",json.dumps(core.info),"DESCRIPTORS",json.dumps(core.desc),"MAPPING",json.dumps(m),flush=True)
 playback=json.loads(pathlib.Path(a.replay).read_text()).get("events") if a.replay else None
 samples=[];events=[];screens=[];ram_samples=[];current=None;begin=0;start=time.monotonic()
 for f in range(a.frames):
  names=next((set(e["buttons"]) for e in playback if e["start"]<=f<e["end"]),set()) if playback else policy(a.profile,f,a.seed,a.left)
  ids={m[b] for b in names if b in m}
  if names!=current:
   if current is not None:events.append({"start":begin,"end":f,"buttons":sorted(current)})
   begin=f;current=set(names)
  core.run(ids,f)
  if f in (0,16,19,25,140) or (a.snap_every and f%a.snap_every==a.snap_every-1) or f==a.frames-1:
   fn=core.snapshot(f)
   if fn:screens.append({"frame":f,"file":fn,"sha256":hashlib.sha256((out/fn).read_bytes()).hexdigest()})
  if f in (0,20,142) or (a.sample_every and f%a.sample_every==0) or f==a.frames-1:
   ram=core.memory()
   samples.append({"frame":f,"framebuffer_sha256":hashlib.sha256(core.pixels).hexdigest() if core.pixels else None,"video_calls":core.counters["video"],"audio_samples":core.counters["audio_samples"],"ram_sha256":hashlib.sha256(ram).hexdigest() if ram else None})
   if ram:ram_samples.append({"frame":f,"raw_ram_hex":ram.hex()})
 events.append({"start":begin,"end":a.frames,"buttons":sorted(current) if current else []})
 core.close()
 (out/"controller_frame_events.json").write_text(json.dumps({"commit":COMMIT,"rom_sha256":ROM_SHA,"profile":a.profile,"left":a.left,"seed":a.seed,"frames":a.frames,"events":events},indent=2))
 (out/"frame_samples.jsonl").write_text("".join(json.dumps(d)+"\n" for d in samples))
 if ram_samples:(out/"read_only_ram.jsonl").write_text("".join(json.dumps(d)+"\n" for d in ram_samples))
 (out/"input_descriptors.json").write_text(json.dumps({"descriptors":core.desc,"mapping":m},indent=2))
 status="PASS" if core.counters["video"]==a.frames and core.counters["audio_samples"]>0 else "INCONCLUSIVE"
 result={"status":status,"case":"real_libretro_stella_input_frame_execution","evidence_class":"REAL_TIA_6507_FRAME_INDEXED","gameplay_completion":"INCONCLUSIVE","tia_exact_scanline_audit":"NOT_RUN","commit":COMMIT,"rom_sha256":ROM_SHA,"core":core.info,"input_mapping":m,"profile":a.profile,"left":a.left,"seed":a.seed,"emulated_frames":a.frames,"video_callbacks":core.counters["video"],"audio_samples":core.counters["audio_samples"],"input_polls":core.counters["input_polls"],"screens":screens,"wall_seconds":round(time.monotonic()-start,3)}
 (out/"result.json").write_text(json.dumps(result,indent=2));print("RESULT",json.dumps(result),flush=True)
 if status!="PASS":raise SystemExit(2)
if __name__=="__main__":main()
