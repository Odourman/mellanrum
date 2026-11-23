# MELLANRUM – individually reviewed 30 original Atari 2600 techniques

**Source review completed 2026-11-23** against the four user-specified Drive technical studies (original, reassessment, Skraun cross-combinations, feasibility), plus HBLANK study and the canonical TIA/6507 constraints. These are cross-game advisory source documents, NOT proof that another game's results generalize to MELLANRUM.

**Final developer-stage status for this candidate:** All 30 names match exactly the original source list and are reviewed individually below. "USED_EMULATOR_OBSERVED" means the relevant behavior is in new source and observed in **new-SHA** Stella/Gopher integration, NOT that a per-TIA-register worst-case cycle proof or independent Verification exists. Hardware-specific rejected techniques were deliberately not tried. No old PR16 PASS transfers.

| No | Trick | Candidate status | MELLANRUM rationale |
|---:|---|---|---|
| 01 | Sprite multiplexing | NOT_NEEDED | P0 U3 owl and P1 pair retained; further vertical reuse risks masks |
| 02 | Mid-scanline GRP rewriting | USED_EMULATOR_OBSERVED | Existing dual S3 P1 rewrites; new exact raster re-measurement required |
| 03 | Venetian Blinds | REJECTED_WITH_REASON | Halving an 8/9-row owl or glyph makes them less legible; avoid |
| 04 | Sprite flickering | REJECTED_WITH_REASON | Removes reliable symbol/Presence legibility at 60 Hz |
| 05 | Dynamic Playfield Sprites | USED_EMULATOR_OBSERVED | Active tree/collision PF plus negative-space Presence; already source-integrated |
| 06 | Mid-frame sprite resizing | NOT_NEEDED | Would alter approved owl mask and not add resource |
| 07 | Asymmetric Playfield | NOT_NEEDED | Woodcut forest is intentionally reflected; asymmetry not needed for mechanics |
| 08 | Two-line kernel | NOT_NEEDED | Current U3/S3 raster uses carefully timed multi-line crown/stem; no two-line conversion proven |
| 09 | VDEL/delayed graphics | NOT_NEEDED | No proved gain with existing P0/P1 mask layout |
| 10 | HMOVE fine positioning | USED_EMULATOR_OBSERVED | Inherited P0/P1/M0 coarse/fine TIA placement from PR16; needs native recheck |
| 11 | Late HMOVE | REJECTED_WITH_REASON | Could disturb left edge; native TIA clone compatibility risk |
| 12 | Raster color changes | NOT_USED_MIDSCANLINE | Current act/polarity palette and two-channel tonal scene; dynamic row color not yet proven |
| 13 | 48-pixel score kernel | NOT_NEEDED | No score by design; title uses separate PF word kernel |
| 14 | Multiple display kernels | USED_EMULATOR_OBSERVED | Inherited title vs active PF + U3/S3 render distinct routines; native retest pending |
| 15 | NUSIZ sprite duplication | USED_EMULATOR_OBSERVED | Existing two far P1 glyph copies via NUSIZ1=$04; native recheck pending |
| 16 | Sprite reflection | NOT_USED_REFP_BITMAP_MIRRORED | PF mirror deliberately used; reflecting approved U3 horizontally again would break art |
| 17 | Missile/Ball reuse | USED_EMULATOR_OBSERVED | M0 1/2/4/8 feedback states; no need for BL yet; source integrated |
| 18 | Playfield score mode | REJECTED_WITH_REASON | PF green forest and owl hues must remain distinct; unsuitable |
| 19 | Playfield priority switching | NOT_NEEDED | Evaluate P0 owl occluding S3: no actual priority rewrite implemented yet |
| 20 | Collision latches | NOT_NEEDED | Game collision uses mirrored live mapRows; latches cannot identify reflected targets |
| 21 | RIOT timer scheduling | USED_EMULATOR_OBSERVED | Existing TIM64T VBLANK/overscan frame budget retained; retest pending |
| 22 | Stack/RAM mirroring | REJECTED_WITH_REASON | Previously only 14 bytes nominal stack room; risks corruption |
| 23 | Undocumented 6502 opcodes | REJECTED_WITH_REASON | Not guaranteed across assemblers/clones; avoid |
| 24 | Precomputed tables/cycle-exact kernels | USED_TABLES_CYCLE_TRACE_OPEN | Existing RoomGateKey/PatchKey, column lookup, dual P1 rewrite and 76-cycle design; rerun required |
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

## Native integration measurement evidence, exact new ROM

**Standard Atari 2600, NTSC, native DASM 4096 bytes, no mapper**; SHA-256 `18163c0435347695ee1cff5a4b6b19c80d280ec255eeb7f9b98711471ccde11c`.
- [Actual new SHA native DASM, source/regression and conservative stack](https://github.com/Odourman/mellanrum/actions/runs/45146265215): 4096 bytes, byte-identical to separate assembler; static call depth 5 JSR = 10 stack bytes; highest RIOT-RAM symbol $F1 leaves 14 stack bytes and 4-byte static margin. **Dynamic SP trace NOT_RUN**.
- [Actual native Gopher2600 and real Stella campaigns](https://github.com/Odourman/mellanrum/actions/runs/45146044733): both completed 15/15 room victory and coda/title solely through controller; Gopher 162/162 sample frames had **262 NTSC scanlines**. Hardware per-register beam-cycle trace NOT_RUN. Genuine Stella original graphics/screenshots and real stereo TIA PCM present.
- [Actual 15-room 600s real Stella idle](https://github.com/Odourman/mellanrum/actions/runs/45146044746): 15×36000 frames, 0 automatic wins, thereafter all 15 rooms solved via normal controller and SELECT restart.
- [15 real Stella input counterfactuals](https://github.com/Odourman/mellanrum/actions/runs/45146044908): omit each room's targeted resonant tree FIRE, 15/15 blocked in same frame-indexed trace (original win+1200 frames); no POKE or patched ROM.

### Techniques observed and limitations

- **#02 + #15:** Original actual S3-A/B user-preferred bitmaps rendered on duplicated P1 NUSIZ1=$04 with mid-scanline GRP1 rewrites; actual Stella/Gopher screenshots across room screenshots. Exact new SHA screenshot-pixel per-register timing not separately audited.
- **#05:** Physical PF and collision rows change from real controller FIRE; negative-space Presence source mask and true emulated graphics observable in Act III. This is PF source manipulation and row rendering; no claim of adding a third independent TIA color domain.
- **#10:** Source uses real coarse+fine P0/P1/M0 placement. Actual screenshot geometry visible, but no independent beam-cycle HMOVE deadline trace.
- **#14:** Separate title and game display kernels genuinely executed in both emulators, coda/title replay documented.
- **#17:** M0 cursor width/feedback retained and COLUP0 colors expanded (neutral, accepted, denied, intercept, plus gold resonance hover). M0 shares owl P0 hue; no independent extra color domain or BL claimed.
- **#21:** Real RIOT timer and stable sampled 262-line NTSC, no separate worst-case register-cycles-for-every-line measurement.
- **#24:** Precomputed authored source tables RoomGateKey/RoomPatchKey and VBLANK work; real 262-sample evidence but a full cycle-exact trace is still open.
- **#12 and #16 specifically NOT used** as mid-scanline color rewrite and REFP hardware mirroring, respectively: per-scene palette swaps and source-pre-mirrored U3 are distinct techniques.
- **#03/#04 and #27–30 rejected here:** hidden-line/flicker compromises for readable U3/S3 or unsupported hardware, not a universal condemnation of those techniques in other games.

**Original external sources remain advisory; new emulator evidence is only for `18163c0435347695ee1cff5a4b6b19c80d280ec255eeb7f9b98711471ccde11c`.** All unlisted statuses remain chosen source decisions rather than misleading experimental claims.
