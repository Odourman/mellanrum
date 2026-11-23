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

## Implementation #9 intake and full-system Pachinko test gate (2026-11-22)

| ID | Datum | Beslut eller fråga | Status | Källa / avgränsning |
|---|---|---|---|---|
| MEL-040 | 2026-11-22 | MEL-037 vänster fysiskt Difficulty A/B har implementerats av ROM DEVELOPMENT; A=Kampanj, B=FRI, endast konsolväxel, FIRE startar, ingen joystick/SELECT-lägesmeny. MAIN verifierade **4096-byte ROM från två Actions-arkiv** med SHA `e9ea87d381bcf8da39ec055d7d6951ceff97b21d3a798addd10fbbe540c5e974`. Produktsource SHA `6cb862...`; PR #4 evidens HEAD `49eb168...`; Draft/unmerged. | DEVELOPER_IMPLEMENTATION_RECEIVED / MAIN_NATIVE_HASH_PASS / STELLA_AB_BLACKBOX_OBSERVED / NO_RELEASE | [MAIN intag](MAIN_FINAL_AB_ROM_INTAKE_2026-11-22.md), Actions 45075716636 / 45075039996; tidigare MEL-037 `DEFERRED` historik nu ersatt i aktuellt projektläge. Faktiska SWCHB/RAM-transkript ännu NOT_VERIFIED |
| MEL-041 | 2026-11-22 | MAIN fryser ovanstående A/B-ROM-bytes och utfärdar [fullständig PACHINKO 2.0 Github Actions diagnostikorder](MAIN_TO_PACHINKO_2_0_FINAL_AB_E9EA_FULL_TEST_2026-11-22.md), inklusive riktig 15-rums joystickgenomspelning, grafik/TIA, TIA-ljud/WAV, A/B, seedad adversariell stress, cykler/scanlines och evidens. | TEST_ORDER_ACTIVE / FULL_SUITE_NOT_RUN | [Pachinko Issue #7](https://github.com/Odourman/mellanrum/issues/7); Stage0 ska ej längre invänta framtida A/B-SHA, testet är bundet till `e9ea87d3...`; independent Verification #5 separat |

**Supersession:** MEL-040/041 ändrar status, inte originalregler: MEL-037 är fortfarande designbeslutet, A/B är nu implementerat och bildobserverat, men inte independent verifierat. MEL-039:s `NOT_YET_IMPLEMENTED` var sant vid dåvarande tidsstämpel men är historik, ej aktuell status. Inga nya gameplayändringar eller release har auktoriserats.

## PACHINKO 2.0 emulator evidence and raster followup (2026-11-22)

| ID | Datum | Beslut eller fråga | Status | Källa / avgränsning |
|---|---|---|---|---|
| MEL-042 | 2026-11-22 | MAIN checked true PACHINKO Gopher real-input **2×15/15** and Stella/libretro **3×15/15** room routes on frozen E9EA ROM, plus actual emulator WAV samples; does **not** count as independent Verification, human playtest or release approval | REAL_EMULATOR_ROUTE_EVIDENCE_RECEIVED / DIAGNOSTIC_PARTIAL | [Original-artifact review](MAIN_PACHINKO_2_0_E9EA_INTERIM_INTAKE_2026-11-22.md); Gopher Actions 45077617532; Stella 45078424709; audio 45078436099. Gopher 166/166 mode/room/beat checkpoints, Stella real original PNG/video callbacks |
| MEL-043 | 2026-11-22 | Native Gopher2600 TV reports stable **261** scanlines for 119/119 frames twice versus NTSC 262 acceptance; old developer 262 CPU-model PASS cannot substitute. MAIN opens **separate diagnostic-only** cross-emulator RCA [Issue #12](https://github.com/Odourman/mellanrum/issues/12), **not** a code change. No PR4 modification, no merge/release. | P1_RASTER_DISCREPANCY_CONFIRMED_IN_GOPHER / ROM_CAUSE_UNCONFIRMED / IMPLEMENTATION_NOT_AUTHORIZED | [PACHINKO Issue #11](https://github.com/Odourman/mellanrum/issues/11), native artifact 14775931750, [MAIN intake](MAIN_PACHINKO_2_0_E9EA_INTERIM_INTAKE_2026-11-22.md). Stella scanline audit NOT_RUN; troubleshoot with known 262 control ROM |

**No gameplay canon change** made by MEL-042/043. Product ROM remains exact `e9ea87d3...`; any confirmed future fix will require separately authorized code change, new immutable SHA and new Pachinko/Verification checks. Earlier MEL-041 full test mandate remains active and only partial cases have real evidence so far.

## Ny symbolpalett och TIA-fördelning – användarens formbeslut (2026-11-23)

| ID | Datum | Beslut eller fråga | Status | Källa / avgränsning |
|---|---|---|---|---|
| MEL-044 | 2026-11-23 | **Designriktning godkänd:** de två påhittade, rituellt/runinspirerade tecknen (ersätter visuellt STEN och UTGÅNG) **och spelarens markör ska vara rödorange i samma färgfamilj**. Ugglan ska i möjligaste mån ha samma färg som barrträden och får avsiktligt vara svårare att hitta. Två tecken ska ha olika form; ingen direkt etikett/förklaring för spelaren. **Föreslagen** TIA-allokering: PF=träd, BL=abstrakt uggla, P0/P1=två olika tecken med samma rödorange färg, M0=rödorange markör (delar P0:s färg). | USER_VISUAL_DIRECTION_APPROVED / TIA_ALLOCATION_TECHNICAL_PROPOSAL_ONLY / NO_ROM_IMPLEMENTATION_AUTHORIZED | Användarens diskussion om egen mystisk symbolvärld och precisering av färgen till rödorange (ersätter tidigare 'orange'); verifiera färgkontrast över alla tre akter, träffsäkerhet/igenkänning, markörens rörelse, 4K utrymme och 6507/TIA raster. Separat GRAPHICS/ROMDEV förstudie krävs; status för faktiska sten/utgångspositioners byte är OPEN, ingen regel-/rumsändring beslutad |

**Avgränsning:** Detta är designavsikt, inte en bekräftelse på att ball/missile kan rita önskade former eller att de 15 rummen ska få andra logiska positioner. Original-ROM `e9ea87d3...` och aktiv PACHINKO/VERIFICATION behåller sin oförändrade identitet; en framtida ändring kräver uttryckligt godkänt implementationsscope, ny ROM-hash och nya tester.

## Förtydligande efter GRAPHICS-koncept (2026-11-23)

| ID | Datum | Beslut eller fråga | Status | Källa / avgränsning |
|---|---|---|---|---|

| MEL-045 | 2026-11-23 | **Korrigering/precisering av MEL-044:** stenens och utgångens **synliga gestalter ska ersättas av två olika mystiska symboler**, i samma rödorange färgfamilj som markören. **Ugglans färg är INTE bunden till trädens färg**; tidigare förslag om kamouflage var ett tekniskt försök att lösa registerdelningen, inte ett krav. Konkreta TIA-objekt och ugglans slutliga visuella färg/form är öppna inför teknisk prövning. | USER_DESIGN_CLARIFICATION / SYMBOL_DESIGN_APPROVED / OWL_COLOR_OPEN / PRODUCT_IMPLEMENTATION_NOT_AUTHORIZED | Användarens direkta korrigering efter GRAPHICS-paketets överlämning; supersedes endast ugglans färgbundenhet och tvärsäkerhet om objektfördelning i MEL-044. Övriga uttryckliga krav, gameplay/koordinater, fryst ROM och testgrindar oförändrade |

**Supersession:** MEL-045 ersätter i MEL-044 endast antagandet att ugglan ska ha samma färg som träden. PF/BL/P0/P1/M0 är en kandidat, inte gällande teknisk arkitektur. GRAPHICS har rekommenderat "Brytning / Kretsrest" (symbolpar 1) som *förslag*, men användarens slutliga symbolparval och teknisk ROM-feasibility är ännu inte godkända. Originalmaskerna behöver levereras/inspekteras separat.

## Bindande designprioritering efter 30-tricksgenomgång (2026-11-23)

| ID | Datum | Beslut eller fråga | Status | Källa / avgränsning |
|---|---|---|---|---|
| MEL-046 | 2026-11-23 | **Stenen och utgången ska visuellt bli två olika mystiska symboler. Ugglan MÅSTE fortfarande vara igenkännbar som en uggla**, inte en punkt eller ett oigenkännligt BL-streck. **Träden bör vara gröna. Alla övriga färger är öppna för bästa tekniskt och konstnärligt fungerande lösning**, inklusive symbolernas tidigare rödorange och markörens tidigare rödorange (nu preferenser/förslag, **inte** hårda färgkrav). Ingen särskild färgkoppling uggla/träd eller fast PF/BL/P0/P1/M0-fördelning är auktoriserad. | USER_DESIGN_PRIORITY_APPROVED / REPLACES_CONFLICTING_MEL-044_AND_MEL-045_COLOR_AND_OWL_ASSUMPTIONS / NO_ROM_IMPLEMENTATION_AUTHORIZED | Användarens uttryckliga korrigering efter granskning av samtliga 30 tricks. Prioritet: 1 två distinkta mystiska symboler 2 uggla visuellt som uggla 3 gröna träd 4 färger/markör/objektfördelning väljs efter verklig TIA-rasterfeasibility. ROOM coordinates/logic remain unchanged unless separately authorized |

**Supersession:** MEL-046 är aktuell canon för ovan angivna visuella mål, och supersederar motsägande MEL-044 och MEL-045. Brytning/Kretsrest är GRAPHICS-förslag, inte slutvalt av användaren. Fryst E9EA ROM och aktiv test/Verification påverkas ej.

## U3-godkännande och separat fullspelsauktorisation – 2026-11-23

| ID | Datum | Beslut/mandat | Avgränsning och källor |
|---|---|---|---|
| MEL-047 | 2026-11-23 | **USER_VISUAL_APPROVED:** horisontellt spegelvänd **U3 Vingkropp** med lodrät näbb och **tre vinganimationsrutor utan ögonblinkning**. Exakt 8-byte top-down: **B0** `18 7E DB F7 F7 7E 7E 24`, **B1** `18 7E DB F7 F7 FF BD 24`, **B2** `18 7E DB F7 F7 FF FF 24`. Källformat 9-byte bottom-up inklusive nollraden: B0 `24 7E 7E F7 F7 DB 7E 18 00`; B1 `24 BD FF F7 F7 DB 7E 18 00`; B2 `24 FF FF F7 F7 DB 7E 18 00`. Exakta frames accepterade som **utseende**, föreslagna animationstider och val av färg inte separat godkända. | [GRAPHICS användarintag](https://github.com/Odourman/mellanrum/issues/13#issuecomment-7088461360), [verifierad portabel data](https://github.com/Odourman/mellanrum/blob/graphics/u3-user-accepted-handoff-20261123/design/u3-user-accepted-handoff/U3_SELECTED.json). **S3:s exakta pixlar och Närvarons B-PF2-frames är användarpreferenser/designförslag, inte egna final-art-PASS.** |
| MEL-048 | 2026-11-23 | **Separat, ny uttrycklig användarauktorisation i [Issue #15](https://github.com/Odourman/mellanrum/issues/15)**: ROM DEVELOPMENT får färdigställa en **ny** komplett spelkandidat med U3/S3/Närvaron och improvisera inom skyddade spelregler. Detta **supersederar äldre 'NO_PRODUCTION_IMPLEMENTATION' endast för ny kandidat**, **inte** för frysta PR #4 eller fri merge/release/canon-avvikelse. Ny 4096-byte ROM SHA `45d3422371d41bf896c0ac0076c57d93e600dcf7f4a1e51d4d352312fce8d7a7`, [Draft PR #16](https://github.com/Odourman/mellanrum/pull/16) på `56d70c316031bf55a5260e1fbbe0fe187c55f297`; development-resultat dokumenterade men **independent Verification pending**. | [Användarorder Issue #15](https://github.com/Odourman/mellanrum/issues/15), [ROMDEV sluthandoff](https://github.com/Odourman/mellanrum/issues/15#issuecomment-7088832924), [MAIN independent Verification #17](https://github.com/Odourman/mellanrum/issues/17) och [PACHINKO #18](https://github.com/Odourman/mellanrum/issues/18). Utvecklarens Gopher/Stella PASS är inte självständig release-verifiering. |

**Historiska avgränsningar:** MEL-044/045/046:s äldre förstudie- och färgformuleringar får inte åberopas som förbud mot den uttryckligt senare begränsade Issue #15-implementationsauktorisationen. MEL-046:s visuella grundkrav består. **U3 godkänd art i MEL-047 ≠ S3/Närvaro-slutgiltigt konstgodkännande ≠ färdigställa/merga/releasa på eget bevåg.**

## Användaråterkoppling efter faktisk PR #16-video och ny MAIN-testning – 2026-11-23

| ID | Datum | Nytt beslut/krav | Status och avgränsning |
|---|---|---|---|
| MEL-049 | 2026-11-23 | **USER_AUDIO_DIRECTION:** Byt det i början brusdominerade ljudet mot **mycket mörka droneljud i titel/start/inledning**; spara korta skrovliga/brusande effekter främst till **Närvarons framträdanden**. Använd autentiska Atari 2600/TIA-kanaler, inte inlagd modern ljudfil. | USER_AUDIO_CHANGE_AUTHORIZED_FOR_NEW_CANDIDATE / SOUND_FINAL_LISTENING_PENDING. [Teknikuppdrag #20](https://github.com/Odourman/mellanrum/issues/20). Ingen förändring av frysta PR #16 `45d342...` eller gamla PR #4, ingen merge/release. Bekräfta i faktisk emulerad TIA-inspelning före slutlig konstnärlig acceptans. |
| MEL-050 | 2026-11-23 | **USER_GAMEPLAY_DIFFICULTY_CONCERN CONFIRMED BY MAIN LOCAL NATIVE STELLA DIAGNOSTIC:** 14/15 ursprungliga rum i nuvarande PR #16 löser sig själva utan joystick/FIRE efter normal rumsstart. I-02 ej löst efter 36 000 idle-frames (10 min). Ingen gameplayinteraktion krävs i 14/15 rumssegment, även om man fortfarande måste trycka FIRE mellan rummen för att avancera. | P1_USER_EXPERIENCE_AND_DESIGN_RELEASE_BLOCKER / EXISTING_CANON_UNCHANGED / DESIGN_REMEDIATION_PROPOSAL_REQUIRED. [Exakt diagnostic evidence](https://github.com/Odourman/mellanrum/blob/review/pr16-passive-idle-evidence-20261123/diagnostics/passive-idle-20261123/MAIN_REAL_STELLA_RESULTS.md) och [designuppdrag #19](https://github.com/Odourman/mellanrum/issues/19). Ändra inte V5.1:s fem geometrier/15 koordinater, regler, mapper eller release utan separat beslut om reviderad canon och implementeringsscope. |
| MEL-051 | 2026-11-23 | **USER_CURSOR_CLARIFICATION:** tre primära spelarmarkörstillstånd ska vara neutral, godkänd, nekad. Separat specialtillstånd vid kapning av Närvaron får finnas och ska inte misstolkas som ett fjärde primärt val. | UI_ART_REVIEW_OPEN; current ROM implements 4 `ackType` statuses only as M0 hardware widths 1/2/4/8 pixlar, while 4 predeclared 8×8 `CursorIdle/Ack/Denied/Intercept` graphic tables are NOT referenced by active renderer. Ingen separat slutacceptans av symbolformen eller ny rasterimplementation. |

**Prioritet:** MEL-050:s verkliga 14/15 passiva auto-vinster är en allvarlig designgrind trots starka tidigare emulator-/stresstestresultat; dessa tidigare bevis var korrekta inom sitt begränsade scope men saknade nollinmatningsgrinden. Förlängning/långsammare uggla eller en trivielt krav på valfri FIRE-tryckning är inte en tillräcklig designlösning. Användarens uttalade kritik ger inte automatiskt fri behörighet att ändra alla skyddade rum/regler tyst. MEL-049 är däremot en uttrycklig ljudändringsbegäran med avgränsat implementationsmandat.

## MELLANRUM cartridge ROM size upper bound – user decision 2026-11-23

| ID | Datum | Beslut | Omfattning och skydd |
|---|---|---|---|
| MEL-052 | 2026-11-23 | **USER_APPROVED NEW MAXIMUM CART_ROM = 32 KiB** (32768 bytes) for future MELLANRUM candidates. Prior `4 KiB unbanked` is **not** a mandatory target or artistic virtue. A standard **F4 32 KiB bank-switched Atari 2600 cartridge** (eight 4 KiB banks) is historically compatible with an unmodified original Atari 2600 when implemented with appropriate cartridge logic; Atari's original *Fatal Run* is a 32 KiB example. No additional coprocessor or non-standard console modification is authorized by this decision. | Design and implementation planning may budget up to 32 KiB **where justified**. Do not fill 32 KiB gratuitously. Smaller 4K/8K/16K outcomes remain acceptable; an image with 24 KiB used may still require physical 32 KiB/F4 image/mapper layout. The Atari 2600's 128-byte RIOT RAM, TIA player/missile/PF, 6507 speed and 76 cycles/scanline limits remain. [Stella bankswitch docs](https://stella-emu.github.io/docs/) and [Fatal Run cartridge reference](https://www.atariprotos.com/2600/software/fatalrun/fatalrun.htm). **No ROM mapping, code, canonical room coordinates, gameplay rules, release, or new implementation step is changed or individually authorized here.** Future mapper choice must be explicit in separately authorized new candidate implementation, with bank layout, reset/IRQ vectors, F4 hotspots, cross-bank jumps, clean DASM, authentic Gopher/Stella, original-Atari cartridge hardware validity, and user RetroN 77 Stella 7 SD/physical cart compatibility evaluated distinctly. Preserve immutable Draft PR #16 source SHA `56d70c316031bf55a5260e1fbbe0fe187c55f297` and original 4 KiB ROM SHA `45d3422371d41bf896c0ac0076c57d93e600dcf7f4a1e51d4d352312fce8d7a7`, plus frozen PR #4/E9EA. |

**Rationale:** The new room-design gate [Issue #19](https://github.com/Odourman/mellanrum/issues/19) found 14/15 passive zero-input wins in the original PR #16 and the user wants genuinely meaningful interaction; [audio Issue #20](https://github.com/Odourman/mellanrum/issues/20) needs authentic low TIA drone and a contrasting noise vocabulary for Närvaron. ROM capacity expansion can relieve code/data/graphics/audio space pressure, but **does not itself solve the level-design flaw or increase RAM/TIA cycles**. A change to 32 KiB *maximum* is not a command to immediately produce a 32 KiB ROM.

## MELLANRUM ROM limit correction — explicit later user decision 2026-11-23

| ID | Datum | Bindande beslut | Omfattning och skydd |
|---|---|---|---|
| MEL-053 | 2026-11-23 | **USER_FINAL_NEW_MAX_ROM = 16 KiB (16384 bytes)**, superseding prior **MEL-052 32 KiB limit** for future MELLANRUM candidates. **Preferred standard mapper: F6 / four 4 KiB banks**, without an unnecessary coprocessor, extra cartridge RAM, console hardware modification or extra accessory. 16 KiB is a **hard upper limit** unless user explicitly revises it again; 4 KiB/8 KiB remain valid when sufficient. User asks that this capacity improve game quality rather than act as artificial restriction. | **MEL-052 SUPERSEDED for ROM-size maximum; its historical approval remains in the log, not active authority.** Do not silently use F4/32 KiB or larger ROM. F6 compatibility supported by [Stella docs](https://stella-emu.github.io/docs/) and [RetroN77 compatibility reports](https://forums.atariage.com/topic/280100-retron77-compatibility-list/page/10/), but end-to-end original Atari NTSC/RetroN77 Stella7 SD/cardridge remains to be actually tested. More ROM allows distinct 15-room state/geometry and solver data, real TIA drone/enhanced sound sequence, distinctive cursor acceptance UI and Presence/animation variants, but DOES NOT increase 128B RIOT RAM, available TIA objects/audio channels or per-scanline 6507 time budget. **User's size choice is architecture/budget authorization, NOT authorization to implement revised V5.1 geometry/rules, to start next separate game-implementation step, or to merge/release.** Keep frozen old 4K Draft PR#16 HEAD `56d70c316031bf55a5260e1fbbe0fe187c55f297`, binary SHA `45d3422371d41bf896c0ac0076c57d93e600dcf7f4a1e51d4d352312fce8d7a7`, and original PR#4 intact. Reworked game design and true no-input tests remain Issue #19 pending explicit design canon approval; scoped audio redesign remains Issue #20. |

**Latest authority:** MEL-053 **16 KiB ceiling overrides MEL-052's 32 KiB**; the previous proposal of “16 KiB preferred with 32 KiB fallback” is no longer authorized. Any actual new ROM hash/bank scheme requires separate tracked implementation and completely fresh source/campaign/idle/graphics/audio/raster/stack/physical compatibility tests; prior 4K source-hash evidence is not portable.

## Ny uttrycklig fullproduktionsauktorisation – 2026-11-23 (senare än MEL-053)

| ID | Datum | Senaste bindande beslut | Avgränsning och supersession |
|---|---|---|---|
| MEL-054 | 2026-11-23 | **USER_AUTHORIZED_COMPLETE_AUTONOMOUS_MELLANRUM_VNEXT_DEVELOPMENT**, fullständig ny spelkandidat, högst **16 KiB (MEL-053)**, konventionell **F6 4×4 KiB** föredras, **omdesign av samtliga 15 rum och nödvändiga regel-/geometriförändringar är nu uttryckligen auktoriserad för den nya kandidaten**. ROM DEVELOPMENT får självständigt lösa tekniska och spelmässiga problem utan mikrogodkännanden, bevara originalets konstnärliga kärna enligt gällande användarbeslut och dokumentera alla kanonavvikelser. Obligatorisk genomgång av **alla 30 Atari 2600-tricken**, använd bara de som faktiskt hjälper och går att bevisa i riktig emulator. Läs tillgänglig Atari-research i Google Drive som rådgivande teknik, inte andra projekts canon. Även tidigare användarönskad **mörk autentisk TIA-drone** i början och **brus kopplat till Närvaron**, samt tydlig markör neutral/godkänd/nekad, ska ingå. | [Ny fullständig implementationsorder Issue #21](https://github.com/Odourman/mellanrum/issues/21), bygger på senare uttrycklig användarinstruktion samma dag. **Supersedes tidigare "Issue #19 endast designförslag/separat tillstånd före geometri- och regeländring" och "Issue #20 endast ljudimplementation" som begränsningar för just den nya integrerade kandidaten**. Historiska Issue #19- och #20-fynd kvarstår som krav. Original Draft [PR #16](https://github.com/Odourman/mellanrum/pull/16) HEAD `56d70c316031bf55a5260e1fbbe0fe187c55f297`, ROM SHA `45d3422371d41bf896c0ac0076c57d93e600dcf7f4a1e51d4d352312fce8d7a7`, och fryst PR #4 får inte ändras. Ny branch + ny ROM/SHA + ny Draft PR krävs. Detta är **utvecklingsauktorisation, inte förhandsgodkänd slutcanon, ändring av konstnärlig kärna, merge, release eller oberoende Verification/Pachinko**. |

**Förändringsdisciplin:** Endast nödvändiga och motiverade förändringar inom den autentiska experimentella/dadaistiska skogsidentiteten (uggla/träd/sten/Närvaron, 3 akter/15 rum) är delegerade. ROM DEVELOPMENT får dokumentera avvikelser och bygga klart utan att fråga om varje rum; slutlig konstnärlig acceptans och release ägs fortsatt av användaren. 16 KiB är fast kapacitetstak, inte krav på utfyllnad.

## MEL-055 – ny separat användarauktorisation: faktisk 16 KiB F6-utbyggnad (2026-11-23)

| ID | Datum | Senaste explicita beslut | Avgränsning och supersession |
|---|---|---|---|
| MEL-055 | 2026-11-23 | Användaren vill **inte längre nöja sig med den 4 KiB-stora vNext-kandidaten**; ger ROM DEVELOPMENT **ny, separat och uttrycklig implementationstillåtelse** att självständigt **utveckla/förbättra MELLANRUM till en verklig 16 KiB (16384 bytes) F6-bankväxlad ROM**, med materiellt bättre spelmekanik, fler nyanser i 15 rum, grafik och genuin TIA-drone/Närvaro-ljud. Den extra kapaciteten ska göra spelet upplevt bättre, inte fyllas med tomma banker/utfyllnad; 30 Atari-trick och Drive-research ska utnyttjas selektivt och bevisas i nya emulatorkörningar. | [Fullskalig nästa implementationsorder Issue #26](https://github.com/Odourman/mellanrum/issues/26). Detta **skärper MEL-053:s äldre 16 KiB-tak och MEL-054:s 4 KiB-tillåtelse** till ett **faktiskt 16 KiB F6-mål för en NY spelkandidat**, inte ändring av historiskt tidigare beslut för äldre kandidater. Förra [PR #23](https://github.com/Odourman/mellanrum/pull/23) HEAD `2a6794f42b2991231a4927cc8c1f5dcdd291bc9b`, ROM `63e719a362ae2eb5689484ca7c28c628b495a2843723898ebec3fe6374c43bdc`, samt tidigare PR#16/PR#4 och deras bevis ska förbli orörda, Draft/unmerged. [Verification #24](https://github.com/Odourman/mellanrum/issues/24) och [Pachinko #25](https://github.com/Odourman/mellanrum/issues/25) gäller ENDAST gammal PR23 4 KiB SHA och kan inte verifiera ny 16 KiB SHA; ny separat oberoende granskningsorder krävs för ny kandidat. Ingen merge/release eller slutlig konstnärlig acceptans ingår i mandatet. |

**Exakt förtydligande:** 16 KiB är här både användarens hårda kapacitetstak och det **positiva produktionsmålet (genuin 16 384-byte F6-binärram)** för Issue #26. Att ensam artificiellt fylla upp den befintliga 4 KiB-ROM:en till 16 KiB uppfyller inte uppdraget. Äkta TIA/6507/RIOT och originalkassettstandard utan extra RAM/hjälpprocessor är oförändrade hårdvarukrav. Om relevanta meningsfulla förbättringar inte kan byggas ska utvecklaren rapportera begränsningen snarare än fabricera nyttan. Dessa krav gäller bara den nya separat auktoriserade implementationen.

## MEL-056 – separat ny implementationsauktorisation efter fullständig videogranskning (2026-11-23)

| ID | Datum | Senaste uttryckliga användarbeslut | Scope / auktoritet och skydd |
|---|---|---|---|
| MEL-056 | 2026-11-23 | **USER_AUTHORIZED_FINAL_ARTISTIC_GAMEPLAY_REDESIGN_IMPLEMENTATION**, "Ok,gör en ny prompt åt Rom development. Låt den göra Följ dina rekommendationer till ett klart spel." ROM DEVELOPMENT får självständigt **IMPLEMENTERA** alla rekommenderade förändringar från MAIN:s genomgång av verklig 16KiB PR27-video och bygga en ny komplett **äkta 16384 byte F6 NTSC** spelkandidat. Prioritet P1: **15 genuint mer mångstegiga och varierade banor**, meningsfulla val och rättvis återkoppling; **tre markörformer som faktiskt ser olika ut** neutral/godkänd/nekad samt extraordinär Närvaron-interception, med riktiga Stella-bilder; mörk, läsbar akt III, synligare barrträd/uggla/sten/utgång, kraftigare negativrums-Närvaro, rikare och mindre 4,267-sekundsrepetitiv TIA-drone och avslut som inte bara fryser/stängs av. Alla 30 relevanta trick/Drive-research värderas på nytt och används när de ger faktisk vinst. | **Full implementation order [Issue #32](https://github.com/Odourman/mellanrum/issues/32).** Ersätter tidigare "bara designförslag, ingen ROM-ändring" i [#30](https://github.com/Odourman/mellanrum/issues/30) och [#31](https://github.com/Odourman/mellanrum/issues/31) **enbart för NY separat full spelkandidat**, inte retroaktiv ändring av testad PR27. Fryst [Draft PR #27](https://github.com/Odourman/mellanrum/pull/27) HEAD `178d915a5395e2b62857886a3c60dd254af858d2`, ROM `7ce777dc273e1c30d8621843052e941ced41fcf2961bcdf835576a11c9592446`, samt PR23, PR16, PR4 **får inte modifieras**. Ny utvecklingsgren, nytt ROM-SHA, nya riktiga DASM/Stella/Gopher-tester behövs. Befintliga oberoende [Verification #28](https://github.com/Odourman/mellanrum/issues/28) / [Pachinko #29](https://github.com/Odourman/mellanrum/issues/29) gäller ENDAST den gamla PR27-checksumman och inte automatiskt nya ROM:en; ny oberoende verifiering krävs efter implementation. Konstnärlig slutacceptans, physical Atari/RetroN77, merge och release är fortfarande **inte auktoriserade**. |

**Förtydligande:** Prompten är faktisk implementationsauktorisation för hela den nya kandidaten; den godkänner inte okända framtida scopeändringar utanför MELLANRUM:s tre grundmotiv (barrträd, autonom uggla, sten), negativa Närvaron och tre akter. En optimerad botgenomspelning på 3m52s eller 92 % bildrutor utan styrning är en signal om låg interaktionstäthet men **inte** ensam vetenskaplig evidens för mänsklig nybörjarsvårighet. Kräv både verkliga emulatortester och ärligt märkt användar-/människoplaytest, utan påhittade PASS.
