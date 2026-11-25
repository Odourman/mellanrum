Warning: truncated output (original token count: 10974)
Total output lines: 1833

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
REFP0   = $0B
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
renderDir   ds 1        ; last successful owl movement, initialized on LoadRoom
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
fireX       ds 1        ; visible cursor column captured on FIRE edge
fireY       ds 1        ; visible cursor row captured on FIRE edge
markerPtr   ds 2        ; active playfield M0+BL two-stroke glyph pointer

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
        sta REFP0
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
        jsr SelectReload   ; rewind completed or active campaign room; preserve FRI mode
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
        cmp #4
        beq FreeForestFire
        jsr LatchFire
        ; FIRE selects the cursor that was on-screen BEFORE this input poll.
        ; A simultaneous direction may move only on a later video frame.
        rts
FreeForestFire:
        ; Distinct free installation: FIRE modulates shadow and TIA score,
        ; but MUST NEVER queue the campaign's stone or tree edit.
        lda cursorX
        sta fireX
        lda cursorY
        sta fireY
        lda #3
        sta ackType
        lda #18
        sta ackFrames
        rts
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
        rts                 ; display spawn marker before any movement
StartCampaign:
        lda #0
        sta room
        lda #1
        sta mode
        jsr LoadRoom
        rts                 ; title FIRE is not also a move command
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
        ; Snapshot the exact grid cell shown last frame. Only accepted
        ; targets are subsequently committed; moving cannot retarget them.
        lda cursorX
        sta fireX
        lda cursorY
        sta fireY
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
        lda RoomAct,x
        sta act
        lda #1            ; all fifteen approved starting columns are 1
        sta owlX
        sta cursorX
        lda RoomOwlY,x
        sta owlY
        sta cursorY
        lda RoomOwlDir,x
        sta owlDir
        sta renderDir
        lda #4            ; all fifteen stone columns are 4
        sta stoneX
        lda RoomStoneY,x
        sta stoneY
        lda #8            ; all fifteen exit columns are 8
        sta exitX
        lda RoomExitY,x
        sta exitY
        lda RoomPolarity,x
        sta polarity
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
        ; 15*8 ROM bytes recovered: source blocked masks were exactly
        ; source tree bits OR 1 in interior, $1F on border rows.
        ; Keep mutable collision byte-for-byte identical to prior ROM.
        lda (mapPtr),y
        ora #1
        cpy #0
        beq CopyWall
        cpy #7
        bne CopyMapStore
CopyWall:
        lda #$1F
CopyMapStore:
        sta mapRows,y
        dey
        bpl CopyMap
        ; Original top six PF bytes are identical in all 15 room tables.
        ; Reconstruct exact 48-byte pfbuf from 36 room bytes + shared top/bottom.
        ldy #35
CopyPF:
        lda (pfPtr),y
        sta pfbuf+6,y
        dey
        bpl CopyPF
        ldy #5
CopyPFTop:
        lda CommonTopPF,y
        sta pfbuf,y
        sta pfbuf+42,y    ; shared bottom row, identical in all 15 rooms
        dey
        bpl CopyPFTop
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

; Toggle true collision bit and both reflected PF 6/14-band bytes.
; Masks are the exact T <-> t XOR according to GRAPHICS V5.1 cell table.
ToggleTree:
; Inline DecodeKey to remove one live JSR frame. Six NOPs replace the
; original JSR+RTS 12-cycle envelope so downstream TIA/audio timing matches.
DecodeKeyInline:
        lda workKey
        ldx #0
DecodeLoopInline:
        cmp #5
        bcc DecodedKeyInline
        sec
        sbc #5
        inx
        bne DecodeLoopInline
DecodedKeyInline:
        sta workX
        stx workY
        nop
        nop
        nop
        nop
        nop
        nop
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
        sta renderDir
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
        st…974 tokens truncated…nter, never a pending target.
        ; A previously selected cell is indicated separately in the lower HUD.
        lda cursorX
        asl
        asl
        asl
        asl
        clc
        adc #12
        ldx #4           ; RESBL/HMBL: right rail or locked FIRE location
        jsr PositionOne
        lda #$20        ; NUSIZ0 missile width=4, owl P0 size unchanged
        sta NUSIZ0
        ; Current pointer and previous FIRE target are distinct concepts.
        ; A rejected new FIRE is displayed at the current pointer.
        ; A queued/committed action is only drawn on the in-scene pointer
        ; while the pointer still occupies the ORIGINAL fireX/fireY.
        ; Otherwise the old choice is shown by a separate HUD glyph.
        ldx #0
        lda ackFrames
        bne MarkerAckActive
        lda pending
        beq MarkerStyleChosen
        ldx #1           ; queued, not yet committed
        jmp MarkerCheckFireXY
MarkerAckActive:
        ldx ackType
        cpx #2           ; denial concerns the NEW attempted cursor cell
        beq MarkerStyleChosen
MarkerCheckFireXY:
        lda cursorX
        cmp fireX
        bne MarkerAtNewCell
        lda cursorY
        cmp fireY
        beq MarkerStyleChosen
MarkerAtNewCell:
        ldx #0           ; active pointer is neutral at a different cell
MarkerStyleChosen:
        lda CursorPlayLo,x
        sta candidateX       ; reuses non-kernel scratch, no new RIOT bytes
        lda CursorPlayHi,x
        sta candidateY
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
        sta COLUP1           ; approved exit amber on the same scanline
        jmp StonePaletteTail  ; shift source PC, retain original PF2 beam cycles
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
        sta workKey          ; original coda color retained for both P1 copies
        sta attempt
        jmp CodaSoundTail
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
        cmp #4
        bne ShadowCampaign
        ; Free-forest FIRE evokes negative space for 18 frames, no map edit.
        lda ackFrames
        beq ShadowGateDone
        lda #2
        sta shadowOn
        rts
ShadowCampaign:
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
; Conifer crowns 10 lines, stems 10; P0/P1 use safe lower-band raster slots.
RenderPlay:
        lda #$11       ; playfield mirror + 2px TIA ball rail
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
        sta WSYNC        ; use first of 15 original top HUD waits
        ldx renderDir
        lda OwlReflect,x
        sta REFP0
        jsr PrepareOwlFrame ; use the same budgeted top HUD line
        ldx #14
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
        ; Fir tips: narrow top for two scanlines, expand branches on line 3.
        ; Only TIA PF drawing changes: collision bits remain untouched.
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
        lda workX
        sta sprite0Ptr
        lda #>OwlB0         ; all U3 wing frames reside in one ROM page
        sta sprite0Ptr+1
        jmp OwlRowChosen
NoOwlOnRow:
        lda #<BlankSprite
        sta sprite0Ptr
        lda #>BlankSprite
        sta sprite0Ptr+1
OwlRowChosen:
        ; On crown line 3 restore the broader needle branches.
        sta WSYNC
        ldy pfIndex
        lda pfbuf,y
        sta PF0
        iny
        lda pfbuf,y
        and #$7D          ; narrower 2-pixel needle tier, x1 and x2
        sta PF1
        iny
        lda pfbuf,y
        and #$3E          ; narrower 2-pixel needle tier, x3 and x4
        ldx shadowOn
        beq NoCrownShadow
        ldx workY
        ora ShadowCrownOr,x
        and ShadowCrownAnd,x
NoCrownShadow:
        sta PF2
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
        ; Fifth crown line selects a pointer, not per-pixel mask gates.
        ; BlankSprite is 9 bytes of zero for noncursor rows; four approved
        ; original bitmap masks remain untouched. No new RAM or JSR.
        lda rowIndex
        cmp cursorY
        beq MarkerCurrentRow
        lda #<BlankSprite
        sta markerPtr
        lda #>BlankSprite
        sta markerPtr+1
        jmp MarkerGateDone
MarkerCurrentRow:
        lda candidateX
        sta markerPtr
        lda candidateY
        sta markerPtr+1
MarkerGateDone:
        lda workY
        sta candidateD    ; current mask frame index for the forthcoming stem
        inc workY         ; next crown row index; no extra work in hot PF2 scanline
        ; Crown ten lines / stem ten lines per 20-line cell.
        ; 1-2 = slender tip, 3-6 = two-pixel boughs, 7-10 = full spread.
        ; TIA only: collision geometry and U3/S3 originals are untouched.
        sta WSYNC           ; crown 6
        sta WSYNC           ; crown 7; expand the low branches
        ldy pfIndex
        lda pfbuf,y
        sta PF0
        iny
        lda pfbuf,y
        sta PF1
        iny
        lda pfbuf,y
        ldx shadowOn
        beq NoWideCrownShadow
        ldx workY
        ora ShadowCrownOr,x
        and ShadowCrownAnd,x
NoWideCrownShadow:
        sta PF2
        sta WSYNC           ; crown 8
        sta WSYNC           ; crown 9
        sta WSYNC           ; crown 10
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
        sta ENAM0
        lda attempt          ; seed P1-left stone color before first stem
        ldx #9
Stem13:
        sta WSYNC
        sta COLUP1          ; 3 cycles, ahead of first S3 at x66
        ldy SpriteRowIndex,x
        lda (sprite0Ptr),y
        sta GRP0
        lda (sprite1Ptr),y
        sta GRP1          ; first P1 copy (glyph A)
        ; Four cycles: preserve *exact* M0/BL/HUD and S3 beam positions.
        ; X=1 is executed via the isolated blank-line tail below.
        nop
        nop
        ; One chosen sprite byte supplies BOTH original M0 and BL bits.
        ; Gated via pointer during crown, not extra instructions on beam.
        ; M0 update at original c35, BL update at original c48.
        lda (markerPtr),y
        sta ENAM0
        nop
        nop
        nop
        nop
        lsr
        sta ENABL
        lda workKey        ; 3+3 replaces original 2+2 NOPs (+2 cycles)
        sta COLUP1          ; original amber before second S3 copy at x130
        lda (pfPtr),y
        sta GRP1          ; second P1 copy must still precede x135 latch
        lda attempt        ; seed next visible line without late red exit bleed
        dex
        cpx #1
        bne Stem13           ; 75 cycles worst normal, next line WSYNC
        ; The X=1 SpriteRowIndex entry is blank for both U3 and S3.
        ; Skip the unnecessary early COLUP1 write on that last blank line,
        ; keeping original first-HUD-PF1 update cycle unchanged.
StemLastBlank:
        sta WSYNC
        ldy SpriteRowIndex,x
        lda (sprite0Ptr),y
        sta GRP0
        lda (sprite1Ptr),y
        sta GRP1
        nop                  ; last line exactly 28 cycles to StemLastFast
        jmp StemLastFast
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
        ; Fixed, deliberately budgeted HUD preparation raster line.
        ; BOTH in-scene rails follow the live cursor. When another FIRE
        ; remains queued, this separated icon is anchored HORIZONTALLY
        ; below its former column (fireX), never mixed into the reticle.
        ; A second rejected FIRE renders a local in-scene X, while HUD
        ; continues to show the older pending ACCEPTED/QUEUED target.
        sta WSYNC
        ldx #0
        stx REFP0        ; lower P0 feedback is never mirrored
        lda pending
        beq HUDCheckAck
        ldx #1           ; pending target persists after second denied FIRE
        bne HUDChoose
HUDCheckAck:
        lda ackFrames
        beq HUDChoose
        ldx ackType
HUDChoose:
        lda CursorSpriteLo,x
        sta sprite0Ptr
        lda #>CursorIdle
        sta sprite0Ptr+1
        ; HUD has no HMOVE after RESP0, so only coarse timing is needed.
        ; floor((16*fireX+8)/15) = fireX + (fireX>=7).
        ; Carry marks the rightmost column; its RESP0 is one CPU cycle
        ; earlier to keep the following WSYNC before the line boundary.
        ldx fireX
        cpx #7
        bcc HUDCoarseReady
        inx
HUDCoarseReady:
        cpx #10
        sta WSYNC
        jsr HUDCoarseDelay
        sta RESP0
HUDIcon8:
        sta WSYNC
        ; 8-line HUD encodes the old fireY as a solid horizontal stroke
        ; at its 0..7 row. Together with fireX-derived P0 positioning this
        ; is a separate 2-D pending-target locator, NOT the live reticle.
        ; The seven other raster lines keep the approved feedback glyph.
        lda pending
        beq HUDNoQueuedRow
        tya
        eor #7
        cmp fireY
        bne HUDNoQueuedRow
        lda #$FF
        bne HUDGlyphReady
HUDNoQueuedRow:
        lda (sprite0Ptr),y
HUDGlyphReady:
        sta GRP0
        dey
        bpl HUDIcon8
        lda #0
        sta GRP0
        ldx #5             ; HUD preparation now has one explicit WSYNC
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
        sta REFP0
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
        ; Three prior identical loops = exactly 103 blank scanlines.
        ; Fold them into one to pay for the new FRI visual response.
        ldx #103
TitleGap:
TitleBlankSelectionBand:
TitleBottom:
        sta WSYNC
        dex
        bne TitleBottom
        rts

; Two JMP tails, no additional JSR or RIOT RAM. This source placement
; restores original cross-page NoStemShadow timing during PF2 first line.
StonePaletteTail:
        sta workKey
        ldx polarity
        beq StoneUsesAmber
        lda #$46
StoneUsesAmber:
        sta attempt
        jmp PlayScore
CodaSoundTail:
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

; RenderPlay depth is one; this call adds at most one (2 total).
PrepareOwlFrame:
        lda beatFrames
        ldx #0
        cmp #55
        bcc OwlFrameReady
        ldx #4
        cmp #61
        bcc OwlFrameReady
        cmp #67
        bcs OwlFrameReady
        ldx #8
OwlFrameReady:
        txa
        ora renderDir
        tax
        lda OwlFrameLo,x
        sta workX        ; preselected low byte, stable until next frame
        rts

        include "rom/src/data.inc"

; Issue48: SELECT must not leave mode=2 (room won) after resetting the room.
; A is still mode from ReadInput's CMP #3. Tail jump retains old JSR depth.
; Placed in existing padding so every existing renderer/score PC stays fixed.
SelectReload:
        cmp #2
        bne SelectReloadRoom
        dec mode
SelectReloadRoom:
        jmp LoadRoom
SelectReloadEnd:

; Same RESP0 write cycle for columns 0..8; column 9 is 3 pixels earlier.
; C is preserved by DEX/BPL/LDY/JSR. Branch-to-next gives 3/2 cycles.
HUDCoarseDelay:
        dex
        bpl HUDCoarseDelay
        ldy #7
        bcc HUDCoarseEnd
HUDCoarseEnd:
        rts
HUDCoarseDelayEnd:

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
