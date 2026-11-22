# Mellanrum: aktuellt projektläge

**Senast uppdaterad:** 2026-11-22  
**Fas:** G0 – projektetablering och designöverlämning.  
**Implementationsstatus:** INGEN ROM-kod eller spelbar ROM.  
**Verifieringsstatus:** CI_STATIC_PASS för projektkontroller i run #2; ROM_BUILD_NOT_RUN för DASM-build samt NOT_RUN för Stella, Gopher2600, fysisk konsol, spelbarhet, ljud och rastertiming.

## Bekräftad projektidentitet
- Namn: **Mellanrum** (beslutat av användaren).
- Plattformsmål: **Atari 2600**.
- GitHub: https://github.com/Odourman/mellanrum
- Google Drive: https://drive.google.com/drive/folders/1rO3ZTTBgyZZhqOx1WCxevM6sE3CrvUcl
- GitHub Actions: bootstrap-workflow tillförd och körd. [Run #2, commit f7cde196](https://github.com/Odourman/mellanrum/actions/runs/45059253560): `project-checks` **SUCCESS**, `rom-build` slutförd med explicit `ROM_BUILD_NOT_RUN`; DASM-installation, assemblering och artefaktpublicering SKIPPED eftersom ROM-källa saknas.
- MAIN-roll: samordning, spårbarhet, uppdrag, mottagning, granskning – inte automatiskt utveckling eller oberoende Verification.

## Designkällans ställning
En tidigare konceptiteration **"Mellanrum: Skogen som lyssnar" V5** beskrevs i föregående designarbete med barrträd, uggla, sten, tre akter och femton rum. Detaljerna i V5 är **inte infogade eller fullständigt lästa i detta repo**. Den senare frågan om en oidentifierbar hotfull varelse har inte ett slutligt dokumenterat designbeslut. V5 ska importeras som originalunderlag, därefter granskas och få uttrycklig status. V3 eller Let Me Out!-material får inte automatiskt fylla luckorna.

## Gjort
- GitHub-repot inventerat som tomt vid projektstart.
- Drive-projektmapp skapad.
- Projektstyrning och statisk CI/valfritt assemblersteg initierade. Det första faktiska projektkontrollsjobbet är grönkört, utan ROM.

## Nästa grind: G0-DESIGN-INTAKE
1. Ta in den faktiska sista V5-filen/ZIP:en och eventuell senare konstnärlig revision.
2. Ange källa, datum, filhash, vad som är `APPROVED` / `PROPOSED` / `OPEN`; reda ut hotvarelsens roll.
3. Sammanställ Mellanrums egna spelregler, ljudkontrakt och simultana TIA-objektschema.
4. Presentera den första avgränsade ROM-uppgiften **för separat uttrycklig implementationsauktorisation**.

**Befintlig nästa arbetsorder:** [GitHub Issue #1 – G0 designintag](https://github.com/Odourman/mellanrum/issues/1). Ingen automatisk fortsättning till G1.

## Statusetiketter
`NOT_RUN` betyder att provet inte genomförts. `SOURCE_ONLY` gäller dokumentstudier. `CI_STATIC_PASS` endast det CI verkligen kontrollerat. `BUILD_PASS` endast korrekt assembler-/binärkontroll. Ingen får skriva "fungerar i Stella" utan emulatorevidens.
