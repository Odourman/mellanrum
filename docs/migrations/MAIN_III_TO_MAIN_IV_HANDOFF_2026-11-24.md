# MELLANRUM: SKOGEN SOM LYSSNAR – MAIN III → MAIN IV
**Datum:** 2026-11-24 (Europe/Stockholm)  
**Typ:** Daterad LIVE-kontrollerad dokumentationsöverlämning, inte implementation, oberoende verifiering eller release.  
**Roll:** MAIN III lämnar över till MAIN IV. Färdiga resultat och öppna frågor ska hållas isär.

## 0. LÄS FÖRST – authority order och skilda roller
1. Användarens senaste uttryckliga beslut i tidsordning och inom korrekt scope.
2. Godkända versionerade designoriginal och grafiska överlämningar.
3. `docs/CURRENT_PROJECT_STATE.md`, `docs/SOURCE_REGISTRY.md` och `docs/DECISIONS.md` som navigering; `main` innehåller ännu äldre PR27/Issue32-status.
4. Faktisk GitHub-kod, original-ROM-bytes, källcommits, byggloggar och emulatorartefakter för implementerade saker.
5. Daterade specialisthandoffs.
6. Extern forskning som rådgivning.
7. Memory/chattsammanfattningar enbart orientering.

Repo: https://github.com/Odourman/mellanrum  
Drive: https://drive.google.com/drive/folders/1rO3ZTTBgyZZhqOx1WCxevM6sE3CrvUcl  
Läs LIVE: `AGENTS.md`, `docs/DECISIONS.md`, `docs/CURRENT_PROJECT_STATE.md`, `docs/SOURCE_REGISTRY.md`, Issues #32, #42, #43, Draft PR #38 och #44, äldre MAIN II→III Draft PR #39 samt Drive-handoff 2026-11-23. Statusen i den äldre Drive-handoffens PR38 HEAD och ROM-SHA är historisk. GitHub-issue eller migrationsdokument startar inte annan specialistchatt.

MAIN samordnar och mottagningsgranskar; ROM DEVELOPMENT kodar, utvecklartestar och redovisar; GRAPHICS/AUDIO levererar förslag; VERIFICATION/PACHINKO granskar separat och oberoende. Användaren beslutar om designkompromisser, merge och release.

## 1. LIVE-snapshot vid denna överlämning
### Skyddad PR #38 – referens före Issue #43
- Draft PR #38: https://github.com/Odourman/mellanrum/pull/38 – OPEN, DRAFT, UNMERGED.
- HEAD: `6e9db179867234a19cce329c709170f2423ffbbb`; produktkällcommit: `9293c46eb323f47197046e07e1178279d6c7f525`.
- 16 384-byte NTSC F6, 4 × 4096 bytes, original ROM SHA-256 `bfdeb5308dcecc526e802cd95886b94e0ce4953628e7bc7190c5d49231deac06`, Git blob `51dc00b5ce8170b289acd0b4d997e0c6080b8f54`.
- Alla senare test och färgförändringar på annan SHA gäller INTE automatiskt BFDEB, och BFDEB:s PASS gäller inte automatiskt senare SHA. PR38 ska inte skrivas över.

### Ny färgprototyp: Issue #43 och Draft PR #44
- Användaren auktoriserade ett försök: S3-A `Minnesskärva` orange när aktuell stenpolaritet=0 och röd vid polaritet=1, helst medan S3-B `Omvänd skog` behåller sin ordinarie färg.
- Issue #43: https://github.com/Odourman/mellanrum/issues/43
- Användarens senare förtydligande: ROM DEVELOPMENT får undersöka och föreslå rimliga alternativ, t.ex. att båda symbolerna ändrar färg, men det är INTE automatiskt godkänt. Ny designkompromiss ska beslutas av användaren: https://github.com/Odourman/mellanrum/issues/43#issuecomment-7135467104
- Draft PR #44: https://github.com/Odourman/mellanrum/pull/44 – OPEN, DRAFT, UNMERGED; senast kontrollerad HEAD `e813181f86d950f058f0da71946b6357eecfcc8e` på `romdev/issue43-s3-polarity-feasibility-20261124`.
- PR44 beskriver implementationens källcommit `eaa6b97f9313cb0c49f39b3f4d301da601df638d` och utvecklarens native DASM-prototyp-ROM SHA-256 `07970f492ca9c8aa2f0445b00ce6a046624176db6ebaa7917d7392b7f6b43c2c`, 16 384 B F6. **Skilj byggd kandidathash från incheckad `rom/bin`; PR-texten varnar att gamla incheckade ROM fortfarande kan vara BFDEB. Verifiera bytes/artifact själv innan identitet fastslås.**
- Enligt rapporterad utvecklarevidens: Stella 15/15/coda på native-prototyp, Gopher 15/15/coda och 278/278 undersökta NTSC-ramar med 262 linjer; samma-rad II-02, II-04, III-02, III-05 visar i deras diagnostik förändrad sten utan färgändrad utgång. Dessa är **DEVELOPER evidence**, inte ny oberoende verifiering, och inkluderar RAM-forced diagnostik som inte är vanliga controller-reached lösningar.
- Exempel på lyckade jobb vid HEAD e813: Stella https://github.com/Odourman/mellanrum/actions/runs/45429003976 ; Gopher https://github.com/Odourman/mellanrum/actions/runs/45429004038 . Vissa legacy 4K-jobb är SKIPPED och får inte markeras PASS. Statiskt approx 75/76 CPU-cykler för normal kritisk rad, alltså ytterst liten marginal. Global all-path/stack/raster/bankfuzz fortfarande ej färdig självständig säkerhetsslutsats. Utvecklaren rapporterar också äldre diagnostiska FAIL i testvarianter som förbättrats.
- Human 1× läsbarhet/acceptans, riktig fysisk Atari/RetroN77, separat ny Verification/Pachinko och slutlig releasegate: NOT_RUN för denna nya SHA. **Ingen merge/release eller uppgradering från prototyp till godkänd produkt utan granskning.**

### Oberoende PR38-BFDEB-verifiering
- Issue #42: https://github.com/Odourman/mellanrum/issues/42. Oberoende granskare verifierade native byteparitet, source-guided 15/15, 15×36000 idle och kausala omission-prover, 6507 stack max 5 JSR enligt CFG + Gopher-prober, 262 NTSC i granskat kampanjspår, 52 forced-RAM rammatriser och specifika WSYNC-fall; MAIN mottagningsgranskade efterföljande ZIP.
- Viktig gräns: source-guided är INTE mänskligt cold play, 52 forced RAM är INTE 52 spelade rum, granskade rastervägar är INTE globalt 76-cykel all-path-bevis. Den sista X=1-radens värstafall/HUD och hela CPU budgeten är ej generellt slutförklarade. Fysisk hårdvara, mänskligt speltest och subjektiv audioacceptans ej PASS.
- Exakta detaljer i https://github.com/Odourman/mellanrum/issues/42#issuecomment-7133451388 . Gäller BFDEB, inte PR44.

### Blint speltest – mycket begränsad slutsats
- MAIN III gjorde en 40-minuters video med **automatiserad bildstyrd** agent i verklig Stella och faktiskt TIA-ljud, utan facit för styrningsbeslut. Efterhandsaudit visade **4/15** vunna rum: I-01 till I-04; I-05 fastnade. Det var **INTE** en mänsklig spelare; agentens slumpmässiga målval och periodiska SELECT-omstarter begränsar svårighetsbedömningen. Ingen belägg för att I-05 är olösligt eller att 15 rum är mänskligt för svåra. Användarens mål är tydligare återkoppling utan full manual; inte artificiell väntetid/slump.
- Sammanfattning: https://github.com/Odourman/mellanrum/issues/32#issuecomment-7133980703

## 2. SENASTE ANVÄNDARINRIKTNING: U3-ugglan, fyra synliga riktningar
**Användaren uttryckte "Det låter perfekt" efter följande förslag. Detta är accepterad grafisk inriktning, INTE redan kodad grafik eller ett nytt ROM DEVELOPMENT-implementationsmandat.**
- Rör sig åt **höger**: nuvarande godkända U3-uggla, med vertikal näbb.
- Rör sig åt **vänster**: exakt samma U3, horisontellt spegelvänd.
- Rör sig **uppåt**: U3 90 grader moturs, liggande på rygg med **huvudet åt vänster**.
- Rör sig **nedåt**: U3 90 grader medurs, med **huvudet åt höger** och synlig nedåtriktning.
- Behåll godkända **tre vinganimationer** i samtliga fyra riktningar. Ingen ny fristående uggledesign, inga nya sprites som bryter U3 original.
- Följ verklig **färdriktning**, inte avsedd rörelse mot ett hinder. Ingen separat sten-vändeffekt behövs.
- Teknisk förstudie: Atari TIA `REFP0` kan spegelvända P0 horisontellt; 90° rotation har ingen hårdvaruinstruktion och kräver förberäknade 8×8-bitmasker/ROM-utrymme, exakta scanline/CPU-tester, 1× original-Stella/Gopher-bilder, mask- och vingsilhuettkontroll. Ugglans nuvarande godkända mask kan vara ganska symmetrisk, men användaren uppfattar tydlig skillnad vid spegling.
- **Detta får inte smygas in i Issue #43**. Föreslå ett separat GRAPHICS SOURCE_ONLY-maskprov och därefter separat implementationsauktorisation efter färgprototypens mottagningsgranskning.

## 3. ANDRA NYA SPELDESIGNINRIKTNINGAR
### Kontrollerad variation mellan omspelningar
Användaren välkomnade förslag om viss variation så att samma knappsekvens inte kan läras utantill. Förslag: några få förhandstestade, alltid lösbara startvarianter, särskilt i akt II/III; små förändringar i ugglans startläge/riktning, stenpolaritet och vissa träd. **Ingen gameplay-RNG-implementation är auktoriserad**. Undvik turbaserade vinster, opålitliga ekon, opredikterbara kausala regler, artificiell väntan eller osynligt svårighetsstraff. Kräver GAME DESIGN/RESEARCH, lösbarhetsbevis per variant, resurssäkring samt nytt separat användarbeslut och utvecklingsscope.

### Manual och lärbarhet
Användaren vill att spelet **inte ska kräva eller få en förklarande manual**. Kreativt förslag diskuterades: ett kort tidstypiskt Atari 2600-häfte med joystick/FIRE/A/B/SELECT/RESET och poetiska, begränsade ledtrådar, utan facit, vinstrumsregler, exakta interna tidsfönster eller lösningssekvenser. Det är **inte en formell beställning** att skapa manual eller ny canon. Själva spelet måste göra experiment/konsekvens/sten/eko synliga nog för cold play.

### Kärncanon som ska bevaras
MELLANRUM: SKOGEN SOM LYSSNAR: huvudspel KAMPANJ, tre akter × 5 = 15 distinkta rum, Difficulty LEFT A; mållös audiovisuell FRI SKOG bonus, LEFT B; titel och tvetydig coda. Materialalfabet barrträd, autonom U3-uggla, sten; två olika S3-symboler; Närvaron via negativa rum, förskjutningar/kapningar, inte kroppslig fiende. Indirekt påverkan, inga konventionella vapen, bossar, HP, poäng, liv. 6507/TIA/RIOT omodifierad NTSC 262×76, 128 byte RAM och max 16KiB standard F6.

## 4. Första arbete för MAIN IV, INTE automatisk utvecklingsstart
1. Läs LIVE-källor och pröva varje ny SHA/claim; beakta att main-status och Drive MAIN III-handoff är daterade och att flera gamla Draft PR är open/unmerged.
2. Ta emot slutförd PR44-överlämning: native byggd exakthash, incheckad ROM-identity, Stella/Gopher 1× sten-/utgång-pixlar för båda polariteter på samma rad, controller-driven causality, 262/76 inkl terminal X=1, stack/bank/risker. Skillnad mellan uppmätt PASS, osäkerhet, NOT_RUN och developer claims.
3. Be användaren om eventuellt designbeslut **endast om** teknisk kompromiss visar sig nödvändig. Utgå inte från att utgången får byta färg.
4. Vid ny kandidathash: oberoende ny Verification + Pachinko före releaseprövning. Gammal #42 gäller inte nya SHA.
5. Efter avslutat färguppdrag: föreslå U3 fyra riktningar som **separat** grafisk maskförstudie, inte automatisk ROM-kod. Kontrollerad randomisering separeras som GAME DESIGN/RESEARCH, inte cutover.
6. Aldrig merge/release, ändra fryst PR, starta annan specialistchatt, lova fysisk PASS eller kalla dokumentationsmigration implementation utan separat tillstånd.

## 5. Navigationsvarningar och supersession
- DRIVE-dokumentet **"MELLANRUM – MAIN III – AKTUELL MIGRATION..."** (2026-11-23) och PR39 `docs/main-iii-handoff-20261123` är historiskt korrekt för dåtida källor men deras PR38 SHA är **föregångare till BFDEB**. Denna fil är senare navigationsunderlag, inte självständig högrangscanon.
- `main`-filerna `docs/CURRENT_PROJECT_STATE.md`, `docs/DECISIONS.md`, `docs/SOURCE_REGISTRY.md` är delvis föråldrade. Att tillföra en ny docs-only Draft PR ändrar inte `main` förrän användaren tillåter merge.
- Inget i denna överlämning upphäver fryst PR38, ger beslutanderätt om release eller förvandlar source-only forskning till produktionsauktorisation.
