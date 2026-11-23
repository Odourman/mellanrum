"""Issue #21 model-only acceptance: 15 different solvable scenes, no passive win
over 600 owl beats (>600 NTSC seconds) and one specific action counterfactual.
DO NOT report this as real Gopher/Stella joystick PASS. Cursor travel is not modeled.
"""
import json
from pathlib import Path
from engine import initial, step
from rooms import ROOMS, DOCUMENT

assert len(ROOMS) == 15
assert len(set(tuple(r.half) for r in ROOMS)) == 15

def replay(r, path, after=0):
    s = initial(r)
    for a in path:
        s = step(r, s, tuple(a))
        if s.done:
            return s
    for _ in range(after):
        s = step(r, s, ('wait', -1))
        if s.done:break
    return s

out=[]
for room, data in zip(ROOMS, DOCUMENT):
    assert room.id == data['id']
    witness = data['solution_oracle_abstract']
    won = replay(room,witness).done
    idle = replay(room,[],after=600).done
    at,kind,key = data['essential_action']
    assert witness[at] == [kind,key],(room.id,'counterfactual source mismatch')
    counterfactual = [a[:] for a in witness]
    counterfactual[at] = ['wait', -1]
    removed_action_wins = replay(room,counterfactual,after=max(0,600-len(witness))).done
    row = dict(room=room.id,act=room.act,steps=len(witness),source_witness=won,
               source_idle_600_beats=idle,one_critical_action_omitted_wins=removed_action_wins,
               critical_action=[at,kind,key],evidence='SOURCE_ONLY')
    out.append(row)
    print(room.id,row,flush=True)
    assert won and not idle and not removed_action_wins,room.id
p=Path(__file__).parent/'issue21_source_only_model_results.json'
p.write_text(json.dumps(out,indent=2)+'\n')
print('SOURCE_ONLY_PASS: 15/15 source-model wins; 0/15 passive and 0/15 counterfactual wins; real emulator NOT_RUN')
