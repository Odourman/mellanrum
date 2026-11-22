# MAIN → ROM DEVELOPMENT: Hardware-only A/B mode selection

**Date:** 2026-11-22
**Authorization:** user design decision MEL-037. This is a **NEW, SEPARATE post-Issue-8 implementation order**; do not reinterpret the previous title+Presence order. Implement only the already agreed hardware-mode selection and necessary UI/input-regression support. This document grants the implementation authorization now that ROM DEVELOPMENT has completed its previous task.

## Source freeze / prerequisite

- PR #4 still open Draft; known visual revision HEAD `eea14339010306de635a8c6238e242b76b28cc64`.
- Latest **actually byte-measured** build at that HEAD: 4,096-byte NTSC ROM SHA256 `a9531d5bbbff033711fbe54f8688b8e0259640e0a9a284c8ab585eea415c0bd5`. Original prior `ec791...` SHA and intermediate `d1005a...` are not the current candidate.
- [MAIN Issue-8 intake](MAIN_ROMDEV_ISSUE8_INTAKE_2026-11-22.md); [Issue #8](https://github.com/Odourman/mellanrum/issues/8), [MEL-037](DECISIONS.md), original V5.1 and GRAPHICS authorities.
- Do not change the newly delivered complete MELLANRUM title or render-only negative-space Presence rules, other original room mechanics, audio, or art to achieve A/B.

## Normative user behavior

1. **Left console Difficulty A = Campaign (15 rooms), recommended/standard mode; left Difficulty B = FRI SKOG** (free mode with no goal). Read hardware RIOT/SWCHB bit 6, not joystick input: Stella debugger references `_diff0A = *SWCHB & $40` and `_diff0B = !(*SWCHB & $40)`. A has bit6 set, B clear. Official documentation: https://stella-emu.github.io/docs/debugger.html. Confirm bit polarity against real running emulator rather than guessing.
2. **Mode selection may ONLY come from physical left console A/B selector** or its faithful emulator/RetroN hardware mapping. No joystick direction or FIRE-selection menu may choose between the modes. FIRE merely starts selected mode. Right difficulty ignored for mode. SELECT (console's SELECT) must never change mode. On the title, SELECT may be a no-op; during gameplay preserve any unrelated SELECT behavior (such as restart same room) insofar as it does not change gameplay mode. RESET returns to title; current A/B position is read at next FIRE start.
3. **Latch A/B upon FIRE start**; changing difficulty during an ongoing room must not suddenly switch campaign/free mode. A/B change only applies at next FIRE from title after RESET/normal return. Changing controls during title before FIRE must deterministically change eventual start mode.
4. The only displayed word on the title remains **MELLANRUM**. Remove or render decorative any formerly *selectable* campaign/free icons; if read-only current hardware setting indication is preserved, it cannot look like a joystick-navigable selector. No text KAM/FRI or extra menu words. Simplest preferred result is one title word, no selection UI.
5. **Hardware 'default' caveat:** Atari 2600 software cannot physically force the mechanical difficulty switch to A. Campaign is the standard **mapping for left A**, and README/manual instructions should tell users to place left switch at A. If B is physically set at boot, user explicitly requests B→FRI. Emulator startup properties may be configured as A for testing, but do NOT silently override B in game code or pretend hardware can be moved by ROM.
6. Keep all other functionality unchanged, original V5.1 complete 15-room maps, TIA 262 NTSC-line budget, both audio channels, stable persistent Presence and echo timing. Keep PR Draft/no merge.

## Required automated developer tests and actual-emulator evidence

- Clean native DASM build, expected **NEW** immutable commit + actual new ROM SHA, exact binary size and retained source geometry; no fabricated reused `a953...` hash.
- Stella console simulated **F5 LEFT A**, **F6 LEFT B**, **F7/F8 RIGHT** (official key mapping https://stella-emu.github.io/docs/). Verify actual `SWCHB` state read and actual selected `mode` in emulator RAM at FIRE.
- Matrix: initial left A→Campaign R01; left B→FRI; A/B switch while title then FIRE; held FIRE one-shot; joystick UP/DOWN/LEFT/RIGHT on title no effect; SELECT on title no mode change; right A/B no effect; RESET during both modes; left A/B toggle in running game no midgame change; change difficulty then RESET+FIRE applies next title; original in-game SELECT restart (if preserved) does not change mode.
- Real title captures in left A and B settings with only word `MELLANRUM`. At least 2 real emulator runs prove each mode starts via FIRE, not just Python model. Test title scanlines in actual Stella debugger (262/frame) where possible; report NOT_RUN honestly.
- Confirm actual RetroN77 hardware button mapping/availability as test target; if inaccessible mark hardware NOT_RUN. Native Atari 2600 and Stella compatibility first.
- Run all existing original room/visual/Presence developer regressions; save native DASM listing, .sym, ROM, input log, real PNGs, new checksum manifest and test-matrix PASS/FAIL/NOT_RUN. Independent Verification and full Pachinko 2.0 run after this commit, with no inherited PASS from `a953...`.

## Handoff and boundaries

Return exact new PR commit, ROM SHA, source patch, issue comments and native Actions links, test data including LEFT/RIGHT Difficulty screenshots, and precise limitation. No independent release PASS, PR merge or unrelated game canon work. MAIN will then freeze the new SHA for PACHINKO 2.0 and independent VERIFICATION.
