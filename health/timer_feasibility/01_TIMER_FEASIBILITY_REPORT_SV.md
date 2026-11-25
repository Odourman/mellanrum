# HEALTH III: genomförbarhetsrapport för kampanjklocka

Datum: 2026-11-25
Roll: HEALTH, tekniskt genomförbarhetslaboratorium
Status: TIMER_FEASIBILITY_INCONCLUSIVE (G0 PASS; G1 delvis undersökt; G2-G5 NOT_RUN)
Produktstatus: RC1/PR49 oförändrade. Ingen merge, tagg, release eller produkt-PR.

## Sammanfattning

Den föreskrivna LAB-baslinjen byggdes om med native DASM från ren källkopia. Den nya ROM-byteströmmen matchar pinned LAB exakt, vilket verifierar G0. Därefter byggdes och länkades ett isolerat minneslayoutprov för den enklaste klockrepresentationen: en framefasbyte och två byte för MM:SS. DASM gav adresserna $F6, $F7, $F8; de två första är skyddad stackreserv och den tredje aktiv stackregion. Den naiva tilldelningen är ogiltig även om assemblern accepterar den.

Detta visar en konkret resurskonflikt men bevisar inte att all möjlig liveness-/bitpackningslösning är omöjlig. Ingen säker återanvändning av två ytterligare variabler har demonstrerats. Därför är slutstatus INCONCLUSIVE, inte ett generellt bevisat NO_GO. Inget timer-ROM byggdes; inga timerbeteenden får räknas som PASS.

## Proveniens

| Objekt | SHA-256 / identifierare | Tillämpning |
|---|---|---|
| LAB ROM | 8a59b84eb5151f78d40e6943c854d7e42c166b531aee3d40432182d32dcdf03b | Exakt experimentbas och clean rebuild |
| LAB main.asm | 3246d67a40470454eb56c38f2f4c32fb34ccb4ff38ed796ccb10cf00a647d53e | Pinned source |
| RC1 ROM | 456005ed691860b32c44b79f2a71666f622b005f5a798eadf9b549c59cff13bd | Fryst jämförelse |
| PR49 HEAD | d013a0f82621d46ad12674a4a8e944bf005cd9c3 | Fryst produkt-PR |
| DASM | cfb23732297a4fe1c8d4a78d44206037d97733aedb2772503bbf029a4aa91291 | Native build binary |
| Native clean build | 8a59b84eb5151f78d40e6943c854d7e42c166b531aee3d40432182d32dcdf03b | 16384 bytes, exact match |

Bankhashar: B0 4f1fefc7513d5c0aef2d1c2a406b77975e59fc60e0a3361fa34455b4c669c49f; B1 8d49d78a7f7ea98d1638693767de146b54b7b97673eb5f077fbf9c0554e3a1e8; B2 6b82511ba23726be41aa5f7a4e8c2555f5e039ee6fc2ec6a1e0774117cfffbfc; B3 b3a24ac48440485518bd99bbc017cb68a8418ccc4247dc87729ea1f573246037.

## Baslinjebyggnad

Byggscript rom/f6/build_f6.py, kommandot, stdout, fyra bankfiler, listningar, symboler och ROM-manifest finns under BASELINE/CLEAN_NATIVE_BUILD. Storlek 16 KiB, mapper F6, build-scriptets bank- och vektorassertions passerade.

## RAM och livslängd

LAB deklarerar sammanhängande variabler $80..$F5: 118 byte. $F6..$F7 är explicit skyddad stackreserv; $F8..$FF är högst åtta aktiva returstackbyte enligt LAB-underlaget. Inget av detta får lånas. Enkel framefasbaserad MM:SS behöver minst tre samtidiga byte: sub-sekundsfas 0..59 och två byte med tid/siffror. 24-bit frameantal behöver också tre byte. Detta utesluter inte komprimerad speltillståndsrepresentation, men ingen sådan lösning har bevisats säker.

Probe-symboler: timerFrames=$F6, timerSeconds=$F7, timerMinutes=$F8. Den genererade ROM-byteströmmen är identisk med LAB eftersom DS endast ändrar symbol-/RAM-layout; den är inte en timer-ROM.

codaLo kan möjligen delas före coda, men är bara en byte och måste lämnas över innan StartCoda skriver 720-frame-countdown. codaHi ändras på soundStep-carry och deltar i ljudsemantik. soundStep ändras varje bildruta och påverkar FRI-startseed. waitFrames, introFrames, beatFrames, presence/pending och flera render scratch har relevanta campaign-livstider. Tidigare HEALTH-alias candidateD/workX avvisades efter bild-/PCM-avvikelser; den har inte återanvänts. Full livenessbevisning för nya alias saknas.

Slutvinst kräver att visad tid kan frysas medan den underliggande tiden fortsätter om room14 spelas om före coda. Det kräver ofta en separat fryst representation; ingen säker dead-state alias har bevisats.

## ROM, raster och ljud

Tidigare pinned gapkarta anger endast fyra isolerade gapbyte i bank3: ett före $FF90 och tre efter coda-code. De kan inte rymma timerkod/font. Bank 0-2 innehåller live soundtrack/interpreter och skyddade F6-trampoliner; de är inte generell fri kod/data. Ingen omlokalisering eller bankgateway har byggts.

Main loop kör ReadInput, GameFrame, SetColorsSound, SetShadowVisibility och PlaceObjects före väntan på INTIM; därefter renderer och overscan. Ingen timerkod lades till, så normal/carry cycles, minsta marginal, TIA-buss, pagecross och timer x9-resultat saknas. Tidigare x9 och audioresultat gäller enbart tidigare hashbundna LAB/RC1-försök.

## Kontrakt och olöst slutkant

A/FIRE från titel + Difficulty A startar 00:00. Tiden räknar i mode 1 och 2 genom förberedelse, väntan och övergångar. SELECT får inte pausa/nollställa. Giltig room14-vinst fryser synlig tid men underliggande tid fortsätter om SELECT används före coda. Coda-start låser definitiv tid; befintlig 720-frame coda ska bevaras. RESET går till titel. Difficulty B + FIRE startar FRI utan timer och utan ändring av ljudräknare. NTSC framebas; cirka 59,92 Hz. Overflow får inte wrappa.

Arbetsordern lämnar en semantisk kant: första vinsten fryser visad tid men coda-start låser senare definitiv tid efter möjlig väntan/SELECT-replay. Ska coda visa den senare tiden, eller ska definitiv tid låsas vid första vinst och sista omspelning exkluderas? Den rekommenderade arbetsregeln räknar replaytiden. Ingen ROM togs fram för att välja mellan dessa.

## Rendering och tester

Playfieldfont och P0/P1-font är endast analyserade som alternativ. Övre 16 rader bär redan fas-/slot-/Presence-HUD och owl-preparation; P0/P1/M0/BL/PF har roller. Inga 1x emulatorbilder, fullframes, busspår eller coda/FRI-bilder producerades. Båda rendereralternativen NOT_RUN.

T01-T24: NOT_RUN. Inga timer Stella/Gopher-resultat, timerbilder/video, timer PCM, bus comparisons, full 15-room timer run, timer stack/raster tests eller naturlig 60-minuterskörning. G0 native rebuild PASS; G1 naiv allokering FAIL; full genomförbarhet INCONCLUSIVE. Tidigare evidence ZIP-filer ingår men tillhör sina egna ROM-hashar.

## Rekommendation

Bevara RC1 och PR49. Behandla timer som ej implementerad. Eventuell fortsättning bör först bevisa minst tre säkra timerbyte och final snapshot/livstid utan att röra stackreserv, samt konkret ROM-/rendererbudget. Om MAIN vill stoppa timern först vid coda-start är det en kontraktsändring som behöver separat beslut. Senare produktimplementation, oberoende verifiering och mänsklig/fysisk prövning kräver egna steg.

## Förtydligande: tidigare cycle-kompenserad decoder och call graph

Det tidigare HEALTH-laboratoriets `LAB_STACK_INLINE_PADDED_B`-variant ersatte JSR DecodeKey med decoder-bytesekvensen och sex NOP efter stores. Den behöll ett 12-cykels JSR+RTS-fönster. Den inline-assemblerade sekvensen var `A5 E2 A2 00 C9 05 90 06 38 E9 05 E8 D0 F6 85 E3 86 E4`; kontrollen verifierade att endast RTS ersattes av sex NOP. En bounded interpreter jämförde 983 040 kombinationer över 40 giltiga nycklar, alla statusbyte med D clear, A/X/Y i {00,01,55,FF} och SP i {FF,F7,F3}. A, X, Y, processorstatus, SP, workX/workY, continuation och sammanlagda cykler matchade. JSR/RTS och NOP har ingen register-/flaggaeffekt. Reset utför CLD och den analyserade reachable-ROM:en saknar SED. Full kampanjens framebuffer/PCM parity bekräftade dessutom den testade raster-/ljudvägen. Detta är bounded verifiering för den exakta LAB-versionen, inte generell semantisk analys av varje tänkbart bytevärde.

Påståendet om fem till fyra nästlade JSR gäller hela den statiskt modellerade giltiga anropsgrafen: CFG startade från alla fyra resetvektorer, tog båda villkorliga branchutfallen, följde F6 bankbyten och modellerade JSR/RTS-returer. Den exacta LAB-ROM:en nådde 2 565 kontexttillstånd, noll analysfel och maxdjup 4; RC1:s motsvarande körning hade maxdjup 5. Stackåtgången minskade 10 till 8 byte; två stackreservbyte behölls. Det är ett whole-modeled-valid-flow-resultat, inte enbart den tidigare djupaste naturliga kodvägen. Den senare riktade oberoende verifieringen stärker bounded fallet men lämnar global all-path rasterrisk INCONCLUSIVE.

## Tidigare experiment som förs vidare oförändrade

- RAM-alias `candidateD/workX` byggdes och kördes separat. 114/116 kontrollbilder och 12 659 984/20 594 248 PCM-sampel avvek trots att logiska game-state-nycklar matchade. Försöket avvisades; orsak ej slutligt isolerad.
- x9-timingstressvarianten med felaktig carry-branch byggdes. Samma x9-input gav 262 linjer för RC1 och 263 för den avsiktligt felaktiga varianten; känt PR47-kontrollfall gav också 263. Detta validerade att Gopher-oraklet fångar 1-cykels sen branch. Det är ett negativt kontroll-ROM, inte produktfel.
- 40-byte tabellförsök misslyckades vid fast $FF90-trampolin innan ROM skapades.
- Oberoende riktad granskning av LAB fann sex TIA-ljudregisterskrivningar 3 color clocks tidigare än RC1, medan ändringen absorberades före observerad WaitVBlank/PF. FRI strict raw PCM A/B var INCONCLUSIVE; global all-path timing INCONCLUSIVE; human/physical NOT_RUN.

Originalpatchen mot RC1 finns i BASELINE/LAB_BEST_SOURCE/SOURCE_DIFF_VS_RC1.patch; hela tidigare experimentkällor, native loggar, listningar, symbolfiler, PCM, bilder, Stella/Gopher och riskmatriser finns i det inbäddade HEALTH-arkivet. Dessa resultat gäller LAB/RC1 och har inte ommärkts som timer-ROM-resultat.
