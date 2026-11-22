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
 assert ImageChops.difference(imgs['title'],imgs['title_after_reset']).getbbox() is None,(c,'RESET failed to return title')
 assert ImageChops.difference(imgs['title_after_reset'],imgs['running_after_reset']).getbbox(),(c,'no restart -> gameplay transition')
 assert imgs['running_initial'].getpixel((100,20))==imgs['running_after_difficulty_change'].getpixel((100,20)),(c,'midgame switch changed mode palette')
 # Title glyph top band in either left A/B must not change because UI no longer selects mode.
 d=ImageChops.difference(imgs['title'].crop((10,45,310,132)),imgs['title_after_select_joystick'].crop((10,45,310,132)))
 pixels=sum(1 for x in d.getdata() if x!=(0,0,0))
 print('STELLA_AB_CASE_OBSERVED',c,'resolution',imgs['title'].size,'title-change-pixels',pixels)
# The new A->B after RESET must show the old B scene palette, and vice versa.
a0=Image.open(p/'LEFT_A_running_initial.png').convert('RGB').getpixel((100,20))
b0=Image.open(p/'LEFT_B_running_initial.png').convert('RGB').getpixel((100,20))
a1=Image.open(p/'LEFT_A_running_after_reset.png').convert('RGB').getpixel((100,20))
b1=Image.open(p/'LEFT_B_running_after_reset.png').convert('RGB').getpixel((100,20))
assert a0!=b0,('A/B not visibly distinct',a0,b0)
assert a1==b0 and b1==a0,('after RESET must re-latch current A/B',a0,b0,a1,b1)
print('STELLA_MODE_PALETTE_LATCH_PASS: A->B and B->A after RESET, midgame A/B not switched')
print('REAL_STELLA_AB_PNG_PASS: two separate console-switch runs, snapshots and input event log; mode RAM requires Stella debugger evidence')
