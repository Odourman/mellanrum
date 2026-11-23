# MELLANRUM vNext – Issue #21, user-authorized Atari 2600 cartridge

**Active vNext candidate** is the isolated Draft PR #23 branch `romdev/issue21-vnext-16k-20261123`; do not mistake this for frozen PR #16 or earlier PR #4. The historic one-line assertion "no gameplay ROM exists" was obsolete.

## Build real Atari 2600 native ROM

From repository root with real DASM:

```sh
mkdir -p build/issue21
dasm rom/src/main.asm -f3 -obuild/issue21/mellanrum_vnext_ntsc.bin -lbuild/issue21/mellanrum_vnext.lst -sbuild/issue21/mellanrum_vnext.sym
wc -c build/issue21/mellanrum_vnext_ntsc.bin
sha256sum build/issue21/mellanrum_vnext_ntsc.bin
python3 -m unittest discover -s reference -p test_engine.py -v
python3 reference/check_rooms.py
```

The new game currently fits **unbanked 4K (4096 bytes)**, well inside the hard **16384-byte** limit. An authentic standard 4K ROM needs neither F6 nor cartridge coprocessors or extra RAM; if a later approved revision crosses 4096, introduce authentic F6 four-bank ROM and test all hotspots. Do not pretend F6 is already in use.

**Canonical new rooms:** `reference/rooms.json`, exactly 15 unique geometries. Their exact generated/hand-packed `GeoMap0..14` and `GeoPF0..14` metadata live in `rom/src/data.inc`; original graphic U3/S3/Presence masks preserved. Do not run `build_issue15.py` against the new candidate; that older script regenerates the **frozen historical PR #16 game** and would overwrite the new 15-room map and audio modifications. Use the native `dasm` command and commit-specific CI as the reproducibility entrypoint. See `docs/GAMEPLAY_CANON_DELTA.md` for intentional rule/map differences.

## Evidence, strict boundaries

- `.github/workflows/issue21-native-vnext.yml`: real native DASM, full listing+symbols, exact ROM SHA and **mandatory** room/model tests.
- `.github/workflows/issue21-stella-vnext.yml`: real Stella/libretro controller-only 15-room campaign and actual TIA PCM; separate true gameplay PASS (not just a successful workflow, because optional experiments may fail).
- `tests/issue21/gopher_full_campaign.py`: real Gopher HEADLESS joystick/FIRE run with no POKE and exact 262-line TV FRAME samples, all 15 rooms and coda.
- Source-only reference/model wins do not count as emulator wins. ROM SHA must match every emulator evidence result.
- The earlier `rom/bin/mellanrum_ntsc.bin` is the **old PR #16 frozen 4 KiB artifact**; do not replace it. The new vNext binary must be distinguished as `mellanrum_vnext_ntsc.bin` in Actions/archive.
- Independent Verification, adversarial Pachinko, physical console/RetroN77/PAL, end-user art and human gameplay/release acceptance remain separately gated.

**NO MERGE / NO RELEASE** under ROM DEVELOPMENT authority.
