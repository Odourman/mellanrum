# Mellanrum

Ett nytt, fristående experimentellt/avantgardistiskt spelprojekt för **Atari 2600**.

**Status 2026-11-22:** Projektet är initierat. Ingen ROM är implementerad eller emulatorverifierad. Det **nya V5.1-förslaget** för "Mellanrum: Skogen som lyssnar" granskas som designkandidat, inte automatiskt godkänd canon. Närvaron är beskriven som ett tvåtickslångt intrång i FIRE:s betydelse, inte traditionell fiende. Det fullständiga ZIP-paketet och modelltesterna inväntar källverifiering.

## Projektkällor

- GitHub (kod, versioner, Issues, tester, GitHub Actions): https://github.com/Odourman/mellanrum
- Drive (originalunderlag och beslut): https://drive.google.com/drive/folders/1rO3ZTTBgyZZhqOx1WCxevM6sE3CrvUcl
- [AGENTS.md](AGENTS.md) – rollgränser och källhierarki
- [Projektstatus](docs/CURRENT_PROJECT_STATE.md) – faktisk status
- [Beslutsregister](docs/DECISIONS.md) – godkända, föreslagna och öppna beslut
- [Designintag](docs/DESIGN_INTAKE.md) – vilken designkälla som saknas/behöver granskas
- [MAIN:s V5.1-designgranskning](docs/MAIN_V5_1_REVIEW_2026-11-22.md) – konstnärlig och teknisk riskbedömning, ännu ingen accept
- [Teknisk och verifieringsmässig arbetsmodell](docs/WORKFLOW.md)

## Arbetsprincip

MAIN samordnar och kontrollerar; användaren godkänner design och större avsteg; ROM Development implementerar efter avgränsad order; Research och Graphics/Audio är rådgivande; separat Verification testar **oberoende**. Ingen får presentera en GitHub Actions-grön byggning som bevis för att TIA, ljud eller gameplay fungerar.

Första tekniska målet efter separat implementationsbeslut är en liten **spelbar** Atari 2600-ROM som bevisar den nya speldesignens kärninteraktion. Arkitektur och mapper beslutas mot spelets egna krav, inte genom att kopiera Let Me Out!.

Se [CI](.github/workflows/ci.yml) för uppstartskontroller; ROM-build aktiveras när en assemblerkälla tillkommer. Emulatortester och slutlig verifiering är ännu **NOT_RUN**.

## Teknisk överföring

`ATARI_2600_AVHANDLING_2026-11-21.md` och dess ZIP är metod- och teknikreferenser från **Let Me Out!**, inte Mellanrums canon. Fysiskt kontrakt för standard-NTSC: 76 CPU-cykler per scanline, 262 scanlines per frame samt 128 byte internt RIOT-RAM inklusive stack. Föreslaget utvecklingssätt: DASM, Stella, Gopher2600 och reproducerbar evidence med hash, register-, pixel- och inputloggar.
