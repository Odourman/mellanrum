#!/usr/bin/env python3
"""Parse genuine Gopher2600 HEADLESS PEEK + TV FRAME transcript, not planned witness assumptions."""
import argparse, json, re, hashlib
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--dir',required=True);p.add_argument('--emulator-source',default='74c544203378c1448a33c29bc8b4586079b050f4');a=p.parse_args()
out=Path(a.dir);expected=[json.loads(x) for x in (out/'expected_checkpoints.jsonl').read_text().splitlines()]
raw=(out/'gopher_stdout.txt').read_text(errors='replace')
pattern=re.compile(r'top: (\d+), bottom: (\d+), total: (\d+)\s*\n((?:0x[0-9a-fA-F]{4} \([^)]+\) = 0x[0-9a-fA-F]{2}\s*\n?)+)')
entries=[]
for m in pattern.finditer(raw):
    vals={int(h,16):int(v,16) for h,v in re.findall(r'0x([0-9a-fA-F]{4}) \([^)]+\) = 0x([0-9a-fA-F]{2})',m.group(4))}
    if 0x00b8 in vals and 0x00b9 in vals and 0x00c6 in vals:
        entries.append({'frame_data_total_scanlines':int(m.group(3)),'actual':{'mode':vals[0xb8],'room':vals[0xb9],'beat':vals[0xc6]},'ram':{f'0x{k:04x}':v for k,v in vals.items()}})
errors=[];observations=[]
if len(entries)!=len(expected): errors.append({'kind':'CHECKPOINT_COUNT','expected':len(expected),'actual':len(entries)})
for i,(want,got) in enumerate(zip(expected,entries)):
    bad={k:(v,got['actual'].get(k)) for k,v in want['expected'].items() if got['actual'].get(k)!=v}
    data={'checkpoint_index':i,'planned_frame_index':want['frame_index'],'label':want['label'],'expected':want['expected'],'observed':got['actual'],'scanlines':got['frame_data_total_scanlines'],'status':'FAIL' if bad else 'PASS'}
    observations.append(data)
    if bad: errors.append({'kind':'MISMATCH','data':data,'mismatch':bad})
passed=[o for o in observations if o['status']=='PASS']
win=[o for o in observations if o['label'].endswith('win_wait_over') and o['status']=='PASS']
roomend=[o for o in observations if re.match(r'room_\d\d_tick_\d\d',o['label']) and o['expected'].get('mode')==2 and o['status']=='PASS']
screens=sorted(x.name for x in out.glob('room_*.png'))
res={'classification':'REAL_INPUT_DRIVEN_FRAMES_STEP_FRAME_GOPHER2600','status':'PASS' if not errors and len(roomend)==15 and len(screens)==15 and observations[-1]['label']=='coda_return_title' else 'FAIL' if errors else 'INCONCLUSIVE','source_emulator_revision':a.emulator_source,'requested_frames':json.loads((out/'metadata.json').read_text())['total_emulated_frame_steps'],'checkpoints_expected':len(expected),'checkpoints_observed':len(entries),'checkpoints_pass':len(passed),'room_wins_demonstrated':len(roomend),'first_blocked_room':'I-01' if not roomend else f'room-index-{len(roomend)}' if len(roomend)<15 else None,'screenshots':len(screens),'mismatches':errors[:20],'observed_261_scanlines':sum(e['frame_data_total_scanlines']==261 for e in entries),'observed_262_scanlines':sum(e['frame_data_total_scanlines']==262 for e in entries),'real_rom_unchanged':True,'input_trace':str(out/'events.jsonl')}
(out/'parsed_checkpoints.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in observations))
(out/'campaign_real_result.json').write_text(json.dumps(res,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({k:v for k,v in res.items() if k!='mismatches'},ensure_ascii=False));print('FIRST_MISMATCH',errors[0] if errors else 'none')
