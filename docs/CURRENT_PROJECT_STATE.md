# Mellanrum: aktuellt projektläge

**Senast uppdaterad:** 2026-11-22  
**Fas:** G0 – V5.1-designgranskning, fortfarande **inte accepterad** som canon.  
**Implementationsstatus:** INGEN ROM-kod eller spelbar ROM. **Nästa avsedda ROM-order:** en fullproduktionsorder i ett svep, först efter mottaget GRAPHICS-underlag och färdigberedd käll-/designbrief.  
**Verifieringsstatus:** CI_STATIC_PASS för projektkontroller i [run #3](https://github.com/Odourman/mellanrum/actions/runs/45059313938); ROM_BUILD_NOT_RUN för DASM-build samt NOT_RUN för Stella, Gopher2600, fysisk konsol, spelbarhet, ljud och rastertiming.

## Bekräftad projektidentitet
- Namn: **Mellanrum** (beslutat av användaren).
- Plattformsmål: **Atari 2600**.
- GitHub: https://github.com/Odourman/mellanrum
- Google Drive: https://drive.google.com/drive/folders/1rO3ZTTBgyZZhqOx1WCxevM6sE3CrvUcl
- GitHub Actions: bootstrap-workflow tillförd och körd. [Run #2, commit f7cde196](https://github.com/Odourman/mellanrum/actions/runs/45059253560): `project-checks` **SUCCESS**, `rom-build` slutförd med explicit `ROM_BUILD_NOT_RUN`; DASM-installation, assemblering och artefaktpublicering SKIPPED eftersom ROM-källa saknas.
- MAIN-roll: samordning, spårbarhet, uppdrag, mottagning, granskning – inte automatiskt utveckling eller oberoende Verification.

## Designkällans ställning
Användaren har överlämnat ett nytt V5.1-förslag till MAIN. Den indexerade filen `MELLANRUM_V5_1_SKOGEN_SOM_LYSSNAR_KRITISKT_REVIDERAD_AVHANDLING.md` har gått att läsa i Library och granska som text. **Det efterfrågade V5.1-ZIP-paketet med `LAS_MIG_FORST.md`, Python-skript och testresultat har däremot inte varit åtkomligt i denna konversation.** Inga original- eller kodhashar har därför verifierats och 15/15-modellresultatet är endast källans *påstående*, inte MAIN:s reproducerade test.

**Bedömning:** V5.1 är en betydligt starkare och välstrukturerad designkandidat än föregående V5. Formell acceptans avvaktar källpaket/regelpreciseringar. Granskning: [MAIN V5.1 review](MAIN_V5_1_REVIEW_2026-11-22.md). Tre materiella motiv, tre akter, femton rum och Närvarons tvåtick-fönster är *föreslagna regler* i väntan på beslut. Ingen gameplay-ROM får startas.

## Gjort
- GitHub-repot inventerat som tomt vid projektstart.
- Drive-projektmapp skapad.
- Projektstyrning och statisk CI/valfritt assemblersteg initierade. Det första faktiska projektkontrollsjobbet är grönkört, utan ROM.

## Nästa grind: G0-DESIGN-INTAKE
1. Ta in det faktiska V5.1-ZIP-paketet inklusive `LAS_MIG_FORST.md`, `reference/engine.py`, `reference/solve.py`, testfiler, JSON-vittnen, kartor och bildoriginal.
2. Ange källa, datum, filhash, verifiera abstrakta tester och status för föreslagna regler; följ granskningens öppna punkter.
3. Bestäm vad som kräver normativ precisering: FIRE-edge-kö, tickprioritet, videonegativ utan kollisionsändring och RAM-/stackrisk; håll ljudprototyp separat från verifierad ROM.
4. Efter GRAPHICS-överlämning och källberedning: formulera ett **enda sammanhållet fullspelsuppdrag** till ROM DEVELOPMENT enligt användarens nya direkta instruktion (MEL-017–019), med fri kreativ/teknisk problemlösning, byggbar ROM, tester och ärliga kvarstående risker. Ingen ny mikrogate mellan ROM-teamets egna arbetsfaser; oberoende Verification hålls separat.

**Befintlig nästa arbetsorder:** [GitHub Issue #1 – G0 designintag](https://github.com/Odourman/mellanrum/issues/1). Ingen automatiskt påbörjad kodning i MAIN-chatten; den framtida fullspelsordern skickas som en uttrycklig handoff efter GRAPHICS-underlaget.

## Statusetiketter
`NOT_RUN` betyder att provet inte genomförts. `SOURCE_ONLY` gäller dokumentstudier. `CI_STATIC_PASS` endast det CI verkligen kontrollerat. `BUILD_PASS` endast korrekt assembler-/binärkontroll. Ingen får skriva "fungerar i Stella" utan emulatorevidens.
