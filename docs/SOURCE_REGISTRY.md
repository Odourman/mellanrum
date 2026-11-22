# Source ID Registry – Mellanrum

## Auktoritativa ingångar
| ID | Källa | Klass | Status |
|---|---|---|---|
| M-SRC-001 | https://github.com/Odourman/mellanrum | Versions-/implementationssanning | Aktiv |
| M-SRC-002 | https://drive.google.com/drive/folders/1rO3ZTTBgyZZhqOx1WCxevM6sE3CrvUcl | Förvaringsplats för designoriginal/handoffs | Skapad, original ännu ej importerade |
| M-SRC-003 | docs/DECISIONS.md | Beslutslogg | Aktiv |
| M-SRC-004 | docs/CURRENT_PROJECT_STATE.md | Aktuell statusnavigering | Aktiv |
| M-SRC-005 | docs/DESIGN_INTAKE.md | Överlämnings-/öppna frågor | Aktiv, ej designcanon |

## Referenser som INTE blir Mellanrums canon
| ID | Källa | Integritetsuppgift | Klass |
|---|---|---|---|
| M-REF-001 | Lokalt uppladdad ATARI_2600_AVHANDLING_2026-11-21.md | SHA-256 `7ed5600fc195f76840b73ee5c899556a72fafbbac108c63e7b14a079aff5ebbb` | Teknik- och metodöverföring från Let Me Out!, rådgivande |
| M-REF-002 | Lokalt uppladdad ATARI_2600_KUNSKAPSOVERFORING_2026-11-21.zip, 50 filer | SHA-256 `fce2ec3aa68797b7c8d152acd138b3481303ea9a233a6d39636cf422c4eab7ac` | Historisk teknik-/metodreferens, innehåller källprojektets föråldrade beslut |
| M-REF-003 | Föregående "Mellanrum: Skogen som lyssnar" V5 | SHA-256 **saknas**, ej inläst i repo | Designkälla väntar på kopia och granskning |
| M-REF-004 | Äldre "Mellanrum: Det som lyssnar" V3 | Version/filhash ej intagen | Historiskt koncept, ej automatiskt slutgiltigt |

Källfilens namn, titel eller senare datum räcker inte ensamt för att ge den högre auktoritet. Ändra alltid detta register när faktisk ny originalfil tas emot. En hash identifierar bytes, inte att innehållet är rätt eller slutligt.

## V5.1 mottagningskandidater, ej auktoriserad slutcanon

| ID | Källa | Integritet | Status |
|---|---|---|---|
| M-CAND-005 | Indexerad Library-text `MELLANRUM_V5_1_SKOGEN_SOM_LYSSNAR_KRITISKT_REVIDERAD_AVHANDLING.md` | 1 396 indexerade rader läsbara. Originalråbyte och SHA-256 inte tillgängliga via materialisering | READABLE_TEXT_ONLY / PROPOSED / REVIEWED_PROVISIONALLY |
| M-CAND-006 | Användaren hänvisar till V5.1-ZIP och `LAS_MIG_FORST.md` | Inte bifogat/åtkomligt för denna MAIN-överföring; inte validerat | WAITING_FOR_SOURCE |
| M-CAND-007 | `reference/engine.py`, `reference/solve.py`, `reference/check_rooms.py`, `reference/validate_traces.py`, `reference/abstract_solution_results.json` | Beskrivna i avhandlingen men varken hämtade eller körda | NOT_RUN / WAITING_FOR_SOURCE |

Använd aldrig slumpmässig liknämnd Drive-fil som ersättning för M-CAND-006. En Drive-sökning gav t.ex. `LAS_MIG_FORST.md` som handlar om **The Cabin**, alltså är den inte Mellanrums källa. Originalens byte och SHA måste verifieras när de finns.
