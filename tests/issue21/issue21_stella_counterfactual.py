#!/usr/bin/env python3
"""15 genuine Stella counterfactuals: suppress the actual resonant-tree FIRE.
Each scenario replays the real full original-controller campaign up to its target
room with identical timing. Does not POKE RAM, patch ROM or force room states.
"""
import argparse,bisect,hashlib,json,pathlib,time
from issue21_libretro_stella_capture import Core,mapping_for,ROM_SHA
from issue21_stella_full_campaign import read_state,symbols

def main():
 ap=argparse.ArgumentParser()
 for name in ("rom","sym","core","first","rooms","out"):ap.add_argument("--"+name,required=True)
 ap.add_argument("--after-win-frames",type=int,default=1200)
 a=ap.parse_args();out=pathlib.Path(a.out);out.mkdir(parents=True,exist_ok=True)
 assert hashlib.sha256(pathlib.Path(a.rom).read_bytes()).hexdigest()==ROM_SHA
 original=pathlib.Path(a.first)
 events=json.loads((original/"controller_frame_events.json").read_text())["events"]
 timeline=[json.loads(s) for s in (original/"timeline.jsonl").read_text().splitlines()]
 full=json.loads((original/"result.json").read_text())
 assert full["status"]=="PASS" and full["win_rooms"]==list(range(15)) and full["rom_sha256"]==ROM_SHA
 wins=full["win_frames"]
 rooms=json.loads(pathlib.Path(a.rooms).read_text())
 frames=[t["frame"] for t in timeline]
 sym=symbols(a.sym)
 cases=[]
 for index,room in enumerate(rooms):
  k=room["resonance_gate_key"];x,y=k%5,k//5;matches=[]
  for interval in events:
   start=interval["start"]
   if "Fire" not in interval["buttons"] or start>=wins[index]:continue
   pos=bisect.bisect_right(frames,start-1)-1
   if pos<0:continue
   s=timeline[pos]["state"]
   if s["room"]==index and s["mode"]==1 and s["cursorX"] in (x,9-x) and s["cursorY"]==y:
    matches.append((start,interval["end"],s["beat"]))
  if not matches:
   cases.append({"id":room["id"],"status":"FAIL","reason":"NO_REAL_GATE_FIRE_FOUND"})
   continue
  omit_start,omit_end,beat=matches[-1]
  duration=wins[index]+a.after_win_frames
  trial=out/("room_%02d"%(index+1));trial.mkdir(exist_ok=True)
  em=Core(a.core,a.rom,trial,0); mapping=mapping_for(em.desc)
  evindex=0; observed_target=False; counter_wins=[];screens=[];at_gate=None
  before_gate=None;last=None
  t0=time.monotonic()
  try:
   for f in range(duration):
    while evindex+1<len(events) and f>=events[evindex]["end"]:evindex+=1
    e=events[evindex]
    buttons=set(e["buttons"]) if e["start"]<=f<e["end"] and f<=wins[index] else set()
    if omit_start<=f<omit_end:buttons.discard("Fire")
    em.run({mapping[b] for b in buttons},f)
    s=read_state(em,sym)
    if s["mode"]==1 and s["room"]==index:observed_target=True
    if f==omit_start-1:before_gate={"frame":f,"state":s}
    if f==omit_end+1:at_gate={"frame":f,"state":s}
    if f in (wins[index]-1,wins[index],wins[index]+72):last={"frame":f,"state":s}
    if s["mode"]==2 and s["room"]==index:
     counter_wins.append(f)
     break
    if s["room"]>index:
     counter_wins.append("ROOM_SKIPPED_AT_FRAME_"+str(f))
     break
  finally:
   em.close()
  status="PASS" if observed_target and not counter_wins else "FAIL"
  case={"id":room["id"],"room_index":index,"status":status,
       "classification":"REAL_STELLA_FULL_CONTROLLER_REPLAY_WITH_ONE_RESonance_FIRE_REMOVED_NO_POKE",
       "gate_key":k,"original_win_frame":wins[index],"omitted_fire_start":omit_start,
       "omitted_fire_end":omit_end,"beat_at_fire":beat,"scenario_frames":f+1,
       "target_room_seen":observed_target,"unmodified_original_win_at":wins[index],
       "counterfactual_wins":counter_wins,"pre_fire":before_gate,"post_fire":at_gate,
       "last_checkpoint":last,"core":em.info,
       "elapsed_seconds":round(time.monotonic()-t0,2)}
  cases.append(case)
  print("STELLA_COUNTERFACTUAL",room["id"],status,"omitted_frame",omit_start,
        "target_original_win",wins[index],"counter_wins",counter_wins,flush=True)
  (trial/"result.json").write_text(json.dumps(case,indent=2)+"\n")
 result={"status":"PASS" if len(cases)==15 and all(c["status"]=="PASS" for c in cases) else "FAIL",
         "rom_sha256":ROM_SHA,"emulator_type":"REAL_STELLA_LIBRETRO",
         "counterfactuals":len(cases),"pass":sum(c["status"]=="PASS" for c in cases),
         "description":"Same real controller trace per case, one physically targeted FIRE suppressed. No POKE/injected room states. Replayed to original win+1200 frames.",
         "cases":cases}
 (out/"result.json").write_text(json.dumps(result,indent=2)+"\n")
 print("COUNTERFACTUAL_SUMMARY",json.dumps({k:v for k,v in result.items() if k!="cases"}),flush=True)
 if result["status"]!="PASS":raise SystemExit(5)
if __name__=="__main__":main()
