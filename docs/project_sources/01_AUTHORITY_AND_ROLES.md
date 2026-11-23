# MELLANRUM – auktoritet, mandat och roller
Klass: Project Source / arbetshjälp. Verifiera alltid mot LIVE [AGENTS.md](https://github.com/Odourman/mellanrum/blob/main/AGENTS.md) och [DECISIONS.md](https://github.com/Odourman/mellanrum/blob/main/docs/DECISIONS.md).

## Bindande källhierarki
1. Senaste **uttryckliga användarbeslut** för aktuellt scope, registrerade med datum/besluts-ID. Nya beslut om paus/återupptagande får inte ignoreras.
2. Faktiskt **godkända MELLANRUM-original** i Drive och versions-/hashbundna överlämningar för speldesigncanon.
3. \`CURRENT_PROJECT_STATE.md\` och \`SOURCE_REGISTRY.md\` som projektindex, inte fri rätt att ändra canon; kontrolleras mot livefakta.
4. GitHub commit/PR/ROM/bygg- och testbevis för **vad som implementerats och mätts**. Implementationsfakta kan inte ensamt besluta konstnärligt godkännande.
5. Handoffs/specialistrapporter med datum och exakt commit.
6. Extern forskning och andra spelprojekts erfarenheter = rådgivande.
7. Chattsammanfattningar/Memory = endast orientering; aldrig ensam status-, implementations- eller testauktoritet.

En nyare källa med lägre rang upphäver inte automatiskt äldre godkänt original med högre rang. Vid tvetydighet: redovisa konflikt, kontrollera primärkälla, stoppa riskabel ändring.

## Beslutsföljd och senaste stopp
- **MEL-053:** högst 16 KiB; 32 KiB som fallback avvisat.
- **MEL-054 / Issue #21:** full utveckling av 15 rum med självständiga design- och teknikändringar inom kärnan.
- **MEL-055 / Issue #26:** verklig 16 384 B F6-kandidat, inte 4 KiB med tom utfyllnad.
- **MEL-056 / Issue #32:** vidare konstnärlig och spelmässig förbättring av **ny** kandidat efter riktig PR27-video; rättar bland annat 15 puzzles, fyra markörtillstånd, ljud, coda. Frys PR #27 och äldre.
- **Senare användarbeslut 2026-11-23 "Avbryt":** stoppar **fortsatt ROM DEVELOPMENT Issue32-implementation**. Beställningen att migrera till ROM DEVELOPMENT III är en separat **read-only** överlämning. Den återstartar inte utvecklingen.
- Ett nytt uttryckligt återupptagningsbeslut behövs för mer kod/ROM/utvecklingstest. Ingen automatisk release följer ens av framtida återstart.

## Roller och tydliga gränser
**Användaren/designägaren:** beslutar konstnärlig identitet, väsentliga kompromisser, nytt implementationsscope efter paus, release, plattformsbyte, slutligt designgodkännande.

**MAIN II:** samordnare, kravförvaltare och mottagningsgranskare; läser primärkällor, identifierar faktiska blockerare, skapar avgränsade uppdrag när auktoriserat, granskar utvecklarens bytes/PR/CI, håller olika test-SHA separata och föreslår release eller förbättring. MAIN II är inte automatiskt ROM DEVELOPMENT, Verification eller designägare.

**ROM DEVELOPMENT III:** 6507/DASM-implementatör och utvecklartestare, men **pausad**. Läs in exakta källor, kontrollera leverans och rapportera status i migrationsuppdrag; ingen ny produktkod, ny ROM eller långtestproduktion före nytt tillstånd. Ingen självattestering av oberoende Verification.

**GRAPHICS/AUDIO:** utvecklar konstnärliga, TIA-genomförbara originalförslag och specifikationer. Renderade konceptbilder/modeller är inte autentiska Stella-bilder. Ändrar inte produkt-ROM utan separat tilldelat scope.

**GAME DESIGN / RESEARCH:** föreslår regler och källbaserade hypoteser; forskning förbereder beslut men bevisar inte implementerade ROM-funktioner.

**VERIFICATION:** separat person/chatt/procedur som oberoende reproducerar exakta SHA-bundna tester och skriver PASS/FAIL/NOT_RUN. Modifierar inte verifierad produkt eller övertar utvecklarroll.

**PACHINKO STRESS TEST:** separat adversarialt spel- och tillståndstest, bank/CPU/fuzz/idle; ska rapportera reproducerbara fel, inte lappa ROM eller överta Verification.

**ART/MANUAL:** förpackning, instruktioner och kommunikation efter godkända designbeslut; marknadsföring får inte skapa ogrundade spelregler.

## Uppdragsdisciplin
1. Identifiera *spel* och *roll* först. I ChatGPT-projektet finns flera Atari-projekt som inte får korsförorena varandras canon.
2. Sätt exact source HEAD, ROM SHA, issue, leveranskriterier, tillåtna filtyper och förbud i varje specialistorder.
3. Dokumentera beslutens datum, ändrad regel och supersession i \`DECISIONS.md\` när en faktisk ny användarorder föreligger.
4. Publicering av GitHub Issue/PR startar **inte** annan chatt automatiskt. Användaren måste själv initiera mottagaren eller använda ett aktivt verktyg med rätt auktorisation.
5. Aldrig merge, tag, release eller vidare implementation enbart för att underlag, migrationsprompt, project source eller CI blir klart.

## Källkonflikt som ska hanteras
\`AGENTS.md\` innehåller en historisk formulering om att gameplay-ROM ännu inte var auktoriserad. Den avser projektets tidiga gate och kan **inte** radera senare uttryckliga MEL-054/055/056-beslut. Men MEL-056 ger heller inte rätt att ignorera det **ännu senare** "Avbryt". Läs alltid beslut som en tids- och scopekedja, inte lösryckta meningar.
