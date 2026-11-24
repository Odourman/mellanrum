# MELLANRUM Issue26 – compatibility, test gates and nonclaims

**Native target:** stock NTSC Atari 2600 6507 + TIA + RIOT 128B, cartridge conventional **F6 four banks × 4096 bytes**. No extra cartridge RAM/Superchip, DPC/DPC+/CDF, ARM, special controller or console modification. Three distinct score banks plus core game bank; 6507 runs a common resident $FF90/$FF99 trampoline and emergency $FF9A reset mapper entry, no bank switching in visible kernel.

## What was tested
- Native DASM assembly each 4096B, concatenate to 16384B, exact F6 selector opcodes and bank3 reset vector. Actual GitHub Actions output and sha256 must be recorded.
- Real Stella 8.0_pre libretro core detects `Bankswitch Type: F6* (16K)`; 15 room wins and coda/title using frame-indexed controller commands, `video_callbacks==frames`, genuine PCM stereo and 128-byte RIOT RAM.
- Per-room long idle and critical-action counterfactual must be run **again for exact new SHA**; older PR23 demonstrations are historical only.
- Gopher2600 must separately prove actual new SHA, controller-only room wins and sampled 262-scanline image quality, not infer from Stella. Simulator source-only tests cannot replace this.
- Original legacy `game.yml`, `ab-stella.yml`, `ab-debugger.yml`, `stella-smoke.yml`, `title-presence-stella.yml` were scoped to unmodified 4K, `build_issue15.py` regenerates the older art and has a deliberately incompatible fixed ROM hash. They are version-gated for Issue26; strict new `issue26-native-f6.yml` is the relevant ROM + actual Stella required test. This avoids falsely reporting an old-4K test failure as a new 16K game defect.

## Still NOT_RUN or not safely proved
- **Physical original Atari** (real 6507/TIA revisions), actual physical reset/difficulty/joystick on CRT and cartridge reader: NOT_RUN.
- **RetroN 77 cartridge reader / Stella7 SD**: NOT_RUN. Ability of a libretro emulator to recognize standard F6 does not prove Hyperkin's cartridge reader accepts this cart. NTSC native 16K game may still work in Stella 7 by loading BIN from SD, but no direct test here.
- **PAL**: NOT_IMPLEMENTED.
- **Dynamic stack high-water and instruction-by-instruction worst-case timing on every possible frame**: NOT_RUN pending adequate tracer; 262 visible scanline samples plus source 76c/scanline are a finite sample, not universal coverage.
- **Independent Verification/Pachinko**: NOT_RUN for new F6 SHA until MAIN opens separately authorized jobs; Issues #24/#25 are pinned to prior 4K PR23 only.
- **Aesthetic/playability and subjective listening**: user/MAIN/GRAPHICS gate, not automatic "PASS" merely because DAC PCM is nonzero.

The developer must never mark any of those green without new same-SHA reproducible evidence. PR27 stays Draft and not merged/released.
