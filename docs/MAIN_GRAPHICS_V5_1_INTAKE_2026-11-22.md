# MAIN – GRAPHICS V5.1: mottagningsgranskning

**Datum:** 2026-11-22. **Status:** `VISUAL_DIRECTION_ACCEPTED_FOR_IMPLEMENTATION`; ZIP-bytes inte självständigt verifierade av MAIN. **Ingen ROM- eller emulator-PASS.**

## Källor och begränsningar

I projektets filhistorik lokaliserades både `MELLANRUM_GRAPHICS_V51_FINAL_TILL_MAIN_2026-11-22.zip` och `MELLANRUM_V5_1_KRITISKT_REVIDERAT_TILL_MAIN_2026-11-22.zip`. De kunde inte råmaterialiseras i denna MAIN-session. Därför kunde MAIN inte själv extrahera alla bilagor, kontrollera SHA-256-manifest eller köra de rapporterade testerna.

Däremot kunde MAIN läsa GRAPHICS:s fullständiga 34-sidiga `00_GRAFIKAVHANDLING_FULLSTANDIG.pdf` via projektets indexerade filtext och den separata `STARTTEXT_TILL_MAIN.txt`. V5.1:s 1 396-radiga kritiska avhandling var läsbar och hade tidigare granskats i `docs/MAIN_V5_1_REVIEW_2026-11-22.md`. Gällande GitHub-status och beslut har kontrollerats. Äldre GRAPHICS-G0-förslag som själv anger att V5.1-original saknades har lägre källvärde än den senare källbundna slutrapporten och får inte ersätta den.

## MAIN:s accepterade visuella produktionsriktning

- `GITTERSKOG / BILDMELLANRUM`: kantig, grafisk träsnittsskrift där negativt rum bär betydelse.
- Exakt tre materiella motiv: barrträd i speglat PF, en P0-uggla, en fast BL-sten. P1-mellanrummet är spelarens gränssnitt, M0 kan märka utgång, M1 är valfri detalj.
- 10×8 rutnät, två 6+14-scanline PF-band och fem grundgeometrier i tre akter. Alla 15 originalrum och koordinater ska jämföras mot V5.1:s `reference/rooms.json`, inte rekonstrueras från PNG.
- Eko-/fas-/Närvaroindikering via speglingskompatibla marginaltecken, med 48 HUD-kombinationer som ROM-datahypotes. Inte 48 samtidiga RIOT-buffertar.
- Närvaron saknar fjärde kropp. Primärt render-only negativ i PF-krona; säker fallback med marginalindikator och P1-kvittens. Inget får ändra själva `tree_bits` eller ta bort verklig FIRE-kapning.
- BL delar `COLUPF` med PF och kan inte rita 8×8-spricka. BL + speglingskompatibel separat stenpolaritetssymbol är godtagbar fallback.
- Visuell kontrollinformation måste fungera i svartvitt och utan ljud. Inget helskärmsstrob eller skräckjakt.
- Ljudets konstnärliga betydelse står kvar enligt V5.1 och får inte behandlas som en valfri kosmetisk effekt.

**GRAPHICS rapporterar** 25 stycken 8×8-masker, 15 källbundna rumsdata, 48 HUD-kombinationer, 69 filer, 20/20 Python-unittester och 15/15 abstrakta lösningar. Dessa har **inte** reproducerats av MAIN i denna session. Grafikrapportens avsnitt M nämner också 23 genererade masker: verklig JSON/ASM-källa och dess manifest måste avgöra. Felsiffern får inte tyst döljas.

## Nästa produktionsorder

MAIN har på användarens uttryckliga instruktion publicerat en **sammanhållen fullspelsorder** till ROM DEVELOPMENT:

[ROM DEVELOPMENT – full-game order](ROM_DEVELOPMENT_FULL_GAME_ORDER_2026-11-22.md)

ROM DEVELOPMENT får stort självständigt mandat att färdigställa hela spelet utan mellanliggande mikrogodkännanden, med faktisk källkontroll som första interna arbetsmoment. MAIN har **inte** startat kodning eller själv producerat ROM.

**Oberoende VERIFICATION förblir separat.** Ingen statisk grafikkontroll är ett Stella-, PAL-, hardware- eller releasegodkännande.

Statusetiketter: `SOURCE_ONLY`, `GRAPHICS_REPORTED`, `ZIP_NOT_VERIFIED_BY_MAIN`, `ROM_NOT_RUN`, `EMULATOR_NOT_RUN`, `INDEPENDENT_VERIFICATION_PENDING`.
