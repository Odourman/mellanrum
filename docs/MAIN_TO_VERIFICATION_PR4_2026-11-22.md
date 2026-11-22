# MAIN → Independent VERIFICATION: MELLANRUM V5.1 ROM candidate PR #4

**Date:** 2026-11-22. **Status:** ACCEPTED_FOR_INDEPENDENT_VERIFICATION, **NOT RELEASE-APPROVED**.
**Candidate commit:** `8bdecde79a6bc1ecb804484d5d257f4f1a99b052` on `romdev/fullgame-20261122` (PR #4, Draft, unmerged with `main`).
**Target:** Atari 2600 / NTSC / standard 4 KiB ROM / DASM.

## Sources and verified anchors

- [Candidate PR #4](https://github.com/Odourman/mellanrum/pull/4) — use **head SHA**, not a mutable branch name, for verification.
- [Native DASM + developer model CI, current head](https://github.com/Odourman/mellanrum/actions/runs/45064977045) — job **SUCCESS**.
- [Actual Stella boot/screenshot smoke, current head](https://github.com/Odourman/mellanrum/actions/runs/45064977006) — job **SUCCESS**, four PNG captures. Title and a gameplay scene are visible; this does not prove whole-game playability.
- Native CI ROM artifact ID `14771180701`; Stella capture artifact ID `14769984347`.
- [Developer test report](https://github.com/Odourman/mellanrum/blob/8bdecde79a6bc1ecb804484d5d257f4f1a99b052/docs/DEVELOPER_TEST_REPORT.md) and [source provenance](https://github.com/Odourman/mellanrum/blob/8bdecde79a6bc1ecb804484d5d257f4f1a99b052/docs/PROVENANCE.md).
- [MAIN design/GRAPHICS intake](https://github.com/Odourman/mellanrum/blob/main/docs/MAIN_GRAPHICS_V5_1_INTAKE_2026-11-22.md), [game design review](https://github.com/Odourman/mellanrum/blob/main/docs/MAIN_V5_1_REVIEW_2026-11-22.md).

## MAIN's intake observations (not independent verification)

- MAIN downloaded the **current-head** GitHub Actions artifact ZIP, extracted the DASM-built 4,096-byte ROM, verified its SHA-256 directly: **`ec791333da37613ec99ea70b2a983ecc1666b4e576211ece41a8e40bd14cbaed`**. The native CI logs printed the same value for native DASM and the independent developer subset assembler. The ROM reset vector is `$F000`; Stella reported NTSC and 4K.
- Current-head GitHub Actions logs show 20/20 reference Python tests, 15/15 model-based witness wins against executing 6502 in custom developer CPU interpreter, 225 random model runs, 4,352 random ticks, 20 playfield edits and developer-timing checks. These are **developer** tests and must not be relabeled independent.
- MAIN directly inspected all four CI-provided 320×228 PNG images: the title and at least one gameplay view have visible nonblank content. Screenshots 1–3 are not a full frame-by-frame joystick replay and do not establish the final 15-room, image or sound quality.
- Source ZIPs and the reported 116/116 manifest, 25 8×8 masks, same 15 canonical rooms, 20/20 original tests and 15/15 abstract solutions were **verified and reported by ROM DEVELOPMENT**, not independently re-run by MAIN. Original full ZIPs are not present in the PR as a full self-contained archive. Request access to originals and reproduce provenance before independent SOURCE_PASS.

## Independent Verification: required scope

1. **Reproducibility/provenance:** clone exact commit, inspect `docs/PROVENANCE.md`, independently obtain both original V5.1 and final GRAPHICS ZIP sources (or state NOT_ACCESSIBLE), verify SHA-256 and manifest content, compare all 15 room records and 25 sprite masks. Distinguish canonical V5.1 source from earlier synthetic R01–R15 material. Validate scripted source generation with no hidden changes.
2. **Independent ROM build:** build in clean environment with genuine DASM, require exactly 4,096 bytes, compare SHA-256 to `ec791333da37613ec99ea70b2a983ecc1666b4e576211ece41a8e40bd14cbaed`; fail if mismatched. Check reset/IRQ vectors, 4K mapping, RAM+stack footprint, any unexpected ROM writes.
3. **Real Stella/Gopher gameplay, not only model:** run all 15 original rooms, verify controls through real joystick input per video frame (not direct memory injection), record each exit, resets, progress, state, initial positions, true move choices, FAIL/NOT_RUN separately. If emulator inputs or automated display are unavailable, mark corresponding verification NOT_RUN rather than passing.
4. **Mechanics invariants:** symmetrical T/t edit by FIRE; exactly one valid action per owl beat, edge/held-FIRE behavior and frame-boundary latching; autonomous owl priority; stone movement behavior; Act II two-slot echoes at 3/5 ticks with 0/1/2 occupancy; Act III actual passability inversion and 4/6 tick phase; beat wrap / queued echo rollover; win/coda and free forest behavior.
5. **Presence semantics:** premonition II-05 t4, III-01 t4, III-02 t2 (no interference); III-03 warn t1 active t2–3; III-04 warn t0 active t1–2; III-05 warn t2 active t3–4; valid tree FIRE becomes stone flip (no tree toggle or echo), first active tick auto-flips stone iff no valid tree FIRE intercepted. Verify actual visual warning distinguishable silently, no conventional monster.
6. **Raster & graphics:** actual TIA scanlines 262/frame NTSC (long run, e.g. >=10,000 frames); no frame slips, severe HMOVE bands or frame flicker, 76 CPU cycles/line, PF two-band geometry and reflection, correct 10×8 mapping, P0 owl, P1 cursor, BL stone, M0 exit, COLOR register sharing, overlaps and priority, phase/echo/polarity/Presence HUD. Compare actual screenshots to intended art with documented fallbacks.
7. **Presentation and accessibility:** inspect title text/mode choices, level transitions, 8-second coda, FRI SKOG, SELECT vs RESET, visual confirmation of rejected/accepted/intercepted actions, readable grayscale and sound-off states, potential light flicker; listen to both TIA audio channels. Title is abbreviated/mirrored; final single-tree coda and local Presence seam were simplified/omitted, requiring explicit artistic acceptance rather than being silently treated as fidelity PASS.
8. **Ports/platforms:** NTSC is candidate scope; PAL not implemented, so explicitly `PAL_NOT_IMPLEMENTED` and not PASS. Physical Atari/RetroN77 checks only if hardware actually available.

## Review outputs to MAIN

- Single verdict: `INDEPENDENT_PASS`, `PASS_WITH_ISSUES`, `FAIL`, or `INCOMPLETE` with per-test evidence and explicit `NOT_RUN`.
- Exact tested SHA and the tool versions. Screenshots/recordings/logs with room IDs, tick/frame conditions, input sequences; reproducible failing traces, screenshots, severity and remediation priority.
- Separate **verified behavior** from subjective artistic assessment and hardware limitations; recommend changes as a review, not an unapproved rewrite of game design.
- Clearly state whether PR #4 is safe to merge, needs ROM DEVELOPMENT corrections, or needs hardware/visual tests. Do not merge or publish a final release yourself.

## Known deliberate developer deviations

- V5.1 F6/16 KiB was a working hypothesis; ROM DEVELOPMENT chose a real standard 4 KiB cart. Hardware proof still matters.
- Simplified title text, less animation, no local PF crown-seam for Presence (still has warning HUD and actual input takeover), M1 chisel omitted, coda uses simplified forest rather than final single-tree art, FRI SKOG selects four existing geometries. These are design deviations for art review, not concealed omissions.
- `BUILD_PASS`, `DEVELOPER_MODEL_PASS` and `STELLA_BOOT_SMOKE_PASS` are **not** `INDEPENDENT_VERIFICATION_PASS`.

**Boundary:** VERIFICATION must be independent of ROM DEVELOPMENT. If defects are found, send a source/ROM-specific handoff back via MAIN; keep PR #4 unmerged until decision.
