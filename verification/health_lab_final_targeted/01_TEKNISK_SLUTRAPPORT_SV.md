# MELLANRUM – slutlig riktad teknisk verifiering av HEALTH LAB
**25 november 2026 | Oberoende VERIFICATION | Svensk beslutsrapport till MAIN IV**

**Slutstatus: `FINAL_TARGETED_VERIFICATION_PASS_BOUNDED`.** Separat gäller `GLOBAL_ALL_PATH_TIMING_INCONCLUSIVE`, `FRI_RAW_PCM_STRICT_AB_INCONCLUSIVE` och `HUMAN_AND_PHYSICAL_NOT_RUN`. Inget nytt bekräftat LAB-specifikt releaseblockerande fel. Ingen produktändring, timerimplementation, RC2-promotion, merge eller release.

Det här är en kompletterande **svensk teknisk rapport**. Den detaljerade instruktions-, klock-, buss- och testbeskrivningen samt samtliga råspår finns i [fullständig teknisk rapport](01_FINAL_TARGETED_VERIFICATION_REPORT.md) och [originalets ZIP](MELLANRUM_HEALTH_LAB_FINAL_TARGETED_VERIFICATION_EVIDENCE_2026-11-25.zip). Nya mätningar får inte blandas samman med tidigare Verification eller Pachinko.

## 1. Identitet och källauktoritet

Båda binärerna är omodifierade NTSC F6-ROM på 16 384 byte. RC1 SHA-256: `456005ed691860b32c44b79f2a71666f622b005f5a798eadf9b549c59cff13bd`. LAB `LAB_STACK_INLINE_PADDED_B` SHA-256: `8a59b84eb5151f78d40e6943c854d7e42c166b531aee3d40432182d32dcdf03b`. Originalkällan `main.asm` har SHA `758d5ad2eb14942d4b2ca6263aa2942ba61f927285291fa51bbedf4e8ff1f01d`, experimentkällan SHA `3246d67a40470454eb56c38f2f4c32fb34ccb4ff38ed796ccb10cf00a647d53e`.

PR #49 är fortsatt öppen Draft, HEAD `d013a0f82621d46ad12674a4a8e944bf005cd9c3`. Produktfilernas Git-blobhashar är oförändrade. Tre tidigare källarkiv från HEALTH, oberoende VERIFICATION och PACHINKO har hämtats och kontrollerats på faktiska bytes: ZIP-CRC PASS, SHA matchar, hela respektive rotmanifest har 1 299/1 299, 1 047/1 047 och 514/514 giltiga payloadposter. Förra verifieringens fyra native DASM-byggen återanvänds **som tidigare bevis**; ingen ny uppsättning DASM-byggen påstås.

## 2. Naturligt bank1-anrop – komplett nytt bussbevis

En autentisk, source-guided controllersekvens når **akt II, rum II-01, frame 5880**, utan RAM-POKE. I samma sammanhängande original-Gopher2600-spår för respektive ROM dokumenteras:

| Kontrollpunkt | RC1 | LAB |
|---|---|---|
| Caller före JSR | PC `$F706`, SP `$FD` | PC `$F708`, SP `$FD` |
| Bank3 `$FF90` | SP `$FB` | SP `$FB` |
| Faktisk F6-bussläsning | `$FFF7`, bank3→1 | `$FFF7`, bank3→1 |
| Ljudbankens inre JSR | skriver `$01FB/$01FA`, SP `$F9` | samma |
| Bankretur | `$FFF9`, bank1→3, `$FF99` | samma |
| Återkomst till caller | PC `$F709`, SP `$FD` | PC `$F70B`, SP `$FD` |

Varje spår innehåller 577 klockobservationer, 182 deduplicerade busscykler, samtliga tio stackbytes och guard `$F5` före/under/efter. Inga nya stackskrivningar träffar `$01F5–$01F7`; 262 scanlines på båda ROM:arna. Tillfälligt överskrivna, **inaktiva** stackbytes får legitimt skilja sig. Ett tidigare felaktigt RC1-breakpoint som använde LAB:s förskjutna PC avvisades och kördes om med rätt PC. **PASS_BOUNDED för ett komplett naturligt bank1-anrop.** Ytterligare ett meningsfullt annorlunda naturligt akt II-tillstånd: NOT_RUN.

## 3. Stackreservens gräns

Tidigare oberoende, kontextkänslig ROM-CFG ger högst **5 samtidiga JSR i RC1, 4 i LAB** inom giltigt källflöde. Ett tidigare naturligt I-01-vittne nådde den djupaste LAB-vägen med SP `$F7`, medan RC1:s femte JSR nådde `$F5`. LAB:s två reserverade stackbytes `$F6/$F7` används inte som extra spelvariabler. Nya bank1-vittnet stannar vid SP `$F9`; det stärker resultatet men är inte en ny fullständig all-path-attest. **PASS_CONDITIONAL för giltigt programflöde.**

## 4. OwlTryNext: faktisk konsekvens av den sparade cykeln

Naturlig FRI SKOG-sekvens, Difficulty B, **frame 2142**. Tagen `BCS OwlTryNext`: RC1 **4 cykler**, LAB **3 cykler**. Därefter är `WaitVBlank`-starten samma SL18 CL−41, första verkliga CPU-`INTIM` ger 20 i båda, exit samma SL34 CL88, `VBLANK=0` samma SL35 CL−53, första synliga PF0 samma SL35 CL76 och 262 scanlines på båda.

**Viktigt mätfynd:** Innan denna synkronisering nås skriver LAB **sex TIA-ljudregister tre färgklockor tidigare** än RC1 i samma naturliga frame2142. Samtliga värden är identiska. Den autentiska CPU/TIA-bussloggen registrerar **258 ljudregisterskrivningar per ROM över 43 bildrutor**; de första 252 har identiska tider och värden, de sista sex är tidigarelagda i LAB. Cykeln har alltså **verklig intern ljudeffekt på skrivpositionen**, men ingen observerad missad synlig deadline. Detta är varken total timingparitet eller ett bevisat hörbart ljudfel. **PASS_BOUNDED för synlig fortsättning; verklig ljudtimingskillnad dokumenterad.**

## 5. Fyra naturliga rumsinläsningar med sidgränspåslag

| Rum | Naturlig frame | Indexerad läsning | Ny kostnad |
|---|---:|---|---:|
| I-02 | 964 | `GeoMapHi,X=1` | 4→5 cykler |
| I-03 | 2497 | `GeoMapHi,X=2` | 4→5 |
| I-05 | 4483 | `RoomStoneY,X=4` | 4→5 |
| II-01 | 5872 | `RoomStoneY,X=5` | 4→5 |

Alla fyra har mätts **naturligt på båda ROM:arna** med full kedja till faktisk RIOT- och TIA-buss. Den extra cykeln absorberas under den normala synkroniserande VBLANK-väntan. Verklig CPU-läsning av `INTIM=$0C` inträffar SL25 CL−29 i både RC1 och LAB, väntan avslutas SL34 CL88, VBLANK stängs SL35 CL−53, de första PF0/PF1/PF2-busskrivningarna har samma värden och beampositioner. **Åtta kompletta 262-linjers övergångsbilder och fyra matchande A/B-händelser. PASS_BOUNDED.**

Denna nyare kontroll ersätter inte tidigare sann data om titelns 64 skrivningar som flyttades +3 färgklockor: de hade mätt marginal minst 32 färgklockor till relevant PF-segment och inga pixelskillnader, men kördes inte om nu. Sidgränsavgifterna för GeoMapHi och RoomStoneY är på skilda giltiga index och summeras inte automatiskt inom samma LoadRoom.

## 6. HUD x9, terminal rendering och negativa orakel

En ny naturlig Gopher2600-körning kontrollerar uttryckligen **låst `fireX=9`**, inte bara rörlig `cursorX=9`. RC1 och LAB har RESP0-busskrivning **SL214 CL151** och **262** scanlines; den separata gamla PR47-negativa kontrollen ger förväntade **263** scanlines och senare RESP0-skrivning. Det visar att metoden kan upptäcka det konkreta gamla felet.

Tio nya riktade LAB-scenarier ger alla 262 scanlines och samma observerade RESP0-tid: **ett naturligt** och **nio uttryckligt RAM-forcerade diagnostiska**, med bland annat ack accepted/denied, pending, Presence/interception, echo/phase och beat54/55. Forceringen är **inte bevis för naturlig nåbarhet**. Tidigare oberoende, giltig `Stem13`-väg ger 75/76 CPU-cykler och HUD x9:s sista WSYNC 76/76, **noll ytterligare marginal**. Terminal `StemLastFast` använder avsiktliga flera rasterrader, så en sammanslagen flerradscykelsumma kan inte jämföras med en scanlinegräns som om allt vore samma rad. **PASS_BOUNDED för nya mätningar; global alla nåbara kombinationer INCONCLUSIVE.**

## 7. FRI SKOG: fyra nya Stella-ljudfångster

Två helt separata färska Stella-processer per ROM kördes med samma Difficulty B och controllerinput: **2 400 verkliga callbacks per process**, **1 257 076 stereo-PCM-frames** per inspelning vid 31 440 Hz, alltså **2 514 152 int16-värden** per körning. Antal ljudframes, bildcallbacks och controller-RLE stämmer.

| Rå jämförelse | Olika int16-värden |
|---|---:|
| RC1-A mot RC1-A2, **samma ROM** | **694 036** |
| LAB-B mot LAB-B2, **samma ROM** | **752 110** |
| RC1-A mot LAB-B | 744 868 |
| RC1-A2 mot LAB-B2 | 689 758 |

Alla sampelcheckpoints för bilder överensstämmer inom respektive samma-ROM-par. LAB:s råa RAM-checkpoints matchar; RC1-paren skiljer en gång vid frame900 trots likadan provtagen bild och detta har inte dolts. Därför är **strikt FRI-PCM-A/B ett otillförlitligt orakel och INCONCLUSIVE**. Den tidigare fullständiga kampanjens 20 594 248 identiska PCM-värden gäller endast det tidigare deterministiska kampanjscenariot. Den verkliga sexskrivningars ljudbussförskjutningen ovan kvarstår som separat faktum; mänsklig hörbarhet är NOT_RUN.

## 8. Avgränsning, negativa test och källa till siffror

De tidigare oberoende 15/15 kampanjvinsterna på båda emulatorerna, 19 652 identiska fullbilder, 540 000 idle-frames, 15 kausala/SELECT-prover, U3 och markörer samt Pachinkos 105×2 profilstress är **tidigare, checksumslåsta bevis**. De har inte fått status `NEW` i denna komplettering.

Nytt material omfattar de två kompletta bank1-kedjorna, två Owl-fortsättningar, fyra naturliga rumsindex inom vardera ROM:s **en** 5 880-frame-controllertransport, tre nya x9-positiv-/negativkontroller, tio korta terminala scenarier, fyra nya Stella FRI-ljudfångster och två 43-frame-spår med verkliga ljudregisterskrivningar. En `TV FRAME`-avläsning räknas inte som en ny unik spelbildruta. Maskinmatrisen har 41 rader och skiljer `NATURAL_CONTROLLER`, `SOURCE_GUIDED_CONTROLLER`, `FORCED_RAM_DIAGNOSTIC`, gammal evidens, `NOT_RUN`, `INCONCLUSIVE` och ett korrigerat testharnessfel.

## 9. Slutliga svar till MAIN IV

**Nytt bank-, stack-, 262-linje-, spelflödes- eller synligt TIA-releaseblockerande fel?** Nej, inget sådant har reproducerats inom de giltiga prov som genomförts. Det är inte ett matematiskt frånvarobevis.

**Fullständigt naturligt bank1-anrop?** Ja, ett på varje ROM, inklusive CPU-hotspots, riktig stackbuss och korrekt yttre retur-PC; ett andra distinkt tillstånd har inte körts.

**Är stackförbättringen verklig?** Ja inom tidigare källgiltig analys och observerad naturlig maximal kedja: 5→4 JSR, två reservbyte. Reserven är inte nytt allokerbart RAM.

**Var tar de förskjutna cyklerna vägen?** De fyra +1-kostnaderna vid rumsinläsning absorberas vid timerväntan innan synlig raster. `OwlTryNext` −1-cykel flyttar sex verkliga ljudskrivningar tre färgklockor tidigare men är absorberad före synliga PF-skrivningar i den uppmätta naturliga FRI-bildrutan.

**Har global timing bevisats?** Nej. Särskilt x9-HUD har noll CPU-cykelmarginal i den tidigare giltiga vägmodellen och alla naturliga sammanfallande Presence/echo/pending/terminaltillstånd är inte uttömmande analyserade.

**Är FRI ljudparitet säkerställd?** Inte som strikt rå-PCM över oberoende processer; samma-ROM varierar kraftigt. Den verkliga TIA-registerskrivtidsskillnaden är uppmätt, men ingen hörbar regressionsbedömning har utförts.

**Vilket beslut rekommenderas?** LAB med sin **verkliga tvåbyte-stackreserv** är rimlig som *teknisk experimentbas* för ett **separat uttryckligen auktoriserat framtida** tidtagar-genomförbarhetsuppdrag, inte som accepterad RC2 eller färdig produkt. RC1 förblir fryst produktreferens. Riskerna ovan ska delges användaren. Fysisk original-Atari, RetroN77, mänsklig cold-play I-05 och mänsklig ljud-/konstacceptans är alla **NOT_RUN**.

## 10. Rapport och originalbevis

- [Fullständigt ZIP med verkliga råa native CPU/TIA-/RIOT-loggar, reproduktionsskript, ROM-bytes, source snapshots, tidigare DASM-listningar, fyra WAV, exakta CSV/JSON och hela SHA-manifestet](MELLANRUM_HEALTH_LAB_FINAL_TARGETED_VERIFICATION_EVIDENCE_2026-11-25.zip): **951 526 byte**, SHA-256 `200730e9ffe2d2467111289a5f30f7be4200ca7ebf72eef1f147a914c510ccf8`, 239 ZIP-poster, 238/238 SHA256-payload, CRC PASS. Binär Git-blob `934a142f49f1df9f117df5d0c3ab435ca7fcbeeb` verifierad.
- [Maskinläsbar 41-raders testmatris](02_TEST_MATRIX.csv), [detaljerad riskdisposition](03_REMAINING_RISK_DISPOSITION.md), [reproduktion](04_REPRODUCE.md), [harness-/negativa kontroller](05_FAILURE_REPRODUCTIONS.md).
- [Svensk kort handoff också i MELLANRUM:s Google Drive-mapp](https://docs.google.com/document/d/1eTcqwt-C9fMhBUW5SI6dzPpW-rZnAhnRFgt_w0rexaY/edit). Direkt Drive-uppladdning av ZIP avvisades av filreferensvalideringen; GitHubs originalbytes är åtkomliga. Ingen Drive-ZIP-länk hittas på.

**Ingen produktkod, fryst PR, mapper, spelregel, trädgrafik, ROM-byte, taggning eller release har ändrats. Inga senare specialistfaser har startats.**