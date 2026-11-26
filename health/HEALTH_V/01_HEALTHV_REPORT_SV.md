# MELLANRUM – HEALTH V: room number

## Slutstatus

`ROOM_NUMBER_NO_GO_WITHIN_TESTED_CONSTRAINTS`

Ingen spelbar experiment-ROM kunde byggas med de prövade lokala renderingsmetoderna. Ingen kandidat-ROM finns att spela eller verifiera. Det här är ett avgränsat NO-GO inom de testade begränsningarna, inte ett bevis på att ingen tänkbar omstrukturering alls kan rymma funktionen.

## Baslinje och byggresultat

Jag hämtade den angivna kompletta LAB-källan och ROM:en från projektets Drive. ZIP-kopian var 48 144 byte och passerade ZIP/CRC-kontroll. Källans `main.asm` hade SHA-256 `3246d67a40470454eb56c38f2f4c32fb34ccb4ff38ed796ccb10cf00a647d53e`. ROM:en var 16 384 byte och hade SHA-256 `8a59b84eb5151f78d40e6943c854d7e42c166b531aee3d40432182d32dcdf03b`.

Ren native DASM-ombyggnad av alla fyra F6-banker lyckades. Resultatet var 16 384 byte, 4 096 byte per bank, och ROM-hashen matchade exakt den föreskrivna LAB-ROM:en. Därmed är den valda baslinjen reproducerad.

## Metodförsök

| Försök | Vad som prövades | DASM-resultat | Slutsats |
|---|---|---|---|
| A: PF2 3×5 | Rumsindex + 1, raddata för tio siffror och en kompakt PF2-renderarkrok | FAIL: `Origin Reverse-indexed`; aktuell kodadress `$FFCA`, nästa fasta origin `$FF90` | Den lilla lokala PF2-kroken och tabellen överskrider det sammanhängande utrymmet i bank 3. Ingen spelbar/asymmetrisk PF-implementation byggdes. |
| B: P0/P1 | Rumsindex + 1, glyphrader och tillfällig GRP0/GRP1-återställning | FAIL: `Origin Reverse-indexed`; aktuell kodadress `$FFD2`, nästa fasta origin `$FF90` | Den lokala spritevägen kräver också utrymme utanför bank 3:s marginal och tillför dessutom positionerings-/återställningsarbete. Ingen kandidat byggdes. |

Bankgapinventeringen från LAB-evidensen visar i bank 3 endast ett ledigt byte vid `$FF8F` och tre vid `$FFF3–$FFF5`, åtskilda av F6-trampolin, coda och vektorer. Bank 0–2 har större lediga områden, men koden för rumsbilden körs i bank 3. Att anropa renderer över bankgräns under synlig raster kräver en ny dispatch-/återgångsväg och noggrann ombudgetering. Jag provade inte det eftersom det riskerar att ändra kritisk timing och går utanför en lokal, låg-risk lösning.

Metodfilerna är **footprint-prober**, inte färdiga implementationer. De är isolerade kopior och ändrar inte LAB-källan. Att deras DASM-byggen misslyckas räknas som faktisk resursmätning, men inte som ett funktionstest.

## Testmatris

| Område | Status | Evidens/anmärkning |
|---|---|---|
| Drive-baslinje och föreskrivna SHA | PASS | Hashar dokumenterade i `baseline/` och manifestet. |
| Native DASM-baslinje, fyra banker, ROM-hash | PASS | `baseline/ROM_16K_BUILD.json`; ROM-SHA matchar. |
| PF2-lokal renderer footprint | FAIL | DASM reverse-origin i bank 3. |
| Sprite-lokal renderer footprint | FAIL | DASM reverse-origin i bank 3. |
| Rumsnummer 1–15 och 9→10 | NOT_RUN | Ingen kandidat-ROM. |
| Alla aktövergångar, SELECT, RESET, vinst, coda, titel, FRI SKOG | NOT_RUN | Ingen kandidat-ROM. |
| Stella/Gopher2600 spelprov | NOT_RUN | Ingen kandidat-ROM; historisk LAB-evidens räknas inte som nytt HEALTH V-prov. |
| 15 autentiska kandidatskärmbilder och spelvideo | NOT_RUN | Ingen kandidat-ROM. |
| Grafikdiff med endast siffer-ROI maskerad | NOT_RUN | Ingen kandidat-ROM. |
| Scanlines, TIA-skrivningar, WSYNC, HUD x9, Stem13, terminalvägar | NOT_RUN | Ingen kandidat-ROM. |
| RIOT/VBLANK, F6-bankning, stackreserv, ljudregister/PCM | NOT_RUN | Ingen kandidat-ROM. |
| PR47 263-linjers negativ kontroll | NOT_RUN | Inte relevant utan kandidat och ingick inte i dessa footprint-byggen. |
| Full 15-rums regression och controllersekvens | NOT_RUN | Ingen kandidat-ROM. |

## Ändringar, gräns och rekommendation

Ingen ändring gjordes på `main`, PR49 eller den frysta produkt-ROM:en. Endast två isolerade assemblerkopior och evidensfiler skapades. Ingen timer, poängräknare eller ny spelmekanik har införts.

Rekommendation: behåll LAB utan rumsnummer inom nuvarande godkända ROM-layout. Om MAIN vill återuppta idén krävs separat beslut om omstrukturering av bank 3 eller en synlig raster-/bankningsändring, följt av en ny implementerings- och verifieringsgrind. Denna rapport i sig ger inget sådant mandat.
