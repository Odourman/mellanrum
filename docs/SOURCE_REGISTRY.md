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
