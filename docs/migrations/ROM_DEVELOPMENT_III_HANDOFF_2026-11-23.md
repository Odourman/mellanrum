# MELLANRUM – ROM DEVELOPMENT II → III: kontrollerad migration efter AVBRYT
**Datum:** 2026-11-23, efter användarens "Avbryt" och efterföljande uttryckliga begäran att migrera till ny chatt. **Detta är ENDAST dokumentation/överlämning. Inte en återupptagen implementationsorder.** Stoppad produktionskod ska inte modifieras under migrationen.

## Vem bestämmer?
Läs i ordning `AGENTS.md` (roll och källhierarki), `docs/DECISIONS.md` (MEL-053–MEL-056, samt senare användarbeslut), original och registry, `docs/CURRENT_PROJECT_STATE.md`, `docs/SOURCE_REGISTRY.md`, Issue #32 och faktiskt PR #33 HEAD. MAIN förvaltar status och release-gate; ROM DEVELOPMENT implementerar bara uttryckligen tillåtet scope; oberoende Verification/Pachinko är fristående. GitHub är källan till **vad som faktiskt ligger i commit/ROM/Actions**, inte ChatGPT Memory eller gamla chattsammandrag.

## Pålitligt fryspunkts-ID
- Repo: https://github.com/Odourman/mellanrum
- Stoppat WIP: Draft PR **#33** https://github.com/Odourman/mellanrum/pull/33
- Kodgren **`romdev/issue32-finish-game-20261123`**, faktiskt kontrollerad HEAD **`48c0d5026d5a9ea22de1ff93028f3e18046e521b`** (2026-11-23). PR är OPEN, DRAFT, UNMERGED.
- Issue #32 https://github.com/Odourman/mellanrum/issues/32 är den ursprungliga omfattande användarauktorisationen med fulla kvalitetskrav. Den efterföljande användarordern **"Avbryt"** pausade genomförandet. Den nuvarande migrationsbegäran är **inte** ett återupptagande. Den nya chatten ska orientera sig och därefter invänta nytt uttryckligt klartecken innan produktkod, rum, ROM eller tester för fortsatt utveckling ändras.
- Skyddade Draft PR **#27, #23, #16, #4** får inte skrivas över; inga merge/tag/release-beslut finns.
- Gamla oberoende Verification #28 och Pachinko #29 gäller **endast** PR27-SHA **`7ce777dc273e1c30d8621843052e941ced41fcf2961bcdf835576a11c9592446`**, inte PR33.

## Hårdvaran och faktisk byteidentitet
- Mål: standard NTSC Atari 2600, äkta F6 **4 × 4096 = 16384 bytes**, RIOT 128B, 6507 + två TIA-ljudkanaler. Ingen SC/RAM, ARM, DPC, CDF eller modifierad konsol.
- Senaste reproducerbara **native DASM Actions-kandidat från just PR33 HEAD**: ROM SHA256 **`962818fa6a8a26eb22a66c66bd3da519467b78f790b149748ea3f036a97d011a`**, 16384 byte, verifierad genom faktiskt ZIP-extraherade bytes och omräknad SHA; [Actions run #45184894712](https://github.com/Odourman/mellanrum/actions/runs/45184894712), [ursprunglig artefakt #14823930347](https://github.com/Odourman/mellanrum/actions/runs/45184894712/artifacts/14823930347). Drive-kopia: https://drive.google.com/file/d/1M9eBl579Jq6MvUQg2sehABIV24c3IUiH/view
- **KRITISK IDENTITETSGRÄNS:** Trots PR33-källändringarna pekar `rom/bin/MELLANRUM_16K_NTSC_F6.bin` i PR33 fortfarande på gammalt Git blob **`958d7505e5e1af7fbf43cb2e1d8571aa9e12c6b5`** (=PR27-binär/SHA `7ce777...`). Den **nya** SHA `962818...` finns i byggartefakten, inte som incheckad versionsmärkt produkt-ROM i PR33. Mottagaren får absolut inte råka testa den äldre binären som om den vore nya! En pinning/överlämning av ny ROM är en kvarvarande uppgift **först efter** ny uttrycklig återupptagningsauktorisation, och måste följas av samma-SHA omtest.

## Vad som faktiskt implementerades på WIP-grenen före stoppet
- Fyrformig markörstatus i separat nedre P0-spritefält: neutral ring, godkänd bock, nekad X, Närvaro bruten symbol; M0 används som positioneringsmarkör. 8×8 källmasker finns nu i aktiv renderingsrutin. Att samma scen, samma x/y och 1× kontrasterna är estetiskt godkända är **inte** bevisat av enbart kod.
- Samtliga 15 rums exit-rutin använder olika faktiska orsaksvillkor: stenens polaritet, stenbesök, eko köat eller tomt, fas; källmodell och styrlösningar uppdaterades. Gameplay kvalitets-/svårighetsgrad för nybörjare fortfarande **NOT_RUN**. Ugglan fortsätter autonomt; inga konventionella poäng, vapen, fiender eller bossar.
- Grön PF-skog med tydligare barren/krona och stam; mörkare akt III; titel och coda har ny grafik/ljud; långsam ca 34s ytterligare TIA-modulation för att bryta 256-frame repetitivitet. 4 KiB F6 spelbankens utrymmes-/cykelmarginal kräver fortsatta mätningar.
- Originalspelidentitet bibehålls: 3 akter × 5 rum, barrträd/uggla/sten, U3 tre vingar och lodrät näbb, två S3-symboler, icke-identifierbar Närvaro, experimentell indirekt påverkan.

## Bevis som HAR kontrollerats efter avbrott
- Native GitHub Actions #45184894712 = **SUCCESS** på HEAD `48c0d...`. Nedladdad artifact ZIP = CRC OK, ROM 16384 bytes och egen SHA256-beräkning matchar `962818...`. `CAMPAIGN/result.json`: **DEVELOPER_STELLA_PASS 15/15**, 19412 riktiga emulerade bildrutor, verklig joystick/FIRE, coda→titel på frame 19411, 115 skärmbilder enligt index, autentisk PCM. Stella core `8.0_pre 8dd5600`, core SHA `2130ed1153cef66ef3f34bf9063f675f1f3342bc18320eb9ae5101743e3042df`. Stella-resultatet märker själv exakt NTSC-scanline-kontroll **NOT_RUN**.
- Föregående chatt **rapporterade** Gopher2600 15/15 och 278/278 prov à 262 scanlines på samma ROM. Vid migrationen finns inget separat arkiv bekräftat i GitHub Actions-artefakten som bevisar hela Gopher-resultatet. **REPRODUCERA** innan det upphöjs till kontrollerad PASS.
- Föregående chatt **rapporterade** 0/15 passiva och åtgärdsutelämnade vinster för första 10 rum och 5 kvarstående. Ingen fullständig 15-rumsserielogg har verifierats för det nya SHA här. **15/15 long-idle och counterfactual NOT CONFIRMED**; den gamla PR27 0/15 gäller inte.
- Ett verkligt rasterfel upptäcktes med 264 NTSC-linjer i tidigare WIP; HEAD `48c0...` ändrade `HUDBottom7` från 7 till 5; Gopher **rapporterades** sedan 262. Det kräver oberoende och fullständigt ny-SHA-timingprov.
- **VIKTIG KVALITETSDEFEKT:** lokal MP4 `MELLANRUM_ISSUE32_FULL_REAL_STELLA_TIA_1PANE.mp4` (5m29.5s, H264 640x456 AAC) är i själva verket **nästan helsvart mellan titel och slut**, verifierat genom ffmpeg-avkodade bilder vid sek 8, 60, 135, 205, 290, 320 (medel RGB runt 0,0,0). Tidigare påståendet att videon rättats är FEL. **DENNA MP4 ÄR INVALID/REJECTED, EJ VIDEOEVIDENS.** Återskapa från en korrekt Stella-session och granska faktiska avkodade frames + synkat TIA-ljud efter ny auktorisation. Lägg inte svartfilen som godkänd slutvideo.
- Befintliga fyra lokala markörskärmbilder är från separata emulerade tidpunkter; krav på **fyra samma-scene/motsvarande faktisk cursor-position** och synlighet i 1× kräver stringent återtest.
- Många gamla 4 KiB CI-jobb är korrekt SKIPPED för vNext, och senast statisk CI PASS. Det är inte samma sak som att samtliga tester är gröna; kontrollera alla utförda/failed/felaktigt versionstagna workflows.
- **Ej bevisat:** användarens slutliga spelbarhets-/estetikgodkännande, mänsklig förstagångstest, ljudlyssning, komplett 600s×15 idle + utelämnade kritiska val på slut-SHA, alla alternativa felbeslut, worst-case CPU/cycles/stack, original Atari/RetroN77 fysisk test, PAL, ny oberoende Verification/Pachinko.

## Omgående åtgärd för NY chatt (ENDAST onboarding)
1. Ta rollen ROM DEVELOPMENT III. Bekräfta tillgång till GitHub och Google Drive, läs realtidskällorna och denna handoff (inte Memory).
2. Jämför MAIN state/registry med faktisk PR33 HEAD och bevis; nuvarande main `CURRENT_PROJECT_STATE` beskriver fortfarande Issue32 som "not started" och är **STALE**. Föreslå en statuskorrigering till MAIN men ändra inte main canon obehörigt.
3. Verifiera zip och rom SHA och klassificera PASS/INCONCLUSIVE/NOT_RUN utan att fortsätta implementation, köra nya långtester eller röra PR33.
4. Redovisa blockerare och vänta på nytt uttryckligt "återuppta ROM DEVELOPMENT Issue32" innan ytterligare produktförändringar.
5. Om/när användaren auktoriserar återupptagning, arbeta endast i nytt godkänt scope på separat gren, leverera full källa/nya bytes, 15/15 Stella/Gopher, 0/15 36k frames, 15 kausala motprov, 4 likadant-scene P0-former, korrekt 1-pane video, TIA WAV/long-form ljudprov, F6/raster/cycles/stack/fuzz, SHA-proveniens, och lämna Verification/Pachinko helt oberoende.

## Navigering
- [MEL-056 och beslut](https://github.com/Odourman/mellanrum/blob/main/docs/DECISIONS.md)
- [MAIN current state, historiskt föråldrad kring PR33](https://github.com/Odourman/mellanrum/blob/main/docs/CURRENT_PROJECT_STATE.md)
- [Source Registry](https://github.com/Odourman/mellanrum/blob/main/docs/SOURCE_REGISTRY.md)
- [Issue #32](https://github.com/Odourman/mellanrum/issues/32)
- [Draft PR #33 WIP](https://github.com/Odourman/mellanrum/pull/33)
- [F6 native Actions #45184894712](https://github.com/Odourman/mellanrum/actions/runs/45184894712)
- [Google Drive-mapp](https://drive.google.com/drive/folders/1rO3ZTTBgyZZhqOx1WCxevM6sE3CrvUcl)

**Handoffens auktoritet:** status- och bevisrapport, inte ny kanon, inte bekräftad release, inte implementationstillstånd. Senare användarorder och högre projektkällor avgör.
