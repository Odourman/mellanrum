# MAIN: Real Stella no-input test of PR #16 – 2026-11-23

**Status: LOCAL_MAIN_NATIVE_STELLA_DIAGNOSTIC / NOT_INDEPENDENT_VERIFICATION / GAMEPLAY_DESIGN_DEFECT.**

- Target: Draft PR #16 frozen source HEAD `56d70c316031bf55a5260e1fbbe0fe187c55f297`, ROM 4096 bytes, SHA-256 `45d3422371d41bf896c0ac0076c57d93e600dcf7f4a1e51d4d352312fce8d7a7`.
- Real emulator: Stella/libretro 8.0_pre 8dd5600, core SHA-256 `2130ed1153cef66ef3f34bf9063f675f1f3342bc18320eb9ae5101743e3042df`.
- Baseline: replay the previously recorded actual frame-indexed controller-only 15-room campaign (see original [Actions run #45091957175](https://github.com/Odourman/mellanrum/actions/runs/45091957175)) with actual Stella/libretro.
- At every room's true start (`mode=1`, `introFrames=107`, `beat=0`, original owl/cursor start), save a **real libretro emulator serialized state**, not a synthetic RAM-modded room. Restore it in same core, then send **no control input** (no FIRE, joystick, RESET or SELECT) for up to 7200 frames per room. Read real RIOT 128-byte RAM `mode` and `room` **without writes or POKE**. `mode=2` means automatic room victory. For remaining I-02 repeat to 36000 zero-input frames.

| Original room | No-input native Stella result | Frames until automatic victory |
|---|---|---:|
| I-01 | AUTO_WIN | 971 |
| I-02 | NO_WIN_OBSERVED (10 minutes) | >36000 |
| I-03 | AUTO_WIN | 827 |
| I-04 | AUTO_WIN | 971 |
| I-05 | AUTO_WIN | 971 |
| II-01 | AUTO_WIN | 971 |
| II-02 | AUTO_WIN | 971 |
| II-03 | AUTO_WIN | 827 |
| II-04 | AUTO_WIN | 971 |
| II-05 | AUTO_WIN | 971 |
| III-01 | AUTO_WIN | 1979 |
| III-02 | AUTO_WIN | 1403 |
| III-03 | AUTO_WIN | 3995 |
| III-04 | AUTO_WIN | 1979 |
| III-05 | AUTO_WIN | 1907 |

**14/15 rooms independently auto-win within 13.8–66.6 seconds with literally no player action.** Room I-02 did not auto-win within 600 seconds (does not prove it never can).

**Important caveats:** In full original campaign, the player still has to press FIRE after winning a room to advance to the next (`mode=2`), so the 15-room progression is not literally fully hands-off. But player intervention is not necessary for solving 14/15 *individual rooms*, a major design issue. This independent MAIN local run is not a new GitHub Actions job, release approval, or a second role's Verification PASS. No ROM/PR4/product source changes.

**Exact reexecution instructions:** obtain native ROM + DASM symbol file from [Actions #45090981800 artifact 14781417357](https://github.com/Odourman/mellanrum/actions/runs/45090981800), original Stella controller events/core from development [Actions #45091957175](https://github.com/Odourman/mellanrum/actions/runs/45091957175), replay to legitimate room start, snapshot via `retro_serialize`, resume via `retro_unserialize` and run 7200 blank-button frames, sample RAM via read-only `retro_get_memory_data(2)`. The exact 2 scripts, manifest JSON, original ROM, and source replay inputs were packaged as a downloadable MAIN chat ZIP; they are not hosted on GitHub. Preserve exact source SHA and core binary SHA.

**Art/design:** Do not "fix" this only by slowing the owl or by arbitrary 'press FIRE once' gating. Require meaningful interactive choices through tree edits, stone polarity, echo/phase/Presence, with designed puzzle state graphs and no passive win paths. Original V5.1 room coordinate/canon changes need separate MAIN/user review; seek design proposals first, not unapproved production geometry changes.