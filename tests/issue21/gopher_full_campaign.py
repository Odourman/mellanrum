#!/usr/bin/env python3
"""Issue21 native Gopher2600 controller-only full campaign, no POKE.
Real STEP FRAME + STICK, read-only RAM via PEEK. Requires Gopher HEADLESS.
Records all input edges and all TV FRAME scanline totals. No CPU model PASS claims.
"""
import argparse,hashlib,json,re,subprocess,time
from pathlib import Path
p=argparse.ArgumentParser()
for k in ('rom','emulator','rooms','out'):p.add_argument('--'+k,required=True)
p.add_argument('--limit',type=int,default=15)
args=p.parse_args()
rom=Path(args.rom).resolve(); em=Path(args.emulator).resolve(); out=Path(args.out).resolve()
out.mkdir(parents=True,exist_ok=True)
rooms=json.loads(Path(args.rooms).read_text())
assert len(rooms)==15 and 1<=args.limit<=15
sha=hashlib.sha256(rom.read_bytes()).hexdigest()
assert len(rom.read_bytes())<=16384
cmd=[];events=[];checks=[];frame=0;cursor=(0,0)
def step(n):
 global frame
 assert n>=0,(n,frame)
 cmd.extend(['STEP FRAME']*n);frame+=n
def to(n):step(n-frame)
def change(c,label='input'):
 cmd.append(c);events.append({'frame':frame,'command':c,'purpose':label})
def checkpoint(label):
 cmd.extend(['TV FRAME','PEEK 0x00b8 0x00b9 0x00c6 0x00cc 0x00cd'])
 checks.append({'frame':frame,'label':label})
def image(name):cmd.append('SCREENSHOT '+str(out/name))
def move_to(x,y):
 global cursor
 for a,b,pos,neg in [(cursor[0],x,'RIGHT','LEFT'),(cursor[1],y,'DOWN','UP')]:
  direction=pos if b>a else neg
  for _ in range(abs(b-a)):
   change('STICK LEFT '+direction,'cursor step');step(1)
   change('STICK LEFT NO'+direction,'cursor release');step(1)
 cursor=(x,y)
def fire(label):
 change('STICK LEFT FIRE',label);step(3)
 change('STICK LEFT NOFIRE','fire release');step(1)
cmd.extend(['VERSION','CARTRIDGE HASH'])
change('PERIPHERAL LEFT STICK')
change('PANEL SET P0PRO','difficulty A')
change('PANEL SET P1PRO','right difficulty irrelevant')
step(6);checkpoint('title');image('title.png')
start=frame;fire('start');room_entry=start+1
step(5);checkpoint('room00_started');image('room_00.png')
for idx,r in enumerate(rooms[:args.limit]):
 cursor=tuple(r['owl_start'][:2])
 if idx>0:checkpoint('room%02d_started'%idx);image('room_%02d.png'%idx)
 actions=r['solution_oracle_abstract']
 for tick,(typ,key) in enumerate(actions):
  action_at=room_entry+(20 if tick==0 else 108+(tick-1)*72+20)
  to(action_at)
  if typ=='tree':
   move_to(key%5,key//5);fire('room%02d_beat%02d_tree%02d'%(idx,tick,key))
  elif typ=='stone':
   move_to(*r['stone']);fire('room%02d_beat%02d_stone'%(idx,tick))
  to(room_entry+108+tick*72+4)
  checkpoint('room%02d_tick%02d'%(idx,tick+1))
 to(frame+52);checkpoint('room%02d_complete'%idx)
 if idx+1<args.limit:
  change_frame=frame;fire('next_room')
  room_entry=change_frame+1;step(5)
if args.limit==15:
 change_frame=frame;fire('start_coda');checkpoint('coda_start')
 step(495);checkpoint('back_to_title');image('title_after_coda.png')
cmd.append('QUIT')
(out/'commands.txt').write_text('\n'.join(cmd)+'\n')
(out/'input_events.json').write_text(json.dumps(events,indent=2)+'\n')
(out/'checkpoints.json').write_text(json.dumps(checks,indent=2)+'\n')
started=time.monotonic()
with (out/'gopher_stdout.txt').open('w') as fh:
 proc=subprocess.run([str(em),'HEADLESS',str(rom)],input='\n'.join(cmd)+'\n',
                     text=True,cwd=str(out),stdout=fh,stderr=subprocess.STDOUT,timeout=900)
log=(out/'gopher_stdout.txt').read_text(errors='replace')
modes=[int(x,16) for x in re.findall(r'0x00b8[^\n]*= 0x([0-9a-fA-F]{2})',log)]
numbers=[int(x,16) for x in re.findall(r'0x00b9[^\n]*= 0x([0-9a-fA-F]{2})',log)]
scanlines=[int(x) for x in re.findall(r'total: (\d+)',log)]
assert len(modes)==len(checks) and len(numbers)==len(checks),(len(modes),len(checks))
wins=[]
for i in range(args.limit):
 labels=[k for k,x in enumerate(checks) if x['label']=='room%02d_complete'%i]
 if labels and modes[labels[0]]==2 and numbers[labels[0]]==i:wins.append(i)
complete=(args.limit<15 or (modes[-2:]==[3,0]))
status='PASS' if proc.returncode==0 and len(wins)==args.limit and complete and scanlines and all(n==262 for n in scanlines) else 'FAIL'
res={'status':status,'evidence':'REAL_GOPHER_CONTROLLER_ONLY_NO_POKE','rom_sha256':sha,
     'emulator_stdout_file':'gopher_stdout.txt','rooms_won':wins,'requested_rooms':args.limit,
     'coda_title':complete,'scanlines_checked':len(scanlines),'all_262':all(n==262 for n in scanlines),
     'frames':frame,'input_events':len(events),'checkpoints':len(checks),
     'mode_trace':modes,'room_trace':numbers,'elapsed_seconds':round(time.monotonic()-started,2)}
(out/'result.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res))
if status!='PASS':raise SystemExit(4)
