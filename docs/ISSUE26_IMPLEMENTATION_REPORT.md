# MELLANRUM – Issue #26 ROM DEVELOPMENT complete developer handoff (2026-11-23)

**Issue #26 MEL-055 authorized product target:** authentic **16,384-byte NTSC Atari 2600 standard F6**, four banks of 4,096 bytes with meaningful use. New **Draft PR #27**, branch `romdev/issue26-f6-16k-20261123`, separate from unchanged historic PR #23 / #16 / #4.

**Exact complete real product ROM**: `rom/bin/MELLANRUM_16K_NTSC_F6.bin`; **16384 bytes**, SHA-256 **`7ce777dc273e1c30d8621843052e941ced41fcf2961bcdf835576a11c9592446`**; Git blob SHA **`958d7505e5e1af7fbf43cb2e1d8571aa9e12c6b5`**. Native DASM re-build four banks is deterministic using `python3 rom/f6/build_f6.py`. Native bank0..3 listing/symbols/vectors/hotspots/build metadata are in Issue26 Actions artifacts. No additional cartridge RAM, CPU, DPC/CDF/ARM or special controller.

## 4 KiB PR23 → 16 KiB Issue26 concrete changes

| Area | Frozen PR23 4K | New Issue26 authentic F6 |
|---|---|---|
| ROM code/data | Single 4,096B bank | Four independent **4,096B banks**, exact 16,384B, standard stock Atari F6 |
| Real room soundtrack | Four small tone/pitch constants and brief Presence noise | **15 distinct per-room 256-frame × 3-stream TIA score pages**, 768 bytes/room, **11,520 actual score bytes** used across all 15 rooms (five scores per act bank); changes true AUDC/AUDF/AUDV plus linked subtle visual background |
| CPU bank architecture | None | Shared resident-PC `$FF90` trampoline, `LDA $FFF6,X` bank0..2, original score interpreter, return `LDA $FFF9`, emergency crossbank reset recovery at `$FF9A`; source-specific bank vectors and tests |
| Gameplay | 15 distinct levels, echoes revert after delay | **New optional Act II/III 'recall echo' mechanic**: press FIRE again on a queued tree to cancel future reversal and flip stone polarity; creates a consequential alternative decision; old 15 puzzle witnesses preserved |
| Art | Fixed per-act background colors | Per-room TIA second voice drives low-key color breathing; Act-specific green forest/PF stays; original approved U3, S3, negative Presence retained |
| CI | Several obsolete Issue15 4K workflows failed | Native F6 exact build and real Stella 15-room gate **SUCCESS**; old 4K workflows appropriately scoped away on Issue26; old fixed `len==4096` audio guard repaired in new branch |
| Editorial | Prior 30-technique audit | All **30/30** re-reviewed against six actual Google Drive source docs; 10 useful original TIA techniques, incompatible special cartridge tricks 27..30 excluded |

All 15 earlier vNext room maps are retained (not redesigned a second time). Scope explicitly prioritizes audio/atmosphere, an alternative meaningful interaction and authentic architecture. This is **not** a claim that the 15 puzzles each gained a mandatory new submechanic. That qualitative goal requires human playing and independent assessment.

## REAL native development test matrix, same exact final 16KiB ROM SHA

| Gate | Actual measured result | Classification |
|---|---|---|
| Native DASM / F6 / linker | Four 4096-byte banks, 16,384-byte concatenation, opcode and vector tests, startup bank3, no cart RAM | **DEVELOPER PASS** |
| Stella mapper and hardware core | Real Stella 8.0_pre core SHA `2130ed1153cef66ef3f34bf9063f675f1f3342bc18320eb9ae5101743e3042df`, detects `F6* (16K)`, NTSC 60fps, RIOT 128B, TIA output 31440Hz | **DEVELOPER PASS** |
| Native Stella joystick-only campaign | **15/15** actual room victories, **13,940** authentic video frames, entire coda and title return at frame **13,939**, no POKE or forced RAM; 103 screenshots | **DEVELOPER PASS** |
| Native Gopher2600 joystick-only campaign | **15/15** verified room completion checkpoints `mode=2`, **14,068** real frames, `mode=3` coda then title `mode=0`; **202/202** genuine sampled TV FRAME frames exactly 262 NTSC raster lines | **DEVELOPER PASS** |
| No input / 600-second session each room | **0/15** autonomous victories, **15×36,000 = 540,000** real Stella frames from emulator states reached normally by joystick | **DEVELOPER PASS** |
| Omitted necessary FIRE counterfactual | **0/15** room victories when one designated mandatory action deleted from its original replay and followed by 36,000 frames per room, **540,000** additional actual Stella frames | **DEVELOPER PASS** |
| New active echo-recall mechanic | Real Stella frame-indexed joystick+FIRE in II-01, **slot0Key 17→255**, polarity **1→0**, tree map unchanged, no ROM/RIOT injection, exact 16K SHA | **DEVELOPER PASS** |
| Long FRI SKOG stress | **50,000** native Stella video/audio callback frames on same SHA, no crash, frame callbacks match requests | **DEVELOPER PASS** |
| Real original hardware TIA sound | Full real Stella captured two-channel **31,440Hz stereo PCM** throughout 13,940 campaign frames; native audio excerpts ACT I, ACT II, ACT III/Presence and FRI; full video uses original source mixer | **SIGNAL PASS; subjective listening NOT_RUN** |
| Replayed real audio/video | MP4 contains **13,940 genuine Stella video callback frames at 60fps**, exact original 15 winning frames and title/coda sequence; soundtrack derived from genuine Stella TIA mixer, not a simulated retro track | **DEVELOPER PASS** |
| 30 tricks | 30/30 source-audited (six linked original Google docs), 10 used where helpful, excluded special cart schemes | **SOURCE AUDIT PASS; not 30 physical experiments** |
| PAL / RetroN77 cart reader / physical Atari2600 | No physical console test, no PAL build. Stella core recognized F6, which is **not** hardware compatibility proof | **NOT_RUN / NOT_IMPLEMENTED** |
| Worst-case SP stack high-water and every executed instruction register beam deadline | Actual 262-line samples and native DASM listing, but no comprehensive worst-case proof across all states/hardware revisions | **NOT_RUN** |
| Independent Verification and Pachinko | Existing Issues #24/#25 apply only to frozen PR23 **4K**; cannot certify new 16K candidate | **NOT_RUN; NEW ISSUES REQUIRED** |
| Subjective graphics/audio/gameplay acceptance and release | End-user artistic approval and actual gameplay playtesting not completed; no merge/release | **BLOCKED BY USER/MAIN** |

**Historical comparison:** PR23 4K product SHA `63e719a362ae2eb5689484ca7c28c628b495a2843723898ebec3fe6374c43bdc` and independent verification #24/#25 concern only that version, never used as new F6 results.

## Exact source and artifact index

- Native ROM and build: `rom/bin/MELLANRUM_16K_NTSC_F6.bin`, `rom/f6/build_f6.py`, `rom/f6/bank0_score.asm`, `bank1_score.asm`, `bank2_score.asm`, `rom/src/main.asm`, `rom/src/data.inc`.
- Authoritative new design detail: `docs/ROM_16K_F6_BANK_MAP.md`, `docs/GAMEPLAY_16K_DESIGN_DELTA.md`, `docs/SOUND_DESIGN.md`, `docs/TECHNIQUE_30_AUDIT.md`, `docs/COMPATIBILITY_16K_F6.md`.
- Reproducible native CI `.github/workflows/issue26-native-f6.yml` and byte-locked `.github/workflows/issue26-pin-rom.yml`. Green CI run [45165327606](https://github.com/Odourman/mellanrum/actions/runs/45165327606) / native source snapshot. F6 pinned success [45165359110](https://github.com/Odourman/mellanrum/actions/runs/45165359110).
- Real Stella controller capture: `tests/issue15/stella_full_campaign.py`, `tests/issue15/libretro_stella_capture.py` guarded by new exact 16K hash.
- True Gopher controller harness `tests/issue21/gopher_full_campaign.py` with strict 202 checkpoints and code/RAW log.
- Local bundled archive from ROM DEVELOPMENT includes exact native 16KiB ROM and all four native DASM bank listings/symbols, immutable source snapshot ZIP/TAR, Gopher all-room screenshots and raw checkpoints, Stella 103 authentic gameplay screenshots, original two-channel WAV/three edited excerpts and full original synchronized game video, 15-room idle/counterfactual individual evidence, new echo recall proof, 50K FRI run result, checksummed manifest.

## F6 memory, DMA and timing risks

F6 changes the cartridge ROM window only, **never** system RAM/TIA hardware. Shared crossbank trampoline uses 6507 CPU stack only for normal JSR/RTS; RIOT memory remains 128B. Bank-dependent sound interpreter runs during VBLANK, not within critical displayed sprites and playfield raster; exact worst-case 76 CPU cycles/line on physical revisions still not certified. This is the crucial difference between developer-emulator result and release-ready hardware proof.

**Delivery state: NEW FULL 16KiB F6 DEVELOPER CANDIDATE IMPLEMENTED; Draft PR, no merge, no release.** MAIN must open fresh independent Verification and Pachinko issues pinned to the exact `7ce777dc...` ROM SHA. User retains final art/audio/gameplay/physical release authority.
