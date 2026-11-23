#!/usr/bin/env python3
"""Produce and execute two actual normal-cartridge controller input traces.
No POKE, patched ROM, forced program counter or direct cursor movements.
Solutions from V5.1 are SCHEDULING HINTS, NOT assumed real emulator wins.
"""
import argparse,hashlib,json,subprocess,time,sys,re
from pathlib import Path
SHA='18163c0435347695ee1cff5a4b6b19c80d280ec255eeb7f9b98711471ccde11c'
p=argparse.ArgumentParser();p.add_argument('--emulator',required=True);p.add_argument('--rom',required=True);p.add_argument('--rooms',default='reference/rooms.json');p.add_argument('--paths',required=True);p.add_argument('--out',default='build/pachinko/campaign');p.add_argument('--attempt',type=int,default=1);p.add_argument('--generate-only',action='store_true');args=p.parse_args()
rom=Path(args.rom).resolve();em=Path(args.emulator).resolve();rooms=json.loads(Path(args.rooms).read_text());out=Path(args.out).resolve();out.mkdir(parents=True,exist_ok=True)
assert hashlib.sha256(rom.read_bytes()).hexdigest()==SHA and len(rom.read_bytes())==4096
paths=json.loads(Path(args.paths).read_text());assert len(paths)==15 and all(r['id']==p['id'] and p['abstract_solver']=='PASS' for r,p in zip(rooms,paths))
for r,p in zip(rooms,paths):r['solution_oracle_abstract']=p['abstract_solution']
assert len(rooms)==15
cmd=[];events=[];checks=[];frame=0;cursor=(0,0)
def add(line):cmd.append(line)
def step(n):
 global frame
 if n<0:raise RuntimeError(f'backwards frame scheduling {n} at {frame}')
 cmd.extend(['STEP FRAME']*n);frame+=n
# Endpoints of each event are measured as frame calls to the real Gopher2600 debugger.
def e(c,meaning='controller'):
 events.append({'frame_index':frame,'command':c,'class':meaning});add(c)
def to(n):step(n-frame)
def checkpoint(label,expected):
 checks.append({'frame_index':frame,'label':label,'expected':expected});
 add('TV FRAME');add('PEEK 0x00b8 0x00b9 0x00bc 0x00bd 0x00bf 0x00c3 0x00c4 0x00c6 0x00db')
def image(name):add('SCREENSHOT '+str(out/name))
def move_to(x,y):
 global cursor
 x0,y0=cursor
 for axis,old,new,positive,negative in [('x',x0,x,'RIGHT','LEFT'),('y',y0,y,'DOWN','UP')]:
  direction=positive if new>old else negative
  for _ in range(abs(new-old)):
   e('STICK LEFT '+direction,'cursor_tap_press');step(1)
   e('STICK LEFT NO'+direction,'cursor_tap_release');step(1)
 cursor=(x,y)
def fire(label):
 e('STICK LEFT FIRE',label+'_down');step(3)
 e('STICK LEFT NOFIRE',label+'_up');step(1)
# Start at normal title, no state injection.
add('VERSION');add('CARTRIDGE HASH');e('PERIPHERAL LEFT STICK');e('PANEL SET P0PRO','hardware_A');e('PANEL SET P1PRO','right_irrelevant')
step(6);image('title.png');checkpoint('title',{'mode':0})
start=frame;fire('start_campaign');room_entry=start+1
step(5);checkpoint('room_00_started',{'mode':1,'room':0});image('room_00.png')
for idx,r in enumerate(rooms):
 owl=r['owl_start'];cursor=(owl[0],owl[1])
 # Start times from planned asynchronous controller actions; will be checked against real emulator RAM.
 if idx>0:
  checkpoint(f'room_{idx:02d}_started',{'mode':1,'room':idx})
  image(f'room_{idx:02d}.png')
 actions=r['solution_oracle_abstract']
 for tick,(typ,k) in enumerate(actions):
  action_frame=room_entry+(20 if tick==0 else 108+(tick-1)*72+20)
  to(action_frame)
  if typ=='tree':
   target=(k%5,k//5);move_to(*target);fire(f'room{idx:02d}_tick{tick:02d}_tree{k}')
  elif typ=='stone':
   target=tuple(r['stone']);move_to(*target);fire(f'room{idx:02d}_tick{tick:02d}_stone')
  # WAIT performs no discretionary command.
  to(room_entry+108+tick*72+4)
  checkpoint(f'room_{idx:02d}_tick_{tick:02d}',{'mode':2 if tick==len(actions)-1 else 1,'room':idx,'beat':tick+1})
 # Advance next room by FIRE after 48-frame completion freeze.
 if idx<14:
  to(frame+52)
  checkpoint(f'room_{idx:02d}_win_wait_over',{'mode':2,'room':idx})
  change=frame;fire('next_room');room_entry=change+1
  step(5)
 else:
  to(frame+52)
  change=frame;fire('start_coda')
  checkpoint('coda_started',{'mode':3,'room':14})
  step(495)
  checkpoint('coda_return_title',{'mode':0})
  image('coda_after.png')
add('QUIT')
(out/'commands.txt').write_text('\n'.join(cmd)+'\n')
(out/'events.jsonl').write_text(''.join(json.dumps(x)+'\n' for x in events))
(out/'expected_checkpoints.jsonl').write_text(''.join(json.dumps(x)+'\n' for x in checks))
(out/'metadata.json').write_text(json.dumps({'run':args.attempt,'classification':'REAL_INPUT_DRIVEN_NO_INSTRUMENTATION','input_time_base':'GOPHER2600 STEP FRAME', 'expected_ROM_SHA':SHA,'total_emulated_frame_steps':frame,'command_count':len(cmd),'checkpoints':len(checks)},indent=2)+'\n')
if args.generate_only:
 print(json.dumps({'frames':frame,'events':len(events),'checkpoints':len(checks),'commands':len(cmd)}));raise SystemExit(0)
with (out/'gopher_stdout.txt').open('w') as stdout:
 try:
  proc=subprocess.run([str(em),'HEADLESS',str(rom)],cwd=str(out),input='\n'.join(cmd)+'\n',text=True,stdout=stdout,stderr=subprocess.STDOUT,timeout=600)
 except subprocess.TimeoutExpired:
  (out/'result.json').write_text(json.dumps({'status':'INCONCLUSIVE','reason':'EMULATOR_TIMEOUT','frames_commanded':frame,'classification':'REAL_INPUT_DRIVEN'})+'\n');raise
log=(out/'gopher_stdout.txt').read_text(errors='replace');screens=[x.name for x in out.glob('*.png')]
res={'status':'INCONCLUSIVE','classification':'REAL_INPUT_DRIVEN','cause':'No verified automatic RAM checkpoint parser yet; real gameplay wins must not be inferred from planned input','emulator_return_code':proc.returncode,'requested_frames':frame,'screenshots':len(screens),'checkpoint_count':len(checks),'rom_sha':SHA,'requested_room_paths':15,'verified_real_room_wins':0,'first_blocked_room':'UNKNOWN_UNTIL_RAM_TRACE_VALIDATED'}
if proc.returncode!=0:res['status']='FAIL';res['cause']='Gopher2600 returned nonzero; inspect stdout'
(out/'result.json').write_text(json.dumps(res,indent=2)+'\n')
print(json.dumps(res));print(log[-1500:]);sys.exit(0 if proc.returncode==0 else 1)
