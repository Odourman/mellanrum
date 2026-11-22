# Mellanrum: Skogen som lyssnar

**Atari 2600 / NTSC / 4 KiB / 6507-DASM source**, implementation proposal from ROM DEVELOPMENT, 2026-11-22.

This is a complete 15-room _implementation candidate_ grounded in the original V5.1 Python state machine and GRAPHICS V5.1 source data. Native DASM build has passed in GitHub Actions; actual Stella/Gopher2600/physical-hardware verification remains outstanding. The 4 KiB file shipped in the local package is **byte-for-byte identical to the real DASM-built ROM** obtained from GitHub Actions `rom-build` artifact, run `45064122338`. The independent Python subset assembler was corrected to match DASM's `$FF`-filled unused ROM bytes. This proves byte identity and assembler production, **not** emulated or physical hardware functionality. GitHub Actions also runs state/model/raster developer checks.

## Gameplay

Three acts of five rooms: mirror editing; echoes and delayed reversals; XOR collision phase and an intermittent intent-stealing Presence. The owl is autonomous and moves each 72 NTSC frames. The cursor, not the owl, is directly controlled. There are no lives, scores, weapons, or conventional enemies. The image uses the three material motifs of trees, owl and stone; Presence has no separate physical entity.

- **Joystick:** move cursor. Immediate first move, about 200 ms before repeat, 100 ms subsequent repeat. Direction order when diagonal: up, left, down, right.
- **FIRE:** på titeln startar vald fysisk A/B-inställning och låser spelläget fram till RESET eller titelretur. I spelet är FIRE edge-activated. When the cursor is on an editable tree, flip its mirrored pair; on the stone, reverse stone polarity. Max one accepted action each owl tick. Other cells give a denied cursor shape.
- **VÄNSTER Difficulty A/B:** fysisk vänster konsolomkopplare avgör spelläge, **A = kampanj (rekommenderat standardläge)**, **B = FRI SKOG**. Välj innan FIRE på titeln. Du måste ställa den fysiska omkopplaren på A för kampanj; ROM kan inte flytta den. I Stella används F5 (vänster A) och F6 (vänster B). Höger Difficulty påverkar inte spelläge.
- **SELECT:** på titeln ingen funktion; inne i spelet startar SELECT om aktuellt rum men byter aldrig spelläge.
- **RESET:** return to title.
- **KAMPANJ:** all original I-01 through III-05 in order. When owl finds exit, wait for FIRE to continue after a 48-frame stillness. After the last room, an 8-second coda then title.
- **FRI SKOG:** goal-free version of an original Act III geometry, selected by a deterministic seed from title-frame count. Press RESET to leave.

## Building

Requires `dasm` (`apt install dasm`) and Python 3. No pip dependencies.

```sh
make check
```

Or:

```sh
mkdir -p build
dasm rom/src/main.asm -f3 -obuild/mellanrum_ntsc.bin -lbuild/mellanrum_ntsc.lst -sbuild/mellanrum_ntsc.sym
python3 scripts/check_rom.py build/mellanrum_ntsc.bin
```

The native ROM target is a fixed 4,096-byte, standard 4K cart; no F6 bank switching is required by the final compact code. This is a deliberate mapper downgrade from a V5.1 16K F6 *working hypothesis*, not a change to the room logic.

### Automated checks

- Reference suite: `cd reference && python3 -m unittest -q test_engine.py`.
- Data provenance: `python3 scripts/generate_rom_data.py --original reference/rooms.json --graphics graphics --output rom/src/data.inc --check`.
- Genuine 6502 binary subset compiler (developer comparison only): `python3 scripts/assemble_check.py rom/src/main.asm -o build/mellanrum_ntsc.bin`.
- Instruction-level ROM vs V5.1 tick engine: `python3 scripts/check_rom_vs_model.py`.
- Playfield integrity after dynamic toggles: `python3 scripts/check_playfield.py`.
- Frame-level control tests: `python3 scripts/check_input.py`.
- 262-line timer/WSYNC model, all 15 rooms: `python3 scripts/check_frame_budget.py`.
- CPU trace: `python3 scripts/cpu_trace.py`.

**Evidence boundary:** the standalone Python assembler, CPU interpreter, and frame model are developer test tools. They do **not** replace DASM/Stella/Gopher2600 nor independent VERIFICATION. Full raster timing, display stability, color fidelity, CRT readability, and audio listening are unverified until actual emulator and hardware tests are run.

## Technical implementation

- One 4K ROM with all 15 room metadata and exactly five repeated original geometries.
- 128 bytes of RIOT RAM only. `pfbuf` 48 bytes and up to 16 used stack bytes.
- True TIA reflection `CTRLPF.REF`, per-row upper 6-line crown/lower 14-line trunk bands, P0 owl/P1 player cursor/BL stone/M0 exit; no fabricated framebuffer.
- Two-channel TIA sound with deliberately sparse drones, echo variation, and audible silence. No PCM or imported music.
- Short visual indicators for phase, echo occupancy, stone polarity, Presence warning/active/return, and input acceptance/denial.
- Gameplay input is latched from the video-frame polling point then processed before echo/phase/actor movement at the next logical beat. One pending event per beat; held FIRE never repeats.

See [Developer report](docs/DEVELOPER_TEST_REPORT.md) and [Source integrity](docs/PROVENANCE.md).

## Independent Verification

Verification is a separate role and has not approved this build. Developer checks do not substitute for independent review.

## A/B hardware-control revision, Issue #9

Title remains exactly **MELLANRUM** without mode-selection icons. Only LEFT Difficulty A/B determines mode at title FIRE. Joystick directions, SELECT and RIGHT Difficulty are never mode selectors. Switching A/B midgame cannot affect the already-latched mode. See `docs/ISSUE9_AB_HARDWARE_REPORT.md` and GitHub Actions results for the new ROM SHA. The superseded Issue #8 ROM hash is not this candidate. On RetroN 77, the front **SKILL P1** button is documented as toggling player-1/left Difficulty A/B; this mapping was not physically tested with our ROM and updated firmware.
