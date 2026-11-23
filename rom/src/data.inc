; MAIN II: five deterministic visible crown families after Towering Inferno
; compositional research. Only upper PF1/PF2 needles of rows 1..6 change.
; Every stem byte (offset 3..5) and all 15 GeoMap collision maps remain
; byte-identical, as do walls on boundary rows 0/7. U3/S3 remain approved.
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
        dc.b $70,$E0,$0E,$07,$70 ; three-pixel needle crown
LowerToggle:
        dc.b $20,$40,$04,$02,$20 ; slender trunk
SpriteRowIndex:
        dc.b $08,$08,$08,$08,$00,$01,$02,$03,$04,$05,$06,$07,$08,$08
PresenceHUD:
        dc.b $00,$04,$0A,$01
PaletteBG:
        dc.b $A0,$A0,$F0,$82,$84
PalettePF:
        dc.b $B6,$B6,$46,$B4,$B6
PaletteOwl:
        dc.b $0E,$0E,$0C,$0E,$0E  ; COLUP0 shared with M0 marker
PaletteGlyph:
        dc.b $3A,$3A,$38,$36,$3A  ; S3 symbols, valid NTSC TIA orange/amber
RoomAct:
        dc.b $01,$01,$01,$01,$01,$02,$02,$02,$02,$02,$03,$03,$03,$03,$03
RoomPolarity:
        dc.b $00,$01,$00,$01,$00,$01,$01,$01,$01,$00,$00,$01,$00,$00,$01
RoomOwlX:
        dc.b $01,$01,$01,$01,$01,$01,$01,$01,$01,$01,$01,$01,$01,$01,$01
RoomOwlY:
        dc.b $05,$02,$05,$04,$02,$03,$04,$02,$02,$02,$04,$05,$02,$04,$05
RoomOwlDir:
        dc.b $03,$00,$02,$00,$00,$00,$00,$00,$02,$02,$01,$00,$00,$00,$02
RoomStoneX:
        dc.b $04,$04,$04,$04,$04,$04,$04,$04,$04,$04,$04,$04,$04,$04,$04
RoomStoneY:
        dc.b $05,$02,$03,$03,$04,$04,$05,$04,$04,$02,$05,$03,$05,$04,$05
RoomExitX:
        dc.b $08,$08,$08,$08,$08,$08,$08,$08,$08,$08,$08,$08,$08,$08,$08
RoomExitY:
        dc.b $02,$03,$04,$02,$03,$03,$05,$02,$04,$05,$02,$03,$02,$03,$05
RoomGeom:
        dc.b $00,$01,$02,$03,$04,$05,$06,$07,$08,$09,$0A,$0B,$0C,$0D,$0E
RoomGate:
        dc.b $02,$03,$01,$03,$01,$04,$07,$04,$03,$07,$05,$04,$07,$02,$05
; Extra causal tests: bit 0 = owl actually visited stone,
; bit 1 = polarity one, bit 2 = an outstanding delayed echo,
; bit 3 = polarity zero. Only original physical state is checked.
RoomExtra:
        dc.b $00,$01,$08,$00,$08,$08,$02,$08,$01,$08,$03,$08,$08,$05,$03
RoomWarning:
        dc.b $FF,$FF,$FF,$FF,$FF,$FF,$FF,$FF,$FF,$04,$04,$02,$01,$00,$02
RoomActive:
        dc.b $FF,$FF,$FF,$FF,$FF,$FF,$FF,$FF,$FF,$FF,$FF,$FF,$02,$01,$03
GeoMap0:
        dc.b $00,$00,$08,$0A,$02,$04,$00,$00,$1F,$01,$09,$0B,$03,$05,$01,$1F
GeoPF0:
        dc.b $F0,$FF,$FF,$60,$66,$66,$F0,$00,$00,$60,$00,$00,$F0,$00,$07,$60
        dc.b $00,$02,$F0,$E0,$07,$60,$40,$02,$F0,$E0,$00,$60,$40,$00,$F0,$0E
        dc.b $00,$60,$04,$00,$F0,$00,$00,$60,$00,$00,$F0,$FF,$FF,$60,$66,$66
GeoMap1:
        dc.b $00,$08,$00,$04,$00,$10,$04,$00,$1F,$09,$01,$05,$01,$11,$05,$1F
GeoPF1:
        dc.b $F0,$FF,$FF,$60,$66,$66,$F0,$00,$03,$60,$00,$02,$F0,$00,$00,$60
        dc.b $00,$00,$F0,$06,$00,$60,$04,$00,$F0,$00,$00,$60,$00,$00,$F0,$00
        dc.b $30,$60,$00,$20,$F0,$06,$00,$60,$04,$00,$F0,$FF,$FF,$60,$66,$66
GeoMap2:
        dc.b $00,$10,$12,$06,$0C,$14,$0C,$00,$1F,$11,$13,$07,$0D,$15,$0D,$1F
GeoPF2:
        dc.b $F0,$FF,$FF,$60,$66,$66,$F0,$00,$70,$60,$00,$20,$F0,$E0,$70,$60
        dc.b $40,$20,$F0,$E6,$00,$60,$44,$00,$F0,$06,$03,$60,$04,$02,$F0,$06
        dc.b $70,$60,$04,$20,$F0,$06,$03,$60,$04,$02,$F0,$FF,$FF,$60,$66,$66
GeoMap3:
        dc.b $00,$04,$00,$08,$0C,$1C,$08,$00,$1F,$05,$01,$09,$0D,$1D,$09,$1F
GeoPF3:
        dc.b $F0,$FF,$FF,$60,$66,$66,$F0,$0E,$00,$60,$04,$00,$F0,$00,$00,$60
        dc.b $00,$00,$F0,$00,$07,$60,$00,$02,$F0,$0E,$07,$60,$04,$02,$F0,$0E
        dc.b $37,$60,$04,$22,$F0,$00,$07,$60,$00,$02,$F0,$FF,$FF,$60,$66,$66
GeoMap4:
        dc.b $00,$08,$10,$14,$08,$00,$0C,$00,$1F,$09,$11,$15,$09,$01,$0D,$1F
GeoPF4:
        dc.b $F0,$FF,$FF,$60,$66,$66,$F0,$00,$03,$60,$00,$02,$F0,$00,$60,$60
        dc.b $00,$20,$F0,$06,$60,$60,$04,$20,$F0,$00,$03,$60,$00,$02,$F0,$00
        dc.b $00,$60,$00,$00,$F0,$06,$03,$60,$04,$02,$F0,$FF,$FF,$60,$66,$66
GeoMap5:
        dc.b $00,$12,$1A,$14,$0A,$12,$04,$00,$1F,$13,$1B,$15,$0B,$13,$05,$1F
GeoPF5:
        dc.b $F0,$FF,$FF,$60,$66,$66,$F0,$E0,$70,$60,$40,$20,$F0,$E0,$77,$60
        dc.b $40,$22,$F0,$0E,$70,$60,$04,$20,$F0,$E0,$07,$60,$40,$02,$F0,$E0
        dc.b $70,$60,$40,$20,$F0,$0E,$00,$60,$04,$00,$F0,$FF,$FF,$60,$66,$66
GeoMap6:
        dc.b $00,$10,$0A,$02,$1C,$00,$04,$00,$1F,$11,$0B,$03,$1D,$01,$05,$1F
GeoPF6:
        dc.b $F0,$FF,$FF,$60,$66,$66,$F0,$00,$30,$60,$00,$20,$F0,$60,$03,$60
        dc.b $40,$02,$F0,$60,$00,$60,$40,$00,$F0,$06,$33,$60,$04,$22,$F0,$00
        dc.b $00,$60,$00,$00,$F0,$06,$00,$60,$04,$00,$F0,$FF,$FF,$60,$66,$66
GeoMap7:
        dc.b $00,$04,$04,$0A,$0A,$06,$1C,$00,$1F,$05,$05,$0B,$0B,$07,$1D,$1F
GeoPF7:
        dc.b $F0,$FF,$FF,$60,$66,$66,$F0,$06,$00,$60,$04,$00,$F0,$06,$00,$60
        dc.b $04,$00,$F0,$E0,$03,$60,$40,$02,$F0,$E0,$03,$60,$40,$02,$F0,$E6
        dc.b $00,$60,$44,$00,$F0,$06,$73,$60,$04,$22,$F0,$FF,$FF,$60,$66,$66
GeoMap8:
        dc.b $00,$0C,$04,$00,$04,$12,$14,$00,$1F,$0D,$05,$01,$05,$13,$15,$1F
GeoPF8:
        dc.b $F0,$FF,$FF,$60,$66,$66,$F0,$0E,$07,$60,$04,$02,$F0,$0E,$00,$60
        dc.b $04,$00,$F0,$00,$00,$60,$00,$00,$F0,$0E,$00,$60,$04,$00,$F0,$60
        dc.b $30,$60,$40,$20,$F0,$0E,$30,$60,$04,$20,$F0,$FF,$FF,$60,$66,$66
GeoMap9:
        dc.b $00,$08,$04,$0C,$10,$1C,$0C,$00,$1F,$09,$05,$0D,$11,$1D,$0D,$1F
GeoPF9:
        dc.b $F0,$FF,$FF,$60,$66,$66,$F0,$00,$03,$60,$00,$02,$F0,$06,$00,$60
        dc.b $04,$00,$F0,$06,$03,$60,$04,$02,$F0,$00,$60,$60,$00,$20,$F0,$06
        dc.b $63,$60,$04,$22,$F0,$06,$03,$60,$04,$02,$F0,$FF,$FF,$60,$66,$66
GeoMap10:
        dc.b $00,$00,$00,$1E,$04,$04,$10,$00,$1F,$01,$01,$1F,$05,$05,$11,$1F
GeoPF10:
        dc.b $F0,$FF,$FF,$60,$66,$66,$F0,$00,$00,$60,$00,$00,$F0,$00,$00,$60
        dc.b $00,$00,$F0,$EE,$77,$60,$44,$22,$F0,$0E,$00,$60,$04,$00,$F0,$0E
        dc.b $00,$60,$04,$00,$F0,$00,$70,$60,$00,$20,$F0,$FF,$FF,$60,$66,$66
GeoMap11:
        dc.b $00,$00,$10,$08,$18,$04,$00,$00,$1F,$01,$11,$09,$19,$05,$01,$1F
GeoPF11:
        dc.b $F0,$FF,$FF,$60,$66,$66,$F0,$00,$00,$60,$00,$00,$F0,$00,$30,$60
        dc.b $00,$20,$F0,$00,$03,$60,$00,$02,$F0,$00,$33,$60,$00,$22,$F0,$06
        dc.b $00,$60,$04,$00,$F0,$00,$00,$60,$00,$00,$F0,$FF,$FF,$60,$66,$66
GeoMap12:
        dc.b $00,$02,$08,$1A,$04,$08,$14,$00,$1F,$03,$09,$1B,$05,$09,$15,$1F
GeoPF12:
        dc.b $F0,$FF,$FF,$60,$66,$66,$F0,$E0,$00,$60,$40,$00,$F0,$00,$03,$60
        dc.b $00,$02,$F0,$E0,$73,$60,$40,$22,$F0,$06,$00,$60,$04,$00,$F0,$00
        dc.b $03,$60,$00,$02,$F0,$06,$70,$60,$04,$20,$F0,$FF,$FF,$60,$66,$66
GeoMap13:
        dc.b $00,$0A,$18,$18,$08,$06,$0A,$00,$1F,$0B,$19,$19,$09,$07,$0B,$1F
GeoPF13:
        dc.b $F0,$FF,$FF,$60,$66,$66,$F0,$60,$07,$60,$40,$02,$F0,$00,$37,$60
        dc.b $00,$22,$F0,$00,$37,$60,$00,$22,$F0,$00,$07,$60,$00,$02,$F0,$6E
        dc.b $00,$60,$44,$00,$F0,$60,$07,$60,$40,$02,$F0,$FF,$FF,$60,$66,$66
GeoMap14:
        dc.b $00,$00,$00,$12,$02,$08,$02,$00,$1F,$01,$01,$13,$03,$09,$03,$1F
GeoPF14:
        dc.b $F0,$FF,$FF,$60,$66,$66,$F0,$00,$00,$60,$00,$00,$F0,$00,$00,$60
        dc.b $00,$00,$F0,$C0,$60,$60,$40,$20,$F0,$C0,$00,$60,$40,$00,$F0,$00
        dc.b $03,$60,$00,$02,$F0,$C0,$00,$60,$40,$00,$F0,$FF,$FF,$60,$66,$66
GeoMapLo:
        dc.b <GeoMap0,<GeoMap1,<GeoMap2,<GeoMap3,<GeoMap4,<GeoMap5,<GeoMap6,<GeoMap7,<GeoMap8,<GeoMap9,<GeoMap10,<GeoMap11,<GeoMap12,<GeoMap13,<GeoMap14
GeoMapHi:
        dc.b >GeoMap0,>GeoMap1,>GeoMap2,>GeoMap3,>GeoMap4,>GeoMap5,>GeoMap6,>GeoMap7,>GeoMap8,>GeoMap9,>GeoMap10,>GeoMap11,>GeoMap12,>GeoMap13,>GeoMap14
GeoPFLo:
        dc.b <GeoPF0,<GeoPF1,<GeoPF2,<GeoPF3,<GeoPF4,<GeoPF5,<GeoPF6,<GeoPF7,<GeoPF8,<GeoPF9,<GeoPF10,<GeoPF11,<GeoPF12,<GeoPF13,<GeoPF14
GeoPFHi:
        dc.b >GeoPF0,>GeoPF1,>GeoPF2,>GeoPF3,>GeoPF4,>GeoPF5,>GeoPF6,>GeoPF7,>GeoPF8,>GeoPF9,>GeoPF10,>GeoPF11,>GeoPF12,>GeoPF13,>GeoPF14
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
; P0 feedback HUD: authentic black-and-white distinct bitmaps.
CursorIdle:
        dc.b $00,$3C,$42,$81,$81,$42,$3C,$00 ; open circle
CursorAck:
        dc.b $00,$04,$0C,$1C,$38,$70,$E0,$40 ; check mark
CursorDenied:
        dc.b $00,$81,$42,$24,$18,$24,$42,$81 ; blocked X
CursorIntercept:
        dc.b $00,$99,$24,$42,$81,$18,$42,$99 ; broken contradictory mark
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
        dc.b $FF,$FF,$1F,$07,$1F,$FF,$FF,$FF
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

