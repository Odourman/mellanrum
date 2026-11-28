# HEALTH VI · Teknisk slutrapport

MELLANRUM: SKOGEN SOM LYSSNAR — GLOBAL HOLD AUTONOMOUS PR59  
Datum: 2026-11-28 · Roll: diagnostik, experiment och utvecklarens tekniska analys. Detta är inte oberoende Verification.

## 1. Källidentitet och G0

| Del | Identitet / resultat |
|---|---|
| PR59 source HEAD | `57f95a7ab48ad981dd5f1d5eeaf3d5a07f61b28d` |
| PR59 ROM | 16 384 byte, F6 NTSC, SHA-256 `47a4d379a050c50bd4c2781c4b82ffcb90e175f8f3e670393ac2a0b2473b701e` |
| Git blob | `ccb1d3b311c1ca176f98fdfed94efec9eb934113` |
| PR58 jämförelse | commit `c4ca55d6a2ed8e6dc6f7790b0e5ced998011e28a`, ROM SHA `4d14a6c8a886962f0ab5def14e69309676bc5dacb805c7aeca2ab1ff225cf7d5` |
| Verktyg | DASM 2.20.14.1; Stella/libretro 8.0_pre `8dd5600`; Gopher2600 pinned source `74c544203378c1448a33c29bc8b4586079b050f4` |
| Reproducering | Två rena PR59-byggen, båda PR59 SHA; GitHub/Drive/CI/source-evidence bytes överensstämmer. PR58 byggdes separat och matchade exakt sin ROM SHA. |

PR59 bankhashar:

| Bank | SHA-256 |
|---:|---|
| 0 | `4f1fefc7513d5c0aef2d1c2a406b77975e59fc60e0a3361fa34455b4c669c49f` |
| 1 | `8d49d78a7f7ea98d1638693767de146b54b7b97673eb5f077fbf9c0554e3a1e8` |
| 2 | `6b82511ba23726be41aa5f7a4e8c2555f5e039ee6fc2ec6a1e0774117cfffbfc` |
| 3 | `96cec4367f3884af818579f5c57158998e5306b5fbe6bb7bbbeca614130851ee` |

Källan byggdes före emulatorprov. De sex aktiva PR59 build inputs jämfördes med exakta Git-objekt på källcommiten. Källpaketets äldre `main.vertical-overflow.asm` är ej input till builden.

## 2. FRI SKOG: isolering och utfall

### Metod

Ett kallt Stella/libretro-core per ROM och varje av fyra startfaser. Samma Difficulty A/LEFT och FIRE i frame 30+fas och 31+fas, därefter ingen input; 240 frameanrop per process. Proben sparade RAM-fält, full framebuffer-SHA per frame, Stella-native rå stereoljud-PCM och faktiska 160×228 PNG-snapshots. PR58 och PR59 identifierades av de verifierade binärerna ovan. Pachinko Issue #60:s Gopher-instruktionsspår och tidigare 12 000-frame-prover återanvändes som underliggande verifieringskontext; de är tydligt märkta upstream och blandas inte med HEALTH VI:s nya specimen.

### Nya experiment

| Experiment | Källändring i isolerad PR59-kopia | Byggresultat / ROM SHA | 240-frame Stella-resultat |
|---|---|---|---|
| `read_restore` | Endast PR58:s `ReadMovement` återställd | PASS build; `a948d12e2f05514f4498c1e1249253bbedad6eaf6f5e1d99572ffd99c7b412cf` | Bildavvikelsen oförändrad; RAM-fält 0 avvikelser. PCM första avvikelse oförändrad, skillnadsmängd marginellt mindre i faser 0–2, lika i fas 3. Ej lösning. |
| `prepare_schedule_restore` | Återställer anropstidpunkt för `PrepareOwlFrame` | PASS build; `94bfbd33d2c048896c8117f6776a3e8db93158ff5f33d0c149f3c1e83c659301` | FRI-bildfelet oförändrat i alla faser. |
| `renderer_restore` | PR58 `RenderPlay` + `PrepareOwlFrame` i PR59; övrig PR59-mekanik kvar | PASS build; `4f04a38fa1e03be72b258605c48f18347c70e23e961055a35b271d788b57be72` | Exakt framebufferparitet 240/240 per fas, 960/960 sammanlagt. RAM-spår paritet. Rå PCM lika PR59, skiljer fortsatt från PR58. Inte kampanjregressionstestad. |
| `fieldpulse_restore` | Endast tidigare `FieldPulse`-block | FAIL build: bank 3 når `$FFE9`, fast `$FFDA` coda-origin bakåtriktad. ROM produceras ej. |
| `read_field_restore` | ReadMovement + FieldPulse återställs | FAIL build av samma bank 3-overflow. |
| `fieldpulse_pad` | Åtta cyklers kompensation med NOP-probe | FAIL build: slutposition `$FFDD`, tre byte över `$FFDA`. Ingen NOP-kandidat kördes. |
| `fri_restore_all` | Renderer_restore + PR58 ReadMovement + PR58 FieldPulse | FAIL build: aktuell position `$FFE9` vid `$FFDA`. Ingen binär eller emulatorresultat. |

### Bildens kausala grund

- Baseline PR59 divergerar visuellt från PR58 från första kontrollerade FRI-bilden. HEALTH VI:s fyra körningar skiljer 206–209 av 240 framehashar, beroende på fas; observerade utvalda logiska RAM-fält förblir identiska.
- PR58-renderaren återställer hashparitet under hela 240-framefönstret för samtliga faser. Autentiska PNG jämförelser 160×228 vid frame 36, 48, 57 visar 32–52 pixelavvikelser i PR59 och exakt 0 med renderer_restore.
- `ReadMovement` och flytten av `PrepareOwlFrame` återställer inte bilden. Det utesluter dem som tillräcklig enskild bildorsak i detta scenario.
- Starkt isolerat: den visuella avvikelsen orsakas av PR59:s renderingsväg (HUD/kron-/stam-/owl-preparation i `RenderPlay`-området). Inte isolerat: vilken delrutin eller enskild COLUBK/COLUPF/PF0/PF1/PF2, WSYNC/HMOVE eller TIA-access som är nödvändig. Ingen binär intern pixeldiff finns här som skulle bevisa en enda skyldig instruktion.
- Renderer_restore återför även PR58:s `PrepareOwlFrame`-kod och anropsschema. FRI-paritet är bevisad, men kampanjens autonoma rörelse/presentation är inte. Därför får den inte marknadsföras som fix eller LAB_BEST.

### Ljud: vad är bevisat

PR59 mot PR58 gav för första 240 frames samma ljudregressionssignatur i Stella PCM som i utökad Pachinko-evidens: första olika 16-bitarsvärde per FRI-fas 31 588 / 32 658 / 33 698 / 34 940. I HEALTH VI:s renderer_restore finns exakt samma rå PCM som PR59, så den visuella återställningen påverkar inte det isolerade ljudet.

PR59:s `ReadMovement`-kontrollflöde sparar en CPU-cykel i den FRI-väg där PR58 tar `BNE` vid `$F156` och PR59 tar `BEQ` vid `$F153`. PR58:s FRI-väg genom `FieldPulse` omfattar `LDX mode / CPX #1 / BNE FieldPulseStore`, vilket inte körs i PR59. Den observerade skillnaden är totalt 9 CPU-cykler = 27 färgklockor till `ChooseBank` i de dokumenterade naturliga spåren. Native Stella visar de sex score-registerskrivningarna 27 färgklockor tidigare i PR59 med samma skrivna värden. Pachinko-spåret visar tidiga färgfaser också: COLUBK samma värde en färgklocka tidigare, PF0/PF1/PF2 en CPU-cykel tidigare. Detta är verkliga timingkorrelationer som starkt stöder ljudets fasdrift.

Exakt kausal separation av PCM-skillnaden är **INCONCLUSIVE**: `ReadMovement`-återställningen ensam löser den inte; den äldre `FieldPulse`-vägen kunde inte byggas in med nuvarande fasta bank-layout; den kombinerade timingproben saknar ROM. Ingen PCM-fasjustering eller efterredigering användes. PR58 har också historiska ljudskillnader mot äldre PR-kandidater, vilket är ett separat jämförelsepar och bedöms inte här.

## 3. CPU, raster och TIA

| Mått | Resultat | Gräns |
|---|---|---|
| Stem13 | 75/76 CPU-cykler inklusive nästa WSYNC i det uppmätta villkoret; instruktioner och cycles i `static_report.json` | Villkorligt kernelresultat, inte varje branch eller alla scenarier. |
| Full frame raster | Upstream natural Stella/Gopher-körningar höll 262 linjer i 18 712/18 712 och 18 713/18 713 kompletta frames; ytterligare instrumenterad Stella-replay 21 500 kompletta 262-linjersbilder | Bounded spår; inget globalt all-path-PASS. |
| TIA timing | Gopher `ONSTEP TV,CPU,TIA` och Stella/libretro PCM/registerväg fångade observerade PC/beam-/registerfaser i FRI. | Full register-write-beam-karta för alla kernelgrenar saknas. |
| Branch-/page-cross | Källlistningar visar page-safe placering för sprite- och glyph-tabeller. Static report markerar indexerade tabellfönster. | Alla grenutfall, alla X/Y page-cross kombinationer och HMOVE-scenarier inte fullständigt uttömda. |
| Timer / WaitVBlank | PR59 använder TIM64T under VBLANK/overscan och läser INTIM i loopar; autonom 96-frame-logik återanvänder `beatFrames`. | Ingen cykelräddning/optimering prövades; inga påståenden om varje timer-branch. |
| Säkra förbättringar | 0 uppmätta CPU-cykler sparade i någon rekommenderad produktionsväg; 0 rastermarginaler förbättrade. | HEALTH VI producerade diagnoser, inte optimerad produkt. |

Bankväxling sker via F6-hotspots `$FFF6–$FFF9` och fast trampoline `$FF90/$FF96/$FF9A`. Ingen ny bank-layout eller kod flyttades. PR59:s renderer_restore ändrade bank 3-kod endast i specimen och bibehöll samma mapper, men kampanjsemantik testades inte.

## 4. RIOT RAM, liveness och stack

PR59 deklarerar 118 byte vid `$80–$F5`; `$F6–$F7` är två reserver; `$F8–$FF` är åttabytes stackbudget. Källan nollställer `$80–$FF` vid reset och startar SP `$FF`. RAM-matrisen i `06_RIOT_RAM_BYTE_MATRIX.csv` har en rad för var och en av 128 adresser. Symbolnamn, faktisk address, storlek, kommentar/ägare och statiskt antal operandträffar är härledda ur PR59-källan och native `.sym`.

Viktiga ägare: `pfbuf` 48 byte för 8×2×3 TIA PF-byte; `mapRows` 8 byte för kollisions-/kartbitdata; spelfas, rum, uggla, sten, exit, ljud-/beat-/input-/slot-/närvarotillstånd; pekare och arbetsbyte; `markerPtr` två byte. Läslivslängder korsar naturligt frames för bland annat spel-, beat-, input-, slot-, närvaro- och rörelsetillstånd. Arbetsbyte (`candidate*`, `attempt`, `work*`, `pfIndex`, `rowIndex`, pointers, `moveTemp`) återanvänds mellan rutiner, men ingen full interprocedural liveness/def-use-matris eller varje-byte read-before-write-bevis har skapats. CSV:n uttryckligen markerar detta som `STATIC_DATAFLOW_INCOMPLETE`; lexical operand count är inte dynamisk frekvens.

Stack: upstream conditional-valid-flow CFG omfattar 2 813 tillstånd, 3 160 kanter och 37 JSR-sites; djupaste samtidiga JSR=4, 8 stackbyte. Native Stella såg naturlig trädändringsväg vid SP `$F7` och lägsta stackwrite `$F8`, dvs. stackbudgeten nåddes. `$F6/$F7` canary överlevde ett separat tidigare stresstest. HEALTH VI förbättrade inte stackdjup eller marginal. Inget av de två reserverade bytena kan räknas ledigt.

Bedömning: **0 säkra RAM-byte frigjorda**. Alias eller temporär återanvändning skulle kräva nya statiska och dynamiska livslängds-/audio-/bildtester; gör ingen sådan ändring utan ny order.

## 5. ROM-bankinventering

| Bank | Dokumenterad layout | Sammanhängande fri yta | Bedömning |
|---:|---|---|---|
| 0 | 3 840 score/data-byte `$F000–$FEFF`; score-engine/table från `$FF00`; gemensam F6-call/return `$FF90–$FF99`; reset `$FF9A–$FF9F`; hotspots `$FFF6–$FFF9`; vectors `$FFFC–$FFFF`. | `$FFA0–$FFF5` är 86 adresser utan aktiv referens i denna scorebank, men F6-hotspots/vectors och hopp-/återkomstkontrakt ligger lägst. | Potentiell fysisk kodyta, ei visad säker att återanvända eller nå från spelbank 3 utan dispatch-/returkostnad. 0 säker byte frigjord. |
| 1 | Som bank 0, Act II score/data och banklokal score-engine. | Samma 86-byte råa intervall. | Samma säkerhetsgräns. |
| 2 | Som bank 0, Act III score/data och banklokal score-engine. | Samma 86-byte råa intervall. | Samma säkerhetsgräns. |
| 3 | Spelkernel, tabeller, grafik, karta, title/coda och FRI/kompanjonlogik. Fasta trampoliner/reset/hotspots/vector. | Static inventory: 6 byte före trampoline och 3 byte efter coda före hotspot; separata små hål, inte en sammanhängande 15-byte yta. | Full FieldPulse restore överlappar coda `$FFDA`; 15-byte overflow. 0 säker byte frigjord. |

Samtliga scorebankar har exakt 3 840 score/sample-byte × 3 = 11 520 score-byte plus real runtime engine. Äldre offline RLE-vinst från HEALTH IV är inte en ROM-vinst; ingen decoder har implementerats eller mätts, och inga bytes räknas frigjorda. Ingen ljudkomprimering eller bankkomprimering kördes här.

## 6. 30 Atari-tekniker, bedömning mot PR59

Klassificering beskriver hur tekniken möter den faktiska källan, inte att den genomförts som HEALTH VI-optimering.

| # | Teknik | Klass | Faktisk bedömning |
|---:|---|---|---|
| 1 | Tidsmultiplex | ALREADY_USED | P1-återanvändning för två S3-symboler; ingen ny aktörsmultiplexering mätt. |
| 2 | Mid-scanline GRP | ALREADY_USED | TIA-registerstyrning finns i kernels; ingen ny spritepassering bevisad. |
| 3 | Venetian blinds | REJECTED_WITH_EVIDENCE | Skulle bryta skyddade 8-radersmasker/läsbarhet. |
| 4 | Flicker | REJECTED_WITH_EVIDENCE | Avstått av läsbarhetsskäl; ingen nytta mätt. |
| 5 | Dynamic PF | ALREADY_USED | Packade kartor och rekonstruktion av PF-buffer redan i PR59. |
| 6 | Resize mitt i frame | REJECTED_WITH_EVIDENCE | Mask-/formrisk, ingen godkänd nytta. |
| 7 | Asymmetrisk PF | ALREADY_USED | Titel/nummerlayout och spelplanens PF-kontrakt. |
| 8 | Tvålinjekernel | REJECTED_WITH_EVIDENCE | Bevarad 75/76-cykels Stem13; ingen bättre budget mätt. |
| 9 | VDEL | NOT_APPLICABLE | Ingen verifierad funktionell nytta i den fasta kerneln. |
| 10 | HMOVE | ALREADY_USED | Finpositionering används; ingen ny HMOVE-optimering mätt. |
| 11 | Late HMOVE | REJECTED_WITH_EVIDENCE | Kompatibilitets-/rasterrisk utan demonstrerad nytta. |
| 12 | Rasterfärg | ALREADY_USED | Sten/exit och statusfärger ligger i PR59. FRI timing är regresserad. |
| 13 | Six-digit-kernel | NOT_APPLICABLE | Spelet visar inte sexsiffrig score. |
| 14 | Flera kernels | ALREADY_USED | Separat title, play och coda; olika vertikala spelband. |
| 15 | NUSIZ | ALREADY_USED | P1 dubblerar S3-symboler. |
| 16 | REFP | ALREADY_USED | Uggle-/spriteorientering och spegling. |
| 17 | Missile/ball | ALREADY_USED | Markör-/feedbackformer använder TIA-objekt. |
| 18 | PF score mode | REJECTED_WITH_EVIDENCE | Olämpligt mot färg-/bildkanon; ingen testad vinst. |
| 19 | PF priority | REJECTED_WITH_EVIDENCE | Ingen ny geometri- eller lagerändring mätt. |
| 20 | Collision latches | REJECTED_WITH_EVIDENCE | Diskret karta är spelregel; TIA-latch ersätter inte kanonisk gridlogik. |
| 21 | RIOT timer | ALREADY_USED | Frame pacing, VBLANK/overscan och beat-logik används. |
| 22 | Stack/spegling | ALREADY_USED | Vanlig RIOT-stack med bank-spegling; 8-byte budget är full i witness. |
| 23 | Illegal opcode | INCOMPATIBLE | Avstå; minskar kompatibilitet, ingen tillåten vinst. |
| 24 | Tabeller/cykelprecision | ALREADY_USED | PF/kart-/sprite-/metadata-tabeller finns; HEALTH VI mätte ingen ny vinst. |
| 25 | Stack-TIA | INCOMPATIBLE | Riskerar stackbudget och två skyddade byte. |
| 26 | Timing-scroll | NOT_APPLICABLE | Fast bräda och spelrum. |
| 27 | SCABS | INCOMPATIBLE | F6-standardkontrakt utesluter detta. |
| 28 | Extra RAM | INCOMPATIBLE | Hårdvarukravet är RIOT 128 byte utan extra RAM. |
| 29 | DPC | INCOMPATIBLE | Utanför hårdvarukontraktet. |
| 30 | DPC+/CDF/ARM | INCOMPATIBLE | Utanför hårdvarukontraktet. |

`USEFUL_MEASURED` nya HEALTH VI-tekniker: **0**. Renderer_restore är en kausal diagnos, inte en överförbar optimering. 

## 7. Tekniska förutsättningar för presentation

Ingen ROM-/CPU-/RAM-vinst kunde omvandlas till bättre owl interpolation, markörrespons eller L2-ljudprioritering, eftersom ingen säker optimering hittades. Renderer_restore visar att PR58:s gamla renderingsfas ger FRI-pixelparitet, men den kan påverka autonom kampanj; den är därför inte en färdig teknisk lösning för jämnare owl-flygning. För eventuell framtida, separat auktoriserad implementation rekommenderas att behålla autonoma precompute-data tills sektionerad rastermätning bevisar en bättre variant.

## 8. Statusmatris

| Område | Status |
|---|---|
| PR59 byteidentitet, 2 native builds | PASS |
| PR58 byteidentitet, separat native build | PASS |
| FRI-strikt framebufferregression i PR59 | FAIL, återproducerad |
| FRI renderingsväg som tillräcklig pixelorsak | PASS_BOUNDED, 4 faser × 240 bilder |
| FRI PCM-paritet experimentellt återställd | FAIL / NOT_SOLVED |
| Kontroll av spellogik/RAM i probespåret | PASS_BOUNDED; valt RAM-fältsspår, inte allt tillstånd |
| Full per-instruktion TIA-residualisering | INCONCLUSIVE |
| Full 15-rums ROM-test på experimentbuild | NOT_RUN |
| Säkra RAM-byte | 0 frigjorda |
| Säkra ROM-byte | 0 frigjorda |
| Stackmarginal | Oförändrad; befintlig 8-byte budget når maximum |
| Full all-path raster | INCONCLUSIVE |
| Full RAM liveness/read-before-write | INCONCLUSIVE; CSV uppmärkt per adress |
| Human play/listening | NOT_RUN |
| Independent Verification | NOT_RUN |
| Physical NTSC hardware | NOT_RUN |
| LAB_BEST | Inte skapad |

## 9. Obligatoriska slutfrågor till MAIN V

1. **Nya tekniska problem:** PR59:s FRI-renderingsväg är tillräcklig för en 32–52-pixelskillnad i de sparade kalla frame-captures; FRI-ljudet har bestående PCM-fasavvikelse; bank 3 har så lite och så splittrad kodmarginal att återställning av den äldre FieldPulse-rutinen kolliderar med fasta coda-origin.
2. **Exakt bildorsak:** den isolerade orsaken inom testat framefönster är PR59:s ändrade `RenderPlay`/`PrepareOwlFrame`-renderingsväg. En intern HUD/krona/stam/TIA-instruktion är inte ytterligare isolerad.
3. **Exakt ljudorsak:** ännu inte fullständigt bevisad. Uppmätt korrelat är 1 cykel skillnad i FRI `ReadMovement` plus 8-cykels bortfall i `FieldPulse` (= 9 CPU cycles/27 color clocks till musikbank) med score-registerwrites tidigare; dessa stödjer fasdrift men ingen byggbar experimentell återställning gav strikt PCM-paritet.
4. **FRI-paritet:** bildparitet återställd i diagnosspecimen 4/4 faser; ljudparitet inte återställd. Specimen ej kampanjtestad.
5. **Säkra RAM-byte:** 0.
6. **Säkra ROM-byte per bank:** bank 0=0, bank 1=0, bank 2=0, bank 3=0. Fysiska råhål är inte bevisad kodkapacitet för säkra ändringar.
7. **Sparade CPU-cykler:** 0 godkända produktvägar. PR59:s baseline tar 1+8 cykler mindre än PR58 på FRI timingvägarna, men detta är orsak till fasavvikelse, inte rekommenderad optimering.
8. **Stack:** djup/marginal oförändrad; full befintlig åttabytesgräns nås i naturlig trädväg.
9. **Raster/TIA-marginal:** inga marginaler förbättrade; 262-linjers frames är bounded baseline-bevis, inte globalt timingpass.
10. **Jämnare uggleflygning:** ingen ny resursförutsättning etablerad. Renderer_restore måste genomgå autonom kampanjtest innan den kan rekommenderas.
11. **Misslyckade försök:** full FieldPulse restore, read+field restore och kombinationen med renderer_restore överträdde fast `$FFDA`-origin; NOP-pad overflowade 3 byte. Läs- och Prepare-scheduling-restores byggde men löste inte bildfelet. Renderer_restore löser bildmen inte PCM och dess kampanjrisk är oprövad.
12. **Rekommenderade förbättringar till ROM DEVELOPMENT:** använd renderer_restore enbart som differensunderlag; gör separata, återkopplade tester av HUD-, kron-/stam- och owl-timing i ny auktoriserad rättningsorder. Spara PCM och TIA-fas rått; testa alla fyra FRI-faser och kampanj samtidigt.
13. **Avvisa:** NOP-lappning utan register/flagga-/TIA-bevis; temporära RAM-alias; rå 86-byte scorebank-hålyta som “ledig”; PR58-renderare som färdig fix utan kampanjtest; offline RLE som ROM-vinst utan runtime decoder proof.
14. **Kvarvarande risker:** PCM-kausalitet; alla fyra FRI-branchpath pixel/TIA-instruktioner; liveness def-use; stack all-path; alla branch/page-cross/HMOVE-kombinationer; kernel all-path; kampanj/coda/SELECT/RESET på alla experimenthashes; mänsklig ljud-/spelbarhetsbedömning; fysisk NTSC; oberoende Verification.
15. **LAB_BEST bättre än PR59?** Nej sådan binär saknas. Renderer_restore är en begränsad diagnostisk vinst för FRI-bildparitet, men inte ett tekniskt bättre spelbevisat övergripande ROM. Därför blev `MELLANRUM_HEALTH_VI_LAB_BEST_EXPERIMENT_ONLY.bin` inte skapad.

## 10. Testreproduktion och evidensgräns

Reproducera de nya 240-frame-proven med `emulator/fri_probe.py` och Stella libretro 8.0_pre core. Harness startar separat subprocess för varje ROM/fas, använder samma controllersekvens, sparar per-frame state/framebuffer hashes, PNG och rå 31 440 Hz stereo PCM. Variantsourcen och varje lyckat native build-output finns under `source/`; misslyckade buildloggar finns kvar. Gopher-spåren och tidigare längre Pachinko evidens finns under `emulator/` och `reference/PR59_PACHINKO_EXTENDED_EVIDENCE.zip`.

Detaljkommandon: `emulator/PACHINKO_REPRODUCE.md`. Genomför inte nya builds till PR59 eller produktbranch; laborationsspecimen är diagnostiska.
