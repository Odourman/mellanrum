; GRAPHICS PR61 EXACT ART-ONLY CROWN FAMILY TABLE PROPOSALS
; SOURCE_ONLY / DO NOT IMPORT TO PRODUCT WITHOUT APPROVAL
; 8 patterns x 4 bytes (32 bytes per family).
GRAPHICS_Tree_Family_A:
    dc.b $C0,$06,$03,$30
    dc.b $A0,$06,$03,$50
    dc.b $C0,$0A,$05,$30
    dc.b $E0,$06,$03,$30
    dc.b $A0,$0A,$03,$50
    dc.b $C0,$06,$01,$30
    dc.b $A0,$06,$03,$70
    dc.b $C0,$0A,$03,$30
GRAPHICS_Tree_Family_B:
    dc.b $E0,$0E,$07,$70
    dc.b $C0,$0E,$07,$50
    dc.b $A0,$0E,$07,$30
    dc.b $E0,$06,$03,$70
    dc.b $C0,$0E,$07,$70
    dc.b $A0,$0E,$03,$70
    dc.b $E0,$0A,$07,$30
    dc.b $C0,$0A,$07,$70
; B additionally needs mid-crown tiering PF0 $20/$60/$F0,
; PF1 & $24/$5E/full and PF2 & $24/$3E/full.
; Cycles and actual color clocks NOT tested; no source layout patches.
