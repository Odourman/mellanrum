# Experimentregister — HEALTH VI

Alla varianter startade från lokala kopior av verifierad PR59-källa. Ingen förändring skrevs till PR59, `main` eller befintlig produktbranch.

| ID | Hypotes | Ändring | Native build | ROM SHA-256 | Observation | Disposition |
|---|---|---|---|---|---|---|
| E01 | 1-cykels input-branchdelta räcker för FRI presentation | Återställ PR58 `ReadMovement` | PASS | `a948d12e2f05514f4498c1e1249253bbedad6eaf6f5e1d99572ffd99c7b412cf` | Bild mismatch samma. PCM first diff samma. | Avvisa som tillräcklig fix |
| E02 | Tidigare owl preparation skapar FRI-divergens | Återställ anropstid för `PrepareOwlFrame` | PASS | `94bfbd33d2c048896c8117f6776a3e8db93158ff5f33d0c149f3c1e83c659301` | Bild mismatch samma. | Avvisa som tillräcklig fix |
| E03 | Renderer code region orsakar bildfelet | PR58 RenderPlay + PrepareOwlFrame | PASS | `4f04a38fa1e03be72b258605c48f18347c70e23e961055a35b271d788b57be72` | Exakt 960/960 framebufferparitet; PCM kvar i PR59-läge. | Behåll som diagnostik; ej kampanj-/releasefix |
| E04 | PR58 FieldPulse återställer 8-cykels musikfas | Återställ block | FAIL | Ingen binär | Bank 3 `$FFE9` korsar `$FFDA`-origin. | Avvisa oförändrad kopiering |
| E05 | ReadMovement+FieldPulse timingrestores är tillräckliga | Återställ båda blocken | FAIL | Ingen binär | Samma bankoverrun. | Avvisa oförändrad kopiering |
| E06 | 4×NOP får tillbaka 8 CPU-cykler | NOP test | FAIL | Ingen binär | `$FFDD`, 3 byte över fast origin. Ändrar dessutom ingen flagga men bytespace saknas. | Avvisa denna probe |
| E07 | Renderer restore plus timingrestore kan ge full FRI parity | Kombinerad specimen | FAIL | Ingen binär | Bank 3 når `$FFE9`; inget A/B resultat. | Inconclusive, ej kandidat |
| E08 | Full autonom/regression-test | Alla 15 rum, reset/select, owl, coda med experiment-SHA | NOT_RUN | n/a | Inget kandidatbevis, eftersom inga optimeringar valdes. | Kräver separat scope om ROM DEVELOPMENT vill fortsätta |
