# MELLANRUM RC1 — INDEPENDENT VERIFICATION, Issue #50

This is independently created verifier-owned evidence for the **unchanged 16,384-byte RC1 NTSC F6** Atari 2600 cartridge. It is **NOT** a modified product ROM and **NOT** a release approval.

**RC1 ROM SHA256:** `456005ed691860b32c44b79f2a71666f622b005f5a798eadf9b549c59cff13bd`

PR49 product commit `7b400ad8678e8341a26f65cc757b1eb762654c83`, later workflow-only PR HEAD `d013a0f82621d46ad12674a4a8e944bf005cd9c3`.

Main report: `INDEPENDENT_VERIFICATION_REPORT.md`. Machine status: `TEST_MATRIX.json`. Source is protected; independent verification branch `verification/issue50-rc1-20261124`; native two-build successful CI https://github.com/Odourman/mellanrum/actions/runs/45466845934 .

## What is inside

- `SOURCE_REFERENCE`: the immutable ROM byte source, source ASM/Python build tooling, original replay *controller-only* witness and its provenance. Source-guided replay is NOT independent puzzle discovery. Includes historical PR47, PR44 ROMs **only for regression**, not as RC1 candidates.
- `TOOLS`: authentic pinned native DASM, Gopher2600, Stella/libretro binaries (original upstream provenance in report). No font assets.
- `BUILD_A` / `BUILD_B`: two genuinely independent full native builds (ROM, four banks, listing `.lst`, symbols `.sym`, build stdout).
- `GOPHER_FULL`: the new full genuine 19,780-frame Gopher controller-only execution, >20,000 all-frame 262 raster observations, 18,190 F6 score bank events and original full stdout.
- `STELLA_CAMPAIGN`, `NATURAL_ROOM_STATES`: verifier-owned complete campaign/coda/restart, original 1× PNGs, serialized room-start states for authentic idle/causal/recovery tests.
- `IDLE`, `CAUSAL`, `RECOVERY`, `HUD_GOPHER`, `FRI_STRESS`, `U3_RUNTIME`, `SYMBOL_PAIRS`, `MARKER_FORCED`: original test JSON/logs and native emulator screenshots. Forced diagnostic RAM tests are labeled in results and cannot count as controller-only natural play.
- `AUDIO_RC1`, `AUDIO_PR47`, `AUDIO_PR44`: real **same-core separate OS-process** original PCM/WAV, screenshot checkpoints, and exact PCM hashes. `AUDIO_COMPARE` 13 pairs of comparison WAV excerpts (RIOT/API provenance in report).
- `STELLA_VIDEO`: **independently recorded** 50-second sample H264/AAC from the same live Stella run (not the whole campaign), genuine TIA output.
- `TEST_SCRIPTS`: Python sources, including archived original common libretro adapter and a reference controller witness.
- `SHA256SUMS`: authoritative complete archive-member SHA manifest excluding itself. Every listed entry must pass. `sha256sum -c SHA256SUMS` from the extraction directory. ZIP CRC passed at packaging.

## Reproduce from same Linux environment

Scripts were executed with root directory `/mnt/data/RC1_INDEPENDENT`; to rerun exactly, place the extracted contents at that root, then reconstruct the nested `src_archive` paths as below or edit each script's constant `P` to the extraction root (a diagnostic-only path edit, not a game ROM change):

- `src_archive/CANDIDATE/MELLANRUM_RC1_NTSC_F6.bin` from `SOURCE_REFERENCE/CANDIDATE/`
- `src_archive/TOOLS/` from `TOOLS/`
- `src_archive/SOURCE/` from `SOURCE_REFERENCE/SOURCE/`
- `src_archive/REFERENCE_PR47/` from `SOURCE_REFERENCE/REFERENCE_PR47/`
- `src_archive/REFERENCE_PR44/` from `SOURCE_REFERENCE/REFERENCE_PR44/`
- `src_archive/EVIDENCE/ALLFRAME/commands.txt` from `SOURCE_REFERENCE/EVIDENCE/ALLFRAME/commands.txt`

In `src_archive/SOURCE/`, set `PATH="$PWD/../../TOOLS:$PATH"` and run `python rom/f6/build_f6.py --out ../../buildA` and again to `buildB`. Compare with `SOURCE_REFERENCE/CANDIDATE/MELLANRUM_RC1_NTSC_F6.bin`.

For Gopher full replay: `python TEST_SCRIPTS/independent_gopher_full.py` with original pinned native tool, original ROM, `SOURCE_REFERENCE/EVIDENCE/ALLFRAME/commands.txt`; this test took minutes, generated original 16 MB stdout and JSON. For Stella: `python TEST_SCRIPTS/independent_stella.py`; `python TEST_SCRIPTS/make_native_room_states.py`, `python TEST_SCRIPTS/run_15_idle.py`, `run_15_causal.py`, `run_15_recovery.py` and `independent_pcm_one.py RC1/PR47/PR44` in separate OS processes. See each script for exact CLI and its immutable SOURCE_GUIDED controller preconditions. Avoid using historical *invalid preliminary* `independent_pcm_compare.py` from this developer session (not included). Preserve distinct paths for source/diagnostic vs product proof.

## Explicit unresolved gates

`GLOBAL_REACHABLE_76_CPU_CYCLES`: **INCONCLUSIVE**; `INDIVIDUAL_PRESENCE/FIRE/ECHO_EXTREME`: **INCONCLUSIVE**; `NATURAL_4_RETICLE_SAME_SCENE`: **NOT_RUN**; physical original NTSC Atari 2600, RetroN 77 and human cold-play/audio/art acceptances: **NOT_RUN**. Strict reference-PR44 PCM *identity* is **FAIL** (50 sample values) but is not independently demonstrated as an audible product defect. **No merge, no release**.