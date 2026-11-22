# Mellanrum: aktuellt projektläge

**Updated:** 2026-11-22 (after ROM DEVELOPMENT full-game candidate handoff).
**Phase:** **V1 candidate / G1: INDEPENDENT_VERIFICATION_PENDING**.
**Implementation:** 15-room Atari 2600 / NTSC / standard 4K **candidate exists on PR #4 only**, branch `romdev/fullgame-20261122`, head `8bdecde79a6bc1ecb804484d5d257f4f1a99b052`. **PR open + Draft + unmerged.** Main branch does not yet contain the game.
**Release:** **NOT APPROVED**. Independent gameplay, visual, sound and hardware testing is not complete.

## What was actually checked by MAIN

- [PR #4](https://github.com/Odourman/mellanrum/pull/4): 31 changed files, entire V5.1 game logic candidate, original game maps/data, 6507 assembler, tests, CI workflows, reports.
- [Current-head native DASM CI](https://github.com/Odourman/mellanrum/actions/runs/45064977045): `SUCCESS` at exact head. Job logs show 4096-byte ROM, native DASM byte equality to independent developer subset assembler, V5.1 Python tests 20/20 and ROM-model comparisons 15/15 plus 225 random runs / 4352 ticks and developer raster checks.
- **MAIN independently downloaded and hashed the native Actions ROM bytes**: SHA-256 `ec791333da37613ec99ea70b2a983ecc1666b4e576211ece41a8e40bd14cbaed`; size 4,096; reset vector `$F000`; Stella reported NTSC / 4K.
- [Current-head Stella boot smoke](https://github.com/Odourman/mellanrum/actions/runs/45064977006): `SUCCESS`; extracted and examined four nonblank 320×228 original Stella PNG captures of title and gameplay. This supports a genuine Stella boot/title/snapshot smoke only; **not gameplay verification of all rooms or pixel/raster/sound fidelity**.
- Development source integrity (GRAPHICS 116/116 manifest, 25 8×8 mask records, 15 original rooms, 20/20 Python, 15/15 original room solutions) is documented in [developer source provenance](https://github.com/Odourman/mellanrum/blob/romdev/fullgame-20261122/docs/PROVENANCE.md). That original ZIP validation was **performed by ROM DEVELOPMENT and reported to MAIN**, not independently repeated by MAIN.

## MAIN verdict / next action

**Accepted for independent Verification only.** Request is recorded in [Issue #5](https://github.com/Odourman/mellanrum/issues/5), with [exact scope and acceptance matrix](MAIN_TO_VERIFICATION_PR4_2026-11-22.md). The [development issue #2](https://github.com/Odourman/mellanrum/issues/2) and [PR #4](https://github.com/Odourman/mellanrum/pull/4) remain open as applicable.

Verification should use immutable commit and ROM SHA, rebuild DASM cleanly, replay all 15 rooms using actual frame-level joystick input in a real Atari emulator, check input/echo/phase/Presence, TIA registers and long-run 262-line budget, watch title/intermediate/coda assets and both audio channels. PAL and real hardware are `NOT_IMPLEMENTED/NOT_RUN` unless independently tested.

## Deliberate developer design divergences that require review

- 4 KiB standard cartridge versus original 16 KiB F6 *provisional technical hypothesis*.
- Simplified mirrored abbreviated title, coda still uses ordinary forest rather than planned single-tree reduction, omitted optional Presence local PF seam and M1 chisel, reduced animation and transitions, FRI SKOG uses four source Act III geometries.
- These do not automatically invalidate model behavior but **must not silently be called full GRAPHICS visual conformance**. Evaluate with GRAPHICS/user if important.

## Authority and historical decisions

Project identity: [GitHub](https://github.com/Odourman/mellanrum) and [Drive folder](https://drive.google.com/drive/folders/1rO3ZTTBgyZZhqOx1WCxevM6sE3CrvUcl). User's full-game authorization was passed to ROM DEVELOPMENT in [full-game order](ROM_DEVELOPMENT_FULL_GAME_ORDER_2026-11-22.md). GAMEPLAN baseline V5.1 and `GITTERSKOG / BILDMELLANRUM` visual direction are implementation targets. Historic G0 source access limitations are documented in [V5.1 review](MAIN_V5_1_REVIEW_2026-11-22.md) and [Graphics intake](MAIN_GRAPHICS_V5_1_INTAKE_2026-11-22.md); the later developer's own source-validation does not make MAIN's earlier claims of inability false.

**Evidence status:** `DASM_BUILD_PASS`, `MAIN_ROM_HASH_MATCH`, `DEVELOPER_MODEL_PASS`, `STELLA_BOOT_SCREENSHOTS_SEEN`, `FULL_REAL_EMULATOR_GAMEPLAY_NOT_RUN`, `AUDIO_LISTEN_NOT_RUN`, `HARDWARE_NOT_RUN`, `PAL_NOT_IMPLEMENTED`, `INDEPENDENT_VERIFICATION_NOT_RUN`. Main has not merged or released any ROM.
