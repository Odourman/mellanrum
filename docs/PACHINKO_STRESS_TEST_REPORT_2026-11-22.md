# MELLANRUM – PACHINKO STRESS TEST – RAPPORT TILL MAIN

**Datum:** 2026-11-22  
**Roll:** PACHINKO STRESS TEST (diagnostisk, skild från ROM DEVELOPMENT och Verification)  
**Samlad disposition:** **PARTIAL / NO NEW CONFIRMED PRODUCT DEFECT WITHIN EXECUTED SCOPE**. Full releasestatus **INCONCLUSIVE / GATE OPEN**.

## 1. Fryst mål och integritet

- Repository: https://github.com/Odourman/mellanrum
- PR #4: https://github.com/Odourman/mellanrum/pull/4 – senast kontrollerad öppen, Draft, inte mergad, head exakt den frysta committen.
- Fryst produktcommit: `8bdecde79a6bc1ecb804484d5d257f4f1a99b052`.
- Binär: NTSC standard 4 KiB, **4 096 byte**.
- **SHA-256** `ec791333da37613ec99ea70b2a983ecc1666b4e576211ece41a8e40bd14cbaed`.
- Identiska bytes i användarens ROM, medföljande native DASM CI-artefakt, körd diagnostisk CPU-modell och ny native DASM/Stella Actions-körning.
- Original `reference/engine.py` och `reference/rooms.py` kopierades från exakt GitHub SHA och deras git-blob-SHA verifierades till `f0425bd02653c281174276d5fae2d33608637d0b` respektive `84c13fd2a466b9e376ac199f755789f8ad7ba983`.
- Komplett original `reference/rooms.json` hämtades INTE som lokala originalbytes. Lokala `REPRO/repo/reference/rooms.json` är tydligt en projektion av GitHub-avlästa ID:n och abstrakta lösningssekvenser. Den ska **inte** påstås ha original SHA eller full canon.
- Stora original V5.1/GRAPHICS-arkiv fanns inte i det levererade stresstestpaketet och har inte materialiserats på nytt.

## 2. Testresultat per evidensklass

| Evidensklass | Faktiskt resultat | Status / begränsning |
|---|---|---|
| ROM-integritet och produkt SHA | 4 096 bytes; tre lokala/CI-artefakter matchar | PASS för identitet |
| Native DASM | Ny diagnostic Actions-branch byggde exakt ROM och SHA-check lyckades | PASS build only |
| SOURCE / V5.1 | Exakt engine.py/rooms.py blob, 15 original-vittnen projicerade | PARTIAL – hela V5.1/GRAPHICS-arkiv inte återlästa |
| Source-guided Pachinko model | 2 400 körningar, 69 747 genomförda uggletick, 0 ROM–Python-paritetsavvikelser | PASS_MODEL_PARITY inom policyurval |
| Model tillståndsgraf | 36 067 unika källstyrda tillståndssignaturer och 44 438 riktade övergångar | OBSERVERAT antal, ej full rymd/täcknings% |
| GATE / IMPOSSIBLE, CLOG, BOG, COUNTERFACTUAL | 152 riktade fall; 0 modellparitetsavvikelser | PASS_MODELED_ONLY |
| 15 abstrakta källvittnen | 15/15 når utgång i ROM-instruktionsmodellen | PASS_MODEL, ej joystick |
| Frame-nivå i CPU/RIOT/WSYNC-modell | 64 körningar, 17 600 bildrutor, 0 instruktionsexceptioner | PARTIAL modell, inte TIA |
| FRI SKOG, lång CPU-körning | 19 080 bildrutor; ett 8-bitars tickomslag, mode4 bevarat | PASS inom modell |
| Verklig Stella | 52 loggade ungefärliga tangenttryckningar + 13 autentiska PNG (12 distinkta), reset, kampanjrum och FRI SKOG. CI **SUCCESS** | EMULATOR_OBSERVED för begränsad inputyta |
| Full 15/15 emulatorgenomspelning | Inte genomförd | NOT_RUN |
| Verklig TIA raster/scanline, spriteöverlagring | Bilder finns, men ingen frame-exakt beam-timing audit | INCONCLUSIVE |
| Ljud | CPU-modellen skriver till båda kanalerna; CI använde dummy-audio | AUDIO_SUBJECTIVE NOT_RUN |
| Gopher2600/fysisk konsol | Ingen tillgänglig exekvering | NOT_RUN |
| PAL | Ingen PAL-ROM implementerad | NOT_IMPLEMENTED |
| Oberoende Verification | Utförs av separat roll | NOT_RUN här |

## 3. RAIN, TILT, CLOG och BOG – 2 400 modellkörningar

15 rum × fem profiler (`RAIN`, `TILT_FIRE`, `TILT_STONE`, `CLOG`, `BOG`) × 32 frön = **2 400 starter**. Varje start hade högst 80 planerade owl ticks, totalt 192 000 planerade. **69 747 ticks exekverades faktiskt** eftersom avslutade rum stoppades vid deras uppnådda mål. Ingen dold utjämning av censurerade starter. Observerade köstorlekar: 0 = 28 860 tick, 1 = 28 250, 2 = 12 637; fas0 = 49 220 tick, fas1 = 20 527. Talen hör till de fem generativa testpolicyerna, **inte mänskliga spelare**.

`REPRO/results/population_32/model_runs.jsonl` innehåller full seed, policy, inputsekvens och observation per tick. `model_metrics.json` anger antal och scope. `REPRO/results/derived/` ger rådatahärledda grafer, rumsstatistik, positioner och övergångstabell. Den lokala runnern använde exakt ROM-binära bytes, men en ny lättvikts-6502-instruktionsadapter och de två byteverifierade kandidatreferenserna. **Inget av detta är äkta Stella-spelning.** Markörens position får injiceras direkt i dessa källstyrda tickspår, vilket begränsar slutsatser om faktisk traversering.

## 4. Riktade adversariella tester

**152 ytterligare testfall**: GATE originalvittnen (15); CLOG två ekoslots och tredje avvisning (20); BOG Närvaron före/under/efter aktiva tidsfönster (12); COUNTERFACTUAL par med en ändrad handling (90 starter, 45 par); CLOG >256 ticks på fem akt III-rum (15). Samtliga 152 jämfördes utan upptäckt mismatch mellan ROM-instruktionsmodell och källa. Rå sekvenser och möjliga avvikelseobjekt finns i `REPRO/results/deep/`. Ingen ny bekräftad produktbugg att minimera skapades.

Detta stödjer kodmodellens konsistens under provade förutsättningar; det styrker **inte** att varje konkret joystick-FIRE når samma mål före nästa 72-frame beat. Varken source-guided direct-positioning eller gamla solution-oracles får felaktigt bli 15/15 real-player PASS.

## 5. Bildrutor och långkörning i egen CPU-modell

60 rum×policy-poster på 240 frames fördelade på 15 rum och fyra frame-inputpolicyer; dessutom 3 BOG-risksessioner på 900 frames samt en 500-frame coda (ingång via kontrollerad debugger-/CPU-rutin, inte genom verklig avslutning av rum 15). **Totalt 64 poster, 17 600 frames**. Alla 64 första modellframes hade en uppstartsfraktion på 19 866 cykler (63) eller 19 892 (1). Resterande **17 536** hade modellvärdet **19 912 = 262×76 cykler**. Inga CPU-exceptioner, negativa markörkoordinater eller otillåtna markörgränser observerades.

**FRI SKOG:** riktig titelstyrd SELECT/FIRE i ROM-instruktionsmodellen startade mode4, room-index 13; 19 080 separata idle-frames kördes som checkpointad exakt förlängning. Alla gav modellvärdet 19 912 cykler; ett beatvarv 255→0 observerades; mode4 förblev aktivt. CPU-modellen skrev till båda TIA-audio-kanalernas kontroll/frekvens/volymregister, men audio kunde inte avlyssnas. Cyclemodellen är uttryckligen approximativ och **kan inte certifiera TIA-scanlines, HMOVE, ljud eller pixelraster**.

## 6. Faktisk Stella – separat isolerad Actions-körning

- GitHub Actions: https://github.com/Odourman/mellanrum/actions/runs/45069826844 – **SUCCESS**.
- Diagnostisk workflow-gren `pachinko/diagnostics-8bdecde-20261122`, HEAD `e6e8f3047d2006418fee0e93a01fb918b7d6e186`.
- GitHub compare från fryst produkts SHA till diagnostisk SHA bekräftar **exakt en tillagd workflow-fil** `.github/workflows/pachinko-stella-diagnostic.yml`, ingen ändring i produktens ROM/källor, PR #4 kvar Draft.
- Native DASM-ombyggnad genomfördes på GitHub Actions ubuntu-24.04 och SHA verifierades. Faktisk Stella i Xvfb användes via SDL software / xdotool med verkliga tangenttryckningar: titel, start av kampanjrum, 24 riktade/kombinerade rumstangenttryckningar, RESET till titel, SELECT FRI, 24 riktade/kombinerade FRItangenttryckningar och idle.
- **52 `tap`-rader, 13 originalskärmbilder (12 distinkta PNG-bytehashar), totalt 66 journalrader**. Autentiska filer, ROM och tidsstämplar är faktiskt återlästa från workflow artifact ID `14772668727`; dess ZIP-digest SHA-256 `bc3e21cb2d981b257d9f9a9d28f0f99592ea56993102dc42d15da5d32c41437f`.
- Skärmbilderna visar visuell skillnad mellan titel/kampanj och FRI, samt olika rörelse-/faslägen. Detta är inte en pixel-oracle mot samtliga originalskärmar.
- `stella.log` visar "X connection ... broken" vid uttrycklig processavslutning, inte bevis om krasch i spelet. `rominfo` klassar kartan NTSC och 4K. Exakt Stella-version loggades inte. `SDL_AUDIODRIVER=dummy` och ljudlyssning gjordes inte.
- xdotool-timing styrs av väggtid och kan inte garantera frame-exakt handling. Bara begränsad svartlådsrörelse och bilder, **inte fulla 15 verkliga rumsgångar**.

## 7. Fel, osäkerhet, nästa MAIN-beslut

**Ingen ny verifierad produktavvikelse**. Första separata diagnostiska workflow-försöket misslyckades med ett reproducerat testverktygsfel (`git diff` mot en commit saknad i grund checkout); efter isolerad fetch-depth-rättning gick körningen igenom. Det är inte ett MELLANRUM-fel. En lokal första ramtestkampanj träffade tidsgräns efter 32 av 60 rumsprofiler, sedan genomfördes återstående 28 separat och ursprungsloggarna bevarades.

Kvarvarande högprioriterat osäkerhetsområde är verifiering av alla 15 rum **med riktiga joystickrutter i Stella eller Gopher**, helst frame-exakt input- och RAM-/TIA-spår; samtidigt PF/P0/P1/BL/M0, Närvarons visuella tidsfönster och 262-linjers rasterbudget; ljudlyssning på verklig ljudutgång; samt oberoende Verification.

**Slutstatus: DIAGNOSTIC_PARTIAL_WITH_EVIDENCE / NO_RELEASE_PASS / STOP → MAIN.** Denna rapport godkänner varken PR-merge, release eller någon produktionskodändring.

## 8. Filförteckning

- `MAIN_SUMMARY.md`: kort besked till MAIN.
- `METRICS.json`, `VERDICTS.csv`, `BUGS.md`: aggregerat utfall och klassning.
- `REPRO/results/population_32/`: 2 400 körningar, hela input-/state-spår, metrics, 0 failure-rader.
- `REPRO/results/deep/`: 152 riktade sekvenser, 0 failure-rader.
- `REPRO/results/frame/`: 64 fulla ROM-instruktionsmodellspår med 17 600 frames.
- `REPRO/results/long_fri/`: 19 080 frame-rader, 5 checkpointblock, slutprogress; runtime-pickle utelämnat som icke-portabelt.
- `REPRO/results/real_stella/`: 13 autentiska Stella-PNG, input_events.tsv, ROM, rominfo, rålogg och autentiskt SHA-manifest; kontaktblad är härledd visualisering.
- `REPRO/results/derived/`: fyra datadrivna PNG, flow/position/edge CSV och metrics.
- `REPRO/repo/`: byteverifierat Python engine/rooms, modellprojection för ursprunglig witness, *diagnostiska* CPU-/diff-script samt exakt binär/symbolfil; **inte** komplett Git checkout.
- `REPRO/input/ci_native/`: omonterad native DASM `.lst`, `.sym`, 4KiB ROM och ursprungligt artefaktmanifest.
- `REPRODUCE.md`: exakta kommandon och rätt evidensetiketter.
- `SHA256SUMS.txt`: hash för varje payloadfil i detta paket.
