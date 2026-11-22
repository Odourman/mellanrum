# MELLANRUM – ROM DEVELOPMENT / FULLSTÄNDIG FULLSPELSORDER

**Mottagare:** ROM DEVELOPMENT för "MELLANRUM: SKOGEN SOM LYSSNAR" (Atari 2600)  
**Utfärdad av:** MAIN, på användarens uttryckliga önskemål om ett enda sammanhållet fullproduktionsuppdrag.  
**Datum:** 2026-11-22  
**Uppdragstyp:** HELA SPELET I ETT UPPDRAG. Inte bara förstudie, grafikdemo, ett rum eller MVP.  
**Arbetsprincip:** Arbeta självständigt, lös problem, bygg om när det behövs och leverera bästa möjliga färdiga fungerande ROM med källkod och evidens. Inga nya MAIN-mikrogodkännanden krävs mellan dina egna interna implementationsteg. Oberoende VERIFICATION förblir separat.

## 1. Ditt uppdrag och dina befogenheter

Du ansvarar för hela den faktiska Atari 2600-implementationen: korrekt 6507/DASM-assembler, TIA-raster och visuella objekt, input, alla spelregler, alla 15 rum, ljud, titel, kampanj, FRI SKOG, aktövergångar, slutsekvens, reset, byggkedja, automatiserade kontroller och egen emulatortestning. Ditt mål är en **färdig spelbar Atari 2600-ROM i ett sammanhängande produktionssvep**.

Du har **mycket stort mandat att improvisera** inom den givna konstnärliga kärnan. Välj implementation, optimize data, komprimera registertabeller, omfördela CPU/RAM, förbättra UX, byt animationer, placera tekniska kompromisser och designa bättre varianter när verklig TIA visar begränsningar. Lös osäkerheter genom undersökning och välgrundade beslut i stället för att reflexmässigt stanna eller fråga MAIN. För dokumenterade, ofrånkomliga konflikter: välj en minimalt förstörande lösning, logga den, uppdatera referensdata och test och fortsätt. Inga osannolika 'PASS' eller tyst ändrad canon.

**Ditt mandat att färdigställa hela spelet är uttryckligt.** Det är **inte** en order att påstå att emulator-/hårdvarutest skett om du inte kunde köra det, och det är inte en fullmakt att ersätta Mellanrums kärnidé med ett mer konventionellt spel. En fungerande teknisk lösning som bevarar verket väger tyngre än bokstavlig perfektion i en dekorativ skiss.

## 2. Läsordning, auktoritet och källintegritet – börja här

Du ska INTE börja med att gissa grafik eller skriva en ny spelidé. Kontrollera faktisk åtkomst och läs i denna ordning:

1. **Aktuell GitHub** `https://github.com/Odourman/mellanrum` – läs `AGENTS.md`, `docs/CURRENT_PROJECT_STATE.md`, `docs/DECISIONS.md`, `docs/SOURCE_REGISTRY.md`, `docs/MAIN_V5_1_REVIEW_2026-11-22.md` och denna fullspelsorder. Kontrollera aktuell `main`-commit och läs gällande source hierarchy; anta inte att en tidigare chatt eller Memory är auktoritet.
2. **V5.1:s verkliga originalpaket** `MELLANRUM_V5_1_KRITISKT_REVIDERAT_TILL_MAIN_2026-11-22.zip`. Läs dess `LAS_MIG_FORST.md` först och sedan den fullständiga V5.1-avhandlingen, revisionen, kritiken, 15 rum, `reference/rooms.json`, `reference/engine.py`, `reference/solve.py`, testfiler och lösta spår.
3. **GRAPHICS:s slutpaket** `MELLANRUM_GRAPHICS_V51_FINAL_TILL_MAIN_2026-11-22.zip`. Följ paketets egen läsordning, börja med `STARTTEXT_TILL_MAIN.txt`, `00_GRAFIKAVHANDLING_FULLSTANDIG.md`, `01_GRAFISKT_MANIFEST_OCH_BESLUT.md`, `14_ARKIV_KALLOR_OCH_PROVENIENS.md`, `SHA256SUMS.txt`, risk/fallback/testplan, maskdata, alla 15 rum, förkodade PF-/HUD-tabeller och generatorer.
4. **Metodreferens, EJ Mellanrum-canon:** `ATARI_2600_AVHANDLING_2026-11-21.md`, `ATARI_2600_KUNSKAPSOVERFORING_2026-11-21.zip`, relevant Stella/TIA/6507/DASM-dokumentation. Återanvänd arbetssätt och maskinfakta, inte tidigare spels sprites eller design.
5. Google Drive-projektmapp: `https://drive.google.com/drive/folders/1rO3ZTTBgyZZhqOx1WCxevM6sE3CrvUcl`. Verifiera faktiska original mot repo och bifogade filer; hitta inte på en Drive-kopia som inte finns.

**Före gameplay-kod:** beräkna SHA-256 för de originalfiler du verkligen har, kör ZIP-integritetskontroll och paketens egna generator-/Python-tester och registrera deras faktiska status. GRAPHICS rapporterar `20/20` Python-unittester och `15/15` abstrakta rumslösningar som SOURCE_ONLY. Det är **inte ROM-bevis**, och MAIN har inte själv kunnat läsa råbytes ur ZIP i föregående chatt. Kontrollera detta i din egen miljö. Den läsbara grafikavhandlingen nämner både **25 masker** och på ett annat ställe **23 genererade masker**; fastställ faktiska JSON/ASM-data i stället för att välja ett tal på känsla. Även ZIP:ens uppgivna 69 filer måste kontrolleras mot verkligt manifest.

Om bilagor verkligen saknas: försök hitta exakt dessa filer via tillgänglig Project/Library och faktisk Drive-/repo-åtkomst, utan att blanda ihop äldre GRAPHICS G0 med V5.1 FINAL. Om original inte kan läsas efter kontrollerna, uppge konkret blockerande fil och fortsätt endast med säkert underbyggt arbete; **fabricera inte källrummen eller falska testresultat**. När originalen finns ska detta vara **en obruten fullproduktion** utan återkommande designmöten.

**Konfliktprioritet:** uttrycklig aktuell användarinstruktion och MAIN:s dokumenterade beslut → verifierad V5.1-speldesign och dess `reference`-data för regler/rum → slutlig GRAPHICS V5.1 för gestaltning → råd från äldre forskning. Ny grafik får aldrig i smyg ändra ett V5.1-speltillstånd. Högre/äldre/motsägande dokument ska redovisas, inte överridas bara för att den senaste filen är lättare att nå.

## 3. Spelets icke förhandlingsbara konstnärliga identitet

- Exakt **tre materiella skogsmotiv**: barrträd, en autonom uggla och en fast sten. Spelarens öppna markör, målcell och minimala HUD är gränssnitt, inte fjärde väsen.
- **GITTERSKOG / BILDMELLANRUM**: speglat, kantigt, grafiskt träsnitt. Bildens mellanrum och materialens inbördes regler är verkets estetik. Ingen naturalistisk skogsbakgrund, filmisk Lynch-/Twin Peaks-pastisch, neonshader eller generiska skräckglitchar.
- Ingen direktstyrning av ugglan, HP, poäng, liv, vapen, skjutande, boss, fiende-AI, jakt, jumpscare eller game-over-straff. Spelaren ingriper i **världens villkor**.
- Tre akter à fem rum: **I spegling, II fördröjt eko, III verklig kollisionsinversion plus Närvaron**. Samma fem grundgeometrier återkommer. Inga rum får tyst saknas eller ersättas med andra.
- **Närvaron** är en oidentifierbar möjlig varelse som endast antyds i trädens negativa konturer och i ljud/beteende. Ingen separat kropp, position, hitbox eller monstersprite. Den **kan stjäla FIRE:s betydelse** vid förvarnade tickar. Den får aldrig bli konventionell skräck.
- Ljudet är konstnärligt centralt: originalskrivna TIA-droner, dissonans, klanglig förskjutning, tystnad och bild-ljud-motsägelse. **Inte** ett musik-/rytmspel, inget samplat soundtrack och inga kopierade ljudstycken.
- Spelaren måste kunna förstå kritiska tillstånd **utan ljud**, inklusive Närvarons varning/aktiv/återgång, stenpolaritet, eko och fas. Ingen obehaglig helskärmsstrob eller högljudd jump-scare-stinger.

Om en utsmyckning hotar ett av dessa krav, skär ned utsmyckningen. Om hårdvaran kräver en verklig ändring av kärnregeln, dokumentera beviset, välj den minst skadliga begränsningen och rapportera den öppet – maskera den aldrig som V5.1-standard.

## 4. Exakta spelregler och kontroller

**Kartan:** 10×8 logiska celler, x=0–9/y=0–7, vänster halva speglas mot `9-x`. Cellklasser `#` fast träd, `.` fast glänta, `T` redigerbart träd, `t` redigerbar glänta. Uggla, sten och exit lagras separat. Spelarens markör passerar genom alla celler. Sten och exit förblir öppna även i fas 1. De **exakta femton rumskandidaterna, deras koordinater och startpolariteter** ska hämtas från V5.1 `reference/rooms.json`, inte återskapas från bilder.

**Ugglan:** en kardinal cell per logiskt steg, cirka **1,2 s** (72 NTSC-frames vid 60 Hz; 60 PAL-frames vid 50 Hz efter korrekt tidsnormalisering). Den testar riktningar **framåt, höger, vänster, bakåt** relativt aktuell riktning, flyttar till första öppna cellen, eller väntar om ingen finns. Riktning 0=öst, 1=söder, 2=väst, 3=norr. Vid faktiskt inträde på stenen roterar den 90° medurs om polaritet 0, annars moturs om 1; detta styr nästa rörelse.

**Spelaren:** port 1 joystick flyttar en öppen 8×8-kontur en ruta; första trycket omedelbart, sedan enligt V5.1:s cirka 200 ms initial återupprepningsfördröjning och cirka 100 ms repetering. Tolka diagonaler deterministiskt med V5.1-prioritet. Edge-detektad FIRE: nedhållen knapp upprepar inte. Högst **ett godkänt FIRE per ugglesteg**. FIRE på `T/t` växlar aktuell spegelgrupp. FIRE på stenen växlar polaritet. FIRE på annat avvisas med tydlig konturkvittens utan statuseffekt. SELECT återställer hela rummet inklusive tid, eko, fas, sten och Närvaro; RESET återgår till titeln. Vid titel växlar SELECT KAMPANJ/FRI SKOG och FIRE startar.

**Rumstart:** ~1,8 sekunder förberedelse, markör får röra sig, FIRE knyts enligt V5.1:s tick-0-semantik. Definiera faktisk frame-latch och FIFO/priority för FIRE-edge i implementationen så att knapptryck nära tickgräns inte försvinner eller dupliceras. Välj deterministisk och dokumenterad exakt policy om modellen inte specificerar en video-frame-detalj.

**Akt I:** speglad växling utan eko och utan fasbyte. Stenen styr ugglans riktningsrotation.

**Akt II:** vid godkänd trädomkoppling bokas ett **motsatt eko** efter 3 logiska tick med stenpol 0 eller 5 tick med stenpol 1 **vid bokning**. Högst två väntande ekoslots, samma grupp får inte redigeras före dess eko; full kö avvisar ytterligare ändring. En senare stenändring ändrar inte en äldre due-tid. Behandla två samtidigt förfallna eko i stabil slotordning. Testa wrap 255→0.

**Akt III:** alla ordinarie cellers passabilitet är `blocked = base_bit XOR phase` där phase=0/1, med sten/exit öppna. Fasen växlar efter 4 eller 6 ugglesteg beroende på **aktuell** stenpol; fasålder bevaras vid polbyte. Ugglan får stå kvar i en cell som blivit blockerad och försöker gå ut vid nästa tick. Inversionen måste vara **verklig fysik**, inte ett färgfilter.

**Närvaron, exakt V5.1-tidtabell efter rumstart:**

| Rum | Föraning/varning | Två aktiva uggletick |
|---|---|---|
| II-05 | tick 4 | inga |
| III-01 | tick 4 | inga |
| III-02 | tick 2 | inga |
| III-03 | tick 1 | tick 2 och 3 |
| III-04 | tick 0 | tick 1 och 2 |
| III-05 | tick 2 | tick 3 och 4 |

**Normativ tickordning, följ V5.1 §10 – inte förenklad pseudokod i §36:**
1. Processa högst ett giltigt FIRE. Under aktiv Närvaro: annars giltig **träd-FIRE** kapas så att **stenen växlar i stället**. Inget trädbyte, inget eko; sätt `intercepted`.
2. Direkt FIRE på stenen och vanliga tillåtna operationer fungerar enligt grundreglerna.
3. Vid **första aktiva Närvarotick**, om ingen träd-FIRE redan kapats på denna tick, vänder Närvaron stenen **en gång autonomt**, även när spelaren avstod eller direkt ändrade stenen. Ingen dubbel autonom vändning.
4. Applicera förfallna ekon, sedan fasräknare/inversion, sedan ugglans val och rörelse, eventuell stenrotation, exit/vinst och sedan ljud-/bildtillstånd. Efter de två aktiva tickarna fungerar FIRE som normalt igen.
5. SELECT nollställer alla episodflaggor. Visuell föraning och faktiskt aktiv kapning måste visas olika; inga randomhändelser får avgöra kampanjens lösbarhet.

**Vinst och mellanrum:** Ugglan når original-exit, fysiken fryser, FIRE går vidare efter rumspaus. Efter III-05: cirka åtta sekunders stilla coda med uggla, träd och sten; en sista **rent visuell, icke-spelkritisk** sprickvändning utan FIRE; återgång till titel / Fri Skog. Inga traditionella triumf- eller straffskärmar.

**FRI SKOG:** ett nåbart mållöst läge med samma tre motiv och begränsade tillstånd, deterministiskt seedad variation, fungerande reset och ingen omöjlig oändlig RAM-tillväxt.

## 5. Grafisk produktionsspecifikation från GRAPHICS V5.1

- Visuell huvudlinje `GITTERSKOG / BILDMELLANRUM`, tvåbands-PF per cellrad: **6 scanlines krona + 14 stam**, åtta rader à 20 linjer, 160 synliga spellinjer plus cirka 16+16 informationslinjer inom 192 aktivlinjers NTSC-plan. Vänstra 20 PF-bitar ger de fem cellerna; `CTRLPF.REF` speglar höger. Originalförslaget använder **48 PF-data-byte** för åtta rader × två band × tre register. Packning och faktiska cykler ska bevisas.
- Använd slutpaketets mask- och färgdata **efter bytes-/statuskontroll**, inte idéillustrationer som spelgrafik. Dokumentet anger **25 8×8-masker** och originalrumsspecifika PF-starttabeller. Stäm av skillnaden mot en formulering om 23 genererade maskvärden i grafikhäftets verifieringsavsnitt.
- TIA-kanalförslag: **P0 uggla, P1 markör, BL sten, M0 utgång, M1 valfri stenpolaritetsdetalj**. PF för träd och marginalsymboler. TIA-färger delas: `COLUPF` av PF+BL; `COLUP0` av P0+M0; `COLUP1` av P1+M1. BL ritar inte 8×8-bitmap och kan inte ge en full spricka. Detta är **inte** fel i underlaget: det finns explicit fallback.
- **Stenfall-back:** BL i PF-färg och en **separat tydlig speglingskompatibel underkantsymbol** för polaritet; låt M1-cisel falla bort om position/cykelbudget kräver det. Ingen falskt oberoende stenfärg.
- **Närvaro-fall-back:** valda "Kronans söm" är en **render-only** PF-negativ kontur som inte ändrar `tree_bits` eller kollisionsfysik. Om timing/semantisk läsbarhet hotas: använd enbart speglad marginalindikator, P1-intercept-kvittens och faktisk stenpolaritetsväxling; bevara hela inputregeln. Ingen monstersprite.
- Använd de **48 reflekteringskompatibla HUD-statuskombinationerna** i `04_PALETTER/HUD_PF_REFLECTED_PRECODED.csv` som ROM-tabell eller komprimerad härledning, **aldrig som 48 samtidiga RAM-buffertar**. Speglad marginalgrafik; inga oberoende vänster/höger-ikoner om `CTRLPF.REF` är aktiv utan bevisad midline-kernel.
- HUD visar med former (även i svartvitt) fas 0/1, eko 0/1/2, stenpolaritet, Närvaro normal/varning/aktiv/återgång; inga texttunga meters eller skräcketiketter. Uggla/markör måste läsas i överlapp.
- Paletterna i GRAPHICS är NTSC-hypoteser, **inte kalibrerade TIA-färger**. Granska kontrast, luminans, svartvit switch, PAL separat. Animationer ska vara korta, stabila och inte fördröja ett faktiskt statebyte. Säker prioritetsordning: sann kollisionsbild → uggla → markör → sten/exit → obligatorisk Närvaroindikator → eko → atmosfär.
- Titel, aktövergångar, alla rum, SELECT-reset, FRI SKOG och coda ska vara *äkta TIA-utdata*, inte skärmbilder inklistrade som framebuffer. Specialkernel på titel är tillåten om den ryms i verklig hårdvara.

**De 15 originalrummen:** läs originaldatans `rooms.json` för de exakta ID:na I-01..III-05 och jämför mot `06_ALLA_15_RUM/<ID>/...` i grafikpaketet. Ändra inte positioner bara för att en illustrativ PNG visar dem annorlunda.

## 6. Ljudet måste färdigställas, inte skjutas upp som en dekorativ bonus

Bygg en faktisk 2-kanalig TIA-ljudmotor med originaldroneprofiler, långsam förändring, dissonans, tystnad, ekoföraning, stenskillnad och Närvarons subtraktiva ljudsignal. V5.1 har sju föreslagna klangrum (`D1`–`D7`) och konkreta **oprövade** AUDC/AUDF/AUDV-patchar. Provlyssna och välj fungerande registervärden; låtsas inte kunna generera exakta valfria intervall, PCM-sampling eller mer än två kanaler. Undvik ständig dissonans och höga nivåer. Ljud på/av och lägre volym får inte ändra logik eller information nödvändig för att vinna. Om real-hårdvarulyssning saknas, märk den `NOT_RUN`, men leverera spelbart TIA-ljud i ROM och emulatorprover om verktyg finns.

## 7. Teknisk arkitektur, arbetsfrihet och fallback

Använd **originalkompatibel Atari 2600** (6507, TIA, RIOT med 128 bytes RAM, ingen ARM, ingen extra RAM, ingen emulator-only-skärm). Primär profil **NTSC**; V5.1 föreslår **16 KiB F6** som utgångspunkt. Du får välja annan kompatibel mapper endast om du kan visa varför det behövs och bevara originalkompatibiliteten; dokumentera avvikelsen. PAL är ett avsett separat mål med verkliga 312-linjers och 50 Hz-tider; gör PAL om källor/testmiljö medger, men påstå inte PAL-PASS utan prov.

**Du får improvisera tekniskt:** rasterkärna, bankswitch-stubbar, bildtabellskompression, bitpackning av status, kortare/mindre animationer, pixelprecisa kontrastval, bättre ljudpatchar, exakt policy för FIRE-edges och övergångsbilder. Var hellre robust och konsekvent än trogen en omöjlig bitmapskiss.

**Undersök särskilt:** komplett RAM-livslängd + stackdjup (V5.1:s grovbudget använder alla 128 byte), 76 cykler/scanline, rätt PF0/PF1/PF2-bitordning, P0/P1/BL/M0/M1-konflikter och COLUP-färger, F6 resetvektorer/hotspots, TIMING vid två samtidiga due-eko + fas + Närvaro + joystick, överlapp i samma cell/rasterband, input vid tickgräns, timer-overflow, felaktiga nya buffers och flicker. Gör internt minimalvideo-/rasterprov som *ett steg i fullproduktionsarbetet* och fortsätt sedan hela vägen. Det är **inte** ett separat nytt uppdrag eller en anledning att stanna vid en PoC.

**Högsta reduceringsordning vid verklig maskinbegränsning:** (1) valfri M1-stenspricka, (2) sekundär uggleanimation, (3) lokal render-only-PF-Närvaro men behåll HUD och inputintrång, (4) övergångsgrafik/färgvarianter, (5) eventuell M0-exitgrafik, men ersätt med likvärdigt synligt mål. Behåll 15 rum, spegling, eko, faktisk fas, Närvarons tvåstegsregel, direktbegriplig kontroll, tre motiv och autentisk TIA-ljudregi. Om enda vägen till stabilitet kräver ändring av källdata/rum: dokumentera först fel/förklaring, skapa nytt källspår + tester och bevara originalet.

## 8. Testning och definition av klart

Bygg och kör så mycket som faktiskt är möjligt, utan falska garantier:

1. **Reproduktion av källa:** oändrad V5.1-Python-modell, 20/20 rapporterade test, 15/15 kandidatlösningar, originalrums-JSON och GRAPHICS-generatorer; resultat/logg/hash ska sparas. Om något faller, utred orsaken och dokumentera avvikelse.
2. **Byggbar ROM:** automatiserat DASM-bygge från rena källor, storlek/mapper/bankvektorer, SHA-256, git-commit och byggartefakter; använd GitHub Actions och uppdatera CI så den **bygger den faktiska ROM:en**. En grön statisk CI innan ROM finns är inte ett speltest.
3. **Spelbarhet:** titel, meny, 15 rum i rätt ordning, SELECT/RESET, FRI SKOG, aktövergångar, coda, fysisk joystick-semantik, alla regler akt I–III, Närvaro, läsbara objekt och faktiskt TIA-ljud. För samtliga 15 rum: generera/utför minst ett verkligt spelbart frame/tick-spår som når exit, inte bara abstrakt vittne.
4. **Negativa tester:** håll FIRE 10 sek; otillåtet FIRE; upprepad target med pending eko; full ekokö; två samtidiga förfall; polbyte efter bokning; phase+echo; uggla i nyblockerad cell; tick 253→0→2; aktiv Närvaro med ingen FIRE, giltig trädfire, direkt sten-FIRE, närvaro slut, SELECT-reset, ljud av.
5. **Raster-/minnessäkerhet:** källkodslokal cykelräkning och emulatorvärden för worst-case 76-cykel-kernel; 262 NTSC scanlines stabilt under minst **10 000 frames** om emulatorautomation är tillgänglig; inga out-of-range RIOT-writes, stackkollision, osäkra bankswitch eller ogiltiga display-register. Testa sprite-PF-överlappar och COLUP-delning.
6. **Ljud/bild:** faktiska Stella/Gopher2600-captures där verktyg finns, bildjämförelse mot originalrumsdata och GRAPHICS:s syntetiska skisser, flera ljudprofiler samt verkligt `AUDV=0` för tystnad. Skilj programmatisk kontroll från subjektiv lyssning/konsttest. PAL testas och märks separat.
7. **Egen utvecklarverifiering ≠ oberoende VERIFICATION.** Lämna all evidens till separat Verification-roll. Ingen signoff får låtsas komma därifrån.

Märk varje status exakt: `SOURCE_ONLY`, `MODEL_TEST_PASS`, `BUILD_PASS`, `DEVELOPER_EMULATOR_PASS`, `PAL_NOT_RUN`, `HARDWARE_NOT_RUN`, `INDEPENDENT_VERIFICATION_PENDING` osv. Använd bara PASS för kontroller som **verkligen körts och dokumenterats**. Om emulator saknas, bygg åtminstone en faktisk binär och leverera tydliga manuella Stella-instruktioner och tekniska bevis; kalla det inte testat i emulator.

## 9. Leveranskrav – inte bara en rapport

I **GitHub-repot** ska allt som behövs för nästa människa/roll finnas i ett reproducerbart tillstånd. Förväntad slutleverans:

- Fullständig körbar **NTSC .bin**, och **PAL .bin om faktiskt framtagen**; exakt ROM-format och SHA-256.
- Samtliga DASM-/6507-källor, data- och grafikregistertabeller, rumsdata, ljudmotor, inkluderade assets och versionslåsta generatorer.
- Reproducerbar build-script/README och fungerande GitHub Actions som faktiskt bygger ROM och publicerar artifact. Tydlig mapp för egna testbevis.
- 15-rums progression, verkliga kontroller, slutsekvens och FRI SKOG; inte en mockup, screenshotfilm eller Python-baserad emulator som ersättning för ROM.
- Checksum-/manifestfil, maskinkarta RAM/stack, bankschema, dokumenterade raster-/inputspår, egen testmatris och ett `PLAYTEST.md` med tryckknappsinstruktioner.
- `IMPLEMENTATION_DECISIONS.md` med alla improviserade val, avsteg från avhandling och varför de behövdes; `OPEN_ISSUES.md` med återstående faktiska fel/begränsningar. Ingen tyst modifiering av MAIN:s historiska beslut.
- Till MAIN: en sanningsenlig slutrapport med commit, filvägar, binärstorlek, ROM-hash, verkliga build-/emulatorresultat, jämförelse mot Python och GRAPHICS samt exakt vad independent Verification ännu måste testa.

**Färdig innebär inte "jag skrev koden"**. Det innebär en faktisk ROM med alla relevanta delar som går att bygga och spelas, tillsammans med bevis inom den åtkomliga testmiljön. Om något genuint inte kunde färdigställas, lämna den **bästa faktiskt fungerande versionen**, inte en påhittat färdig produkt, och tala om exakt vad som saknas.

## 10. Självständig arbetsordning – utan pauser för godkännanden

1. Läs och validera original, lösa käll-/maskkonflikter, identifiera canonical data och definiera referensspår.
2. Bygg första fungerande TIA-rasterkärna och ROM-build. Mät faktiska resurser.
3. Implementera input, uggla, sten och akt I. Spela riktiga spår.
4. Integrera akt II:s ekokö och akt III:s inversion; jämför tick-för-tick mot modellen.
5. Integrera Närvarons t-fönster, exakta stenvändningar, HUD och auditiv/visuell förvarning.
6. Implementera alla 15 originalrum, titel, Fri Skog, övergångar, coda och fullständig tvåkanalig ljudregi.
7. Optimera så att faktisk ROM kör stabilt. Använd fallback när bevisat nödvändigt. Kör och dokumentera tester, push till GitHub, leverera binärer och slutrapport.

Detta är **en intern utvecklingsföljd inom samma fullspelsauktorisation**, inte separata huvuduppdrag. Arbeta hela vägen. Fråga bara om det finns en verkligt blockerande auktoritetskonflikt eller helt saknade original som inte kan lösas genom de åtkomliga verktygen. Annars: gör kvalificerade val, dokumentera dem, färdigställ spelet.

**Slutlig instruktion:** Skapa MELLANRUM som ett genuint avantgardistiskt Atari 2600-spel, inte bara ett märkligt pussel med grafikfilter. Låt TIA:s begränsningar, spelarens brist på ägande över ugglan och Närvarons intrång i handlingsavsikten vara själva verket. Fullfölj hela implementeringen, utan att gå i mål i förtid.
