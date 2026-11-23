# MELLANRUM – Project Sources / LÄS FÖRST
Version: 2026-11-23 18:00 CET · Ägare för samordning: MAIN II · Klass: navigeringsmaterial, inte självständig canon eller implementationsorder.

## Syfte och tillämpning
Detta paket hjälper chattar i ChatGPT-projektet "Atari 2600 avantgarde spel" att hantera just **MELLANRUM: SKOGEN SOM LYSSNAR**. Det ersätter inte projektets primärkällor och får inte automatiskt överföras till THE SKRAUN, THE CABIN, LET ME OUT! eller andra spel.

**VIKTIGT: Utvecklingen är PAUSAD efter användarens "Avbryt".** Issue #32 var ett uttryckligt implementationsmandat, men den senare avbrottsordern har stoppat vidare produktarbete. Den efterföljande migrationsbegäran till ROM DEVELOPMENT III var **endast onboarding/överlämning**, inte återupptagande. Skapa inte ny produktkod, bygg/ändra ROM eller fortsätt omfattande produktionsprov utan nytt uttryckligt användartillstånd. Dokumentationsarbete och läsbaserad mottagningsgranskning inom uppdraget är åtskilda från implementation.

## Obligatorisk läsordning inför betydande beslut
1. Kontrollera det **senaste uttryckliga användarbeslutet** och dess tidsordning/scope. Jämför beslut i [docs/DECISIONS.md](https://github.com/Odourman/mellanrum/blob/main/docs/DECISIONS.md), inklusive MEL-053–056 och senare "Avbryt".
2. Läs aktuellt [AGENTS.md](https://github.com/Odourman/mellanrum/blob/main/AGENTS.md) för roll- och källhierarki.
3. Kontrollera godkända MELLANRUM-designoriginal i [Drive-mappen](https://drive.google.com/drive/folders/1rO3ZTTBgyZZhqOx1WCxevM6sE3CrvUcl), inklusive exakta versioner/hashes om sådana finns. Mappen innehåller i dagens snapshot främst ROM DEVELOPMENT-migration och artefaktbackup, **inte** verifierat fullständiga designoriginal.
4. Läs [CURRENT_PROJECT_STATE.md](https://github.com/Odourman/mellanrum/blob/main/docs/CURRENT_PROJECT_STATE.md) och [SOURCE_REGISTRY.md](https://github.com/Odourman/mellanrum/blob/main/docs/SOURCE_REGISTRY.md) som index. **OBS: main-status är föråldrad angående PR #33**.
5. Kontrollera LIVE-objekt: [Issue #32](https://github.com/Odourman/mellanrum/issues/32), [Draft PR #33](https://github.com/Odourman/mellanrum/pull/33), [docs-only PR #34](https://github.com/Odourman/mellanrum/pull/34), GitHub Actions, exakta commits och ROM-bytes/hashes.
6. Använd överlämningar och research som lägre bevisnivå. Ingen chatthistorik eller Memory får ersätta rådata.

## Akut identitetsvarning
Stoppad WIP: PR #33 HEAD `48c0d5026d5a9ea22de1ff93028f3e18046e521b`.
- Ny byggartefakt från [Actions 45184894712](https://github.com/Odourman/mellanrum/actions/runs/45184894712): 16 384 B F6, SHA-256 `962818fa6a8a26eb22a66c66bd3da519467b78f790b149748ea3f036a97d011a`.
- **Den incheckade** `rom/bin/MELLANRUM_16K_NTSC_F6.bin` i PR #33 är ännu **gamla** PR #27-binärramens SHA-256 `7ce777dc273e1c30d8621843052e941ced41fcf2961bcdf835576a11c9592446`.
- Blanda aldrig versionerna. Ett test-PASS gäller endast exakt testad ROM-SHA + källa + emulatorversion + faktisk metod.
- Förra fullspels-MP4:n för Issue #32 är praktiskt taget svart och underkänd som videoevidens.
- Ingen slutlig release, merge, oberoende Verification eller Pachinko kan hävdas.

## Paketfiler
- `01_AUTHORITY_AND_ROLES.md`: beslut, behörighet, roller och stopp.
- `02_ARTISTIC_CANON_AND_HARDWARE.md`: spelidentitet, skyddade designramar och teknikgränser.
- `03_CURRENT_SNAPSHOT_AND_OPEN_GATES.md`: exakt versionsbunden status och osäkerheter.
- `04_EVIDENCE_AND_WORKFLOW.md`: beviskrav, samordningsprocess och specialistöverlämningar.
- `05_LIVE_SOURCES_AND_RESEARCH.md`: länkar, research, källtyper och underhåll.
- `06_PROJECT_INSTRUCTIONS_COPY.md`: kort text att klistra i ChatGPT-projektets instruktioner.

**Underhållsprincip:** denna daterade snapshot blir snabbt gammal. Kontrollera LIVE GitHub/Drive innan uppdrag, versioner, gatebedömningar eller användarbeslut. Ändra aldrig status genom att bara kopiera in nyare sammanfattningar utan primärkällor.
