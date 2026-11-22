# MAIN — FULL END-TO-END SYSTEM STRESS PROTOCOL / MELLANRUM
Date: 2026-11-22
Status: TEST PLAN / NOT EXECUTED
Scope: frozen draft PR #4, commit `8bdecde79a6bc1ecb804484d5d257f4f1a99b052`, 4,096-byte NTSC standard 4K ROM, SHA-256 `ec791333da37613ec99ea70b2a983ecc1666b4e576211ece41a8e40bd14cbaed`.
Authorities: current `docs/DECISIONS.md`, `docs/CURRENT_PROJECT_STATE.md`, original V5.1/GRAPHICS full source, immutable ROM commit; historical docs only within authority order.

## What Pachinko passed — and what it did not

Previous [Pachinko report](PACHINKO_STRESS_TEST_REPORT_2026-11-22.md) and [MAIN intake](MAIN_PACHINKO_INTAKE_2026-11-22.md) establish the following evidence boundary:
- Pachinko reported 2,400 source-informed model starts (69,747 executed owl ticks, zero model-oracle divergences), 152 targeted modeled runs, 17,600 frame-level CPU-model frames and 19,080 FRI model frames. Main has NOT independently re-counted the full modeled raw ZIP, which was not attached in the MAIN message.
- MAIN verified real [Stella run 45069826844](https://github.com/Odourman/mellanrum/actions/runs/45069826844), artifact `14772668727`: 52 coarse-time input taps, 13 screenshots (12 byte-distinct), genuine 4K candidate ROM with matching hash. This was a limited smoke/black-box session, **not** a 15-room joystick playthrough or line-exact TIA certification.
- Real audiovisual gameplay, every room, full joystick action traces and independent release Verification remain unverified. `MODEL_PARITY_PASS` ≠ `GAME_COMPLETE_PASS`.
- Tool definitions: [Stella integrated debugger](https://stella-emu.github.io/docs/debugger.html) provides breakpoints, frame/scanline advancement, `_scanEnd`, `_sCycles`, `_fCount`. [Gopher2600](https://github.com/JetSetIlly/Gopher2600) supports recorded gameplay/playback and debugger/timeline, useful for reproducible independent runtime evidence.

## Methodology: three separate workstreams

A. **PACHINKO PHASE 2 (diagnostic)**: randomized adversarial *real emulator* input, long runs, corner cases, event graph and minimal failing traces. It may add isolated diagnostic workflow/scripts but MUST NOT modify game source or rewrite original oracle. Reports to MAIN. Never self-awards independent verification.

B. **INDEPENDENT VERIFICATION (separate role)**: clean rebuild and independent oracle, repeats all critical traces, audits actual TIA, compares source and artistic constraints, determines gate result. Does not rely on model parity alone. Issue #5 already covers this role.

C. **Human visual/audio playtest + GRAPHICS design review**: actual legibility, title/game screens, silence and drones, HUD feedback, coda; different from machine proof. Subjective feedback must be attributed to actual viewers/listeners and not falsely claimed from bots.

## Prerequisites and freeze

1. Obtain original V5.1 and GRAPHICS archives and manifests. Verify byte-level integrity and source precedence. Clone exact PR SHA (not mutable HEAD). Verify native DASM build and full ROM SHA-256, symbol listings, 4K mapper. Record tool versions (DASM, Stella, Gopher2600) and flags.
2. Build a **frame-indexed input harness** with emulated-frame state sampling, not wall-clock-only xdotool delays. Prefer a headless emulator with joystick recording/playback and hash checks. If tooling cannot supply exact emulated frame inputs, retain coarse sessions as SMOKE and mark frame-exact checks NOT_RUN.
3. Capture at relevant boundaries: actual controller port events, TIA/RIOT input read, RAM beat, owl x/y/direction, cursor x/y, polarity, phase/phase_age, queue slots and due ticks, Presence phase, room, mode, exit, 6507 PC/SP, frame count and scanline lengths. Do not inject cursor positions in tests advertised as a true joystick traversal.
4. Store inputs, seeds and emulator states exactly; a saved emulator state is an acceleration aid, not evidence that the route from room 1 to that state is playable. Include both real full path and separately label isolated state tests.

## Acceptance matrix

| Gate | Required concrete evidence | PASS conditions |
|---|---|---|
| E01 SOURCE | Original full ZIPs and SHA manifests; 15 room JSON objects, 25 sprite records; script generation | Byte provenance independently verified; no synthetic G0 maps substituted |
| E02 BUILD | Exact commit, clean native DASM output, listing/symbols, checksum | 4,096 B, SHA exactly frozen value |
| E03 FULL CAMPAIGN | Actual emulator joystick/FIRE complete route through all I-01 … III-05, title→room 1→last room→8-s coda→title; room IDs, complete frame-indexed controller events and screenshots/videos, no direct cursor/RAM injection in claimed route | 15/15 won and correctly transitioned, repeat full route at least twice on same ROM and once on second emulator where available |
| E04 ROOM ISOLATION | For EACH 15 rooms: one independent normal route, one recovery/reset route, denied/valid action cases with screen+state trace | All 15 have room-by-room real emulator PASS; any unreachable room is FAIL/INCONCLUSIVE with minimal trace |
| E05 ACT MECHANICS | Symmetric tree edit, correct hitboxes, owl forward/right/left/back choice, stone turn, 2-slot echo 3/5, phase 4/6, true collision inversion, 0/1/2 queue occupancy | Measured actual emulator RAM/event match independently computed V5.1 oracle, every event family includes at least one real frame-indexed sample |
| E06 PRESENCE | Forerunners: II-05 t4, III-01 t4, III-02 t2. Intrusions: III-03 warn t1 active t2–3, III-04 warn t0 active t1–2, III-05 warn t2 active t3–4; intercepted tree-FIRE and automatic first-tick stone flip with and without direct stone FIRE | Correct actual timing/action order and simultaneously visible silent HUD warning, no false extra sprite or mutated tree on intercepted input |
| E07 CONCURRENCY | FIRE edge immediately before/at/after beat, due echo + new FIRE + phase change + stone arrival + Presence, invalid third echo, repeated held FIRE, SELECT mid-tick, RESET in all modes, simultaneous sprite bands | No divergent state, lock, crash, duplicate fire, queue corruption, unexpected visual ambiguity |
| E08 WRAP AND LONG RUN | Tick 254→255→0, due echo crossing wrap, event after Presence windows; idle and adversarial long runs in FRI and each act | No unwanted reactivation/locked queue or crash. For measurable long-run target: >=10,000 consecutive authentic emulator frames per room at worst-case controlled state plus >=50,000 frames in FRI, with explicit frame counts and interruption labels |
| E09 TIA/VIDEO | Stella debugger (prefer corroboration in Gopher): `_scanEnd`, `_sCycles`, TIA register writes, HMOVE, 160×192 logical layout and 262 scanlines/frame in actual TIA emulation; P0/P1/BL/M0 overlaps; grayscale and color switches | 262/262 NTSC scanlines for all observed frames, no late/missed scanlines, stable PF geometry, sprites on correct cells, no unintended collision/timing artifacts; capture highest-load frames |
| E10 VISUAL/ART | Every original room screenshot in initial and changed states, act palettes, Presence pre/active/release, transition, title, FRI, last 8-s coda, compare to GRAPHICS allowed fallbacks | Gameplay-significant visuals legible in grayscale/silent conditions; declared art deviations reviewed explicitly (abbreviated mirrored title, simplified coda, omitted optional PF seam and M1) |
| E11 AUDIO | Real TIA audio output captured (not SDL dummy); two channels audible/listened to, intentional silence, polarity/echo/Presence cues, check clicks, clipping, sharp volumes | No unacceptable audio failures; human listening report documented and sound-off still playable |
| E12 INDEPENDENCE | Independent rebuild/replay/counters not simply developer's bespoke CPU/WSYNC simulator | Independent Verification provides separate signed verdict and evidence from actual emulator; developer/Pachinko result may support but cannot replace |

### Test budget as a measurable floor, not a magic proof of no bugs

- Real emulator full routes: 2 complete campaigns in the primary emulator, 1 in a second emulator if executable and configured; 15 individual rooms x 2 kinds of scenarios.
- Real emulator stress: at least 100 deterministic randomized input seeds per room (1,500 distinct sessions), with independent seed storage, bounded session lengths and early-exit reporting. Choose a coverage-based subset for expensive full video capture and instrumented worst-cases.
- Long TIA stability: >=10k consecutive emulated frames in each room or representative worst-case room state (per-room long runs desirable); >=50k FRI frames; all logs include actual frame counts and TIA scanline counts, not a Python-emulated WSYNC approximation.
- Separate full combinatorial targets: (act/room) x (phase 0/1) x (echo count 0/1/2) x (Presence none/warning/active/release) x (input edge timing -1/0/+1 frame) WHERE REACHABLE. Store coverage denominator: reachable branches generated by V5.1, not imaginary impossible states. No blanket "100%" if not enumerated.
- Execute at least one true controller-input replay for each reported model-only risk family; identify unachievable witness paths and provide exact correction recommendations.
- Every test logs PASS, FAIL, INCONCLUSIVE or NOT_RUN, with commit, ROM sha, emulator version, frame-indexed input trace, expected, actual, screenshots/video, observed state, number of reproductions and minimized reproducer for any FAIL.

## Ordering and stop rules

1. Freeze and independent clean build.
2. Prove 15-room real joystick route first; if impossible, stop pretending model 15/15 is game 15/15 and provide first minimal blocked-room repro to ROM DEVELOPMENT via MAIN.
3. Expand to stress populations in real emulator; run with both random and targeted action policies, preserving seed and input timing.
4. Probe worst-case TIA register activity and >256 beat rollover; never label custom CPU model as real scanline audit.
5. Audio + human visibility checks, GRAPHICS coda/title adjudication.
6. Independent Verification replays highest-risk traces and writes verdict for MAIN.
7. No release until no unresolved P0/P1 failures, all 15 room transitions reached with real controls, real NTSC raster proof, actual audiovisual review, and separate independent Verification PASS. If tool/hardware unavailable, mark NOT_RUN; cannot turn a gap into a PASS.

**Scope honesty:** No finite suite can prove all possible infinite input sequences. "Full stress test" means all documented critical game systems and release gates have reproducible actual-emulator evidence, risk-based randomized coverage, measured denominator and explicitly bounded NOT_RUNs.

**Implementation boundary:** This is a TEST PLAN and optional diagnostic mandate only, NOT a game source modification or new cutover authorization. Leave PR #4 Draft/open pending findings.
