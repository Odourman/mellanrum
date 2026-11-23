# MELLANRUM – LIVE-källindex och teknisk research
Datum: 2026-11-23. Länkarna är navigering, inte garanti att innehållet behållit samma version senare.

## Primära MELLANRUM-källor
- [GitHub repository](https://github.com/Odourman/mellanrum)
- [AGENTS.md – roller/authority order](https://github.com/Odourman/mellanrum/blob/main/AGENTS.md)
- [DECISIONS.md – användarbeslut MEL-053, MEL-054, MEL-055, MEL-056](https://github.com/Odourman/mellanrum/blob/main/docs/DECISIONS.md)
- [CURRENT_PROJECT_STATE.md – statusnavigering](https://github.com/Odourman/mellanrum/blob/main/docs/CURRENT_PROJECT_STATE.md): **föråldrad kring PR33 och "Avbryt" vid detta datum**
- [SOURCE_REGISTRY.md – original- och evidensregister](https://github.com/Odourman/mellanrum/blob/main/docs/SOURCE_REGISTRY.md): historiska dubbletter av vissa M-CAND-ID förekommer, sök källa/SHA
- [Drive: MELLANRUM-mapp](https://drive.google.com/drive/folders/1rO3ZTTBgyZZhqOx1WCxevM6sE3CrvUcl): migrationshandoff och ROM-artifactbackup fanns vid kontroll; originaldesign under uppsamling
- [Issue #32 – senast auktoriserade fulländringsscope före avbrottet](https://github.com/Odourman/mellanrum/issues/32)
- [Issue #30 – gameplaykritik och spelardjup](https://github.com/Odourman/mellanrum/issues/30)
- [Issue #31 – markörkravet](https://github.com/Odourman/mellanrum/issues/31)
- [Issue #20 – användarens mörka TIA-ljud](https://github.com/Odourman/mellanrum/issues/20)
- [Issue #13 – GRAPHICS studier](https://github.com/Odourman/mellanrum/issues/13)

## Exakta gren- och testlänkar
- [PR #33 – stoppad WIP för Issue32](https://github.com/Odourman/mellanrum/pull/33), HEAD 48c0d5026d5a9ea22de1ff93028f3e18046e521b vid snapshot
- [PR #34 – ROM DEVELOPMENT III dokumentationsmigration](https://github.com/Odourman/mellanrum/pull/34); [handoff](https://github.com/Odourman/mellanrum/blob/docs/romdev-iii-migration-20261123/docs/migrations/ROM_DEVELOPMENT_III_HANDOFF_2026-11-23.md); [startprompt](https://github.com/Odourman/mellanrum/blob/docs/romdev-iii-migration-20261123/docs/migrations/ROM_DEVELOPMENT_III_STARTPROMPT_2026-11-23.md)
- [PR33 native Actions 45184894712](https://github.com/Odourman/mellanrum/actions/runs/45184894712); [artifact 14823930347](https://github.com/Odourman/mellanrum/actions/runs/45184894712/artifacts/14823930347); SHA-256 962818fa6a8a26eb22a66c66bd3da519467b78f790b149748ea3f036a97d011a
- [Drive-migrationsdokument](https://docs.google.com/document/d/1kMoR4sjaRHr0XZ8YyZQ0cotdJormmApPD7600Q5jImM/edit); [Drive Native Evidence backup](https://drive.google.com/file/d/1M9eBl579Jq6MvUQg2sehABIV24c3IUiH/view)
- [PR #27 – gammal skyddad 16K F6](https://github.com/Odourman/mellanrum/pull/27): ROM 7ce777dc273e1c30d8621843052e941ced41fcf2961bcdf835576a11c9592446
- [Verification #28](https://github.com/Odourman/mellanrum/issues/28) / [Pachinko #29](https://github.com/Odourman/mellanrum/issues/29): gäller **bara PR27 SHA**
- [Äldre skyddade PR #23](https://github.com/Odourman/mellanrum/pull/23), [PR #16](https://github.com/Odourman/mellanrum/pull/16), [PR #4](https://github.com/Odourman/mellanrum/pull/4). Inga tidigare bevis får automatiskt tillskrivas ny SHA.

## Rådgivande Atari 2600 research i Google Drive
Följande härrör från **andra spelprojekt** och är inte MELLANRUM:s canon, inte heller automatiskt relevant till alla scener:
1. [Originalindex över 30 Atari-trick](https://docs.google.com/document/d/1ASGA7wDZNsYNILVOswdQJfdvpOBtDKM2/edit) – klassificerar klassiska TIA/6507-metoder.
2. [Omvärdering av 30 trick per spelobjekt](https://docs.google.com/document/d/1lC3rz6VF8orv4W1rHSHqAFWZnOlAR5UWcmVfnphGcys/edit).
3. [THE SKRAUN: kombinerade trick](https://docs.google.com/document/d/1dFgqNPsUrEuSajvVC8gGB8odt3WPm54KQXlzUAMCbFI/edit).
4. [Genomförbarhet/10 beslutsgates för andra projektet](https://docs.google.com/document/d/13hW5xRwlcClMCNKn2j-iQ3BBBHOf48Y4drfzFz4-uhM/edit).
5. [HBLANK och 30 trick-risksammanställning](https://docs.google.com/document/d/1XXDmQtS6AcrkP5_ojxen94GjITlEAT2bmzzGwV1ei3s/edit).
6. [PR27:s MELLANRUM teknik-audit 30/30](https://github.com/Odourman/mellanrum/blob/178d915a5395e2b62857886a3c60dd254af858d2/docs/TECHNIQUE_30_AUDIT.md) – gäller äldre kandidat, inte en testbekräftelse för PR33.

### Teknikprioritet för just detta spel
Raster-/PF-manipulation, spritekopiering och M0/BL-återanvändning, positionering (HMOVE), färgregister, multipla kernels, förberäknade tabeller och bankdisciplin är möjliga **förslag som måste mätas i samma ROM**. Försök inte tvinga in alla trick. Flicker/Venetian kan skada originalmaskers läsbarhet; extra cartridge-RAM, SCABS/DPC/DPC+/CDF/ARM bryter vanliga F6-kravet. Att historiska spel visar en teknik är bara feasibility-hypotes för MELLANRUM.

## Source hygiene
Registrera alltid *vad som är original*, *vad som är beslut*, *vad som är implementation* och *vad som är prov*. Ange åtkomstdatum och exakt SHA/filrevision. Saknade originalfiler måste vara "WAITING_FOR_SOURCE", aldrig rekonstruerade som verifierade primärkällor. Undvik att skriva över befintliga handoffs; lägg till daterad supersession med tydligt scope. Google Drive-forskning är inte tillåtelse att använda andra projekts sprites/regelcanon.
