#!/usr/bin/env python3
"""Conservative native screenshot check: title vs real active game, two disjoint non-BG glyph regions."""
import json,sys
from pathlib import Path
from PIL import Image
p=Path(sys.argv[1] if len(sys.argv)>1 else 'build/issue15_stella')
imgs=[]
for n in sorted(p.glob('*.png')):
  im=Image.open(n).convert('RGB');imgs.append((n.name,im))
assert len(imgs)>=2,len(imgs)
found=[]
for name,im in imgs:
  w,h=im.size
  pixels=im.load();left=0;right=0
  # Stella's 320x228 image maps scaled sigils at x approximately 150/255.
  for y in range(int(h*0.24),int(h*0.85)):
    for x in range(int(w*0.42),int(w*0.52)):
      r,g,b=pixels[x,y]
      left+=int(r>g*1.2 and r>b*1.3 and r>110)
    for x in range(int(w*0.82),int(w*0.92)):
      r,g,b=pixels[x,y]
      right+=int(r>g*1.2 and r>b*1.3 and r>110)
  found.append({'file':name,'w':w,'h':h,'left_redorange':left,'right_redorange':right})
status='PASS' if any(v['left_redorange']>10 and v['right_redorange']>10 for v in found) else 'INCONCLUSIVE'
res={'status':status,'screenshots':found,'scope':'native Stella screenshot; broad presence test, not pixel-perfect proof'}
(p/'stella_pixel_check.json').write_text(json.dumps(res,indent=2)+'\n')
print(json.dumps(res))
raise SystemExit(0 if status=='PASS' else 1)
