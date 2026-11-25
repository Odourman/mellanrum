# MELLANRUM HEALTH – PACHINKO handoff to MAIN IV (2026-11-25)

**Role:** PACHINKO STRESS TEST, separate from ROM DEVELOPMENT/HEALTH and independent VERIFICATION. **Diagnostic-only**; no ROM edits, no timer, RC2, merge, tag, or release.

**Specimen** LAB_STACK_INLINE_PADDED_B, 16,384-byte NTSC F6, SHA256 `8a59b84eb5151f78d40e6943c854d7e42c166b531aee3d40432182d32dcdf03b`. **Reference** PR49 RC1 SHA256 `456005ed691860b32c44b79f2a71666f622b005f5a798eadf9b549c59cff13bd`, PR49 HEAD `d013a0f82621d46ad12674a4a8e944bf005cd9c3`, product commit `7b400ad8678e8341a26f65cc757b1eb762654c83`. Experiment source is an archive snapshot, not HEALTH docs HEAD; `rom/src/main.asm` SHA256 `3246d67a40470454eb56c38f2f4c32fb34ccb4ff38ed796ccb10cf00a647d53e`.

**OWN RESULTS:** Fresh native DASM build byte-identical **PASS**. **Naturally taken OwlTryNext** confirmed in genuine Gopher frame2142, RC1 4 vs LAB 3 cycles, actual carry1. **All four targeted room-load extra cycles** observed with actual controller input: GeoMapHi indices1,2 and RoomStoneY indices4,5, each RC1 4 vs LAB 5. Selected complete raster frames 262 lines. Negative HUD x9 PR47 263, RC1/LAB 262. **105 state-guided risk profiles × 2 ROM ×720 frames =151,200 new Stella frames, 3255 matching state/pixel checkpoints, 0 differences**. Original Stella campaign A 2400-frame PCM identical; FRI PCM different across repeat runs of the *same ROM*, hence exact FRI PCM oracle INCONCLUSIVE, no confirmed LAB-specific audio fault.

**UNRESOLVED:** Full natural bank1 $FF90/$FFF7/$FFF9/$FF99 and full ten-byte stack bus trace did not finish (2×210s environment timeouts). Full all-path 76 CPU cycles, TIA register-write beam deadlines, RAM stack high-water, and physical original Atari / RetroN77 remain INCONCLUSIVE/NOT_RUN. A selected 262-line frame is no all-path timing proof.

**DISPOSITION:** `PASS_BOUNDED_PARTIAL / NO_NEW_CONFIRMED_LAB_BLOCKER / GLOBAL_ALL_PATH_TIMING_INCONCLUSIVE`. LAB is a defensible potential new base to *consider*, not a promoted RC2. Keep RC1 and LAB unchanged; seek specific independent bank1+beam timing gate before any later cutover/timer. No merge/tag/release.

**Raw complete evidence (Drive readback SHA and ZIP CRC verified):** https://drive.google.com/file/d/16okmdisZ5rnBDP8Oh_W63MNwXTehC019/view
- Archive exact SHA256: `f706afa7b934c87405a67898dfc48ca28753f3a140d26fc80fe87ac15728bd4e`
- Size **14,605,595 bytes**; **515 ZIP members**, **514/514 SHA manifest payloads PASS**, CRC PASS; original unaltered 16KiB LAB and RC1 ROMs, source snapshot, native DASM logs/listings/symbols, full new JSON input RLE, scripts, Gopher CPU/timer/raster logs, Stella frames and WAV.
- Full archive report `01_PACHINKO_FINAL_REPORT.md`, table `02_TEST_MATRIX.csv`, open timing risks `03_REMAINING_RISKS.md`, exact reproduce `05_REPRODUCE.md`.

**Authoritative limits:** previous HEALTH and VERIFICATION 15/15/idle results are references, *not* newly repeated PACHINKO passes. Gopher used v0.57.2 executable SHA `cca432ce75589d806b4d52ae48b76501e74dd4db0259ffe2b94c01853b0b3148`; Stella/libretro core SHA `2130ed1153cef66ef3f34bf9063f675f1f3342bc18320eb9ae5101743e3042df`; DASM ELF SHA `cfb23732297a4fe1c8d4a78d44206037d97733aedb2772503bbf029a4aa91291`.
