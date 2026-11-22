; MELLANRUM / independent 4K NTSC frame DIAGNOSTIC.
; NOT the final game, not the 16K F6 cartridge, not emulator verified.
; Standalone DASM 6502; intended to exercise assembler CI.
    processor 6502

VSYNC   = $00
VBLANK  = $01
WSYNC   = $02
COLUPF  = $08
COLUBK  = $09
CTRLPF  = $0A
PF0     = $0D
PF1     = $0E
PF2     = $0F

    ORG $F000
Reset
    sei
    cld
    ldx #$FF
    txs
    lda #$00
    sta COLUBK
    lda #$C8
    sta COLUPF
    lda #%00000001
    sta CTRLPF
    lda #%11110000
    sta PF0
    lda #%01010101
    sta PF1
    lda #%11001100
    sta PF2

Frame
    lda #$02
    sta VSYNC
    ldx #3
SyncLoop
    sta WSYNC
    dex
    bne SyncLoop
    lda #$00
    sta VSYNC

    lda #$02
    sta VBLANK
    ldx #37
BlankLoop
    sta WSYNC
    dex
    bne BlankLoop
    lda #$00
    sta VBLANK

    ldx #192
VisibleLoop
    sta WSYNC
    dex
    bne VisibleLoop

    lda #$02
    sta VBLANK
    ldx #30
OverscanLoop
    sta WSYNC
    dex
    bne OverscanLoop
    jmp Frame

    ORG $FFFC
    word Reset
    word Reset
