# Beslutsregister – Mellanrum

Endast uttryckliga designägarbeslut ändrar canon. Registrera varje ändring med datum, källa, omfattning, status och `supersedes`. Tekniskt förslag är inte godkänd regel.

| ID | Datum | Beslut eller fråga | Status | Källa / avgränsning |
|---|---|---|---|---|
| MEL-001 | 2026-11-22 | Spelets namn är "Mellanrum" | APPROVED | Användarens projektstart |
| MEL-002 | 2026-11-22 | Nytt fristående Atari 2600-projekt | APPROVED | Användarens projektstart och projektkontext |
| MEL-003 | 2026-11-22 | GitHub `Odourman/mellanrum` är projektets repository | APPROVED | Användarens URL |
| MEL-004 | 2026-11-22 | Skapa en projektmapp i Google Drive | APPROVED | Användarens begäran |
| MEL-005 | 2026-11-22 | Använd GitHub Actions i arbetsflödet | APPROVED | Användarens begäran; CI-resultat är inte självständig ROM-verifiering |
| MEL-006 | 2026-11-22 | MAIN ansvarar för samordning, status och uppdrag | APPROVED_FOR_PROJECT_SETUP | Användarens uttryckliga fråga om MAIN-roll |
| MEL-007 | 2026-11-22 | V5 med skog/barrträd, uggla och sten som senast diskuterat designförslag | PROPOSED_SOURCE_INTAKE | Kräv faktisk V5-källfil och versionsgranskning före fastställd canon |
| MEL-008 | 2026-11-22 | Oidentifierbar hotfull närvaro som nytt speldesignlager | OPEN | Användaren bad om konstnärlig värdering; inte automatiskt implementerad |
| MEL-009 | 2026-11-22 | 16 KiB F6/NTSC som första tekniska profil | WORKING_ASSUMPTION | Kandidat från design/research, måste godkännas mot spelspecifikation |
| MEL-010 | 2026-11-22 | Auktorisation att börja gameplay-ROM | NOT_AUTHORIZED | Kräver särskilt uppdrag efter designintag |

**Ingen av MEL-007 till MEL-010 får beskrivas som slutligt godkänd bara för att de står i registret.**

Vid ett nytt beslut: skriv `MEL-011` osv. Ändra inte historiska rader i tysthet; ange datum, källhänvisning och exakt ersatt regel.

## Nya granskningstransaktioner: 2026-11-22 (V5.1)

| ID | Datum | Beslut eller fråga | Status | Källa / avgränsning |
|---|---|---|---|---|
| MEL-011 | 2026-11-22 | V5.1 ersätter V5 som **föreslagen designbas för granskning** | PROPOSED_SUPERSESSION | Användarens V5.1-handoff; V5.1-paketets ZIP och `LAS_MIG_FORST.md` ännu ej åtkomliga |
| MEL-012 | 2026-11-22 | Närvaron i III-03 till III-05: varning, två aktiva tick, FIRE-kapning och en autonom stenvändning | PROPOSED_IN_V5_1 | V5.1-kritisk avhandling, §10 och inledande revision; MEL-008 kvarstår historiskt OPEN tills accept |
| MEL-013 | 2026-11-22 | Materialalfabetet exakt barrträd, uggla, sten; ingen fjärde kroppslig fiende | PROPOSED_IN_V5_1 | V5.1 kap. 1–3, 15A |
| MEL-014 | 2026-11-22 | Tre akter, 15 rum, spegling/eko/fas och ljud som konstnärlig mekanik utan musikspel | PROPOSED_IN_V5_1 | V5.1 kap. 5, 10–21, 62–65 |
| MEL-015 | 2026-11-22 | MAIN:s V5.1-granskning är preliminärt **positiv men INTE accept** | REVIEWED_WITH_OPEN_GAPS | `docs/MAIN_V5_1_REVIEW_2026-11-22.md`, ofullständigt källa/ZIP-intag |
| MEL-016 | 2026-11-22 | ROM-implementation förblir spärrad i detta uppdrag | NOT_AUTHORIZED | Uttrycklig användarinstruktion; MEL-010 oförändrat |

**Viktigt:** V5.1 kan vara bättre än V5 och ändå sakna formell projektacceptans. Det gamla versionsförslaget är inte automatiskt raderat; besluten gäller endast det nämnda granskningsskedet. Själva grafiken, Python-källorna, testerna, manifestet och händelseordningen kan inte slutgranskas före det faktiska ZIP-intaget.

## Produktionsinriktning efter GRAPHICS-överlämning, 2026-11-22

| ID | Datum | Beslut eller fråga | Status | Källa / avgränsning |
|---|---|---|---|---|
| MEL-017 | 2026-11-22 | Efter att MAIN mottagit och granskat GRAPHICS-underlaget ska MAIN utfärda **en sammanhållen fullspelsorder** till ROM DEVELOPMENT, i stället för många separata implementeringsauktorisationer | USER_DIRECTED / FUTURE_CONDITIONAL | Användarens uttryckliga uppdrag 2026-11-22. Ingen sådan order skickad ännu |
| MEL-018 | 2026-11-22 | ROM DEVELOPMENT ska få stort handlingsutrymme att improvisera kreativa och tekniska lösningar, utan att stanna för varje icke-kritisk osäkerhet | USER_DIRECTED / FOR_FUTURE_ORDER | Gäller inom målet att göra ett färdigt spel; bevara uttryckliga grundkrav och redovisa avvikelser |
| MEL-019 | 2026-11-22 | Ett enda produktionsmandat innebär inte falska PASS eller att utvecklaren blir sin egen oberoende verifierare | PROCESS_BOUNDARY | ROM DEVELOPMENT ska själv testa och dokumentera; separat VERIFICATION bedömer dess resultat |

**Tolkning av tidigare MEL-010/MEL-016:** de historiska raderna gällde avsaknad av dåtidens ROM-startorder. Användaren har nu beslutat om en *framtida*, villkorad **fullproduktionsorder** efter GRAPHICS-intag. Ingen implementation har påbörjats i detta MAIN-steg och ingen faktisk ROM-order har ännu skickats. I den framtida prompten är däremot hela spelet i scope, utan behov av MAIN-mikrotillstånd mellan interna arbetsfaser.

## GRAPHICS-handoff och fullspelsorder, 2026-11-22

| ID | Datum | Beslut eller fråga | Status | Källa / avgränsning |
|---|---|---|---|---|
| MEL-020 | 2026-11-22 | GRAPHICS V5.1 huvudriktning `GITTERSKOG / BILDMELLANRUM` mottagen och accepterad som visuellt produktionsmål | VISUAL_DIRECTION_ACCEPTED_FOR_IMPLEMENTATION | Användarens GRAPHICS-handoff, MAIN:s granskning av 34-sidig avhandling; ZIP-data ännu inte egen bytevalidering |
| MEL-021 | 2026-11-22 | 25 masker, 15 rum, 48 HUD-kombinationer, 20/20 tester och 15/15 rumslösningar är ännu endast rapporterade av GRAPHICS | GRAPHICS_REPORTED / MAIN_NOT_REPRODUCED | `docs/MAIN_GRAPHICS_V5_1_INTAKE_2026-11-22.md`; avhandlingens avsnitt M nämner även 23 genererade masker |
| MEL-022 | 2026-11-22 | Användarens uttryckliga kommande enda fullproduktionsuppdrag är nu formulerat och publicerat till ROM DEVELOPMENT | FULL_GAME_ORDER_READY_FOR_HANDOFF | `docs/ROM_DEVELOPMENT_FULL_GAME_ORDER_2026-11-22.md`. Ingen kodexekvering eller ROM-produktion startad av MAIN |
| MEL-023 | 2026-11-22 | Independent Verification förblir separat från ROM DEVELOPMENT:s utvecklartester | PROCESS_BOUNDARY_CONFIRMED | Användarens instruktion och GRAPHICS V5.1-handoff |

**Tolkning:** Ett publicerat uppdragsdokument ger ROM DEVELOPMENT ett användarauktoriserat sammanhållet mandat **när uppdraget överlämnas**, utan efterföljande mikrogates. Det innebär inte att MAIN har utfört utveckling eller att källa/grafikpaket är bytevaliderade.

## ROM DEVELOPMENT PR #4 handoff / independent verification gate, 2026-11-22

| ID | Datum | Beslut eller fråga | Status | Källa / avgränsning |
|---|---|---|---|---|
| MEL-024 | 2026-11-22 | Full-game candidate accepted **for independent verification only**: Draft PR #4, exact head `8bdecde79a6bc1ecb804484d5d257f4f1a99b052` | CANDIDATE_REVIEWED / NOT_MERGED | User's ROM DEVELOPMENT handoff; MAIN inspected PR and CI logs |
| MEL-025 | 2026-11-22 | Real native DASM builds 4,096 B standard NTSC 4K ROM; SHA-256 `ec791333da37613ec99ea70b2a983ecc1666b4e576211ece41a8e40bd14cbaed` independently matched against downloaded current-head CI artifact | BUILD_PASS / MAIN_HASH_MATCH | CI run `45064977045`; no independent gameplay implied |
| MEL-026 | 2026-11-22 | Stella boot smoke at exact PR head has four nonblank captured PNGs of title/gameplay; full 15-room real emulator run not established | STELLA_BOOT_SMOKE_PASS / GAMEPLAY_NOT_RUN | CI run `45064977006`, artifact `14769984347`, MAIN directly inspected images |
| MEL-027 | 2026-11-22 | Independent Verification required before merge or release; scope documented in Issue #5 and Verification handoff | VERIFICATION_PENDING / RELEASE_BLOCKED | `docs/MAIN_TO_VERIFICATION_PR4_2026-11-22.md`; no independent PASS yet |
| MEL-028 | 2026-11-22 | Simplified mirrored title and coda, omitted optional PF Presence seam/M1 mark and reduced animation explicitly require artistic conformance review | OPEN_ART_CONFORMANCE | Developer report; these deviations not necessarily full-graphics-accept |

Historical ROM_NOT_AUTHORIZED entries referred to work **before** the later full-game order. That later user authorization was actually exercised by ROM DEVELOPMENT; the current gate concerns independent validation and release, **not a need for another implementation micro-authorization**.
