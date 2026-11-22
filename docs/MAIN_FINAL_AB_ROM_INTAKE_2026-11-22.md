# MAIN — FINAL A/B ROM CANDIDATE INTAKE, 2026-11-22

**Status:** `MAIN_ARTIFACT_INTAKE_PASS / BUILD_PASS / STELLA_AB_VISUAL_PASS / FULL_GAME_STRESS_NOT_RUN / RELEASE_BLOCKED`.

## Identity and source

- Main verified [Draft PR #4](https://github.com/Odourman/mellanrum/pull/4) is OPEN/DRAFT/NOT MERGED, exact HEAD **`49eb168b17d0254d06cf50d87c60e8fb6016db6e`**.
- Game-source commit **`6cb86247c668162b180e5d77377098941b9803b3`**. Later changes at `49eb...` add documentation and real-Stella evidence, not another product ROM according to the developer's report.
- **Native DASM Atari 2600 NTSC standard 4K ROM: 4096 bytes, SHA256 `e9ea87d381bcf8da39ec055d7d6951ceff97b21d3a798addd10fbbe540c5e974`**. This supersedes older intermediate native SHA `a9531d5b...`, `d1005a...` and pre-title SHA `ec791333...`.
- [Native + model full-game developer CI](https://github.com/Odourman/mellanrum/actions/runs/45075716636) `SUCCESS`, commit `49eb...`, artifact **`14775257125`**. MAIN downloaded that exact ZIP. **ZIP CRC valid; 5 entries; `mellanrum_ntsc.bin` exactly 4096 bytes; independently calculated SHA256 matched the expected full hash.** Actual DASM listing, symbol output, CPU trace and SHA manifest included.
- [A/B real-Stella run](https://github.com/Odourman/mellanrum/actions/runs/45075039996) `SUCCESS`, workflow commit `e9eeb668a66254582f2e5ea58b96ffff26418979`, artifact **`14774798060`**. MAIN downloaded that exact ZIP. **ZIP CRC valid; 31 entries, including 12 curated ordinary production-ROM title/gameplay PNGs, actual key-event TSV, additional raw Stella snapshots/listing and `mellanrum_ntsc.bin` 4096 bytes with the SAME independently calculated SHA256**.
- [Developer detailed outcome at exact PR HEAD](https://github.com/Odourman/mellanrum/blob/49eb168b17d0254d06cf50d87c60e8fb6016db6e/docs/ISSUE9_AB_HARDWARE_REPORT.md) and [original evidence README](https://github.com/Odourman/mellanrum/blob/49eb168b17d0254d06cf50d87c60e8fb6016db6e/evidence/issue9/README.md). Raw emulated input events timestamped in seconds, **not frame-indexed**.

## Implemented user-authorized controls (MEL-037)

- Console **LEFT Difficulty A = Campaign (normal; 15 rooms)** / **B = FRI SKOG**. The physical switch position is authoritative at FIRE-from-title; cannot be moved by ROM. RIGHT Difficulty ignored.
- Joystick and SELECT have NO title-mode-select function. FIRE starts LEFT A/B selection. RESET returns title. Next FIRE re-reads A/B; mid-game switches do not change already latched mode. SELECT inside gameplay restarts room within same mode.
- Title shows one horizontal `MELLANRUM` and no mode text or selectable icon. Source render-only negative-space Presence effect from Issue #8 unchanged.
- Developer reports 20/20 reference tests, 15/15 abstract model room solutions, 225 seeded model runs (4352 tick comparisons), 20 PF mutation checks and developer CPU/WSYNC model 262-line frames. These results are **not** independent physical ROM game traversal.
- Real Stella A/B screenshots + log show distinct campaign and free-mode imagery after hardware input, title unaffected by SELECT/joystick, correct RESET+FIRE mode changes; still only black-box visual evidence, not direct RIOT register inspection.

## Unverified boundaries

- **Actual Stella/Gopher debugger `SWCHB` bit6 + RAM mode variable direct trace: `NOT_VERIFIED`.** Two developer probes launched but did not persist a readable transcript despite green workflow status; cannot claim direct RAM verification.
- 15 rooms reached and won through **normal real-emulator joystick events**, 8-s coda, true 262 raster/timing/collisions, human A/V fidelity, real TIA WAV recording, hard TIA audio register checks: `NOT_RUN / PENDING`.
- Presence was visually demonstrated in true Stella using separate instrumented Reset-only room/tick variant ROMs in Issue #8. Actual access during normal campaign and exact timing in unchanged production ROM still `NOT_VERIFIED` from a player route.
- Original physical Atari 2600 and Hyperkin RetroN 77 SKILL P1 hardware: `NOT_RUN`; PAL `NOT_IMPLEMENTED` on this NTSC-only cartridge.
- Independent Verification (Issue #5), user art acceptance, merge and release `PENDING`. Old Pachinko result is bound to old SHA; no evidence inheritance.

## MAIN decision & exact next assignment

**Freeze exact `49eb168b17d0254d06cf50d87c60e8fb6016db6e` + ROM `e9ea87d381bcf8da39ec055d7d6951ceff97b21d3a798addd10fbbe540c5e974` for Pachinko 2.0 diagnostic test.** This is a test-target freeze, **NOT** final acceptance or merge.

- [Binding final Pachinko full-suite order](MAIN_TO_PACHINKO_2_0_FINAL_AB_E9EA_FULL_TEST_2026-11-22.md). It supersedes Stage0's 'wait for A/B revision' requirement; Stage0 tooling can be reused, now target new SHA. [Issue #7](https://github.com/Odourman/mellanrum/issues/7).
- [Independent Verification Issue #5](https://github.com/Odourman/mellanrum/issues/5) must independently rebuild/check same exact ROM and separately test reported critical risks. Pachinko is only diagnostic, not the independent release arbiter.
- No scope expansion for ROM DEVELOPMENT, no code fix authorized absent reproduced bug and new separate MAIN authorization. PR #4 stays Draft; NO RELEASE until human review and independent Verification.
