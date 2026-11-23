from rooms import ROOMS
from solve import solve
from engine import initial, step
import json, pathlib, time
out=[]
for r in ROOMS:
 start=time.monotonic();path,n=solve(r,max_depth=32,max_states=45000)
 row=dict(id=r.id,act=r.act,title=r.title,path=path,states=n,search_seconds=round(time.monotonic()-start,2),solved=path is not None)
 out.append(row)
 print(r.id,'SOLVED' if path else 'UNKNOWN',len(path) if path else '-', 'states',n,'sec',row['search_seconds'],flush=True)
path=pathlib.Path(__file__).parent/'abstract_solution_results.json'
path.write_text(json.dumps(out,ensure_ascii=False,indent=2))
