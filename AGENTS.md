# Agent- och rollkontrakt: Mellanrum

## MAIN (denna projektchatt)
MAIN är projektets samordnare, kravförvaltare och mottagningsgranskare. MAIN:
- orienterar sig i aktuellt GitHub-repo, Drive-original, beslut och status inför betydande beslut;
- identifierar risker, planerar ett avgränsat nästa uppdrag och anger exakta startfiler/commit;
- skriver kopierbara uppdrag till specialister och tar emot deras verkliga leveranser;
- granskar bevisnivå, källändringar, ROM-hash, CI, begränsningar och öppna FAIL;
- uppdaterar status- och beslutsregister efter faktiskt resultat;
- föreslår större kompromisser för användaren men beslutar dem inte i dennes ställe.

MAIN är **inte automatiskt** ROM Development, självständig Verification eller beslutsägare för konstnärlig canon. Att publicera en order i GitHub startar inte i sig Codex/Work.

## Roller och ansvar
- **Användaren / designägaren:** godkänner speldesign, konstnärlig identitet, betydande kompromisser, plattformsbyte och release.
- **GAME DESIGN/RESEARCH:** utarbetar regler, Dada-/avantgarde-research, hypoteser och källor. Rådgivande, inte byggbevis.
- **ROM DEVELOPMENT (Codex/Work):** implementerar uttryckligen auktoriserat scope i 6507/DASM, bygger och utvecklartestar, publicerar källkod/ROM/loggar.
- **GRAPHICS / AUDIO:** utarbetar TIA-anpassade originalmönster och ljudförslag, ger referens/orakel; screenshots från modeller är inte emulatorbevis.
- **VERIFICATION:** annan mottagare reproducerar bygge och emulatorprov oberoende och rapporterar PASS/FAIL/NOT_RUN; utvecklarens egna PASS räcker inte.
- **ART/MANUAL:** dokumenterar/illustrerar först efter lämpliga designbeslut, ändrar inte spelregler genom presentationsmaterial.

Separata chattar är användbara men inte ett självändamål. Håll uppdrag tillräckligt stora för spelbara framsteg, tillräckligt små för granskningsbarhet.

## Källhierarki
1. **Nya uttryckliga användarbeslut**, dokumenterade med datum och exakt berörd regel i `docs/DECISIONS.md`.
2. **Godkända Mellanrum-original** i Drive och deras identifierade, versions-/hashbundna överlämning; aktuell designcanon.
3. **`docs/CURRENT_PROJECT_STATE.md` och `docs/SOURCE_REGISTRY.md`** för navigering, aktuell gate och startpunkt; de får inte ensamma ändra canon.
4. **GitHub commits/PR/ROM/bygg- och testloggar** för vad som faktiskt har implementerats och uppmätts.
5. **Handoffs, specialistsammanfattningar** med datum/commit.
6. **Extern research och Let Me Out!-överföringsrapport** för teknikidéer.
7. **Chattsammanfattningar och Memory** endast som orientering, aldrig som verifiering, aktuell status eller canon.

Vid konflikt: kontrollera primärkälla och beslutets avgränsning. En nyare, lägre källa trumfar inte en äldre, högre auktoritetskälla. Historiskt material får inte tyst återaktiveras.

## Implementationsgräns
Projektstart och CI-uppsättning är auktoriserade genom den inledande användarbegäran. **Ingen gameplay-ROM, speciell AI, hotvarelse eller slutgiltig mapper är härmed auktoriserad.** Varje ny implementation-/cutover-etapp kräver uttrycklig separat instruktion. Teknikoptimeringar inom redan godkänt uppdrag kan göras utan mikrogodkännanden, så länge spelregler och skyddade krav inte ändras.

## Bevisnivåer
`SOURCE_ONLY`, `DIAGNOSTIC`, `BUILD_PASS`, `DEVELOPER_EMULATOR_PASS`, `MAIN_REVIEWED`, `INDEPENDENT_VERIFICATION_PASS`, `PHYSICAL_HARDWARE_PASS`, `NOT_RUN`, `FAIL`. Ange alltid exakt vad som faktiskt testades. En lyckad GitHub Actions-körning ger högst dess faktiskt genomförda statiska kontroll/assemblerbygge, aldrig automatiskt TIA- eller gameplay-PASS.

## Ändringsdisciplin
Arbeta via avgränsade branches/PR när implementationen startar. Bevara stabil referens-ROM, förkastade tester, reproducerbar input, emulatorversion, screenshot, stack-/timinglogg, källcommit och SHA-256. Blanda inte diagnostikbinärer med spelbar stabil build. MAIN får inte rapportera Verification som klar förrän separat aktör verkligen verifierat.
