#!/usr/bin/env python3
"""New source/6507 developer checks for title and visual Presence.
Does NOT replace screenshot review in Stella/Gopher2600 or independent verification.
"""
from pathlib import Path
import re,sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from cpu_trace import load
from check_rom_vs_model import new_room,call

asm=(ROOT/'rom/src/main.asm').read_text()
data=(ROOT/'rom/src/data.inc').read_text()
assert 'TitleMEL:' not in data and 'TitleKAM:' not in data and 'TitleFRI:' not in data
assert 'TitleLeftPF0' in asm and 'TitleRightPF2' in asm
assert "lda SWCHB" in asm and "and #$40" in asm and "bne StartCampaign" in asm
assert "TitleFreeSelected" not in asm and "TitleMenuLeftPF2" not in data and "TitleMenuRightPF2" not in data

def tab(name):
    m=re.search(r'^'+re.escape(name)+r':\s*\n((?:\s+dc\.b [^\n]+\n)+)',data,re.M)
    assert m,name
    return [int(s[1:],16) for s in re.findall(r'\$[A-Fa-f0-9]{2}',m.group(1))]
def r4(n):return int(f'{n:04b}'[::-1],2)
def bits(p):
    a,b,c=p
    return ''.join(f'{n:04b}' for n in [r4(a>>4),b>>4,b&15,r4(c&15),r4(c>>4)])

src_font={'M':['101','111','111','101','101'],'E':['111','100','110','100','111'],
'L':['100','100','100','100','111'],'A':['010','101','111','101','101'],
'N':['101','111','111','111','101'],'R':['110','101','110','101','101'],
'U':['101','101','101','101','111']}
for y in range(7):
    got=bits([tab('TitleLeftPF'+str(i))[y] for i in range(3)])+bits([tab('TitleRightPF'+str(i))[y] for i in range(3)])
    want='00'+''.join((src_font[ch][y-1] if 1<=y<=5 else '000')+'0' for ch in 'MELLANRUM')+'00'
    assert got==want,(y,got,want)
assert all(k not in data for k in ('TitleMenuLeftPF2:', 'TitleMenuRightPF2:', 'TitleMenuY:'))
assert not any(k in data for k in ('TitleWordLo:', 'TitleWordHi:','TitleKAM:','TitleFRI:'))

# Console SELECT is covered by check_input.py; check video title in real CPU model.
c=load(str(ROOT/'build/mellanrum_ntsc.bin'),str(ROOT/'build/mellanrum_ntsc.sym'))
c.run_to_frame(4)
assert all(t==19912 for t,_,_ in c.frame_samples[1:]),c.frame_samples
assert c.ram('mode')==0
c.input_swchb=0xfd;c.run_to_frame(6);assert c.ram('mode')==0
c.input_swchb=0xbf;c.run_to_frame(8);assert c.ram('mode')==0
assert c.frame_samples[-1][0]==19912
print('TITLE_EXACT_WORD_PASS: 9 connected glyphs, no other textual words or mode icons, SELECT no-op in title; 262 scanlines developer CPU')

# Shadow is gated by the precise original state machine. Cases include all three active rooms.
for room,warn,active1,after in [(12,1,2,4),(13,0,1,3),(14,2,3,5)]:
    for tick,state in [(max(0,warn-1),0 if warn>0 else 1),(warn,1),(active1,2),(active1+1,2),(after,3)]:
        c=new_room(room);c.write(c.syms['beat'],tick);call(c,'UpdatePresence')
        assert c.ram('presence')==state,(room,tick,c.ram('presence'),state)
        c.write(c.syms['soundStep'],0);call(c,'SetShadowVisibility')
        assert c.ram('shadowOn')==(state if state in (1,2) else 0),(room,tick,'gate ON')
        c.write(c.syms['soundStep'],33);call(c,'SetShadowVisibility')
        assert c.ram('shadowOn')==0,(room,tick,'gate OFF')
        c.write(c.syms['soundStep'],0);call(c,'SetShadowVisibility')
        before=(bytes(c.mem[0x80:0x80+48]),bytes(c.mem[0xB0:0xB8]))
        pf2=[]
        oldwrite=c.write
        def logwrite(addr,val):
            if addr==0x0F:pf2.append((c.ram('rowIndex'),val))
            oldwrite(addr,val)
        c.write=logwrite
        call(c,'RenderPlay',limit=150000)
        afterrender=(bytes(c.mem[0x80:0x80+48]),bytes(c.mem[0xB0:0xB8]))
        assert before==afterrender,(room,tick,'render mutated physics/PF model')
        assert len(pf2)>=16,(room,tick,'no PF2 scanline updates')
        if state==2:
            # Compare exact same room/tick in invisible interval. No gameplay state changed.
            d=new_room(room);d.write(d.syms['beat'],tick);call(d,'UpdatePresence');d.write(d.syms['soundStep'],33);call(d,'SetShadowVisibility')
            normal=[];old=d.write
            def lognormal(addr,val):
                if addr==0x0F:normal.append((d.ram('rowIndex'),val))
                old(addr,val)
            d.write=lognormal;call(d,'RenderPlay',limit=150000)
            assert pf2!=normal,(room,tick,'shadow not visible at PF2 TIA register')
print('PRESENCE_RENDER_PASS: exact windows III-03/04/05; visual register delta; pfbuf and collision map invariant')
