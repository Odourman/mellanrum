# MELLANRUM Issue #21 – 30 Atari 2600 tricks, source-first audit

Scope: source evaluation 2026-11-23 of 30 original tricks in four linked Google Drive original/reassessment reports. Cross-project source-only guidance is not this game's validation. Existing PR16 native emulator observations are HISTORICAL. Any vNext modified ROM requires its OWN native DASM, Gopher, Stella and beam/pixel evidence. A status `USED_AND_MEASURED` below means used with PR16 measurements, **not vNext PASS**. Treat this as a living audit; do not claim every trick was experimentally run.

| # | Technique | Status | Reason and evidence boundary |
|---:|---|---|---|
| 01 | Sprite multiplexing | NOT_NEEDED | P0 U3 and P1 double symbol already occupy main active band; extra sprite reuse only if an evidenced screen zone demands it. |
| 02 | Mid-scanline GRP rewriting | USED_AND_MEASURED | Current source uses two timed GRP1 writes per active row for different P1 sigils; carry-over from PR16, vNext retest mandatory. |
| 03 | Venetian blinds | REJECTED_WITH_REASON | Interlaced rows would sacrifice recognizable 8-line U3/S3 masks. Another game's negative test does not prove universal failure. |
| 04 | Sprite flickering | REJECTED_WITH_REASON | Visible blinking of owl/sigils defeats user's legibility requirement; no vNext flicker trial. |
| 05 | Dynamic playfield sprites | USED_AND_MEASURED | Source PF2 negative-space Presence B is an already emulator-audited render effect in PR16; vNext independent measurement pending. |
| 06 | Mid-frame sprite resizing | NOT_NEEDED | U3 shape is locked and resize doesn't add distinct bitmap capacity. |
| 07 | Asymmetric playfield | NOT_NEEDED | Current room silhouette is mirrored by contract; asymmetric decor could be evaluated after geometry and timing budget. |
| 08 | Two-line kernel | NOT_NEEDED | Current per-row crown/stem 20-line routine preserves 8px figures; two-line tradeoff unnecessary until measured overflow. |
| 09 | VDEL/delayed graphics | NOT_NEEDED | No demonstrated gain beyond present P0/P1 raster writes, must test latch ordering if introduced. |
| 10 | HMOVE fine positioning | USED_AND_MEASURED | Existing code positions real P0/P1/M0 with hardware fine motion; prior PR16 Gopher/Stella evidence, vNext needs remeasure. |
| 11 | Late HMOVE | REJECTED_WITH_REASON | Avoid TIA revision/race-sensitive late strobe without measured artifact. |
| 12 | Raster color changes | USED_AND_MEASURED | Existing source writes COLUP0/COLUP1/COLUPF/COLUBK; act palette and Presence work; vNext visual gate open. |
| 13 | 48-pixel/six-digit kernel | REJECTED_WITH_REASON | No score HUD; a fixed 48px sequence steals P0/P1 resources from owl and glyphs. |
| 14 | Multiple display kernels | USED_AND_MEASURED | Existing title PF word kernel distinct from active game kernel; inherited proof PR16, vNext source verification pending. |
| 15 | NUSIZ sprite duplication | USED_AND_MEASURED | NUSIZ1=$04 gives two P1 glyph copies; 64 color clocks, actual old 15-room bitmap evidence. |
| 16 | Sprite reflection | NOT_NEEDED | U3 bytes already reflect user's accepted image; runtime REFP0 could reverse recognized shape. |
| 17 | Missile/ball reuse | USED_AND_MEASURED | M0 cursor with four widths, BL spare; future readability work must show real pixels. |
| 18 | PF score mode | REJECTED_WITH_REASON | Palette conflicts with green trees; adds no necessary mechanic. |
| 19 | Playfield priority switching | NOT_NEEDED | P0/S3 occlusion requires real visual evaluation; priority may change owl/tree stacking, not automatically fix P0/P1 overlap. |
| 20 | Collision latches | NOT_NEEDED | Collision rules implemented in mirrored logical map; latch would not identify multiplexed distinct glyph reliably. |
| 21 | RIOT timer scheduling | USED_AND_MEASURED | TIM64T VBLANK and overscan loops plus WSYNC carry NTSC raster, prior native Gopher 262 observed. |
| 22 | Stack/RAM mirroring | REJECTED_WITH_REASON | 128-byte RIOT RAM tight; stack sharing risks unstable state; measure max stack before any reuse. |
| 23 | Undocumented 6502 opcodes | REJECTED_WITH_REASON | Avoid undocumented behavior on original 6507, real hardware compatibility priority. |
| 24 | Precomputed tables/cycle-exact kernel | USED_AND_MEASURED | PF packing/toggle masks, room tables, GRP deadlines and scanline script inherited from PR16; vNext beam profiling pending. |
| 25 | Stack-based TIA writes | REJECTED_WITH_REASON | No measured benefit; stack safety more important than marginal cycles. |
| 26 | Timing-based scrolling | REJECTED_WITH_REASON | Static 10x8 rooms, scrolling harms intended intimate playfield. |
| 27 | SCABS bankswitching | REJECTED_WITH_REASON | Special bank hardware prohibited; prefer ordinary F6 if >4KiB. |
| 28 | Extra cart RAM/Superchip/Supercharger | REJECTED_WITH_REASON | Forbidden custom extra cartridge RAM, RIOT RAM only. |
| 29 | DPC hardware | REJECTED_WITH_REASON | Proprietary supplementary display chip outside unmodified-cartridge target. |
| 30 | DPC+/CDF/ARM | REJECTED_WITH_REASON | Modern cartridge coprocessors prohibited by Issue21. |

## Research consulted
- https://docs.google.com/document/d/1ASGA7wDZNsYNILVOswdQJfdvpOBtDKM2/edit
- https://docs.google.com/document/d/1lC3rz6VF8orv4W1rHSHqAFWZnOlAR5UWcmVfnphGcys/edit
- https://docs.google.com/document/d/1dFgqNPsUrEuSajvVC8gGB8odt3WPm54KQXlzUAMCbFI/edit
- https://docs.google.com/document/d/13hW5xRwlcClMCNKn2j-iQ3BBBHOf48Y4drfzFz4-uhM/edit

## Hardware gate
Ordinary Atari 2600 NTSC 6507/TIA, maximum 16384 ROM bytes, F6 only if banking needed. For `USED_AND_MEASURED`, repeat real-emulator tests after vNext changes and record exact SHA, test command, observed byte/cycle/frame/pixel evidence; downgrade to NOT_RUN if a particular vNext technique is not executed. No undocumented CPU, SCABS, added cart RAM or DPC/CDF/ARM.
