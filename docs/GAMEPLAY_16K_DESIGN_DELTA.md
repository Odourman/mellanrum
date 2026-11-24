# MELLANRUM Issue26 – playable design delta from frozen 4KiB PR23

Prior frozen PR23 HEAD `2a6794f42b2991231a4927cc8c1f5dcdd291bc9b`, ROM SHA256 `63e719a362ae2eb5689484ca7c28c628b495a2843723898ebec3fe6374c43bdc`. New PR27 F6 version remains separate, draft/unmerged.

## 15 rooms (five each act) – what changed
All 15 **individually authored playable PF/geometry and required-action witnesses from PR23 remain the foundation**. The new 16KiB revision changes artistic response and expands optional strategy rather than erasing tested room solutions or manufacturing arbitrary win barriers. Each of the 15 is now associated with its own 256-frame three-stream composition (768 bytes/room) with authored tree topology and room seed determining timber/texture/rhythm. This means rooms based on the same act do not share identical audio feedback. Actual direct per-room 6507 bank lookup uses `room % 5` within the selected act bank.

**New alternative decision – 'återkalla ekot' (recall an echo):** In Act II/III, while a tree already has a queued reversal, pressing FIRE on that tree a second time *cancels the future echo* and instead flips the stone's polarity without flipping the tree's current bits. This gives a controllable alternative to simply waiting for the echo and changes subsequent autonomous owl direction at the stone. A selected tree with no queued echo behaves normally. Invalid/uneditable trees still reject FIRE. Act I has no echoes and stays a clearer introduction. Source reference `reference/engine.py` implements the same state transition and `reference/test_engine.py` tests it. Existing 15 winning controller traces remain usable, but neither a new mandatory recall nor user artistic approval is presumed.

**Graphic/acoustic rhythm:** The volume of the real second TIA channel modulates low-key background luminance; each act has a different base hue; title and Act I remain deep drone, Act II acquires restrained memory pulse, Act III uses more irregular dissonant timbres. Presence still interrupts with abrasion and silences. Trees stay green. Original three 8x8 U3 owl wing masks, vertical beak, two S3 symbols, Presence negative-space silhouette, three-act/15-room progression, hardware difficulty control, FRI SKOG, title/coda all remain. No boss, weapons or traditional score.

## Human play and difficult design limitations

This is a substantive **auditory, visual and strategic-choice expansion**, not a claim that all fifteen maps were entirely redesigned **again** or that 16KiB makes the game intrinsically difficult. The existing original PR23 15 room geometries are already different; the source oracle captures them. Future end-user playtest can reject insufficient qualitative gameplay novelty without changing the fact that the new 16K ROM functions.

**Development evidence must be exact-ROM SHA scoped.** New native Stella, Gopher, idle, counterfactual and extended-stress tests on new hash; independent Verification/Pachinko distinct. An earlier PR23 test is never evidence for F6. The source model is not a substitute for real emulator joystick routing.
