# MELLANRUM – ROM DEVELOPMENT – Issue #9 hardware-only A/B

Date: 2026-11-22. Source freeze: authorized user order `docs/MAIN_TO_ROMDEV_AB_HARDWARE_ONLY_2026-11-22.md` on `main`, GitHub Issue #9.

## Scope

- Starting immutable PR #4 code HEAD `eea14339010306de635a8c6238e242b76b28cc64`, native 4 KiB ROM SHA256 `a9531d5bbbff033711fbe54f8688b8e0259640e0a9a284c8ab585eea415c0bd5`.
- LEFT console Difficulty **A** (SWCHB bit6=1) selects campaign; LEFT **B** (bit6=0) selects goal-free FRI SKOG. Read from hardware **only when the first FIRE press starts the game from title**. During playing, `mode` remains latched even if either difficulty changes.
- No joystick/SELECT-based mode selection. SELECT on title no-op; in-game SELECT reloads the same room and retains mode. RIGHT difficulty (bit7) not consulted. Console RESET returns to title; the next title FIRE re-reads LEFT A/B. Hardware cannot force physical switch into A; the normal campaign is the result **when the user sets left A**.
- Old nonverbal selectable icons and their data tables are removed; the 24-line icon area is now empty. Title's *only text* remains a single horizontal `MELLANRUM`. Raster WSYNC count adjusted by one in former icon band so development tracer still reports 262 NTSC scanlines. The existing title glyphs and V5.1/PRESENCE renderers remain byte-identical at the source level.
- Original 15 rooms/room geometry, tree/echo/phase/Presence logic, two audio channels and title font tables untouched; no change to phase/collision map/gameplay rules.

## Developer checks actually run locally (initial pre-CI snapshot; final matrix below supersedes pending labels)

- `reference/test_engine.py`: 20/20 PASS (original reference).
- `scripts/check_rom_vs_model.py`: 15/15 cursor-aware solutions and 225 seeded runs / 4352 tick comparisons PASS (developer 6502 CPU model).
- `scripts/check_playfield.py`: 20 dynamic edit checks PASS.
- `scripts/check_input.py`: title SELECT no-op, LEFT B to free mode, in-game SELECT same mode, movement/repeat, RESET and FIRE edge PASS.
- `scripts/check_hardware_ab.py`: LEFT/RIGHT A/B combinations, title A->B/B->A, joystick, SELECT title no-op, held FIRE, mid-game switch latch, RESET new latch, RIGHT irrelevant PASS.
- `scripts/check_title_presence.py`: exact 9 glyph `MELLANRUM`, no icon tables, Presence warning/active/release and unchanged PF/map PASS.
- `scripts/check_frame_budget.py`: 15 rooms x 64 sampled frames, 262 NTSC scanlines in **developer CPU/RIOT/WSYNC model**, not a certified real TIA scanline analyzer.
- Native DASM **pending GitHub Actions at the time of this report creation**; exact build SHA and actions links must be filled in handoff after successful job.
- Real Stella F5/F6 left, F7/F8 right, FIRE/RESET and raw screenshot test is set up as `.github/workflows/ab-stella.yml`; actual run results must be read, not inferred from existence of workflow.

## Test evidence boundaries (historical pre-CI expectations; superseded by final measured matrix)

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

## Measured post-run developer handoff (new ROM)

**Immutable game-code commit:** `6cb86247c668162b180e5d77377098941b9803b3`; subsequent GitHub revisions only improve the evidence scripts and documentation. PR #4 remains Draft/open/unmerged.

**New production ROM:** `rom/bin/mellanrum_ntsc.bin`, NTSC, 4096 bytes, SHA-256 `e9ea87d381bcf8da39ec055d7d6951ceff97b21d3a798addd10fbbe540c5e974`.

- **Native DASM and model**: GitHub Actions [45074641192](https://github.com/Odourman/mellanrum/actions/runs/45074641192) **SUCCESS**. Original `reference/test_engine.py` 20/20; 15/15 original model solution sequences; 225 seeded extra runs / 4352 ticks; 20 PF edits; original Presence regression, A/B input matrix and 262-line developer CPU model; native DASM vs separate subset assembler exact binary match. Downloaded Actions artifact SHA equals this file byte-for-byte.
- **Static native DASM**: [45074641135](https://github.com/Odourman/mellanrum/actions/runs/45074641135) and later runs **SUCCESS**.
- **Real Stella raw original PNGs**: GitHub Actions [45075039996](https://github.com/Odourman/mellanrum/actions/runs/45075039996) **SUCCESS**, artifact `14774798060`, 12 authentic 320x228 gameplay/title/RESET/FIRE PNGs plus real input event TSV, exact ROM binary and native assembler listing. Observed A=Campaign green/dark (pixel sample at 100,20 = `(0,39,88)`), B=FRI SKOG white/blue `(210,210,209)`. LEFT A/B toggles during gameplay do not change original scene palette; after RESET+FIRE, the **opposite** scene is launched for both A->B and B->A. SELECT/directional title screenshot is byte-identical to original title; only the nine-glyph MELLANRUM word is present. See `evidence/issue9/README.md` and 12 unmodified `.png` files. The contact sheet only adds labels outside original frames.
- **Real Stella debugger**: [optional debugger workflow](https://github.com/Odourman/mellanrum/actions/runs/45075145159) executed Stella in debugger mode but first run yielded no persisted readable RAM/RIOT session; this is **NOT_VERIFIED**, not a measured SWCHB register value or RAM mode PASS. A larger-display follow-up is diagnostic only and must be evaluated from real artifact contents, not simply workflow success.
- **RetroN 77**: Manufacturer instructions state front SKILL P1 toggles left player difficulty A/B. [Hyperkin RetroN77 manual](https://m.media-amazon.com/images/I/A1JvAxgMXCL.pdf) and [Stella RetroN77 docs](https://fossies.org/linux/stella/docs/index_r77.html) document the hardware-mapped controls; the physical unit and its updated Stella firmware are **NOT_RUN** here, so actual electrical input behavior is not certified.
- **Known unverified**: exact frame-indexed replay for entire 15-room campaign in actual emulator, independent TIA line timing/WSYNC analyzer, real audio audition, PAL (not implemented), physical Atari/RetroN77, independent Verification and MAIN acceptance. Prior Pachinko and Verification evidence applies solely to the superseded `a953...` build; this new SHA requires its own full-system checks.

**Release gate remains CLOSED.** No merge or release authorized by this report. MAIN should freeze the new native ROM hash for later Pachinko 2.0 and independent Verification only after reviewing the attached raw evidence and outstanding limitations.

## Final verification matrix (supersedes the initial pending matrix above)

| Scope | Status | Exact evidence |
|---|---|---|
| 4 KiB NTSC native DASM, source identity, byte equality | **PASS** | Actions 45074641192, 45075040009, 45075144767; downloaded ROM 4096 bytes, SHA256 e9ea87d3... |
| V5.1 original suite and 15/15 CPU/oracle room witnesses | **DEVELOPER_PASS** | 20/20 reference tests, 15/15 witnesses, 225 additional / 4352 ticks, 20 PF edits |
| Original title MELLANRUM only, removal of A/B menu | **PASS in CPU model and real Stella screenshots** | `scripts/check_title_presence.py`, Issue9 raw title PNGs |
| LEFT A vs B starts distinct gameplay, F5/F6, right F7/F8, SELECT/joystick, midgame hold, RESET re-read | **DEVELOPER_PASS / STELLA_VISUAL_PASS** | actual emulator Actions 45075039996; 12 screenshots, input_events.tsv; strict after-RESET opposite-palettes assertions pass |
| Exact RIOT SWCHB and mode=$B8 values **inside Stella debugger** | **NOT_VERIFIED** | Built-in debugger runs 45075145159 and 45075291531 launched with -ld A/B and attempted scripted `print *SWCHB`, `print *$B8`, `saveSes`, but neither saved an inspectable command session; no register value asserted from logs |
| 262 NTSC scanlines for title and 15 rooms | **DEVELOPER_MODEL_PASS; ACTUAL TIA ANALYZER NOT_RUN** | 945 game frames plus title in custom CPU/WSYNC tracer; raw Stella screenshots exist, no 262 frame counter capture |
| Source V5.1 room/Presence/echo/phase/audio unchanged by scoped diff | **SOURCE_DIFFERENCE_PASS** | `docs/ISSUE9_AB_SOURCE_DIFF.patch`, 15 original room JSON SHA ea80a4cc..., prior Presence Stella pictures are historical, not new independent certification |
| RetroN77 hardware SKILL P1 and original physical Atari test | **NOT_RUN** | mapping documented externally, no actual device in tool session |
| Full frame-exact 15-room real-emulator replay / Pachinko 2.0 / independent VERIFICATION | **PENDING** | must be run on exact new e9ea87d3... candidate |

**Observed gameplay colors, not standalone RAM introspection:** the two modes have different world palettes and source rooms in the normal production ROM. After title FIRE, real Stella renders campaign on LEFT A and free forest on LEFT B. When switches are flipped during gameplay, the image remains in the current mode. After RESET+FIRE, it changes appropriately to the new mode. This supports actual A/B functionality in Stella but is not a substitute for a debugger register trace; that subtest is explicitly NOT_VERIFIED.
