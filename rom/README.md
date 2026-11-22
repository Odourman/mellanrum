# ROM-källa

**Ingen gameplay-ROM finns ännu.** Detta är ett reserverat kodområde.

När en uttryckligt auktoriserad utvecklingsetapp börjar läggs DASM-entrypoint på `rom/src/main.asm` eller ändras efter separat dokumenterat buildbeslut. CI kommer då att försöka assemblera `rom/src/main.asm`, kontrollera binärfilen och publicera den som **build-only artifact**, inte spela eller verifiera den i Stella/Gopher.

Skilj mellan:
- `rom/src/` – källkod för byggbar kandidat,
- `rom/diagnostics/` – separata avgränsade teknikprov,
- `rom/evidence/` – manifest/replay/loggar för faktiskt körda tester.

Inga diagnostik-ROM:ar märks om till spelbara ROM:ar utan nya tester.
