# MELLANRUM – ROM DEVELOPMENT II Issue #21 developer completion handoff

**Date:** 2026-11-23. **Classification:** NEW ROM DEVELOPMENT CANDIDATE / native emulator developer PASS / independent Verification+Pachinko NOT_RUN / NO MERGE / NO RELEASE.

## Exact identity
- User-authorization [Issue #21](https://github.com/Odourman/mellanrum/issues/21), MEL-053 and MEL-054.
- [Draft PR #22](https://github.com/Odourman/mellanrum/pull/22), new source branch `romdev/issue21-vnext-resonance-20261123` exclusively; source base immutable PR16 `56d70c316031bf55a5260e1fbbe0fe187c55f297`.
- **New native DASM NTSC 4K unbanked ROM SHA-256 `18163c0435347695ee1cff5a4b6b19c80d280ec255eeb7f9b98711471ccde11c`, size exactly 4096 bytes.**
- Old baseline PR16 `45d3422371d41bf896c0ac0076c57d93e600dcf7f4a1e51d4d352312fce8d7a7` and PR4 `e9ea87d381bcf8da39ec055d7d6951ceff97b21d3a798addd10fbbe540c5e974` remain unchanged.

## Rules and artwork implemented
- 15 physically source-authored room cases in three acts, green mirrored live PF conifers, original autonomous U3 owl, original two distinct user-preferred S3 glyphs on one duplicated P1 channel, negative-space Presence; three source-original acts and coda, no score/guns/bosses.
- **Critical remediation:** Owl crossing exit can no longer autonomously complete. The exact room's specific mirrored resonant-tree bit must be absent. The tree can be genuinely altered by FIRE and may reappear via act II/III delayed reversible echo. A wrong tree does not substitute. Game's normal audio/control actions continue; prior 14/15 self-winning design is superseded for this NEW candidate only.
- Clearer discoverability: cursor and owl share real TIA P0/M0 COLUP0; amber hint when cursor targets exactly the needed tree (before FIRE), green accepted, red rejected, violet intercept. Distinct marker width states retained. User-approved U3 source bitmap/animation unchanged.
- Low title/Act I tone-only TIA drone ($04 tonal channels), intermittent crackle/near-silence when Presence is manifest. Actual Stella PCM captured.

## True exact-SHA developer tests
| Test | Evidence | Classification |
|---|---|---|
| Native DASM 4096B, .lst/.sym, separate subset byte match; source rules and stack bound | [Actions 45146265215](https://github.com/Odourman/mellanrum/actions/runs/45146265215) | PASS |
| Real Stella normal joystick/FIRE title → all 15 rooms → full coda → title, 11,132 frames; original screenshots+TIA PCM | [Actions 45146044733](https://github.com/Odourman/mellanrum/actions/runs/45146044733) | PASS |
| Real Gopher2600 controller-only 15 rooms with coda and title, 162/162 real read-only RAM checkpoints and 162/162 native 262-scanline sample frames | same Actions 45146044733 | PASS |
| 15 actual Stella rooms each 36,000 frames (600sec) of absolutely no controller input, 0 passive wins; then console SELECT and full successful 15-room controller playthrough, 551,162 total frames | [Actions 45146044746](https://github.com/Odourman/mellanrum/actions/runs/45146044746) | PASS |
| 15 independent real Stella counterfactual controller traces with 1 needed tree-FIRE suppressed per room; 15 no-wins within original win+1200 frames, no POKE | [Actions 45146044908](https://github.com/Odourman/mellanrum/actions/runs/45146044908) | PASS |
| Stella 4 FRI B controller stress profiles (3×2500 + 50,000 frames), real video/audio callback and mode4 RAM records | [Actions 45147567733](https://github.com/Odourman/mellanrum/actions/runs/45147567733) | PASS 57,500 |
| Static JSR call path bound Frame→GameFrame→BeatTick→CommitFire→ToggleTree→DecodeKey, 10 stack bytes of 14 available, 4 margin | native source audit Actions 45146265215 | PASS static, dynamic SP NOT_RUN |
| Human graphic acceptance, subjective listening, real physical Atari or RetroN77, PAL, precise worst-case 76cycle beam trace | none | NOT_RUN |

These are **developer's own tests and recorded artifacts**, not equivalent to an independent release Verification. Gopher's 162 TV FRAME sample checks are not a proof of every physical frame's every register deadline. Stella libretro frame callback is not physical console measurement. The actual user may judge whether 15 rooms are sufficiently distinct/engaging beyond their verified necessity. F6 mapping is **not applicable to this unbanked 4KiB candidate**.

## Reproducibility and source
- `rom/src/main.asm`, `rom/src/data.inc`, `reference/rooms.json`, `reference/rooms.py`, `reference/engine.py`.
- `reference/issue21_audit.py`, `tests/issue21/`, `pachinko2/campaign_issue21.py`, `scripts/issue21_stack_source_audit.py`.
- `.github/workflows/issue21-vnext.yml`, `issue21-real-emulator.yml`, `issue21-real-stella-idle.yml`, `issue21-stella-counterfactual.yml`, `issue21-real-stella-fri-stress.yml`.
- Exact build: `dasm rom/src/main.asm -f3 -obuild/issue21/mellanrum_vnext.bin -lbuild/issue21/mellanrum_vnext.lst -sbuild/issue21/mellanrum_vnext.sym`, hash `18163c0435347695ee1cff5a4b6b19c80d280ec255eeb7f9b98711471ccde11c`.
- `docs/GAMEPLAY_CANON_DELTA.md` and `docs/TECHNIQUE_30_AUDIT.md`. Art source preserved by PR branch from PR16.

## Remaining blocker and recommendation to MAIN
Issue #21 is developed into a **true playable developer candidate** and real controller and idle tests passed. Do not merge yet. Commission **independent Verification and new-SHA Pachinko** against this exact SHA, human evaluation of whether correct-tree amber cue, phases, room challenge and darker TIA drone are meaningful, and optionally physical hardware + cycle trace/stack high-water. Confirm that changes are acceptably avant-garde and actually satisfying to play before any release. Retain old PR16 and PR4 as frozen historical references.
