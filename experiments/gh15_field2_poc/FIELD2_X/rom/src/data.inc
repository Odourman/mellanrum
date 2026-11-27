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
        dc.b $01,$01,$02,$03,$03,$03,$03,$03
RoomPolarity:
        dc.b $00,$01,$01,$00,$00,$01,$00,$00
RoomOwlY:
        dc.b $03,$05,$02,$05,$04,$05,$02,$04
RoomOwlDir:
        dc.b $00,$02,$03,$00,$01,$00,$00,$00
RoomStoneY:
        dc.b $03,$03,$06,$01,$05,$03,$05,$04
RoomExitY:
        dc.b $03,$03,$05,$01,$02,$03,$02,$03
RoomPresence:
        dc.b $02,$02,$02,$00,$02,$02,$02,$02
CommonTopPF:
        dc.b $F0,$FF,$FF,$60,$66,$66
RoomData0:
        dc.b $00,$04,$00,$00,$00,$00,$08,$00,$02,$08,$08,$08,$08,$04
RoomData1:
        dc.b $00,$00,$00,$08,$1E,$00,$00,$00,$08,$08,$06,$05,$08,$08
RoomData2 = RoomData0 ; inaccessible campaign index in 4-room PoC
RoomData3 = RoomData0 ; inaccessible campaign index in 4-room PoC
RoomData4 = RoomData0 ; inaccessible campaign index in 4-room PoC
RoomData5:
        dc.b $00,$02,$04,$18,$08,$1C,$06,$00,$00,$02,$0F,$04,$0A,$03
RoomData6 = RoomData0 ; inaccessible campaign index in 4-room PoC
RoomData7 = RoomData0 ; inaccessible campaign index in 4-room PoC
RoomData8 = RoomData0 ; inaccessible campaign index in 4-room PoC
RoomData9 = RoomData0 ; inaccessible campaign index in 4-room PoC
RoomData10 = RoomData0 ; inaccessible campaign index in 4-room PoC
RoomData11 = RoomData0 ; inaccessible campaign index in 4-room PoC
RoomData12 = RoomData0 ; inaccessible campaign index in 4-room PoC
RoomData13:
        dc.b $00,$00,$10,$18,$12,$14,$08,$00,$08,$07,$0C,$0B,$0D,$04
RoomData14 = RoomData0 ; inaccessible campaign index in 4-room PoC
RoomData15:
        dc.b $00,$00,$00,$1E,$04,$04,$10,$00,$08,$08,$09,$02,$02,$01
RoomData16:
        dc.b $00,$00,$10,$08,$18,$04,$00,$00,$08,$07,$06,$10,$0E,$08
RoomData17:
        dc.b $00,$02,$08,$1A,$04,$08,$14,$00,$00,$06,$11,$0E,$06,$12
RoomData18:
        dc.b $00,$0A,$18,$18,$08,$06,$0A,$00,$13,$0C,$0C,$04,$14,$13
GeoMapLo:
        dc.b <RoomData0,<RoomData1,<RoomData5,<RoomData13,<RoomData15,<RoomData16,<RoomData17,<RoomData18
GeoMapHi:
        dc.b >RoomData0,>RoomData1,>RoomData5,>RoomData13,>RoomData15,>RoomData16,>RoomData17,>RoomData18
PFPattern0:
        dc.b $E0,$00,$0E,$EE,$00,$E6,$00,$00,$00,$EE,$0E,$60,$00,$0E,$06,$00,$00,$E0,$06,$60,$6E
PFPattern1:
        dc.b $00,$70,$00,$00,$07,$33,$03,$30,$00,$77,$77,$30,$37,$30,$00,$77,$33,$73,$70,$07,$00
PFPattern2:
        dc.b $40,$00,$04,$44,$00,$44,$00,$00,$00,$44,$04,$40,$00,$04,$04,$00,$00,$40,$04,$40,$44
PFPattern3:
        dc.b $00,$20,$00,$00,$02,$22,$02,$20,$00,$22,$22,$20,$22,$20,$00,$22,$22,$22,$20,$02,$00

LoadMetaIndex:
        lda RoomIndex,x
        tax
        lda RoomAct,x
        jmp LoadMetaIndexed
RoomIndex:
        dc.b 0,1,0,0,0,2,0,0,0,0,0,0,0,3,0,4,5,6,7
PoCAdvance:
        ldx room
        cpx #13
        beq PoCEnd
        lda PoCNext,x
        sta room
        lda #1
        sta mode
        jmp LoadRoom
PoCEnd:
        jmp StartCoda
EventStart:
        lda pending
        sta usedFire
        ldx presenceEnd
        cpx #1
        bne EventInit
        cmp #2
        bne EventSinglePresence
        lda #8
        bne EventPresenceSet
EventSinglePresence:
        lda #7
EventPresenceSet:
        sta usedFire
EventInit:
        lda #0
        sta pending
        sta presence
        sta intercepted
        jmp EventStartReturn
PoCStoneColor:
        sta workKey
        ldx polarity
        lda mode
        cmp #4
        beq LegacyStoneColor
        lda room
        asl
        asl
        adc room ; carry clear
        sta rowIndex
        lda #10
        sta pfIndex
        lda #$46
        cpx #0
        beq PoCColorDone
        lda #$9A
        bne PoCColorDone
LegacyStoneColor:
        lda workKey
        cpx #0
        beq PoCColorDone
        lda #$46
PoCColorDone:
        jmp FieldPulse
EventSound:
        lda mode
        cmp #1
        bne EventSoundEnd
        lda ackFrames
        beq EventSoundEnd
        ldx ackType
        cpx #2
        beq DenialSound
        ldx usedFire
        cpx #8
        beq AccentSound
        lda presence
        bne PresenceSound
        cpx #3
        bne AccentSound
        lda slot1Key
        bmi EventSoundEnd
        ldx #9
AccentSound:
        lda EventDivisor,x
        sta AUDF1
        lda #5
        sta AUDV1
EventSoundEnd:
        rts
DenialSound:
        lda #$0B
        sta AUDF1
        lda #2
        sta AUDV1
        rts
PresenceSound:
        lda #0
        sta AUDV1
        rts
EventDivisor:
        dc.b 31,19,12,31,29,25,15,31,7,23

NumberEntry:
        lda mode
        cmp #3
        bcs PlainTop
        ldx rowIndex
NumberLoop:
        sta WSYNC
        lda #0
        sta PF0
        lda NumberRows,x
        sta PF1
        jmp NumDelayHelper
NumberTail:
        beq EventTop
        and #1
        bne NumberLoop
        inx
        bne NumberLoop
PlainTop:
        ldx #14
Top16:
        sta WSYNC
        dex
        bne Top16
        jmp NumberContinue
EventTop:
        sta WSYNC
        lda #$A0
        ldx phase
        beq EventPhase
        lda #$F0
EventPhase:
        sta PF0
        lda #0
        ldx slot0Key
        cpx #$FF
        beq NoTreeStatus
        lda #$80
NoTreeStatus:
        ldx slot1Key
        cpx #$FF
        beq NoEchoStatus
        ora #$20
NoEchoStatus:
        sta PF1
        ldx presence
        bne KeepPresenceStatus
        lda ackFrames
        beq KeepPresenceStatus
        lda ackType
        cmp #1
        bne KeepPresenceStatus
        ldx usedFire
        lda MoveGlyph,x
        sta PF2
KeepPresenceStatus:
        ldx #3
        jmp Top16
MoveGlyph:
        dc.b 0,0,0,0,$18,$66,$24,0,0,0
NumberRows:
        dc.b $E4,$AC,$A4,$A4,$EE,$EE,$A2,$AE,$A8,$EE,$EE,$A2,$AE,$A2,$EE,$EA,$AA,$AE,$A2,$E2,$EE,$A8,$AE,$A2,$EE,$EE,$A8,$AE,$AA,$EE,$EE,$A2,$A2,$A2,$E2,$EE,$AA,$AE,$AA,$EE,$EE,$AA,$AE,$A2,$EE,$4E,$CA,$4A,$4A,$EE,$44,$CC,$44,$44,$EE,$4E,$C2,$4E,$48,$EE,$4E,$C2,$4E,$42,$EE,$4A,$CA,$4E,$42,$E2,$4E,$C8,$4E,$42,$EE

        ORG $FD9F
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

