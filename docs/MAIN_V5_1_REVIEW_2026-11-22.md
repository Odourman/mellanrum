# MELLANRUM – MAIN:s preliminära V5.1-designgranskning

**Datum:** 2026-11-22  
**Status:** `REVIEWED_PROVISIONALLY`, **inte `ACCEPTED_CANON`**.  
**Scope:** design, konstnärlig granskning, teknisk förstudie och källintag. **Ingen ROM-implementation auktoriseras.**  
**Repo:** https://github.com/Odourman/mellanrum  
**Öppen arbetsorder:** https://github.com/Odourman/mellanrum/issues/1

## 1. Källa och integritetsbegränsning

Användaren instruerade MAIN att läsa V5.1-ZIP:ens `LAS_MIG_FORST.md` och sedan full spelavhandling. Någon ny ZIP har inte varit tillgänglig bland den aktuella konversationens monterade filer eller via kontrollerad projektsökning. Ett annat Google Drive-dokument med samma startfilnamn identifierades, men det hör till **The Cabin**, och får inte användas här.

Däremot har en **indexerad Library-text** varit läsbar med titeln `MELLANRUM_V5_1_SKOGEN_SOM_LYSSNAR_KRITISKT_REVIDERAD_AVHANDLING.md` (1 396 rader). Denna granskning grundas på dess faktiska innehåll. Bibliotekets råbyte kunde inte materialiseras för hashkontroll. Fullt ZIP-innehåll, referens-Python, bilder, JSON-vittnen och checksums har **inte** hämtats och deras faktiska teststatus är **NOT_RUN**. Dokumentets uppgift att 15/15 rum har abstrakta lösningsvittnen återges som **designförfattarens rapport**, inte MAIN:s egen verifiering.

Detta är därför **en preliminär källbunden läsgranskning**, inte slutligt formell acceptans eller revision av det underliggande ZIP-paketet.

## 2. MAIN:s bedömning och beslut

**Rekommendation: V5.1 bör ersätta V5 som huvuddesignkandidat, förutsatt att det riktiga V5.1-originalpaketet och dess företrädesordning valideras.** Den normerande spelbasen har ännu **inte** accepterats; inga skyddade designvärden får smygas in i kod.

Styrkor:
- Spelaren manipulerar en frånvaromarkör och världens villkor, men inte ugglans autonoma riktning.
- Tre materiella motiv: barrträd, uggla, sten. Ett fjärde monster är uttryckligen förbjudet.
- Tre akter med 15 rum, spegling → eko → verklig kollisionsinversion, deterministisk kampanj, särskilt fritt läge.
- Droner, dissonans, tystnad och audiovisuell motsägelse är inte ett rytmspel.
- Närvaron är en tidsbunden regelintervention, inte fiendejakt: förvarning, två aktiva ugglesteg, högst ett autonomt stenbyte första aktivsteget, begränsad kapning av giltiga träd-FIRE till stenoperation.
- Tillgänglighet: den kritiska informationen om varning och aktivperiod måste synas även med ljudet avstängt.

Risken för att bli en konventionell pusselprodukt finns kvar, men är mindre än i V5. Kvalitativa speltester behövs för att särskilja verklig konstnärlig effekt från mekanisk 'control debuff'.

## 3. Alla tio avantgardekriterierna

| Nr | Kriterium i V5.1 | Implementerad konceptidé | MAIN:s bedömning | Kan godkännas slutligt nu? |
|---|---|---|---|---|
| 1 | Bryta mot etablerade spelregler | Indirekt kontroll, Närvaron omtolkar FIRE | Tydligt konkret regelbrott | Nej, kräver inputtest + speltest |
| 2 | Experiment före resultat | Omstart utan straff, väntan, Fri Skog | Starkare än konventionell vinstloop | Nej, observera verkliga spelare |
| 3 | Tänja definitionen av tv-spel | Självständig process + aktiv intervention | Idén ändrar maktfördelningen | Nej, kräver spelbar ROM |
| 4 | Upplevelse före begriplighet | Tvetydig identitet men exakt kausalitet | Rätt avgränsad osäkerhet | Nej, tolkningsstudie |
| 5 | Teknik och material | Speglad PF, negativ gestalt, TIA-ljud, fysisk inversion | Stark koppling mellan maskin och form | Nej, TIA/ROM behövs |
| 6 | Slump och oförutsägbarhet | Deterministiska samverkande tidsskikt; seedad Fri Skog | God balans mellan undran och rättvisa | Nej, replay/fuzz behöver reproduceras |
| 7 | Utmana spelaren | Avsiktskapning, förvarning, SELECT | Hot utan död/jakt; skärpa och fairness viktiga | Nej, användartest |
| 8 | Blanda konstformer | Ljud, bild, procedur och event scores | Mer än ett soundtrack ovanpå pussel | Nej, ljudjämförelser |
| 9 | Bortom traditionell design | Ingen score/boss/jakt, frånvaro och kausalitet är verkets ämne | Positivt, men rumsseger är fortfarande pussel | Nej, helhetsupplevelse |
| 10 | Förändra perceptionen | Samma synlig form får olika lag, FIRE kan stjälas | Viktigaste potentialen i V5.1 | Nej, perceptuell test |

**Slutsats om tio kriterier:** 10/10 **behandlade på konceptnivå med mekanik, otillräckligt motexempel och testansats** i §§43–53 och kritisk jämförelsematris. **0/10 experimentellt verifierade som upplevelseeffekt** i en färdig ROM. Notera att `0/10` här betyder `NOT_RUN`, inte tio konstnärliga FAIL.

## 4. Närvaron: regelkontrakt för fortsatt granskning, inte kodorder

| Rum | Varning/föraning | Aktiv | Fysikeffekt |
|---|---|---|---|
| II-05 | t4 | Ingen | Enbart visuell/ljudlig antydan |
| III-01 | t4 | Ingen | Enbart antydan |
| III-02 | t2 | Ingen | Enbart antydan |
| III-03 | t1 | t2, t3 | Två steg med FIRE-kapning + första stegets stenvändning |
| III-04 | t0 | t1, t2 | Som ovan |
| III-05 | t2 | t3, t4 | Som ovan |

Exakt ordning enligt **§10**, som bör vara högst normerande av de två interna kodbeskrivningarna:
1. Högst ett godkänt FIRE; vid aktivt fönster och annars giltig trädomkoppling ändras **stenen i stället**, inga trädbitar och inget eko, sätt `intercepted=true`.
2. Annars tillåt vanliga träd-/stenåtgärder.
3. Första aktiva Närvarotick: självständig stenvändning **om inte** ett träd-FIRE just kapats. Ett direkt FIRE på stenen kan därför neutraliseras av separat automatisk stenvändning.
4. Förfallna ekon i slotordning; sedan fas, ugglerörelse, stenrotation vid inträde, exit och ljud-/bildstatus.
5. Efter två aktiva steg återgår FIRE till normal semantik. SELECT nollställer rum/timer/episodstatus. Ingen HP, hittbar fiendekropp, jakt, jump scare eller permanent förlust.

**Konstnärligt godtagbar riktning:** form som antyds i negativa trädkonturer och auditiva subtraktioner; ingen separat monstruös sprite, förklaring eller filmisk pastisch. Rädslan gäller förlust av förutsägbar kausalitet, inte kroppslig jakt.

## 5. Öppna tekniska blockerare och preciseringar före designaccept

| ID | Klass | Problem / varför det spelar roll | Rekommenderad nästa åtgärd |
|---|---|---|---|
| MR-01 | SOURCE/BLOCKER | Saknat V5.1-ZIP, `LAS_MIG_FORST.md`, originalhash och Python-filer | Ta emot originalpaketet och verifiera manifest/SHA, testloggar och source-of-truth |
| MR-02 | MODEL/BLOCKER | 15/15 abstrakta lösningsvittnen påstås men kan inte reproduceras utan koden/JSON | Kör clean Python-miljö efter intake, kontrollera testutfall och kart/vittnes-konsistens; etikett SOURCE_ONLY tills dess |
| MR-03 | VIDEO/HIGH | RAM-plan (§34) använder **hela 128 byte** och endast 16 byte reserv för faktisk stack; noll marginal | Producera separat RAM-live-range/stack-budget, överväg komprimering, test av dolda bankswitch-/ljudtemporärer |
| MR-04 | VIDEO/HIGH | Negativ PF-Närvaro måste ändra *bildens gestalt* utan att oavsiktligt ändra 40-bitars logisk kollision | Precisera separat `render_only_negative_mask`/tillståndsbuffer och verifiera TIA-resurs-/cykelkonsekvens; erbjud förenkling av gestalt |
| MR-05 | INPUT/HIGH | Rapporterade abstrakta actioner saknar exakt NTSC/PAL-FIRE-edge, debounce, markörflyttning och ticklatch | Skriv explicit policy: första/ sista tillåtna FIRE-edge per tick, avvisad action, prep-t0, latens, NEXT room och SELECT-edge |
| MR-06 | LOGIC/HIGH | Modulo-256 tick, förfallna ekon och polskifte/periodbyte kan ge fel runt wrap | Konkreta negativa scenarier vid t253–t2, två due ekon, pending + Presence, fasvinst och reset |
| MR-07 | SPEC/MEDIUM | §36:s frame-pseudokod saknar V5.1:s Närvaro-steget och kan misstolkas som auktoritativ | Märk pseudokoden 'förenklad' eller inför korrekt intercept/autonom steg före echoes enligt §10 i V5.1-final |
| MR-08 | DISPLAY/MEDIUM | Varning och aktiv tvåticksperiod måste synas utan audio, samtidigt som marginal och PF kan vara upptagna | Rita 2 testbara statiska symboltillstånd, testa överlapp och färg-/svartvitt läge, undvik strob |
| MR-09 | AUDIO/MEDIUM | Två kanaler kan inte ge tre samtidiga ljudroller; sju profiler och upplevda intervall är hypotetiska | Separat AUDIO-research/provlyssning, kontroll av AUDC/AUDF/AUDV och nivå; ingen musikalisk eller fysiologisk garanti |
| MR-10 | EMULATOR/HIGH | F6-bankning, 76 cykler/scanline, NTSC/PAL, 262/312 frames och joystickspel har ännu inget faktiskt test | Föreslå avgränsad test-ROM **för separat användarorder**, byt inte mapper av bekvämlighet |
| MR-11 | ART/MEDIUM | Hotet riskerar att bli en banal "debuff", samtidigt som uggla/skog/drone kan kännas som en färdig Lynch-symbolik | Testa med deltagare utan artbrief; mät både regelförståelse och olika tolkningar; avvisa konkreta imitationer |
| MR-12 | SPEC/MEDIUM | §16:s cirka åtta sekunders epilog och den sista autonoma visuella stenvändningen behöver entydig ordning mot titel/FRI SKOG | Dokumentera frames/trigger/visuell coda utan att ändra post-win logik eller reset |
| MR-13 | SOURCE/MEDIUM | §6 säger "Antagna beslut" i en avhandling som samtidigt är `PROPOSED` | Vid slutlig version skilj DESIGN_PROPOSED, USER_APPROVED och ROM_VERIFIED; skriv inte om historiska beslut tyst |

**Konstnärlig acceptansbarriär:** Lägg inte till identifierbar monsterfigur, strid, slumpmässig inkonsekvent FIRE eller obligatorisk hörsel för att göra Närvaron tydligare.

## 6. Teknisk genomförbarhet: omdöme

**Plausibel i princip, INTE verifierad.** En symmetrisk 10×8-värld, en P0-uggla, P1-markör, BALL-sten, M0-utgång och en tvåticksförskjutning av logiska kommandon är mindre objektkrävande än många vanliga 2600-spel. Ingen separat fiendesprite behövs. Men playfield-konturernas band, överlapp, blankningspreparering, ljuduppdatering, ROM-banktrampoliner och full RIOT-budget har ännu inte mätts. Att Python-modellen kan hitta en väg är inte bevis för att 6507 hinner rita eller att kontrollerna känns bra.

Tekniska kontrollkällor:
- [Stella Programmer's Guide](https://www.ataricompendium.com/archives/documents/tech_docs/2600_Stella_Guide_12-3-79_reformatted.pdf): 76 CPU-cykler/scanline och realtidsrendering.
- [Stella Debugger](https://stella-emu.github.io/docs/debugger.html): register/RIOT, _sCycles, _scan, breakpoints och framekontroller.

**Förslag till separat G1-order, inte start:** en stabil NTSC-DASM ROM med ett 10×8-rum, speglad PF-ändring, autonom uggla, markör, sten, kort tydlig visuell varning och testbart tvåtick-kommandoövertagande. Använd standard-NTSC och auditbar ROM/byte/hash/emulatorlogg. Koppla sedan mot referensmodellen och oberoende Verification. Bredare system (alla 15 rum, sju droneprofiler, Fri Skog, PAL) är senare scope, inte implicit auktoriserade.

## 7. Formell beslutsmatris

| Fråga | Beslut nu |
|---|---|
| Kan V5.1 ersätta V5 som **granskningskandidat**? | JA, provisoriskt |
| Är 10/10 avantgardekriterier behandlade i dokumentet? | JA, på konceptnivå |
| Gör Närvaron spelet till traditionell skräck? | NEJ enligt design; faktisk upplevelse ej testad |
| Är hårdvaruarkitekturen realistisk? | PLAUSIBEL, med öppna RAM/timing/visual/audio risker |
| Är källpaket och 15/15 Python-resultat verifierade? | NEJ, saknat ZIP/code |
| Är V5.1 accepterad som slutlig projektcanon? | NEJ |
| Har ROM Development fått startauktorisation? | NEJ |
| Finns oberoende Verification-pass? | NEJ |

## 8. Nästa steg inom G0

1. Ta emot exakt V5.1-paket. Läs `LAS_MIG_FORST.md` först, verifiera filhash/proveniens och kör Python-testmodellen självständigt utan att ändra den; matcha vittnen mot kartorna.
2. Stäm av MR-03 till MR-13 mot faktisk källa och föreslå små redaktionella/tekniska precisioner utan att ändra spelets konstnärliga kärna.
3. Föreslå separat **formell V5.1-designacceptans** till designägaren, följd av separat auktorisation för en snäv ROM-prototyp om så beslutas.
4. **Independent Verification** är en annan aktör än ROM Development. MAIN-granskning räknas inte som den aktörens bevis.

**Källhygien:** Den här rapporten är MAIN:s *preliminära källgranskning av avhandlingen* (läsbar text, inte verifierat binärt originalpaket). Ändra inte dess status till `FINAL_ACCEPTED` eller `L1_REPRODUCED` genom att bara läsa sammanfattningen.
