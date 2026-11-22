# Arbetsmodell, gates och teknisk kvalitet

## G0. Initiering och källgranskning (nu)
MAIN säkrar att senaste Mellanrum-design faktiskt finns och läses, registrerar original/versionshash, sammanställer öppna designbeslut (särskilt varelsen) och återkommer med en uppdelad men sammanhängande implementationsplan. Ingen ROM har blivit godkänd för utveckling i G0.

## G1. Designerat, avgränsat genomförbarhetsbevis (kräver uttrycklig start)
Efter användarbeslut: ROM Development bygger första körbara DASM-ROM med originalmechanikens minimala interaktion och korrekt reset/TV timing. Proof-of-concept får inte ersätta riktig gameplayvertikal slice. Testa konkreta worst-case TIA-scenarier och ljudkanalbudget tidigt.

## G2. Spelbar utveckling (separat uppdrag)
Utveckling sker via GitHub branch/PR med commit, källfiler, deterministiskt byggkommando, binär + SHA256, joysticktest, emulatorlogg, rätt skärmutsnitt, frames/scanlines/RAM/stack och kända FAIL. Gå framåt i större men avgränsade steg, inte oändliga enradiga diagnostikexperiment.

## G3. Granskning och verifiering
MAIN granskar leverans och GitHub Actions, men kan endast skriva MAIN_REVIEWED. Fristående Verification hämtar fryst commit, bygger på nytt, kör emulator/fysiskt tester där det ingår och rapporterar PASS/FAIL/NOT_RUN med egen evidens. Vid FAIL: behåll fel, välj ny hypotes eller be designägaren ta ställning.

## G4. Release (kräver uttryckligt beslut)
Först efter accepterad design, spelbar full integration, särskilt oberoende resultat, kompatibilitetsgenomgång och godkänd release. Inga automatiska publiceringar till itch.io eller andra mål.

## GitHub / GitHub Actions
- Issues = avgränsade uppdrag, beslut och blockers; inte bevis på att en specialist körts.
- PR = kodgranskning och diskussion; `main` representerar den senast accepterade **källbasen**, inte automatiskt verifierad release.
- `.github/workflows/ci.yml` = projektstruktur och eventuellt ASM-build. En grön CI-kontroll är INTE automatiskt Stella/Gopher-, gameplay-, timing- eller ljudpass.
- Ingen automatisk merge, release eller deploy. Permissions för Actions är read-only.
- ROM-artefakter får inte stå för samma saker som fullständiga reproducerbara evidenspaket.

## Resursdisciplin
TIA visar videon i realtid. För standard NTSC används 76 CPU-cykler per scanline, 262 scanlines per frame och 128 byte RIOT-RAM inklusive stack. ROM/mapperavgörande tas mot Mellanrums egen objektmatris. Programmeringen ska vara realiserbar; undvik att lösa en fysisk TIA-gräns genom att tyst ändra spelregler.

## Stoppregel
Samma misslyckade hypotes upprepas inte utan ny falsifierbar mekanism. Bokför verklig runtime, syntetiskt men logiskt konsistent tillstånd och domänöverskridande stresstest som olika bevisklasser. Ändrad spelregel eller tydligt grafiskt avsteg kräver användarbeslut.
