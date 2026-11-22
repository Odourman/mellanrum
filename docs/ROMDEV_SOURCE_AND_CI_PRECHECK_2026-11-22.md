# ROM DEVELOPMENT: käll- och CI-förkontroll 2026-11-22

Status: **utvecklarens första kontroll**, inte MAIN-accept eller independent verification.

## Gällande uppdrag
- [Fullspelsorder](ROM_DEVELOPMENT_FULL_GAME_ORDER_2026-11-22.md) och [Issue #2](https://github.com/Odourman/mellanrum/issues/2) har inspekterats.
- GitHub-startcommit vid arbetsstart: `0ed8f6517c8870854576ee56f5995952f236de0c`.
- Den slutliga GRAPHICS-V5.1-ZIP:en `MELLANRUM_GRAPHICS_V51_FINAL_TILL_MAIN_2026-11-22.zip` har lokaliserats som Library-filpost men dess råbyte kunde inte materialiseras i denna session. Ingen slutgrafik får hittas på eller rapporteras som verifierad.

## Återfunnen designmodell (inte slutgrafik)
- Råbyte från **äldre uppdragspaket till GRAPHICS**: `MELLANRUM_GRAPHICS_V5_1_OVERLAMNING_2026-11-22.zip`, SHA-256 `05e859233b8f514b1acf9f27224b75a02bc55d7a244f0de52607631f15767fe9`, 69 ZIP-poster och `testzip() == None`.
- Därin finns en inbäddad **original-V5.1-kopia** `ORIGINAL_V5_1_HUVUDPAKET.zip`, 570796 byte, SHA-256 `7bb664dcd5a64e9dd8435aa83328827c72c345da5d9fb83b9d41bf70a34a3e5e`, 40 ZIP-poster och `testzip() == None`. Kontrollera mot separat fullspelsorigial när åtkomst ges; lika stor fil är inte bevis på byte-identitet.
- Ursprunglig `reference/rooms.json` från inbäddad kopia SHA-256 `ea80a4cc7d736db6b0b107560b37b064dc06399ee681d3c50ae3e042b05ada78`.
- `SHA256SUMS.txt` i uppackat original validerades lokalt med `sha256sum --check`.
- `python3 -m unittest -v test_engine.py`: **20/20 PASS** (ren Python).
- `python3 check_rooms.py`: **15/15** abstrakta lösningsspår funna.
- `python3 validate_traces.py`: **15/15** grov cursor-travel-kontroll PASS, **inte** frame-exakt joystick.
- `ATARI_2600_AVHANDLING_2026-11-21.md` SHA-256 `7ed5600fc195f76840b73ee5c899556a72fafbbac108c63e7b14a079aff5ebbb`; teknikreferens, **inte** Mellanrum-canon.
- `ATARI_2600_KUNSKAPSOVERFORING_2026-11-21.zip` SHA-256 `fce2ec3aa68797b7c8d152acd138b3481303ea9a233a6d39636cf422c4eab7ac`; teknikreferens.

## Actions och statusgräns
- Existerande `project-checks` och valfria `rom-build` bevaras.
- Separat `dasm-toolchain-smoke` i branch bygger `rom/diagnostics/ntsc_frame_smoke.asm` och publicerar .bin/.lst/.sym/SHA.
- Detta är **inte** en gameplay-ROM: inga 15 rum, ingen joysticklogik eller slutgrafik. Syftet är att faktiskt pröva assemblerkedjan i Actions utan att förväxla dess binär med ett färdigt spel.
- GitHub Actions-jobbets verkliga körresultat måste kontrolleras på PR:n innan `DASM_DIAGNOSTIC_BUILD_PASS` kan anges. `ROM_GAMEPLAY_NOT_RUN`, `EMULATOR_NOT_RUN`, `HARDWARE_NOT_RUN` och `INDEPENDENT_VERIFICATION_PENDING` gäller fortsatt.
