MirrorX:
        dc.b $00,$01,$02,$03,$04,$04,$03,$02,$01,$00
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
        dc.b $08,$08,$00,$01,$02,$03,$04,$05,$06,$07 ; old location, padding for beam layout
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
        dc.b $01,$01,$01,$01,$01,$02,$02,$02,$02,$02,$03,$03,$03,$03,$03,$03,$03,$03,$03
RoomPolarity:
        dc.b $00,$01,$00,$00,$01,$01,$00,$01,$00,$01,$00,$01,$01,$01,$00,$00,$01,$00,$00
RoomOwlY:
        dc.b $03,$01,$06,$04,$01,$01,$01,$03,$06,$05,$01,$06,$06,$04,$05,$04,$05,$02,$04
RoomOwlDir:
        dc.b $00,$03,$03,$00,$00,$01,$03,$00,$02,$00,$00,$02,$02,$00,$01,$01,$00,$00,$00
RoomStoneY:
        dc.b $01,$06,$06,$04,$03,$05,$03,$01,$06,$04,$01,$06,$06,$06,$01,$05,$03,$05,$04
RoomExitY:
        dc.b $03,$01,$03,$02,$05,$01,$01,$02,$02,$04,$01,$01,$02,$06,$05,$02,$03,$02,$03
RoomPresence:
        dc.b $02,$02,$02,$02,$02,$02,$02,$02,$02,$02,$00,$00,$00,$00,$00,$02,$02,$02,$02
CommonTopPF:
        dc.b $F0,$FF,$FF,$60,$66,$66
RoomData0:
        dc.b $00,$02,$10,$04,$06,$08,$1A,$00,$00,$01,$02,$03,$04,$05
RoomData1:
        dc.b $00,$14,$0E,$1E,$08,$10,$0A,$00,$06,$07,$08,$09,$0A,$0B
RoomData2:
        dc.b $00,$0A,$18,$08,$12,$0E,$00,$00,$0B,$0C,$09,$0D,$07,$0E
RoomData3:
        dc.b $00,$1E,$04,$12,$00,$10,$0C,$00,$0F,$02,$10,$0E,$0A,$11
RoomData4:
        dc.b $00,$1C,$1C,$0A,$1A,$1C,$0C,$00,$12,$12,$0B,$13,$12,$14
RoomData5:
        dc.b $00,$10,$16,$1E,$08,$02,$1C,$00,$01,$15,$16,$04,$00,$17
RoomData6:
        dc.b $00,$08,$0E,$06,$02,$16,$12,$00,$09,$18,$19,$1A,$1B,$1C
RoomData7:
        dc.b $00,$08,$08,$18,$0E,$18,$0C,$00,$09,$09,$0C,$07,$0C,$14
RoomData8:
        dc.b $00,$18,$14,$14,$12,$16,$04,$00,$1D,$1E,$1E,$1C,$1F,$02
RoomData9:
        dc.b $00,$0C,$04,$0C,$08,$0C,$16,$00,$14,$20,$14,$09,$14,$21
RoomData10:
        dc.b $00,$00,$18,$1C,$18,$1A,$06,$00,$0E,$22,$17,$22,$05,$03
RoomData11:
        dc.b $00,$04,$0C,$0A,$12,$0E,$04,$00,$20,$14,$0B,$10,$07,$20
RoomData12:
        dc.b $00,$0A,$1C,$06,$02,$16,$08,$00,$0B,$23,$24,$00,$25,$09
RoomData13:
        dc.b $00,$1E,$1C,$1E,$0C,$1E,$08,$00,$26,$27,$26,$11,$26,$04
RoomData14:
        dc.b $00,$04,$1E,$1C,$0E,$1C,$1E,$00,$02,$28,$29,$2A,$29,$28
RoomData15:
        dc.b $00,$00,$00,$1E,$04,$04,$10,$00,$0E,$0E,$16,$02,$02,$01
RoomData16:
        dc.b $00,$00,$10,$08,$18,$04,$00,$00,$0E,$0A,$09,$2B,$20,$0E
RoomData17:
        dc.b $00,$02,$08,$1A,$04,$08,$14,$00,$00,$09,$2C,$20,$09,$2D
RoomData18:
        dc.b $00,$0A,$18,$18,$08,$06,$0A,$00,$2E,$1D,$1D,$04,$2F,$2E
GeoMapLo:
        dc.b <RoomData0,<RoomData1,<RoomData2,<RoomData3,<RoomData4,<RoomData5,<RoomData6,<RoomData7,<RoomData8,<RoomData9,<RoomData10,<RoomData11,<RoomData12,<RoomData13,<RoomData14,<RoomData15,<RoomData16,<RoomData17,<RoomData18
GeoMapHi:
        dc.b >RoomData0,>RoomData1,>RoomData2,>RoomData3,>RoomData4,>RoomData5,>RoomData6,>RoomData7,>RoomData8,>RoomData9,>RoomData10,>RoomData11,>RoomData12,>RoomData13,>RoomData14,>RoomData15,>RoomData16,>RoomData17,>RoomData18
PFPattern0:
        dc.b $E0,$00,$0E,$EE,$00,$E0,$06,$E6,$E6,$00,$00,$E0,$00,$E0,$00,$EE,$E0,$0E,$06,$E0,$06,$EE,$EE,$0E,$66,$66,$60,$66,$60,$00,$0E,$6E,$06,$E6,$00,$06,$E6,$E6,$6E,$0E,$CE,$0E,$CE,$00,$E0,$06,$60,$6E
PFPattern1:
        dc.b $00,$70,$00,$00,$07,$77,$30,$03,$33,$03,$30,$03,$73,$70,$00,$37,$30,$07,$63,$63,$03,$70,$77,$77,$03,$00,$00,$30,$30,$37,$30,$30,$00,$60,$77,$73,$00,$70,$37,$37,$63,$63,$03,$33,$73,$70,$07,$00
PFPattern2:
        dc.b $40,$00,$04,$44,$00,$40,$04,$44,$44,$00,$00,$40,$00,$40,$00,$44,$40,$04,$04,$40,$04,$44,$44,$04,$44,$44,$40,$44,$40,$00,$04,$44,$04,$44,$00,$04,$44,$44,$44,$04,$44,$04,$44,$00,$40,$04,$40,$44
PFPattern3:
        dc.b $00,$20,$00,$00,$02,$22,$20,$02,$22,$02,$20,$02,$22,$20,$00,$22,$20,$02,$22,$22,$02,$20,$22,$22,$02,$00,$00,$20,$20,$22,$20,$20,$00,$20,$22,$22,$00,$20,$22,$22,$22,$22,$02,$22,$22,$20,$02,$00
BlankSprite:
        dc.b $00,$00,$00,$00,$00,$00,$00,$00,$00
; U3 mirrored horizontally with vertical beak; user-approved B0/B1/B2.
OwlB0:
        dc.b $24,$7E,$7E,$F7,$F7,$DB,$7E,$18,$00
OwlB1:
        dc.b $24,$BD,$FF,$F7,$F7,$DB,$7E,$18,$00
OwlB2:
        dc.b $24,$FF,$FF,$F7,$F7,$DB,$7E,$18,$00
OwlDown0:
        dc.b $1C,$7E,$FA,$67,$7F,$FA,$7E,$1C,$00
OwlDown1:
        dc.b $7C,$3E,$FA,$67,$7F,$FA,$3E,$7C,$00
OwlDown2:
        dc.b $7C,$7E,$FA,$67,$7F,$FA,$7E,$7C,$00
OwlUp0:
        dc.b $38,$7E,$5F,$FE,$E6,$5F,$7E,$38,$00
OwlUp1:
        dc.b $3E,$7C,$5F,$FE,$E6,$5F,$7C,$3E,$00
OwlUp2:
        dc.b $3E,$7E,$5F,$FE,$E6,$5F,$7E,$3E,$00
OwlFrameLo:
        dc.b <OwlB0,<OwlDown0,<OwlB0,<OwlUp0
        dc.b <OwlB1,<OwlDown1,<OwlB1,<OwlUp1
        dc.b <OwlB2,<OwlDown2,<OwlB2,<OwlUp2
OwlReflect:
        dc.b $00,$00,$08,$00
; Compact 2-column x 8-raster glyphs: $02 enables M0 left rail,
; $04 enables BL right rail. Different silhouettes in the actual game
; cell, not only the 8x8 HUD feedback. No P0 owl or P1 S3 reuse.
CursorPlayNeutral:
        dc.b $00,$06,$06,$06,$06,$06,$06,$00 ; two clear brackets
CursorPlayAccepted:
        dc.b $00,$04,$04,$06,$02,$02,$02,$00 ; angled causal tick
CursorPlayDenied:
        dc.b $06,$06,$00,$00,$00,$00,$06,$06 ; blocked ends
CursorPlayIntercept:
        dc.b $02,$00,$04,$00,$04,$00,$02,$00 ; broken Presence
CursorPlayLo:
        dc.b <CursorPlayNeutral,<CursorPlayAccepted,<CursorPlayDenied,<CursorPlayIntercept
CursorPlayHi:
        dc.b >CursorPlayNeutral,>CursorPlayAccepted,>CursorPlayDenied,>CursorPlayIntercept
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
        ; User-approved right exit arrow, always amber.
        dc.b $08,$0C,$0E,$FF,$FF,$0E,$0C,$08,$00

