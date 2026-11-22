# MAIN → PACHINKO 2.0: post-visual delivery test infrastructure, final SHA gate

**Date:** 2026-11-22. **Stage:** STAGE 0 authorized to begin immediately; final all-system test waits for ROM DEVELOPMENT's separate A/B hardware-only implementation. **NOT RUN YET.**

## Read these authorities first

1. [Current Project State](CURRENT_PROJECT_STATE.md) / [Decisions including MEL-037 and MEL-039](DECISIONS.md) / [Source Registry](SOURCE_REGISTRY.md).
2. [PACHINKO 2.0 complete end-to-end design and mandatory CI coverage](MAIN_TO_PACHINKO_2_0_FULL_COVERAGE_2026-11-22.md); [Full E2E stress plan](MAIN_FULL_END_TO_END_STRESS_TEST_PLAN_2026-11-22.md).
3. [MAIN reviewed Issue #8 revision](MAIN_ROMDEV_ISSUE8_INTAKE_2026-11-22.md); [Original ROM DEVELOPMENT matrix](https://github.com/Odourman/mellanrum/blob/eea14339010306de635a8c6238e242b76b28cc64/docs/ISSUE8_TEST_MATRIX_2026-11-22.md).
4. [User-directed new hardware-only A/B selector order](MAIN_TO_ROMDEV_AB_HARDWARE_ONLY_2026-11-22.md) and [ROM DEVELOPMENT Issue #9](https://github.com/Odourman/mellanrum/issues/9).
5. Previous Pachinko report and issue #6 remain **historical** diagnostics for `ec791333...` pre-visual version. Current verified visual ROM SHA is a new identity.

## Exact known current candidate (for Stage 0 tool qualification only)

- GitHub Draft PR #4 HEAD `eea14339010306de635a8c6238e242b76b28cc64`.
- Native DASM 4KiB NTSC ROM SHA256 `a9531d5bbbff033711fbe54f8688b8e0259640e0a9a284c8ab585eea415c0bd5`. MAIN downloaded [native CI artifact 14773519887](https://github.com/Odourman/mellanrum/actions/runs/45072844664/artifacts/14773519887) and independently hashed ROM bytes. Earlier intermediary `d1005a...` is not the final current build.
- Real Stella [visual workflow run 45073465951](https://github.com/Odourman/mellanrum/actions/runs/45073465951), artifact `14774191179`, contains production-ROM title snapshots but **separate instrumented test-ROM variants** for III-03/III-04/III-05 Presence frames. This is not all-room full gameplay.
- This SHA does **NOT** implement user-approved hardware-only Difficulty A/B mode selector yet. Current title has selectable graphic icons and SELECT toggle. **Do not report full-game final PASS at this stage.**

## Stage 0: build actual testing machinery NOW

Create independent test-only branch/PR with CI workflows and runner scripts (no production ROM code changes), and execute *tool qualification* jobs on the known `a953...` interim candidate:

1. Verify exact product source checkout and native DASM bytes including user requirements in baseline. Validate emulator installations/CLI and document versions.
2. Demonstrate **recorded, deterministic, frame-indexed** controller events with actual emulator hardware input port, covering both joystick and console switches. Confirm real Stella/Gopher2600 behavior: Left Difficulty A/B must map to SWCHB bit6; A=bit6 set, B=bit6 clear, test installed emulator with actual trace, not just the documentation. Stella F5=left A, F6=left B; F7/F8=right A/B. F1=SELECT; F2=RESET.
3. Build an independent sample trace for title→start→actual game and record **exact emulated frame number**, input, RAM state and TIA screenshot. The test runner must distinguish real controller sequences from debugger-injected room/cursor RAM. A simple Xvfb/xdotool `sleep` timeline is only `COARSE_SMOKE`, never `FRAME_EXACT`.
4. Demonstrate actual display **frame/scanline/WSYNC checks** and screenshot series. The visible title must be `MELLANRUM` only, full horizontal title. Validate shadow pixel differences from actual production renderer using explicitly named `INSTRUMENTED_VARIANT` if ordinary player route is not yet available; avoid false `REAL_PLAYER_REACHABLE` certification.
5. Capture genuine TIA audio WAV via tested Gopher2600 `-wav` (or another verified audio device route) instead of `SDL_AUDIODRIVER=dummy`. Verify file is complete, sampled, not muted, all intended sound events measurable; create an explicit human-audition checklist and mark `HUMAN_LISTEN_REVIEW_PENDING` until actually heard. The runner cannot certify aesthetic quality.
6. Shard test suite, preserve all deterministic seeds/trace inputs and machine version; provide artifacts on every failure with SHA manifest, not merely a green workflow.
7. Publish a documented `STAGE0_TOOLCHAIN_PASS/PARTIAL` outcome with evidence, then wait for a verified **new** native ROM commit+SHA from Issue #9 to execute the final matrix. Do **not** claim Stage 0 validates new A/B or replaces independent Verification.

## Stage 1: final complete system stress after Issue #9 delivers

**Gate:** MAIN validates new immutable PR commit, native DASM .bin SHA256, source diff and user A/B control behavior. PACHINKO must read that newly published MAIN intake before starting Stage 1. It is prohibited to substitute current `a953...` as final target, infer the future hash, or silently reuse earlier PASS.

In addition to ALL gates of the 13k [Pachinko full coverage brief](MAIN_TO_PACHINKO_2_0_FULL_COVERAGE_2026-11-22.md), test the following version-specific user requirements:

- **Only left console Difficulty** selects between modes, A=Campaign (standard) and B=FRI SKOG. Switch bit6 polarity proved by emulator.
- Right difficulty, joystick up/down/left/right and SELECT cannot change current or next-start mode. FIRE starts the left-switch choice; RESET returns to title and next FIRE reads current switch.
- A/B switch during gameplay cannot change running game mode. A/B change on title before next FIRE must change that launch. SELECT during gameplay may still restart same room, but not change mode.
- Startup 'default Campaign' means **hardware switch physically at A**, not an unsupported code-side forced A overriding real B. Run with explicit left A and left B; don't treat emulator's own initial configuration as a hardware guarantee. Verify RetroN 77 difficulty SKILL behavior if hardware available, otherwise `HARDWARE_NOT_RUN`.
- Title shows one readable `MELLANRUM` word and no joystick-menu icons. Newly added negative-space Presence must be genuinely reachable and visible in production ROM across III-03/04/05 with actual timed joystick route; compare same room pre/during/post and preserve map collision invariants.
- Full **genuine emulator joystick** 15/15 route to finale/coda twice; second emulator once where possible. Every room provides exact controller-frame trace, exit event, win state and replay checksum.
- All act I, II, III mechanics: owl priority, reversible mirrored tree edit, 2-slot echo delays, 3/5-tick polarity periods, 4/6-tick phase, presence schedule/override, simultaneous events, 8-bit wrap, title, FRI, RESET/SELECT/FIRE, no deadlocks or unwanted state corruption.
- Objective actual TIA raster/collision/hmove scanline measurement, 262 NTSC lines and 76 CPU cycles/scanline across worst-state 10k+ real emulator frames per room plus 50k+ FRI. Distinguish approximation and instrumented synthetic initial states from proven player-reachable sequences.
- Real TIA WAV captures for title, normal gameplay, sound cues, echoes, Silence and Presence and coda; analyze RMS/peak/clipping/channel activity, reproduce anomalies. Explicit `HUMAN_AUDIO_REVIEW_PENDING` for actual hearing.
- Real pixel/screenshots/video for all 15 rooms and all significant states, source art conformance checked separately and all aesthetics subject to MAIN user approval. No invented character sprite just because source negative-space effect is visible.
- At least 100 *real emulator* randomized seeded input sessions per room (1,500 total) with RAIN/TILT/CLOG/BOG/counterfactual, reachability denominators, full JSONL/CSV traces and exact seeds. Model-only runs may supplement but cannot count as actual emulator sessions.

### CI job architecture (verify in installed tooling; do not fake or handwave features)

`identity-native-dasm`, `frame-exact-input-replay`, `15-room-full-campaign`, `act-mechanics`, `presence-visual`, `tia-beam-raster`, `audio-wav`, `real-emulator-fuzz-15x100`, `long-run`, `manifest-and-artifact-validation`.

Separate PR-fast subset from full workflow_dispatch heavy run; return `PASS/FAIL/INCONCLUSIVE/NOT_RUN` per test. A green generic workflow cannot mean full all-systems PASS unless all required gates have run and passed.

## Release isolation

PACHINKO is diagnostic only and cannot modify game code, approve an unreviewed visual design, independently verify its own results, approve merge/release, or hide unavailable real hardware. Full release remains controlled by MAIN and separate independent Verification Issue #5.

**Output:** documented test-only GitHub branch/PR; Actions run URLs, exact ROM bytes/SHA; verified native frame-indexed replay source; complete independent oracle; actual TIFF? **PNG/MP4** for screenshots, WAV for real audio; logs and minimizable FAILs; state-graph CSV/JSONL; manifest SHA256; Swedish MAIN report with risks and explicit missing gates. The final user experience and human hearing must be judged by humans, not inferred from model numerical passes.
