# MELLANRUM – Issue #21 ROM DEVELOPMENT vNext completion evidence
Date: 2026-11-23. **Development candidate, not independent Verification, not release approval.**

## Exact ROM and protected predecessors

- New Draft [PR #23](https://github.com/Odourman/mellanrum/pull/23), branch `romdev/issue21-vnext-16k-20261123`. Product source changed on isolated branch from frozen PR #16. No merge.
- New **real native DASM** 6507, **4,096-byte Atari 2600 NTSC standard unbanked cartridge** `rom/bin/mellanrum_vnext_ntsc.bin`. **SHA-256 `63e719a362ae2eb5689484ca7c28c628b495a2843723898ebec3fe6374c43bdc`**; binary Git blob `bf5f62990b59ac35e1ff83224248bf0bc1745b02`. Source-to-byte agreement also checked with independent local subset assembler; source native .lst/.sym and GitHub Actions artifacts available. No F6 necessary because the complete game fits 4K (under user ceiling 16K), no DPC/CDF/ARM/Superchip.
- PR #16 prior 4K SHA `45d3422371d41bf896c0ac0076c57d93e600dcf7f4a1e51d4d352312fce8d7a7` unchanged; separate PR #4 E9EA frozen.
- All new tests below use **the new 63e719a3 SHA**. Never cite PR16 tests as new-ROM PASS.

## Actual design implementation

- 15 **independently authored, geometrically different** new room maps across three acts; updated owl starting positions, stone/exit coordinates, explicit source solution witnesses and necessary-action counterfactual. Original 14/15 auto-win failure addressed by new geometry **rather than longer forced waits**.
- One newly authorized gameplay rule change: **hovering the cursor over a tree no longer invisibly clears its collision**; only deliberate accepted FIRE changes a tree. This prevents cursor positioning during travel from silently overriding path choices. See `docs/GAMEPLAY_CANON_DELTA.md` for room-by-room original→new table and exact implications.
- Preserved green PF pine trees, user-approved U3 three horizontal mirror frames with vertical beak and constant eyes, 2 S3 sigils sharing P1, negative-space Presence B, indirect autonomous owl, 15-room campaign/FRI SKOG, V5.1 echoes and phase/inversion/Presence events, title and full coda, two real TIA audio channels. No conventional weapons, scores, bosses or enemies.
- Improved M0 feedback: neutral 1px steady; accepted 2px/4px pulse; denied 4px steady; Presence intercept shivering 8px/1px. Acknowledgement lasts 18 frames, without altering acceptance rules.
- Darker title/early-act TIA drone via `AUDC0=$0C`/low `AUDF0`, title sound-state reset. Presence warning sparse noise; active effect pulsed distortion and silence. A separate **diagnostic**, *non-product*, AUDC04 tonal alternative was assembled with source-checking and recorded in real Stella. Human quality preference is NOT_RUN.

## Reproduced actual native emulator evidence, all EXACT same game ROM SHA

| Case | Evidence and actual outcome | Class |
| --- | --- | --- |
| Native DASM ROM and vectors | **4096 B, SHA exact**, real DASM listing and symbols, local 6502 subset byte comparison equal | DEVELOPER PASS |
| Model tests and source witnesses | **20/20** reference unit tests; **15/15** source witness/600 beat passive + designated omission counterfactual checks (not emulation) | SOURCE PASS |
| Stella 15-room actual input | **15/15** room wins, original TIA and video callbacks, full coda and title at frame **13,939**; **13,940** authentic frames; original controller event log + **103 real screenshots** | DEVELOPER PASS |
| Gopher2600 actual input | **15/15** source rooms with real controller input only, no POKE; 14,068 frames, actual coda and title, **202/202 native TV FRAME samples 262 NTSC scanlines**, raw PEEK/timing/log, 15 screenshots | DEVELOPER PASS |
| Real Stella 600 second *no input* per room | **0/15 automatic wins** from 15 authentic serialized emulator states reached by controller-only full campaign; **36,000 no-input frames per room = 540,000 frames total**, first-win never observed. No POKE or forced RAM. | DEVELOPER PASS |
| Real Stella omitted critical action | **0/15 counterfactual wins**, one specific mandatory FIRE in each room removed from recorded legitimate controller replay, then 36,000 idle frames; original full game was won. 15×36,000 further no-input frames plus actual game-branch replay. | DEVELOPER PASS |
| Real Stella TIA sound | Native original WAV (31,440 Hz stereo) for title/in-game/FRI and complete 13,940 frame campaign; nonzero real callbacks, video replay frame-indexed 15 win frames exactly match raw result. Full MP4 with captured frame pixels plus recorded TIA soundtrack; diagnostic AUDC04 alternative WAV kept distinct. | DEVELOPER PASS for signal, SUBJECTIVE LISTENING NOT_RUN |
| Real Stella FRI stress | **57,500 frames**, BOG 2,500, CLOG 2,500, TILT_FIRE 2,500, TILT_STONE 50,000; native input, actual video callbacks equal requested frames, no crash. | DEVELOPER PASS |
| 30 Atari trick assessment | `docs/TECHNIQUE_30_AUDIT.md` explicitly evaluates 30 original methods and original cross-project research; 9 existing methods useful; rejected / not-used reasons recorded, no fake trials. | RESEARCH + SOURCE AUDIT |

Gopher output symbol-aware PEEK parser handles `0x00b8 (mode) (RAM) = ...`. A preliminary locally captured run printed no parsed RAM states because the previous regex expected unnamed labels; **raw immutable log was reparsed to 202 actual modes/rooms/beats**, 15 correct completed rooms and final coda→title, and the GitHub source runner parser was corrected. Do not promote preliminary unchecked `result.json` to PASS; use full raw trace + strict parsed file.

## Authority and reproducibility
- Exact byte source in `rom/src/main.asm`, `rom/src/data.inc`, `reference/rooms.json`, native build `.github/workflows/issue21-native-vnext.yml`. The old `build_issue15.py` regenerates prior PR16, **do not run it to build Issue21**. See `rom/README.md`.
- Gopher real controller harness `tests/issue21/gopher_full_campaign.py`; original Stella core harness `tests/issue15/stella_full_campaign.py` and `tests/issue15/libretro_stella_capture.py`. Local full artifact handoff includes exact 15-room Gopher log, original screenshots, raw event traces, Stella input/visuals/audio, idle and counterfactual source+JSON, video and SHA256 manifest.
- Actual handoff received by MAIN must use exact candidate SHA and code head. Earlier GRAPHICS final mask preference does not equal user-final subjective acceptance.

## Explicit limitations and release gates
**NOT independent Verification or independent Pachinko.** Physical standard Atari/RetroN77, PAL, actual dynamic worst-case SP/stack highwater and instruction-level per-register critical scanline timing **NOT_RUN**. Gopher 202 measured 262-line samples and Stella 13,940-frame visible callback evidence do not prove *every possible frame* cycle-safe. End-user artistic/hand-play and subjective TIA drone quality, S3 contrast/occlusion, +/-4 colorclock visible exit anchor and accessibility remain open. 30-trick research is not a claim all 30 were experimentally implemented.

**MAIN release gate remains BLOCKED. Do not merge PR #23 or alter PR #16/#4 until separately authorized after independent reviews.**
