# MELLANRUM – real 16KiB F6 NTSC (Issue #26, Draft PR #27)

## Build a standard unmodified Atari 2600 ROM
The Issue26 product is **NOT** the old single-bank Issue21 ROM. Current user-approved game candidate uses standard **F6 four-bank 16KiB cartridge** and real 6507/TIA/RIOT only.

```bash
sudo apt-get install dasm
python3 rom/f6/build_f6.py --out build/issue26
sha256sum build/issue26/MELLANRUM_16K_NTSC_F6.bin
```

**Exactly 16,384 bytes** and expected binary SHA-256 `7ce777dc273e1c30d8621843052e941ced41fcf2961bcdf835576a11c9592446`. A source modification must produce a **new** hash and rerun all emulator tests; never keep using a frozen SHA.

The already built, hash-confirmed game ROM is versioned in GitHub `rom/bin/MELLANRUM_16K_NTSC_F6.bin`, not generated as empty padded banks. Score banks are `rom/f6/bank0_score.asm`, `bank1_score.asm`, `bank2_score.asm`; real 15-room game/NTSC raster lives in `rom/src/main.asm`, `rom/src/data.inc`. Three score banks include 15 individually active room-specific TIA sequences, with shared crossbank call/return/reset trampoline; all are actually executed by 6507.

## How to play / controls
On **title**: physical left difficulty switch **A = campaign**, **B = FRI SKOG**; press **FIRE** to start selected mode. **Joystick** moves the visible mark, not the autonomous owl; hover over mutable trees or stone and press FIRE to influence the forest/stone. **SELECT** restarts the current room. **RESET** returns to title. On a completed room, FIRE advances. In Acts II/III, a second FIRE on an echo-pending tree cancels the queued reversal and instead flips stone polarity. The active Presence can intercept specific FIRE gestures. Title text is only `MELLANRUM`; no action gameplay, scores, conventional enemies or boss.

For a stock 2600 cartridge, F6 is the standard 16KiB bank mechanism, no custom cartridge RAM/assist CPU. Authentic original hardware and Hyperkin RetroN77 **have not been physically tested**. Stella 8.0_pre authentic libretro recognizes F6* (16K) and runs all 15 rooms.

## Reproducibility / evidence
`docs/ISSUE26_IMPLEMENTATION_REPORT.md` is the developer receipt. `docs/ROM_16K_F6_BANK_MAP.md` documents all bank windows/selector/reset, `docs/SOUND_DESIGN.md` actual two-channel TIA score, `docs/GAMEPLAY_16K_DESIGN_DELTA.md` exact scope vs PR23, `docs/TECHNIQUE_30_AUDIT.md` original 30 technique cross-reference and `docs/COMPATIBILITY_16K_F6.md` residual risks. 
`.github/workflows/issue26-native-f6.yml` builds all banks, runs strict source tests and **requires actual complete 15-room Stella controller gameplay and PCM audio**. `.github/workflows/issue26-pin-rom.yml` commits *only* the versioned ROM file on the new branch, byte-for-byte native DASM.

**Historic protected ROMs:** PR23 frozen 4KiB ROM SHA `63e719...bdc`; PR16 `45d342...`; PR4 `e9ea87...`. They remain unchanged. **Do not run `build_issue15.py`** against Issue26; it regenerates historical PR16 source/graphics and is not the F6 build method. Legacy 4K CI jobs are guarded for this Issue26 branch.

**No merge or final release under ROM Development authority**. Independent Verification and Pachinko on this exact new SHA, worst-case timing/stack and original hardware/RetroN77 remain pending.
