# MELLANRUM HEALTH LAB – FINAL TARGETED INDEPENDENT VERIFICATION, 2026-11-25

**Status:** `FINAL_TARGETED_VERIFICATION_PASS_BOUNDED`, separate `GLOBAL_ALL_PATH_TIMING_INCONCLUSIVE` and `FRI_RAW_PCM_STRICT_AB_INCONCLUSIVE`, `HUMAN_AND_PHYSICAL_NOT_RUN`. **Not RC2, not release, no product code edits.**

Read `00_MAIN_IV_HANDOFF.md` for the decision, `01_FINAL_TARGETED_VERIFICATION_REPORT.md` for complete technical adjudication (including a newly measured 3-colorclock audio bus delta), `02_TEST_MATRIX.csv` for every run and scope, `03_REMAINING_RISK_DISPOSITION.md`, `04_REPRODUCE.md`, `05_FAILURE_REPRODUCTIONS.md`, and `RESUME_STATE.json` for resumability.

All raw evidence captured in this new work is in EVIDENCE/* with original native Gopher command scripts, raw CPU/TIA/RIOT bus events, Stella true WAV and callback metadata; model ledgers in `ANALYSIS/*`. Original frozen RC1/LAB ROM bytes and exact source are under ROMS/SOURCE_SNAPSHOT. `BUILD_OR_PRIOR_BUILD_REFERENCE` are **previous** independent DASM outputs, preserved not counted as fresh builds. Three prior ZIPs referenced by their exact hashes, never misrepresented as new work.

Main evidence distinctions: 1 natural actII complete bank1 matched call, 4 naturally transported roomload cycle deltas with full RIOT INTIM and PF bus A/B, 1 natural taken OwlTryNext branch with 6 earlier same-value TIA sound register writes, 1 natural HUD fireX9 plus PR47 263-line negative and 9 forced state kernel diagnostics, 4 same-input FRI Stella captures showing within-ROM PCM nondeterminism. No new proven release-blocker. Global combined paths not formally closed.

**Full manifest:** `SHA256SUMS.txt` lists every other payload exactly once; test via `sha256sum -c SHA256SUMS.txt` after extraction. The manifest itself is excluded intentionally. ZIP CRC independently verified.
## Verifierade externa leveranslänkar

- [Original, komplett 951 526-byte SHA256-verifierad evidens-ZIP i GitHub](https://github.com/Odourman/mellanrum/blob/verification/health-lab-final-targeted-20261125/verification/health_lab_final_targeted/MELLANRUM_HEALTH_LAB_FINAL_TARGETED_VERIFICATION_EVIDENCE_2026-11-25.zip). ZIP SHA256: `200730e9ffe2d2467111289a5f30f7be4200ca7ebf72eef1f147a914c510ccf8`. Git binary blob SHA1: `934a142f49f1df9f117df5d0c3ab435ca7fcbeeb`; 239 entries, 238/238 payload SHA verified, ZIP CRC PASS. Not a base64 placeholder: committed raw binary bytes.
- [MAIN IV-handoff som native Google Doc i projektets Drive-mapp](https://docs.google.com/document/d/1eTcqwt-C9fMhBUW5SI6dzPpW-rZnAhnRFgt_w0rexaY/edit). Google Drive returnerade id och mapp-parent `1rO3ZTTBgyZZhqOx1WCxevM6sE3CrvUcl`; dokumenttexten återlästes.
- **Drive ZIP:** direkt uppladdning av lokal fil nekades av connectorns file-reference-validering. Den läsbara arkivfilen finns på GitHub ovan och i originalkonversationens verifierade `sandbox:/mnt/data`; **ingen påhittad ZIP-Drive-länk**.
