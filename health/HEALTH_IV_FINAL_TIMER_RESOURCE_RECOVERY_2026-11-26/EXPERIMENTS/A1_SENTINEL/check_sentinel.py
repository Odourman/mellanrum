import argparse,json,pathlib,hashlib,sys
sys.path.insert(0,'/workspace/scratch/c1a21baf9747/timer_lab/package/BASELINE/PRIOR_HEALTH_EVIDENCE/MELLANRUM_HEALTH_OPTIMIZATION_LAB_EVIDENCE/TEST_TOOLS')
from libretro_stella_capture import Core,mapping_for
p=argparse.ArgumentParser()
for k in ('core','rom','replay','out'):p.add_argument('--'+k,required=True)
a=p.parse_args(); out=pathlib.Path(a.out);out.mkdir(parents=True,exist_ok=True)
e=json.loads(pathlib.Path(a.replay).read_text()); rom=pathlib.Path(a.rom); b=rom.read_bytes(); sha=hashlib.sha256(b).hexdigest()
assert len(b)==16384
core=Core(a.core,str(rom),str(out),0); mp=mapping_for(core.desc); events=e['events'];idx=0;bad=[];modes=set();rooms=set();
for f in range(e['frames']):
 while idx+1<len(events) and f>=events[idx]['end']:idx+=1
 row=events[idx]; buttons=set(row['buttons']) if row['start']<=f<row['end'] else set()
 core.run({mp[x] for x in buttons},f); ram=core.memory(); assert len(ram)==128
 sentinel=ram[0xC1-0x80]
 if sentinel != 0xA5:bad.append({'frame':f,'value':sentinel});break
 modes.add(ram[0xB8-0x80]);rooms.add(ram[0xB9-0x80])
core.close();result={'status':'PASS' if not bad else 'FAIL','diagnostic_only':True,'rom_sha256':sha,'stella_core_sha256':hashlib.sha256(pathlib.Path(a.core).read_bytes()).hexdigest(),'watched_ram_address':'$C1','sentinel':'$A5','frames_checked':f+1,'modes_seen':sorted(modes),'room_indices_seen':sorted(rooms),'first_corruption':bad[0] if bad else None,'method':'real Stella libretro, controller replay, read-only 128-byte RAM per frame'}
(out/'sentinel_result.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result));core.close if False else None
if bad:raise SystemExit(1)
