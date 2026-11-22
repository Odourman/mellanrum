# Mellanrum: aktuellt projektläge

**Updated:** 2026-11-22 (MAIN independently inspected Issue #8 delivery; A/B separate order #9 now issued).
**Phase:** **TITLE+PRESENCE DEVELOPER CANDIDATE RECEIVED / HARDWARE A/B IMPLEMENTATION ORDER OPEN / PACHINKO 2.0 FINAL FREEZE PENDING**.
**Implementation:** Updated 15-room 4K NTSC product candidate exists on Draft PR #4, head `eea14339010306de635a8c6238e242b76b28cc64`; `main` contains coordination docs, not merged game. Native ROM SHA256 `a9531d5bbbff033711fbe54f8688b8e0259640e0a9a284c8ab585eea415c0bd5` (4096 bytes), verified from GitHub Actions by MAIN. **Further A/B-only UI/input change is ordered but not implemented; this SHA is not final for full Pachinko.**
**Release:** **NOT APPROVED**. Independent gameplay, visual, sound and hardware testing is not complete.

## Nästa auktoriserade designbeslut, uppskjutet ROM-arbete – A/B-konsolreglage

- **USER-APPROVED control design, NOT YET IMPLEMENTED:** vänstra fysiska Difficulty-reglaget används **exklusivt** för val av spelläge; **A = Kampanj (standard)** och **B = FRI SKOG**. Joystick och SELECT får inte byta spelläge; FIRE startar den hårdvaruvalda varianten, titelskärmen visar enbart `MELLANRUM`.
- **Mekanisk begränsning:** ROM kan läsa Difficulty A/B, men kan inte flytta det fysiska reglaget till A. "Standard Kampanj" betyder normalt läge när A är inställt; om användaren har reglaget på B aktiveras B vid nästa start. Under pågående spel ska A/B inte tvinga ett oavsiktligt lägesbyte.
- **WAIT:** användaren vill att ROM DEVELOPMENT först slutför befintlig Issue #8 (titel och Närvaro). MAIN ska ge ett separat nytt ändringsuppdrag efter leveransen och därefter uppdatera PACHINKO 2.0 till den resulterande SHA. Detta dokument ger ingen auktorisation att utöka pågående kodscope.

## Developer title + Presence delivery (Issue #8), MAIN intake

[MAIN technical/artistic intake](MAIN_ROMDEV_ISSUE8_INTAKE_2026-11-22.md) · [Developer original matrix at exact commit](https://github.com/Odourman/mellanrum/blob/eea14339010306de635a8c6238e242b76b28cc64/docs/ISSUE8_TEST_MATRIX_2026-11-22.md) · [Stella Actions](https://github.com/Odourman/mellanrum/actions/runs/45073465951).

- PR #4 is Draft/open/unmerged at `eea14339010306de635a8c6238e242b76b28cc64`. Main downloaded native DASM developer artifact `14773519887`; archive CRC verified, ROM 4096 bytes, SHA256 `a9531d5bbbff033711fbe54f8688b8e0259640e0a9a284c8ab585eea415c0bd5`. Intermediate `d1005a...` and old `ec791...` are superseded product candidates, never retarget old Pachinko runs.
- Main downloaded actual Stella evidence artifact `14774191179`; title now reads exactly **MELLANRUM** on one line, with nonverbal mode icons. Geometric partial Presence is visibly rendered in III-03/04/05 through **instrumented Reset-only test-variant ROMs** (not native 15-room production ROM route). No physics changed reported by ROMDEV; MAIN has not independently audited all source/oracle.
- Actual emulator playthrough 15/15, full beam cycles, audible review, PAL, hardware and independent Verification remain NOT_RUN/PENDING. Issue #8 implementation developer reception **is not** independent release approval.
- **New post-#8 order** [hardware A/B issue #9](https://github.com/Odourman/mellanrum/issues/9): LEFT Difficulty A=Campaign (recommended normal), B=FRI SKOG; only console physical A/B selects; joystick and SELECT must not change mode, FIRE starts switch selection. The previous text-free **selectable icons must no longer form a navigable menu**. Read the hardware SWCHB bit 6, preserve running mode while A/B toggles; mechanical default A cannot be software-forced. [Full directive](MAIN_TO_ROMDEV_AB_HARDWARE_ONLY_2026-11-22.md).
- **PACHINKO 2.0** diagnostic infrastructure may start now; full-game final system stress must freeze **the next immutable A/B ROM SHA after #9**, and independent Verification must use the same next SHA. No release/PR merge authorization given.

## Nya användarbeslut: titel, Närvaron och fullständig Pachinko 2.0-testning (2026-11-22)

- ROM DEVELOPMENT har **uttrycklig ny implementationsauktorisation** för att titeln ska visa exakt ett läsbart ord **MELLANRUM**, utan andra textord (men med valbar kampanj/FRI SKOG), och för att Närvaron ska skymtas tillfälligt som en **ofullständig oidentifierbar silhuett av negativt rum mellan träden**. Ingen traditionell monstersprite, egen AI, collision eller ändrad V5.1-tidsregel. [ROM order](MAIN_TO_ROMDEV_TITLE_AND_PRESENCE_2026-11-22.md) · [Issue #8](https://github.com/Odourman/mellanrum/issues/8).
- PACHINKO 2.0 ska **bygga och köra GitHub Actions-driven komplett diagnostisk matris** för nästa verkliga ROM-SHA: verifierbart **frame-indexerad joystickreplay** (inte bara `xdotool sleep`), alla 15 rum i riktig emulator, grafik/TIA, riktiga WAV-filer och ljudanalyser, långkörning, slump-/edge-case-populationer, rapporter och reproducerbara SHA-bundna artefakter. [Full testorder](MAIN_TO_PACHINKO_2_0_FULL_COVERAGE_2026-11-22.md) · [Issue #7](https://github.com/Odourman/mellanrum/issues/7).
- **Föregående Pachinko** hade 2 400 rapporterade modellkörningar och en verklig [Stella Actions-run](https://github.com/Odourman/mellanrum/actions/runs/45069826844), som installerade DASM/Stella/Xvfb/xdotool, körde 52 grovtidsstyrda knappar, fångade 13 PNG, men använde `SDL_AUDIODRIVER=dummy` och gjorde inte fullspel eller exakt frame-replay. Därför var det `PARTIAL_WITH_EVIDENCE`, inte en misslyckad åtgärd eller release-PASS.
- **Viktigt tidsberoende:** PR #4 står ännu på gammal produkt-SHA `8bdecde79a6bc1ecb804484d5d257f4f1a99b052` och har inte mergats. Inga av nya användarändringar eller ny fullsystemsuite är utförda. Efter kodändring får utvecklaren ett **nytt** ROM-hash och Pachinko/Verification måste testa den nya kandidaten. Alla tidigare gröna tester gäller endast äldre ROM-bytes.
- **Grenser:** PACHINKO får skriva testinfrastruktur och GitHub Actions-workflows i isolerad diagnostikgren, men inte produktionskoden eller oberoende slutbedömning. GitHub Actions kan kontrollera vågformsdata och automatiska pixel/cykelmått; mänsklig upplevelse och ljudlyssning kräver faktisk granskare och får inte bedömas automatiskt från CI.

## What was actually checked by MAIN

- [PR #4](https://github.com/Odourman/mellanrum/pull/4): 31 changed files, entire V5.1 game logic candidate, original game maps/data, 6507 assembler, tests, CI workflows, reports.
- [Current-head native DASM CI](https://github.com/Odourman/mellanrum/actions/runs/45064977045): `SUCCESS` at exact head. Job logs show 4096-byte ROM, native DASM byte equality to independent developer subset assembler, V5.1 Python tests 20/20 and ROM-model comparisons 15/15 plus 225 random runs / 4352 ticks and developer raster checks.
- **MAIN independently downloaded and hashed the native Actions ROM bytes**: SHA-256 `ec791333da37613ec99ea70b2a983ecc1666b4e576211ece41a8e40bd14cbaed`; size 4,096; reset vector `$F000`; Stella reported NTSC / 4K.
- [Current-head Stella boot smoke](https://github.com/Odourman/mellanrum/actions/runs/45064977006): `SUCCESS`; extracted and examined four nonblank 320×228 original Stella PNG captures of title and gameplay. This supports a genuine Stella boot/title/snapshot smoke only; **not gameplay verification of all rooms or pixel/raster/sound fidelity**.
- Development source integrity (GRAPHICS 116/116 manifest, 25 8×8 mask records, 15 original rooms, 20/20 Python, 15/15 original room solutions) is documented in [developer source provenance](https://github.com/Odourman/mellanrum/blob/romdev/fullgame-20261122/docs/PROVENANCE.md). That original ZIP validation was **performed by ROM DEVELOPMENT and reported to MAIN**, not independently repeated by MAIN.

## PACHINKO stress test received – 2026-11-22

[Full Pachinko report](PACHINKO_STRESS_TEST_REPORT_2026-11-22.md) · [MAIN's measured intake and caveats](MAIN_PACHINKO_INTAKE_2026-11-22.md) · [diagnostic issue #6](https://github.com/Odourman/mellanrum/issues/6).

**Reported by PACHINKO:** 2,400 source-guided model runs / 69,747 completed owl ticks / 36,067 observed states / 44,438 transitions; zero modeled ROM/reference mismatches; 152 adversarial modeled cases; 17,600 short modeled frames plus 19,080 long FRI SKOG frames; no newly confirmed product defect. The full 150-entry result ZIP with 149 payload hashes is **not present in MAIN** and those totals are *not* a new MAIN independent reproduction.

**MAIN checked directly:** [Stella diagnostic workflow 45069826844](https://github.com/Odourman/mellanrum/actions/runs/45069826844) is `SUCCESS`, diagnostic commit `e6e8f3047d2006418fee0e93a01fb918b7d6e186`; compare with frozen product `8bdecde...` changed **only one workflow file**. Downloaded artifact `14772668727`, SHA `bc3e21cb2d981b257d9f9a9d28f0f99592ea56993102dc42d15da5d32c41437f`: exactly 4 KiB ROM with expected hash `ec791333da37613ec99ea70b2a983ecc1666b4e576211ece41a8e40bd14cbaed`, 13 original PNG / 12 distinct, 52 logged taps, 15/15 artifact SHA manifest entries, ZIP CRC valid. This is genuine but **coarsely timed** Stella observation, not 15 real joystick wins, TIA timing certification or subjective audio.

**Disposition:** `DIAGNOSTIC_PARTIAL_WITH_EVIDENCE`; `NO_NEW_CONFIRMED_BUG_WITHIN_EXECUTED_SCOPE`; `INDEPENDENT_VERIFICATION_PENDING`. Keep PR #4 Draft/open; no merge/release. Verification Issue #5 has been updated with these findings. Artistically intended single-tree coda and full graphical fidelity still require their own review.

## MAIN verdict / next action

**Accepted for independent Verification only.** Request is recorded in [Issue #5](https://github.com/Odourman/mellanrum/issues/5), with [exact scope and acceptance matrix](MAIN_TO_VERIFICATION_PR4_2026-11-22.md). The [development issue #2](https://github.com/Odourman/mellanrum/issues/2) and [PR #4](https://github.com/Odourman/mellanrum/pull/4) remain open as applicable.

Verification should use immutable commit and ROM SHA, rebuild DASM cleanly, replay all 15 rooms using actual frame-level joystick input in a real Atari emulator, check input/echo/phase/Presence, TIA registers and long-run 262-line budget, watch title/intermediate/coda assets and both audio channels. PAL and real hardware are `NOT_IMPLEMENTED/NOT_RUN` unless independently tested.

## Deliberate developer design divergences that require review

- 4 KiB standard cartridge versus original 16 KiB F6 *provisional technical hypothesis*.
- Simplified mirrored abbreviated title, coda still uses ordinary forest rather than planned single-tree reduction, omitted optional Presence local PF seam and M1 chisel, reduced animation and transitions, FRI SKOG uses four source Act III geometries.
- These do not automatically invalidate model behavior but **must not silently be called full GRAPHICS visual conformance**. Evaluate with GRAPHICS/user if important.

## Authority and historical decisions

Project identity: [GitHub](https://github.com/Odourman/mellanrum) and [Drive folder](https://drive.google.com/drive/folders/1rO3ZTTBgyZZhqOx1WCxevM6sE3CrvUcl). User's full-game authorization was passed to ROM DEVELOPMENT in [full-game order](ROM_DEVELOPMENT_FULL_GAME_ORDER_2026-11-22.md). GAMEPLAN baseline V5.1 and `GITTERSKOG / BILDMELLANRUM` visual direction are implementation targets. Historic G0 source access limitations are documented in [V5.1 review](MAIN_V5_1_REVIEW_2026-11-22.md) and [Graphics intake](MAIN_GRAPHICS_V5_1_INTAKE_2026-11-22.md); the later developer's own source-validation does not make MAIN's earlier claims of inability false.

**Evidence status:** `DASM_BUILD_PASS`, `MAIN_ROM_HASH_MATCH`, `DEVELOPER_MODEL_PASS`, `PACHINKO_REPORTED_MODEL_PARITY_PASS`, `PACHINKO_STELLA_DIAGNOSTIC_ARTIFACT_CHECKED`, `PACHINKO_PARTIAL_WITH_EVIDENCE`, `FULL_REAL_EMULATOR_GAMEPLAY_NOT_RUN`, `AUDIO_LISTEN_NOT_RUN`, `HARDWARE_NOT_RUN`, `PAL_NOT_IMPLEMENTED`, `INDEPENDENT_VERIFICATION_NOT_RUN`. Main has not merged or released any ROM.
