# Issue #43 — ROM DEVELOPMENT III, Gate A developer handoff (2026-11-24)

**Decision:** **TECHNICAL FEASIBILITY PASS for the separate prototype**, not independent verification, merge or release. In the tested emulator conditions only **S3-A Minnesskärva** changes orange/red by committed `polarity`, while **S3-B Omvänd skog** retains its original amber color even when both glyphs share a raster row. This is the originally authorized option A; no alternative requiring a user decision was implemented.

## Exact ROM and source identity

- Frozen original [Draft PR #38](https://github.com/Odourman/mellanrum/pull/38): HEAD `6e9db179867234a19cce329c709170f2423ffbbb`, ROM SHA-256 `bfdeb5308dcecc526e802cd95886b94e0ce4953628e7bc7190c5d49231deac06`, unchanged.
- Separate [Draft PR #44](https://github.com/Odourman/mellanrum/pull/44), branch `romdev/issue43-s3-polarity-feasibility-20261124`.
- Product code commit **`eaa6b97f9313cb0c49f39b3f4d301da601df638d`**, pinned native ROM SHA-256 **`07970f492ca9c8aa2f0445b00ce6a046624176db6ebaa7917d7392b7f6b43c2c`**, Git blob **`ccc93afc6ecf93b4bc818c83f255d03d43e50e5f`**, **16,384-byte standard F6 NTSC**. This report and CI scoping changed only workflow/documentation, not the ROM.
- Bank0 `4f1fefc7513d5c0aef2d1c2a406b77975e59fc60e0a3361fa34455b4c669c49f`, bank1 `8d49d78a7f7ea98d1638693767de146b54b7b97673eb5f077fbf9c0554e3a1e8`, bank2 `6b82511ba23726be41aa5f7a4e8c2555f5e039ee6fc2ec6a1e0774117cfffbfc` are **identical to frozen PR38**; bank3 `d4061eda4a50ba9b18f925eb30f935dbd2599764ff53b881548961b1ae79e239` is the only changed bank.
- Original S3-A, S3-B, U3 three-wing sprites, all room geometry, gameplay/collision rules, audio score, title/coda, 118-byte RIOT variable layout intact. No added RAM/JSR or special hardware.

## Failed prototypes and final raster fix

- Prior E (`08ddf89a...`, ROM `12160ea...`) colored the exit's right-hand pixels red — **VISUAL FAIL** despite Stella/Gopher 15/15.
- Prior F (`b0849c6...`, ROM `953c725...`) retained separate colors but altered 4 non-stone HUD pixels in 2/116 baseline-aligned Stella screenshots — **PARITY FAIL**.
- Final G (`eaa6b97...`) sets `COLUP1` to stone's committed-polarity color after the next row's `WSYNC`, restores original amber before the second P1 GRP1, leaves it amber until exit's final pixel, and routes the last blank stem line through a separate short raster path. `$46` is visibly red in actual Stella, not an assumed untested hue. No additional JSR or variable.
- Native bank3 listing: regular `Stem13` (`$F912`–`$F93D`) **75/76 6507 CPU cycles including WSYNC**, pointer tables page-safe for used Y values; last blank-stem branch **28 cycles before subsequent bookkeeping**. Only **one-cycle normal-path margin**. **Global all-path/physical hardware timing remains INCONCLUSIVE**; sampled emulator PASS does not imply exhaustive proof.

## Actual native evidence — exactly new ROM SHA

| Evidence | Result | Link |
|---|---|---|
| Native DASM rebuild and exact byte-for-byte ROM pin after actual Stella replay | **PASS** | [Actions #45428317775](https://github.com/Odourman/mellanrum/actions/runs/45428317775) |
| Real Stella controller 15/15 rooms, title/coda, authentic TIA audio/FRI | **PASS** | [Actions #45426587119](https://github.com/Odourman/mellanrum/actions/runs/45426587119), artifact `14934339773` |
| Real Gopher2600 controller 15/15 rooms, coda/title | **PASS** | [Actions #45426587251](https://github.com/Odourman/mellanrum/actions/runs/45426587251), artifact `14938660470` |
| Gopher 262 NTSC lines | **278/278 sampled PASS** | same run |
| Eight separate actual Gopher per-instruction frame diagnostics for rooms II-02, II-04, III-02, III-05, polarities 0/1 | **8/8 complete 262 lines, 33,896 instructions, 0 skipped visible WSYNC** | original raw CPU traces in indexed local handoff |
| Eight 160×228 same-room Stella pairs (room controller-reached, polarity **forced with RAM POKE**, marked DIAGNOSTIC) | **18 stone pixels recolor, 0 exit pixels recolor in each room** | original PNGs in handoff |
| 116 exact matched controller-only original 1× Stella frames compared pixelwise with frozen PR38 | **46 frames intended stone changes, 788 stone pixels, 0 changed pixels outside stone** | source/JSON/PNG in handoff |
| Genuine controller-only polarities from accepted FIRE, echo recall, Presence | **PASS observed 19 before/after original-frame samples, no POKE** | same-SHA trace and PNGs in handoff |
| 15 independent room-specific genuine Stella idle 36,000-frame tests | **15/15 PASS, 0/15 passive wins** | [Actions #45428565608](https://github.com/Odourman/mellanrum/actions/runs/45428565608); 15 individual artifacts, new SHA checked |
| 15 controller-reached Stella critical FIRE omission tests | **15/15 PASS bounded to original win+360f** | same-SHA results/script in handoff |

The **complete 90-item ZIP** `MELLANRUM_ISSUE43_S3_ORANGE_RED_G07970_MAIN_III_FULL_EVIDENCE.zip` includes source snapshot/diff, old+new ROM with separate clear paths, authentic PNGs, 19 natural controller samples, raw Gopher CPU traces, 15 CI idle artifacts, 15 causal results, reproducible scripts, Stella/Gopher original artifacts, 89/89 validated SHA-256 manifest entries, ZIP CRC PASS. Provided to user in ROM DEVELOPMENT conversation. Do not invent a GitHub or Drive URL for the ZIP. Original individual evidence is available through linked GitHub Actions.

## CI failures separated from product behavior

Legacy `.github/workflows/game.yml` runs Issue15 **4KiB** `build_issue15.py` and requires `git diff --exit-code` for the old source overlay, which rejects the authorized 16KiB F6 change. Legacy `title-presence-stella.yml` attempts a 4KiB visual diagnostic variant and fails DASM `Origin Reverse-indexed` at `$FF90`. Both **historical FAIL remain visible** and were scoped to **SKIPPED** on this Issue43 branch; skipped is **not** PASS. The actual native 16KiB F6 jobs and Stella/Gopher game tests are PASS.

## Open gates

- Full exhaustive 76-cycle/scanline across *all* possible states, stack/fuzz/F6 hotspots, all-frame Gopher timing, physically measured Atari 2600 and RetroN77 **NOT_RUN/INCONCLUSIVE**. No extra JSR/RAM in this prototype, but original 5-deep JSR uses all 10 stack bytes, so tiny safety margin remains.
- Human first-time playability, subjective audio and artwork approval, PAL, independent fresh-SHA Verification and Pachinko **NOT_RUN**.
- Same-row polarity pairs forced RAM are **diagnostic**, not alternative human solutions. 15 causal omissions bounded, not comprehensive softlock-proof.

**Recommendation:** MAIN III may review the successful stone-only color behavior on this isolated Draft PR. Keep original PR38 and all earlier frozen work untouched. Before merge/release, require separate new-SHA independent Verification/Pachinko and human artistic/hardware approval. **No merge, no release, no unauthorized both-red compromise.**
