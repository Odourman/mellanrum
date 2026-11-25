# MELLANRUM HEALTH LAB — Pachinko natural CPU witnesses (2026-11-25)

**Diagnostic only**, no product ROM changes. Frozen PR49 HEAD `d013a0f82621d46ad12674a4a8e944bf005cd9c3`; RC1 `456005ed691860b32c44b79f2a71666f622b005f5a798eadf9b549c59cff13bd`; LAB experiment `8a59b84eb5151f78d40e6943c854d7e42c166b531aee3d40432182d32dcdf03b`. Experiment source snapshot's `rom/src/main.asm` SHA256 `3246d67a40470454eb56c38f2f4c32fb34ccb4ff38ed796ccb10cf00a647d53e`.

## P0 natural OwlTryNext taken

Original Gopher2600 v0.57.2 (binary SHA `cca432ce75589d806b4d52ae48b76501e74dd4db0259ffe2b94c01853b0b3148`), physical emulated left Difficulty B, genuine FIRE from title and idle controller. No RAM POKE, no solution replay. **Frame2142, bank3**:
- RC1: `BCS` at PC `$F4FC`, Carry=1, taken to `$F567`, **4 cycles /12 color clocks**, SP `$F9`.
- LAB: `BCS` at PC `$F4FE`, Carry=1, taken to `$F569`, **3 cycles /9 color clocks**, SP `$F9`.
- Seven further observed branches per ROM had carry=0 and 2 CPU-cycles. The naturally taken path was also raster complete (262 sampled scanlines). This **closes the prior natural-taken reachability question** but not global TIA beam timing or maximum stack depth. Full raw SCRIPT, CPU register timeline and JSON in delivered evidence ZIP `OUTPUT/GOPHER_OWL_FRI_TAKEN/`.

## P0 true natural pagecross

Using native Gopher controller-only source-guided transport to genuine room loads, **without RAM POKE**:
- `GeoMapHi,X` PC `$F2ED`: room index1 frame964, index2 frame2497, **RC1 4 / LAB 5 CPU cycles** in both.
- `RoomStoneY,X` PC `$F2D5`: room index4 frame4483 and index5 frame5872, **RC1 4 / LAB 5 CPU cycles** in both, with full sampled frames at 262 lines in both. All four valid page-cross indices now have natural independent controller witnesses; full global VBLANK timer/first visible TIA deadline remains INCONCLUSIVE.

These are disjoint room index domains, *not* two penalties on one LoadRoom. Calls occur during VBLANK before RIOT timer wait. Detailed all-path timer-phase budget is not proven.

## Sensitive HUD x9 negative control

Same real joystick x9+FIRE on three ROMs: LAB **262,262**, RC1 **262,262**, original PR47 SHA `5b8315512bf274398c3d2f4622dc96e081d1481d93b2c8adaf6411de2e2a0ed5` **263,263**. Distinguishes actual detected historical fault from false all-pass monitor. This is one bounded controller sequence, not an all-case proof.

## Independent targeted differential Stella

New 105 naturally started room-adversarial sequences **per ROM**, seven profiles in all 15 rooms at 720 genuine frames per run = 75,600 frames each, 151,200 total. **3,255 matching pixel hashes and normalized game state checkpoints**, 0 differences. Full RLE and savestate provenance in archive.

## Outstanding P0

Natural `$FF90 → $FFF7 bank1 → $FFF9/$FF99` complete pre/post stackbus snapshots timed out after 210 seconds (twice, no valid snapshots); **INCONCLUSIVE**. Own max SP observation only `$F9` at the taken branch, not an independent full stack-high-water measurement. Global reachable 76-cycle/beam-register-write proof INCONCLUSIVE; physical Atari NOT_RUN. Do not promote LAB to RC2 or implement timer from this report.

Original PCM FRI strict equality is an **invalid comparative oracular basis in these captures**: three clean same-ROM runs per candidate generated different WAV PCM data despite identical input, read-only RAM samples and framebuffer hashes. Campaign 2,400-frame original TIA WAV AB was byte-equal. No confirmed LAB-specific audio defect.

Authentic raw data, exact ROMs, own rebuilt DASM listing, Gopher and Stella scripts, SHA manifest and CRC-verified ZIP are supplied independently. **No product code changed and no release authorization.**
