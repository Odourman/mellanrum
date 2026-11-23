# MELLANRUM – skyddad spelidentitet och hårdvarukontrakt
Klass: sammanställning ur [DECISIONS](https://github.com/Odourman/mellanrum/blob/main/docs/DECISIONS.md), [Issue #32](https://github.com/Odourman/mellanrum/issues/32), [GRAPHICS Issue #13](https://github.com/Odourman/mellanrum/issues/13) och [AGENTS](https://github.com/Odourman/mellanrum/blob/main/AGENTS.md). **Detta är inte ersättning för ännu saknade verifierade originalfiler i Drive.** Nya konkreta beslut kräver primärkälla.

## Spelidentitet – kärna
- Titel: **MELLANRUM: SKOGEN SOM LYSSNAR**, Atari 2600.
- **Tre akter, fem rum vardera, 15 spelbara och olikartade rum** samt titel, FRI SKOG och avsiktlig coda.
- Tre materiella grundmotiv: **barrträd, uggla och sten**. Symboler och negativa rumsliga förändringar utgör speltecken, inte nya vanliga figurer.
- **Autonom uggla**; spelaren förändrar villkor, skog, sten och samband i stället för att direkt styra ugglans hastighet. Minst två tydligt särskilda mystiska tecken.
- **Närvaron** ska förbli oidentifierbar och icke-kroppslig: hot genom förskjutning, negativt utrymme, avbrott och kausala motsägelser, inte synlig standardfiende med hitbox.
- Avantgarde, surrealism, dadaism och experimentell orsak/verkan ska vara faktisk spelmekanik, inte bara dekor. Undvik traditionella vapen, bossar, poäng/HP och vanliga stridsloopar.
- Spelet ska vara begripligt nog att lära sig genom synlig respons; inte vara antingen automatiskt vunnet eller svårt enbart genom långa väntetider, slumpmässiga knapptryckningar och godtyckliga räknare.

## Specifika skyddade grafikpunkter
- U3-uggla: horisontellt spegelvänd godkänd gestalt, lodrät näbb, samma ögon och tre vingmasker. Bitmaprader rapporterade i Issue #32: B0 \`18 7E DB F7 F7 7E 7E 24\`, B1 \`18 7E DB F7 F7 FF BD 24\`, B2 \`18 7E DB F7 F7 FF FF 24\`. Matcha mot godkända grafikoriginal innan slutlig canonförklaring.
- S3: två skilda mystiska symboler med läsbar kontrast; sten och utgång måste hållas isär även vid överlappande P0/P1.
- Fyra markörresponser: **neutral, godkänd, nekad** (tre tydligt olika former), plus särskild **Närvaron-kapning**. Att bara ändra M0-bredd är inte uppfyllt krav. Testa vid faktisk native 1× spelupplösning, samma rum och position.
- Barrträd ska kunna kännas igen med krona/stam men gärna vara obehagligt abstrakta. Akt I mörk grön/blå, akt II jordnära och förändrad, akt III mörk kall grön/grå/blåsvart med tillfälliga bleka intrång. Kontrast och läsbarhet måste provas.
- Coda ska ge en märkbar men tvetydig förvandling före återgång till titel, utan konventionellt "YOU WIN".

## Ljudmål
- Enbart **riktiga TIA-ljudkanaler**, två kanaler. Titel/akt I mörka, låga, långa droner. Akt II minnespuls/eko. Akt III återhållsam oro, tystnad och störningar huvudsakligen kopplade till Närvaron.
- PR27:s 256-emulatorrutsfras = cirka 4,267 s har upplevts kort repetitiv; Issue32 efterfrågar längre 20–40s dramaturgiska utvecklingskurvor. Kvaliteten ska bedömas genom autentiska WAV/lyssning, inte bara loggade DAC-värden.
- En soundbank eller värdelös tystnad är inte ett artistiskt PASS enbart för att koden kompilerar.

## Hårdvarukontrakt – nya spelkandidaten
- **Oförändrad vanlig Atari 2600, NTSC**, 6507 + TIA + RIOT (128 B RAM).
- **Hård ROM-gräns 16 384 byte**, använd vanlig **F6 4×4096 bytes** bankväxling för 16 KiB-kandidaten. Ingen ARM, DPC/DPC+, CDF, SC-kassett, extra kassett-RAM eller modifierad konsol.
- Normalt NTSC mål **262 scanlines per bildruta**, CPU-budget **högst 76 cykler per aktiv skanlinje**. Kräver riktig beam-/worst-case-analys, inte härlett från enbart FPS eller få samplingsbilder.
- Native DASM-bygge, körning med verklig joystick/FIRE, autentisk Stella och Gopher2600, banker/hotspots/stack samt käll-/ROM-paritet. PAL och fysisk Atari/RetroN77 är separata testgrindar, inte automatiskt godkända.

## Var går gränsen för improvisation?
Vid **framtida uttryckligen auktoriserad återstart** får ROM DEVELOPMENT förbättra rum, grafik, TIA-kernel, logik, ljud och interaktion autonomt **inom Issue32 och ovanstående identitet**, och redovisar design-delta, visuella kompromisser och testbevis. Det ger inte rätt att överge motiv, byta plattform, öka till 32 KiB, göra en mainstream-fiende, acceptera en ny canon utan användarbeslut, eller börja innan pausen hävts.
