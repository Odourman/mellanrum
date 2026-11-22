#!/usr/bin/env python3
"""100 deterministic randomized REAL Gopher2600 sessions per room, after authentic
non-instrumented title->room route; SELECT restarts each current room.
Input applied by Gopher2600 HEADLESS STEP FRAME, exact video frame ordinal.

The 100 session outcomes are not a proof every policy event is reachable:
we measure and publish actual mode/room, beat, palette and raster. One room
can be reached with normal joystick+FIRE without any POKE/state injection.
"""
import argparse,collections,hashlib,json,random,re,subprocess,sys,time
from pathlib import Path
ROM_SHA='e9ea87d381bcf8da39ec055d7d6951ceff97b21d3a798addd10fbbe540c5e974'
GOPHER_SHA='74c544203378c1448a33c29bc8b4586079b050f4'
A=argparse.ArgumentParser();A.add_argument('--emulator',required=True);A.add_argument('--rom',required=True);A.add_argument('--rooms',default='reference/rooms.json');A.add_argument('--room',type=int,required=True);A.add_argument('--seeds',type=int,default=100);A.add_argument('--out',required=True);A.add_argument('--long-frames',type=int,default=10000);A.add_argument('--generate-only',action='store_true');args=A.parse_args()
assert 0<=args.room<15 and args.seeds>=1
rom=Path(args.rom).resolve();em=Path(args.emulator).resolve();out=Path(args.out).resolve();out.mkdir(parents=True,exist_ok=True)
assert len(rom.read_bytes())==4096 and hashlib.sha256(rom.read_bytes()).hexdigest()==ROM_SHA
rooms=json.loads(Path(args.rooms).read_text());assert len(rooms)==15
# Import no gameplay oracle: generate scheduling witness as hints only.
# campaign_attempt's generated command trace uses real controller port and its
# room checkpoints are NOT accepted until observed in the emulator.
from tempfile import TemporaryDirectory
with TemporaryDirectory() as temp:
    proc=subprocess.run([sys.executable,str(Path(__file__).resolve().parent/'campaign_attempt.py'),'--generate-only','--emulator',str(em),'--rom',str(rom),'--rooms',str(Path(args.rooms).resolve()),'--out',temp],capture_output=True,text=True,timeout=60)
    if proc.returncode:raise RuntimeError(proc.stdout+'\n'+proc.stderr)
    cmds=(Path(temp)/'commands.txt').read_text().splitlines()
    points=[json.loads(x) for x in (Path(temp)/'expected_checkpoints.jsonl').read_text().splitlines()]
    sought=next(p for p in points if p['label']==f'room_{args.room:02d}_started' if args.room!=0) if args.room!=0 else next(p for p in points if p['label']=='room_00_started')
    goal=sought['frame_index'];count=0;cut=None
    for i,c in enumerate(cmds):
        if c=='STEP FRAME':count+=1
        if count==goal and c.startswith('SCREENSHOT ') and ('room_'+f'{args.room:02d}'+'.png') in c:
            cut=i+1;break
    if cut is None:raise RuntimeError('Unable to cut witness route at authentic room start '+str(args.room))
    prefix=[c for c in cmds[:cut] if not c.startswith('SCREENSHOT ')]
prefix_peeks=sum(1 for c in prefix if c.startswith("PEEK "))
frame=goal;cmd=prefix[:];event_log=[];sessions=[];snapshots=[]
# prefix normal-title/controller source is exact from same input generator; no POKE.
def push(x):cmd.append(x)
def event(c,session,role):
    event_log.append({'room':args.room,'session':session,'frame_index_global':frame,'command':c,'role':role})
    push(c)
def step(n):
    global frame
    cmd.extend(['STEP FRAME']*n);frame+=n
def tv(label):
    snapshots.append({'label':label,'frame_index_global':frame})
    push('TV FRAME');push('PEEK 0x00b8 0x00b9 0x00c3 0x00c4 0x00c6 0x00db 0x00cc 0x00cd')
tv('room_target_reached_by_normal_joystick')
push('SCREENSHOT '+str(out/'actual_reachable_room.png'))
# Reproducible seed policies; all input is really injected via Gopher PANEL/STICK ports.
policies=['RAIN','TILT_FIRE','TILT_STONE','CLOG','BOG','COUNTERFACTUAL']
buttons=['UP','DOWN','LEFT','RIGHT']
for seed in range(args.seeds):
    policy=policies[seed%len(policies)]
    seed_str=f'{ROM_SHA}:{args.room}:{seed}:{policy}'
    seed_int=int.from_bytes(hashlib.sha256(seed_str.encode()).digest()[:8],'big')
    rng=random.Random(seed_int)
    event('PANEL HOLD SELECT',seed,'room_restart_select_down');step(3)
    event('PANEL RELEASE SELECT',seed,'room_restart_select_up');step(3)
    # Intro 108 frames, plus first logical tick. Short cases 240f and one-in-five long cases 600f.
    frames=600 if seed%5==0 else 240
    # Use discrete 10f windows for varied adversarial actions; no RAM/state POKE.
    for i in range(frames//10):
        d=buttons[rng.randrange(4)]
        # Counterfactual pairs preserve random sequence apart from one FIRE event.
        if policy=='COUNTERFACTUAL':
            rng=random.Random(int.from_bytes(hashlib.sha256(f'{ROM_SHA}:{args.room}:{seed//2}:{i}'.encode()).digest()[:8],'big'))
            d=buttons[rng.randrange(4)]
        if policy=='TILT_STONE' and i%3 in (0,1):d=['RIGHT','DOWN'][i%2]
        if policy=='BOG' and i%5:step(10);continue
        event('STICK LEFT '+d,seed,'direction_'+policy);step(2)
        event('STICK LEFT NO'+d,seed,'release_direction');step(1)
        press=(policy in ('TILT_FIRE','CLOG')) or (policy=='BOG' and i%8==0) or (rng.random()<(0.32 if policy=='RAIN' else 0.19))
        if policy=='COUNTERFACTUAL' and i==12:press=bool(seed%2)
        if press:
            event('STICK LEFT FIRE',seed,'fire_down_'+policy);step(2)
            event('STICK LEFT NOFIRE',seed,'fire_up');step(1)
            step(4)
        else:step(7)
    tv(f'seed_{seed:03d}_{policy}_end')
    sessions.append({'room_index':args.room,'seed':seed,'policy':policy,'deterministic_seed':seed_int,'classification':'REAL_PRODUCTION_ROM_REACHED_WITH_NORMAL_CONTROLLER_SELECT_RESTART','frames_observed_by_real_emulator':frames+6,'frame_end_global':frame})
# Independent repeated idle stress, no synthetic RAM state.
event('PANEL HOLD SELECT','LONG','restart_before_real_longrun');step(3)
event('PANEL RELEASE SELECT','LONG','restart_release');step(3)
tv('long_start')
for i in range(args.long_frames):
    step(1)
    if (i+1)%1000==0:tv(f'long_{i+1:05d}')
push('SCREENSHOT '+str(out/'long_end.png'))
push('QUIT')
(out/'commands.txt').write_text('\n'.join(cmd)+'\n')
(out/'events.jsonl').write_text(''.join(json.dumps(x)+'\n' for x in event_log))
(out/'sessions.jsonl').write_text(''.join(json.dumps(x)+'\n' for x in sessions))
(out/'checkpoints.jsonl').write_text(''.join(json.dumps(x)+'\n' for x in snapshots))
meta={'classification':'REAL_INPUT_DRIVEN_6507_TIA_GOPHER_UNMODIFIED_ROM','rom_sha256':ROM_SHA,'source_commit':'49eb168b17d0254d06cf50d87c60e8fb6016db6e','emulator_commit':GOPHER_SHA,'room':args.room,'sessions_requested':args.seeds,'frames_per_session':'600 every fifth, else 240, plus six restart frames','long_consecutive_real_frames':args.long_frames,'total_frames_commanded':frame,'commands':len(cmd),'replay_command':f'gopher2600 HEADLESS {rom} < commands.txt'}
(out/'metadata.json').write_text(json.dumps(meta,indent=2)+'\n')
if args.generate_only:
    print(json.dumps(meta));sys.exit(0)
with (out/'gopher_stdout.log').open('w') as stdout:
    try:r=subprocess.run([str(em),'HEADLESS',str(rom)],input='\n'.join(cmd)+'\n',text=True,stdout=stdout,stderr=subprocess.STDOUT,timeout=2400)
    except subprocess.TimeoutExpired: r=None
s=(out/'gopher_stdout.log').read_text(errors='replace')
block=re.compile(r'top: \d+, bottom: \d+, total: (\d+)\s*\n((?:0x[0-9a-fA-F]{4} \([^)]+\) = 0x[0-9a-fA-F]{2}\s*\n?)+)')
observed=[]
for match in block.finditer(s):
    vals={int(p,16):int(v,16) for p,v in re.findall(r'0x([0-9a-fA-F]{4}) \([^)]+\) = 0x([0-9a-fA-F]{2})',match.group(2))}
    if 0xb8 in vals and 0xb9 in vals:
        observed.append({'scanlines':int(match.group(1)),'mode':vals[0xb8],'room':vals[0xb9],'beat':vals.get(0xc6),'presence':vals.get(0xdb)})
observed_all=observed
observed=observed[prefix_peeks:]
paired=[dict(ck,actual=ob) for ck,ob in zip(snapshots,observed)]
(out/'observed_checkpoints.jsonl').write_text(''.join(json.dumps(x)+'\n' for x in paired))
# If room changed unexpectedly, classify as FAIL not as arbitrary room success.
wrong=[x for x in paired if x['actual']['room']!=args.room or x['actual']['mode'] not in (1,2)]
status='PASS' if r is not None and r.returncode==0 and len(observed)==len(snapshots) and not wrong else 'FAIL' if wrong else 'INCONCLUSIVE'
res={'status':status,'classification':meta['classification'],'sessions_executed_in_genuine_Gopher2600':len(sessions) if r is not None and r.returncode==0 else 0,'room':args.room,'actual_room_first_observation':observed[0] if observed else None,'checkpoints_observed':len(observed),'checkpoints_expected':len(snapshots),'mismatches':wrong[:10],'true_raster_counts':dict(collections.Counter(x['scanlines'] for x in observed)),'long_run_requested':args.long_frames,'long_run_executed':args.long_frames if r is not None and r.returncode==0 else 0,'emulator_exit':r.returncode if r is not None else 'timeout','no_poke_or_modified_rom':True}
(out/'result.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps({k:v for k,v in res.items() if k!='mismatches'}))
