# MELLANRUM: SKOGEN SOM LYSSNAR — RC1 INDEPENDENT VERIFICATION

Datum: 2026-11-24. Roll: **VERIFICATION**. Uppdragsgivare: MAIN IV, [Issue #50](https://github.com/Odourman/mellanrum/issues/50). **Övergripande slutsats: INDEPENDENT_VERIFICATION_INCONCLUSIVE för ovillkorlig teknisk release**, trots omfattande avgränsade PASS. Inget nytt bekräftat, releaseblockerande RC1-produktfel har hittats inom utförda tester. PR49 lämnas Draft, ingen merge/tag/release, ingen ändring av produktkod/ROM. Pachinko/human/physical hardware är separata grindar.

## 0. Exakt identitet, proveniens och miljö

- Fryst [Draft PR49](https://github.com/Odourman/mellanrum/pull/49) HEAD `d013a0f82621d46ad12674a4a8e944bf005cd9c3`, ursprungligt **produktcommit** `7b400ad8678e8341a26f65cc757b1eb762654c83` (senare HEAD har workflow-steg). RC1-källans `rom/src/main.asm` Git blob `6224bc13a17eb45d898118e72f6fc15a7586267c`.
- Faktisk GitHub/Drive-/DASM-ROM: `rom/bin/MELLANRUM_16K_NTSC_F6.bin`, **16384 B standard NTSC F6, 4×4096 B**, Git blob `afce29944cce726fa0f935ed3104abc954e7e6da`, full **SHA256 `456005ed691860b32c44b79f2a71666f622b005f5a798eadf9b549c59cff13bd`**.
- Bank0 SHA256 `4f1fefc7513d5c0aef2d1c2a406b77975e59fc60e0a3361fa34455b4c669c49f`; bank1 `8d49d78a7f7ea98d1638693767de146b54b7b97673eb5f077fbf9c0554e3a1e8`; bank2 `6b82511ba23726be41aa5f7a4e8c2555f5e039ee6fc2ec6a1e0774117cfffbfc`; bank3 `46855dddaefd3de616e41e61f9e0fc6c921d16983800a2dd514239df610080cb`.
- Själv nedladdad original Drive-ROM och **FINAL** developer ZIP: arkiv **46 647 172 B**, **SHA256 `293b5db45e126993695aa0e59c5c193b527ef5d5cbb456d0a0bacd89c5b9ab7c`**, CRC PASS, **1201 filer/1200 manifestposter, 1200/1200 SHA256 PASS**, inga saknade eller obevakade poster; både underliggande SHA256SUMS finns med och deras refererade filer har verifierats. Ingen förväxling med äldre ZIP-hash i PR-beskrivning. En separat Gopher CI-ZIP saknar ROM-binärram; detta redovisas, inte gissas.
- Native DASM **2.20.14.1**, lokalt arkiverat originalkörbart verktyg SHA256 `cfb23732297a4fe1c8d4a78d44206037d97733aedb2772503bbf029a4aa91291`. **Två helt nya separata byggkataloger** `buildA`, `buildB`: fyra banker och full ROM byteidentiska med varandra och Drive/GitHub/CI. Listnings-/symbolfiler och byggloggar bevarade. Separat verifieringsgren har dessutom egen tvåbygges-GitHub Actions **[run #45466845934](https://github.com/Odourman/mellanrum/actions/runs/45466845934) SUCCESS**, med bevarade artefakter i [artifact #14954213597](https://github.com/Odourman/mellanrum/actions/runs/45466845934/artifacts/14954213597). Den enda branchändringen är verifierings-workflow; produktfilerna är byteidentiska.
- Äkta Stella **libretro `8.0_pre 8dd5600`**, core SHA256 `2130ed1153cef66ef3f34bf9063f675f1f3342bc18320eb9ae5101743e3042df`; native Gopher2600 `unreleased`, source pin `74c544203378c1448a33c29bc8b4586079b050f4`, ELF SHA256 `7b12dff57fcb73154122d2477f35d9c8ae8b344649bc0faa8ff6f5663c70470b`.

## A. Oberoende verklig gameplay och konsolregression

- **Stella 15/15 PASS_BOUNDED SOURCE_GUIDED.** 19 652 original emulatorframes, 295 inputintervall från en historiskt känd controller-witness. Körningen utfördes i egen ny emulatormiljö, **utan POKE**. Alla rum nåddes/vanns ordning 0–14, coda→titel och FIRE startar ny kampanj. Varje vunnet rum sparades **från verkligt controller-nått tillstånd**, oberoende SELECT-hårdvaruknapp och därefter FIRE: **15/15 korrekt samma rum/mode1, 0/15 falska övergångar**, RC1-korrigering A **PASS**. Rålogg `emulator_RC1/independent_result.json`; egen medföljande 15-rumskontaktbild och bildrutor.
- **SELECT efter avvikande input, återhämtning och rumsomspelning 15/15 PASS_BOUNDED**, återhämtning från original sparade legitima rumsstarter; ingen POKE. Rådata `recovery/`.
- **Stella idle 15×36 000=540 000 frames PASS_BOUNDED**, 0 passiva rumsvinster. Nya emulatorprocesser från naturligt controller-nådda, serialiserade room-start states, observerat **varje** frame, no input under idle. Rådata `idle/`.
- **15/15 kritiska kausala FIRE-utelämningar PASS_BOUNDED** med samma normalrums-vittne och ett individuellt valt borttaget FIRE, följt till original vinsttid+360 frames; ingen vinst inom horisonten. Inte bevis för ingen senare alternativ lösning. Rådata `causal/`.
- **HUD x9 regression B PASS i Gopher2600 med riktig controller, ingen POKE**: RC1 10/10 riktiga x0–9 + FIRE-kontroller gav 262/262 på de två observerade fulla frames per kolumn. Samma x9-controllersekvens på oförändrad PR47 gav **263/263**, reproducerat fel i fryst föregångare. Exakt `hud_tests/` innehåller inskickade inputkommandon, logs och RAM-värden; `hud_cpu_RC1.json` visar **4241 CPU-instruktionsgränser, 201 verkliga WSYNC, 184 synliga WSYNC, 0 överhoppade synliga** i RC1 x9. PR47 x9: 4250 instruktioner, 201 WSYNC, 183 synliga; 263 totallinjer. Den extra PR47-linjen är inte nödvändigtvis en synlig WSYNC-skipp. Inte alla extrema respons-/Present/samtidig FIRE-varianter controller-nådda.
- **FRI SKOG PASS_BOUNDED**: 50 010 egen Stella-bildrutor (seed 260024) med riktig Difficulty B, joystick/FIRE/SELECT/difficulty-toggle, 0 ogiltiga spellägen; 27 000 ytterligare frames utan SELECT/RESET observerade beat **255→0 vid bildruta 18 484** och inga mode-fel. Original input/poll/PCM-loggar under `fri_50000/`, `fri_wrap/`.

## B. Full native Gopher2600, per-frame NTSC, bank och stack

- Ny separat native Gopher HEADLESS-process med känt, `SOURCE_GUIDED`, **controller-only** fullkampanjspår (`gopher_full/input_controller_source_guided.txt`, 40 533 kommandon, **19 780** verkliga `STEP FRAME`, ingen POKE). **Exit 0**. Full stdout `gopher_full/stdout.log`, självständig parser `independent_gopher_full.py`, resultat `gopher_full/result.json`.
- **20 057/20 057 fullständiga TV FRAME-observationer efter boot exakt 262 scanlines**. En första **partiell boot-bildruta med 20 scanlines** är separat klassad, inte felaktig full bildruta. Totalt 20 058 TV-avläsningar (278 extra kontrollpunkter efter step). Detta är ett **PASS_BOUNDED för exekverade frames**, INTE automatiskt global worst-case 76-cykel-säkerhet på samtliga alternativa vägar.
- Riktiga F6-hotspots i hela spelspåret: `$FFF6` **5 600**, `$FFF7` **4 711**, `$FFF8` **7 879**, tillsammans **18 190** score-bankval; `$FFF9` **18 191** returaktiveringar med **en extra reset/boot**; ingen saknad återgång i det observerade normala flödet. **F6 PASS_BOUNDED**. Trace guard `WATCH STRICT WRITE 0x01F5`: **0 misstänkta stackskrivningar** under verklig full kampanj. Giltig RAM-kedja max SP $F5, RIOT RAM spegling `$01F6–$01FF→$F6–$FF`.
- Ny **RC1-specifik** statisk originalbank/ROM/DASM-anrop- och återgångsanalys med konservativt båda grenutfall, fyra bankresetvägar, 2 541 nåbara (bank, PC, call-context) tillstånd, max **5 samtidiga JSR**, 0 parser-rapporterade okända returer/ogiltiga instruktioner, inga nåbara andra stack-push. 118 byte variabler `$80–$F5`, tio byte returstack `$F6–$FF`; **STACK PASS_CONDITIONAL för giltig ROM/data/kontrollström**, utan reserv. Ingen garanti vid korrupt RAM, onormal cartridge-hårdvara eller framtida ändring. Fil `static_cfg_RC1.json` + `static_stack_RC1.py`.
- **Globala alla-kodvägar/cykler-76 och TIA-kerneltiming: INCONCLUSIVE.** Viss faktisk x9-instruktionsspårning och all-frame 262 finns, men allPath register-/beamindex-/pagecross/terminal-Stem13/PrepareOwlFrame/Presence-FIRE-eko är inte formellt stängda. 262 line totals är inte ett värstafallssäkerhetsbevis. Specifik känd normal Stem13 75/76 från utvecklare får inte automatiskt påstås vår fullständiga allPath-beräkning. **Ny heltäckande Stella CPU debugger run: NOT_RUN.** Original fysisk NTSC Atari: NOT_RUN.

## C. Grafik, mask, symboler, markörer

- Egen binärmaskgeometri: **12/12** faktiska U3 riktning×ving-matriser är korrekta enligt B0/B1/B2, mirroring och 90° rotationsregler, med DOWN B2 slut `7C`. Under **ny verklig Stella fullkampanj** observerades **12/12 faktiska U3-grafikindex med motsvarande senaste lyckade rörelseriktning**, 226 förflyttningar (51 upp, 116 höger, 48 ned, 11 vänster), 19 stationära beats och 7 stenankomster, 0 observerade avvikelser. Detta ersätter inte tester av alla framtida AI-motfakta. Rådata `u3_masks.json`, `visual_runtime_summary.json`, `visual_independent/` (12 original 1x PNG).
- Same-row II-02, II-04, III-02, III-05: **4/4 jämförda polaritetspar i faktisk Stella-rendering**, godkänd S3-B mask `08 0C 0E FF FF 0E 0C 08` oförändrad, 28 synliga färgade pilpixlar, 18 stenpixlar omfärgade, ingen oavsiktlig pil-diff. Dessa polaritetspar har **RAM-POKE efter controller-nådda room starts: DIAGNOSTIC, INTE två naturliga spelarlösningar**. `symbol_pairs/` original 1x PNG och JSON.
- **Fyra visuellt skilda markör-ROI** i äkta Stella 1× bilder, från jämförbart room-start: **4/4 PASS_BOUNDED DIAGNOSTIC** genom RAM-tillståndsstyrning efter controller-nådd rumsstart. Naturlig aktivering av alla fyra former med endast joystick/FIRE har **NOT_RUN** i denna specifika jämförande matris; mänsklig läsbarhet **NOT_RUN**. `markers/`.
- Äkta `emulator_RC1` pixeljämförelse med levererat developer-video-snapshot-arkiv gav **101/116 råbild-PASS**; **15 room-win-frame** avvek efter att detta test hade förgrenat emulatorn för SELECT-regressionsprover, en känd bild-återställningstestkonfounder. Dessa 15 mismatch klassas INCONCLUSIVE för exakt utvecklarbildparitet (inte konstaterat ROM-fel); nytt oberoende RC1-vs-PR47 jämförelse i **två fullständigt separata OS-processer** gav **19/19 checkpoint-png-pixlar och 118/118 periodiskt provtagna framebuffer-SHA identiska**. Dessa nya jämförelser utgör giltigt separat regressionsbevis.
- Själv genererad 15-rums autentisk Stella PNG-kontaktbild, 1× originalmasker och H264/AAC video (nedan). Trädens godkända konstnärliga form ändras inte. Ingen fullständig subjektiv mänsklig konstnärlig bedömning: NOT_RUN.

## D. Autentiskt ljud, video och RC1/PR47/PR44 regression

- Färska **separata OS-processer** för Stella RC1, PR47, PR44 med identiska 19 652 frames SOURCE_GUIDED controllerinputs. PCM **20 594 248 int16 värden** per körning, verkliga 31 440Hz TIA-samplar. **RC1 kontra PR47 0/20 594 248 differenser** och identisk PCM SHA256 `ac35c19bfb388fe83699d18f0bc47d713a89e75fe8c7c191a8deb951eba56d3b`, **PASS** för exakt gemensam kampanjinput. Samma 19/19 snapshot- och 118/118 sparse framebufferhashar identiska. Rå-WAV `fresh_RC1/tia_audio.wav`, `fresh_PR47/tia_audio.wav`, `fresh_PR44/tia_audio.wav`.
- **RC1 kontra PR44 strikt PCM-identitet FAIL:** 50 av 20 594 248 int16-samples skiljer, 13 bildruteindex, maximal absolut diff 5 957 och RMS 4,72954088547. 13 matchade 1s jämförande rå-WAV-par i `audio_comparison/`. Detta är inte i sig bevisad hörbar kvalitetsbrist; **mänsklig lyssning NOT_RUN**, ingen ogrundad ohörbarhetsclaim.
- Verklig egen 3000 frames Stella H264/AAC inspelning (`video/MELLANRUM_RC1_INDEPENDENT_STELLA_TIA_50SEC.mp4`, 640×456 nearest neighbor, FFmpeg ffprobe 49,984s, 2999 muxade videoframes pga AAC -shortest), samma-callback riktig tvåkanalig TIA-ljud; **PASS_BOUNDED för autentisk 50s capture**, ej självständigt inspelad fullspels-MP4. Original 1× PNG från samma SHA medföljer.
- **Testmiljöfel korrigerade, inte ROM-fel:** ett preliminärt script som återinitierade olika libretro-ROM i samma Pythonprocess gav felaktigt mörka PR47-bilder; alla giltiga PCM-/PNG-regressionspåståenden baseras på tre separata, nystartade OS-processer. En första HUD-råparser feltolkade pre-FIRE `fireX`; korrigerad testassertion och omkörning gav 10/10 riktiga kolumner. Dessa ogiltiga äldre harness-protokoll ingår inte i slutligt PASS.

## E. Samlad statusmatris

| ID | Kontroller | Verifieringsstatus | Avgränsning |
|---|---|---|---|
| RC1-I | SHA, Drive ZIP CRC + 1200 manifest, Git blob, 4 bankhash | **PASS** | Byte-/källdetaljer ovan |
| RC1-B | Två nya native DASM-byggen; separat GitHub Actions | **PASS** | Native produktparitet, ej hårdvarusäkerhet |
| RC1-S | 6507/RIOT max JSR=5, 0 write-under guard | **PASS_CONDITIONAL** | Giltig source/data-kontrollström |
| RC1-F6 | 18 190 faktiska anrop och 18 191 bank3-hotspots | **PASS_BOUNDED** | SOURCE_GUIDED full Gopher-kampanj |
| RC1-R | Full kampanj all-frame 262, plus x9/PR47 kontroll | **PASS_BOUNDED** | 20 057 av 20 057 fulla frames |
| RC1-CYCLE | Samtliga nåbara 76 CPU-cykler inkl terminal och Presence | **INCONCLUSIVE** | Fortfarande huvudgrind |
| RC1-CAMPAIGN | Stella + Gopher real controllers, 15/15 coda/title/restart | **PASS_BOUNDED** | SOURCE_GUIDED, ej blind lösning |
| RC1-SELECT | 15/15 SELECT-after-win, ingen falsk övergång | **PASS** | Controller-nått äkta vinsttillstånd |
| RC1-HUD | 10/10 x0–9 RC1 262; PR47 x9 263 | **PASS** | Bounded controller/regression |
| RC1-IDLE | 15×36 000, 0 passiv win, varje frame | **PASS_BOUNDED** | 540 000 frames, naturliga starts |
| RC1-CAUSE | 15/15 nödvändiga FIRE utelämnade | **PASS_BOUNDED** | Vinsttid+360 testhorisont |
| RC1-RECOVERY | 15/15 SELECT/omspelning | **PASS_BOUNDED** | Source-guided restväg |
| RC1-U3 | 12/12 masker verklig Stella, 226 moves | **PASS_BOUNDED** | Inget fullständigt AI-branchbevis |
| RC1-SYMBOL | 4/4 same-row polaritetspar och pilmask | **PASS_BOUNDED** | DIAGNOSTIC POKE för pol0/1 |
| RC1-CURSOR | 4 olika original 1× markörer | **PASS_BOUNDED** | DIAGNOSTIC forced ack states; natural all4 NOT_RUN |
| RC1-FRI | 50 010 frames + 27 000 beat wrap | **PASS_BOUNDED** | Verklig Stella-konsolinput |
| RC1-PCM47 | RC1=PR47 20 594 248/20 594 248 | **PASS** | Samma controller och core, isolerade processer |
| RC1-PCM44 | RC1=PR44 strikt PCM jämförelse | **FAIL** | 50 differenser; ej konstaterat hörbart fel |
| RC1-VIDEO | 50s original TIA/H264 same-run | **PASS_BOUNDED** | Inte hela spelet |
| RC1-ART | Mänsklig cold-play, musik, konstnärlig acceptans | **NOT_RUN** | Användarens separata beslut |
| RC1-HW | Fysisk original-Atari/RetroN77 | **NOT_RUN** | Emulatorer ersätter ej fysisk provning |

## F. Rekommendation till MAIN IV

**INDEPENDENT_VERIFICATION_INCONCLUSIVE** för fullständig teknisk slutattest/release. Den exakta RC1-ROM:en är reproducerbart byggbar och de två avgränsade Final Polish-felen är självständigt rättade i verklig emulator; 15 rum, idle/kausalitet, F6/stackförutsättningar, godkända viktiga pixelmasker, FRI och kampanjljud stöds av riktiga nya resultat. **Inget nytt demonstrerat releaseblockerande produktfel i RC1 inom dessa prov**, men global worst-case 76-cykel TIA/6507 under ALLA nåbara vägar återstår; fullständig naturlig fyrmarkörmatris och mänsklig förstagångs-I05/musik/art/physical kräver separata bevis. PR44 strikt PCM-likhet är fortfarande FAIL som numerisk likhetskontroll, men inte fastställt ljudproduktfel. Föreslå inte en ny ROM-patch utan konkret reproducerat fel: varje byteändring ändrar SHA och kräver ny Verification/Pachinko. Behåll Draft PR49, **ingen merge/tag/release**, MAIN IV och användaren äger grindbeslut.

## G. Reproduktion och integritet

Fullt separat ZIP `MELLANRUM_RC1_INDEPENDENT_VERIFICATION.zip`, originalkandidat 16 384 byte, nya native DASM ROM/listningar/sym, 15 naturliga room-start savestates, scripts, 15× idle/causal/recovery JSON, full original Gopher raw stdout/commands, faktisk native 1× Stella PNG, U3/symbol/marker bilder, tre original WAV + PCM snippets, MP4, verktygshashar, `TEST_MATRIX.json`, `README.md`, manifest och CRC. Det kompletta developer source/archive förvaras separat på användarens Drive; inputvittne märks uttryckligen SOURCE_GUIDED och bifogas för replay.

Officiell separat native Verification Actions: https://github.com/Odourman/mellanrum/actions/runs/45466845934 . Rapporter och scripts i verifieringsgren `verification/issue50-rc1-20261124`, produktfiler oförändrade. Rå originalartefakter ingår i ZIP, inte automatiskt i GitHub Issue.