# U3 Vingkropp – horisontellt spegelvänd efter lodrät näbb
**Status:** GRAPHICS_DESIGN_PROPOSED. Enbart konstgrafik: inga produktionsfiler ändrade.

User request: "Men gör ugglan spegelvänd nu". Spegelvändning betyder **vänster–höger (x-axel)**, inte upp–ned. Källan är tidigare lodräta näbbversionen `graphics/mel046-u3-vertical-beak-20261123`.

Alla tre U3-ramar är bitreverserade på varje 8-bitars scanline:
- B0 vilande: `18 7E DB F7 F7 7E 7E 24`
- B1 mellan: `18 7E DB F7 F7 FF BD 24`
- B2 utbredda vingar: `18 7E DB F7 F7 FF FF 24`

**Näbben** ändras `EF EF` → `F7 F7`; ögonraden `DB` förblir `DB`. Ugglans kropp är i övrigt nästan symmetrisk. Animationen och tidigare timingförslag är oförändrade; tvåframesalternativet återanvänder B1 och B0.

Konkreta bitrader, 9-byte bottom-up-tabeller och en offline-PNG/GIF-jämförelse finns i det till användaren levererade ZIP-paketet. GitHub-filerna `ART_ONLY.inc` och `U3_SPEGELVAND_MASKER.json` är endast grafikunderlag.

Ingen emulator- eller hårdvarukörning har utförts för dessa bytes. Fryst PR #4 och produktions-ROM med SHA `e9ea87d381bcf8da39ec055d7d6951ceff97b21d3a798addd10fbbe540c5e974` orörda. Ingen merge eller release.