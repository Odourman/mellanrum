# Mall: oberoende Verification

**Uppdrag:** MEL-VERIFY-nn  
**Granskningsobjekt:** full commit-SHA, PR, mapper, tv-mode, ROM SHA256 och specificerad designversion.  
**Oberoende:** Verification använder egen hämtning/byggning och bevis. Utvecklarens logg används som testplan men inte som egen mätning.
**Preflight:** DASM-version, Gopher2600-version, Stella-version, runner/miljö, relevanta filhashar.  
**Kontroller:** reproducerbart ROM-byte, fysisk scanline/cycle, originalpixels, PF-kollisioner, RAM/stack, joystick, state-machine, ljud, HUD och speciallägen.  
**Scenarier:** normal verklig spelrutt, maximal samtidighet, återstart, död/fel, gränspassager, lastad/tyst audio, felaktiga stimuli och kända tidigare FAIL.  
**Bevis:** rålogg, dumpade register/spår, bilder, replay, tidsstämplar och tester som inte kunde genomföras.  
**Utfall:** PASS / FAIL / PARTIAL_BOUNDED / NOT_RUN per specificerat krav; separat slutomdöme.  
**Inte behörighet:** ändra gameplaycanon, godkänna framtida etapp eller automatiskt släppa spelet.
