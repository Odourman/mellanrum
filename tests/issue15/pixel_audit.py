#!/usr/bin/env python3
"""Read genuine Gopher native screenshot RGB and assert U3 B1 + exact S3 bitmaps.
Room injection is diagnostic only, not normal 15-room game-play evidence.
"""
import json,sys
from pathlib import Path
from PIL import Image
from collections import Counter
root=Path(sys.argv[1] if len(sys.argv)>1 else 'build/issue15_gopher_15')
A=list(bytes.fromhex('18 24 42 24 18 24 5A 24'))
B=list(bytes.fromhex('42 66 3C 24 5A 3C 66 42'))
B1=list(bytes.fromhex('18 7E DB F7 F7 FF BD 24'))
colors_g=[(255,152,70),(255,119,54),(234,89,40)]
colors_o=[(255,255,254),(255,255,255),(136,136,136)]
errors=[];matched=0;checked=0;per=[]
for room in range(15):
    img=Image.open(root/f'room_{room:02d}.png').convert('RGB')
    assert img.size==(1026,700),img.size
    act=room//5
    detail=[]
    for name,base,mask,rgb in [('S3A',475,A,colors_g[act]),('S3B',885,B,colors_g[act]),('U3_B1',148,B1,colors_o[act])]:
        ys=[y for y in range(40,630) if any(img.getpixel((x,y))==rgb for x in range(base,base+55))]
        assert ys,(room,name,'missing sprite color')
        top=min(ys)
        cur=0
        for row,m in enumerate(mask):
            for col in range(8):
                x=round(base+(col+0.5)*6.4125)
                y=top+round(row*3.27)+1
                exp=bool(m & (0x80 >> col))
                got=img.getpixel((x,y))==rgb
                checked+=1
                if exp==got:
                    matched+=1;cur+=1
                else:errors.append({'room':room,'item':name,'row':row,'col':col,'expected':exp,'actual':got,'x':x,'y':y})
        detail.append({'glyph':name,'bits_matched':cur,'bits_expected':64,'y_top':top})
    per.append({'room':room,'id':f"{('I','II','III')[act]}-{room%5+1:02d}",'groups':detail})
result={'case':'ISSUE15_REAL_GOPHER_NATIVE_U3B1_S3A_S3B_BITS_15_ROOMS','status':'PASS' if not errors and checked==2880 else 'FAIL','bits':checked,'matched':matched,'mismatches':errors[:30],'per_room':per,'classification':'real Gopher screenshot, original room geometry via DIAGNOSTIC POKE (not full controller replay)','source':'U3 user accepted flipped art; S3 GRAPHICS masks'}
(root/'issue15_pixel_audit.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ('per_room','mismatches')}))
if errors:print('FIRST_ERRORS',errors[:8])
raise SystemExit(bool(errors) or checked!=2880)
