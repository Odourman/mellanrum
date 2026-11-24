from rooms import ROOMS
from engine import initial, step,index_xy
import json, pathlib
results=json.loads((pathlib.Path(__file__).parent/'abstract_solution_results.json').read_text())
for r,res in zip(ROOMS,results):
    assert r.id==res['id'] and res['solved']
    state=initial(r)
    cursor=r.owl[:2]
    last_tick=-2 # 1.8s of opening time before the first owl beat
    max_load=0
    for t,a in enumerate(res['path']):
        kind,k=a
        if kind=='tree':
            x,y=index_xy(k)
            targets=[(x,y),(9-x,y)]
            target=min(targets,key=lambda p:abs(p[0]-cursor[0])+abs(p[1]-cursor[1]))
        elif kind=='stone':target=r.stone
        else:target=cursor
        if kind!='wait':
            dist=abs(target[0]-cursor[0])+abs(target[1]-cursor[1])
            allowed=(t-last_tick)*7
            assert dist<=allowed,(r.id,t,a,cursor,target,dist,allowed)
            last_tick=t
            cursor=target
        state=step(r,state,tuple(a))
        max_load=max(max_load,len(state.queue))
    assert state.done,r.id
    res['coarse_cursor_travel_checked']=True
    res['max_queue_load']=max_load
    res['completed_at_tick']=len(res['path'])
print('All 15 abstract solutions pass 7-cells-per-owl-step travel envelope; not an exact joystick frame trace.')
(pathlib.Path(__file__).parent/'abstract_solution_results.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
