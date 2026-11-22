# MELLANRUM – ROM DEVELOPMENT – Issue #9 hardware-only A/B

Date: 2026-11-22. Source freeze: authorized user order `docs/MAIN_TO_ROMDEV_AB_HARDWARE_ONLY_2026-11-22.md` on `main`, GitHub Issue #9.

## Scope

- Starting immutable PR #4 code HEAD `eea14339010306de635a8c6238e242b76b28cc64`, native 4 KiB ROM SHA256 `a9531d5bbbff033711fbe54f8688b8e0259640e0a9a284c8ab585eea415c0bd5`.
- LEFT console Difficulty **A** (SWCHB bit6=1) selects campaign; LEFT **B** (bit6=0) selects goal-free FRI SKOG. Read from hardware **only when the first FIRE press starts the game from title**. During playing, `mode` remains latched even if either difficulty changes.
- No joystick/SELECT-based mode selection. SELECT on title no-op; in-game SELECT reloads the same room and retains mode. RIGHT difficulty (bit7) not consulted. Console RESET returns to title; the next title FIRE re-reads LEFT A/B. Hardware cannot force physical switch into A; the normal campaign is the result **when the user sets left A**.
- Old nonverbal selectable icons and their data tables are removed; the 24-line icon area is now empty. Title's *only text* remains a single horizontal `MELLANRUM`. Raster WSYNC count adjusted by one in former icon band so development tracer still reports 262 NTSC scanlines. The existing title glyphs and V5.1/PRESENCE renderers remain byte-identical at the source level.
- Original 15 rooms/room geometry, tree/echo/phase/Presence logic, two audio channels and title font tables untouched; no change to phase/collision map/gameplay rules.

## Developer checks actually run locally

- `reference/test_engine.py`: 20/20 PASS (original reference).
- `scripts/check_rom_vs_model.py`: 15/15 cursor-aware solutions and 225 seeded runs / 4352 tick comparisons PASS (developer 6502 CPU model).
- `scripts/check_playfield.py`: 20 dynamic edit checks PASS.
- `scripts/check_input.py`: title SELECT no-op, LEFT B to free mode, in-game SELECT same mode, movement/repeat, RESET and FIRE edge PASS.
- `scripts/check_hardware_ab.py`: LEFT/RIGHT A/B combinations, title A->B/B->A, joystick, SELECT title no-op, held FIRE, mid-game switch latch, RESET new latch, RIGHT irrelevant PASS.
- `scripts/check_title_presence.py`: exact 9 glyph `MELLANRUM`, no icon tables, Presence warning/active/release and unchanged PF/map PASS.
- `scripts/check_frame_budget.py`: 15 rooms x 64 sampled frames, 262 NTSC scanlines in **developer CPU/RIOT/WSYNC model**, not a certified real TIA scanline analyzer.
- Native DASM **pending GitHub Actions at the time of this report creation**; exact build SHA and actions links must be filled in handoff after successful job.
- Real Stella F5/F6 left, F7/F8 right, FIRE/RESET and raw screenshot test is set up as `.github/workflows/ab-stella.yml`; actual run results must be read, not inferred from existence of workflow.

## Test evidence boundaries

| Target | Status at report creation | Evidence target |
|---|---|---|
| ROM normal gameplay from 15 source rooms | DEVELOPER_PASS | native DASM and CPU oracle |
| A/B physical SWCHB bit 6 input | DEVELOPER_PASS; Stella pending | CPU model reads $0282; genuine Stella hotkey and debugger evidence required |
| LEFT A vs LEFT B starts 2 game modes | DEVELOPER_PASS; Stella pending | Stella screenshots of title and started room with actual F5/F6 |
| RIGHT F7/F8 irrelevant; SELECT and joystick cannot switch | DEVELOPER_PASS; Stella pending | nonselected visual title + RAM model |
| Midgame latch and RESET then FIRE new mode | DEVELOPER_PASS; Stella pending | RAM model and Stella input event logs |
| Title one word and no icons | DEVELOPER_PASS; Stella pending | Stella native production ROM PNG |
| III-03/04/05 original Presence renderer | DEVELOPER_PASS; old image evidence not transferred automatically | unchanged source + candidate-specific Stella captures |
| 262-line actual Stella beam, complete campaign, audio listening, physical Atari/RetroN77 | NOT_RUN | independent Verification/Pachinko later; specific hardware unavailable locally |
| PAL | NOT_IMPLEMENTED | NTSC scope only |
| Independent Verification, MAIN release authorization | PENDING | no merge/release |

**RetroN 77**: physical left-difficulty availability and any RetroN-to-Stella mapping must be checked on that actual hardware. Neither emulator PC hotkeys nor source proves the RetroN 77 has equivalent accessible buttons; hardware is NOT_RUN.

## Source identity and handoff

Authoritative prior Issue-8 production candidate SHA `a9531d5b...` must not inherit PASS on changed bytes. Freeze the new 4096-byte ROM's exact GitHub Actions SHA in the final comment to Issue #9, together with immutable commit, actual PNG log artifact and new matrix. Subsequent Pachinko 2.0 and independent Verification must use **this new** hash. PR #4 remains **Draft / unmerged**.
