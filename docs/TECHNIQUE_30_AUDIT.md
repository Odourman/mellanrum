# MELLANRUM Issue26 – original 30 Atari tricks re-audited for actual 16K F6

**2026-11-23, native 16384-byte source.** This supersedes old Issue21 recommendations only for the new PR27 branch. All 30 original items were re-read from the original archived research and per-object reassessments in the six Google Docs below. The prior Let Me Out!/Skraun research is *advisory*, not proof for this different game or its F6 ROM. No claim is made that all 30 were implemented or benchmarked. `USED_AND_MEASURED` means source is present and a native Stella execution has observed its whole-game function; it does **not** assert a full instruction-level worst-case beam trace or physical chip PASS unless separately indicated.

| No. | Technique | Category | Actual Issue26 disposition / evidence boundary |
|---:|---|---|---|
| 01 | Sprite Multiplexing | `NOT_NEEDED` | Rows already use P0 owl and P1 doubled symbols; no extra same-row actor required. |
| 02 | Mid-scanline GRP Rewriting | `USED_AND_MEASURED` | Two different P1 glyph masks inside two far NUSIZ copies; source+real Stella rooms, register deadlines not exhaustively probed. |
| 03 | Venetian Blinds | `NOT_NEEDED` | U3/S3 8-line mask fidelity more important; prior cross-project 9-row FAIL not proof for this ROM. |
| 04 | Sprite Flickering | `NOT_NEEDED` | Recognizability and original eye/wing consistency; alternating missing frames rejected as design policy. |
| 05 | Dynamic Playfield Sprites | `USED_AND_MEASURED` | Presence uses PF2 OR/AND animation negative space rather than third player; original Stella views. |
| 06 | Mid-frame Sprite Resizing | `NOT_NEEDED` | Would change approved U3 silhouette and not add an object. |
| 07 | Asymmetric Playfield | `USED_AND_MEASURED` | Unmirrored left/right title kernel renders single-line MELLANRUM; gameplay stays deliberately reflected. |
| 08 | Two-Line Kernel | `NOT_NEEDED` | Existing 20 physical scanline cells with separate crown/stem maintain target appearance. |
| 09 | VDEL / Delayed Graphics | `NOT_NEEDED` | Existing reliable GRP writes; latch changes not justified without more TIA beam evidence. |
| 10 | HMOVE Fine Positioning | `USED_AND_MEASURED` | P0/P1/M0 coarse/fine placement present in actual native Stella 15-room campaign; worst per-line beam not fully measured. |
| 11 | Late HMOVE | `NOT_NEEDED` | Compatibility/race risk on original TIA revisions; no measured need. |
| 12 | Raster Color Changes | `USED_AND_MEASURED` | New F6 score updates COLUBK based on actual second TIA voice; old per-act COLUP? retained; original Stella screenshots. |
| 13 | 48-pixel / Six-Digit Score Kernel | `NOT_NEEDED` | No traditional score, fixed 48px graphic incompatible with symbolic spatial UI. |
| 14 | Multiple Display Kernels | `USED_AND_MEASURED` | Title separate from room raster kernel, plus banked offscreen audio code. |
| 15 | NUSIZ Sprite Duplication | `USED_AND_MEASURED` | Actual P1 double S3 glyph mask separation via NUSIZ1=$04; visual native frames. |
| 16 | Sprite Reflection REFP0/1 | `NOT_NEEDED` | U3 mirrored bitmap source is user-approved; runtime hardware flip would deform the beak direction. |
| 17 | Missile and Ball Reuse | `USED_AND_MEASURED` | M0 used for four state feedback widths, BL unused; actual symbol/cursor screenshots. |
| 18 | Playfield Score Mode | `NOT_NEEDED` | Would link trees to player color and weaken consistent green PF. |
| 19 | Playfield Priority Switching | `NOT_NEEDED` | Could obscure owl/symbol recognition; no dynamic priority reordering requirement. |
| 20 | Hardware Collision Latches | `NOT_NEEDED` | Deterministic mirrored-grid software collision is required; latches cannot identify logical queued tree. |
| 21 | RIOT Timer Scheduling | `USED_AND_MEASURED` | TIM64T and WSYNC schedule VBlank/overscan; 262 NTSC needs exact new F6 Gopher proof before all-frame gate. |
| 22 | Stack / RAM Mirroring | `NOT_NEEDED` | 128B RIOT RAM careful but no new RAM; prevent aliasing score interpreter and hardware stack. |
| 23 | Undocumented 6502 Opcodes | `NOT_NEEDED` | Real 6507 compatibility; no undocumented instructions in F6 interpreter. |
| 24 | Precomputed Tables / Cycle-exact Kernel | `USED_AND_MEASURED` | 15 distinct 5x768 three-stream score blocks read from F6, 15 PF maps, glyph/toggle tables; native DASM+Stella 15/15. Per-line cycle high-water still NOT_RUN. |
| 25 | Stack-based TIA Register Writes | `NOT_NEEDED` | Risk stack collision, banked JSR requires deterministic return PC. |
| 26 | Timing-Based Horizontal Scrolling | `NOT_NEEDED` | Rooms are static 10x8; camera movement would obscure agency rather than add gameplay. |
| 27 | SCABS Automatic Bank Switching | `INCOMPATIBLE_F6` | Special bank hardware, NOT equivalent to common built-in F6 address hot spots. |
| 28 | Extra Cartridge RAM / Superchip / Supercharger | `INCOMPATIBLE_F6` | Extra cart RAM prohibited, 128B RIOT only. |
| 29 | DPC Display Chip | `INCOMPATIBLE_F6` | Additional display coprocessor prohibited. |
| 30 | DPC+ / CDF / ARM | `INCOMPATIBLE_F6` | Modern helper CPU and special mapper prohibited. |

## Research, primary sources consulted again on 2026-11-23
- https://docs.google.com/document/d/1ASGA7wDZNsYNILVOswdQJfdvpOBtDKM2/edit
- https://docs.google.com/document/d/1lC3rz6VF8orv4W1rHSHqAFWZnOlAR5UWcmVfnphGcys/edit
- https://docs.google.com/document/d/1dFgqNPsUrEuSajvVC8gGB8odt3WPm54KQXlzUAMCbFI/edit
- https://docs.google.com/document/d/1XXDmQtS6AcrkP5_ojxen94GjITlEAT2bmzzGwV1ei3s/edit
- https://docs.google.com/document/d/13hW5xRwlcClMCNKn2j-iQ3BBBHOf48Y4drfzFz4-uhM/edit
- https://docs.google.com/document/d/1pvIl7dpS3NXS9sa-1C9ZxdrH2rtYL1e1/edit

## Why ordinary F6 matters (not one of the SCABS / chip tricks 27–30)
Four native DASM 4096-byte banks selected by ordinary cartridge F6 hotspots $1FF6–$1FF9. The actual added 11,520 live score/control bytes are a *data/code organization choice*, not an added TIA register channel. The same two real AUDCx/AUDFx/AUDVx sets feed all sound. The shared identical-PC trampoline and bank0–2 reset recovery are critical implementation work not equivalent to technique #27's SCABS.

## Measurement matrix
- **Native DASM/real Stella:** F6 identified at boot; 15/15 rooms won with joystick/FIRE, actual PCM callback and screenshot source hashes on new exact 16KiB SHA.
- **Real Gopher scanline-level and hardware worst-case timing:** separate F6 exact-SHA gate; do not reuse PR23's 202/202 observations.
- **Physical TIA/RetroN77:** NOT_RUN; low-level sound/visual difference user audition NOT_RUN.
- **30-trick cross-project negative outcomes:** historically relevant design reasons but NOT tests performed on this ROM. Accordingly rejected-but-unrun entries are `NOT_NEEDED`, not spurious `TESTED_AND_REJECTED`.
