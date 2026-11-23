"""Abstract reachability search for authored rooms. NOT joystick-trajectory verification."""
from collections import deque
from engine import initial,step,options,intrusion_search_key

def solve(room,max_depth=34,max_states=90000):
    root=initial(room)
    todo=deque([root]);vis={key(room,root):None};depth={key(room,root):0};dct={key(room,root):root}
    acts=options(room)
    while todo:
        s=todo.popleft();k=key(room,s);dep=depth[k]
        if s.done:
            out=[]
            while vis[k] is not None:
                p,ac=vis[k];out.append(ac);k=p
            return list(reversed(out)),len(vis)
        if dep>=max_depth:continue
        for a in acts:
            t=step(room,s,a)
            kt=key(room,t)
            if kt not in vis:
                vis[kt]=(k,a);depth[kt]=dep+1;dct[kt]=t;todo.append(t)
                if len(vis)>=max_states:return None,len(vis)
    return None,len(vis)

def key(r,s):
    # Future matters only via relative due tick offsets, not absolute tick.
    return (s.x,s.y,s.direction,s.bits,s.polarity,s.phase,s.phase_age,
            tuple((k,d-s.tick) for k,d in s.queue),s.done,s.visitedstone, intrusion_search_key(r,s.tick))
