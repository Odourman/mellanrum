# Source ID Registry – Mellanrum

## Auktoritativa ingångar
| ID | Källa | Klass | Status |
|---|---|---|---|
| M-SRC-001 | https://github.com/Odourman/mellanrum | Versions-/implementationssanning | Aktiv |
| M-SRC-002 | https://drive.google.com/drive/folders/1rO3ZTTBgyZZhqOx1WCxevM6sE3CrvUcl | Förvaringsplats för designoriginal/handoffs | Skapad, original ännu ej importerade |
| M-SRC-003 | docs/DECISIONS.md | Beslutslogg | Aktiv |
| M-SRC-004 | docs/CURRENT_PROJECT_STATE.md | Aktuell statusnavigering | Aktiv |
| M-SRC-005 | docs/DESIGN_INTAKE.md | Överlämnings-/öppna frågor | Aktiv, ej designcanon |

## Referenser som INTE blir Mellanrums canon
| ID | Källa | Integritetsuppgift | Klass |
|---|---|---|---|
| M-REF-001 | Lokalt uppladdad ATARI_2600_AVHANDLING_2026-11-21.md | SHA-256 `7ed5600fc195f76840b73ee5c899556a72fafbbac108c63e7b14a079aff5ebbb` | Teknik- och metodöverföring från Let Me Out!, rådgivande |
| M-REF-002 | Lokalt uppladdad ATARI_2600_KUNSKAPSOVERFORING_2026-11-21.zip, 50 filer | SHA-256 `fce2ec3aa68797b7c8d152acd138b3481303ea9a233a6d39636cf422c4eab7ac` | Historisk teknik-/metodreferens, innehåller källprojektets föråldrade beslut |
| M-REF-003 | Föregående "Mellanrum: Skogen som lyssnar" V5 | SHA-256 **saknas**, ej inläst i repo | Designkälla väntar på kopia och granskning |
| M-REF-004 | Äldre "Mellanrum: Det som lyssnar" V3 | Version/filhash ej intagen | Historiskt koncept, ej automatiskt slutgiltigt |

Källfilens namn, titel eller senare datum räcker inte ensamt för att ge den högre auktoritet. Ändra alltid detta register när faktisk ny originalfil tas emot. En hash identifierar bytes, inte att innehållet är rätt eller slutligt.

## V5.1 mottagningskandidater, ej auktoriserad slutcanon

| ID | Källa | Integritet | Status |
|---|---|---|---|
| M-CAND-005 | Indexerad Library-text `MELLANRUM_V5_1_SKOGEN_SOM_LYSSNAR_KRITISKT_REVIDERAD_AVHANDLING.md` | 1 396 indexerade rader läsbara. Originalråbyte och SHA-256 inte tillgängliga via materialisering | READABLE_TEXT_ONLY / PROPOSED / REVIEWED_PROVISIONALLY |
| M-CAND-006 | Användaren hänvisar till V5.1-ZIP och `LAS_MIG_FORST.md` | Inte bifogat/åtkomligt för denna MAIN-överföring; inte validerat | WAITING_FOR_SOURCE |
| M-CAND-007 | `reference/engine.py`, `reference/solve.py`, `reference/check_rooms.py`, `reference/validate_traces.py`, `reference/abstract_solution_results.json` | Beskrivna i avhandlingen men varken hämtade eller körda | NOT_RUN / WAITING_FOR_SOURCE |

Använd aldrig slumpmässig liknämnd Drive-fil som ersättning för M-CAND-006. En Drive-sökning gav t.ex. `LAS_MIG_FORST.md` som handlar om **The Cabin**, alltså är den inte Mellanrums källa. Originalens byte och SHA måste verifieras när de finns.

## GRAPHICS slutöverlämning 2026-11-22

| ID | Källa | Kontrollerad åtkomst | Status |
|---|---|---|---|
| M-CAND-008 | Project/Library `MELLANRUM_GRAPHICS_V51_FINAL_TILL_MAIN_2026-11-22.zip` | Filpost och storlek 1 539 775 bytes identifierade; raw materialization misslyckades | GRAPHICS_REPORTED / ZIP_BYTES_NOT_VERIFIED_BY_MAIN |
| M-CAND-009 | Project/Library `00_GRAFIKAVHANDLING_FULLSTANDIG.pdf` | 34 sidor läsbara som indexerat dokument | VISUAL_DIRECTION_REVIEWED |
| M-CAND-010 | Project/Library `STARTTEXT_TILL_MAIN.txt` | Indexerad text läsbar | GRAPHICS_HANDOFF_READABLE |
| M-CAND-011 | Project/Library `MELLANRUM_V5_1_KRITISKT_REVIDERAT_TILL_MAIN_2026-11-22.zip` | Filpost och storlek 570 796 bytes identifierade; raw materialization misslyckades | ORIGINAL_MODEL_ZIP_NOT_REPRODUCED_BY_MAIN |

Slutleveransen anger 25 maskvärden men ett avsnitt anger 23; 20/20 Python och 15/15 rumslösningar är uppgifter från GRAPHICS, inte nya MAIN-test. Fullspelsorder: `docs/ROM_DEVELOPMENT_FULL_GAME_ORDER_2026-11-22.md`. Överlämningsgranskning: `docs/MAIN_GRAPHICS_V5_1_INTAKE_2026-11-22.md`. Registrera verkliga SHA från råpaketen när dessa kan läsas; hitta inte på hashvärden.

## Developer implementation and independent verification candidates, 2026-11-22

| ID | Source | Verified information | Status |
|---|---|---|---|
| M-CAND-012 | [PR #4](https://github.com/Odourman/mellanrum/pull/4), exact head 8bdecde79a6bc1ecb804484d5d257f4f1a99b052 | Open Draft, unmerged, 31 files changed; native source and 4 KiB ROM | IMPLEMENTATION_CANDIDATE |
| M-CAND-013 | [DASM / model CI run 45064977045](https://github.com/Odourman/mellanrum/actions/runs/45064977045) | SUCCESS, original native DASM artifact ID 14771180701; MAIN extracted ROM 4096 B and measured SHA256 ec791333da37613ec99ea70b2a983ecc1666b4e576211ece41a8e40bd14cbaed | BUILD_PASS / MAIN_ARTIFACT_HASH_MATCH |
| M-CAND-014 | [Stella smoke run 45064977006](https://github.com/Odourman/mellanrum/actions/runs/45064977006) | SUCCESS, artifact 14769984347, four original captured PNGs read by MAIN (320x228 title/gameplay) | STELLA_BOOT_SMOKE_PASS / NOT_FULL_GAMEPLAY |
| M-CAND-015 | [developer provenance](https://github.com/Odourman/mellanrum/blob/romdev/fullgame-20261122/docs/PROVENANCE.md) | GRAPHICS ZIP SHA b9ae037d7e29602dc44ea7401e6739ba3cd606e03a90375ebc23ad3b06d5e419; nested V5.1 SHA 7bb664dcd5a64e9dd8435aa83328827c72c345da5d9fb83b9d41bf70a34a3e5e, 116/116, 25 masks, 15 rooms | DEVELOPER_SOURCE_REPORTED; INDEPENDENT_PROVENANCE_NOT_RUN |
| M-CAND-016 | [Independent Verification handoff](https://github.com/Odourman/mellanrum/blob/main/docs/MAIN_TO_VERIFICATION_PR4_2026-11-22.md) | exact scope, source/ROM IDs, tests, stop criteria | READY_FOR_SEPARATE_VERIFICATION |

Historical M-CAND-005..011 describe MAIN's **earlier** source-limited intake; M-CAND-015 records later developer-supplied evidence without silently changing those historical claims.

## ROM V5.1 runtime candidate 2026-11-22

| ID | Källa | SHA/typ | Status |
|---|---|---|---|
| M-CAND-012 | [PR #4 immutable head](https://github.com/Odourman/mellanrum/tree/8bdecde79a6bc1ecb804484d5d257f4f1a99b052) | commit `8bdecde79a6bc1ecb804484d5d257f4f1a99b052` | DRAFT / DEVELOPER_BUILD_PASS |
| M-CAND-013 | [Native DASM build artifact](https://github.com/Odourman/mellanrum/actions/runs/45064977045) | 4096-byte ROM SHA256 `ec791333da37613ec99ea70b2a983ecc1666b4e576211ece41a8e40bd14cbaed` | BUILD_PASS, GAMEPLAY_NOT_FULLY_VERIFIED |
| M-CAND-014 | [Actual Stella boot snapshots](https://github.com/Odourman/mellanrum/actions/runs/45064977006) | four actual emulator PNG captures from same head | BOOT_SMOKE_PASS, NOT 15-room replay |
| M-CAND-015 | [PACHINKO independent diagnostics instructions](MAIN_TO_PACHINKO_STRESS_TEST_2026-11-22.md) | Issue #6; no result attached yet | DIAGNOSTIC_HANDOFF_READY |
| M-CAND-016 | [Independent verification brief](MAIN_TO_VERIFICATION_PR4_2026-11-22.md) | Issue #5 | VERIFICATION_PENDING |

## Pachinko diagnostic outputs – 2026-11-22

| ID | Källa | Hash eller identifierare | Status |
|---|---|---|---|
| M-CAND-017 | [User-uploaded Pachinko report](PACHINKO_STRESS_TEST_REPORT_2026-11-22.md) | Ursprunglig MD SHA256 `9d09d6358d54a3dbd08a3bd7114124772fd425b92e05019ab4ef250c509cf22a`; 2 400 modellkörningar och 150 ZIP-payload-poster **rapporterade** | USER_REPORT_RECEIVED; FULL_EVIDENCE_ZIP_NOT_PRESENT |
| M-CAND-018 | [Pachinko Stella workflow run 45069826844](https://github.com/Odourman/mellanrum/actions/runs/45069826844) | Diagnostic commit `e6e8f3047d2006418fee0e93a01fb918b7d6e186`; only added workflow vs frozen product | CI_SUCCESS / PRODUCT_CODE_UNCHANGED |
| M-CAND-019 | [Stella diagnostic artifact 14772668727](https://github.com/Odourman/mellanrum/actions/runs/45069826844/artifacts/14772668727) | Archive SHA256 `bc3e21cb2d981b257d9f9a9d28f0f99592ea56993102dc42d15da5d32c41437f`, 13 PNG (12 distinct), 52 logged taps, 15/15 manifest, ROM SHA verified | MAIN_CHECKED_STELLA_DIAGNOSTIC_ONLY |
| M-CAND-020 | [MAIN's Pachinko intake](MAIN_PACHINKO_INTAKE_2026-11-22.md) | Source classifications and independent test priorities | MAIN_REVIEW / NO_RELEASE_PASS |

Older registry entries `M-CAND-012..016` were duplicated in historical append-only sections; do not interpret repeated IDs as separate sources or assume highest repeated section changes provenance authority.

## User-authorized revisions and Pachinko 2.0 scope – 2026-11-22

| ID | Källa | Bindande identifierare | Status |
|---|---|---|---|
| M-SRC-006 | [ROM DEVELOPMENT scope: title and fleeting Presence](MAIN_TO_ROMDEV_TITLE_AND_PRESENCE_2026-11-22.md) | User-approved design delta, [Issue #8](https://github.com/Odourman/mellanrum/issues/8) | USER_APPROVED / IMPLEMENTATION_PENDING |
| M-SRC-007 | [PACHINKO 2.0 full test order](MAIN_TO_PACHINKO_2_0_FULL_COVERAGE_2026-11-22.md) | Planned tests for **next** immutable ROM SHA, [Issue #7](https://github.com/Odourman/mellanrum/issues/7) | TEST_INFRASTRUCTURE_AUTHORIZED / NOT_EXECUTED |
| M-REF-005 | [Prior diagnostic workflow](https://github.com/Odourman/mellanrum/blob/e6e8f3047d2006418fee0e93a01fb918b7d6e186/.github/workflows/pachinko-stella-diagnostic.yml) | Product baseline `8bdecde...`, 52 wall-clock taps, 13 Stella screenshots, dummy audio | HISTORICAL_STELLA_DIAGNOSTIC, NOT 15-ROOM/FRAME-EXACT/AUDIO |

No new ROM SHA is yet available. Do not use the old `ec791333...` ROM identity to assert new title/silhouette implementation. Gopher2600 and Stella APIs are tools to verify against installed versions rather than conjectural guarantees.

## Latest native candidate after title+Presence – 2026-11-22

| ID | Källa | Identifierare/evidens | Status |
|---|---|---|---|
| M-CAND-021 | [Draft PR #4 head](https://github.com/Odourman/mellanrum/commit/eea14339010306de635a8c6238e242b76b28cc64) | `eea14339010306de635a8c6238e242b76b28cc64`; source code `6f6319be31985ea9009b7c21988f2977f1509e46` | DEVELOPER_TITLE_PRESENCE_REVISION / NOT_MERGED |
| M-CAND-022 | [DASM native CI artifact 14773519887](https://github.com/Odourman/mellanrum/actions/runs/45072844664/artifacts/14773519887) | 4096-byte NTSC ROM, SHA256 `a9531d5bbbff033711fbe54f8688b8e0259640e0a9a284c8ab585eea415c0bd5`; MAIN bytes checked, ZIP CRC good | MAIN_ROM_HASH_CHECK_PASS / NOT_FULL_GAMEPLAY |
| M-CAND-023 | [Stella visual artifact 14774191179](https://github.com/Odourman/mellanrum/actions/runs/45073465951/artifacts/14774191179) | 193 ZIP entries; includes genuine product-ROM title captures and **instrumented variant** Presence captures III-03/04/05 | TITLE_REAL_STELLA_OBSERVED / PRESENCE_TEST_VARIANT_ONLY |
| M-CAND-024 | [MAIN Issue #8 intake](MAIN_ROMDEV_ISSUE8_INTAKE_2026-11-22.md) | Evidensgränser, developer SHA/visual acceptance, new AB dependency | MAIN_REVIEWED / PACHINKO_FINAL_PENDING |
| M-SRC-008 | [Main to ROM DEV A/B order](MAIN_TO_ROMDEV_AB_HARDWARE_ONLY_2026-11-22.md) | [Issue #9](https://github.com/Odourman/mellanrum/issues/9), source decision MEL-037 | IMPLEMENTATION_AUTHORIZED / NOT_YET_BUILT |

Previous `M-CAND-012..020` are historical and/or duplicated append-only IDs. Do not treat old SHA evidence as if it validates the later `a953...` ROM or future post-A/B changes.

| M-SRC-009 | [Post-Issue8 PACHINKO Stage0 and final SHA gate](MAIN_TO_PACHINKO_2_0_POST_ISSUE8_STAGE0_FINAL_GATE_2026-11-22.md) | Current 4K native developer visual SHA `a953...` only Stage0; full suite after A/B Issue #9 yields new SHA | AUTHORIZED_STAGE0_TEST_INFRASTRUCTURE / FINAL_TEST_WAITING_FOR_NEW_ROM |

## 2026-11-22 post-A/B current candidate / test orders

| ID | Källa | Immutable identifier / important evidence | Status |
|---|---|---|---|
| M-CAND-025 | [Draft PR #4 current A/B HEAD](https://github.com/Odourman/mellanrum/commit/49eb168b17d0254d06cf50d87c60e8fb6016db6e) | `49eb168b17d0254d06cf50d87c60e8fb6016db6e`; game code `6cb86247c668162b180e5d77377098941b9803b3` | CURRENT_FROZEN_DIAGNOSTIC_TARGET / DRAFT / NOT_MERGED |
| M-CAND-026 | [Native DASM Actions artifact 14775257125](https://github.com/Odourman/mellanrum/actions/runs/45075716636/artifacts/14775257125) | 4096-byte NTSC standard 4K, ROM SHA256 `e9ea87d381bcf8da39ec055d7d6951ceff97b21d3a798addd10fbbe540c5e974` independently checked by MAIN; ZIP CRC good | MAIN_NATIVE_ROM_HASH_PASS / NOT_RELEASE |
| M-CAND-027 | [Stella A/B real artifact 14774798060](https://github.com/Odourman/mellanrum/actions/runs/45075039996/artifacts/14774798060) | 12 original production-ROM PNG, wall-clock input log, same ROM exact hash, extracted ZIP CRC good | STELLA_AB_VISUAL_PASS / NOT_FRAME_EXACT / SWCHB_RAM_NOT_VERIFIED |
| M-CAND-028 | [MAIN final A/B intake](MAIN_FINAL_AB_ROM_INTAKE_2026-11-22.md) | exact SHA, status evidence and remaining gates | MAIN_INTAKE_PASS / FULL_SYSTEM_NOT_RUN |
| M-SRC-010 | [MAIN final Pachinko 2.0 order](MAIN_TO_PACHINKO_2_0_FINAL_AB_E9EA_FULL_TEST_2026-11-22.md) | applies **only** to `e9ea87d3...` A/B ROM + all 15 rooms, image, sound, TIA, stress; independent Verification separate | FULL_DIAGNOSTIC_EXECUTION_AUTHORIZED / NOT_RUN |

Pre-AB `a953...` and original `ec791...` remain historical checks and are NOT a substitute for testing M-CAND-025/026. Prior Stage0 `WAIT` gate is satisfied only by the frozen current developer identity; do not reuse current SHA for future modified game source.

## PACHINKO 2.0 verified interim evidence / MAIN audit – 2026-11-22

| ID | Källa | Identity / limits | Status |
|---|---|---|---|
| M-CAND-029 | [MAIN full original-artifact Pachinko interim audit](MAIN_PACHINKO_2_0_E9EA_INTERIM_INTAKE_2026-11-22.md) | exact frozen E9EA native ROM; 2 Gopher campaign + 3 Stella/libretro campaign; scanned native logs and manifests | PARTIAL_REAL_EMULATOR_EVIDENCE / NOT_RELEASE |
| M-CAND-030 | [Gopher Actions 45077617532](https://github.com/Odourman/mellanrum/actions/runs/45077617532) | real native HEADLESS two 11,548-frame complete 15-room paths, 166/166 RAM checkpoints each, artifacts 14776331457 / 14776331656 | REAL_CONTROLLERS_ROUTE_15x2_PASS / NO_FULL_MECHANICS_PASS |
| M-CAND-031 | [Gopher native raster artifact 14775931750](https://github.com/Odourman/mellanrum/actions/runs/45077617532/artifacts/14775931750) | two native `TV FRAME` transcripts report 261 lines 119/119 each, plus campaign mode/room/beat logs | Gopher_NATIVE_RASTER_FAIL / STELLA_CROSS_CHECK_NEEDED |
| M-CAND-032 | [Stella/libretro Actions 45078424709](https://github.com/Odourman/mellanrum/actions/runs/45078424709) | artifact 14776451289, 3×11,420-frame 15/15 automated full campaigns+coda, 86 first-run PNG, 189 SHA manifest rows matched; **no native scanline audit** | REAL_STELLA_ROUTE_PASS / RASTER_NOT_RUN |
| M-CAND-033 | [Gopher native TIA audio 45078436099](https://github.com/Odourman/mellanrum/actions/runs/45078436099) | artifact 14776068795, two nonzero genuine TIA WAV with quantitative summaries, no human listening approval | GENUINE_WAV_CAPTURE_PASS / HUMAN_AUDIO_NOT_RUN |
| M-SRC-011 | [ROM DEV cross-emulator scanline diagnosis Issue #12](https://github.com/Odourman/mellanrum/issues/12) | No production edits; reproduce 261 against known 262 controls and independent Stella true beam | DIAGNOSIS_ONLY_ORDER / NOT_IMPLEMENTATION |
