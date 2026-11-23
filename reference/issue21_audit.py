#!/usr/bin/env python3
"""Issue #21 independent reference-level gate/idle audit; NOT a native-emulator pass."""
import json,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from engine import initial,step
from rooms import ROOMS
from solve import solve
out=[]
for r in ROOMS:
    s=initial(r)
    for i in range(500):  # 500 owl beats ~= 600 s normal 72 NTSC frames/beat
        s=step(r,s,('wait',-1))
        if s.done: break
    idle=bool(s.done)
    other=next((5*y+x for y,row in enumerate(r.half) for x,c in enumerate(row) if c in 'Tt' and 5*y+x!=r.gate_key),None)
    w=initial(r)
    for i in range(500):  # wrong editable tree vs the exact resonant tree
        w=step(r,w,('tree',other) if other is not None and i==0 else ('wait',-1))
        if w.done: break
    path,states=solve(r,max_depth=45,max_states=150000)
    pass_model=path is not None
    if path:
        a=initial(r)
        for action in path:
            a=step(r,a,action)
        assert a.done
    row={'id':r.id,'gate_key':r.gate_key,'idle_500beat_win':idle,'wrong_tree_500beat_win':w.done,
         'abstract_solver':'PASS' if pass_model else 'NOT_SOLVED','abstract_solution':path,'states_explored':states,
         'source_level_only':True}
    out.append(row)
    print(r.id,'idle',idle,'wrong-tree',w.done,'abstract',row['abstract_solver'],'steps',len(path) if path else None,flush=True)
dst=Path('build/issue21')
dst.mkdir(parents=True,exist_ok=True)
(dst/'model_gate_idle_results.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
assert len(out)==15 and not any(x['idle_500beat_win'] or x['wrong_tree_500beat_win'] for x in out)
print('SOURCE_IDLE_0_OF_15_AND_WRONG_TREE_COUNTERFACTUAL_PASS')
if not all(x['abstract_solver']=='PASS' for x in out):
    print('ABSTRACT_SOLVER_NOT_ALL_ROOMS_PASS: developer game certification BLOCKED')
    sys.exit(2)
print('ABSTRACT_ALL_15_REACHABLE_PASS - EMULATOR_CONTROLLER_TEST_STILL_NOT_RUN')
