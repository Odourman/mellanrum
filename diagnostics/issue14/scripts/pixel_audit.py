#!/usr/bin/env python3
"""Compare ORIGINAL Gopher PNG color-bitmap pixels to immutable synthetic probe masks.
No OCR or hand estimates; rows measured from actual emulator raster via pixel sampling.
Issue14 diagnostic only (not canonical GRAPHICS designs).
"""
from pathlib import Path
from PIL import Image
import argparse,json
p=argparse.ArgumentParser();p.add_argument('--input',default='build/gopher_15');p.add_argument('--output',default='build/gopher_15/pixel_audit.json');args=p.parse_args()
root=Path(args.input);rooms=json.loads((Path(__file__).resolve().parents[1]/'rooms.json').read_text())
A=[0x18,0x24,0x5A,0xBD,0x5A,0x24,0x18]
B=[0xC3,0x81,0xA5,0xBD,0xA5,0x81,0xC3]
OWL=[0x24,0x7e,0xff,0xdb,0xff,0x7e,0x5a,0xa5]
colors=[(199,107,33),(234,89,40),(236,51,51)]
# Gopher2600 saved 1026px fullscreen: TIA colorclocks map to ~6.41px each.
# Left P1 copied glyph begins native colorclock 74, right begins at 138.
def center(base,idx):return round(base+(idx+.5)*6.4125)
def ycenter(top,idx):return top+round(idx*3.27)+1
checks=[];errors=[]
for n,r in enumerate(rooms):
 img=Image.open(root/f'room_{n:02d}.png').convert('RGB')
 glyph_color=colors[n//5]
 for typ,base,masks in [('A',475,A),('B',885,B)]:
  xvals=range(base,base+52)
  ys=[y for y in range(40,630) if any(img.getpixel((x,y))==glyph_color for x in xvals)]
  if not ys:errors.append({'room':n,'item':typ,'error':'no colored pixels'});continue
  top=min(ys)
  for row,m in enumerate(masks):
   for col in range(8):
    expected=(m>>(7-col))&1
    actual=int(img.getpixel((center(base,col),ycenter(top,row)))==glyph_color)
    checks.append({'room':n,'item':typ,'row':row,'col':col,'pass':actual==expected})
    if actual!=expected:errors.append({'room':n,'item':typ,'row':row,'col':col,'actual':actual,'expected':expected,'x':center(base,col),'y':ycenter(top,row)})
 # full original P0 owl 8x8 from diagnostics copied unchanged
 owl_color=(255,255,254) if n<5 else (255,255,255) if n<10 else (6,6,6)
 ys=[y for y in range(40,630) if any(img.getpixel((x,y))==owl_color for x in range(148,200))]
 if not ys:errors.append({'room':n,'item':'OWL','error':'no owl sprite detected'});continue
 top=min(ys)
 for row,m in enumerate(OWL):
  for col in range(8):
   expected=(m>>(7-col))&1
   actual=int(img.getpixel((center(148,col),ycenter(top,row)))==owl_color)
   checks.append({'room':n,'item':'OWL','row':row,'col':col,'pass':actual==expected})
   if actual!=expected:errors.append({'room':n,'item':'OWL','row':row,'col':col,'actual':actual,'expected':expected,'x':center(148,col),'y':ycenter(top,row)})
result={'test':'GOPHER2600_NATIVE_P1_A_B_AND_P0_OWL_PIXEL_AUDIT','status':'PASS' if not errors else 'FAIL','tested_rooms':15,'bits_checked':len(checks),'bits_matched':sum(x['pass'] for x in checks),'mismatch_count':len(errors),'mismatches':errors[:60],'scope':'synthetic not canonical glyphs; original owl bitmap; test room state injected via POKE'}
Path(args.output).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k!='mismatches'}));print('FIRST_MISMATCHES',errors[:12]);raise SystemExit(bool(errors))
