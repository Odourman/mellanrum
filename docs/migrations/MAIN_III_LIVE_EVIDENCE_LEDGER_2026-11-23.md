# MELLANRUM – MAIN III live evidence ledger
As-of: 2026-11-23 sent på kvällen, omkontroll före användning.

| Bevis | Källa / revisionsnyckel | Slutsats |
|---|---|---|
| Aktiv ny utvecklarkandidat | [Draft PR38](https://github.com/Odourman/mellanrum/pull/38), head 2c70bf7468fc33eed198246281a8ffd0a7cc9252 | OPEN DRAFT, UNMERGED |
| Byggd källversion | bacd37102e858e3652097a3aa2608834ef26b609 | Använd med pin/rebuild-logg, inte som samma sak som senaste HEAD |
| PR38 checkad ROM | Git blob 87371e9cbbe584e21a85d855062e50e13721ef17 / exakt fil rom/bin/MELLANRUM_16K_NTSC_F6.bin | 16384 byte, SHA256 7e5add7d2580e7ebb3e871a79c13d7ba5680e71354946c941fe79b826e158134 |
| Native F6 + Stella 15/15 / FRI profiles | [run 45264527061](https://github.com/Odourman/mellanrum/actions/runs/45264527061) | DEVELOPER_CI_SUCCESS, bygg/artifact och enbart körda steg |
| Gopher2600 15 rum | [run 45264527051](https://github.com/Odourman/mellanrum/actions/runs/45264527051) | DEVELOPER_CI_SUCCESS |
| Stella idle 15 ×36k | [run 45264527111](https://github.com/Odourman/mellanrum/actions/runs/45264527111), 15 success jobs och separata JSON-artefakter | DEVELOPER_CI_SUCCESS, granska loggarnas rätt state och ROM SHA |
| Difficulty A/B | [run 45264527210](https://github.com/Odourman/mellanrum/actions/runs/45264527210) | DEVELOPER_CI_SUCCESS |
| Older ROM model overlay | [run 45264537305](https://github.com/Odourman/mellanrum/actions/runs/45264537305) | FAIL; Issue15 overlay/source art check; måste klassificeras |
| Title/Presence visual | [run 45264527127](https://github.com/Odourman/mellanrum/actions/runs/45264527127) | FAIL; "Observe title + all three III intrusion rooms"; undersök om produkt- eller testspecifik avvikelse |
| PR38 project sources proposal | [Drive ZIP](https://drive.google.com/file/d/1owkqh8N-dWjKzs8QNiYcqgvKLB3fsIDZ/view) | SOURCE_PROPOSAL; 13 filer, skapade före senaste ROM HEAD; behöver reconcile |
| Older ChatGPT project source master | [Drive Doc](https://docs.google.com/document/d/1BrneppdB_30vI9K7Nv18hjonoHfYF6iJoyIiTcbm6Xg/edit) | PAUSED PR33 snapshot; HISTORICAL/STALE |
| Historical PR33 | [PR33](https://github.com/Odourman/mellanrum/pull/33) | Incheckad PR27-ROM skild från faktisk PR33-native, får ej blandas med PR38 |
| PR37 | [PR37](https://github.com/Odourman/mellanrum/pull/37) | F6 ROM d3754d78...; inte final SHA PR38 |

**VIKTIG VIDEO-KONFLIKT:** PR38-exporter rapporterades på SHA 4921f723ff989bffaf48e4bebdab36406c83c9f5083588f55f21528fb7e5bba0; checkad HEAD ROM är 7e5add7d2580e7ebb3e871a79c13d7ba5680e71354946c941fe79b826e158134. Film kan vara giltig för sin egen äldre revision men är inte samma-SHA bevis för nya träd/FRI-former. Be om nya inspelningar på exakt final bytes.

**ÖPPNA GATES:** kritisk-kausal test 15/15 exact latest ROM, alternativ-väg softlocks, CPU 76c/line worst-case, stack/RAM highwater, end-to-end raster, full video/audio QA same-SHA, mänskligt kallstartstest, audiovisuell/ljusacceptans, fysisk originalkonsol/RetroN77, oberoende final-SHA Verification + Pachinko. Allt öppet tills genuina artefakter erhållits.

**BEVISREGLER:** SOURCE_ONLY, BUILD_PASS, DEVELOPER_STELLA_PASS, DEVELOPER_GOPHER_PASS, MAIN_REVIEWED, INDEPENDENT_VERIFICATION_PASS, PACHINKO_PASS, PHYSICAL_HARDWARE_PASS, NOT_RUN, INCONCLUSIVE, FAIL. Skilj separat CI-head från ROM-data, video/audio artefakter och verifierarens faktiska input.
