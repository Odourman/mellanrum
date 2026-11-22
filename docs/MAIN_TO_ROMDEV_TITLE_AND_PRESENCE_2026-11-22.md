# MAIN → ROM DEVELOPMENT: title + Presence visual revision

Date: 2026-11-22. **User expressly authorizes both changes.**
Base: existing open Draft [PR #4](https://github.com/Odourman/mellanrum/pull/4), immutable baseline commit `8bdecde79a6bc1ecb804484d5d257f4f1a99b052`, standard 4 KiB NTSC baseline ROM SHA256 `ec791333da37613ec99ea70b2a983ecc1666b4e576211ece41a8e40bd14cbaed`.
Status: **AUTHORIZED CHANGE ORDER / NOT IMPLEMENTED**. Implement in ROM DEVELOPMENT, not in MAIN, PACHINKO or Verification.

## User-approved visual changes

### A. Title screen: exact single readable name

The ONLY textual word displayed on the title screen must be **MELLANRUM**. Render this exact complete spelling, legible as one word, not the prior vertically split MEL/LAN/RUM abbreviation. No KAM, FRI or other menu words. Keep the existing campaign/FRI SKOG menu functionality, console SELECT/FIRE navigation, accessibility and start/RESET behavior; choose a purely graphical, distinct non-text selection indicator or other elegant nonverbal affordance. Do not remove Free Forest to achieve a clean title. No unintended extra on-screen words.

### B. Presence: perceptible but unidentifiable fleeting silhouette among conifers

Preserve V5.1's concept: the Presence is a disturbing ambiguity made from **negative space between the trees**, not a normal monster. The player should occasionally glimpse a short-lived, **incomplete suggestion of a silhouette**. It must be visible in actual TIA rendering on the emulator, not merely an optional illustrative PNG or the existing small HUD icons. Keep it sparse and ambiguous, no face, eyes, chasing, distinct corporeal sprite, name, HP, AI, hitbox or jump scare.

Implement under Atari 2600 TIA constraints. Prefer render-only PF shape/band subtraction or other safe kernel method that leaves actual collision/map bits unchanged and does not steal the owl P0, player marker P1, stone BL, exit M0, or timing critical raster updates. No fictitious framebuffer, arbitrary alpha or impossible independent colors. The silhouette may use a staged form: in noninteractive foreshadows II-05 t4 / III-01 t4 / III-02 t2 and for active intrusion in III-03, III-04 and III-05. **At minimum each of III-03, III-04 and III-05 must have a real-emulator screenshot/frame where a discernible but unidentifiable silhouette appears, and a comparable before/after frame where it does not.** Do not insist on an impossible full independent moving sprite if render-only PF or transient sprite reuse meets the artistic need.

Use the exact V5.1 mechanics and timing: III-03 warning t1 active t2–3; III-04 warning t0 active t1–2; III-05 warning t2 active t3–4. Intercept of an otherwise-legal tree FIRE flips stone polarity instead and does not mutate tree or book echo; first active tick autonomously flips stone iff no intercepted valid tree FIRE; do not alter phase/echo/stone/exit/room rules. Keep warning/active/release legible even with sound off, and avoid aggressive strobe or contrast flashes.

**The visible fleeting silhouette is now a design requirement.** If truly infeasible with the tested hardware budget, do NOT quietly fall back to 'HUD only' and claim complete. Provide a measured failure and alternatives for MAIN. You have wide creative/technical freedom to solve the implementation, including optimizations, reorganizing title/kernel and, if demonstrably necessary, an appropriately documented cartridge mapping/ROM size change. Do not silently change normative game mechanics or break existing PR features.

## Build and evidence required before handoff

1. Read CURRENT_PROJECT_STATE, DECISIONS, original V5.1 and GRAPHICS V5.1, the 15 original rooms, native source and existing tests. Preserve their authority and exact geometry. Check both original ZIPs if accessible; note any evidence gaps.
2. Implement title and Presence together as a coherent upgrade. Keep source, generated data, assembler listing, ROM, build scripts and checks in a revision PR/branch; do not merge or release autonomously.
3. Run native DASM and all existing source/model/control/timing checks. Add **new** automated expectations for exact title text/screen state, unchanged menu controls, Presence visibility and exact state machine under interference. Prefer actual emulator logs and screenshots at pre-warning, warning, active and release, including overlapping P0/P1/BL/PF states.
4. Use actual Stella/Gopher emulator, not only developer CPU simulator, to capture title and each intrusion room before/during/after; verify 262 NTSC scanlines on difficult frames and visually inspect. Ensure no hidden collisions, TIA color smearing or lost controls. Preserve artifacts (PNG, traces, WAV if audio changed).
5. Return immutable commit, full source diff, native .bin and its new SHA-256, evidence for all 15 rooms at least in developer model plus actual emulator cases for the changes, test matrix PASS/FAIL/NOT_RUN, legitimate design deviations, and an updated handoff to MAIN. Distinguish BUILD_PASS / DEVELOPER_PASS / EMULATOR_OBSERVED; never assert independent approval.

## Boundaries and release coordination

The existing Pachinko report and independent Verification status apply to **OLD baseline SHA only**. Any changed ROM gets a new commit/hash; Pachinko Phase 2 must rerun on that immutable updated candidate. Independent Verification must remain separate, and old PASS markers must not transfer silently to the new ROM. If the 4K limit cannot hold, demonstrate necessity; do not fake the same ROM hash.

MAIN's explicit artistic acceptance will inspect the actual title text and the intended 'glimpsed' quality in the emulator images. PACHINKO runs diagnostics, independent VERIFICATION decides technical readiness, MAIN decides art/release. No merge without further explicit approval.
