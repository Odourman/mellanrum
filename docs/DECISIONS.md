# Beslutsregister – Mellanrum

Endast uttryckliga designägarbeslut ändrar canon. Registrera varje ändring med datum, källa, omfattning, status och `supersedes`. Tekniskt förslag är inte godkänd regel.

| ID | Datum | Beslut eller fråga | Status | Källa / avgränsning |
|---|---|---|---|---|
| MEL-001 | 2026-11-22 | Spelets namn är "Mellanrum" | APPROVED | Användarens projektstart |
| MEL-002 | 2026-11-22 | Nytt fristående Atari 2600-projekt | APPROVED | Användarens projektstart och projektkontext |
| MEL-003 | 2026-11-22 | GitHub `Odourman/mellanrum` är projektets repository | APPROVED | Användarens URL |
| MEL-004 | 2026-11-22 | Skapa en projektmapp i Google Drive | APPROVED | Användarens begäran |
| MEL-005 | 2026-11-22 | Använd GitHub Actions i arbetsflödet | APPROVED | Användarens begäran; CI-resultat är inte självständig ROM-verifiering |
| MEL-006 | 2026-11-22 | MAIN ansvarar för samordning, status och uppdrag | APPROVED_FOR_PROJECT_SETUP | Användarens uttryckliga fråga om MAIN-roll |
| MEL-007 | 2026-11-22 | V5 med skog/barrträd, uggla och sten som senast diskuterat designförslag | PROPOSED_SOURCE_INTAKE | Kräv faktisk V5-källfil och versionsgranskning före fastställd canon |
| MEL-008 | 2026-11-22 | Oidentifierbar hotfull närvaro som nytt speldesignlager | OPEN | Användaren bad om konstnärlig värdering; inte automatiskt implementerad |
| MEL-009 | 2026-11-22 | 16 KiB F6/NTSC som första tekniska profil | WORKING_ASSUMPTION | Kandidat från design/research, måste godkännas mot spelspecifikation |
| MEL-010 | 2026-11-22 | Auktorisation att börja gameplay-ROM | NOT_AUTHORIZED | Kräver särskilt uppdrag efter designintag |

**Ingen av MEL-007 till MEL-010 får beskrivas som slutligt godkänd bara för att de står i registret.**

Vid ett nytt beslut: skriv `MEL-011` osv. Ändra inte historiska rader i tysthet; ange datum, källhänvisning och exakt ersatt regel.

## Nya granskningstransaktioner: 2026-11-22 (V5.1)

| ID | Datum | Beslut eller fråga | Status | Källa / avgränsning |
|---|---|---|---|---|
| MEL-011 | 2026-11-22 | V5.1 ersätter V5 som **föreslagen designbas för granskning** | PROPOSED_SUPERSESSION | Användarens V5.1-handoff; V5.1-paketets ZIP och `LAS_MIG_FORST.md` ännu ej åtkomliga |
| MEL-012 | 2026-11-22 | Närvaron i III-03 till III-05: varning, två aktiva tick, FIRE-kapning och en autonom stenvändning | PROPOSED_IN_V5_1 | V5.1-kritisk avhandling, §10 och inledande revision; MEL-008 kvarstår historiskt OPEN tills accept |
| MEL-013 | 2026-11-22 | Materialalfabetet exakt barrträd, uggla, sten; ingen fjärde kroppslig fiende | PROPOSED_IN_V5_1 | V5.1 kap. 1–3, 15A |
| MEL-014 | 2026-11-22 | Tre akter, 15 rum, spegling/eko/fas och ljud som konstnärlig mekanik utan musikspel | PROPOSED_IN_V5_1 | V5.1 kap. 5, 10–21, 62–65 |
| MEL-015 | 2026-11-22 | MAIN:s V5.1-granskning är preliminärt **positiv men INTE accept** | REVIEWED_WITH_OPEN_GAPS | `docs/MAIN_V5_1_REVIEW_2026-11-22.md`, ofullständigt källa/ZIP-intag |
| MEL-016 | 2026-11-22 | ROM-implementation förblir spärrad i detta uppdrag | NOT_AUTHORIZED | Uttrycklig användarinstruktion; MEL-010 oförändrat |

**Viktigt:** V5.1 kan vara bättre än V5 och ändå sakna formell projektacceptans. Det gamla versionsförslaget är inte automatiskt raderat; besluten gäller endast det nämnda granskningsskedet. Själva grafiken, Python-källorna, testerna, manifestet och händelseordningen kan inte slutgranskas före det faktiska ZIP-intaget.
