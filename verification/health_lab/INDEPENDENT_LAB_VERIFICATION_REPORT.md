# MELLANRUM: SKOGEN SOM LYSSNAR – HEALTH LAB_STACK_INLINE_PADDED_B
## Slutrapport: oberoende VERIFICATION av isolerat stackexperiment, 2026-11-25

**Uppdrag:** MAIN IV:s `MELLANRUM_HEALTH_LAB_INDEPENDENT_VERIFICATION_STARTPROMPT`, separat från den frysta RC1-verifieringen #50 och från PACHINKO. **Status: `LAB_INDEPENDENT_DELTA_PASS_BOUNDED` för här angivna test och source-domäner; `GLOBAL_ALL_PATH_TIMING_INCONCLUSIVE`; `NO_RELEASE_APPROVAL`.** Ingen produktionskod eller ROM har ändrats. Detta är **inte RC2**, och inte en begäran att automatiskt börja en senare implementation eller Pachinko. Tidigare HEALTH-resultat används som referens, inte ommärkta som vår verifiering.

## A. Oföränderliga identiteter och källauktoritet

| Objekt | Identitet |
|---|---|
| RC1 – produktreferens | PR49 Draft/ej mergad, HEAD `d013a0f82621d46ad12674a4a8e944bf005cd9c3`, produktcommit `7b400ad8678e8341a26f65cc757b1eb762654c83`, Git blob `afce29944cce726fa0f935ed3104abc954e7e6da` |
| RC1 – faktisk ROM SHA-256 | `456005ed691860b32c44b79f2a71666f622b005f5a798eadf9b549c59cff13bd` |
| LAB_STACK_INLINE_PADDED_B – isolerat experiment | **`8a59b84eb5151f78d40e6943c854d7e42c166b531aee3d40432182d32dcdf03b`** |
| HEALTH:s dokumentationsgren | `health/optimization-lab-2026-11-25`, dokument-HEAD `3cf158aaa2f74ed95f36f46a0e75806ac54e80eb`, **inte** experimentets produktcommit |
| Faktiskt levererad HEALTH-arkivfil | 3 318 898 B, SHA `f8950badc9fed8495a7dfa5fbd7849dd8b5b252cfe9dfba125b041fe7e1289f1`, 1 300 unika poster, 1 299 manifestposter, CRC PASS |
| Native DASM | 2.20.14.1, ELF `cfb23732297a4fe1c8d4a78d44206037d97733aedb2772503bbf029a4aa91291` |
| Native Gopher2600 | source `74c544203378c1448a33c29bc8b4586079b050f4`, ELF `7b12dff57fcb73154122d2477f35d9c8ae8b344649bc0faa8ff6f5663c70470b` |
| Stella/libretro | `8.0_pre 8dd5600`, core `2130ed1153cef66ef3f34bf9063f675f1f3342bc18320eb9ae5101743e3042df` |

Båda ROM-filerna är exakt 16 384 byte, normal NTSC F6 med 4×4 096 byte och utan extra RAM/specialchip. Oberoende två rena native DASM-byggen **per ROM**, totalt fyra, matchade båda levererade kandidaterna byte för byte; fullständiga listningar, symbolfiler, bankbinärer och byggloggar finns under `BUILD/`. RC1 och LAB ger exakt samma SHA i bank 0, 1 och 2: `4f1fefc7513d5c0aef2d1c2a406b77975e59fc60e0a3361fa34455b4c669c49f`, `8d49d78a7f7ea98d1638693767de146b54b7b97673eb5f077fbf9c0554e3a1e8`, `6b82511ba23726be41aa5f7a4e8c2555f5e039ee6fc2ec6a1e0774117cfffbfc`. Bank 3 ändras från `46855dddaefd3de616e41e61f9e0fc6c921d16983800a2dd514239df610080cb` till `b3a24ac48440485518bd99bbc017cb68a8418ccc4247dc87729ea1f573246037`.

Exakt fullständig källjämförelse av de sex filerna i `rom/` pekar ut **endast `rom/src/main.asm` som ändrad**. Källa RC1 SHA `758d5ad2eb14942d4b2ca6263aa2942ba61f927285291fa51bbedf4e8ff1f01d` och LAB SHA `3246d67a40470454eb56c38f2f4c32fb34ccb4ff38ed796ccb10cf00a647d53e`. Den reella diffen flyttar `DecodeKey`-kroppen in i `ToggleTree`, ersätter den tidigare `JSR`/`RTS`-kostnaden med sex officiella `NOP` och tar bort den separat anropade avkodningen. **Två netto ROM-byte tillkommer**. Fullständig bank-offsetjämförelse ger 0/0/0/**2 547** olika bytes, huvudsakligen omlokalisering, inte 2 547 oberoende algoritmändringar. Bank 3:s fria luckor går 3+3 → 1+3 byte; inget ytterligare variabel-RAM deklareras.

## B. Omlokaliseringsledger, 6507-cykler och verkliga giltiga index

Från **två nybyggda native DASM-listningar och verkliga bytes** mappades 1 381 gemensamma semantiska bank3-instruktioner. 203 inbördes mappade relativa branchplatser i bank3 analyserades; övriga oförändrade bank0–2 behöver ingen ny bank3-lokalisering. En branch ändrar sidgränsstatus: `BCS OwlTryNext`, RC1 `$F4FC` med mål `$F567` (tagen branch +1 page-cross) → LAB `$F4FE` mål `$F569` (utan denna extracykel). **Taget villkor blir en cykel snabbare**, inte långsammare. Kontrollerad naturlig prefixobservering nådde branchplatsen men dokumenterade inte ett taget utfall; om just gränskandidatens villkor är naturligt nåbart i alla avsedda rum är därmed inte bevisat. Rutinen ligger i spellogik före VBLANK-synkronisering, inte inne i Stem13. Klassning: `PASS_CONDITIONAL` för instruktions-/sidgränsberäkningen, naturligt branchvillkorskomplement `INCONCLUSIVE`.

**Samtliga 58 indexerade instruktioner vars SIDGRÄNSINDEX ändras** finns var för sig i `ANALYSIS/RELOCATION_DOMAIN_AUDIT.csv/json`, med gamla/nya basadresser, hela åttabitarsdifferensen, källkodens giltiga indexdomän och disposition. I **55** av 58 fall ligger alla nytillkomna sidgränsindex utanför dokumenterad giltig domän. **Tre fall ligger inom giltig domän** och orsakar faktiskt en extra CPU-cykel:

| Indexed instruction | Giltigt index med +1 | Konsekvens och bevis |
|---|---|---|
| `LDA TitleLeftPF2,Y`, `$FEFC → $FEFE` | Y=2,3 i titelns Y0..6 | 5 i stället för 4 CPU-cykler. Riktig TIA-bus: 64 efterföljande PF-skrivningar förskjutna **+3 färgklockor** över 16 titelrader, se avsnitt C. |
| `LDA GeoMapHi,X`, `$FDFD → $FDFF` | room X=1,2 | Native Gopher-instruktionssteg visar **4→5** CPU-cykler. Rumsinläsningen sker under VBLANK, före RIOT timer-väntan. |
| `LDA RoomStoneY,X`, `$FAFA → $FAFC` | room X=4,5 | Native Gopher-instruktionssteg visar **4→5** CPU-cykler. Samma VBLANK-fas; X1/2 och X4/5 är disjunkta, så dessa två nya kostnader summeras inte i samma rumsinläsning. |

Till exempel `TitleRightPF1,Y` får nya sidgränsindex Y9,10, men titelrutinens källkod håller Y i 0..6; **ingen ny giltig titelpenalty** där. Alla 16 aktuella blank-/uggla-/symbol-/markörspriteadressbaser ligger inom sin ROM-sida även med högsta giltiga rowindex; `SpriteRowIndex,X` i den ordinarie stemloopen använder **X=9..2 → Y=7..0** och terminal X=1 → Y=8 (blankbyte). Ingen ny `(zp),Y`-pagecross i dessa 16 tabeller för giltiga Y0..8. Indexerade writes har inte behandlats som om de vore read-penalties. Allt detta är **villkorat av de legitima 0..14 rumsindexen, 0..39 key, 0..3 riktningar, oförstörd pekar-RAM och ingen obehörig bankväxling**.

Konsekvens/fortplantning: De nya room-load-cyklerna föregår timerbaserad väntan i VBLANK och är i **19 652-bildrutors nytt fullt Stella-spår** absorberade utan ens en framebuffer- eller PCM-avvikelse. Detta är inte en formell gränsbevisning av alla tänkbara timerfasförhållanden. Uppdaterad `Stem13` `$F90E` har oförändrad ordinarie villkorlig **75/76**-budget per rad; sprite-/tabellsidgränser och tillåtna Y ändrar inte den budgeten. Terminal X=1, PrepareOwlFrame `$FA4B`, kronrader, Top16, `HUDCoarseDelay` `$FF87`, samtliga kritiska F6-hotspots testade inom mätt scope. En övergripande all-path-deadline är fortsatt INCONCLUSIVE.

## C. Titelbilden: 64 verkliga TIA-bussförskjutningar adjudicerade

Genuin Gopher2600 `TRACE STRICT + ONTRACE TV,CPU` i ett giltigt **controller-naturligt titelscenario** gav 408 TIA-registeraccesser per ROM och identisk ordning/datatyp. **64** accesser flyttas exakt **+3 color clocks** (en 6507 CPU-cykel), alla på scanlines **84–99**, fyra per linje: första PF2, därefter PF0/PF1/PF2 för den omritade högra halvan. Busspårens `CL` är relativt HBlank/slutet före synlig start; fysisk rasterfärgklocka = CL+68. Vi redovisar verkligt skriven registerposition, inte instruktionsstart som om det vore busskrivning.

| Write/segment | Ny observerad CL relativt synlig x=0 | När datat måste finnas | Uppmätt tidsmarginal |
|---|---:|---:|---:|
| Första PF2 (vänstra halvan) | −2 | Före PF2-pixlar på vänstra delen, från x48 | 50 color clocks |
| PF0 högra halvan | 43 | x80 | 37 color clocks |
| PF1 högra halvan | 64 | x96 | 32 color clocks |
| PF2 högra halvan | 85 | x128 | 43 color clocks |

**Samtliga deadlines i denna matris passeras med positiv marginal** inom dessa 16 giltiga titelrader. 64 skrivningar är alltså **reella osynliga timingskillnader** i uppmätt scope, inte full timingidentitet. Våra separata nystartade autentiska Stella-processer RC1-A, RC1-A2 och LAB-B har därefter fångat hela originalupplösningen **160×228** på titel-frame 0,27,28,29,30,60,180,400: **0 olika pixlar i alla åtta A/A2- och A/B-par**, inklusive frame28 med uppmätta bussförskjutningar. Den fulla kampanjen nedan har också noll framehash-differenser. Ingen synlig regression bekräftas. Komplett 64-raders deadline-ledger och äkta PNG finns i `ANALYSIS/TITLE_64_TIA_REAL_BUS_DEADLINES.json` och `EVIDENCE/TITLE/STELLA_1X_PIXEL/`.

## D. Funktion/CPU-status/stack – reell förbättring och korrekt avgränsning

Oberoende programflödesanalys på båda verkliga native-bankuppsättningarna ger **RC1 2 541 kontexttillstånd/max 5 simultana JSR** och **LAB 2 565 kontexttillstånd/max 4 simultana JSR**. Branschforkning är konservativ; tillstånden betyder *analysens nåbara kontrollkontexter*, inte antal empiriskt besökta gameplaystates. I analysens giltiga anropsflöde finns ingen sjätte respektive femte JSR och ingen ytterligare PHA/PHP/pushväg. Reset initierar SP `$FF`, ingen extra RIOT-RAM. Deklarerade 118 byte ligger i `$80..$F5`. RC1 använder vid fem JSR faktisk speglad stack `$F6..$FF` och ingen marginal. LAB använder högst `$F8..$FF`, med **`$F6..$F7` som två oanvända reservbyte**. Dessa är reserv, **inte nya spelvariabler**.

Den tidigare kritiska naturliga joysticksekvensen i I-01 (bildruta **124**) återskapades i nya native Gopherprocesser utan POKE: RC1 stoppar före `F4AE JSR DecodeKey` med SP `$F7`; faktisk CPU-buss skriver returbyte till `$01F7` och `$01F6`, slut-SP `$F5`. LAB går vid motsvarande **`F49B DecodeKeyInline`** redan med SP `$F7` och gör **inga motsvarande stackskrivningar**. Båda fortsätter korrekt; `$01F5` bevaras. Loggarna avser **faktiska bussaccesser**, inte bara CPU-registret SP. Anropskedjor i `ANALYSIS/CFG_*` samt `EVIDENCE/STACK_BUS`.

Därtill kördes **åtta separata genuine Gopher decoder-gränsfall** workKey 0,4,5,9,10,34,35,39, med riktad injektion av endast key i en genuint uppnådd avkodningsstart. A/X/Y/processorstatus/SP efter gemensam fortsättning, `workX/workY`, och lokal cykeltid matchar; RC1 har de gamla inaktuella returadressbyten i F6/F7 medan LAB inte skriver dit. HEALTH:s 983 040 interpreterfall är **utvecklarens** bevis och räknas inte som nya verifierarkörningar. Statisk instruktionsemantik: `JSR`/`RTS` ändrar stack/PC men inte statusflaggor, `NOP` ändrar inga flaggor, och samma byteavkodningskropp utför samma statusändrande instruktioner vid giltigt key 0..39 med `CLD` och inget giltigt `SED`-flöde. `P`-kontrakt utanför dessa antaganden förblir villkorat. Normaliserade returadresser och inaktuella stackbytes är avsiktligt olika, inte spelstatusfel.

F6: I fyra nya native Gopher-brytpunktsscenarier valdes bank0 naturligt, bank1 två gånger och bank2 en gång diagnostiskt (ingen POKE för bank0, `FORCED_RAM_DIAGNOSTIC` för övriga). Hotspots `$FFF6/$FFF7/$FFF8` väljs via fasta `$FF90`, retur `$FFF9/$FF99` återställer bank3. **SP `$FB`, alla 10 speglade `$F6..$FF`-byte före/efter och retur-PC** matchade i varje test. Bank0–2/trampoliner och resetvektorer är byteidentiska med RC1. Ny LAB native Gopher-kampanj passerade dessutom alla tre akter; det är naturlig spelomfångstäckning, men ett nytt fullständigt bank1-bussövervakningsspår över hela kampanjen är **NOT_RUN**.

## E. Nya verkliga raster- och gameplaytester

| Test | Eget faktiskt observerat utfall | Status |
|---|---|---|
| Native DASM, två rena byggen vardera | 4/4 byggresultat exakt SHA, 4×4096-byte banker | **PASS** |
| Stella controller-only från titel | 15/15 distinkta rum, coda, återgång titel; **19 652** bildrutor | **PASS_BOUNDED** |
| Gopher native controller-only från titel | 15/15 rumsvinster, coda/titel; **19 780 `STEP FRAME`**, **278 separata TV-observationer alla 262**; exitkod0 | **PASS_BOUNDED** |
| Full Stella A1/A2/B-differential | **19 652/19 652** rå framebuffer-SHA identiska; 517/517 loggade tillståndsövergångar identiska; **20 594 248** int16 PCM-värden identiska; PCM SHA `ac35c19bfb388fe83699d18f0bc47d713a89e75fe8c7c191a8deb951eba56d3b` | **PASS**, strikt denna controllersekvens |
| Naturlig högerkant x9 | RC1 262, LAB 262; negativa kontroller PR47 **263**, HEALTH avsiktligt sen-BCS **263**, samma controller | **PASS_BOUNDED** (sensitivt orakel) |
| Riktade CPU/TIA-frames | Ursprungliga Gopher realregisterpositioner i titel, normal I-01, II-02, III-03 med Presence/echo och HUD. Ingen extra full scanline; 64 titel-positionsdifferenser separat klassade | **PASS_BOUNDED** |
| Samma rad S3-A/S3-B | II-02, II-04, III-02, III-05 × båda polariteter = **8 jämförda par/16 original-Gopher-körningar**, 377 event/par och samtliga 262, inga betydelsebärande PF/GRP/COLUP-position-/värdeavvikelser i dessa forcerade rum | **PASS_BOUNDED DIAGNOSTIC** |
| Ordinarie Stem13/spriteindex | Samma giltiga Y0..7, terminal Y8, inga nya sprite-table page-crosses; **75/76** för ordinarie loop | **PASS_CONDITIONAL** |
| SELECT efter vinst | **15/15** naturligt vunna rum → SELECT + FIRE stannar i samma rum utan oförtjänt rumskip | **PASS_BOUNDED** |
| Avvikande FIRE/SELECT/återlösning | **15/15** separat startade LAB-Stellaprocesser, 19 140 nya frames: FIRE efter förflyttning till x9, bevisad SELECT-room-reset med `introFrames=107`, sedan normal lösning och ny vinst | **PASS_BOUNDED** |
| Kausala FIRE-utelämningar | **15/15**; ingen vinst inom ursprunglig vinstframe +360, inte globalt omöjlighetsbevis | **PASS_BOUNDED** |
| Idle | **15×36 000 = 540 000 genuina Stella-frames** från naturligt controller-nådda rumstarter; varje frame kontrollerad, 0 passiva segrar | **PASS_BOUNDED** |
| FRI SKOG, styrd kontrollserie | **50 010** genuina frames, 49 996 i mode4, inga olovliga modebyten, 7 703 controllerintervall | **PASS_BOUNDED** |
| FRI SKOG utan SELECT/RESET | Separata **27 000** genuina frames; beat **255→0** vid frame **18 484** med fortsatt mode4 | **PASS_BOUNDED** |
| U3 grafiskt | Ny original Stella controller-replay: **12/12 riktning×vingfas**, 1× PNG per naturligt vittne; samma ROM-spritebytes och no-page-cross | **PASS_BOUNDED** |
| Markörstatus | Naturligt neutral, godkänd, nekad i spelkampanjen; naturlig intercepted i III-04 genom ny FIRE vid beat1 och aktiv Presence, **två separata kallstartsprocesser**, samma frame **16 637** och **0 pixelavvikelser** i tre originaljämförelser. Ingen ROM-POKE | **PASS_BOUNDED** |
| Samma-rad naturliga polariteter | 7 naturliga rum/polaritet-vittnen på 4 avsedda rum (ett rum får bara en polaritet i normal replay); övriga diagnostiska | **PASS_BOUNDED**, inte natural full8 |
| Ljud, titel/campaign/act/coda | Äkta Stereo TIA PCM, strikt A/A2/B likhet ovan, igen utan digital retuschering | **PASS** för vald sekvens; mänsklig lyssning NOT_RUN |
| All-path raster/TIA/sprite-latch | Ingen genomgripande register-/bank-/stackproof för varje tänkbar naturlig tillståndskombination | **INCONCLUSIVE** |
| Fysisk Atari 2600, RetroN77, mänsklig kallspelsgrupp, mänsklig lyssning/konstacceptans | Ingen faktisk fysisk eller mänsklig kontroll genomförd | **NOT_RUN** |

Verifieringen av normal x9 är särskilt stark som **negativ kontroll**: både PR47 och en avsiktligt felaktig sentiming-variant gav genuin 263-linjersframe medan båda avsedda ROM gav 262. Diagnostiska RAM-POKE-scenarier används aldrig som påstående om naturligt controller-nåbart tillstånd. 278 TV FRAME-kontroller under 19 780 STEP FRAME är **inte 19 780 självständigt undersökta rastervärden**.

För 5 riktade Gopher-A/B-bussfallen innehöll den första parserns `same_tia_register_order_values=false` en falsk varningsindikator: exakt en ändrad **skrivdata-byte till WSYNC** i varje fall. **WSYNC ignorerar datavärdet**. Alla andra betydelsebärande TIA-registers värden, ordning och fysiska skrivpositioner matchade. Vi har **inte raderat** dessa råskillnader: original och korrekt normaliserat orakel i `ANALYSIS/FOCUSED_TIA_BUS_WSYNC_VALUE_ADJUDICATION.json`. TIA-WSYNC-värdet är inte ett ljud-/pixelproblem.

## F. Oberoende testverktygsfel, negativa resultat och begränsningar

1. Original verktygsreplay kom med två separata emulatorinstanser i samma OS-process i ett tidigt grafiktillståndstest, vilket gav falskt olika (och i en instans frusna) PNG. **Dessa bilder avvisades som orakel** och arkiverades märkt `INVALID_SAMEPROCESS`. Kallstartsreplay utfördes i två separata OS-processer och tre jämförda bilder per körning blev pixelidentiska; en verifierbar `ackType=3` vid frame16 637 i båda. **Harness-problem, inte ett ROM-fel.**
2. Första 15-rums återhämtningstestet slog SELECT bara en `retro_run`, trots att controllerändringar aktiveras på efterföljande callback; `introFrames` förblev ca 43, alltså hade rumreset inte faktiskt testats. Oraklet korrigerades till två frames SELECT + bevisad `introFrames=107`; **hela 15-rumsmatrisen kördes därefter om**, 15/15 PASS. Första pilotprovet räknas inte som PASS.
3. Full körning av ett separat gammalt Gopher-prefix till akt II avbröts på tidsgräns; **NOT_COMPLETED**, inte en ny naturlig bank1-mätning. Befintlig ny original-Gopher-kampanj på LAB_BEST har 15/15 spelprogression men ingen full bank1-busstrace.
4. Den äldre strikta RC1–PR44-ljudpariteten var numeriskt FAIL (50 samplevärden), men detta är **historisk annan jämförelse**; LAB–RC1:s egen fulla PCM-ström är identisk i vår nya körning. Inget påstående om mänsklig ohörbarhet.
5. Alla analyser har tillståndsgränser: giltiga keys 0..39, rum0..14, 8-bit RIOT enligt de faktiska källvariablerna, fungerande F6 och ingen godtycklig RAM-korruption. Det går inte att uppnå universell 76-cycle/TIA-beam-säkerhet genom fler slumpbilder eller genom att enbart säga att 262 linjer finns. Måltest som återstår om MAIN kräver strikt matematisk release-proof: modellera samtliga legitimt samtidiga Presence+FIRE+echo+terminalt HUD med state-aware CPU/busspositioner och timer-överskridanden. Det är **en separat mer omfattande verifieringsinsats**, inte automatiskt mandat här.

## G. Slutlig teknisk bedömning och de tolv MAIN IV-frågorna

1. **Rätt identitet/bygg?** Ja. RC1 och LAB två rena native builds vardera, identiska mot levererade respektive ROM. Fryst PR49 orörd; HEALTH-dokumentgrenen är inte experimentkällans commit.
2. **Är diffen bara inline + NOP?** Ja i `rom/src/main.asm`, verifierad mot exakt frozen RC1; +2 bytes bank3. De 2 547 byteoffsetändringarna beror till stor del på följande omlokalisering.
3. **Ändrade branch/index/page crossing?** En tagen branch −1 cykel. 58 ändrade index-domänmönster, men bara tre nya +1 inom giltiga index (titel Y2/3, room index1/2 respektive4/5). Alla 58 är inventerade, sidgränsstyrda sprites granskat. Detta är villkorad source-bound-analys, inte arbitrarisk RAM.
4. **Buss/beam?** Titelns 64 verkliga +3-clock-accesser ligger med ≥32 clock marginal till sin aktuella högersidessegment-deadline, 0 pixeldifferens. Rumsinläsningscykler native-mätta, och full kampanjvisning, HUD/x9, Stem/terminal, Presence, Same-row, PrepareOwlFrame kontrollerade inom beskriven domän. All-path fortfarande INCONCLUSIVE.
5. **Maxstack?** Modellmax 5→4 JSR. Fyra faktiskt nått på legitim I-01 frame124, LAB-SP som lägst F7 där, inga femte JSR-returbyte; `$F6..$F7` fria i giltig statisk anropsgraf, utan extra variabler. 2-byte marginal, ingen större marginal.
6. **Status/decoder?** 8 genuina Gopher gränskeys + source opcode proof; identiska meningsbärande A/X/Y/flags, scratch, lokalklocka inom giltig decimal-klar domän. Inaktuella F6/F7-stackbyte får skilja.
7. **Bankning?** F6 bank0/1/2 riktat PASS_BOUNDED med returer, bank3 reset/trampoline oförändrad och 15-rum Gopher klar. Full naturlig instrumenterad bank1-trace saknas.
8. **Stella/Gopher 15/15?** Ja, 19 652 Stella callbacks + 19 780 Gopher STEP FRAME, med 278 rasterfrågor. Idle 540 000, FRI 50 010 plus 27 000 wrap, återhämtning 19 140, etc redovisas separat utan dubbelt TV FRAME-räknande.
9. **Full frame/PCM?** Ja, tre isolerade Stella-körningar (A/A2/B): exakt 19 652 framebuffer-poster + 20 594 248 int16. Dynamiska titelbus-accesser skiljer trots identiska pixlar/PCM; en ny fullständig bus-tidslinje för alla frames krävs för global bus-identitet (vilken inte påstås).
10. **Fixar/canon?** 15 kausala omtag, 15 SELECT-after-win, 15 divergerande SELECT-recovery, naturliga fyra markörer, U3 12/12, 4 same-row tvåpolaritetsdiagnostiska par, Närvaro/eko inom scope PASS_BOUNDED.
11. **Finns produktblockerare?** Inget nytt bekräftat eller två gånger reproducerat LAB-specifikt produktfel. Globala timingrester, human cold play, original Atari/RetroN och sensorisk konst/ljud bedömning är ännu öppna risker. Forcerade tillstånd är testscenarier, inte naturliga regressionsfynd.
12. **Är stackvinsten värd ROM-kostnaden?** **Ja inom utförda tekniska tester**: +2 verkliga stackreservbyte och 4-byte bank3 ROM-luckor kvar, med uppmätt ofarlig titelbus-förskjutning, två indexkostnader vid room load och ingen output-/spelregressionsavvikelse i utfört scope. Rekommendera **separat självständig PACHINKO på exakt LAB_BEST-SHA** om MAIN/användaren beslutar fortsättning. **Behåll RC1 som officiell fryst produktreferens**. Ingen RC2-promotion, merge, release eller ny optimering genom denna rapport.

### Formell disposition

**`LAB_INDEPENDENT_DELTA_PASS_BOUNDED` / `GLOBAL_ALL_PATH_TIMING_INCONCLUSIVE` / `EXPERIMENT_ONLY` / `RC1_FROZEN_UNCHANGED` / `HUMAN_AND_PHYSICAL_NOT_RUN`**.

Den här verifieringen har uppfyllt sin beställda avgränsning med faktisk native kod, riktade negative-oracles och återuppspelning. Kandidaten är tekniskt rimlig att **överlämna till ett separat kommande Pachinko-beslut**, men inte att ensidigt anta som RC2 eller släppa kommersiellt. Inget nytt implementationsmandat har tillkommit.