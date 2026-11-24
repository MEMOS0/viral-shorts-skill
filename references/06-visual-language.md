# 06 — Visual language: shots, motion, typography, evidence

Sources: frame-by-frame study of Zack D. Films (3 top Shorts, 31–41 s), Fern documentaries (ISS, Air India, Disneyland: median shot 3.2 s / 2.2 s / 2.5 s), the 80-Short dataset in `data/`, and 60 FirstEngineer Shorts we produced and the user's rejections of them.

## 1. Core law: every shot explains the sentence being spoken

Write the shot list against the narration word by word. If the narrator says "the lake drained", the screen shows the lake draining — not "a lake", not "water", not a logo. Literal first, then metaphorical only if the literal is impossible.

Rejected by the user and banned:
- decorative 3D objects that rotate while unrelated narration plays
- the same image, 3D shot or graphic used twice in one video (and near-duplicates back to back)
- empty black backgrounds behind floating images ("nothing may stand naked")
- AI-generated images or footage of any kind; AI-looking typography (glow, gradient, emoji, Canva templates)
- a single still held longer than ~3 s without a reframe, punch-in or new element

## 2. Shot rhythm

| Parameter | Target for a 30–45 s story Short |
|---|---|
| Median shot length | 1.5–2.5 s (pure storytelling), 2.5–3.5 s (explainers with diagrams) |
| Longest static hold | ≤ 3 s, except one deliberate "silence beat" (≤ 1.5 s of black or freeze) at the turn |
| First cut | 0.8–2.0 s (the frame 0 image must earn the first second, then change) |
| Environment change | every 2–3 s change something big: location, angle, scale, close-up vs. wide |
| Cut points | on the stressed word of the narration, or on action (object hits, door closes, number lands) |

A "shot" can be a continuous camera move: Zack D. uses 0–4 hard cuts in 30–40 s but the camera never stops moving and the subject changes every phrase. Fern uses many hard cuts with motivated moves inside each.

## 3. Shot vocabulary (rotate, never repeat the same type 3× in a row)

1. **Archive photo with motion** — slow push / lateral drift, source label bottom-left (`SOURCE: NTSB`), period-correct grade.
2. **Document / report page** — the page lands on a desk or slides in; camera pushes to the exact line; the line is highlighted (yellow marker wipe, not a glow).
3. **Message / screen** — a monitor or phone in an environment; text types on with keystroke sounds; timestamps in mono.
4. **Map / location** — real geography, a pin drops, a route draws on, a distance counter.
5. **Data line / counter** — the curve draws itself; the number counts up and stops on the stressed word.
6. **Timeline** — dates as physical markers along a line in 3D space; the camera travels along it.
7. **Cutaway diagram** — the object opens (exploded view, cross-section) to show the mechanism; one labelled part at a time.
8. **Scale reveal** — the camera pulls back from a human-sized detail to the full structure (awe).
9. **POV / close-up** — hands on the control, the gauge needle, the bolt.
10. **Reconstruction** — a 3D or drawn recreation of the moment, labelled `RECONSTRUCTION`.
11. **Evidence board** — photos pinned and connected with string; the camera moves photo to photo.
12. **Comparison / small multiples** — designed vs. built, before vs. after, the 3 options side by side.
13. **Black / freeze beat** — one per video at most, at the peak or the turn, with a sound drop.

## 4. Camera motion

- Every move is motivated: it follows a subject, reveals a detail the narrator mentions, or shows scale.
- Bézier ease in/out, never linear; slight organic noise (handheld amplitude ≈ 0.2–0.5 % of frame); focus pulls from one evidence item to the next.
- Speed matches energy: slow push for dread, fast whip or snap zoom for a shock word, pull-back for awe.
- Motion blur on fast moves; no jittery software zooms.

## 5. Vertical composition (1080×1920)

- Subject centre or slightly above centre (eye-line ~ y 700–900).
- Keep text out of the caption band (~ y 1300–1460) and the IG/YT UI zones: top 250 px, bottom 400 px, right 140 px.
- One focal point per frame. If two things matter, cut between them.
- Fill the frame: no letterboxed horizontal archive with black bars — blur-extend, crop to the action, or place the photo inside an environment (desk, monitor, board).

## 6. Typography

- Two families only: a clean grotesk (e.g. IBM Plex Sans / Inter) for headlines and a mono (IBM Plex Mono) for dates, times, sources, data.
- Captions: 1–3 words per chunk, sentence case, bold white with a subtle dark shadow or a soft grey pill; current word may be highlighted in one accent colour.
- On-screen headline text ≤ 5 words, appears on the stressed word, leaves before the next idea.
- Labels for real evidence: `SOURCE: <agency/archive>`; reconstructions: `RECONSTRUCTION`. Always readable (≥ 28 px at 1080 width).
- No glow, no neon gradients, no emoji, no "Did you know?" stickers.

## 7. Colour and look

- One look per video, chosen from the story: newsprint/editorial, sepia archive, cold steel, terminal, night, space, deep ocean. Never the same look on two consecutive uploads.
- Grade archive consistently (contrast, slight grain) so mixed sources feel like one film.
- Accent colour (one) for the critical element: the failed part, the wrong number, the warning.

## 8. Evidence density (credibility)

- At least one real artefact (photo, document, data, map) per 5–7 s.
- Key claims (numbers, quotes, dates) appear on screen as evidence, not just as narration.
- Never invent a document. Reconstructed screens use the real text from the source and are labelled.

## 9. Visual hooks for frame 0 (pick one)

| Type | Example |
|---|---|
| Impossible image | two bridge halves that do not meet |
| Mid-action | the moment the roof is already falling |
| Extreme close-up of the cause | the 11-line function, the bolt, the decimal point |
| Human face at the moment | the pilot, the engineer, the crowd looking up |
| Stark number on evidence | "54 cm" written on a real drawing |
| Scale contrast | a person tiny next to the failure |

Frame 0 must be readable as a thumbnail at 30 % size on a phone.
