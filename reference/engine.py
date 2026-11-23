"""MELLANRUM V5.1: deterministic reference model, not an Atari ROM.
Abstract planner tick: one discretionary command before each owl step. Joystick
travel time not modelled by solve.py; full input trace validation is a later gate.
Only standard library. Coordinates: x=0..9, y=0..7. Half-board x=0..4,
right half reflected, target index=5*y+min(x,9-x).
"""
from dataclasses import dataclass, replace
from typing import Tuple
W,H=10,8
DX=(1,0,-1,0); DY=(0,1,0,-1) # E S W N

@dataclass(frozen=True)
class Room:
    id:str
    act:int
    title:str
    half:Tuple[str,...]  # 8 strings x 5: # immutable tree, . immutable clearing, T mutable tree, t mutable clearing
    owl:Tuple[int,int,int] # x,y,direction
    stone:Tuple[int,int]
    exit:Tuple[int,int]
    stone_initial:int=0
    instruction:str=''
    dramaturgy:str=''
    def validate(self):
        assert len(self.half)==8 and all(len(row)==5 for row in self.half)
        assert all(set(row)<=set('#.Tt') for row in self.half)
        for x,y in (self.owl[:2],self.stone,self.exit):
            assert 0<=x<W and 0<=y<H and self.half[y][min(x,9-x)] in '.t'
        assert self.act in (1,2,3)

@dataclass(frozen=True)
class State:
    x:int;y:int;direction:int;bits:int;polarity:int;phase:int;phase_age:int
    tick:int;queue:Tuple[Tuple[int,int],...];done:bool=False

def index(x,y):return 5*y+min(x,9-x)
def index_xy(idx):return (idx%5,idx//5)
def initial(r):
    r.validate()
    bits=0
    for y,row in enumerate(r.half):
        for x,c in enumerate(row):
            if c in ('#','T'):bits|=1<<(5*y+x)
    return State(*r.owl,bits,r.stone_initial,0,0,0,(),False)
def is_mutable(r,k):
    x,y=index_xy(k)
    return r.half[y][x] in 'Tt'
def passable(r,s,x,y,cursor=None):
    if not (0<=x<W and 0<=y<H):return False
    if (x,y)==r.stone or (x,y)==r.exit:return True
    k=index(x,y)
    blocked=bool(s.bits&(1<<k))
    if r.act==3: blocked = blocked ^ bool(s.phase)
    # Issue21: cursor hover is visual only; FIRE is the only tree edit.
    return not blocked

# Normative V5.1 interruption schedule, timed in owl beats (0-based).
# A warning occurs one beat before interception starts. All appearance is
# assembled from the three established motifs, never a fourth actor in RAM.
# These are candidate room-specific timings, subject to ROM/playtest verification.
INTRUSION_WINDOWS={"III-03":(2,2), "III-04":(1,2), "III-05":(3,2)}
FORESHADOW={"II-05":4, "III-01":4, "III-02":2}

def intrusion_phase(r,tick):
    """'none', 'warning', 'active', or 'glimpse' (non-interactive)."""
    w=INTRUSION_WINDOWS.get(r.id)
    if w is not None:
        start,duration=w
        if tick==start-1:return 'warning'
        if start<=tick<start+duration:return 'active'
    if FORESHADOW.get(r.id)==tick:return 'glimpse'
    return 'none'

def intrusion_search_key(r,tick):
    """Conserve absolute time only until this room's anomaly is over."""
    w=INTRUSION_WINDOWS.get(r.id)
    if w:
        start,duration=w
        return min(tick,start+duration)
    return 0

def options(r):
    opts=[('wait',-1),('stone',-1)]
    for y,row in enumerate(r.half):
        for x,c in enumerate(row):
            if c in 'Tt':opts.append(('tree',5*y+x))
    return opts

def step(r,s,action=('wait',-1),cursor=None):
    if s.done:return s
    typ,k=action
    bits=s.bits;polarity=s.polarity;queue=list(s.queue)
    intercepted=False
    # Player commands execute first. Rejected commands do not change any state.
    if typ=='stone':polarity^=1
    elif typ=='tree' and is_mutable(r,k):
        if r.act>1 and any(e[0]==k for e in queue):
            # Issue26: a second deliberate gesture cancels a future echo;
            # current tree state is left untouched, stone polarity flips.
            queue=[e for e in queue if e[0]!=k]
            polarity^=1
        elif r.act==1 or len(queue)<2:
            # V5.1: for two announced beats the unnamed presence intercepts
            # an otherwise legal tree command. It flips stone polarity INSTEAD
            # of toggling tree, never scheduling an echo. The action is spent.
            if intrusion_phase(r,s.tick)=='active':
                polarity^=1
                intercepted=True
            else:
                bits ^= (1<<k)
                if r.act>1:queue.append((k,s.tick+(3 if polarity==0 else 5)))
    # On the FIRST active owl beat, the presence changes stone polarity even
    # when ignored. If a valid tree action was intercepted that beat, that
    # single polarity flip already constitutes the event (no double-flip).
    w=INTRUSION_WINDOWS.get(r.id)
    if w and s.tick==w[0] and not intercepted:
        polarity^=1
    # Then committed echoes (no echo due on the same tick as its scheduling).
    due=[e for e in queue if e[1]==s.tick]
    queue=[e for e in queue if e[1]!=s.tick]
    for ek,_ in due:bits^=(1<<ek)
    # Phase count since previous inversion; polarity selects 4 vs 6 owl beats.
    phase=s.phase;phase_age=s.phase_age
    if r.act==3:
        phase_age+=1
        if phase_age>=(4 if polarity==0 else 6):
            phase^=1;phase_age=0
    ns=State(s.x,s.y,s.direction,bits,polarity,phase,phase_age,s.tick+1,tuple(sorted(queue)),False)
    # Owl chooses forward, right, left, backward; no truly random choices.
    x,y,d=s.x,s.y,s.direction
    for nd in (d,(d+1)&3,(d+3)&3,(d+2)&3):
        nx,ny=x+DX[nd],y+DY[nd]
        if passable(r,ns,nx,ny,cursor):
            x,y,d=nx,ny,nd
            break
    # Stone rotates heading on arrival, not every tick standing on stone.
    if (x,y)==r.stone and (s.x,s.y)!=r.stone:
        d=(d+(1 if polarity==0 else 3))&3
    return replace(ns,x=x,y=y,direction=d,done=(x,y)==r.exit)

def path_preview(r,sequence,maxsteps=40):
    s=initial(r)
    hist=[(s.x,s.y,s.direction,s.phase,s.bits)]
    for action in sequence[:maxsteps]:
        s=step(r,s,action)
        hist.append((s.x,s.y,s.direction,s.phase,s.bits))
        if s.done:break
    return s,hist
