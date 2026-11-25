# MELLANRUM – PACHINKO HEALTH LAB final diagnostic report 2026-11-25

## Exact objects and own provenance
- Experiment: `LAB_STACK_INLINE_PADDED_B`; 16,384-byte NTSC standard F6 ROM `8a59b84eb5151f78d40e6943c854d7e42c166b531aee3d40432182d32dcdf03b`.
- Baseline: frozen PR49 draft/unmerged product SHA256 `456005ed691860b32c44b79f2a71666f622b005f5a798eadf9b549c59cff13bd`; PR HEAD `d013a0f82621d46ad12674a4a8e944bf005cd9c3`; product commit `7b400ad8678e8341a26f65cc757b1eb762654c83`.
- HEALTH documentation HEAD `3cf158aaa2f74ed95f36f46a0e75806ac54e80eb` / independent Verification documentation HEAD `dbccdb4fde6b8f900eb6f971acb8e99ae2047b1f` are not specimen product commits. Experiment material is an immutable source snapshot; main.asm SHA `3246d67a40470454eb56c38f2f4c32fb34ccb4ff38ed796ccb10cf00a647d53e`.
- Fresh native DASM 2.20.14.1 build in isolated output matches delivered LAB ROM exactly; raw .lst/.sym/banks/build logs in Drive archive. Original HEALTH archive SHA `f8950badc9fed8495a7dfa5fbd7849dd8b5b252cfe9dfba125b041fe7e1289f1` checked CRC/1299 manifest. Independent Verification archive SHA `d4eca534a98cc5cb5222a05fed961cc05e6d3f5bd8fa472ad15df24229b4a599` checked CRC/1047 manifest. Those results are references, not own emulator work.

## Own P0: NATURAL taken branch
An independent, naturally reached FRI SKOG difficulty B + title FIRE then idle Gopher2600 controller route reached `BCS OwlTryNext` at **frame2142** in both ROMs, carry=1. Actual bank3 PC RC1 `$F4FC` to `$F567` cost **4 cycles/12 color clocks**; LAB `$F4FE` to `$F569` cost **3 cycles/9 color clocks**, both SP `$F9`. Seven further observed carry0 visits per ROM cost 2 cycles each. Natural reachability for this taken branch is now empirically confirmed without POKE; this is not a global downstream TIA-beam proof. Full original CPU, register, line traces and Gopher SCRIPT in evidence archive.

## Own P0: all four naturally controller-reached room-load extra cycles
- `LDA GeoMapHi,X` PC `$F2ED`: room index1 frame964 **4→5** RC1→LAB, index2 frame2497 **4→5**, full Gopher raster 262.
- `LDA RoomStoneY,X` PC `$F2D5`: room index4 frame4483 **4→5** and index5 frame5872 **4→5**, full Gopher raster 262.
These domains do not occur together in one LoadRoom. They are before RIOT wait in VBLANK. Complete TIM64T/INTIM all-path phase and first visible TIA write bus deadlines not proven. All results are **PASS_BOUNDED**.

## Own P0: HUD x9 negative oracle
Natural joystick x9+FIRE scripts on original immutable PR47 `5b8315512bf274398c3d2f4622dc96e081d1481d93b2c8adaf6411de2e2a0ed5`: **263,263 lines**. Exact RC1 and LAB **262,262** each. True hardware debugger execution, proves sensitivity to known historical fault; not all paths safe.

## Own P1: 151,200 genuine Stella controller frames
Seven different profiles across all 15 rooms for each ROM, **105 cases per ROM ×720 frames**. Naturally controller-reached initial savestates (SOURCE_GUIDED transport separated) and new deterministic per-case input RLE. Profiles EDGE_X9, PENDING_FIRE_STORM, CTRL_RESET_SELECT, BEAT_BOUNDARY, PRESENCE_HUNT, RANDOM_FUZZ, STICK_DIAGONALS. Last profile includes diagnostically possible counter-direction stubs, not a physical joystick claim. **3,255** matched framebuffer and normalised game-state checkpoints, no differences and no observed bounded state range violation. These are 105 independent new room-conditioned scenarios per ROM, not 105 complete blind campaigns or all-path coverage. Includes all three acts, cursor x9, all ack statuses and Presence states across trials.

## Authentic PCM / 1x image controls
Separate Stella captures LAB/RC1 × campaign Difficulty A/FRI B, 2400 frames each, real 31,440 Hz TIA stereo PCM and native screenshots. Campaign 2400 frame WAV exact same hash `41b84640d19ca449fcbe5b416c2b19e489d96623bf099c7fdf5ef317f0da673c`. First FRI WAV pair differed, but **two independent same-ROM repeat attempts for EACH candidate** using identical controller RLE, read-only sampled RAM, pixelhashes, seed and core *also differ in PCM within the same ROM*: strict FRI LAB vs RC1 equality cannot be treated as regression oracle. Original sampled PNGs same. **FRI AUDIO PARITY INCONCLUSIVE; no confirmed LAB-specific audio defect**.

## Missing/blocked own tests and scope
Natural full bank1 pre-$FF90 to $FFF7 sound bank and return $FFF9/$FF99, preserving every RIOT stack byte, was attempted in two new native Gopher processes but both timed out after 210.02 seconds without a complete sample. **INCONCLUSIVE**. Max dynamic stack depth across all game states NOT_RUN by this actor (selected natural Owl branch SP=$F9 only). Overall 76 CPU cycles/scanline and exact WSYNC/TIA write beam position along all reachable paths INCONCLUSIVE. Physical original NTSC Atari, RetroN77, human cold play and subjective audio NOT_RUN. P2 1M random-frame target not pursued because target natural P0 branch and pagecross gave more information. No product ROM changes or release approved.

## Overall conclusion and next step
**No newly reproduced LAB-specific release blocker** in measured PACHINKO tests. `PASS_BOUNDED_PARTIAL` for actual controller paths; `GLOBAL_ALL_PATH_TIMING_INCONCLUSIVE` and `BANK1_FULL_STACKBUS_INCONCLUSIVE`. Recommend to MAIN IV: retain frozen RC1 and LAB for now, LAB may be preferred *as candidate* based on restored two-byte stack reserve (independent Verification) plus observed natural faster branch, but do not call it RC2. Require dedicated independent full natural bank1+stackbus and worst-case TIA timing pass before any promotion; any timer implementation needs separate user authorization. No merge/tag/release.

## Complete reproducibility and provenance
Drive ZIP with raw inputs/scripts/logs/real WAV/PNG/native ROMs/DASM listing/symbols and 514/514 SHA manifest entries, CRC PASS:
https://drive.google.com/file/d/16okmdisZ5rnBDP8Oh_W63MNwXTehC019/view
SHA256 `f706afa7b934c87405a67898dfc48ca28753f3a140d26fc80fe87ac15728bd4e`, 14,605,595 bytes, 515 entries. All exact executed counts and limitations are in archived `02_TEST_MATRIX.csv`, `03_REMAINING_RISKS.md`, `04_FAILURE_REPRODUCTIONS.md`, and `05_REPRODUCE.md`.

**Test branch contains only diagnostic text; do not imply it is a rebuilt product or an independently verified release.**
