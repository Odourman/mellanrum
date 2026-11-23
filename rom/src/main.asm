; MELLANRUM: SKOGEN SOM LYSSNAR - ISSUE #15 USER-AUTHORIZED CANDIDATE
; Atari 2600 / 6507 / DASM 2.20+, F6 16 KiB NTSC bank 3 (runtime kernel).
; Issue26: bank0/1/2 are ACT I/II/III score engines + 5x768 live soundtrack bytes each.
; Full 15-room reference-derived rule set. Hardware/playability is UNVERIFIED.
        processor 6502
VSYNC   = $00
VBLANK  = $01
WSYNC   = $02
NUSIZ0  = $04
NUSIZ1  = $05
COLUP0  = $06
COLUP1  = $07
COLUPF  = $08
COLUBK  = $09
CTRLPF  = $0A
PF0     = $0D
PF1     = $0E
PF2     = $0F
RESP0   = $10
RESBL   = $14
ENAM1   = $1E
AUDC0   = $15
AUDC1   = $16
AUDF0   = $17
AUDF1   = $18
AUDV0   = $19
AUDV1   = $1A
GRP0    = $1B
GRP1    = $1C
ENAM0   = $1D
ENABL   = $1F
HMP0    = $20
HMOVE   = $2A
HMCLR   = $2B
SWCHA   = $0280
SWCHB   = $0282
INTIM   = $0284
TIM64T  = $0296
INPT4   = $0C

        SEG.U variables
        ORG $80
pfbuf       ds 48       ; 8 rows x upper/lower x 3 TIA bytes
mapRows     ds 8        ; current collision bits, 5 left-hand columns each
mode        ds 1        ; 0 title, 1 campaign, 2 room done, 3 coda, 4 free forest
room        ds 1        ; 0..14, original I-01..III-05
act         ds 1
geom        ds 1
owlX        ds 1
owlY        ds 1
owlDir      ds 1
stoneX      ds 1
stoneY      ds 1
exitX       ds 1
exitY       ds 1
polarity    ds 1
phase       ds 1
phaseAge    ds 1
beat        ds 1
beatFrames  ds 1
introFrames ds 1
waitFrames  ds 1
codaLo      ds 1
codaHi      ds 1
cursorX     ds 1
cursorY     ds 1
moveDir     ds 1
moveWait    ds 1
prevFire    ds 1
prevSelect  ds 1
pending     ds 1        ; 0 none 1 tree 2 stone
pendingKey  ds 1        ; reflected group index, 0..39
usedFire    ds 1        ; one accepted FIRE/beat
ackFrames   ds 1        ; cursor feedback timer
ackType     ds 1        ; 0 normal, 1 accepted, 2 denied, 3 intercepted
slot0Key    ds 1        ; FF = empty
slot0Due    ds 1
slot1Key    ds 1
slot1Due    ds 1
presence    ds 1        ; 0 normal,1 warning,2 active,3 release
presenceEnd ds 1        ; no recurrence on tick byte overflow
intercepted ds 1
candidateX  ds 1
candidateY  ds 1
candidateD  ds 1
attempt     ds 1
workKey     ds 1
workX       ds 1
workY       ds 1
pfIndex     ds 1
rowIndex    ds 1
sprite0Ptr  ds 2
sprite1Ptr  ds 2
mapPtr      ds 2
pfPtr       ds 2
moveTemp    ds 1
soundStep   ds 1
shadowOn    ds 1        ; render-only: 0 normal / 1 warning / 2 active

        SEG code
        ORG $F000
Reset:
        sei
        cld
        ldx #$FF
        txs
        lda #0
        ldx #$7F
ClearRAM:
        sta $80,x
        dex
        bpl ClearRAM
        lda #$FF
        sta moveDir
        sta slot0Key
        sta slot1Key
        lda #0
        sta mode
        sta prevFire
        sta prevSelect
        lda #1
        sta CTRLPF           ; reflect 20 PF left bits
        lda #0
        sta NUSIZ0
        lda #$04
        sta NUSIZ1       ; two far-separated S3 symbols, x=71 and x=135
        lda #0
        sta ENAM1        ; M1 must remain OFF (NUSIZ1 would ghost M1)
        sta GRP0
        sta GRP1
        sta ENAM0
        sta ENABL

Frame:
        lda #2
        sta VSYNC
        sta WSYNC
        sta WSYNC
        sta WSYNC
        lda #0
        sta VSYNC
        lda #2
        sta VBLANK
        lda #43
        sta TIM64T
        jsr ReadInput
        jsr GameFrame
        jsr SetColorsSound
        jsr SetShadowVisibility
        jsr PlaceObjects
WaitVBlank:
        lda INTIM
        bne WaitVBlank
        sta WSYNC
        lda #0
        sta VBLANK
        lda mode
        beq RenderTitle
        jsr RenderPlay
        jmp EndVisible
RenderTitle:
        jsr DrawTitle
EndVisible:
        lda #2
        sta VBLANK
        lda #35
        sta TIM64T
WaitOverscan:
        lda INTIM
        bne WaitOverscan
        sta WSYNC
        sta WSYNC         ; NTSC raster correction: verified native Gopher 262, see #12
        jmp Frame

; Console RESET returns title. SELECT restarts active room, never selects a mode.
; LEFT physical Difficulty A/B is latched exclusively when FIRE starts title.
ReadInput:
        lda SWCHB
        and #1
        bne NotReset
        lda #0
        sta mode
        sta pending
        sta prevFire
        rts
NotReset:
        lda SWCHB
        and #2
        bne SelectReleased
        lda prevSelect
        bne AfterSelect
        lda #1
        sta prevSelect
        lda mode
        beq AfterSelect     ; SELECT on title has no mode effect
        cmp #3
        beq AfterSelect
        jsr LoadRoom       ; full state rewind on SELECT, same mode
        jmp AfterSelect
SelectReleased:
        lda #0
        sta prevSelect
AfterSelect:
        lda INPT4
        bmi FireReleased
        lda prevFire
        bne ReadMovement
        lda #1
        sta prevFire
        lda mode
        beq StartMode
        cmp #2
        beq AdvanceRoom
        cmp #3
        beq ReadMovement
        jsr LatchFire
        jmp ReadMovement
FireReleased:
        lda #0
        sta prevFire
        jmp ReadMovement
StartMode:
        lda SWCHB
        and #$40           ; LEFT Difficulty A (1) = campaign, B (0) = free forest
        bne StartCampaign  ; read ONCE at FIRE; game mode is latched
        lda #4
        sta mode
        lda soundStep
        and #3              ; deterministic title-frame seed: four original Act III forests
        clc
        adc #10
        sta room
        jsr LoadRoom
        jmp ReadMovement
StartCampaign:
        lda #0
        sta room
        lda #1
        sta mode
        jsr LoadRoom
        jmp ReadMovement
AdvanceRoom:
        lda waitFrames
        bne ReadMovement
        lda room
        cmp #14
        beq StartCoda
        inc room
        lda #1
        sta mode
        jsr LoadRoom
        jmp ReadMovement
StartCoda:
        lda #0
        sta presenceEnd
        lda #3
        sta mode
        lda #$D0         ; 720 frames = $02D0
        sta codaLo
        lda #2
        sta codaHi

; Joystick input: UP > LEFT > DOWN > RIGHT, no diagonal.
ReadMovement:
        lda mode
        cmp #1
        beq ReadStick
        cmp #4
        beq ReadStick
        rts
ReadStick:
        lda #$FF
        sta moveTemp
        lda SWCHA
        and #$10
        bne TryLeft
        lda #3
        sta moveTemp
        jmp StickChosen
TryLeft:
        lda SWCHA
        and #$40
        bne TryDown
        lda #2
        sta moveTemp
        jmp StickChosen
TryDown:
        lda SWCHA
        and #$20
        bne TryRight
        lda #1
        sta moveTemp
        jmp StickChosen
TryRight:
        lda SWCHA
        and #$80
        bne StickChosen
        lda #0
        sta moveTemp
StickChosen:
        lda moveTemp
        cmp #$FF
        bne StickActive
        sta moveDir
        lda #0
        sta moveWait
        rts
StickActive:
        cmp moveDir
        beq StickHeld
        sta moveDir
        lda #12            ; 200ms initial delay
        sta moveWait
        jmp DoCursorMove
StickHeld:
        lda moveWait
        beq StickRepeat
        dec moveWait
        rts
StickRepeat:
        lda #6             ; 100ms sustained repeat
        sta moveWait
DoCursorMove:
        ldx moveDir
        lda cursorX
        clc
        adc DeltaX,x
        cmp #10
        bcs MoveY
        sta cursorX
MoveY:
        lda cursorY
        clc
        adc DeltaY,x
        cmp #8
        bcs MoveDone
        sta cursorY
MoveDone:
        rts

; Input edge is latched with the cursor location from the actual video frame.
; One latch maximum per owl step; processing is BEFORE echoes/phase/motion.
LatchFire:
        lda pending
        bne FireDenied
        lda usedFire
        bne FireDenied
        lda cursorX
        cmp stoneX
        bne TryEditable
        lda cursorY
        cmp stoneY
        bne TryEditable
        lda #2
        sta pending
        rts
TryEditable:
        lda cursorX
        cmp #5
        bcc AtLeftX
        eor #$FF
        clc
        adc #10
AtLeftX:
        tax
        lda BitMask,x
        sta moveTemp
        ldy cursorY
        lda (mapPtr),y
        and moveTemp
        beq FireDenied
        ; cursorX >=5 must be mirrored before group-index formation.
        ldx cursorX
        cpx #5
        bcc UseXDirect
        txa
        eor #$FF
        clc
        adc #10
        tax
UseXDirect:
        txa
        clc
        adc GroupBase,y
        sta pendingKey
        lda #1
        sta pending
        rts
FireDenied:
        lda #2
        sta ackType
        lda #18
        sta ackFrames
        rts

GameFrame:
        lda ackFrames
        beq NoAckDecay
        dec ackFrames
NoAckDecay:
        lda mode
        cmp #3
        bne NotCoda
        lda codaLo
        bne CodaLow
        dec codaHi
CodaLow:
        dec codaLo
        lda codaHi
        bne CodaNoFlip
        lda codaLo
        cmp #$F0
        bne CodaNoFlip
        lda presenceEnd
        bne CodaNoFlip
        inc presenceEnd
        lda polarity
        eor #1
        sta polarity
CodaNoFlip:
        lda codaLo
        ora codaHi
        bne GameFrameDone
        lda #0
        sta mode
        jmp GameFrameDone
NotCoda:
        cmp #2
        bne NotSolved
        lda waitFrames
        beq GameFrameDone
        dec waitFrames
        jmp GameFrameDone
NotSolved:
        cmp #1
        beq ActiveFrame
        cmp #4
        bne GameFrameDone
ActiveFrame:
        lda introFrames
        beq CountBeat
        dec introFrames
        bne GameFrameDone
        jsr BeatTick         ; the first logical tick after the 108-frame preparation
        lda #72
        sta beatFrames
        jmp GameFrameDone
CountBeat:
        dec beatFrames
        bne GameFrameDone
        jsr BeatTick
        lda #72
        sta beatFrames
GameFrameDone:
        rts

; Original game state initialization: all 15 metadata entries and 5 true geoms.
LoadRoom:
        lda #0
        sta phase
        sta phaseAge
        sta beat
        sta pending
        sta usedFire
        sta ackFrames
        sta waitFrames      ; active-room stone encounter evidence, cleared on load
        sta ackType
        sta presence
        sta presenceEnd
        sta intercepted
        sta moveWait
        lda #1
        sta prevFire
        lda #$FF
        sta slot0Key
        sta slot1Key
        sta moveDir
        lda #108
        sta introFrames
        lda #72
        sta beatFrames
        ldx room
        lda RoomGeom,x
        sta geom
        lda RoomAct,x
        sta act
        lda RoomOwlX,x
        sta owlX
        sta cursorX
        lda RoomOwlY,x
        sta owlY
        sta cursorY
        lda RoomOwlDir,x
        sta owlDir
        lda RoomStoneX,x
        sta stoneX
        lda RoomStoneY,x
        sta stoneY
        lda RoomExitX,x
        sta exitX
        lda RoomExitY,x
        sta exitY
        lda RoomPolarity,x
        sta polarity
        ldx geom
        lda GeoMapLo,x
        sta mapPtr
        lda GeoMapHi,x
        sta mapPtr+1
        lda GeoPFLo,x
        sta pfPtr
        lda GeoPFHi,x
        sta pfPtr+1
        ldy #7
CopyMap:
        lda (mapPtr),y  ; mutable geometry mask is in first 8 bytes
        ; blocked base masks in mapPtr+8, copied from indirect offset
        tya
        clc
        adc #8
        tay
        lda (mapPtr),y
        sta mapRows-8,y
        tya
        sec
        sbc #8
        tay
        dey
        bpl CopyMap
        ldy #47
CopyPF:
        lda (pfPtr),y
        sta pfbuf,y
        dey
        bpl CopyPF
        rts

; Discrete logical owl beat. Strict ordering: FIRE, autonomous Presence,
; due echoes (slot 0 then 1), phase, owl move, stone arrival, victory.
BeatTick:
        lda #0
        sta intercepted
        jsr UpdatePresence
        jsr CommitFire
        lda presence
        cmp #2
        bne NoAutoTurn
        lda room
        cmp #12
        bcc NoAutoTurn
        tax
        lda RoomActive,x
        cmp beat
        bne NoAutoTurn
        lda intercepted
        bne NoAutoTurn
        lda polarity
        eor #1
        sta polarity
NoAutoTurn:
        lda slot0Key
        cmp #$FF
        beq NoEcho0
        lda slot0Due
        cmp beat
        bne NoEcho0
        lda slot0Key
        sta workKey
        jsr ToggleTree
        lda #$FF
        sta slot0Key
NoEcho0:
        lda slot1Key
        cmp #$FF
        beq NoEcho1
        lda slot1Due
        cmp beat
        bne NoEcho1
        lda slot1Key
        sta workKey
        jsr ToggleTree
        lda #$FF
        sta slot1Key
NoEcho1:
        lda act
        cmp #3
        bne NoPhaseTick
        inc phaseAge
        lda polarity
        beq PhaseFour
        lda #6
        bne CheckPhase
PhaseFour:
        lda #4
CheckPhase:
        cmp phaseAge
        bcc InvertPhase
        bne NoPhaseTick
InvertPhase:
        lda #0
        sta phaseAge
        lda phase
        eor #1
        sta phase
NoPhaseTick:
        jsr MoveOwl
        lda #0
        sta usedFire
        inc beat
        jsr UpdatePresence
        rts

; State is always inferred, not random and not a fourth moving sprite.
UpdatePresence:
        lda #0
        sta presence
        lda mode
        cmp #4
        beq PresenceDone
        lda presenceEnd
        bne PresenceDone
        lda beat
        cmp #8
        bcc PresenceWindowEarly
        lda #1
        sta presenceEnd
        rts
PresenceWindowEarly:
        ldx room
        lda RoomWarning,x
        cmp beat
        bne CheckActive
        lda #1
        sta presence
        rts
CheckActive:
        cpx #12
        bcc PresenceDone
        lda beat
        sec
        sbc RoomActive,x
        cmp #2
        bcc IsActive
        cmp #2
        bne PresenceDone
        lda #3
        sta presence
        rts
IsActive:
        lda #2
        sta presence
PresenceDone:
        rts

CommitFire:
        lda pending
        bne FireActionPresent
        rts
FireActionPresent:
        cmp #2
        bne FireTree
        lda polarity
        eor #1
        sta polarity
        jmp FireAccepted
FireTree:
        lda pendingKey
        sta workKey
        ; Issue26: RECALL THE FUTURE. Touching an echo-queued tree
        ; again CANCELS its coming reversal, without another tree toggle.
        ; The cancelled memory flips stone polarity: a second strategic path.
        cmp slot0Key
        bne TryRecallSlot1
        lda #$FF
        sta slot0Key
        jmp RecallEcho
TryRecallSlot1:
        cmp slot1Key
        bne NewTreeGesture
        lda #$FF
        sta slot1Key
RecallEcho:
        lda polarity
        eor #1
        sta polarity
        jmp FireAccepted
NewTreeGesture:
        lda act
        cmp #1
        beq TreeCapacityOkay
        lda slot0Key
        cmp #$FF
        beq TreeCapacityOkay
        lda slot1Key
        cmp #$FF
        bne InvalidFire
TreeCapacityOkay:
        lda presence
        cmp #2
        bne RealTreeEdit
        lda polarity
        eor #1
        sta polarity
        lda #1
        sta intercepted
        lda #3
        sta ackType
        jmp FinishFireAccepted
RealTreeEdit:
        jsr ToggleTree
        lda act
        cmp #1
        beq FireAccepted
        lda polarity
        beq DueThree
        lda #5
        bne HaveDueOffset
DueThree:
        lda #3
HaveDueOffset:
        clc
        adc beat
        sta moveTemp
        lda slot0Key
        cmp #$FF
        bne FillSlotOne
        lda workKey
        sta slot0Key
        lda moveTemp
        sta slot0Due
        jmp FireAccepted
FillSlotOne:
        lda workKey
        sta slot1Key
        lda moveTemp
        sta slot1Due
FireAccepted:
        lda #1
        sta ackType
FinishFireAccepted:
        lda #18
        sta ackFrames
        lda #1
        sta usedFire
        jmp FinishFire
InvalidFire:
        lda #2
        sta ackType
        lda #18
        sta ackFrames
FinishFire:
        lda #0
        sta pending
NoFireAction:
        rts

; Convert 0..39 reflected cell key to x=0..4 / y=0..7.
DecodeKey:
        lda workKey
        ldx #0
DecodeLoop:
        cmp #5
        bcc DecodedKey
        sec
        sbc #5
        inx
        bne DecodeLoop
DecodedKey:
        sta workX
        stx workY
        rts

; Toggle true collision bit and both reflected PF 6/14-band bytes.
; Masks are the exact T <-> t XOR according to GRAPHICS V5.1 cell table.
ToggleTree:
        jsr DecodeKey
        ldy workY
        ldx workX
        lda mapRows,y
        eor BitMask,x
        sta mapRows,y
        ; PF row offset = y * 6, source precomputed in ROM.
        lda PFBase,y
        clc
        adc UpperPFOffset,x
        tay
        lda pfbuf,y
        eor UpperToggle,x
        sta pfbuf,y
        ldy workY
        lda PFBase,y
        clc
        adc LowerPFOffset,x
        tay
        lda pfbuf,y
        eor LowerToggle,x
        sta pfbuf,y
        rts

MoveOwl:
        lda #0
        sta attempt
TryOwlDirection:
        ldx attempt
        lda owlDir
        clc
        adc TurnOffset,x
        and #3
        sta candidateD
        tax
        lda owlX
        clc
        adc DeltaX,x
        cmp #10
        bcs OwlTryNext
        sta candidateX
        lda owlY
        clc
        adc DeltaY,x
        cmp #8
        bcs OwlTryNext
        sta candidateY
        jsr PassableCandidate
        bcc OwlTryNext
        ; On stone entry rotate future facing by +/- 90 degrees.
        lda owlX
        cmp stoneX
        bne UpdateOwlCell
        lda owlY
        cmp stoneY
        beq AlreadyOnStone
UpdateOwlCell:
        lda candidateX
        sta owlX
        lda candidateY
        sta owlY
        lda candidateD
        sta owlDir
        lda owlX
        cmp stoneX
        bne OwlVictoryCheck
        lda owlY
        cmp stoneY
        bne OwlVictoryCheck
        lda #1
        sta waitFrames      ; real owl has encountered the stone
        lda polarity
        beq RotateClockwise
        lda owlDir
        clc
        adc #3
        and #3
        sta owlDir
        jmp OwlVictoryCheck
RotateClockwise:
        inc owlDir
        lda owlDir
        and #3
        sta owlDir
        jmp OwlVictoryCheck
AlreadyOnStone:
        lda candidateX
        sta owlX
        lda candidateY
        sta owlY
        lda candidateD
        sta owlDir
        jmp OwlVictoryCheck
OwlTryNext:
        inc attempt
        lda attempt
        cmp #4
        beq OwlNoExit
        jmp TryOwlDirection
OwlNoExit:
        rts
OwlVictoryCheck:
        lda mode
        cmp #4
        beq OwlMoved
        lda owlX
        cmp exitX
        bne OwlMoved
        lda owlY
        cmp exitY
        bne OwlMoved
        ldx room
        lda RoomGate,x
        beq ExitResonates
        cmp #1
        beq GateStoneVisit
        cmp #2
        beq GatePolarityOne
        cmp #3
        beq GatePolarityZero
        cmp #4
        beq GateEchoEmpty
        cmp #5
        beq GatePhaseOne
        ; Gate7 needs at least one unsettled echo at the exit.
        lda slot0Key
        cmp #$FF
        bne ExitResonates
        lda slot1Key
        cmp #$FF
        bne ExitResonates
        beq ExitDissonance
GateStoneVisit:
        lda waitFrames
        bne ExitResonates
        beq ExitDissonance
GatePolarityOne:
        lda polarity
        bne ExitResonates
        beq ExitDissonance
GatePolarityZero:
        lda polarity
        beq ExitResonates
        bne ExitDissonance
GateEchoEmpty:
        lda slot0Key
        cmp #$FF
        bne ExitDissonance
        lda slot1Key
        cmp #$FF
        beq ExitResonates
        bne ExitDissonance
GatePhaseOne:
        lda phase
        bne ExitResonates
        beq ExitDissonance
ExitDissonance:
        ; Visible and reversible wrong guess, not a mandatory FIRE counter.
        lda #2
        sta ackType
        lda #18
        sta ackFrames
        rts
ExitResonates:
        ; Multi-causal resonance: an exit may require a memory, stone visit
        ; or polarity beyond its original gate, never a FIRE count.
        jsr CheckExitExtras
        bcc ExitDissonance
        lda #2
        sta mode
        lda #48
        sta waitFrames
OwlMoved:
        rts
; Candidate coordinates already range-checked; carry 1 => can move.
PassableCandidate:
        lda candidateX
        cmp stoneX
        bne TryExitOverride
        lda candidateY
        cmp stoneY
        beq PassYes
TryExitOverride:
        lda candidateX
        cmp exitX
        bne CheckTreeCell
        lda candidateY
        cmp exitY
        beq PassYes
CheckTreeCell:
        lda candidateX
        cmp #5
        bcc CandidateLeft
        eor #$FF
        clc
        adc #10
CandidateLeft:
        tax
        ldy candidateY
        lda mapRows,y
        and BitMask,x
        beq IsBaseClear
        lda phase
        bne PassYes
        jmp PassNo
IsBaseClear:
        lda phase
        beq PassYes
        ; Issue #21: no invisible marker hover collision override.
        ; Only a deliberate FIRE edit can open a mutable tree.
PassNo:
        clc
        rts
PassYes:
        sec
        rts

; Coarse/fine horizontal TIA positioning in VBLANK, four genuine TIA objects.
; X is TIA index: 0=P0 U3 owl, 1=P1 both S3 sigils, 2=M0 cursor; BL spare.
PlaceObjects:
        lda mode
        beq NoObjects
        lda #$04
        sta NUSIZ1       ; two wide-separated P1 sprite copies
        lda owlX
        asl
        asl
        asl
        asl
        clc
        adc #4
        ldx #0           ; P0 is original full 9-byte OWL bitmap
        jsr PositionOne
        lda stoneX
        asl
        asl
        asl
        asl
        clc
        adc #7           ; logical stoneX 4 => x=71
        ldx #1           ; P1 first symbol; second copy automatically x+64
        jsr PositionOne
        lda cursorX
        asl
        asl
        asl
        asl
        clc
        adc #4
        ldx #2           ; M0 is cursor, no separate P1 mark
        jsr PositionOne
        ; M0 stays a precise 1px locator. P0 bottom HUD draws genuine
        ; ring / check / X / broken Presence feedback glyphs instead.
        lda #0
        sta NUSIZ0
        sta WSYNC
        sta HMOVE
NoObjects:
        rts
PositionOne:
        sta WSYNC
        sec
Position15:
        sbc #15
        bcs Position15
        eor #7
        asl
        asl
        asl
        asl
        sta HMP0,x
        sta RESP0,x
        rts

; Issue32: eight evolving 256-frame pages = 34.1-second aural envelope.
; codaHi is free until actual mode 3 and reused for the coda countdown.
SetColorsSound:
        inc soundStep
        bne NoSlowCarry
        lda mode
        cmp #3
        beq NoSlowCarry
        inc codaHi
NoSlowCarry:
        lda mode
        cmp #3
        beq CodaColorsSound
        cmp #0
        beq TitleColors
        lda act
        clc
        adc phase
        tax
        lda PaletteBG,x
        sta COLUBK
        lda room
        and #$06
        eor PalettePF,x
        sta COLUPF
        lda PaletteOwl,x
        sta COLUP0
        lda PaletteGlyph,x
        sta COLUP1
        jmp PlayScore
TitleColors:
        lda #$A0
        sta COLUBK
        lda #$B6
        sta COLUPF
        lda #$0E
        sta COLUP0
        lda #$26
        sta COLUP1
PlayScore:
        lda mode
        cmp #2
        beq Silence
        ldx #0
        lda mode
        beq ChooseBank
        ldx act
        dex
ChooseBank:
        jsr $FF90
        ; Every eight 256f periods new silence/partial dissonance pattern.
        lda codaHi
        eor polarity       ; player stone decisions alter the long-form score
        eor phase          ; act III dissonance changes on phase inversion
        and #7
        cmp #5
        bne LongPhaseThree
        lda soundStep
        and #$80
        beq SoundDone
        lda #0
        sta AUDV1
        jmp SoundDone
LongPhaseThree:
        cmp #3
        bne SoundDone
        lda #$1F
        sta AUDF1
SoundDone:
        rts
CodaColorsSound:
        jsr CodaPalette    ; genuine three-stage TIA palette transformation
        lda #$0E
        sta COLUP0
        lda #$26
        sta COLUP1
        lda #$0C
        sta AUDC0
        lda #$1E
        sta AUDF0
        lda codaHi
        asl
        clc
        adc #1
        sta AUDV0
        lda #0
        sta AUDV1
        rts
Silence:
        lda #0
        sta AUDV0
        sta AUDV1
        rts

 ; Render-only silhouette gate, 24 frames on / 40 frames off (~0.4 s glimpses).
 ; Active intrusion and early warning have different PF behavior; no collision writes.
SetShadowVisibility:
        lda #0
        sta shadowOn
        sta moveTemp       ; render-only mask frame offset 0/8/16; safe scratch
        lda mode
        cmp #3
        bne ShadowOnlyGame
        lda codaHi
        bne ShadowGateDone
        lda #2
        sta shadowOn
        lda codaLo
        and #$18
        sta moveTemp
        rts
ShadowOnlyGame:
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
        rts

; NTSC display: 16 top status lines, 8*20 gameplay rows, 16 bottom lines.
; Crowns are 6 lines, stems 14; P0/P1 use safe lower-band raster slots.
RenderPlay:
        lda #1
        sta CTRLPF
        lda #0
        sta GRP0
        sta GRP1
        sta ENABL
        sta ENAM0
        lda phase
        beq NormalPhaseHUD
        lda #$F0
        bne HavePhaseHUD
NormalPhaseHUD:
        lda #$A0
HavePhaseHUD:
        sta PF0
        lda #0
        sta PF1
        lda slot0Key
        cmp #$FF
        beq NoHUDSlot0
        lda #$80
        sta PF1
NoHUDSlot0:
        lda slot1Key
        cmp #$FF
        beq NoHUDSlot1
        lda PF1
        ora #$20
        sta PF1
NoHUDSlot1:
        ldx presence
        lda PresenceHUD,x
        sta PF2
        ldx #15
Top16:
        sta WSYNC
        dex
        bne Top16
        lda #0
        sta rowIndex
        sta pfIndex
        lda moveTemp
        sta workY          ; render-only PF2 frame index, 0/8/16
NextRow:
        ; crown first line: register updates, no sprites
        sta WSYNC
        ldy pfIndex
        lda pfbuf,y
        sta PF0
        iny
        lda pfbuf,y
        sta PF1
        iny
        lda pfbuf,y
        ldx shadowOn
        beq NoCrownShadow
        ldx workY
        ora ShadowCrownOr,x
        and ShadowCrownAnd,x
NoCrownShadow:
        sta PF2
        lda #0
        sta GRP0
        sta GRP1
        sta ENABL
        sta ENAM0
        ; crown second line: choose owl sprite/blank per logical row
        sta WSYNC
        lda rowIndex
        cmp owlY
        bne NoOwlOnRow
        lda mode
        cmp #3
        bne OwlPresent
        lda codaHi
        bne OwlPresent
        lda codaLo
        cmp #128
        bcc NoOwlOnRow
OwlPresent:
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
OwlRowChosen:
        ; crown third line: select first glyph from source stoneY.
        sta WSYNC
        lda rowIndex
        cmp stoneY
        bne NoSymbolAOnRow
        lda #<GlyphA
        sta sprite1Ptr
        lda #>GlyphA
        sta sprite1Ptr+1
        jmp SymbolAReady
NoSymbolAOnRow:
        lda #<BlankSprite
        sta sprite1Ptr
        lda #>BlankSprite
        sta sprite1Ptr+1
SymbolAReady:
        ; fourth crown line: choose independent glyph B for exitY.
        sta WSYNC
        lda rowIndex
        cmp exitY
        bne NoSymbolBOnRow
        lda mode
        cmp #4           ; FRI SKOG has no exit
        beq NoSymbolBOnRow
        lda #<GlyphB
        sta pfPtr
        lda #>GlyphB
        sta pfPtr+1
        jmp SymbolBReady
NoSymbolBOnRow:
        lda #<BlankSprite
        sta pfPtr
        lda #>BlankSprite
        sta pfPtr+1
SymbolBReady:
        ; fifth crown line: prepare M0 cursor gate (not game state).
        sta WSYNC
        lda #0
        sta candidateY
        lda rowIndex
        cmp cursorY
        bne MarkerGateDone
        lda #2
        sta candidateY
MarkerGateDone:
        lda workY
        sta candidateD    ; current mask frame index for the forthcoming stem
        inc workY         ; next crown row index; no extra work in hot PF2 scanline
        ; sixth crown line: BL unused; P0 real U3 owl retained.
        sta WSYNC
        ; stem first line: register change + BL/M0 gating
        sta WSYNC
        ldy pfIndex
        iny
        iny
        iny
        lda pfbuf,y
        sta PF0
        iny
        lda pfbuf,y
        sta PF1
        iny
        lda pfbuf,y
        ldx shadowOn
        cpx #2              ; warning: incomplete crown only, no full void
        bne NoStemShadow
        ldx candidateD
        ora ShadowStemOr,x
        and ShadowStemAnd,x
NoStemShadow:
        sta PF2
        lda #0
        sta ENABL
        lda candidateY
        sta ENAM0
        ldx #13
Stem13:
        sta WSYNC
        ldy SpriteRowIndex,x
        lda (sprite0Ptr),y
        sta GRP0
        lda (sprite1Ptr),y
        sta GRP1          ; first P1 copy (glyph A)
        cpx #1           ; last blank sprite row must update PF bookkeeping
        beq StemLastFast  ; early, avoiding >76 cycles from post-loop bookkeeping
        ; P1 glyph A fetches around beam c46-50; wait until after its right edge.
        nop
        nop
        nop
        nop
        nop
        nop
        nop
        nop
        nop
        nop
        nop
        nop
        nop
        nop
        lda (pfPtr),y
        sta GRP1          ; second P1 copy, before x=135 fetch at c68
        dex
        bne Stem13
StemLastFast:
        lda pfIndex
        clc
        adc #6
        sta pfIndex
        inc rowIndex
        lda rowIndex
        cmp #8
        beq AllRowsFinished
        jmp NextRow
AllRowsFinished:
        ; bottom 16 status scanlines, polarity is encoded in a mirrored slash.
        lda #0
        sta GRP0
        sta GRP1
        sta ENABL
        sta ENAM0
        sta PF0
        lda polarity
        beq PolarityLeft
        lda #$02
        bne PolarityReady
PolarityLeft:
        lda #$01
PolarityReady:
        sta PF2
        lda #$44
        sta PF1
        ; Four authentic 8x8 P0 bitmap symbols in lower HUD.
        ; Owl is only drawn in upper forest rows; use P0 again safely.
        lda #72
        ldx #0
        jsr PositionOne
        lda ackFrames
        beq HUDNeutral
        ldx ackType
        bne HUDChoose
HUDNeutral:
        ldx #0
HUDChoose:
        lda CursorSpriteLo,x
        sta sprite0Ptr
        lda CursorSpriteHi,x
        sta sprite0Ptr+1
        ldy #7
HUDIcon8:
        sta WSYNC
        lda (sprite0Ptr),y
        sta GRP0
        dey
        bpl HUDIcon8
        lda #0
        sta GRP0
        ldx #5
HUDBottom7:
        sta WSYNC
        dex
        bne HUDBottom7
        rts

; Only legible title word: MELLANRUM. 40 PF bits, 9 letters in one line.
; Unmirrored 20+20 PF scanline rewrite; no other text.
; NO selectable title UI: the console's LEFT Difficulty A/B is the sole mode selector.
; FIRE starts the hardware-selected mode, SELECT and joystick do not select.
; The previous icon band is deliberately blank; 192-line raster retained.
DrawTitle:
        lda #0
        sta CTRLPF           ; no mirroring, distinct L/R PF halves
        sta GRP0
        sta GRP1
        sta ENABL
        sta ENAM0
        sta PF0
        sta PF1
        sta PF2
        ldx #32
TitleTop:
        sta WSYNC
        dex
        bne TitleTop
        ldy #0
        ldx #8
TitleGlyphLine:
        sta WSYNC
        lda TitleLeftPF0,y
        sta PF0
        lda TitleLeftPF1,y
        sta PF1
        lda TitleLeftPF2,y
        sta PF2
        nop
        nop
        nop
        nop
        lda TitleRightPF0,y
        sta PF0
        lda TitleRightPF1,y
        sta PF1
        lda TitleRightPF2,y
        sta PF2
        dex
        bne TitleGlyphLine
        iny
        cpy #7
        beq TitleGlyphDone
        ldx #8
        jmp TitleGlyphLine
TitleGlyphDone:
        lda #0
        sta PF0
        sta PF1
        sta PF2
        ldx #23
TitleGap:
        sta WSYNC
        dex
        bne TitleGap
        ; Preserve the original 24-scanline layout without menu icons.
        lda #0
        sta PF0
        sta PF1
        sta PF2
        ldx #25       ; preserve 262 NTSC lines after removing long icon kernel
TitleBlankSelectionBand:
        sta WSYNC
        dex
        bne TitleBlankSelectionBand
        ldx #55
TitleBottom:
        sta WSYNC
        dex
        bne TitleBottom
        rts

        include "rom/src/data.inc"

        ; Every bank has the 6507 trampoline at the exact SAME address.
        ; $FFF6+X selects F6 bank 0..2, then execution falls into the selected
        ; bank's $FF93: JSR score interpreter; $FFF9 returns bank3 and RTS.
        ORG $FF90
F6ScoreTrampoline:
        lda $FFF6,x
        nop
        nop
        nop
        lda $FFF9
F6ScoreReturn:
        rts

        ; Common reset recovery when SELECT/RESET occurs with bank0..2 selected.
        ORG $FF9A
F6BankReset:
        lda $FFF9
        jmp Reset

        ; Bank3-only routines in the free pre-vector area.
        ; F6 reset/trampoline code remains byte-for-byte at $FF90/$FF9A.
        ORG $FFA0
CheckExitExtras:
        ldx room
        lda RoomExtra,x
        and #1
        beq ExtraPolarity
        lda waitFrames
        beq ExtraNo
ExtraPolarity:
        lda RoomExtra,x
        and #2
        beq ExtraEcho
        lda polarity
        beq ExtraNo
ExtraEcho:
        lda RoomExtra,x
        and #4
        beq ExtraPolZero
        lda slot0Key
        cmp #$FF
        bne ExtraPolZero
        lda slot1Key
        cmp #$FF
        beq ExtraNo
ExtraPolZero:
        lda RoomExtra,x
        and #8
        beq ExtraYes
        lda polarity
        bne ExtraNo
ExtraYes:
        sec
        rts
ExtraNo:
        clc
        rts

; A three-stage coda: the forest darkens and finally disappears.
; U3 vanishes late while the glowing S3 stone is still readable.
CodaPalette:
        ; Compact: never execute from F6 bank-switch hotspots $FFF6-$FFF9.
        ldx #$86
        lda #$82
        ldy codaHi
        bne CodaApply
        ldx #$84
        lda #$80
        ldy codaLo
        bmi CodaApply
        ldx #$02
        lda #$00
CodaApply:
        sta COLUBK
        stx COLUPF
        rts
CodaPaletteEnd:

        ORG $FFFC
        dc.w Reset
        dc.w Reset
