# Förslag till separat PACHINKO-riskgranskning – ännu inte startad

**Specimen:** HEALTH `LAB_STACK_INLINE_PADDED_B` SHA256 `8a59b84eb5151f78d40e6943c854d7e42c166b531aee3d40432182d32dcdf03b`. **Jämförelse:** RC1 SHA256 `456005ed691860b32c44b79f2a71666f622b005f5a798eadf9b549c59cff13bd`. Inget mandat för produktändringar, automatiskt separat PACHINKO, RC2-promotion eller release.

Verifierat före denna eventuella grind: egen full 15-rumskampanj i Stella och Gopher; två rena native byggen per ROM; 5→4 JSR, naturligt stackbusvittne; 19 652/19 652 frames och 20 594 248/20 594 248 PCM-värden lika i en source-guided A/B replay; 540 000 idle, 15 kausala, 15 SELECT/återhämtning, FRI 50 010 + 27 000 beatwrap; 64 förskjutna men deadline-säkra titelskrivningar.

**Riskstyrda kvarstående tester för senare *separat auktoriserad* PACHINKO:**
1. Naturliga controllerkombinationer som kan ta `BCS OwlTryNext` med branchförändring −1 cykel; särskilt parallellt FIRE/Presence/echo/phase, samt uppföljning till nästa faktiskt relevant timer/WSYNC.
2. Naturliga rumsövergångar vid giltigt `GeoMapHi X=1/2` och `RoomStoneY X=4/5`; timer/VBLANK-restmarginal och första synliga TIA-skrivning. För en branch en cykel snabbare och tre domängiltiga pagecross-klasser en cykel långsammare, skilj ny tidsläggning från ny pixel.
3. Terminala sprite/StemLastFast/Top16+HUD x9 med `ackType 0..3`, pending låst FIRE-target, Presence release/active, recall och beat wraps; scenval som ger verkliga maximala deadline-kandidater, inte full kartesisk produkt av onåbara tillstånd.
4. Naturliga bank1-musiktrampoliner under akt II med live CPU-bus, full `$F6..$FF` stackbytes och återgång före/efter, inklusive FRI/RESET/coda.
5. Självständig controllerfuzz med återställningar och boot-/power-on-tillstånd, inklusive stresstest av den två-byte stackreserven; utan RAM-korruption som falskt naturligt fel.

**Orakel:** 262 scanlines och verkliga 6507/TIA bus-write-deadlines. Gopher ONSTEP CPU/TIA instruktionsstart är inte den faktiska STA-busskrivningen; WSYNC stannar processorn och kan ge skenbar sen position i debugger. Aktuell originalverifiering innehåller genuin `TRACE STRICT` bussposition, inklusive titelmarginaler. Titelscener Y2/Y3 har exakt +3 colorclock i 64 accesser men 0 framebuffer-pixeldiff. Negativ kontroll PR47/avsiktligt sent-BCS 263 vid x9 finns. Instrumentera utan att ändra specimen.

**Bedömning inför denna grind:** inga nya bekräftade releaseblockerare; `LAB_INDEPENDENT_DELTA_PASS_BOUNDED`, men `GLOBAL_ALL_PATH_TIMING_INCONCLUSIVE`. Människa/original Atari ej testad. PACHINKO:s tidigare RC1-rapport på en annan SHA kan inte automatiskt återanvändas.