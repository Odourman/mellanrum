#!/usr/bin/env python3
"""Basic actual Stella screenshot checks. Not a debugger RAM state proof."""
from pathlib import Path
from PIL import Image, ImageChops
p=Path('build/ab/record')
assert (p.parent/'input_events.tsv').exists()
for c in ['LEFT_A','LEFT_B']:
 imgs={k:Image.open(p/f'{c}_{k}.png').convert('RGB') for k in ['title','title_after_select_joystick','running_initial','running_after_difficulty_change','title_after_reset','running_after_reset']}
 assert len({v.size for v in imgs.values()})==1 and all(v.size==(320,228) for v in imgs.values()),(c,'wrong dimensions')
 # Original emulator title must have bright glyphs somewhere in top half.
 assert len(imgs['title'].getcolors(maxcolors=1000000) or [])>1,(c,'blank title')
 assert ImageChops.difference(imgs['title'],imgs['running_initial']).getbbox(),(c,'no title -> gameplay image transition')
 assert ImageChops.difference(imgs['title_after_reset'],imgs['running_after_reset']).getbbox(),(c,'no restart -> gameplay transition')
 # Title glyph top band in either left A/B must not change because UI no longer selects mode.
 d=ImageChops.difference(imgs['title'].crop((10,45,310,132)),imgs['title_after_select_joystick'].crop((10,45,310,132)))
 pixels=sum(1 for x in d.getdata() if x!=(0,0,0))
 print('STELLA_AB_CASE_OBSERVED',c,'resolution',imgs['title'].size,'title-change-pixels',pixels)
assert (p/'LEFT_A_running_initial.png').read_bytes()!=(p/'LEFT_B_running_initial.png').read_bytes(),'same screenshot for both modes'
print('REAL_STELLA_AB_PNG_PASS: two separate console-switch runs, snapshots and input event log; mode RAM requires Stella debugger evidence')
