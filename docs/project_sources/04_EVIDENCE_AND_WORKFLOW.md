# MELLANRUM – verifieringsdisciplin, leveranser och arbetsflöde
Klass: Project Source / procedur. Följ senaste uttryckliga användarbeslut. Vid snapshot 2026-11-23 är produktutvecklingen stoppad.

## Bevisstatus – använd snäva etiketter
- SOURCE_ONLY: källa/text/idé finns, inget exekverat hårdvarubevis.
- DIAGNOSTIC: avgränsat experiment, inte spelbar verifiering.
- BUILD_PASS: visat DASM-/CI-bygge samt vilken artefakt och hash som faktiskt producerats.
- DEVELOPER_EMULATOR_PASS: utvecklarkontrollerad riktig Stella/Gopher med dokumenterad input och samma ROM SHA.
- MAIN_REVIEWED: MAIN har kontrollerat underlaget och utvärderat scope/limits; **inte** likvärdigt med oberoende PASS.
- INDEPENDENT_VERIFICATION_PASS: separat verifierare har reproducerat definierade tester mot exakt bytes/hash.
- PACHINKO_PASS: separat adversarialt stresstest enligt eget ärende, avgränsat till faktiskt genomförda kontroller.
- PHYSICAL_HARDWARE_PASS: påvisad fysisk originalhårdvara med protokoll; RetroN77-emulator är separat.
- NOT_RUN / INCONCLUSIVE / FAIL: använd dessa uttryckligen för saknat, otillräckligt eller negativt bevis.

En GitHub Actions-grön ruta innebär endast PASS för faktiskt körda steg. SKIPPED, no-job failure och statiskt test är inte ROM-kompatibilitet, 15/15 gameplay eller riktig beam-timing.

## Proveniens per körning – obligatoriska fält
1. Titel/uppdrag/Issue, PR-nummer och låst **full commit SHA**.
2. Exact bytekälla: checkad Git blob eller Actions-artifact ZIP/Drive-backup, filväg, **storlek och full SHA-256 för ROM**.
3. DASM-kommando/version, mapping (F6 4×4096), bygglogg och byte-paritet mellan byggt och levererat ROM.
4. Emulator och **version/build/core**, faktisk input med frame-index, starttillstånd (genuint controller-reached), seed och färdig trace/savestate enligt testupplägg.
5. Bilder/WAV/MP4 från *samma ROM* med verifierade frames/audio-sync; skilj modell-/illustrationsbilder från riktig emulator.
6. Raster: korrekt 262 NTSC, worst-case 76 cykler/scanline, NUSIZ-/HMOVE-tider, stack-RAM highwater, F6 hotspots/trampoliner.
7. Vilka testfall verkligen kördes; PASS/FAIL/NOT_RUN per kontroll; kvarstående risker och om användaren själv godkänt visuellt/ljudmässigt.

**Underkänn direkt** ett byte-/SHA-missmatch, ogiltig spelvideo, påstått fulltest utan trace, artificiell ROM-padding som "förbättring" eller återanvänd old-hash Verification som new-hash PASS.

## Testmatris för framtida ny version EFTER uttrycklig återstart
- ROM ≤16 384 byte, standard F6 och fungerande på omodifierad NTSC Atari 2600 i princip. Inga specialchips/RAM.
- Native DASM clean build med identisk faktisk ROM, originalspel från titel → rum 1–15 → coda → titel i *Stella och Gopher2600* med joystick/FIRE; inga RAM POKEs för att hoppa förbi pussel.
- 15× minst 36 000 verkliga idle-frames från äkta room starts; **0/15 självvinster**, och 15 matchade critical-action-counterfactuals. Tillfälligt misslyckade/rimligt alternativa beslut får inte skapa osynligt softlock.
- Värdera *riktiga beslut*, inte bara antal FIRE eller replay-längd. Human cold playtest får endast PASS om faktiskt mänskligt speltest utförts.
- Fyra riktiga, jämförbara 1× Stella-bilder av markören i samma rum/läge/tillstånd, samt U3/S3/tree/Presence/coda alla rum.
- Riktig TIA-vågform och lyssningsprov för titel, Presence, alla tre akter; minst en **verkligt synlig** enplansvideo med ljud och kontrollerad H.264/yuv420p/SAR.
- Gopher/Stella raster, worst-case timing/stack och bankväxlingsfuzz, RESET/SELECT/difficulty, 50k FRI, stress kring ljudfas och eko.
- Teknikrapport som värderar samtliga 30 Atari-trick individuellt, anger faktiskt använda vs avfärdade, mätbar nytta och hårdvarubegränsningar; forskningsprosa räcker inte som test.

Detta är **framtida acceptanskriterier**, inte en order att genomföra tester nu medan "Avbryt" gäller.

## MAIN II:s normala loop
1. Kontrollera live källor, senaste användarbeslut, vem äger nästa steg. Efter paus: bara docs, statusrevision och mottagningsgranskning, om auktoriserat.
2. Identifiera risker och samla ändringsförslag i en smal, fullt källbunden order; ändra inte frysta referens-PR.
3. Vid nytt tillstånd: delegera implementation till ROM DEVELOPMENT (en ansvarig gren/ROM-family per order). Förslag från Graphics/Research behandlas som rådgivande fram till godkännande och faktisk kod.
4. Ta emot versionerat DASM/ROM/CI/trace/bevispaket och kontrollera faktisk bytes mot rapport.
5. När en **ny slutkandidat har frysts**, skapa NYA oberoende SHA-bundna Verification- och Pachinko-uppdrag; låt dem köras av andra roller.
6. Om något är FAIL/NOT_RUN, föreslå reparation eller dokumenterad kompromiss. Varje ändrad ROM-byte kräver ny SHA och test för ändrat scope.
7. Efter full teknisk och mänsklig granskning föreslå release för **användaren**. Ingen automatisk merge/tag/publicering.

## Mottagningsformat för specialister
Svara alltid med: **ROLL / UPPDRAG / SOURCE HEAD / ROM SHA / VAD ÄNDRADES / KONKRETA BEVIS / PASS–FAIL–NOT_RUN / RISKER / BEHÖRIGHETSGRÄNS / REKOMMENDERAT NÄSTA ENDA STEG**.

## Avvikelsehantering
Om användarbeslut och docs verkar motsäga varandra, fråga inte efter redan tillgänglig länk: öppna Live GitHub/Drive och spåra beslutets datum/scope. Vid verklig oförenlighet mellan två användarbeslut gäller det senare, explicit för dess avgränsning; inga tysta supersessions. Ingen sluten chatt, agentprompt eller Docs-projektkälla får själv skapa ny auktorisation.
