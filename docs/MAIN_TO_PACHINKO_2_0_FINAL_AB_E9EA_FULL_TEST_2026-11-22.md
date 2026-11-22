# MAIN → PACHINKO STRESS TEST 2.0 — FULL-SYSTEM FINAL ROM ORDER
**Date:** 2026-11-22
**Status:** MAIN-authorized diagnostic execution order. **No full-suite result is claimed by this document.**
**Goal:** Exhaustively *exercise documented functionality* of MELLANRUM (all 15 campaign rooms, free forest, controls, game logic, rendered graphics and audio) using real Atari 2600 emulators in GitHub Actions, with adversarial reproducible evidence. An unbounded set of all possible input histories is not mathematically testable; report explicit coverage and residual risk.

## 0. Authority, frozen identity and prerequisites — do these before tests

READ IN ORDER:
1. `docs/CURRENT_PROJECT_STATE.md`, `docs/DECISIONS.md`, `docs/SOURCE_REGISTRY.md`; use current source authority order, **not memory**.
2. `docs/MAIN_FINAL_AB_ROM_INTAKE_2026-11-22.md` (MAIN's independent artifact intake; check this file exists on main).
3. This order, [Pachinko 2.0 detailed matrix](MAIN_TO_PACHINKO_2_0_FULL_COVERAGE_2026-11-22.md), [end-to-end test plan](MAIN_FULL_END_TO_END_STRESS_TEST_PLAN_2026-11-22.md).
4. All real V5.1 original sources and final GRAPHICS V5.1 archives; verify provenance, expected original 15 rooms, sprite masks and audio requirements.
5. Current ROM source in Draft [PR #4](https://github.com/Odourman/mellanrum/pull/4), immutable HEAD **`49eb168b17d0254d06cf50d87c60e8fb6016db6e`**, game code commit **`6cb86247c668162b180e5d77377098941b9803b3`**. Native NTSC 4K **4096 bytes**, **SHA256 `e9ea87d381bcf8da39ec055d7d6951ceff97b21d3a798addd10fbbe540c5e974`**. MAIN independently extracted + verified that exact hash from both GitHub Actions artifacts.
6. Latest native DASM [run #45075716636](https://github.com/Odourman/mellanrum/actions/runs/45075716636), [DASM ZIP artifact 14775257125](https://github.com/Odourman/mellanrum/actions/runs/45075716636/artifacts/14775257125). Stella real-A/B [run #45075039996](https://github.com/Odourman/mellanrum/actions/runs/45075039996), [artifact 14774798060](https://github.com/Odourman/mellanrum/actions/runs/45075039996/artifacts/14774798060) has 12 original PNGs, exact binary and wall-clock event log. **Neither is a full gameplay trace.**
7. [A/B issue #9](https://github.com/Odourman/mellanrum/issues/9), [Pachinko issue #7](https://github.com/Odourman/mellanrum/issues/7), [independent Verification #5](https://github.com/Odourman/mellanrum/issues/5). Older Pachinko SHA `ec791...` and visual revision `a953...` are **obsolete baselines**, never reused as final evidence.

**Version gate:** Verify PR #4 still matches frozen commit and native ROM hash. If PR moves, **do not silently retarget**: snapshot the frozen commit and annotate the difference; send exact new-commit question to MAIN before upgrading test target. No production code changes by Pachinko. A test-only GitHub branch may add CI workflows, harnesses, manifests, fixtures and reports, but `rom/src`, shipped binary, original `reference` engine and original room JSON must remain untouched. Independent Verification is a separate role.

## 1. Real emulation rather than a second homemade model

The previous Pachinko ran 2400 Python-model scenarios and a limited actual Stella smoke test with `xdotool` key presses timed by `sleep`, 13 real PNGs, `SDL_AUDIODRIVER=dummy`. It did NOT play 15 rooms, produce actual TIA audio or measure genuine scanlines. Avoid mistaking `GitHub Actions success` for complete test coverage.

Create and RUN a **frame-indexed** deterministic emulator input/replay harness, using verified Stella debugger / Gopher2600 playback or another genuinely 6507/TIA-executing emulator interface:
- Each applied real joystick state / FIRE edge / SELECT / RESET / left and right Difficulty switch change is indexed to emulated frame number and recorded with complete seed, ROM hash, emulator version, runner OS and replay command.
- Distinguish REAL INPUT-DRIVEN, INSTRUMENTED RESET/STATE-VARIANT, CPU MODEL, SNAPSHOT-ONLY and HUMAN-REVIEW evidence clearly. Direct cursor, beat or RAM manipulation is **for isolated targeted checks only** and can NEVER be credited as a title→room-to-room real gameplay pass.
- Do not assume guessed emulator CLI flags. Qualify installed tools with actual version/help and a known short verified replay first. A wall-clock `xdotool sleep` script is `COARSE_STELLA_SMOKE` until exact emulated-frame timing is proven.
- Record 6507 PC/SP, TIA/RIOT reads/writes, game mode/room, cursor, owl position+heading, map bits, stone polarity, beat, phase+age, 0/1/2 echo slots and due ticks, presence warn/active/release, coda, frame/scanline counters when exposed. If no reliable actual-state visibility exists, report `UNKNOWN/NOT_RUN` rather than inventing telemetry.

## 2. True complete campaign — primary acceptance gate

Produce **actual end-to-end** real controller port sequence(s) starting from normal product ROM title with physical left Difficulty A, FIRE and normal marker moves and action presses, winning **I-01 through III-05 in order**, traversing room win/continue sequences, waiting through 8-second coda and returning to title. Replay at least TWICE deterministically in first emulator and ONCE on another emulator if viable. For every room attach original screenshot / optional video, exit frame, state transition and full input trace. Avoid abstract model witness that teleports the cursor or assumes impossible one-tick travel. If any room cannot be won, flag the exact first blocked room and minimal reproduced sequence; report as FAIL/INCONCLUSIVE rather than a fake 15/15.

Separately cover 15 independent per-room scenarios for reset, room start 108-frame preparation, cursor movement/repeat, editable and denied actions, exit, and victory/next FIRE. Include title restart and FRI SKOG continuous free-mode behavior.

## 3. Physical A/B mode selection — user critical change

The **left Difficulty hardware A/B selector alone** determines mode *when starting from title*:
- A (SWCHB bit6 = 1, if confirmed in real emulator) → 15-room KAMPANJ; B (bit6 = 0) → FRI SKOG. It is meaningful as a physical switch setting, not a software-forced default. RIGHT Difficulty must not affect mode.
- Title shows **only** full single horizontal word `MELLANRUM`, no KAM/FRI words and **no selectable menu icons**.
- Joystick directions and console SELECT must NEVER choose/toggle title mode. FIRE starts the mode selected by LEFT Difficulty; held FIRE must not repeat.
- Changing left A/B **during gameplay** must NOT alter existing mode. RESET returns to title; next FIRE reads present A/B. Check A→B and B→A before FIRE and across RESET; SELECT inside game restarts same room without changing mode.
- Real Stella F5/F6/F7/F8 actions as black box plus *independently demonstrated* direct `SWCHB` and in-ROM mode RAM state; developer's two attempted built-in debugger scripts did NOT produce readable transcripts and this is still `NOT_VERIFIED`.
- Hyperkin RetroN 77 SKILL P1 actual hardware remains `NOT_RUN` until physical check, independent from the Stella mappings.

## 4. Mechanics invariant matrix — original V5.1

For **all original 15 room maps** and 3 acts, build table with expected vs actual real-emulator event outcomes:
- 10×8 symmetric map, immutable cells, editable left/right mirrored tree, marker anywhere, actual owl autonomous every ~72 NTSC frames, heading preference forward/right/left/back, stone entry polar turn clockwise/counterclockwise, exit and frozen win frames, transitions; console input latching, simultaneous keys, FIRE edge, denied action and max 1 accepted FIRE per beat.
- Act II echo: tree-change queue max 2; 3-tick with stone polarity0 / 5-tick with polarity1 **at scheduling time**; due time immutable, duplicate key denied, third queue denied, simultaneous due echoes stable ordering, wrap tick 255→0; no false time/delay.
- Act III physical collision inversion `blocked = base XOR phase` except always-open stone and exit, 4/6 beat phase periods by current stone polarity, preserve age on polarity change, echo/phase overlap and owl state in temporarily blocked cell.
- Presence foreshadows II-05 beat4, III-01 beat4, III-02 beat2; active intrusion III-03 warning1 / active2–3, III-04 warning0 / active1–2, III-05 warning2 / active3–4. During intrusion, an otherwise valid tree FIRE instead flips the stone with no tree/echo mutation; first active beat autonomously flips once if no interception; direct stone FIRE remains valid. Validate event ordering FIRE→Presence autonomous→due echoes→phase→owl→stone entry→win→render/audio.
- Race cases: frame just before/on/after tick, held input, movement at FIRE, reset while due echo, two queued echoes, two simultaneous callbacks, rapid mode restart, >256 logical beats and long loop stability. Report exact reachable denominator; do not claim unreachable combinations as failures.

## 5. Graphics, visual design and TRUE TIA

- Render from actual 6507/TIA emulation and capture all **15 rooms** in normal/crossed state, all tree phases, owl/marker/stone/exit HUD, title, title A/B visual invariance, coda, FRI SKOG, foreshadow/warning/active/release and all significant transitions. Preserve original PNG/MP4 plus event/frame trace and approved art reference per state.
- Title word MELLANRUM one line, no icons or extra text; both hardware mode settings leave it visually unchanged. Check after RESET/SELECT, audio on/off, phase transitions.
- **Presence** must be an **actual visible intermittent incomplete negative-space silhouette between conifers** (not a body with eyes/AI/hitbox) in III-03, III-04, III-05, with matched before/on/off/after frame captures **from uninstrumented production ROM reached by actual real-player input**. Historical developer screenshots were produced from explicit reset-instrumented variant ROMs: useful but NOT proof of production traversal.
- Audit true emulator TIA per-scanline counts (NTSC 262), 76 CPU cycles per scanline with CPU execution timing, VSYNC/WSYNC, HMOVE, PF update timing and reflection, P0 owl/P1 marker/BL stone/M0 exit overlap/flicker/clipping, 160×192 playfield presentation, color/contrast/silent legibility and grayscale state communication. If tool cannot expose true raster counters report distinct `TIA_SCANLINES_NOT_RUN`, never substitute CPU-model 262.
- Compare to actual GRAPHICS V5.1 source assets and approved render-only Presence deviation. A pixel difference proves visible change, **not** artistic acceptance or emotional response. Record what remains for human MAIN art review.

## 6. Real TIA audio and silence, not dummy

- Record **real audio output** from genuine TIA emulator in WAV. Verify actual installed Gopher2600 -wav behavior or another tested capture method; include tool command/version, waveform SHA, sample rate/channel configuration, gain and time-indexed game events.
- Capture representative sustained drone, echo cues 3/5, stone flip, phase inversion, Presence warning/active/release, FRI mode, coda, intentionally silent periods and all important transitions. Test both TIA channels through register or targeted recordings where feasible.
- Quantify expected audible vs intentionally silent signals, RMS, peak, clipping, DC bias, saturation/clicks and mute behavior; reproduce defects with event/frame trace. Synthetic PCM or sound from a developer Python model is not a real TIA audition.
- A CI numeric waveform PASS does NOT substitute for an actual human listening review of quality, dissonance, impact or sound-off experience. Upload playable WAVs, label `HUMAN_AUDIO_PENDING` until listened to.

## 7. Adversarial and long-run STRESS in real emulator

- At least **15 rooms × 100 reproducible seeded REAL emulation sessions = 1500** with defined policies: RAIN, TILT_FIRE, TILT_STONE, CLOG, BOG, counterfactual matched-seed and hand-built worst-cases. Record unique states/edges, observed versus reachable branch totals, looping, softlocks, failure severity and every seed/input policy. Developer CPU/model runs do not count towards the 1500.
- At least 10,000 consecutive actual emulator frames per room's specified worst-case state, plus 50,000 actual frames in FRI SKOG, with precise frame totals, true raster status and labeled state-injection if used. Include authentic input-driven long-run cases for practical reachable paths.
- Intentional idle loops and open-ended FRI SKOG are *not bugs*. Diagnose state locks only when the player cannot escape as specified or the engine violates invariants.
- If defects, replay 2/2 and minimize input/seed sequence. Report CPU/timing/display/audio evidence, impact level P0–P3, expected actual diff and reproduction from exact commit.

## 8. GitHub Actions implementation and result contract

Implement isolated test-only workflows and code on a reviewable branch or PR; do not change production sources, fixtures or original oracle. Suggested separate jobs (smoke CI and **heavy workflow_dispatch**): `identity-build`; `frame-exact-replay`; `ab-hardware`; `all-15-room-campaign`; `mechanics-matrix`; `presence-and-graphics`; `tia-raster`; `audio-wav`; `seeded-stress-matrix`; `long-run`; `artifact-manifest`. Shard by room/seed, set limits, preserve `always()` artifacts on failures.

**Required per-case JSON status:** `PASS | FAIL | INCONCLUSIVE | NOT_RUN`; immutable source commit, ROM hash, emulator binary+version, exact seed, controller file, tested emulated frame span, observable state data, screenshot/audio/raster artifact refs, expected/actual, evidence classification, independent oracle derivation and coverage denominator. Distinguish a green workflow plumbing check from all intended tests passing; a skipped audio/real-gameplay job is `NOT_RUN`, not `PASS`.

Produce full evidence ZIP with SHA256SUMS, CSV/JSONL tests, video/PNG, WAV, replay files and commands, full 15-room path, all failures minimized, test summary and a self-critical limitations section. Add result links to [Issue #7](https://github.com/Odourman/mellanrum/issues/7), notify MAIN with exact artifact IDs and run URLs.

## 9. Non-negotiable independence and stop rules

- This is a **diagnostic** assignment. Pachinko may deliver `PACHINKO_DIAGNOSTIC_PASS_WITH_EVIDENCE` ONLY for actually completed matrix; otherwise `PARTIAL/INCONCLUSIVE/FAIL`. It must never claim independent Verification or approve a release.
- [Independent Verification Issue #5](https://github.com/Odourman/mellanrum/issues/5) must separately rebuild/replay selected critical results for the **same exact SHA** and adjudicate remaining game/AV/raster risk. MAIN reserves art acceptance and merge/release decision.
- No more gameplay features are authorized by this test order. If actual ROM fails, send minimal repro and recommended correction to MAIN; only ROM DEVELOPMENT changes source with proper authorization, then **new** SHA and re-run regressions.
- Hardware Atari 2600/RetroN 77 & PAL remain explicit `NOT_RUN / NOT_IMPLEMENTED` until authentic verification. This cannot be papered over by Actions emulator success.

**Start all test infrastructure and actual GitHub Actions execution against exactly `e9ea87d381bcf8da39ec055d7d6951ceff97b21d3a798addd10fbbe540c5e974` NOW. Do not stop at writing a plan or repeating old model-only tests. Return evidence-backed completeness, not artificial success.**
