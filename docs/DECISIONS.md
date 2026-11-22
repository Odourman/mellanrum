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

## ROM-kandidat, Pachinko och verifikationsgräns – 2026-11-22

| ID | Datum | Beslut eller fråga | Status | Källa / avgränsning |
|---|---|---|---|---|
| MEL-024 | 2026-11-22 | ROM DEVELOPMENT har överlämnat 4K NTSC-kandidat, PR #4 head `8bdecde`, SHA `ec791333da37613ec99ea70b2a983ecc1666b4e576211ece41a8e40bd14cbaed` | DEVELOPER_BUILD_PASS / DRAFT_PR | Verifierat i GitHub Actions run 45064977045, ej release eller merge |
| MEL-025 | 2026-11-22 | Stella boot/screenshot smoke för samma head, fyra bilder, är godkänt endast som uppstartsevidens | STELLA_BOOT_SMOKE_PASS / FULL_GAMEPLAY_NOT_RUN | Run 45064977006 och fyra arkiverade PNG; ingen 15-rums manual replay |
| MEL-026 | 2026-11-22 | MAIN utfärdar separat Pachinko-diagnostiskt stresstestuppdrag för oförändrad PR #4-kandidat | HANDOFF_READY / NOT_RUN | `docs/MAIN_TO_PACHINKO_STRESS_TEST_2026-11-22.md`, Issue #6; user begär 'be nu Pachinko chatten' |
| MEL-027 | 2026-11-22 | Pachinko genomför bred flödes-/edge-case-stress, men fattar inga independent Verification- eller releasebeslut | SEPARATE_DIAGNOSTIC_ROLE | Användarens inriktning, Issue #6; independent Verification Issue #5 |

**Historisk korrigering:** de första FAIL-körningarna (t.ex. `bb700a8`, run 45064295977, bytejämförelse vid byte 2911) är äldre än nuvarande lyckade `8bdecde`-CI. De får inte felaktigt förvandlas till nuvarande FAIL eller döljas ur historiken.

## PACHINKO rapport mottagen – 2026-11-22

| ID | Datum | Beslut eller fråga | Status | Källa / avgränsning |
|---|---|---|---|---|
| MEL-029 | 2026-11-22 | PACHINKO har avslutat en omfattande diagnostisk delkampanj mot oförändrad PR #4 SHA `8bdecde...`: rapporterade 2 400 modellexekveringar / 69 747 tick / noll ROM–modell-avvikelser / 152 adversariella fall | PACHINKO_DIAGNOSTIC_PARTIAL_WITH_EVIDENCE | [Pachinko report](PACHINKO_STRESS_TEST_REPORT_2026-11-22.md); fulla 150-posters bevis-ZIP finns inte hos MAIN, därför inte MAIN_REPRODUCED |
| MEL-030 | 2026-11-22 | GitHub diagnostic Stella-körning 45069826844 på diagnostik-HEAD `e6e8f304...` SUCCESS; diff mot produkt bara en workflow, MAIN verifierade 13 PNG, 52 taps, SHA och manifest för faktiska artifact 14772668727 | STELLA_DIAGNOSTIC_OBSERVED / NOT_FULL_GAMEPLAY | [MAIN Pachinko intake](MAIN_PACHINKO_INTAKE_2026-11-22.md), ROM hash `ec791333da37613ec99ea70b2a983ecc1666b4e576211ece41a8e40bd14cbaed` |
| MEL-031 | 2026-11-22 | PACHINKO:s 0 nya verifierade fel innebär **inte** release-godkännande; prioritera oberoende full 15-rums Stella-/joystickreplay, TIA-raster, ljud, originalarkivets bevis, grafik och coda | RELEASE_BLOCKED / INDEPENDENT_VERIFICATION_PENDING | [Independent Verification Issue #5](https://github.com/Odourman/mellanrum/issues/5), PR #4 fortsatt Draft/open |

**Historik:** MEL-024..MEL-027 förekommer två gånger i äldre avsnitt med närliggande betydelser. Dessa rader ska renummereras i en separat arkivstädning, inte tolkas som självständiga nya auktoritetsbeslut. Ingen historisk källa eller status skrivs över i tysthet.

## User-authorized title, Presence silhouette and Pachinko 2.0 – 2026-11-22

| ID | Datum | Beslut eller fråga | Status | Källa / avgränsning |
|---|---|---|---|---|
| MEL-032 | 2026-11-22 | Titelskärmen får ha **endast ordet `MELLANRUM`** som text, helt och läsbart; bibehåll val av kampanj/FRI SKOG utan ytterligare skrivna ord | DESIGN_APPROVED / ROM_CHANGE_AUTHORIZED / NOT_IMPLEMENTED | Användaren har uttryckligen bekräftat titeländringen. [ROM DEVELOPMENT Issue #8](https://github.com/Odourman/mellanrum/issues/8); ersätter aktuell MEL/LAN/RUM + KAM/FRI-avvikelse i MEL-028 när implementation lyckats |
| MEL-033 | 2026-11-22 | Närvaron får en **sällsynt, oidentifierbar, ofullständig silhuett av negativt utrymme mellan barrträden** under sina redan fastställda varnings-/intrångsfönster. Måste faktiskt kunna skymtas i emulatorn, inte bara margin-HUD. Ingen separat fiende eller regeländring | DESIGN_APPROVED / ROM_CHANGE_AUTHORIZED / NOT_IMPLEMENTED | Användaren: "Det låter bra. Kör på det och låt Rom development göra det." [Scope](MAIN_TO_ROMDEV_TITLE_AND_PRESENCE_2026-11-22.md). Preciserar V5.1 visuell fallback; ersätter inte de tre materiella motiven eller Närvarons FIRE-timing |
| MEL-034 | 2026-11-22 | PACHINKO ska utveckla verklig **GitHub Actions-driven allsystemsdiagnostik**: frame-indexerad joystick, 15 verkliga rum, faktisk TIA-grafik/scanlines, WAV-ljud, slump-/extremstress, tillståndsgrafer och reproducibla artefakter | TEST_MANDATE_APPROVED / NOT_EXECUTED | [PACHINKO 2.0 order](MAIN_TO_PACHINKO_2_0_FULL_COVERAGE_2026-11-22.md), [Issue #7](https://github.com/Odourman/mellanrum/issues/7); "ALLT" gäller kontrollerbar testmatris, inte matematiskt oändliga möjliga inputs |
| MEL-035 | 2026-11-22 | Gammal PR #4-ROM SHA `ec791...` är fryst historisk baslinje. **Efter ROM DEVELOPMENT:s nya commit/ROM-SHA måste tester och oberoende verifiering återköras på den nya identiteten** | VERSION_BOUNDARY / NO_CARRYOVER_PASS | Ny source-/build-/emulatorkontroll efter reviderad titel/Närvaro, ingen automatisk release |
| MEL-036 | 2026-11-22 | PACHINKO kör diagnostiska tester även i GitHub Actions men utfärdar aldrig Independent Verification- eller release-PASS. Faktisk audiolyssning, estetisk bedömning och eventuell fysisk hårdvara kan inte antas PASS bara för att CI är grön | PROCESS_BOUNDARY_RECONFIRMED | Independent Verification [Issue #5](https://github.com/Odourman/mellanrum/issues/5), ny testmatris |

**Supersession exakt:** MEL-032 ersätter behovet av att godkänna developer-designens gamla segmenterade text; MEL-033 gör tidigare valfri lokala PF-silhuett till ett nytt synligt genomförandekrav, men upphäver inte förbudet mot traditionell monsterkropp, extra materiellt motiv eller ny hot-AI. Dessa är beslut **från användaren**, inte verifierad implementation. Tidigare rapporter för `8bdecde...` gäller tills vidare endast gamla ROM-bytes.

## Framtida kontrollprofil för A/B Difficulty – användarbeslut 2026-11-22

| ID | Datum | Beslut eller fråga | Status | Källa / avgränsning |
|---|---|---|---|---|
| MEL-037 | 2026-11-22 | **Enda valmetod för spelläge är konsolens fysiska vänstra Difficulty A/B-reglage** (eller dess motsvarande hårdvaruknapp på RetroN 77). **A = standard/Kampanj** (15 rum), **B = FRI SKOG**. **Joysticken ska aldrig användas för att välja eller växla spelläge**; SELECT ska inte heller växla spelläge. FIRE startar det läge som konsolens A/B-reglage anger. Normalt rekommenderad uppstart: A = Kampanj. Inga lägesnamn eller menytext ska synas på titelskärmen, som endast visar `MELLANRUM`. | USER_DESIGN_APPROVED / **DEFERRED_IMPLEMENTATION_NOT_AUTHORIZED_YET** | Användaren instruerade att **vänta tills ROM DEVELOPMENT avslutat nuvarande titel/Närvaro-uppdrag** innan nytt implementationsuppdrag. Teknisk implementerbarhet och knappmappning ska därefter kontrolleras med riktig Atari 2600/RetroN 77/Stella. Mekanisk A/B-position kan inte ställas om av ROM:en; om reglaget fysiskt står på B vid start är B valt. |

**Giltighet och vänteläge:** Detta är en beslutad framtida användarkontroll, inte instruktion att avbryta eller expandera pågående ROM DEVELOPMENT Issue #8. MAIN ger en separat implementation order **efter att användaren skickat nuvarande ROM-leverans**. Den nya A/B-funktionen måste därefter testas i riktig emulator och RetroN 77-kartläggningen. Eventuella gamla textval (KAM/FRI) och SELECT-menylogik försvinner först när den nya implementeringen är verifierad, inte genom detta dokumentbeslut.

## Issue #8 handoff verified and post-Issue #9 assigned – 2026-11-22

| ID | Datum | Beslut eller fråga | Status | Källa / avgränsning |
|---|---|---|---|---|
| MEL-038 | 2026-11-22 | ROM DEVELOPMENT levererade uppdaterad horisontell titel MELLANRUM och en rent visuell, ofullständig Närvaro; MAIN hämtade native DASM ROM från CI och fick 4 096 bytes, SHA `a9531d5bbbff033711fbe54f8688b8e0259640e0a9a284c8ab585eea415c0bd5`. Stella-bilder visar titel i produkt-ROM och silhuett i **separata instrumenterade testvarianter** | DEV_IMPLEMENTATION_RECEIVED / NATIVE_HASH_VERIFIED / REAL_STELLA_VISUAL_OBSERVED / NOT_RELEASE | [MAIN intake](MAIN_ROMDEV_ISSUE8_INTAKE_2026-11-22.md), [CI run 45073465951](https://github.com/Odourman/mellanrum/actions/runs/45073465951), Draft PR #4 HEAD `eea143...`; ej full 15-rums joystickreplay |
| MEL-039 | 2026-11-22 | Nu när Issue #8 har levererats genomförs MEL-037 som **ett separat auktoriserat ROM DEVELOPMENT-uppdrag**: vänster fysisk Difficulty A/B för lägen, ingen joystick/SELECT-meny | IMPLEMENTATION_ORDERED / NOT_YET_IMPLEMENTED | [Order](MAIN_TO_ROMDEV_AB_HARDWARE_ONLY_2026-11-22.md), [Issue #9](https://github.com/Odourman/mellanrum/issues/9). Ny ROM-SHA ska sedan styra Pachinko 2.0 och independent Verification. Ingen merge/release |

**Observera:** MEL-032/033:s nya titel- och Närvarokrav är implementerade enligt utvecklaren och delvis synliga i MAIN-kontrollerade Stella-bilder. MEL-037 A/B är fortfarande **inte** implementerat. Godkännande av bildmaterial eller bygget får inte likställas med ett independent gameplay- eller ljud-PASS.
