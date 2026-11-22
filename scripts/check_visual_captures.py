#!/usr/bin/env python3
"""Check real screenshots exist and visual region differs on/off (not aesthetic acceptance)."""
from PIL import Image,ImageChops
from pathlib import Path
import collections
p=Path('build/visual/shots')
labels=['III03_before','III03_warning','III03_active','III03_after',
        'III04_warning','III04_active','III04_after',
        'III05_before','III05_warning','III05_active','III05_after']
images={}
for label in labels:
    files=sorted(p.glob(label+'*.png'))
    assert len(files)>=3,(label,len(files))
    images[label]=[Image.open(f).convert('RGB') for f in files]
    assert all(x.width>=160 and x.height>=192 for x in images[label])
print('EMULATOR_PNG_FILES_PRESENT',sum(len(x) for x in images.values()))
# Actual TIA framebuffer evidence, not just PNG file existence.
# Compare snapshots of ONE fixed room and logical beat. In the variants only
# soundStep's 24-on/40-off visual gate advances; owl, stone, collisions and
# stored PF/cursor geometry are held stable by an explicitly marked Reset stub.
# This verifies that the actual emulator raster visibly changes with the gate.
for id in ['III03','III04','III05']:
    for state,minimum in [('active',500),('warning',200)]:
        im=images[id+'_'+state]
        box=(im[0].width//3,im[0].height//4,2*im[0].width//3,3*im[0].height//4)
        diffs=[]
        for a in im[1:]:
            diff=ImageChops.difference(im[0].crop(box),a.crop(box))
            count=sum(any(px) for px in diff.getdata())
            diffs.append(count)
        assert max(diffs,default=0)>=minimum,(id,state,diffs)
        print('STELLA_REAL_PF_GLIMPSE_PASS',id,state,'changed_pixels_at_least',max(diffs))
print('EMULATOR_CAPTURE_PASS: real-Stella selected room/tick ON-OFF frames; NOT full product joystick replay or artistic certification')
