; GRAPHICS U3 VERTICAL BEAK: 9-byte bottom-up + trailing 00.
; Source-only; do not modify product ROM.
; top-down FF E7 -> EF EF, eyes DB remain unchanged.
U3Beak_B0:
    dc.b $24,$7E,$7E,$EF,$EF,$DB,$7E,$18,$00
U3Beak_B1:
    dc.b $24,$BD,$FF,$EF,$EF,$DB,$7E,$18,$00
U3Beak_B2:
    dc.b $24,$FF,$FF,$EF,$EF,$DB,$7E,$18,$00
