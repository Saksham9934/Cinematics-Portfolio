# The build briefs — how this portfolio was directed

A record of the creative direction each scene was built from, in the order it
arrived. Every brief came with reference assets (images/videos in the project
root), and every brief carried the same standing rules:

- **The supplied reference is the pixel-level source of truth.** Replicate it
  as closely as technically possible; never generate replacement assets —
  anything needed is extracted from the references themselves.
- **Entrances are choreographed, never plain fades**: darkness → light →
  atmosphere → elements → settle → subtle continuous life (~2s reveals).
- **Card sets appear as ONE coordinated event**, never one-by-one.
- **The person is the main character** and layers IN FRONT where the brief
  says so.
- **Strict palette discipline per scene**; premium and restrained, not flashy.
- **Portrait recomposes intelligently** — never just shrinks desktop.

## Scene 1 — Cinematic hero opening
Black screen → the walking man (video 1, white backdrop removed, no visible
rectangle) enters centre → the giant red distressed SAKSHAM rises from below,
dissolving and sharpening in → WELCOME TO MY WORLD drops in front → chips,
arrows and dots fly in → header reveals → settled hero with subtle motion and
mouse parallax. Mid-build corrections: videos 2 & 3 removed entirely; the
top-left dot cluster removed; final layering fixed as background → SAKSHAM →
walking person IN FRONT → labels → header, with the animated reveal kept.

## Scene 2 — The creative universe
All twelve tool cards materialise TOGETHER, rise bottom-to-top as one event,
settle, then float; red energy lines draw and travel; central circle alive.
Superseded by direction: play the supplied reference film itself as the
section ("i just want to see the section 2 video"), then "add text on the
video" — the chapter title now sits over the footage; the loop seam hides
behind a breathing veil.

## Scene 3 — A journey through time
Match the reference: giant clock whose hand is driven by the cursor mapped
intelligently to the years 2021–2026 (projection onto the timeline, not raw
mouse X), smooth inertia, active-year cards, curved rail, rotating floor
rings, warm amber/red grading. Final corrections: person slightly left and
BROUGHT IN FRONT of the cards (his own layer over the deck), visible via
reference lighting (warm pool, wraparound rim, floor bounce — not brightened),
clock rebuilt to the reference (ball pivot, divider-pose hands, ornate screw
ornament, beam projecting light into the active year), year labels dark and
warm rather than white pills.

## Scene 4 — The project universe
Replicate the reference inch-for-inch: the amphitheatre of twelve project
screens around the creator. Built by cutting the reference apart — every card
becomes a sprite of the reference's own pixels, the emptied room becomes the
plate the shader stages and re-lights (ring, floor-circle ignition, wet
shimmer). Cards rise as one system with pop-overshoot and dephased floating;
pointer moves the whole universe by depth; hover lifts a card while its
siblings ease back; scroll dollies in.

## Scene 5 — Certifications (built, then removed)
A man walks out of darkness into a cyan world; five glass plaques summoned as
one event. Required a black-void matte preset (subject brighter than the
backdrop, detached smoke kept, silhouette solidify with a tracked soft
corridor, luminance-shaped smoke translucency). The section was later deleted
at the client's direction; its tools remain in `tools/` for regeneration.

## Finale — the closing shot (footer)
Replicate `Footer image.jpg` exactly: the reference itself is split into
layers — the smoking man GrabCut-matted out of the artwork, everything else
(wordmark + red fog) becoming a plate staged by a luminance-gated reveal (the
title surfaces through the fog and sharpens). Captions return as live DOM;
a whispering functional row carries contact/socials/copyright. A later brief
added a SECOND frame: past the settled scene, extra scroll slides the
supplied Ferrari still in from the left — damped progress, blur-to-sharp,
leading-edge shadow — the film's last cut.

## Cross-cutting passes
- **Background-removal fixes**: repeated briefs demanded frame-stable person
  isolation — no halos, no flicker, cigarette and natural smoke preserved,
  "filmed inside the environment" compositing (room-tinted smoke, rim light
  from each room's glow).
- **Final polish pass**: every section awakens on screen (reveal thresholds
  raised), ~2s reveal pacing, buttery easing, HD sprite sharpening, 60fps.

The technical companion to this document is the README, which explains how
each direction was implemented.
