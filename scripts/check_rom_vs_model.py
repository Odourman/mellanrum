#!/usr/bin/env python3
"""Compare 6507 machine code states against the unmodified V5.1 Python tick oracle.
This verifies instruction-level execution by a bespoke development model, not Atari TIA or Stella.
"""
import collections, json, pathlib, random, sys
ROOT=pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
sys.path.insert(0,str(ROOT/'reference'))
from cpu_trace import load
from rooms import ROOMS
from engine import initial,step

def call(c, label,limit=30000):
    before=c.pc;ret=before-1;c.pus((ret>>8)&255);c.pus(ret&255);c.pc=c.syms[label]
    steps=0
    while c.pc!=before:
        c.step();steps+=1
        if steps>=limit:raise AssertionError(f'{label} stalled at {c.pc:04X}')
    return steps

def new_room(i):
    c=load(str(ROOT/'build/mellanrum_ntsc.bin'),str(ROOT/'build/mellanrum_ntsc.sym'))
    c.pc=c.syms['Frame'];c.sp=255
    c.write(c.syms['room'],i);c.write(c.syms['mode'],1)
    call(c,'LoadRoom')
    return c

def rowbits(s,y):return sum(((s.bits>>(5*y+x))&1)<<x for x in range(5))
def observe(c):
    q=tuple(sorted([(c.ram('slot0Key'),c.ram('slot0Due'))] if c.ram('slot0Key')!=255 else [])+[])
    q=tuple(sorted((c.ram(f'slot{i}Key'),c.ram(f'slot{i}Due')) for i in (0,1) if c.ram(f'slot{i}Key')!=255))
    return dict(x=c.ram('owlX'),y=c.ram('owlY'),direction=c.ram('owlDir'),polarity=c.ram('polarity'),
                phase=c.ram('phase'),phase_age=c.ram('phaseAge'),tick=c.ram('beat'),
                queue=q,bits=tuple(c.read(c.syms['mapRows']+y) for y in range(8)),done=c.ram('mode')==2)

def expected(s):return dict(x=s.x,y=s.y,direction=s.direction,polarity=s.polarity,phase=s.phase,
                           phase_age=s.phase_age,tick=s.tick&255,queue=tuple(sorted((k,due&255) for k,due in s.queue)),
                           bits=tuple(rowbits(s,y) for y in range(8)),done=s.done)

def execute_action(c,r,a,cursor):
    c.write(c.syms['cursorX'],cursor[0]);c.write(c.syms['cursorY'],cursor[1]);
    typ,k=a
    c.write(c.syms['pending'],0 if typ=='wait' else (1 if typ=='tree' else 2))
    if typ=='tree':c.write(c.syms['pendingKey'],k)
    call(c,'BeatTick')

def cursor_for_action(r,a,old):
    typ,k=a
    if typ=='tree':return (k%5,k//5)
    if typ=='stone':return r.stone
    return old

def check(i,sequence,tag):
    r=ROOMS[i];c=new_room(i);s=initial(r)
    old_cursor=(r.owl[0],r.owl[1])
    for j,a in enumerate(sequence):
        if s.done:break
        cursor=cursor_for_action(r,a,old_cursor);old_cursor=cursor
        s=step(r,s,a,cursor=cursor)
        execute_action(c,r,a,cursor)
        got,want=observe(c),expected(s)
        if got!=want:
            diffs=[(k,got[k],want[k]) for k in want if got[k]!=want[k]]
            raise AssertionError(f'{tag}: {r.id} tick {j} action={a} cursor={cursor} mismatches: {diffs}')
    return s.done,s.tick

def main():
    rooms=json.loads((ROOT/'reference/rooms.json').read_text())
    count=0;win=0
    for i,room in enumerate(rooms):
        solution=[tuple(v) for v in room['solution_oracle_abstract']]
        done,ticks=check(i,solution,tag='witness');count+=ticks;win+=done
        print('ROOM',room['id'],'steps',ticks,'actual_cursor-aware_win',done)
    rng=random.Random(2600)
    random_runs=0;random_ticks=0
    for i,r in enumerate(ROOMS):
        opts=[('wait',-1),('stone',-1)]+[('tree',5*y+x) for y,row in enumerate(r.half) for x,c in enumerate(row) if c in 'Tt']
        for _ in range(15):
            actions=[rng.choice(opts) for _ in range(30)]
            done,ticks=check(i,actions,tag='random')
            random_runs+=1;random_ticks+=ticks
    print('ROM_REFERENCE_COMPARISON_PASS: witness_sequences',len(rooms),'cursor-aware-wins',win,
          'witness_ticks',count,'random_runs',random_runs,'random_ticks',random_ticks)
    return win==15
if __name__=='__main__':sys.exit(0 if main() else 1)
