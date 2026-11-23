# MELLANRUM – individually reviewed 30 original Atari 2600 techniques

**Source review completed 2026-11-23** against the four user-specified Drive technical studies (original, reassessment, Skraun cross-combinations, feasibility), plus HBLANK study and the canonical TIA/6507 constraints. These are cross-game advisory source documents, NOT proof that another game's results generalize to MELLANRUM.

**Honest interim status:** `PENDING_NEW_ROM_MEASUREMENT` is explicitly provisional and must become `USED_AND_MEASURED`, `EXPERIMENTED_FAILED`, `REJECTED_WITH_REASON`, or `NOT_NEEDED` based on genuine *new candidate* emulator evidence. No prior PR16 emulator PASS automatically transfers. Older Let Me Out! negative Venetian Blinds tests only apply to their exact prior experiments.

| No | Trick | Candidate status | MELLANRUM rationale |
|---:|---|---|---|
| 01 | Sprite multiplexing | NOT_NEEDED | P0 U3 owl and P1 pair retained; further vertical reuse risks masks |
| 02 | Mid-scanline GRP rewriting | PENDING_NEW_ROM_MEASUREMENT | Existing dual S3 P1 rewrites; new exact raster re-measurement required |
| 03 | Venetian Blinds | REJECTED_WITH_REASON | Halving an 8/9-row owl or glyph makes them less legible; avoid |
| 04 | Sprite flickering | REJECTED_WITH_REASON | Removes reliable symbol/Presence legibility at 60 Hz |
| 05 | Dynamic Playfield Sprites | PENDING_NEW_ROM_MEASUREMENT | Active tree/collision PF plus negative-space Presence; already source-integrated |
| 06 | Mid-frame sprite resizing | NOT_NEEDED | Would alter approved owl mask and not add resource |
| 07 | Asymmetric Playfield | NOT_NEEDED | Woodcut forest is intentionally reflected; asymmetry not needed for mechanics |
| 08 | Two-line kernel | NOT_NEEDED | Current U3/S3 raster uses carefully timed multi-line crown/stem; no two-line conversion proven |
| 09 | VDEL/delayed graphics | NOT_NEEDED | No proved gain with existing P0/P1 mask layout |
| 10 | HMOVE fine positioning | PENDING_NEW_ROM_MEASUREMENT | Inherited P0/P1/M0 coarse/fine TIA placement from PR16; needs native recheck |
| 11 | Late HMOVE | REJECTED_WITH_REASON | Could disturb left edge; native TIA clone compatibility risk |
| 12 | Raster color changes | PENDING_NEW_ROM_MEASUREMENT | Current act/polarity palette and two-channel tonal scene; dynamic row color not yet proven |
| 13 | 48-pixel score kernel | NOT_NEEDED | No score by design; title uses separate PF word kernel |
| 14 | Multiple display kernels | PENDING_NEW_ROM_MEASUREMENT | Inherited title vs active PF + U3/S3 render distinct routines; native retest pending |
| 15 | NUSIZ sprite duplication | PENDING_NEW_ROM_MEASUREMENT | Existing two far P1 glyph copies via NUSIZ1=$04; native recheck pending |
| 16 | Sprite reflection | PENDING_NEW_ROM_MEASUREMENT | PF mirror deliberately used; reflecting approved U3 horizontally again would break art |
| 17 | Missile/Ball reuse | PENDING_NEW_ROM_MEASUREMENT | M0 1/2/4/8 feedback states; no need for BL yet; source integrated |
| 18 | Playfield score mode | REJECTED_WITH_REASON | PF green forest and owl hues must remain distinct; unsuitable |
| 19 | Playfield priority switching | NOT_NEEDED | Evaluate P0 owl occluding S3: no actual priority rewrite implemented yet |
| 20 | Collision latches | NOT_NEEDED | Game collision uses mirrored live mapRows; latches cannot identify reflected targets |
| 21 | RIOT timer scheduling | PENDING_NEW_ROM_MEASUREMENT | Existing TIM64T VBLANK/overscan frame budget retained; retest pending |
| 22 | Stack/RAM mirroring | REJECTED_WITH_REASON | Previously only 14 bytes nominal stack room; risks corruption |
| 23 | Undocumented 6502 opcodes | REJECTED_WITH_REASON | Not guaranteed across assemblers/clones; avoid |
| 24 | Precomputed tables/cycle-exact kernels | PENDING_NEW_ROM_MEASUREMENT | Existing RoomGateKey/PatchKey, column lookup, dual P1 rewrite and 76-cycle design; rerun required |
| 25 | Stack-based TIA tricks | REJECTED_WITH_REASON | Interrupt/stack risk and no compelling raster saving yet |
| 26 | Timing-based scrolling | NOT_NEEDED | Screen consists of fixed rooms, not scrolling |
| 27 | SCABS bank switching | REJECTED_WITH_REASON | Specialized mapper violates conventional F6 target |
| 28 | Extra cartridge RAM/Superchip | REJECTED_WITH_REASON | Hardware restriction explicitly disallows extra cartridge RAM |
| 29 | DPC processor | REJECTED_WITH_REASON | Nonstandard hardware prohibited |
| 30 | DPC+/CDF/ARM processors | REJECTED_WITH_REASON | Modern cartridge compute assistance prohibited |

## Sources directly read in Google Drive
- [Original 30](https://docs.google.com/document/d/1ASGA7wDZNsYNILVOswdQJfdvpOBtDKM2/edit)
- [30 techniques reassessed](https://docs.google.com/document/d/1lC3rz6VF8orv4W1rHSHqAFWZnOlAR5UWcmVfnphGcys/edit)
- [Skraun combined techniques](https://docs.google.com/document/d/1dFgqNPsUrEuSajvVC8gGB8odt3WPm54KQXlzUAMCbFI/edit)
- [Hardware feasibility](https://docs.google.com/document/d/13hW5xRwlcClMCNKn2j-iQ3BBBHOf48Y4drfzFz4-uhM/edit)
- [HBLANK analysis](https://docs.google.com/document/d/1XXDmQtS6AcrkP5_ojxen94GjITlEAT2bmzzGwV1ei3s/edit)
- [Atari programming bibliography](https://docs.google.com/document/d/1pvIl7dpS3NXS9sa-1C9ZxdrH2rtYL1e1/edit)

## Evidence gates
A genuine native DASM build is only `BUILD_PASS`; RAM/stack/HMOVE timing, original Gopher/Stella screenshots, ACT III Presence audio, and 15 real-input game completions are separate gates. Future evidence reports must include exact ROM SHA, emulator revision, raster and source commit.
