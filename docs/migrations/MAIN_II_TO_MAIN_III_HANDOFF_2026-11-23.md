# MELLANRUM – MAIN II → MAIN III: kontrollerad överlämning
Datum: 2026-11-23, kväll (Europe/Stockholm). Typ: docs-only, LIVE-källgranskning. Ägare: MAIN II → ny MAIN III. Inget produktmandat, ingen release, ingen merge.

## LÄS FÖRST
Denna fil är ett **daterat navigeringsunderlag**, inte överordnad godkänd canon eller ett live-uppdaterat register. Kontrollera senast uttryckliga användarbeslut och dessa källor LIVE:
- Repo: https://github.com/Odourman/mellanrum
- Drive: https://drive.google.com/drive/folders/1rO3ZTTBgyZZhqOx1WCxevM6sE3CrvUcl
- AGENTS.md / docs/DECISIONS.md / docs/CURRENT_PROJECT_STATE.md / docs/SOURCE_REGISTRY.md (main är fortfarande inaktuellt vid migrationen)
- Issue #32: https://github.com/Odourman/mellanrum/issues/32
- Aktuell utvecklar-PR #38: https://github.com/Odourman/mellanrum/pull/38

MAIN III är **samordnare, mottagningsgranskare och beslutsförberedare**, inte automatiskt ROM DEVELOPMENT, oberoende VERIFICATION, PACHINKO eller konstnärlig godkännare. Dokumentationsmigration är inte produktimplementation. Specialistchatten ROM DEVELOPMENT III:s redan uttryckligt godkända implementationsscope förblir separat.

## Tidsordning och användarbeslut
1. MEL-056/Issue32 auktoriserade ny 16 KiB F6-kandidat med bättre 15-rumspussel, ljud, grafik och Närvaron.
2. Användarens senare "Avbryt" stoppade då utvecklingen. PR #34 var read-only-migration.
3. Användaren gav därefter ny uttrycklig full implementationsauktorisation till ROM DEVELOPMENT III; arbetet återupptogs och PR #36 skapades. Det tidigare stoppet är inte aktuellt fortsatt stopp för dessa senare uttryckligen auktoriserade familjer.
4. MAIN II:s videogranskning: skogen alltför T-formad, uggla/markör små, 15 rum för lika visuellt, ljuddramaturgi, coda och Närvaro behöver stärkas. Användaren GODKÄNDE den korta titeln och önskade elektriskt TIA-brus, samt mer harmoni/dissonans och originalkänsla inspirerad av Twin Peaks (inga musikaliska kopior).
5. Användaren valde uttryckligen **KAMPANJ som primärspel**, 3×5 rum, och FRI SKOG som bonus. Träd får förvridas individuellt med inspiration från **Towering Inferno** (1982), men egen grafik och funktionell TIA-kollisionslogik krävs.
6. Därefter gav användaren nytt mandat att göra FRI SKOG till en **mållös, musikaliskt och visuellt interaktiv installation** med joystick/FIRE-kopplade ljud, färg, negativa former, långsam deformation, begränsade blinkningar. FRI får inte tränga undan KAMPANJ.
7. Användaren bad MAIN II att **uppdatera GitHub/Google Drive och migrera till ny MAIN-chatt**. Det är mandat för dokumentations- och koordinationsöverlämning, **inte** en ny automatisk ROM-order eller release.

För historiska formuleringar, se användarens exakta projektkonversationer; nya beslut finns ännu inte korrekt inlagda på main i DECISIONS.md. Bevara tidsordning och scope.

## Nuvarande produktgren – exakt revisionsidentitet
PR #38 (OPEN/DRAFT/UNMERGED): https://github.com/Odourman/mellanrum/pull/38
Branch: romdev/mainii-freeforest-and-campaign-20261123
Source HEAD: 2c70bf7468fc33eed198246281a8ffd0a7cc9252
PINNED source build commit: bacd37102e858e3652097a3aa2608834ef26b609
Checkad F6 NTSC 16,384-byte ROM: rom/bin/MELLANRUM_16K_NTSC_F6.bin
ROM SHA-256: 7e5add7d2580e7ebb3e871a79c13d7ba5680e71354946c941fe79b826e158134
Git blob: 87371e9cbbe584e21a85d855062e50e13721ef17
Pinned dokument: docs/MAINII_FRI_PINNED_ROM.md på PR38-grenen.
**Bytekontroll:** 16,384 ROM-bytes från PR38 HEAD avkodades och SHA-256 beräknades till 7e5add7d... (full ovan). Skilj build-commit från senare test-/dokumentationscommits på HEAD.

Tidigare angivna PR38-video-SHA **4921f723ff989bffaf48e4bebdab36406c83c9f5083588f55f21528fb7e5bba0** avser en ANNAN ROM. Ett ännu äldre mellansteg rapporterade **4934b082bc6557874c2ae40744fefcc12c2af93d04d6776aeacf71d2450ef545**. Varken dessa videoresultat eller äldre PR37-video ska hävdas som final-SHA-visuellt test för 7e5add7d...

## GitHub Actions – exakt vad som är lyckat
Alla nedan avser HEAD 2c70bf... vid kontroll:
- Native DASM + riktiga Stella 15 rum + FRI-profiler: SUCCESS #45264527061
  https://github.com/Odourman/mellanrum/actions/runs/45264527061
- Gopher2600 hela 15-rumskampanjen: SUCCESS #45264527051
  https://github.com/Odourman/mellanrum/actions/runs/45264527051
- 15 × 36,000 no-input Stella-idle-matris: SUCCESS, 15 separata rumjobb #45264527111
  https://github.com/Odourman/mellanrum/actions/runs/45264527111
- Stella Difficulty A/B: SUCCESS #45264527210
- Stella boot smoke: SUCCESS #45264537323
- Legacy full-game Issue15 jämförelse: FAIL #45264537305, felsteget "Check reproducible Issue15 overlay against pinned source art and reference". Kan bero på föråldrat legacy-test, men ska **klassificeras med logg**, inte ignoreras.
- Title/Presence visual capture: FAIL #45264527127, felsteget "Observe title + all three III intrusion rooms in genuine Stella images". **Inte automatisk legacy-friskrivning**; undersök bilder, indata, kompatibilitet och om det faktiskt visar produktbugg.

**Bevisnivå:** DEVELOPER_BUILD_PASS / DEVELOPER_STELLA_CAMPAIGN_PASS / DEVELOPER_GOPHER_CAMPAIGN_PASS / DEVELOPER_IDLE_MATRIX_PASS per namngivna CI-jobb. Grön CI gäller bara exekverade steg; inga oberoende, fysiska eller mänskliga PASS följer därav.

### Öppet eller inte slutbevisat
- **15 kausala motprov på exakt 7e5add7d**: tidigare lokala/CI-rapportering finns för andra SHA; kräver verifiering av just denna SHA och loggar.
- Fullständig värstafallsmätning: 76 cykler/skanlinje, stack/RIOT RAM highwater, F6-hotpots, raster/alternativa tillstånd: INCONCLUSIVE/NOT_RUN tills exakta bevis.
- Faktiska samma-SHA filmer (kampanj med titelåtergång, FRI), individuellt läsbara barrträd och deformationer, U3/S3/markör, närvaron och audioacceptans: MAIN-videogranskning för 7e5add... ännu inte genomförd.
- Mänskligt cold playtest (15 kvalitativt olika pussel), subjektiv ljud/ljus-bedömning, fysisk Atari 2600/RetroN77: NOT_RUN.
- Oberoende Verification/Pachinko på 7e5add...: NOT_RUN. Befintliga #28/#29 gäller PR27-ROM, inte PR38.
- ROM DEVELOPMENT III:s anslutning bröts innan slutrapport; GitHub-arbetet är bevarat, men **mottagningsleveransen är inte komplett**. Läs faktisk CI/artefakter i stället för att tolka framstegslogg som PASS.

## Tidigare kandidater, strikt separerade
- PR37: source HEAD 5be20a9bc1cb7c6ea095657ef8d4ecaf3b42904f, ROM d3754d78ec6c435b4641d4fc281f95a79acff0126c0ad3370db8156c8465853a.
- PR36: source HEAD bc5ad4a118f8909be131163529325055d4e0413e, ROM a14524ce18c4f2575238ed187d7166e903b1209d2d1f3cf4a80044a67e3ad270.
- PR33: source HEAD 48c0d5026d5a9ea22de1ff93028f3e18046e521b; native Actions ROM 962818fa6a8a26eb22a66c66bd3da519467b78f790b149748ea3f036a97d011a; **incheckad binär äldre PR27** 7ce777dc273e1c30d8621843052e941ced41fcf2961bcdf835576a11c9592446.
- PR27 (frozen): ROM 7ce777dc273e1c30d8621843052e941ced41fcf2961bcdf835576a11c9592446.
- Andra PR för äldre utvecklingsfamiljer bevaras oförändrade.

## Konstnärlig kärna / hårdvara
- MELLANRUM: SKOGEN SOM LYSSNAR, Atari 2600 NTSC; KAMPANJ = 3 akter × 5 rum, primär; FRI SKOG = Difficulty B, mållös experimentell bonus; Difficulty A kampanj. Titel kort och frivilligt startad med FIRE, elektrisk TIA-störning.
- Barrträd, sten, autonom U3-uggla med lodrät näbb/tre vingmasker, två S3-symboler, fyra tydligt skilda HUD-markörer, oidentifierbar negativrumslig Närvaro. Indirekt spelarskap, ingen normal fiende, vapen, HP, poäng/boss.
- KAMPANJ måste ha varierade kausala pussel, rättvis feedback, 15 distinkta rum, läsbara träd/uggla/symboler och verklig coda.
- FRI SKOG får ge joystick/FIRE-styrd TIA-musik, harmoni/dissonans, brus, tystnad, långsamma förvrängningar och lokala färg/ljuseffekter. Undvik skarpa frekventa blinkningar, särskilt helskärmsstroboskop; kampanjens resursbudget prioriteras.
- Originalmusik i stämning inspirerad av Twin Peaks, inga kopior/PCM/samplingar. Stereo-inspelad fil ≠ äkta Atari-stereoutgång.
- Stock 6507/TIA/RIOT 128B RAM, max 16 384 byte standard F6 4×4096; inga specialchip/SC/ARM/CDF/DPC; 262 NTSC scanlines och 76 CPU-cykler per scanline som mätkrav.
- Alla 30 tricks utvärderas vid relevant implementation och väljs bara vid faktisk nettofördel.

## Project Sources och gammal status – migreringsrisk
- docs/CURRENT_PROJECT_STATE.md på main har fortfarande "Issue32 authorized NOT_STARTED" och PR27. **STALE**.
- docs/DECISIONS.md på main slutar vid MEL-056, saknar senare avbrott/återstart samt PR37/38-prioriteringar. **INCOMPLETE**.
- docs/SOURCE_REGISTRY.md på main saknar senare kandidater och har äldre historik. **INCOMPLETE**.
- Draft docs-only PR35 och Drive-master "PAUSED WIP" påstår att ROM DEV är stoppad vid PR33. HISTORISKT, INTE NUVARANDE.
- ROM DEV:s PR38-förslag ZIP i Drive: https://drive.google.com/file/d/1owkqh8N-dWjKzs8QNiYcqgvKLB3fsIDZ/view . ZIP skapad före senaste PR38 HEAD och behöver versionsreconciliation.
- Denna migrations-PR uppdaterar ovanstående dokument **endast i docs-only granskningsgren**, inte main förrän separat merge-godkännande. ChatGPT:s faktiska Project Instructions och bifogade Project Sources ändras **inte automatiskt** av GitHub/Drive-dokument.

## MAIN III:s första mottagningsåtgärder
1. Bekräfta access till GitHub/Drive, öppna LIVE repo, Issue32, PR38, Actions och separat Project Sources ZIP; spåra beslutens tidsordning.
2. Läs PR38:s fulla diff, 16KiB ROM-hash, Native/Stella/Gopher/idle artefakter och de två CI FAIL-loggarna; skilj gamla familjens design-/källtester från verkliga produktfel.
3. Begär en **avslutad, samma-SHA** utvecklaröverlämning från ROM DEVELOPMENT III inklusive 15 kausala motprov och korrigerade autentiska videor från 7e5add... eller efterföljande ny ROM-SHA. **Starta inte nytt produktarbete bara för statusrapport**.
4. Gör MAIN:s konstnärliga granskning av faktiskt senaste spelvideo och ljud: träd/Tower­ing Inferno-inspirerad variation, uggla, fas-kollision, markör, Nårvaron, ljud/harmoni/dissonans, kampanjens djup, riktig FRI SKOG och coda.
5. Vid ny final-SHA: separat oberoende Verification och separat Pachinko, därefter användarens konstnärliga och release-beslut.
6. Rapportera PASS/FAIL/NOT_RUN/INCONCLUSIVE och exakta länkar. Ingen merge/tag/release utan användaren.

## Migrationsgräns
Detta är docs-only och auktoriserar inte ROM-bygg, kodredigering, test som produktutveckling, godkännande av ny designcanon, merge eller release. Alla nästa beslut kräver latest authority check.
