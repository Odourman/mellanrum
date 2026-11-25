# MELLANRUM HEALTH LAB – FINAL TARGETED INDEPENDENT VERIFICATION, 2026-11-25

**Status:** `FINAL_TARGETED_VERIFICATION_PASS_BOUNDED`, separate `GLOBAL_ALL_PATH_TIMING_INCONCLUSIVE` and `FRI_RAW_PCM_STRICT_AB_INCONCLUSIVE`, `HUMAN_AND_PHYSICAL_NOT_RUN`. **Not RC2, not release, no product code edits.**

Read `00_MAIN_IV_HANDOFF.md` for the decision, `01_FINAL_TARGETED_VERIFICATION_REPORT.md` for complete technical adjudication (including a newly measured 3-colorclock audio bus delta), `02_TEST_MATRIX.csv` for every run and scope, `03_REMAINING_RISK_DISPOSITION.md`, `04_REPRODUCE.md`, `05_FAILURE_REPRODUCTIONS.md`, and `RESUME_STATE.json` for resumability.

All raw evidence captured in this new work is in EVIDENCE/* with original native Gopher command scripts, raw CPU/TIA/RIOT bus events, Stella true WAV and callback metadata; model ledgers in `ANALYSIS/*`. Original frozen RC1/LAB ROM bytes and exact source are under ROMS/SOURCE_SNAPSHOT. `BUILD_OR_PRIOR_BUILD_REFERENCE` are **previous** independent DASM outputs, preserved not counted as fresh builds. Three prior ZIPs referenced by their exact hashes, never misrepresented as new work.

Main evidence distinctions: 1 natural actII complete bank1 matched call, 4 naturally transported roomload cycle deltas with full RIOT INTIM and PF bus A/B, 1 natural taken OwlTryNext branch with 6 earlier same-value TIA sound register writes, 1 natural HUD fireX9 plus PR47 263-line negative and 9 forced state kernel diagnostics, 4 same-input FRI Stella captures showing within-ROM PCM nondeterminism. No new proven release-blocker. Global combined paths not formally closed.

**Full manifest:** `SHA256SUMS.txt` lists every other payload exactly once; test via `sha256sum -c SHA256SUMS.txt` after extraction. The manifest itself is excluded intentionally. ZIP CRC independently verified.