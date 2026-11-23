#!/usr/bin/env python3
from pathlib import Path
import json, re
R=Path(__file__).resolve().parent
src=(R/'diagnostics/issue14/rom/src/main.asm').read_text()
data=(R/'diagnostics/issue14/rom/src/data.inc').read_text()
def rep(old,new):
 global src
 assert old in src,old[:100]
 src=src.replace(old,new,1)
def subst_data(old,new):
 global data
 assert old in data,old[:100]
 data=data.replace(old,new,1)
# Turn the proven isolated P1/TIA diagnosis into normal game source.
src=src.replace('; MELLANRUM: SKOGEN SOM LYSSNAR','; MELLANRUM: SKOGEN SOM LYSSNAR - ISSUE #15 USER-AUTHORIZED CANDIDATE',1)
src=src.replace('        sta WSYNC         ; DIAGNOSTIC ONLY: +1 WSYNC isolate 261 -> 262','        sta WSYNC         ; NTSC raster correction: verified native Gopher 262, see #12',1)
src=src.replace('; X is hardware index: 0=P0 owl, 1=P1 cursor, 2=M0 exit, 4=BL stone.','; X is TIA index: 0=P0 U3 owl, 1=P1 both S3 sigils, 2=M0 cursor; BL spare.',1)
src=src.replace('        sta NUSIZ1       ; DIAGNOSTIC wide two-copy P1 (64 color clocks)','        sta NUSIZ1       ; two far-separated S3 symbols, x=71 and x=135',1)
src=src.replace('; DIAGNOSTIC keep original pine green across all acts','; V5.1 pine green across all acts and phase states',1)
src=src.replace('        lda #$B6          ; V5.1 pine green across all acts and phase states\n        sta COLUPF','        lda PalettePF,x\n        sta COLUPF',1)
src=src.replace('        lda PaletteCursor,x\n        sta COLUP1','        lda PaletteGlyph,x\n        sta COLUP1',1)
# U3, three valid frames sourced from user-approved 2026-11-23 mirrored vertical-beak art. Selector is visual only.
old='''        lda rowIndex
        cmp owlY
        bne NoOwlOnRow
        lda #<OwlSprite
        sta sprite0Ptr
        lda #>OwlSprite
        sta sprite0Ptr+1
        jmp OwlRowChosen
NoOwlOnRow:
        lda #<BlankSprite
        sta sprite0Ptr
        lda #>BlankSprite
        sta sprite0Ptr+1
OwlRowChosen:'''
new='''        lda rowIndex
        cmp owlY
        bne NoOwlOnRow
        ; 72 NTSC frames: B1 x6, B2 x6, B1 x6, B0 x54.
        ; Beat timer counts downward; do not modify actual owl AI timing.
        lda beatFrames
        cmp #55
        bcc OwlB0Frame
        cmp #61
        bcc OwlB1Frame
        cmp #67
        bcc OwlB2Frame
OwlB1Frame:
        ldx #1
        bne OwlFrameReady
OwlB2Frame:
        ldx #2
        bne OwlFrameReady
OwlB0Frame:
        ldx #0
OwlFrameReady:
        lda OwlFrameLo,x
        sta sprite0Ptr
        lda OwlFrameHi,x
        sta sprite0Ptr+1
        jmp OwlRowChosen
NoOwlOnRow:
        lda #<BlankSprite
        sta sprite0Ptr
        lda #>BlankSprite
        sta sprite0Ptr+1
OwlRowChosen:'''
rep(old,new)
# Presence B: pick graphics frame with existing 24-on/40-off cadence, no gameplay change.
old='''SetShadowVisibility:
        lda #0
        sta shadowOn
        lda mode
        cmp #1
        bne ShadowGateDone
        lda presence
        cmp #1
        beq ShadowGateTime
        cmp #2
        bne ShadowGateDone
ShadowGateTime:
        sta shadowOn
        lda soundStep
        and #$3F
        cmp #24
        bcc ShadowGateDone
        lda #0
        sta shadowOn
ShadowGateDone:
        rts'''
new='''SetShadowVisibility:
        lda #0
        sta shadowOn
        sta moveTemp       ; render-only mask frame offset 0/8/16; safe scratch
        lda mode
        cmp #1
        bne ShadowGateDone
        lda presence
        cmp #1
        beq ShadowGateTime
        cmp #2
        bne ShadowGateDone
ShadowGateTime:
        sta shadowOn      ; 1 warning, 2 active: unchanged original roles
        lda soundStep
        and #$3F
        cmp #24
        bcs ShadowGateOff
        and #$18          ; 0/8/16 -> GRAPHICS Presence B0/B1/B2
        sta moveTemp
        rts
ShadowGateOff:
        lda #0
        sta shadowOn
ShadowGateDone:
        rts'''
rep(old,new)
rep('''        sta rowIndex
        sta pfIndex
NextRow:''','''        sta rowIndex
        sta pfIndex
        lda moveTemp
        sta workY          ; render-only PF2 frame index, 0/8/16
NextRow:''')
# No additional cycles in the PF2 register update itself vs original.
rep('''        ldx shadowOn
        beq NoCrownShadow
        ldx rowIndex
        ora ShadowCrownOr,x''','''        ldx shadowOn
        beq NoCrownShadow
        ldx workY
        ora ShadowCrownOr,x''')
rep('''MarkerGateDone:
        ; sixth crown line: BL not used, leave P0 owl and PF tree graphics.
        sta WSYNC''','''MarkerGateDone:
        lda workY
        sta candidateD    ; current mask frame index for the forthcoming stem
        inc workY         ; next crown row index; no extra work in hot PF2 scanline
        ; sixth crown line: BL unused; P0 real U3 owl retained.
        sta WSYNC''')
rep('''        ldx rowIndex
        ora ShadowStemOr,x''','''        ldx candidateD
        ora ShadowStemOr,x''')
# TIA source path for cartridge file and new art source
src=src.replace(' ; DIAGNOSTIC',' ; ISSUE15',2)
# Replace 9-byte old Owl with three approved U3 frames. S3 has precise user-preferred original symmetric masks.
subst_data('''OwlSprite:
        dc.b $A5,$5A,$7E,$FF,$DB,$FF,$7E,$24,$00''','''; U3 mirrored horizontally with vertical beak; user-approved B0/B1/B2.
OwlB0:
        dc.b $24,$7E,$7E,$F7,$F7,$DB,$7E,$18,$00
OwlB1:
        dc.b $24,$BD,$FF,$F7,$F7,$DB,$7E,$18,$00
OwlB2:
        dc.b $24,$FF,$FF,$F7,$F7,$DB,$7E,$18,$00
OwlFrameLo:
        dc.b <OwlB0,<OwlB1,<OwlB2
OwlFrameHi:
        dc.b >OwlB0,>OwlB1,>OwlB2''')
subst_data('''; ISSUE #14 DIAGNOSTIC ONLY; synthetic/noncanonical placeholder symbols!
; Same probe bytes as MAIN #7087704443; not GRAPHICS Brytning/Kretsrest.
GlyphA:
        dc.b $00,$18,$24,$5A,$BD,$5A,$24,$18,$00
GlyphB:
        dc.b $00,$C3,$81,$A5,$BD,$A5,$81,$C3,$00''','''; USER-PREFERRED S3 GRAPHICS (MEL-046), exact 8 x 8 masks, top-down reversed.
; A = Minnesskärva (stone function), B = Omvänd skog (exit function).
GlyphA:
        dc.b $24,$5A,$24,$18,$24,$42,$24,$18,$00
GlyphB:
        dc.b $42,$66,$3C,$5A,$24,$3C,$66,$42,$00''')
# Preserve trees green in all act & phase combinations; also light-scene readable glyph/OWL contrasts.
subst_data('''PalettePF:
        dc.b $B6,$B6,$E6,$84,$0C''','''PalettePF:
        dc.b $B6,$B6,$B6,$B6,$B6''')
subst_data('''PaletteOwl:
        dc.b $0E,$0E,$0C,$00,$0E
PaletteCursor:
        dc.b $26,$26,$36,$46,$4A''','''PaletteOwl:
        dc.b $0E,$0E,$0C,$06,$0E  ; COLUP0 shared with M0 marker
PaletteGlyph:
        dc.b $3A,$3A,$38,$36,$3A  ; S3 symbols, valid NTSC TIA orange/amber''')
# Replace fixed original silhouette with user's 3-state B animation exact PF2 OR and AND bytes.
old='''ShadowCrownOr:
        dc.b $00,$00,$33,$15,$13,$00,$00,$00
ShadowCrownAnd:
        dc.b $FF,$FF,$3F,$1F,$3F,$FF,$FF,$FF
ShadowStemOr:
        dc.b $00,$00,$11,$11,$10,$20,$00,$00
ShadowStemAnd:
        dc.b $FF,$FF,$1F,$1F,$1F,$3F,$FF,$FF'''
new='''; GRAPHICS Presence B 3-state PF2 OR/AND, each eight rows,
; soundStep 0-7 B0, 8-15 B1, 16-23 B2, then 40 off frames.
ShadowCrownOr:
        dc.b $00,$00,$31,$11,$13,$00,$00,$00 ; B0
        dc.b $00,$00,$33,$15,$13,$00,$00,$00 ; B1
        dc.b $00,$00,$32,$13,$11,$00,$00,$00 ; B2
ShadowCrownAnd:
        dc.b $FF,$FF,$3F,$1F,$3F,$FF,$FF,$FF
        dc.b $FF,$FF,$3F,$1F,$3F,$FF,$FF,$FF
        dc.b $FF,$FF,$3F,$0F,$3F,$FF,$FF,$FF
ShadowStemOr:
        dc.b $00,$00,$10,$11,$10,$20,$00,$00 ; B0
        dc.b $00,$00,$11,$11,$10,$20,$00,$00 ; B1
        dc.b $00,$00,$11,$10,$10,$20,$00,$00 ; B2
ShadowStemAnd:
        dc.b $FF,$FF,$1F,$1F,$1F,$3F,$FF,$FF
        dc.b $FF,$FF,$1F,$1F,$1F,$3F,$FF,$FF
        dc.b $FF,$FF,$1F,$1F,$0F,$3F,$FF,$FF'''
subst_data(old,new)
# Make data fully declarative about canon overlay. Legacy generator still validates baseline only;
# exact overlay must be reproduced by this script.
data=data.replace('; AUTOGENERATED by scripts/generate_rom_data.py. DO NOT EDIT.','; BASELINE: scripts/generate_rom_data.py; U3/S3/Presence B overlay: issue15/build_issue15.py')
data=data.replace('; The mask atlas contains exactly 25 8x8 images; selected P0/P1 masks follow.','; Exact owl U3 + glyph S3 from GRAPHICS U3 horizontal mirror + MEL-046 source.')
(R/'rom/src/main.asm').write_text(src)
(R/'rom/src/data.inc').write_text(data)
print('Created issue15 ROM source',len(src),'asm chars, data',len(data),'chars')
