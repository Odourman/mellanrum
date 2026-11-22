#!/usr/bin/env python3
"""REAL Stella libretro seeded test matrix, per-room read-only state and authentic-input-derived savestates."""
import argparse,ctypes as C,hashlib,json,pathlib,random,time,wave
from core_harness import Core,mapping_for,COMMIT,ROM_SHA
from route_driver import read_state,symbols
def authentic_checkpoint(core,prefix,room,syms):
 events=prefix["events"];j=0;previous=None;mapping=mapping_for(core.desc)
 lib=core.lib
 lib.retro_serialize_size.argtypes=[];lib.retro_serialize_size.restype=C.c_size_t
 sz=lib.retro_serialize_size();assert sz>0,("LIBRETRO_SERIALIZATION_UNAVAILABLE",sz)
 lib.retro_serialize.argtypes=[C.c_void_p,C.c_size_t];lib.retro_serialize.restype=C.c_bool
 lib.retro_unserialize.argtypes=[C.c_void_p,C.c_size_t];lib.retro_unserialize.restype=C.c_bool
 for f in range(prefix["frames"]):
  while j+1<len(events) and f>=events[j]["end"]:j+=1
  e=events[j];names=set(e["buttons"]) if e["start"]<=f<e["end"] else set()
  core.run({mapping[x] for x in names},f)
  s=read_state(core,syms)
  if s["mode"]==1 and s["room"]==room and (previous is None or previous["mode"]!=1 or previous["room"]!=room):
   buf=C.create_string_buffer(sz)
   if not lib.retro_serialize(buf,sz):raise RuntimeError("LIBRETRO_SERIALIZE_FAILED")
   return {"frame":f,"data":buf.raw,"source_state":s,"total_prefix_frames":f+1,"size":sz}
  previous=s
 raise RuntimeError("TARGET_ROOM_NOT_REACHED_BY_AUTHENTIC_CONTROLS")
def policy(profile,f,seed,cf=False):
 rng=random.Random((seed+71)*6364136223846793005+(f//11)*1442695040888963407);k=f%61
 if profile=="CLOG":b={"Fire"} if k<18 else {"Right"} if k<27 else {"Left","Fire"} if k==30 else set()
 elif profile=="TILT_FIRE":b={"Fire"} if k in (0,2,7,10,19,27) else {rng.choice(["Up","Down","Left","Right"])} if k%3<2 else set()
 elif profile=="TILT_STONE":b={"Right"} if k<12 else {"Down"} if k<24 else {"Fire"} if k in (24,31) else set()
 elif profile=="BOG":b={"Fire","Right"} if k in (0,1,2) else {"Fire","Up"} if k==3 else {"Left","Down"} if k in (17,18) else {"Fire"} if k%17==0 else set()
 else:b={"Fire"} if k in (0,13,42) else {rng.choice(["Up","Down","Left","Right"])} if k<30 else set()
 if cf and f==237:b={"Fire"} if "Fire" not in b else set()
 return b
def invariants(s):
 fails=[]
 for k,hi in [("mode",4),("room",14),("cursorX",9),("cursorY",7),("owlX",9),("owlY",7),("owlDir",3),("phase",1),("polarity",1),("phaseAge",6)]:
  if not 0<=s[k]<=hi:fails.append({"field":k,"actual":s[k],"limit":hi})
 for k in ("slot0Key","slot1Key"):
  if s[k]!=255 and s[k]>=40:fails.append({"field":k,"actual":s[k],"limit":39})
 if any(v>31 for v in bytes.fromhex(s["mapRows"])):fails.append({"field":"mapRows","actual":s["mapRows"],"expect":"five valid bit positions"})
 return fails
def run_case(core,checkpoint,room,profile,seed,frames,syms,cf=False,snap=False):
 buf=C.create_string_buffer(checkpoint["data"]);assert core.lib.retro_unserialize(buf,len(checkpoint["data"]))
 m=mapping_for(core.desc);init=read_state(core,syms)
 assert init["mode"]==1 and init["room"]==room,("RESTORE_WRONG_ROOM",init)
 last=None;start=0;events=[];trace=[];viol=[];seen=set();edges=set();prev=None;images=[]
 for f in range(frames):
  buttons=policy(profile,f,seed,cf)
  if buttons!=last:
   if last is not None:events.append({"start":start,"end":f,"buttons":sorted(last)})
   start=f;last=buttons
  core.run({m[x] for x in buttons},f)
  s=read_state(core,syms)
  if f%40==0 or prev is None or s["beat"]!=prev["beat"] or s["mode"]!=prev["mode"] or s["presence"]!=prev["presence"]:
   trace.append({"frame":f,"mode":s["mode"],"room":s["room"],"beat":s["beat"],"owl":[s["owlX"],s["owlY"],s["owlDir"]],"cursor":[s["cursorX"],s["cursorY"]],"phase":s["phase"],"polarity":s["polarity"],"presence":s["presence"],"queue":[s["slot0Key"],s["slot0Due"],s["slot1Key"],s["slot1Due"]],"mapRows":s["mapRows"],"pfbuf_sha256":s["pfbuf_sha256"]})
  fail=invariants(s)
  if fail:viol.append({"frame":f,"failures":fail,"state":s});break
  seen.add((s["mode"],s["room"],s["beat"],s["owlX"],s["owlY"],s["owlDir"],s["polarity"],s["phase"],s["slot0Key"],s["slot1Key"],s["mapRows"]))
  if prev:edges.add((prev["mode"],prev["room"],prev["beat"],s["mode"],s["room"],s["beat"]))
  if snap and f in (0,frames//2,frames-1):
   fn=core.snapshot(f)
   if fn:
    dest=core.out/("R%02d_%s_seed%04d_frame%06d.png"%(room+1,profile,seed,f))
    (core.out/fn).rename(dest);images.append(dest.name)
  prev=s
 events.append({"start":start,"end":f+1,"buttons":sorted(last or [])})
 return {"status":"FAIL" if viol else "PASS","scope":"actual_emulator_ram_bounds_and_continuity_only_not_win","evidence_class":"REAL_STELLA_INPUT_FRAME_EXACT_SAVESTATE_REACHED_WITH_REAL_INPUT","room_index":room,"seed":seed,"policy":profile,"counterfactual":cf,"real_emulated_frames":f+1,"source_checkpoint_frame":checkpoint["frame"],"start_mode":init["mode"],"end_mode":s["mode"],"end_room":s["room"],"end_beat":s["beat"],"unique_projected_states":len(seen),"unique_projected_edges":len(edges),"frameindexed_controller_events":events,"sampled_state_trace":trace,"violations":viol,"original_pngs":images,"last_frame_sha256":hashlib.sha256(core.pixels).hexdigest() if core.pixels else None}
def main():
 p=argparse.ArgumentParser()
 for name in ("core","rom","sym","prefix","out"):p.add_argument("--"+name,required=True)
 p.add_argument("--room",type=int,required=True);p.add_argument("--seeds",type=int,default=100);p.add_argument("--frames",type=int,default=900);p.add_argument("--long-frames",type=int,default=10000)
 a=p.parse_args();assert 0<=a.room<15;out=pathlib.Path(a.out);out.mkdir(parents=True,exist_ok=True);syms=symbols(a.sym)
 core=Core(a.core,a.rom,out,0);pref=json.loads(pathlib.Path(a.prefix).read_text())
 cp=authentic_checkpoint(core,pref,a.room,syms)
 (out/"authentic_room_entry_checkpoint.state").write_bytes(cp["data"])
 (out/"checkpoint_provenance.json").write_text(json.dumps({"source_frame":cp["frame"],"actual_state_at_capture":cp["source_state"],"serialized_bytes":cp["size"],"state_sha256":hashlib.sha256(cp["data"]).hexdigest(),"controller_prefix_sha256":hashlib.sha256(pathlib.Path(a.prefix).read_bytes()).hexdigest(),"ROM_SHA":ROM_SHA,"commit":COMMIT,"no_direct_RAM_mutation":True,"libretro_serialize_restoration":True},indent=2))
 started=time.monotonic();cases=[];before_video=core.counters["video"];before_audio=core.counters["audio_samples"]
 for seed in range(a.seeds):
  name=["RAIN","TILT_FIRE","TILT_STONE","CLOG","BOG"][seed%5]
  cases.append(run_case(core,cp,a.room,name,seed,a.frames,syms,snap=seed==0))
  if seed%25==0:print("ROOM",a.room,"SEED",seed,"STATUS",cases[-1]["status"],flush=True)
 long=run_case(core,cp,a.room,"BOG",2600,a.long_frames,syms,snap=True)
 cf0=run_case(core,cp,a.room,"RAIN",999,650,syms)
 cf1=run_case(core,cp,a.room,"RAIN",999,650,syms,cf=True)
 (out/"seeded_cases.jsonl").write_text("".join(json.dumps(x)+"\n" for x in cases))
 (out/"long_case.json").write_text(json.dumps(long,indent=2))
 (out/"counterfactual_pair.json").write_text(json.dumps([cf0,cf1],indent=2))
 # A completed run is proof of testing the declared runtime bounds, not proof of room solution.
 status="PASS" if all(x["status"]=="PASS" for x in cases+[long,cf0,cf1]) else "FAIL"
 result={"status":status,"scope":"runtime bounds on real Stella, NO room-win or scanline acceptance","room_index":a.room,"sessions":len(cases),"real_seeded_frames":sum(x["real_emulated_frames"] for x in cases),"real_long_frames":long["real_emulated_frames"],"real_counterfactual_frames":cf0["real_emulated_frames"]+cf1["real_emulated_frames"],"actual_video_callbacks_including_controller_reached_prefix":core.counters["video"],"actual_audio_samples_including_prefix":core.counters["audio_samples"],"core_sha256":core.info["core_sha256"],"ROM_SHA":ROM_SHA,"commit":COMMIT,"checkpoint_source":"authentic controller-only campaign with no RAM edits; libretro serialized state restored for acceleration","distinct_projection_per_case_not_global_coverage":sum(x["unique_projected_states"] for x in cases),"TIА_SCANLINES":"NOT_RUN","full_game_completion_per_seed":"NOT_CLAIMED","elapsed_wall_seconds":round(time.monotonic()-started,3)}
 (out/"result.json").write_text(json.dumps(result,indent=2));print("SEED_MATRIX",json.dumps(result),flush=True);core.close()
 if status!="PASS":raise SystemExit(5)
if __name__=="__main__":main()
