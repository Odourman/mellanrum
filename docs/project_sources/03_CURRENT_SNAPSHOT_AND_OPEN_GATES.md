# MELLANRUM – status och öppna grindar
**As-of: 2026-11-23 cirka 18:00 CET.** Detta är en ögonblicksbild, inte ett självläkande statusregister. LIVE-PR, commits, CI, användarorder och Drive måste omkontrolleras före varje framtida beslut.

## Sammanfattning
**STATUS: ISSUE32-WIP FRYST EFTER "AVBRYT" / ROM DEVELOPMENT III-MIGRATION ENDAST / PR33 EJ RELEASEKLAR / NO MERGE / NO RELEASE.**

| Objekt | Versionsbunden sakuppgift | Bedömning |
| --- | --- | --- |
| [main](https://github.com/Odourman/mellanrum/tree/main) | HEAD  e1f70ccd7bab353fbe2232612c408683a41d937f | Statusfil på main är inaktuell för PR33 |
| [Issue #32](https://github.com/Odourman/mellanrum/issues/32) | MEL-056, full redigering av ny 16K-kandidat | Auktoriserade tidigare arbete; därefter stopp genom "Avbryt" |
| [Draft PR #33](https://github.com/Odourman/mellanrum/pull/33) | kodgren romdev/issue32-finish-game-20261123, HEAD 48c0d5026d5a9ea22de1ff93028f3e18046e521b | OPEN, DRAFT, UNMERGED, WIP STOPPED |
| [Actions #45184894712](https://github.com/Odourman/mellanrum/actions/runs/45184894712) | Issue32 native F6, HEAD 48c0d..., Actions success | BUNDEN UTVECKLAREVIDENS, INTE RELEASEBEVIS |
| Native ROM i [Actions-artefakt #14823930347](https://github.com/Odourman/mellanrum/actions/runs/45184894712/artifacts/14823930347) | 16 384 B, SHA-256 **962818fa6a8a26eb22a66c66bd3da519467b78f790b149748ea3f036a97d011a** | Nya PR33-källans byggda ROM |
| Incheckad rom/bin/MELLANRUM_16K_NTSC_F6.bin i PR33 | Fortfarande gammal Git blob 958d7505e5e1af7fbf43cb2e1d8571aa9e12c6b5, SHA-256 **7ce777dc273e1c30d8621843052e941ced41fcf2961bcdf835576a11c9592446** | **FEL BINÄR FÖR PR33-KÄLLAN**; åtgärdas först efter nytt tillstånd |
| [Draft PR #27](https://github.com/Odourman/mellanrum/pull/27) | HEAD 178d915a5395e2b62857886a3c60dd254af858d2; 16K F6 ROM 7ce777dc... | Fryst föregångare; egen utvecklarevidens |
| [Draft PR #34](https://github.com/Odourman/mellanrum/pull/34) | docs-only; HEAD 83cf0bf639ff51087535e2ef30dfcf35ce748662 | ROM DEVELOPMENT III-migration; inte kod eller återstart |
| [Google Drive handoff](https://docs.google.com/document/d/1kMoR4sjaRHr0XZ8YyZQ0cotdJormmApPD7600Q5jImM/edit) | stoppad migrationsrapport, senast 2026-11-23 | Underbyggd handoff, underordnad användarbeslut |
| [Drive-artefaktbackup](https://drive.google.com/file/d/1M9eBl579Jq6MvUQg2sehABIV24c3IUiH/view) | ZIP-kopia av native Actions-evidens, 4 663 228 B | Kopia; kontrollera bytes/SHA före användning |
| [Verification #28](https://github.com/Odourman/mellanrum/issues/28) och [Pachinko #29](https://github.com/Odourman/mellanrum/issues/29) | låsta till **PR27 7ce777dc...**, inte PR33 962818fa... | Kan **inte** certifiera PR33 |

## Vad som finns i WIP-koden enligt granskad PR/handoff
- 15 ändrade rumsavslut med orsaksvillkor kring stenbesök, polaritet, eko och fas, samt ändrade modellösningar.
- Markör i nedre HUD med P0-8×8-former ring / bock / X / bruten Närvaro; positionering med M0. Källmässigt större skillnad från PR27:s M0-bredd; verklig jämförbar 1×-acceptans saknas.
- Tydligare barrträd, mörkare tredje akt, längre ~34 s TIA-modulation, modifierad coda.
- Spelet är fortfarande gjort för tre akter och 15 rum, autonom U3-uggla och negativrumslig Närvaro.

## Bevisnivå, inte påstådda helhets-PASS
**Kontrollerad utvecklarevidens enligt migrationens arkivgranskning:**
- GitHub Actions workflow #45184894712: SUCCESS på specificerad HEAD.
- Arkivet är enligt handoff ZIP-CRC-kontrollerat; ny 16 384 B ROM re-hashad till 962818fa...
- Riktig Stella-utvecklargenomspelning **15/15**, 19 412 emulerade bildrutor, coda→titel, med joystick/FIRE och original PCM enligt artifactsammanfattning.
- Inbyggd exakt Stella-NTSC-scanlinegranskning är uttryckligen **NOT_RUN**.

**Rapporterat men inte självständigt bekräftat som komplett:**
- Gopher2600 15/15 och 278/278 prover med 262 skanlinjer.
- No-input/critical-omission endast för påstått 10 av 15 rum; återstående fem samt full sammanhängande slutmatris saknas i mottaget bevis.
- Ett tidigare 264-line HUD-fel har fått en källkodskorrigering `HUDBottom7` 7→5, men komplett värstafallskontroll och oberoende replikering återstår.

**UTTRYCKLIG FAIL/EJ GODKÄND MEDIA:**
- Den lokalt producerade 5m29s MP4 med namn `MELLANRUM_ISSUE32_FULL_REAL_STELLA_TIA_1PANE.mp4` har avkodats till nära helsvarta gameplay-bilder vid flera tidpunkter. **INVALID/REJECTED; får aldrig visas som verifierad spelvideo**.
- Skärmbilder av fyra markörformer från skilda tillfällen uppfyller inte kravet på samma-scene/samma läge och faktisk 1× jämförelse.

**ÖPPNA/NOT_RUN:** oberoende PR33 Verification + Pachinko med exakt nya SHA, samtliga 15×36 000-framestester utan input, 15 kausala motprov, fel- och alternativa handlingssekvenser, värstafalls 76 cykler per scanline och stack-/RAM-highwater, fysisk Atari/RetroN77, PAL, korrekt video, TIA-lyssningsacceptans, mänsklig förstagångstest, konstnärligt användargodkännande, release.

## Kritisk statuskonflikt
[CURRENT_PROJECT_STATE.md på main](https://github.com/Odourman/mellanrum/blob/main/docs/CURRENT_PROJECT_STATE.md) skriver fortfarande "Issue32 authorized/not started" och främst PR27. Detta är **STALE** jämfört med live PR33, run 45184894712, dokumentations-PR34 och senare "Avbryt". Korrigera huvudregistret i en godkänd **dokumentationsuppdatering**, men låt inte denna Project Source tyst ändra historiskt beslutsdatum, slå samman ROM-SHA eller hävda release.

## När en mottagare vaknar
Kontrollera aktualitet först. Om status eller SHA skiljer sig, markera denna fil STALE, använd live källa, rapportera nytt faktum till MAIN. Utredning/läsning av gamla artefakter är något annat än att återstarta stoppad implementation.
