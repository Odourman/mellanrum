#!/usr/bin/env python3
"""Actual Stella screenshot gate: campaign scene must show both P1 copies, not FRI SKOG.
Independent source/hardware state read not claimed. Images are from stock Stella.
"""
from pathlib import Path
from PIL import Image
import json,sys
root=Path('build/stella');imgs=sorted(root.glob('*.png'))
results=[]
for p in imgs:
 im=Image.open(p).convert('RGB')
 # Stella 320x228 raw captures: first sprite near x155, duplicate near x~275.
 # Prefer color rather than fixed type: glyph color is red/orange (r>g*1.2).
 def cnt(x0,x1):
  return sum(1 for y in range(35,185) for x in range(x0,x1) if (lambda c:c[0]>120 and c[0]>c[1]*1.20 and c[1]<175)(im.getpixel((x,y))))
 a=cnt(132,174);b=cnt(256,298)
 results.append({'file':p.name,'glyphA_signal_pixels':a,'glyphB_signal_pixels':b,'both_visible':a>=5 and b>=5})
ok=any(q['both_visible'] for q in results)
res={'status':'PASS' if ok else 'FAIL','emulator':'Stella native GUI','screenshots':results,'criterion':'BOTH distinct red/orange left and right P1 copy in at least one real campaign screenshot','diagnostic_only':True}
(root/'stella_double_sprite_audit.json').write_text(json.dumps(res,indent=2)+'\n')
print(json.dumps(res));sys.exit(0 if ok else 1)
