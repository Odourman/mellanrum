#!/usr/bin/env python3
"""REAL Stella/libretro controller-only campaign. RAM is sampled READ-ONLY."""
import argparse,hashlib,json,pathlib,re,time
from issue21_libretro_stella_capture import Core,mapping_for,COMMIT,ROM_SHA
READ_NAMES=["mode","room","act","geom","owlX","owlY","owlDir","stoneX","stoneY","exitX","exitY","polarity","phase","phaseAge","beat","beatFrames","introFrames","waitFrames","codaLo","codaHi","cursorX","cursorY","moveDir","moveWait","prevFire","prevSelect","pending","pendingKey","usedFire","slot0Key","slot0Due","slot1Key","slot1Due","presence","presenceEnd","intercepted"]
def symbols(path):
 t=pathlib.Path(path).read_text();d={}
 for n,h in re.findall(r"(?m)^([A-Za-z]\w*)\s*=\s*\$([0-9A-Fa-f]+)\s*$",t):d[n]=int(h,16)
 for n,h in re.findall(r"(?m)^([A-Za-z]\w*)\s+([0-9A-Fa-f]{4})\s+\(",t):d[n]=int(h,16)
 for n in READ_NAMES+["mapRows","pfbuf"]:
  if n not in d:raise RuntimeError("missing_native_symbol: "+n)
  if not 0x80<=d[n]<0x100:raise RuntimeError("not_real_128B_ram: "+n)
 return d
def read_state(core,syms):
 b=core.memory()
 if not b or len(b)!=128:raise RuntimeError("REAL_STELLA_RAM_NOT_AVAILABLE")
 d={n:b[syms[n]-0x80] for n in READ_NAMES}
 d["mapRows"]=b[syms["mapRows"]-0x80:syms["mapRows"]-0x80+8].hex()
 d["pfbuf_sha256"]=hashlib.sha256(b[syms["pfbuf"]-0x80:syms["pfbuf"]-0x80+48]).hexdigest()
 return d
def action_xy(action,s):
 typ,k=action
 if typ=="stone":return (s["stoneX"],s["stoneY"])
 if typ=="tree":
  x=k%5;y=k//5
  return (x,y) if abs(s["cursorX"]-x)<=abs(s["cursorX"]-(9-x)) else (9-x,y)
 return None
def next_target(actions,s):
 for tick in range(s["beat"],len(actions)):
  typ,k=actions[tick]
  if typ=="wait":continue
  if tick==s["beat"] and (s["pending"] or s["usedFire"]):continue
  return (tick,action_xy((typ,k),s),typ)
 return None
def run(a):
 out=pathlib.Path(a.out);out.mkdir(parents=True,exist_ok=True)
 room_data=json.loads(pathlib.Path(a.rooms).read_text())
 assert len(room_data)==15 and [x["id"] for x in room_data]==[p+"-%02d"%i for p in ("I","II","III") for i in range(1,6)]
 paths=json.loads(pathlib.Path(a.paths).read_text())
 assert len(paths)==15 and all(row["id"]==room["id"] and row["abstract_solver"]=="PASS" for row,room in zip(paths,room_data)), "ISSUE21_MODEL_PATHS_INVALID"
 sol=[[tuple(v) for v in row["abstract_solution"]] for row in paths]
 syms=symbols(a.sym);core=Core(a.core,a.rom,out,a.audio_frames);mapping=mapping_for(core.desc)
 assert mapping["Left"]==6 and mapping["Right"]==7,("JOYPAD_MAPPING_INVALID",mapping)
 for button in ["Left Difficulty A","Left Difficulty B","Right Difficulty A","Right Difficulty B"]:
  assert button in mapping,("DIFFICULTY_MAPPING_UNQUALIFIED",button,mapping)
 replay=json.loads(pathlib.Path(a.replay).read_text())["events"] if a.replay else None
 replay_idx=0;previous=None;previous_state=None;last_buttons=None;start=0
 events=[];timeline=[];screens=[];win=[];fire_tick=set();observed_presence={};unique_edges=set()
 first_coda=None;first_title_end=None;fire_inputs=0
 idle_rooms={}; idle_current=None; idle_age=0; idle_violations=[]
 started=time.monotonic();stop_reason="FRAME_BUDGET";f=-1
 try:
  for f in range(a.frames):
   s=read_state(core,syms);buttons=set()
   if replay is not None:
    while replay_idx+1<len(replay) and f>=replay[replay_idx]["end"]:replay_idx+=1
    row=replay[replay_idx]
    if row["start"]<=f<row["end"]:buttons=set(row["buttons"])
   else:
    if f<4:buttons={"Left Difficulty A"}
    elif s["mode"]==0:
     if f<600:buttons={"Fire"} if 16<=f<18 else set()
    elif s["mode"]==2:
     if s["waitFrames"]==0 and not s["prevFire"]:buttons={"Fire"}
    elif s["mode"] in (1,4) and s["room"]<15:
     i=s["room"]
     # A real controller-reached room is left completely untouched for a fixed
     # 36,000-frame interval; then physical SELECT rewinds this exact room.
     if a.idle_frames and s["mode"]==1 and i not in idle_rooms:
      if idle_current!=i:
       idle_current=i;idle_age=0
      if idle_age<a.idle_frames:
       buttons=set();idle_age+=1
      else:
       idle_rooms[i]={"frames":idle_age,"room":i,"mode":s["mode"],"beat":s["beat"],"classification":"REAL_STELLA_EMPTY_INPUT"}
       buttons={"Select"}
       idle_current=None
     else:
      ng=next_target(sol[i],s)
      if ng:
       tick,target,typ=ng;x,y=s["cursorX"],s["cursorY"]
       if tick==s["beat"] and (x,y)==target and not s["pending"] and not s["usedFire"] and (i,tick) not in fire_tick:
        buttons={"Fire"};fire_tick.add((i,tick));fire_inputs+=1
       elif x!=target[0]:buttons={"Right" if target[0]>x else "Left"}
       elif y!=target[1]:buttons={"Down" if target[1]>y else "Up"}
   if buttons!=last_buttons:
    if last_buttons is not None:events.append({"start":start,"end":f,"buttons":sorted(last_buttons)})
    start=f;last_buttons=buttons
   core.run({mapping[b] for b in buttons},f)
   after=read_state(core,syms)
   if a.idle_frames and idle_current is not None and after["mode"]==2:
    idle_violations.append({"room":idle_current,"frame":f,"actual":after})
    stop_reason="REAL_STELLA_IDLE_AUTOWIN_"+str(idle_current)
    break
   if previous_state is not None:
    unique_edges.add((previous_state["room"],previous_state["mode"],previous_state["beat"],after["room"],after["mode"],after["beat"]))
   relevant_keys=("room","mode","beat","phase","presence","polarity","mapRows","slot0Key","slot0Due","slot1Key","slot1Due","pending","cursorX","cursorY")
   changed=[k for k in relevant_keys if previous_state is None or after[k]!=previous_state[k]]
   special=any(k in changed for k in ("room","mode","beat","phase","presence","mapRows"))
   if changed:
    timeline.append({"frame":f,"controller":sorted(buttons),"changed":changed,"state":after})
   should_snap=previous_state is None or any(k in changed for k in ("room","mode","phase","presence","mapRows"))
   if after["mode"]==3:
    if first_coda is None:first_coda=f
    if (f-first_coda) in (119,239,359,479):should_snap=True
   if should_snap and a.screens:
    name=core.snapshot(f)
    if name:
     new=out/("room%02d_f%07d_mode%d_beat%d_presence%d.png"%(after["room"]+1,f,after["mode"],after["beat"],after["presence"]))
     (out/name).rename(new)
     screens.append({"frame":f,"name":new.name,"room_index":after["room"],"mode":after["mode"],"beat":after["beat"],"presence":after["presence"],"sha256":hashlib.sha256(new.read_bytes()).hexdigest()})
   if after["room"]>=12:
    observed_presence.setdefault(after["room"],set()).add(after["presence"])
   if previous_state and previous_state["mode"]!=2 and after["mode"]==2:win.append({"room_index":after["room"],"frame":f,"state":after})
   if after["mode"]==0 and len(win)==15:
    first_title_end=f;stop_reason="COMPLETE_CODA_AND_TITLE";break
   if after["mode"]==1 and after["room"]<15 and after["room"] in idle_rooms and after["beat"]>len(sol[after["room"]])+24:
    stop_reason="BLOCKED_ROOM_"+str(after["room"]);break
   previous_state=after
  events.append({"start":start,"end":f+1,"buttons":sorted(last_buttons or [])})
 finally:core.close()
 info={"status":"PASS" if stop_reason=="COMPLETE_CODA_AND_TITLE" and [x["room_index"] for x in win]==list(range(15)) else "INCONCLUSIVE",
       "case":"controller_only_full_15_room_campaign","evidence_class":"REAL_6507_TIA_INPUT_FRAME_EXACT_READ_ONLY_RAM","production_commit":COMMIT,"rom_sha256":ROM_SHA,"core":core.info,"emulated_frames":f+1,"start_mode":"LEFT_DIFFICULTY_A","win_rooms":[x["room_index"] for x in win],"win_frames":[x["frame"] for x in win],"full_coda_first_frame":first_coda,"back_to_title_frame":first_title_end,"stop_reason":stop_reason,"frameindexed_input_intervals":len(events),"controller_fire_actions":fire_inputs,"unique_room_mode_beat_edges":len(unique_edges),"presence_by_last_three_rooms":{str(k):sorted(v) for k,v in observed_presence.items()},"video_callbacks":core.counters["video"],"audio_samples":core.counters["audio_samples"],"screen_count":len(screens),"seconds":round(time.monotonic()-started,3),
       "actual_tia_scanline_262":"NOT_RUN","human_audio_quality":"NOT_RUN","idle_frames_per_room":a.idle_frames,"idle_rooms_tested":len(idle_rooms),"idle_violations":idle_violations}
 (out/"controller_frame_events.json").write_text(json.dumps({"commit":COMMIT,"rom_sha256":ROM_SHA,"events":events,"frames":f+1},indent=2))
 (out/"timeline.jsonl").write_text("".join(json.dumps(s)+"\n" for s in timeline))
 (out/"screenshot_index.json").write_text(json.dumps(screens,indent=2))
 (out/"result.json").write_text(json.dumps(info,indent=2))
 print("FULL_CAMPAIGN_RESULT",json.dumps(info),flush=True)
 (out/"real_idle_results.json").write_text(json.dumps({"rooms":idle_rooms,"violations":idle_violations,"required_rooms":15,"frames_per_room":a.idle_frames,"status":"PASS" if len(idle_rooms)==15 and not idle_violations else "FAIL","classification":"REAL_STELLA_CONTROLLER_REACHED_600_SEC_EMPTY_INPUT"},indent=2)+"\n")
 if a.idle_frames and (len(idle_rooms)!=15 or idle_violations): info["status"]="FAIL"
 if info["status"]!="PASS":raise SystemExit(4)
def main():
 p=argparse.ArgumentParser()
 for name in ("core","rom","sym","rooms","paths","out"):p.add_argument("--"+name,required=True)
 p.add_argument("--replay");p.add_argument("--idle-frames",type=int,default=36000);p.add_argument("--frames",type=int,default=600000);p.add_argument("--audio-frames",type=int,default=0);p.add_argument("--screens",action="store_true")
 run(p.parse_args())
if __name__=="__main__":main()
