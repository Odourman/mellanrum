#!/usr/bin/env python3
"""Exhaustive finite-state check for C2 bit0 FIRE / bit1 SELECT encoding."""
import json
states=range(4)
checks=[]
for packed in states:
    fire=packed&1; select=(packed>>1)&1
    assert fire==bool(packed&1) and select==bool(packed&2)
    # Press/release each edge independently while preserving the other edge.
    for action,mask,want in [('fire_press',1,1),('fire_release',1,0),('select_press',2,2),('select_release',2,0)]:
        new=(packed|mask) if want else (packed&(~mask&3))
        expected_fire=(want if mask==1 else fire)
        expected_select=(1 if mask==2 and want else 0 if mask==2 else select)
        assert (new&1)==expected_fire and ((new>>1)&1)==expected_select
        checks.append({'from':packed,'action':action,'to':new,'fire':new&1,'select':(new>>1)&1})
out={'status':'PASS_MODEL_ONLY','state_domain':[0,1,2,3],'transition_checks':len(checks),
     'preserves_unmodified_edge':True,'actual_ROM_emulator_transition_test':'NOT_RUN: C2 native build exceeds fixed bank3 origin by 15 bytes'}
from pathlib import Path
Path(__file__).with_name('C2_BITPACK_EXHAUSTIVE_MODEL.json').write_text(json.dumps({**out,'cases':checks},indent=2)+'\n')
print(json.dumps(out))
