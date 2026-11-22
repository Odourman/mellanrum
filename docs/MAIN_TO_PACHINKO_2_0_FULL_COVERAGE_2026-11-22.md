# MAIN → PACHINKO 2.0: fully automated real-emulator system stress for MELLANRUM

Date: 2026-11-22. **Status: AUTHORIZED DIAGNOSTIC TEST INFRASTRUCTURE / NOT EXECUTED**. This replaces a model-first smoke campaign with actual-emulator-first coverage for the next immutable ROM revision.

## Priority and target selection

1. First wait for ROM DEVELOPMENT's user-authorized title + fleeting Presence silhouette work, [change order](MAIN_TO_ROMDEV_TITLE_AND_PRESENCE_2026-11-22.md). The currently tested old PR #4 head `8bdecde79a6bc1ecb804484d5d257f4f1a99b052` has 4K ROM SHA `ec791333da37613ec99ea70b2a983ecc1666b4e576211ece41a8e40bd14cbaed`. It remains an **archived baseline**, NOT evidence for the future revised ROM.
2. When ROM DEVELOPMENT provides the new immutable source commit + native DASM ROM hash, **freeze that exact commit and SHA** in new tests and results. If implementation is unavailable, you MAY build generic test infrastructure against the archived baseline, but results must remain clearly baseline-only. Never copy an old baseline PASS to changed bytes.
3. PACHINKO owns independent diagnostic scripts, GitHub Actions workflows and reports, not game production code, original reference oracle rewriting, merge, independent Verification, release or user art acceptance.

## How the previous test actually ran (verified in GitHub)

- Historical diagnostic branch `pachinko/diagnostics-8bdecde-20261122`, commit `e6e8f3047d2006418fee0e93a01fb918b7d6e186`, [GitHub Actions 45069826844](https://github.com/Odourman/mellanrum/actions/runs/45069826844) succeeded.
- The single workflow added `.github/workflows/pachinko-stella-diagnostic.yml`. In `ubuntu-24.04`, it installed `dasm`, `stella`, `xvfb`, `xdotool`; assembled the ROM and SHA-checked it; ran Stella software mode inside Xvfb. It emulated key presses using `xdotool keydown/keyup` with `sleep` durations, took `F12` snapshots, stored a timestamped TSV and uploaded an artifact.
- MAIN checked its genuine artifact `14772668727`: 13 screenshots (12 byte-distinct), 52 taps, 4K SHA-match and internal artifact SHA manifest. These were **real Stella screen images**, but SDL audio was `dummy`, inputs were wall-clock timed rather than frame-exact, and it never won all 15 rooms. A green workflow checked screen capture and executable survival, **not full functional game pass**.
- The source-guided 2,400 model starts and 69,747 owl beats reported by prior Pachinko are supplementary, not genuine emulator routes. [Full report](PACHINKO_STRESS_TEST_REPORT_2026-11-22.md) and [MAIN intake](MAIN_PACHINKO_INTAKE_2026-11-22.md).

## New non-negotiable architecture

**A. Immutable candidate and source integrity gate**
- Clone checkout by commit and separately record SHA. Obtain authentic V5.1/GRAPHICS archives, compare full rooms/masks/data hashes; don't substitute projected/synthetic rooms. Compile true DASM binary and compare SHA to developer delivery. Record emulator versions and runner OS; test status `BLOCKED_SOURCE` if required sources cannot be accessed.

**B. Actual emulated-frame input & replay harness**
- Build runner in test-only directory (e.g., `tests/pachinko2/` or `diagnostics/pachinko2/`), with documented, deterministic controller events indexed by **emulated frame** and actual emulator state transitions. Prioritize Gopher2600 recording/playback and HEADLESS/REGRESS capabilities or Stella debugger scripting; empirically verify the chosen emulator API/CLI with a short proof recording, not a guessed command. Gopher2600 documents `-record`, `-playbackCheckROM`, `-playbackCheckHashes`, `-wav`, `-video` flags and HEADLESS/REGRESS modes; validate exact flags on installed version.
- Every trace must distinguish manual joystick actions through input ports from debugger-forced RAM/cursor state. State injection is allowed ONLY for separate isolated TIA edge-case tests, **never** as proof a real player can reach/cross a room. If true frame-indexed API cannot be established, label coarse Xvfb/xdotool tests `EMULATOR_SMOKE` and frame-exact claims `NOT_RUN`.
- Replays must compare expected/actual room ID, owl direction and x/y, cursor x/y, stone polarity, phase & age, beat tick, echo queue, Presence/warn/active state, collision map, mode and screen checksum at meaningful events; failures include minimal input/frame/time and full state diff. Use independent oracle derived from original design, not the ROM dev CPU interpreter.

**C. Exact full-game traversal**
- Program/record a genuine start-from-title joystick+FIRE route through **all 15 original rooms**: title → I-01..I-05 → II-01..II-05 → III-01..III-05 → actual 8-second coda → title; no direct position injection. Replay the full route twice on primary emulator, once on a second emulator if available. Separately check each room reset, exit trigger, wait for continue, reentry, SELECT, RESET, and FRI SKOG progression/idle. If human-realistic frame travel invalidates a model witness, make reproducible FAIL/INCONCLUSIVE with exact blocked room and repair request.

**D. Mechanical and adversarial game invariant coverage**
- All 15 rooms: symmetric T/t toggles, immutable cells and denied FIRE, held FIRE, FIRE-edge at frame boundary (-1/0/+1), movement and repeats, diagonal priority, no repeated held actions, one action/tick, autonomous owl priority, rotations on stone arrival, room exit/win and all menu modes.
- Act II/III: 0/1/2 echo slots and denied third, delayed 3/5 due, same-tick FIRE+echo, phase inversion 4/6, due echo during phase change and stone entry; event ordering independent of graphics; collision always matches V5.1 even when visually negative.
- Presence: II-05 t4, III-01 t4, III-02 t2 foreshadows; III-03 warn t1/active t2–3, III-04 warn t0/active t1–2, III-05 warn t2/active t3–4; interception (legal tree FIRE → stone flip, no echo/tree change), autonomous first-active-tick polarity flip when no intercept; ensure visual silhouette exists in **actual emulator frames** for each active room and ends, while warning is readable with muted audio. Validate no unapproved enemy logic.
- Wrap & race: beat 254→255→0, queue due crossing 8-bit boundary, repeated resets, simultaneous inputs and overlapping graphic objects, at least one room that triggers every supported intervention state.

**E. Graphics & TIA: objective measurements plus art review**
- Authentic TIA raster: actual per-frame scanline lengths (NTSC normally 262), cycle timing (~76 CPU cycles/scanline), VSYNC/VBLANK/WSYNC, P0/P1/BL/M0/PF simultaneous object positioning, HMOVE artifacts, playfield reflection and two crown/trunk bands, correct 10×8 geometry, phase/color changes, hidden collision/overlap, grayscale mode and flicker safety. Verify loaded/edited logical maps versus pixel-rendered cells with measured comparisons, not a mocked framebuffer.
- Save keyed screenshots/video for **all 15 rooms** at start and at changed map/echo/phase/Presence states plus title exact readable **MELLANRUM** and NO other words, FRI mode choice via icon, transitions and 8-second finale. Cross-check against source GRAPHICS but don't label an intentional new silhouette a bug just because an old golden PNG is different: golden comparisons need versioned/approved baseline.
- For each III-03/04/05, require a matched trio of authentic emulator screenshots: before, silhouette partially appearing, after; ensure not HUD-only, no P0/P1 critical sprite corruption, no separate monster or hitbox, no visually confusing interaction. Prefer per-frame pixel region diffs and coordinates where practical; also request human review for ambiguous emotional effect.

**F. Audio: real waveform artifact + measurable checks**
- Obtain genuine TIA audio through supported emulator recording (Gopher2600 `-wav` if supported by actual installed version) or a configured virtual sound device. The previous `SDL_AUDIODRIVER=dummy` means audio WAS NOT heard or recorded.
- Capture real WAV (and optionally MP4) for title, calm forest, both echo periods, polarity flips, phase inversion, warning, active Presence, coda/silence, Free Forest. Assert nonzero signal where intended, silence where intended, channel 0+1 contribution at register level, stable sample rate, no sustained clipping, violent envelope spikes, unintended noise/clicks or missing cues. Report actual durations and RMS/peak/frequency/envelope metrics with samples and frame IDs.
- Audio waveform automatic metrics cannot certify artistic sound quality, annoyance, contrast or safety. Provide downloadable WAVs and an explicit **HUMAN_LISTEN_REVIEW_PENDING** until someone actually listens and records findings; same for color/legibility subjective judgment.

**G. RAIN / TILT / CLOG / BOG / counterfactual in real emulator**
- At least 100 seeded actual emulator input sessions per room (≥1500), including response-aware RAIN, action bias TILT, queue/input flood CLOG, delayed anomalies BOG, matched-seed counterfactual pairs and minimal failing reproductions. Report each population policy, reachability denominator, completed/censored counts, source-informed vs black-box separation, observed directed state graph, dead ends, loops and hotspots. Don't claim all 1500 run unless real emulator did run them.
- At least 10,000 consecutive authentic emulator frames for each room's controlled worst-case state and 50,000 in Free Forest (test harness injected state should be labelled isolated); separate 10k+ frame normal route/sample where suitable. Record precise count of 262-line frames and any deviations, not developer-model estimates.

## CI deliverables: multiple real GitHub Actions jobs

Create **isolated, reviewable diagnostic PR/branch** containing workflows and test runners (no changes in `rom/src`, `rom/bin`, reference engine, original rooms or production build scripts). Preserve the product candidate SHA via a test-only checkout at an exact commit. If another commit is needed to hold test infrastructure, verify a path-limited diff from candidate; display the list in CI.

Suggested workflow graph:

| Job | What it runs | What makes it fail |
|---|---|---|
| `identity-build` | Exact source + native DASM + 4K/mapper + SHA + reproducibility | Wrong bytes / missing source / build errors |
| `real-input-route` | 15/15 authentic emulator joystick full campaign, 2 repeats, resets/modes | Missing authentic win/traces or incorrect state |
| `mechanics-matrix` | Per-room exact timing/echo/phase/Presence and event order with real frame input | Any oracle mismatch, or required case absent |
| `raster` | Per-frame NTSC TIA scanline and overlapping object/collision instrumentation | Extra/missing scanline or mismatched visible state |
| `screenshots` | Versioned all-room title/Presence/phase/coda screenshots and pixel checks | Missing image or objective incorrect feature (e.g. title text) |
| `audio-capture` | Genuine emulator WAV and numerical signal checks | WAV missing/empty/clipping/failing expected audio event |
| `stress-matrix` | 15 rooms × ≥100 seeds, sharded, actual emulator, high-load and long run | Any confirmed invariant failure / missing reproducibility evidence |
| `artifact-verify` | Complete manifest, per-test `result.json` with status/frames/seeds/hash, PNG/WAV/trace/CSV | Missing coverage denominator or corrupt hashes |

Use `workflow_dispatch` for heavy runs and PR checks for a fast **smoke subset**. The heavy run must be explicitly invoked, recorded and allowed to finish; green fast smoke must never masquerade as full matrix. Parallelize per-room/per-seed jobs with GitHub Actions matrix, sensible caps/timeouts and no cache of mutable ROM. Artifact retention should be long enough for independent Verification. Workflows must report PASS, FAIL, NOT_RUN, INCONCLUSIVE distinctly rather than returning SUCCESS when a required test was not run. A failed visual or audio test should not be waived by the next job.

## Evidence output and exit gates

Upload one top-level manifest/checksum package containing exact candidate commit + ROM SHA; native DASM listing; runner version and OS/container hash; all frame-indexed actual controller sequences with replay commands; 15-room exit paths; PNG/MP4 screenshots; WAV audio; TIA frame/cycle/register traces; full seed lists; transition/state graph and coverage numerator+denominator; all test results labelled; failures P0-P3 with 2/2 reproduction, minimized seed/sequence and expected/actual; human-art and human-audio review request.

**Release-ready from Pachinko? Never.** Pachinko only reports `DIAGNOSTIC_PASS_WITH_EVIDENCE` or `PARTIAL/FAIL`, not official release PASS. Independent VERIFICATION (Issue #5) must independently review actual ROM and samples, re-run highest-risk traces; MAIN handles art and release decisions. If CI tool cannot test a class, deliver evidence-backed `NOT_RUN` with exact blocker and proposed next method, don't hallucinate completion.

## Primary documented tools (verify installed CLI)

- Gopher2600 source code documents HEADLESS/REGRESS, replay recording and `-wav` recording: https://github.com/JetSetIlly/Gopher2600/blob/master/gopher2600.go
- Stella debugger supports breakpoints, watchpoints, frame/scanline stepping, TIA and RIOT register inspection: https://stella-emu.github.io/docs/debugger.html
- Existing [full E2E acceptance matrix](MAIN_FULL_END_TO_END_STRESS_TEST_PLAN_2026-11-22.md), [PACHINKO report](PACHINKO_STRESS_TEST_REPORT_2026-11-22.md) and [previous workflow run](https://github.com/Odourman/mellanrum/actions/runs/45069826844).

**Instruction to PACHINKO:** Build and actually execute the full reachable automated diagnostic suite after ROM DEVELOPMENT's new immutable SHA is available. Do not stop at a plan or a green Stella boot; carry the full stress campaign to captured evidence and report deficiencies truthfully. Do not modify or release game code.
