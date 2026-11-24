# INDEPENDENT VERIFICATION #42 — PR #38 BFDEB — 2026-11-24

**Verdict: INCOMPLETE / RELEASE_BLOCKED.** Genuine independent tests have run against the immutable 16 KiB NTSC F6 product. The zero-byte observed stack margin and unverified worst-case CPU/raster/banking remain P0 blockers. This is NOT a release, artistic signoff, or Pachinko #41 result.

## Identity / independent build
- Exact Draft PR: https://github.com/Odourman/mellanrum/pull/38; source HEAD `6e9db179867234a19cce329c709170f2423ffbbb`; product commit `9293c46eb323f47197046e07e1178279d6c7f525`.
- Git ROM blob `51dc00b5ce8170b289acd0b4d997e0c6080b8f54`; standard F6, 4 × 4096 B = **16,384 B**; whole SHA-256 `bfdeb5308dcecc526e802cd95886b94e0ce4953628e7bc7190c5d49231deac06`, independently computed.
- Bank 0 SHA `4f1fefc7513d5c0aef2d1c2a406b77975e59fc60e0a3361fa34455b4c669c49f`
- Bank 1 SHA `8d49d78a7f7ea98d1638693767de146b54b7b97673eb5f077fbf9c0554e3a1e8`
- Bank 2 SHA `6b82511ba23726be41aa5f7a4e8c2555f5e039ee6fc2ec6a1e0774117cfffbfc`
- Bank 3 SHA `58411650362d2bd377a85b44fbb1cf3ee9f87d35b1ab26170c1d2efd8b0f9cf5`
- **Independent clean native DASM BUILD_PASS**, Github Actions https://github.com/Odourman/mellanrum/actions/runs/45381991878, job `138403084696`, Ubuntu 24.04 DASM Debian package `2.20.15~20201109+really2.20.14.1-2`: assemble `rom/f6/bank{0,1,2}_score.asm` and `rom/src/main.asm` individually with `dasm FILE -f3 -oOUTPUT -lLIST -sSYMS`, concatenate four banks. Exactly byte-identical to Git product, all four SHA values and whole SHA. Own native build artifact `14913109392`. Bank0–2 reset/IRQ vectors `$FF9A`; bank3 `$F000`. Production code untouched.

## P0 actual stack risk — no fabricated overflow
- Source has **118 contiguous RIOT variables $80–$F5** and stack starts `SP=$FF`. Only `$F6–$FF` (10 bytes) free.
- Actual **native Gopher2600 CPU instruction trace of 296,758 instructions** under source-guided controller input in Act I, 215-frame bounded run: observed **minimum `SP=$F5`**, exactly 10 bytes used and **zero spare byte margin**. Actual five-JSR chain `Frame → GameFrame → BeatTick → CommitFire → ToggleTree → DecodeKey`. No corruption was observed in that bounded run. This is a reproduced *risk*, NOT a reproduced stack-overflow FAIL.
- Independent forced-room Act III diagnostic (separately labeled RAM POKE): **306,601 actual CPU instruction observations**, minimum `SP=$F7` (8 bytes). Again no observed corruption. No whole-game maximum-SP trace. **FULL_STACK_SAFETY=INCONCLUSIVE/P0.**
- On the 6507, stack page `$01xx` mirrors RIOT byte range; an additional push beyond 10 bytes would overlap variables such as `markerPtr` near `$F4/$F5`. Recommend an engineering proof or additional headroom, never an unauthorized in-place ROM patch.

## F6 and 262 lines
- Own real Gopher native F6 trace: bank3→bank0/1/2→bank3, correct hotspots `$FFF6/$FFF7/$FFF8/$FFF9`, 8 switching pairs per test. Act I is controller-reached; Act II/III are clearly labeled `FORCED_ROOM_POKE_DIAGNOSTIC`. Correct bank return observed, no misbank in three bounded probes; exhaustive bank/stack/audio transitions **INCONCLUSIVE**.
- **2,224 genuine complete NTSC TV FRAME reports** = 262 scanlines, from an independently reexecuted early section of controller-only Gopher campaign. First boot transient report (20 lines) explicitly excluded. An attempted `TV FRAME` after every step of full 19k campaign exceeded execution window; **do not call it a full Gopher 15/15 PASS**.
- Extra real Gopher isolated Act II (room5) 312/312 and Act III (room12) 312/312 native TV reports = 262 lines, but forced-room diagnostics. **Total 2,848/2,848 measured complete frame samples 262** in these bounded windows.
- All frame raster, all object paths, **76 CPU cycles/scanline worst-case**: **NOT_RUN/INCONCLUSIVE**. Stella video callbacks alone do not prove that beam timing.

## Actual independently executed Stella/libretro controller tests
Native **Stella 8.0_pre 8dd5600**, core SHA `2130ed1153cef66ef3f34bf9063f675f1f3342bc18320eb9ae5101743e3042df`, original 160×228 screen and original 31,440Hz PCM, no product ROM edits.

- **PASS SOURCE_GUIDED full campaign:** independently restarted Stella/libretro and re-executed existing developer-known physical frame-indexed joystick/FIRE witness (295 input intervals), **19,652 actual video frames** through rooms0–14 (15 active+15 solved), coda mode3, return title mode0, no POKE. This is independent *emulator reproduction*, NOT newly solved puzzles. Additional independent fresh per-frame telemetry observed 73 genuine FIRE rising edges, 170 relevant state changes, three acts/Presence warning+active+release, actual original screenshots.
- **PASS 15/15 independent 36,000-frame idle:** 15 separate Stella instances, each begun from own genuine controller-reached serialized room-start state; **540,000 real frames**, 0 passive wins, 0 unrequested room swaps.
- **PASS 15/15 bounded causal omissions:** 16 separate Stella original-witness-altered FIRE-omission trials. Each of 15 rooms had at least one original FIRE interval whose deletion prevented victory **at the original baseline win frame**; this does NOT prove absence of delayed wins or alternate routes.
- **PASS 50,010 active FRI SKOG frames:** independently seeded physical joystick/FIRE/SELECT, toggled physical Difficulty during gameplay, state bounds and mode4 held, no POKE; recorded exact original inputs and native frames. Additional independent 26,000-frame Stella FRI run without SELECT/RESET observed real `beat=255→0` at **frame 18,486** with no measured state violation.
- **Four different original-resolution 160×228 HUD images:** `ackType 0/1/2/3` have objectively different native rendered bitmap regions, **FORCED_RAM_DIAGNOSTIC**, not physical-reachability proof of every mode. Separate **PASS controller-driven actual Presence interception** from authentic ActIII room12 state: 1 direction move + FIRE during Presence active, real `ackType=3` from frame 15,904 for 26 frames, no POKE. 15 different room screenshots and source-art faithful masks retained. Human 1× readability INCONCLUSIVE.

## Original TIA audio evidence
Independently captured authentic Stella PCM 16bit 31,440Hz `tia_audio.wav` for whole SOURCE_GUIDED campaign, **327.517s**, 10,297,124 samples/channel, SHA256 `dfc844225143a4e90f6f5e4d5c8da7f735948c82066632754ef7701e3760c52a`. Recorded two output channels are mono-identical, NOT separate hardware stereo. Segment-level RMS provided. **PASS original emulator PCM capture; human artistic listening NOT_RUN.**

## Remaining final gates and recommendation
**INCOMPLETE/NOT_RUN:** exact all-frame 262 raster and real all-path 76 CPU cycles, all-mode dynamic stack highwater after full 15-room play, full independent native Gopher 15/15 (partial only), arbitrary bank-hotspot fuzz with audio/presence/beat edge, independent full alternate puzzle solutions / generalized softlock search, physical unmodified Atari/RetroN77, original approved design archive byte provenance, human cold-play, moving-mark legibility, sound/music acceptance, PAL.

**MAIN III recommendation:** DO NOT MERGE / RELEASE. Reassess 0-byte stack margin and obtain complete worst-case bank/stack and CPU-budget verification (or separately authorized product changes with *new* checksum and fresh tests). Then independent graphics/sound/hardware and human review.

## Reproducing / raw evidence
Separate Verification-only branch: `verification/issue42-pr38-bfdeb-20261124`. Original source and ROM in PR38 never changed. Verification delivered **275-entry evidence ZIP** in the Verification Chat, including **273 evidence/source files + SHA256SUMS + JSON**, 22,462,435 bytes, archive SHA256 `c10b3c4930f31a03225c104b6b35b225511a5e6a91398e19b22c90fbc1ba796c`. ZIP itself is **not on GitHub**. It contains exact ROM, 4-bank independent DASM listings/symbols/results, original Gopher and Stella binaries, Python replay scripts, developer-labeled source-guided input witness, saved frame-indexed inputs, 15 serialized room starts, all original PNG, 327s WAV, raw CPU/bank/raster debugger logs, all idle and causal JSON, and full Swedish report. Every member independently validated against its embedded SHA256SUMS; ZIP CRC PASS. Evidence archive is available to the user from this ChatGPT conversation only. No source, ROM, game design or original artwork changed.