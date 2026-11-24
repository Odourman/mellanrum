# MELLANRUM RC1 — INDEPENDENT VERIFICATION, Issue #50

This is independently created verifier-owned evidence for the **unchanged 16,384-byte RC1 NTSC F6** Atari 2600 cartridge. It is **NOT** a modified product ROM and **NOT** a release approval.

**RC1 ROM SHA256:** `456005ed691860b32c44b79f2a71666f622b005f5a798eadf9b549c59cff13bd`

PR49 product commit `7b400ad8678e8341a26f65cc757b1eb762654c83`, later workflow-only PR HEAD `d013a0f82621d46ad12674a4a8e944bf005cd9c3`.

Main report: `INDEPENDENT_VERIFICATION_REPORT.md`. Machine status: `TEST_MATRIX.json`. Source is protected; independent verification branch `verification/issue50-rc1-20261124`; native two-build successful CI https://github.com/Odourman/mellanrum/actions/runs/45466845934 .

## What is inside

- `src_archive/`: the immutable ROM byte source, source ASM/Python build tooling, original replay *controller-only* witness and its provenance. Source-guided replay is NOT independent puzzle discovery. Includes historical PR47, PR44 ROMs **only for regression**, not as RC1 candidates.
- `src_archive/TOOLS/`: authentic pinned native DASM, Gopher2600, Stella/libretro binaries (original upstream provenance in report). No font assets.
- `buildA/` / `buildB/`: two genuinely independent full native builds (ROM, four banks, listing `.lst`, symbols `.sym`, build stdout).
- `gopher_full/`: the new full genuine 19,780-frame Gopher controller-only execution, >20,000 all-frame 262 raster observations, 18,190 F6 score bank events and original full stdout.
- `emulator_RC1/`, `room_states/`: verifier-owned complete campaign/coda/restart, original 1× PNGs, serialized room-start states for authentic idle/causal/recovery tests.
- `idle/`, `causal/`, `recovery/`, `hud_tests/`, `fri_50000/`, `fri_wrap/`, `visual_independent/`, `symbol_pairs/`, `markers/`: original test JSON/logs and native emulator screenshots. Forced diagnostic RAM tests are labeled in results and cannot count as controller-only natural play.
- `fresh_RC1/`, `fresh_PR47/`, `fresh_PR44/`: real **same-core separate OS-process** original PCM/WAV, screenshot checkpoints, and exact PCM hashes. `audio_comparison/` 13 pairs of comparison WAV excerpts (RIOT/API provenance in report).
- `video/`: **independently recorded** 50-second sample H264/AAC from the same live Stella run (not the whole campaign), genuine TIA output.
- Verifier-owned Python scripts are at ZIP root; original common adapter and known controller witness under `src_archive/`.
- `SHA256SUMS`: authoritative complete archive-member SHA manifest excluding itself. Every listed entry must pass. `sha256sum -c SHA256SUMS` from the extraction directory. ZIP CRC passed at packaging.

## Reproduce from same Linux environment

Scripts were executed with root directory `/mnt/data/RC1_INDEPENDENT`; extract the ZIP into that directory to reproduce **the same absolute paths**. The artifact already includes **all necessary `src_archive/` source, original tools, ROM and SOURCE_GUIDED replay files**. The ZIP's embedded README incorrectly mentions a separate `SOURCE_REFERENCE` folder; it does not exist and **no reconstruction is needed**. This corrected GitHub document supersedes that paragraph of the embedded ZIP README; ZIP bytes/hashes are unchanged. For alternative extraction paths change each verifier-side diagnostic script's constant `P` to point to your extraction root, without changing the product ROM.

From `/mnt/data/RC1_INDEPENDENT/src_archive/SOURCE/`:

```bash
export PATH="/mnt/data/RC1_INDEPENDENT/src_archive/TOOLS:$PATH"
python rom/f6/build_f6.py --out /mnt/data/RC1_INDEPENDENT/rebuildA
python rom/f6/build_f6.py --out /mnt/data/RC1_INDEPENDENT/rebuildB
cmp /mnt/data/RC1_INDEPENDENT/rebuildA/MELLANRUM_16K_NTSC_F6.bin /mnt/data/RC1_INDEPENDENT/src_archive/CANDIDATE/MELLANRUM_RC1_NTSC_F6.bin
cmp /mnt/data/RC1_INDEPENDENT/rebuildA/MELLANRUM_16K_NTSC_F6.bin /mnt/data/RC1_INDEPENDENT/rebuildB/MELLANRUM_16K_NTSC_F6.bin
```

From extraction root, run `python independent_gopher_full.py`, `python independent_stella.py`, `python make_native_room_states.py`, `python run_15_idle.py`, `python run_15_causal.py`, `python run_15_recovery.py`. For reproducible PCM, invoke `python independent_pcm_one.py RC1`, then `python independent_pcm_one.py PR47`, then `python independent_pcm_one.py PR44` in three **separate OS processes**. Some runners depend on complete original source relative paths, captured inside `src_archive`; see their code. Original known replay traces: `src_archive/REFERENCE_PR47/CAMPAIGN/controller_frame_events.json` and `src_archive/EVIDENCE/ALLFRAME/commands.txt`. They are independently replayed inputs, NOT verifier-discovered puzzle solutions.

## Explicit unresolved gates

`GLOBAL_REACHABLE_76_CPU_CYCLES`: **INCONCLUSIVE**; `INDIVIDUAL_PRESENCE/FIRE/ECHO_EXTREME`: **INCONCLUSIVE**; `NATURAL_4_RETICLE_SAME_SCENE`: **NOT_RUN**; physical original NTSC Atari 2600, RetroN 77 and human cold-play/audio/art acceptances: **NOT_RUN**. Strict reference-PR44 PCM *identity* is **FAIL** (50 sample values) but is not independently demonstrated as an audible product defect. **No merge, no release**.