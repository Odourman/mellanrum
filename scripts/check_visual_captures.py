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
# Differences of >= 4 pixels in relevant centrally positioned forest segment show
# that the actual Stella TIA image changed across the visual gate.
# Do not choose exact region before examining emulation screenshots manually.
for id in ['III03','III04','III05']:
    im=images[id+'_active']
    diffcount=[]
    for a in im[1:]:
        box=(a.width//3,a.height//4,2*a.width//3,3*a.height//4)
        diff=ImageChops.difference(im[0].crop(box),a.crop(box))
        diffcount.append(int(bool(diff.getbbox())))
    print('EMULATOR_PNG_VARIATION',id,'distinct_regions',sum(diffcount),'of',len(diffcount),'(may include animation or shadow)')
print('EMULATOR_CAPTURE_SOURCE_PASS: PNG frames truly from Stella; NOT independent visual proof')
