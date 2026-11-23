; BASELINE: scripts/generate_rom_data.py; U3/S3/Presence B overlay: issue15/build_issue15.py
; EXACT source geometry: V5.1 rooms.json; PF and bitmaps: GRAPHICS V5.1.
; Exact owl U3 + glyph S3 from GRAPHICS U3 horizontal mirror + MEL-046 source.
DeltaX:
        dc.b $01,$00,$FF,$00
DeltaY:
        dc.b $00,$01,$00,$FF
TurnOffset:
        dc.b $00,$01,$03,$02
BitMask:
        dc.b $01,$02,$04,$08,$10
GroupBase:
        dc.b $00,$05,$0A,$0F,$14,$19,$1E,$23
PFBase:
        dc.b $00,$06,$0C,$12,$18,$1E,$24,$2A
UpperPFOffset:
        dc.b $00,$01,$01,$02,$02
LowerPFOffset:
        dc.b $03,$04,$04,$05,$05
UpperToggle:
        dc.b $50,$A0,$0A,$05,$50
LowerToggle:
        dc.b $60,$60,$06,$06,$60
SpriteRowIndex:
        dc.b $08,$08,$08,$08,$00,$01,$02,$03,$04,$05,$06,$07,$08,$08
PresenceHUD:
        dc.b $00,$04,$0A,$01
PaletteBG:
        dc.b $A0,$A0,$F0,$0C,$80
PalettePF:
        dc.b $B6,$B6,$B6,$B6,$B6
PaletteOwl:
        dc.b $0E,$0E,$0C,$06,$0E  ; COLUP0 shared with M0 marker
PaletteGlyph:
        dc.b $3A,$3A,$38,$36,$3A  ; S3 symbols, valid NTSC TIA orange/amber
SoundControl0:
        dc.b $08,$08,$06,$0A
SoundControl1:
        dc.b $06,$06,$0C,$04
SoundPitch0:
        dc.b $0F,$0C,$0F,$0D
SoundPitch1:
        dc.b $15,$16,$1A,$1C
RoomAct:
        dc.b $01,$01,$01,$01,$01,$02,$02,$02,$02,$02,$03,$03,$03,$03,$03
RoomPolarity:
        dc.b $00,$00,$01,$00,$01,$00,$01,$00,$01,$00,$00,$01,$00,$01,$00
RoomOwlX:
        dc.b $01,$01,$01,$01,$01,$01,$01,$01,$01,$01,$01,$01,$01,$01,$01
RoomOwlY:
        dc.b $03,$02,$04,$03,$03,$03,$02,$04,$03,$03,$03,$02,$04,$03,$03
RoomOwlDir:
        dc.b $00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00
RoomStoneX:
        dc.b $04,$04,$04,$04,$04,$04,$04,$04,$04,$04,$04,$04,$04,$04,$04
RoomStoneY:
        dc.b $03,$04,$03,$02,$02,$03,$04,$03,$02,$02,$03,$04,$03,$02,$02
RoomExitX:
        dc.b $08,$08,$08,$08,$08,$08,$08,$08,$08,$08,$08,$08,$08,$08,$08
RoomExitY:
        dc.b $03,$02,$04,$03,$03,$03,$02,$04,$03,$03,$03,$02,$04,$03,$03
RoomGeom:
        dc.b $00,$01,$02,$03,$04,$00,$01,$02,$03,$04,$00,$01,$02,$03,$04
RoomWarning:
        dc.b $FF,$FF,$FF,$FF,$FF,$FF,$FF,$FF,$FF,$04,$04,$02,$01,$00,$02
RoomActive:
        dc.b $FF,$FF,$FF,$FF,$FF,$FF,$FF,$FF,$FF,$FF,$FF,$FF,$02,$01,$03
GeoMap0:
        dc.b $00,$00,$04,$04,$08,$00,$00,$00,$1F,$01,$05,$05,$09,$01,$01,$1F
GeoPF0:
        dc.b $F0,$FF,$FF,$60,$66,$66,$F0,$00,$00,$60,$00,$00,$F0,$0B,$00,$60
        dc.b $06,$00,$F0,$0B,$00,$60,$06,$00,$F0,$00,$0D,$60,$00,$06,$F0,$00
        dc.b $00,$60,$00,$00,$F0,$00,$00,$60,$00,$00,$F0,$FF,$FF,$60,$66,$66
GeoMap1:
        dc.b $00,$00,$04,$08,$02,$04,$00,$00,$1F,$01,$05,$09,$03,$05,$01,$1F
GeoPF1:
        dc.b $F0,$FF,$FF,$60,$66,$66,$F0,$00,$00,$60,$00,$00,$F0,$0B,$00,$60
        dc.b $06,$00,$F0,$00,$0D,$60,$00,$06,$F0,$B0,$00,$60,$60,$00,$F0,$0B
        dc.b $00,$60,$06,$00,$F0,$00,$00,$60,$00,$00,$F0,$FF,$FF,$60,$66,$66
GeoMap2:
        dc.b $00,$00,$0C,$00,$04,$08,$00,$00,$1F,$01,$0D,$01,$05,$09,$01,$1F
GeoPF2:
        dc.b $F0,$FF,$FF,$60,$66,$66,$F0,$00,$00,$60,$00,$00,$F0,$0B,$0D,$60
        dc.b $06,$06,$F0,$00,$00,$60,$00,$00,$F0,$0B,$00,$60,$06,$00,$F0,$00
        dc.b $0D,$60,$00,$06,$F0,$00,$00,$60,$00,$00,$F0,$FF,$FF,$60,$66,$66
GeoMap3:
        dc.b $00,$08,$00,$0C,$08,$00,$00,$00,$1F,$09,$01,$0D,$09,$01,$01,$1F
GeoPF3:
        dc.b $F0,$FF,$FF,$60,$66,$66,$F0,$00,$0D,$60,$00,$06,$F0,$00,$00,$60
        dc.b $00,$00,$F0,$0B,$0D,$60,$06,$06,$F0,$00,$0D,$60,$00,$06,$F0,$00
        dc.b $00,$60,$00,$00,$F0,$00,$00,$60,$00,$00,$F0,$FF,$FF,$60,$66,$66
GeoMap4:
        dc.b $00,$00,$04,$18,$04,$04,$00,$00,$1F,$01,$05,$19,$05,$05,$01,$1F
GeoPF4:
        dc.b $F0,$FF,$FF,$60,$66,$66,$F0,$00,$00,$60,$00,$00,$F0,$0B,$00,$60
        dc.b $06,$00,$F0,$00,$DD,$60,$00,$66,$F0,$0B,$00,$60,$06,$00,$F0,$0B
        dc.b $00,$60,$06,$00,$F0,$00,$00,$60,$00,$00,$F0,$FF,$FF,$60,$66,$66
GeoMapLo:
        dc.b <GeoMap0,<GeoMap1,<GeoMap2,<GeoMap3,<GeoMap4
GeoMapHi:
        dc.b >GeoMap0,>GeoMap1,>GeoMap2,>GeoMap3,>GeoMap4
GeoPFLo:
        dc.b <GeoPF0,<GeoPF1,<GeoPF2,<GeoPF3,<GeoPF4
GeoPFHi:
        dc.b >GeoPF0,>GeoPF1,>GeoPF2,>GeoPF3,>GeoPF4
BlankSprite:
        dc.b $00,$00,$00,$00,$00,$00,$00,$00,$00
; U3 mirrored horizontally with vertical beak; user-approved B0/B1/B2.
OwlB0:
        dc.b $24,$7E,$7E,$F7,$F7,$DB,$7E,$18,$00
OwlB1:
        dc.b $24,$BD,$FF,$F7,$F7,$DB,$7E,$18,$00
OwlB2:
        dc.b $24,$FF,$FF,$F7,$F7,$DB,$7E,$18,$00
OwlFrameLo:
        dc.b <OwlB0,<OwlB1,<OwlB2
OwlFrameHi:
        dc.b >OwlB0,>OwlB1,>OwlB2
CursorIdle:
        dc.b $C3,$81,$00,$00,$00,$00,$81,$C3,$00
CursorAck:
        dc.b $C3,$81,$00,$18,$18,$00,$81,$C3,$00
CursorDenied:
        dc.b $81,$42,$24,$18,$18,$24,$42,$81,$00
CursorIntercept:
        dc.b $C3,$81,$00,$18,$24,$00,$81,$C3,$00
CursorSpriteLo:
        dc.b <CursorIdle,<CursorAck,<CursorDenied,<CursorIntercept
CursorSpriteHi:
        dc.b >CursorIdle,>CursorAck,>CursorDenied,>CursorIntercept
TitleLeftPF0:
        dc.b $00,$40,$C0,$C0,$40,$40,$00
TitleRightPF0:
        dc.b $00,$40,$D0,$D0,$D0,$50,$00
TitleLeftPF1:
        dc.b $00,$BA,$A2,$B2,$A2,$BB,$00
TitleRightPF1:
        dc.b $00,$B2,$AA,$B2,$AA,$AB,$00
TitleLeftPF2:
        dc.b $00,$84,$44,$C4,$44,$5D,$00
TitleRightPF2:
        dc.b $00,$15,$1D,$1D,$15,$15,$00
; GRAPHICS Presence B 3-state PF2 OR/AND, each eight rows,
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
        dc.b $FF,$FF,$1F,$1F,$0F,$3F,$FF,$FF

; USER-PREFERRED S3 GRAPHICS (MEL-046), exact 8 x 8 masks, top-down reversed.
; A = Minnesskärva (stone function), B = Omvänd skog (exit function).
GlyphA:
        dc.b $24,$5A,$24,$18,$24,$42,$24,$18,$00
GlyphB:
        dc.b $42,$66,$3C,$5A,$24,$3C,$66,$42,$00
MarkerWidth:
        dc.b $00,$10,$20,$30 ; M0 widths: normal=1, ack=2, denied=4, intercept=8 pixels
