# MELLANRUM HEALTH IV – slutlig resursåtervinning och timerprototyplabb

**Roll:** HEALTH  
**Status:** `TIMER_NO_GO_WITHIN_TESTED_CONSTRAINTS`  
**Datum:** 2026-11-26  
**Behörighet:** isolerade, reversibla experiment godkända av denna order. Ingen ändring av RC1/PR49, `main`, releasegren, regler eller kanon.

## Sammanfattning

HEALTH III hade bara visat att tre raka `DS 1`-deklarationer landade på skyddad stack (`$F6–$F8`). Det var inte ett bevis för att varje säker liveness-/komprimeringslösning var omöjlig. HEALTH IV provade därför faktisk källkod för A1 (`exitX`), B1 (pekardelning), C2 (bitpackning), en separat sentinel-diagnostik samt offline RLE-packning av alla scorebytes.

Resultatet visar en verklig RAM-byte-vinst, men den räcker inte för minsta timerbehovet. B1 och kombinationen A1+B1 överskrider bank 3:s fasta `$FF90`-trampolin. Två inputflaggor kan packas till en byte, men patchen växer kod med netto 15 byte över tillgänglig bank 3 före justeringar för font/timer. Timerkärna och renderer byggdes därför inte; de skulle vara pseudoresurser utan konkret placering. Sluttidens SELECT-återhämtning kräver dessutom en snapshot under mode 2, när liveklockan fortsätter.

## Låsta identiteter och källkontroll

- Projekt: `Odourman/mellanrum`; aktuell LAB är `LAB_STACK_INLINE_PADDED_B`.
- `main.asm` SHA-256: `3246d67a40470454eb56c38f2f4c32fb34ccb4ff38ed796ccb10cf00a647d53e`.
- Clean native LAB ROM: 16,384 B F6 NTSC, SHA-256 `8a59b84eb5151f78d40e6943c854d7e42c166b531aee3d40432182d32dcdf03b`.
- RC1 jämförelse: SHA-256 `456005ed691860b32c44b79f2a71666f622b005f5a798eadf9b549c59cff13bd`; Draft PR49, live HEAD `d013a0f82621d46ad12674a4a8e944bf005cd9c3`, open/draft/unmerged vid kontroll. Ingen skrivning gjordes dit.
- DASM 2.20.14.1 SHA-256 `cfb23732297a4fe1c8d4a78d44206037d97733aedb2772503bbf029a4aa91291`. Stella/libretro 8.0_pre `8dd5600`, core SHA-256 `2130ed1153cef66ef3f34bf9063f675f1f3342bc18320eb9ae5101743e3042df`. Gopher2600 SHA-256 `7b12dff57fcb73154122d2477f35d9c8ae8b344649bc0faa8ff6f5663c70470b` (ingen ny Gopher-körning i HEALTH IV).
- HEALTH III Drive ZIP `1h-GH9l552CGNv0Rc2577zd4dOcQMUhtb`: Drive-metadata angav 41,749,484 B; lokal återanvänd evidens-ZIP har SHA-256 `a3fd35f80ab424931dce2d74e273862f82475eb609038b031ff2fe9e563e8fa2`, samma storlek, `unzip -t` PASS. Tidigare G0 och testresultat förblir historiska, inte ny timer-PASS.

## Resultat per hypotes

### A1 – konstant utgångskolumn

Källinventering över alla assemblerfiler fann endast symbolens deklaration, initiering i `LoadRoom` och två spelregeljämförelser; inget `$C1`-hårdkodat alias hittades. Alla 15 rum laddar `#8`, FRI går runt utgångschecken, och room/coda/reset-övergångar ändrar inte kolumnen. Sentinel-prov bekräftar att score-/spelkörning inte skriver den tidigare variabelplatsen under det testade fulla förloppet.

Fysisk adress i LAB är `$C1`. A1 ersätter variabeln med `timerSlotA` på samma plats, tar bort fyra kodbyte (`lda #8` + `sta exitX`) och byter två `CMP zp` (3 cykler) mot `CMP #8` (2 cykler). ROM byggs som 16,384 B F6; SHA `68f945ade7441ea8c59b4ccdecf216af8a06d399e8b38e0162e7c6f788af0def`, bank 3 SHA `9a5777723a1b3f5badee98354d73d2b8c177f0030aeb3d141d5d99e8ce400bef`. Bank 0–2 är byteidentiska med LAB. Fritt kodutrymme före `$FF90` ökar med 4 B, inte tillräckligt för kod/font.

Real Stella playback, 295 inputintervall/19,652 frames, klarade alla 15 vinster och coda/title med samma vinstframes som baseline. Bild-/PCM-paritet är däremot inte exakt: 19,220/19,652 framebufferhashar skiljer; ett jämförbart sparat checkpoint har 8 pixelavvikelser vid två fyra-pixelssegment; PCM skiljer 28/41,188,496 byte (7 stereo sample frames). Ändringen sparar cykler och flyttar efterföljande ROM-adresser; detta påverkar visad raster-/audio-output. A1 godtas därför endast som en byte-liveness-demonstration, inte som semantiskt identisk timerbas.

A1C försökte lägga till en 2-cykels NOP efter varje jämförelse. Då matchade alla framebufferhashar, men PCM skilde 1,935,416 byte. Eftersom en 2-cykels instruktion inte kompenserar exakt en cykel per `CMP`, och källlayout också skiftade, avvisas A1C.

### A1 sentinel – oberoende dynamiskt vittne

Diagnostisk A1-kopia skriver `$A5` till `$C1` efter RAM-clear; spelet skriver därefter inte dit i source. Stella läste 128-byte RIOT RAM varje frame under samma controllerreplay. `$C1` behöll `$A5` i 19,652/19,652 frames; observerade mode 0,1,2,3 och room-index 0–14. ROM SHA `97f0377383934ce8dd9867b221c3b9ccccdcc2220b50dc2036ea041bf4c7268f`. DIAGNOSTIC ONLY; detta sentinel-ROM är inte spelet och inte timer-ROM.

### B1 – mapPtr delas med pfPtr

B1 ersätter `mapPtr`-RAM med `pfPtr`: `LoadRoom` läser kartan först och PF-data efter, medan FIRE-vägen beräknar `GeoMapLo/Hi[room]` igen. Käll-liveness: `pfPtr` skrivs om till `GlyphB`/`BlankSprite` för varje renderer-rad innan dess enda indirekta renderer-read; den återberäknade kartpekaren är inte live efter collision-checken. Ingen kollisionstabell ersätts med muterade `mapRows`.

Native DASM avvisar patchen: sektionen når `$FF9B`, men den låsta ROM-gränsen/trampolinen är `$FF90` (11 B overflow). Ingen ROM-hash, Stella-/Gopher-vittne eller audio-/raster-PASS finns för B1. Samma två-byte budgetidé i kombination med A1 ger `$FF97`, fortfarande 7 B overflow. Det saknar fortfarande timerkod och font. B1 är därför `BUILD_FAIL`, inte bevisat spelbart.

### C2 – packade FIRE/SELECT-kanter

C2 packar `prevFire` (bit 0) och `prevSelect` (bit 1) i `inputFlags`, domän `$00–$03`. Den sparar 1 RAM-byte men kräver mask/OR-sekvenser vid press, release, reset och room load. Native DASM når `$FF9F`, 15 B över gränsen; timer-/renderkod är inte med. Den lilla ändliga avkodningen kan verifieras för alla fyra flaggtillstånd, men det finns ingen byggbar ROM att köra controllerövergångar på. Markeras `BUILD_FAIL`; ingen ROM-emulator-PASS tillskrivs.

### R2 – lossless scoredata

Offline-parser extraherade 45 streams × 256 byte = 11,520 B från de tre faktiska bankkällorna. Enkel RLE `(run,value)` packade bank 0: 3,840→758 B, bank 1: 3,840→778 B, bank 2: 3,840→798 B, totalt 2,334 B. Alla 45 avkodade streams jämfördes byte-för-byte och SHA-256 matchade (45/45). Teoretisk lagringsvinst är 9,186 B.

Ingen runtime RLE byggdes. Nuvarande `BankScoreDone` ligger vid `$FF86`/`$FF8A`; bara 10/6 byte återstår före `$FF90`. En löpande avkodare behöver persistent pekar-/run-tillstånd eller en skanning av komprimerad data varje bildruta, vilket ökar CPU-arbetet och flyttar TIA-skrivningar. Varken decoderstate eller en sådan cykelbudget har bevisats. Oförändrade scorebytes bevarar TIA-värden och timing; en offline-packning ensam är inte en ROM-optimering. R2 räknas därför inte som återvunnet körbart ROM-utrymme.

## G0–G5 och resultat

| Gate | Resultat | Skäl |
|---|---|---|
| G0 baseline/tool | PASS | Pinned clean LAB hash och DASM-identitet kontrollerades; clean LAB build finns i tidigare package. |
| G1 RAM/stack/ROM/renderer netto | FAIL inom testade lösningar | A1 ger 1 byte; B1 byggfel; C2 +1 byte men mer ROM; avslutsnapshot saknas; banklucka inte nog. Stackreserv `$F6–$F7` förbrukades inte. |
| G2 timerkärna/orakel | NOT_RUN | Inga säkra 3 byte och ingen kodplacering. |
| G3 verklig renderer | NOT_RUN | Ingen glyph/font/timer-ROM byggdes. |
| G4 integrerad F6-kandidat | NOT_RUN | Ingen timerkandidat producerad. |
| G5 T01–T24 och regression | NOT_RUN | Timerfunktionerna kunde inte köras; A1 replay är resurs-/regressionsprov, ej timerprov. |

## MAIN IV:s tolv frågor

1. Utöver ALLOC3: A1, A1C, A1 sentinel diagnostic, B1, A+B native build, C2 native build, R2 pack/unpack offline.
2. `exitX` konstantersättning sparar fysiskt `$C1`, 1 persistent byte. A1 tar 4 ROM-byte bort och två `CMP zp` blir `CMP #8`, -1 cykel vardera. Samma input vann samma rumframes; framebuffer/PCM var inte exakt lika. A1C bekräftar att enkel NOP-padding inte samtidigt bevarar PCM.
3. `mapPtr` käll-liveness återanvändning är rimlig och ändrar inte kartdata; omräkning sker vid FIRE från `room`. Byggfel 11 B över fast `$FF90`; därför inget dynamiskt/emulatorvittne för B1.
4. `prevFire`+`prevSelect` packades till bit0/bit1, -1 RAM, men källväxt överskrider bankgräns med 15 B. Sluttid kräver 3 bytes live timer + 2 bytes snapshot under mode2; `codaHi` är fortfarande soundtracktillstånd och `codaLo` används av coda-countdown. Ingen säker återanvändning av de två snapshot-byte bevisades.
5. A1 lämnar 4 extra bank3-byte före `$FF90`; inget font/gateway-utrymme efter dem. RLE är 9,186 byte mindre som offline-data men inte netto körbar ROM utan decoder/runtime state. Bank 0–2 scoredata och TIA-streamar har inte ändrats i någon ROM.
6. Ingen timerkärna; normal/carry/overflow-cykler, tidbas och SELECT efter vinst `NOT_RUN`.
7. Ingen autentisk timer-renderer; font, reset, TIA-cycles och läsbarhet `NOT_RUN`.
8. Alla tester behöll LAB:ens stackdelning. $F6–$F7 skyddades; aktiva `$F8–$FF` lånas inte. Bästa A1 har ingen stackändring. Timerstack inte mätt eftersom timerkod saknas.
9. Ingen spelbar timer-ROM; A1/A1C är resursvarianter och sentinel är `DIAGNOSTIC_ONLY`.
10. T01–T24: samtliga `NOT_RUN` på timer-ROM, eftersom ingen sådan ROM finns.
11. Nytt mätt fynd: A1 och A1C ger olika små men mätbara outputavvikelser; B1/C2 kan inte placeras i bank 3. Avsaknad av full 262-line/TIA-bus/stack-/Gopher-labbevis är `NOT_RUN`, inte bevisat maskinfel.
12. Rekommendation: helt avstå från timern inom nuvarande krav. Nästa beslut kräver ingen utvidgad researchorder. Fråga om designkompromiss behövs endast om användaren själv vill överväga ny tidkontrakt, större ROM eller annan plattform; alla ligger utanför denna order.

## Leverans-/behörighetsgräns

Detta är HEALTH-experimentdata till MAIN IV. Ingen produktkandidat, oberoende verifiering, Pachinko, merge, release eller ny specialistfas startas. Full zip/manifest och lokala reproduktionsfiler finns i denna leverans; historiskt evidence-zip dupliceras inte.
