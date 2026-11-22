# MAIN – Pachinko Stress Test mottagningsbeslut 2026-11-22

**Disposition:** `PACHINKO_DIAGNOSTIC_PARTIAL_WITH_EVIDENCE`; inga nya verifierade produktfel inom provad yta; **inte** oberoende Verification, inte release och ingen PR-merge.

## Fryst testmål

- [Draft PR #4](https://github.com/Odourman/mellanrum/pull/4), exakt produkt-commit `8bdecde79a6bc1ecb804484d5d257f4f1a99b052`; GitHub kontrollerat att PR-head var oförändrat och inte sammanslaget.
- ROM: 4 096 bytes 4K NTSC, SHA-256 `ec791333da37613ec99ea70b2a983ecc1666b4e576211ece41a8e40bd14cbaed`.
- Originalrapport: [PACHINKO_STRESS_TEST_REPORT_2026-11-22.md](PACHINKO_STRESS_TEST_REPORT_2026-11-22.md). MAIN mottog också filen `MELLANRUM_PACHINKO_STRESS_TEST_REPORT_2026-11-22(1).md`, bytes-SHA-256 `9d09d6358d54a3dbd08a3bd7114124772fd425b92e05019ab4ef250c509cf22a`.
- [PACHINKO Issue #6](https://github.com/Odourman/mellanrum/issues/6) avser diagnos, medan [independent Verification Issue #5](https://github.com/Odourman/mellanrum/issues/5) är separat.

## Rapporterade Pachinko-resultat – ej fullständigt omräknade av MAIN

| Provyta | PACHINKO rapporterar | Evidensklass |
| --- | --- | --- |
| 15 rum × 5 profiler × 32 frön | 2 400 körningar, 69 747 exekverade owl ticks; noll paritetsavvikelser mot referens | SOURCE-GUIDED MODEL_PARITY_REPORTED |
| Tillstånds-/väggraf | 36 067 unika signerade tillstånd, 44 438 riktade övergångar | Modellpopulation, **inte** full state-space-täckning |
| Adversariella edge-case-prov | 152 riktade tester, 0 paritetsavvikelser | MODEL_ONLY_REPORTED |
| Framnavigering till utgång | 15/15 abstrakta vittnen i CPU-instruktionsmodell | MODELED_ONLY; markör kan direktpositioneras |
| Rumnivå frame-input | 64 testfall, 17 600 frames, noll exekveringsstopp | CPU/WSYNC-modell, **inte** verklig TIA |
| FRI SKOG långkörning | 19 080 frames, ett beatvarv 255→0, mode4 bestod | CPU-modell |
| Verklig Stella | 52 input-taps och 13 skärmbilder, 12 skilda bytehashar | REAL_EMULATOR_OBSERVED, men 15/15 passage NOT_RUN |
| Ljudlyssning, Gopher, PAL, fysisk konsol, 15 fullständiga emulatortester | Inte genomfört eller inte implementerat | NOT_RUN/NOT_IMPLEMENTED |

Skillnaden mellan maximalt planerade 192 000 ticks och faktiskt exekverade 69 747 ticks beror på att framgångsrika körningar stoppade tidigt. Statistik gäller de fem testpolicyerna, inte mänskliga spelare. `REPRO/repo/reference/rooms.json` i PACHINKO:s eget material anges uttryckligen vara en projektion och **inte** full original-canon; originalens fullständiga ZIP har inte återlästs av PACHINKO.

**Viktig inskränkning:** Användaren bifogade Markdownrapporten, men **inte** det rapporterade 150-posters evidensarkivet. MAIN har därför inte kontrollerat alla 149 payload-SHA, journalrader, seedpopulationer eller modellräkningar genom omkörning. Ingen ogrundad `MAIN_REPRODUCED_MODEL_PASS` tillskrivs.

## GitHub och faktisk, kontrollerad Stella-evidens

- [GitHub Actions run 45069826844](https://github.com/Odourman/mellanrum/actions/runs/45069826844) var `completed/success` på diagnostik-HEAD `e6e8f3047d2006418fee0e93a01fb918b7d6e186`.
- GitHub compare från produktens SHA till diagnostik-HEAD visar endast **en tillagd workflow-fil** `.github/workflows/pachinko-stella-diagnostic.yml`. Diagnostikkoden ändrar inte produktionens källkod eller ROM.
- MAIN hämtade artifacts `14772668727`, namn `pachinko-8bdecde-stella-blackbox-coarse-input`, 18 751 bytes. Dess ZIP SHA-256 är `bc3e21cb2d981b257d9f9a9d28f0f99592ea56993102dc42d15da5d32c41437f`; ZIP CRC `testzip()=None`.
- MAIN verifierade mot artefaktets filer: 13 PNG, **12 distinkta PNG-bytehashar**, 66 händelserader med **52 tap** och 13 screenshotnoteringar, 15/15 poster i artefaktets eget SHA-manifest matchar, samt exakt ROM på **4 096 bytes** och den auktoriserade SHA ovan.
- Run loggarna visar en verklig DASM-kompilering, installerad Stella 6.7.1 från Ubuntu-paket, Xvfb/xdotool och fungerande PNG-fångst. Det är grov väggtidsstyrd knapptryckning, inte frame-exakt 15-rumsspelning. Ljud kördes med dummy-driver.
- Testverktygets äldre `git diff`-checkout-fel blev korrigerat utan produktändring, och är inte ett MELLANRUM-spelfel.

## MAIN:s bedömning och nästa grind

**Teknisk slutsats:** Omfattande modellstress med noll rapporterade paritetsfel och bekräftade, begränsade riktiga Stella-observationer är positivt. Men modeller av TIA och direkt injicerad markörposition kan dela fel med utvecklarens oracle och saknar faktisk joystick-bevisning. Inget uttalande om fullständig spelbarhet, säkert runtimebeteende eller full konstnärlig överensstämmelse följer därav.

**Fortsatt prioritering:**
1. **Independent VERIFICATION (Issue #5)**: 15/15 riktiga emulatorjoystickrutter, frame-/inputloggar och konkret gameplayinklusive ekon/fasinversion/Närvaron; verifiera original-rooms, source/manifests och bygg själv från exakt commit.
2. **TIA/raster:** exakta scanline/CPU registertraces för extremt överlappande P0/P1/BL/M0, transitions, phase, PRESENCE och 10k+-frame persistens utan timingfel.
3. **Konst och ljud:** faktisk bildjämförelse mot GITTERSKOG; titel- och codaavvikelser flaggade i MEL-028; audiolyssning på riktig TIA-emulering; PAL och fysisk Atari explicit NOT_RUN.
4. Om oberoende granskning ger **reproducerat fel**, skicka minimal indata-/state-/frame-repro till ROM DEVELOPMENT via MAIN. Pachinko upprepas på ny SHA först efter kodändring, inte med gamla PASS som överförda till en ny ROM.

**MAIN-beslut:** Knyt fast rapporten vid versionen; behåll Draft PR #4 öppen. Ingen merge/release/canon-omskrivning och ingen automatisk ny implementation. Den diagnostiska kampanjen är `PARTIAL_WITH_EVIDENCE` och source- och releasegates står kvar öppna.
