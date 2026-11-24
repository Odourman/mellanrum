# MELLANRUM – VERIFICATION #42: riktad CPU-/TIA-timing och sen WSYNC

**Datum:** 2026-11-24. **Mottagare:** MAIN III. **Roll:** oberoende VERIFICATION, **ej ROM DEVELOPMENT/PACHINKO**. **Övergripande:** P0 TIMING PARTIAL / global all-path INCONCLUSIVE / ingen releaseattest. Det här är ett nytt och begränsat testuppdrag enligt MAIN III Issue #42 kommentar `7132704046`. Tidigare stack/fem-JSR och F6 fullkampanj återanvänds endast som versionsbundet tidigare bevis, inte som ny testkörning.

## Frysning av produkt

- Draft PR #38 HEAD: `6e9db179867234a19cce329c709170f2423ffbbb`.
- Produktcommit: `9293c46eb323f47197046e07e1178279d6c7f525`.
- Oförändrad `rom/bin/MELLANRUM_16K_NTSC_F6.bin`, **16 384 byte**, NTSC standard F6.
- **ROM-SHA-256:** `bfdeb5308dcecc526e802cd95886b94e0ce4953628e7bc7190c5d49231deac06`.
- Original-ROM kontrollerades med Python `hashlib` före alla prov. GitHub Actions kontrollerade samma ROM-hash och Git blob `51dc00b5ce8170b289acd0b4d997e0c6080b8f54` samt `git diff --exit-code` mot PR38 HEAD för produktkällorna. Ingen produktändring har gjorts.
- Native Gopher2600 Linux `unreleased`, source `74c544203378c1448a33c29bc8b4586079b050f4`, exe SHA `7b12dff57fcb73154122d2477f35d9c8ae8b344649bc0faa8ff6f5663c70470b`.
- Native Stella/libretro `8.0_pre 8dd5600`, core SHA `2130ed1153cef66ef3f34bf9063f675f1f3342bc18320eb9ae5101743e3042df`.

## A. Verklig CPU-/rastermatris – 52 + 8 lokala fall

1. **52/52 självständiga Gopher2600-instruktionsbildrutor:** 15 rum × `BASELINE`, `PRESENCE_ACTIVE`, `OVERLAP_PHASE`; plus sju `ECHO_STRESS` i rum 0,4,5,9,10,12,14. **205 824** faktiskt loggade CPU-instruktionsgränser och **10 452** WSYNC-händelser. **52/52** hela bildrutor = 262 NTSC scanlines, exitcode 0. **0** överhoppade WSYNC, även i den synliga ritkärnan. Scenernas rums-/Presencetillstånd sattes via **explicit `FORCED_RAM_DIAGNOSTIC` POKE**. De är INTE 52 controller-nådda pussellösningar och kan inte accepteras som mänsklig spelbarhet.
2. **Ytterligare 8 lokala original-ROM-fall** med verklig Gopher instruktionstiming: 31 090 instruktionsobservationer; 8/8 med 262, 0 synligt hoppad WSYNC. Dessa nådde aktiverade skuggberäkningar i samtliga åtta logiska rader, med (a) vanlig aktiv Närvaro, (b) FIRE, (c) ändrad fas, (d) fyllda eko-slots och FIRE, (e) varningsläge, (f) akt I, samt riktigt controller-startad titel och FRI. All tvingad RIOT RAM tydligt separat DIAGNOSTIC. Spåren visar för aktiv skugga `F859/F85C` 8× och i symbolraden `F867/F86F` 1×, alltså inte bara ett test där skuggberäkningen var avstängd.
3. **Ny oberoende GitHub Actions-omkörning, råartefakt tillgänglig:** run [#45404953206](https://github.com/Odourman/mellanrum/actions/runs/45404953206) **SUCCESS**, verifierad efter loggläsning och ny nedladdning av artifact `14925600592`. Åtta riktade scenarier **31 074** CPU-instruktionsobservationer och **1 549** WSYNC-händelser, **8/8 262**, **0 hoppad synlig WSYNC**. En enda sen VBLANK-WSYNC vid `$F68C` som väntar två scanlines. **25/25** SHA256-manifestposter omräknade korrekt. Denna körning är en ny faktisk emulatorprocess; inte bara det tidigare lokala materialets vidarekopierade PASS. Historiska initiala CI-försök #45404691279 (shallow checkout) och #45404797578 (saknade SDL2-bibliotek på runner) var **INFRASTRUCTURE FAIL**, inte produkt-FAIL, och de ersätts av den faktiskt framgångsrika körningen.

**Bevismaterial, verifierbara på GitHub:** [testkod](https://github.com/Odourman/mellanrum/blob/verification/issue42-pr38-bfdeb-20261124/verification/issue42/timing_native_gopher.py), [separat CI-workflow](https://github.com/Odourman/mellanrum/blob/verification/issue42-pr38-bfdeb-20261124/.github/workflows/verification42-p0-timing.yml), [run #45404953206 och ZIP-artifact](https://github.com/Odourman/mellanrum/actions/runs/45404953206). Råloggar innehåller varje instruktions PC, register, SP, absolut TIA `FR/SL/CL`, varje testkommando, resultat-JSON och checksummor. CI använder en exakt SHA-låst Gopher-binärram hämtad från tidigare repository-artifact (GitHub artifact ID `14780574047`), original-ROM från PR38-verifieringsgren, och `ubuntu-24.04` med installerad SDL2.

## B. DASM-listning och beräknade cykelvägar

`kernel_cycle_envelope.py` läser **verklig native DASM bank3.lst**, verifierar opcodes mot oförändrade BFDEB-bank3-bytes och går igenom 19 WSYNC-startpunkter i spel-/titelkerneln. Villkorliga hopp grenas konservativt i båda riktningar och page-cross-tillägg läggs på indexläsningar. Den rena överapproximationen ger **tre påstådda möjliga överskridandekandidater** (`F83C`, `F90E`, `F9CF`). **Dessa är inte verifierade produktfel:** den ursprungliga modellen tillåter samtidiga oförenliga branchutfall, felaktiga sidgränspassager och låter sista radens housekeeping löpa över naturlig scanlinegräns som om det vore en vanlig WSYNC-loop. Slutlig universell worst-case-bevisning är därför INCONCLUSIVE.

**Riktad förfining F83C→F87A (tredje kronlinjen/skugga/symbol):** `pfbuf` ligger vid `$0080`, `pfIndex` är `0,6,...42`, läsindex Y blir högst 47; tabellerna `ShadowCrownOr $FF1E` och `ShadowCrownAnd $FF36` använder `workY<=23`. Ingen av dessa indexläsningar kan korsa en 256-byte-sidgräns inom giltig renderingsdata. Genomgång med båda branchutfall fortfarande öppna ger **max 69 CPU-cykler fram till nästa `STA WSYNC`**, plus skrivinstruktionens 3 = **72/76 cykler**. **PASS för denna begränsade WSYNC-delsträcka med giltiga tabellindex**, bekräftad mot uppmätt verklig aktiv-skugga/symbol i Gopher (startcykel 67 + 3 = 70).

**Sprites/stammar F90E, normal X>1-väg:** käll- och operandbaserad cykelsumma för loopens renderingsväg är **65 cykler fram till nästa `STA WSYNC`**, inklusive de två `NOP`, båda `(ptr),Y`-markörläsningarna och den andra P1-spriten. Pointertabeller i `FE81..FEC0`/`FF7E..FF87` samt `SpriteRowIndex $FA45` har inom giltiga rowindex Y<=8 och X<=9 ingen sidkorsning. `STA WSYNC` kräver ytterligare 3 => **68/76 cykler**. **PASS för vanliga X>1-loopvarv, ej universellt för exit X=1**. Den sista raden (`X=1`, `StemLastFast`) har separat book-keeping/övergång till nästa rad eller HUD; där kan en vanlig CPU-räkning passera naturlig scanlinegräns utan att automatiskt visa produktfel. Emulatorspåren har inte påvisat synlig radförlust.

**Titeln F9CF:** Gopher-testet i riktigt, icke RAM-tvingat titelläge observerar sju teckenrader × åtta rader, högsta WSYNC-startcykel **66**, fullbordat senast cykel **69**. Exakta title-tabelladresser visar att den naiva page-cross-modellens sex möjliga extracykler inte inträffar samtidigt; höger PF0 `$FEFB+Y` kan däremot passera vid Y=5/6, vilket syns som 1 verklig cykel extra. **PASS för exekverad titelväg, ingen global proof för andra tänkbara minnesförhållanden.**

## C. Reproducerad sen `STA WSYNC` `$F68C`

Den tidigare genuina Gopher-instruktionstidsdiagnostiken gav **2/2** reproduktioner av `STA WSYNC`, bank3 PC `$F68C`, scanline 6, `CL=157` / CPU startcykel 75; nästa instruktion utfördes först scanline **8** (hopp över 7). Ny GitHub Actions-körning ger **ytterligare 1/1** genuin reproduktion under samma diagnostiska aktiva Närvarotillstånd. Detta inträffar **under VBLANK**, när den källkodsstyrda `WaitVBlank` synkroniserar mot RIOT-timer före att `VBLANK` avaktiveras.

**Strikt Gopher-differens av ordinarie mot tvingad aktiv Närvaro:** samtliga jämförda vertikala renderingspunkter (`F7C7`, `F7D6`, `F7F8`, `F83C`, `F87A`, `F89B`, `F90E`, `F963`, `F98E`) började på **samma absoluta scanlines**, däribland första spelraden på **scanline 51** och nedre HUD kring 212–221. Scenen slutade **262** i båda varianterna.

**Verkliga Stella pixlar i två egna färska originalspel-emu-processer:** samma ROM och kontrollingångar; enda skillnaden före sista spelbildrutan var RIOT-RAM `presence=0` kontra `presence=2` (**FORCED_RAM_DIAGNOSTIC**, inte controller-nådd). Autentiska 160×228 PNG. Exakt **256** av 36 480 bildpunkter skilde sig, samtliga på bildrader **14–29** i avsiktlig övre Presence-HUD. **Bildrader 30–227 är pixelidentiska (198 rader)**, och övriga indata är identiska. Detta är specifikt relevant: ingen vertikal shift av synlig playfield/sprites kan hänföras till sen VBLANK-WSYNC i just detta par. **PASS att fallet inte orsakar synlig bildförskjutning i denna reproduktion**, **inte PASS för alla varianter eller subjektiv spelkvalitet**. I skugg-aktiva varianter varierar själva PF2-utseendet avsiktligt, vilket måste skiljas från timingkorruption.

## D. Öppna risker och avgränsningar

| Grind | Status | Täckning/begränsning |
| --- | --- | --- |
| Exakt produktidentitet och tidigare oberoende DASM | **PASS** | BFDEB SHA och original-DASM-listning; produkten oförändrad |
| Tidigare max fem JSR, giltigt kontrollflöde | **PASS VILLKORAT (REDAN ACCEPTERAT)** | Ingen onödig omkörning |
| 52 extra native Gopher envist svåra kombinationer | **PASS AVGRÄNSAT** | 52/52 × 262, 205 824 instruktioner, 10 452 WSYNC; 52 är forced-room diagnosis, inte fulla kampanjer |
| Åtta mer fokuserade verkliga shadow/FIRE/echo/title/FRI | **PASS AVGRÄNSAT** | 8/8 ×262, 0 synliga WSYNC-skips, shadow/symbol verklig exekvering |
| Ny extern nyckelbar GitHub CI + råartefakt | **PASS** | Run #45404953206, 31 074 instruktioner, 1549 WSYNC, 25/25 SHA manifest, original råloggar kan hämtas av MAIN |
| Specifik kron/Presence/symbol WSYNC F83C→F87A | **PASS VILLKORAT** | worst 72/76 cykler vid verifierade giltiga index |
| Normal sprite-/stamloop X>1 | **PASS VILLKORAT** | 68/76 cykler inklusive WSYNC, utan pointer page cross |
| Titel i original emulator | **PASS AVGRÄNSAT** | 56 dynamiska glyph WSYNC, start <=66, STA klar <=69 |
| Sen VBLANK-WSYNC `$F68C` upptäckt | **PASS REPRODUCERAT** | 2/2 tidigare + 1/1 ny CI, en extra VBLANK-linje |
| Synlig vertikal förskjutning från just sen WSYNC | **INGET PÅVISAT FEL / PASS AVGRÄNSAT** | 9/9 uppmätta absoluta kernel-positioner lika; Stella y30..227 pixelidentiskt i jämförbart prov |
| **Global matematisk worst-case för hela renderkärnans samtliga kombinationer** | **INCONCLUSIVE** | Sista stamrad/transition, titelns sista glyphrad, `F83C` med ogiltiga korrupta tabellindex, alla alternativa branch-/TIA-skrivtimingar ej fullständigt formellt stängda |
| Alla samtidigt controller-nådda Presence+FIRE+eko+fas-/rumsbyte, alla markerformer | **INCONCLUSIVE / NOT_RUN** | Enstaka verkliga Gopher/Stella-sammanfall; många svåra tillstånd var forced RAM, inte bevisad ordinarie rumsstart |
| Ny fullständig Stella-CPU-cycle-debugger över alla bildrutor | **NOT_RUN** | Genomförda Stella-proven visar riktiga bildpunkter, inte en CPU-instruktions-API |
| Original-Atari/RetroN77, mänskligt cold play, artistiskt ljudgodkännande | **NOT_RUN** | Separata processer, ingen releaseorder |

**Viktigt:** Den konservativa kodmodellen saknar tills vidare värde-/kontrollflödeskoppling för alla x-/y-register, alla tabellindex, vågräta HMOVE-/P1-renderingsstunder och TIA-objektkollisionsgrenar. Därför är 76-cykelgrinden globalt **INCONCLUSIVE** även om ingen synlig avvikelse påvisats i genomförda verkliga tester. Om nya specifika fel demonstreras ska de sparas två gånger och minimeras före produktfelklassificering.

## E. Leverans till MAIN III

- Real native GitHub Actions [run #45404953206](https://github.com/Odourman/mellanrum/actions/runs/45404953206) SUCCESS, råartefakt ID **14925600592**, bevis i GitHub och 25/25 checksumsposter lokalt nedladdade och omräknade.
- [GitHub testskript](https://github.com/Odourman/mellanrum/blob/verification/issue42-pr38-bfdeb-20261124/verification/issue42/timing_native_gopher.py) och [workflow](https://github.com/Odourman/mellanrum/blob/verification/issue42-pr38-bfdeb-20261124/.github/workflows/verification42-p0-timing.yml) i **egen verifieringsgren**, ingen ändring av `rom/src`, `rom/f6`, `rom/bin`.
- Kompletterande självständig lokal ZIP: minst 52× original Gopher `stdout.log` + commands/result, åtta extra deep-shadow-case, konservativ och indexförfinad DASM-cycleanalys, Stella originalbilder/diff, manifest med fulla SHA. Avsiktligen inte kallad en GitHub-artefakt innan någon faktiskt laddar upp den; MAIN kan redan läsa 8-case råartefakt genom ovanstående Actions.

**Rekommendation:** Avför sen VBLANK-WSYNC som **bekräftad synlig ROM-defekt**; någon sådan har inte reproducerats. Godta säkra, avgränsade kernel-delsträckor och exakt råartefakt. Behåll global 76-cykel- och alternativa samtidiga spelhändelser som **INCONCLUSIVE**; ingen spekulativ patch, ingen merge eller release utan användarens separata beslut.