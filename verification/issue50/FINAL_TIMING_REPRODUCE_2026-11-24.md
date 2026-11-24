# VERIFICATION #50 — reproduction for final targeted RC1 timing addendum (2026-11-24)

Follow-up to MAIN IV [authorized order #7144993648](https://github.com/Odourman/mellanrum/issues/50#issuecomment-7144993648), not a repeat of earlier full campaign/idle/native build. Product PR #49 must remain unchanged.

**Immutable RC1**: exact 16,384-byte standard NTSC F6 SHA-256 `456005ed691860b32c44b79f2a71666f622b005f5a798eadf9b549c59cff13bd`; PR HEAD `d013a0f82621d46ad12674a4a8e944bf005cd9c3`; product commit `7b400ad8678e8341a26f65cc757b1eb762654c83`.

Full original evidence directly supplied as `MELLANRUM_RC1_FINAL_TIMING_VERIFICATION.zip` in the **independent Verification ChatGPT conversation**; it has not been uploaded to GitHub or Drive and no URL is invented.

Archive identity: **21,419,217 bytes**, SHA256 `f53c5ea0c2550237ce53a4ec63d2fb7ff5ee3df7f73e440b6b6cb102915f8005`, **202 ZIP entries / 201 SHA256SUMS entries**, CRC PASS. Check `unzip -t` and after extraction `sha256sum -c SHA256SUMS`.

Package includes genuine original RC1 ROM (verify SHA), prior independent complete native DASM listings / symbols, pinned native Gopher2600 ELF (SHA256 `7b12dff57fcb73154122d2477f35d9c8ae8b344649bc0faa8ff6f5663c70470b`, upstream source `74c544203378c1448a33c29bc8b4586079b050f4`), original source snapshot, exact command files for every new test, raw Gopher instruction/CPU/TIA bus logs, four bank hotspot return traces, natural frame124 5th JSR stack-bus event, ten HUD columns, 7 beat threshold cases, 4x2 same-row polarity cases, machine-readable matrices and the full 15KB Swedish technical report `REPORTS/FINAL_TIMING_VERIFICATION_REPORT_2026-11-24.md`.

Original executable commands are in `EVIDENCE/FRESH/<case>/commands.txt`. On supported Linux x86_64, inspect the original command file then run `TOOLS/gopher2600 HEADLESS SOURCE/MELLANRUM_RC1_ORIGINAL_NTSC_F6.bin < EVIDENCE/FRESH/<case>/commands.txt`, with SDL2/OpenGL/ALSA dependencies installed. The test Python scripts used absolute paths rooted `/mnt/data/RC1_TIMING_WORK` on the original verifier machine. For reexecution elsewhere, update the ROOT/ROM/GOP/OUT defaults at the head of `SCRIPTS/*.py` to extracted paths and choose an empty output directory; do not modify the original game ROM.

Important distinctions: Cases labeled `DIAGNOSTIC_POKE` are forced RIOT state; natural controller-only cases are labeled separately. Native Gopher **ONSTEP CPU,TIA** reports PC instruction start, whereas real TIA bus writes are reported in `EVIDENCE/FRESH/bus_write/...` via `TRACE STRICT/ONTRACE`; real WSYNC write cycle is inferred from instruction-start +3 CPU cycles because tracing can emit post-stall WSYNC location. Ordinary 75/76 Stem13 bound is conditional on valid sprite/Y indexes, no ROM-page crossings. HUD x9 WSYNC completes exactly at 76/76 and has no spare cycles. No universal all-path TIA timing proof claimed.

Marker correction code is separately published at [independent_markers_roi_fix.py](https://github.com/Odourman/mellanrum/blob/verification/issue50-rc1-20261124/verification/issue50/independent_markers_roi_fix.py). It uses the four original 160×228 Stella PNGs and gives **0/14/30/28 pixel differences from neutral**. Earlier self-comparison zero field was a test-script mistake, NOT product ROM failure.

Global status remains `INDEPENDENT_VERIFICATION_INCONCLUSIVE` for all-reachable-codepath 76-cycle and every TIA write deadline. No new confirmed game defect. No merge, release or unauthorized implementation.
