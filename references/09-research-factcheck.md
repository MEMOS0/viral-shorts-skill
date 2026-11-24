# 09 — Story selection, research and fact-check

## Story scoring (pick only stories scoring ≥ 20/25)

| Criterion | 1 | 5 |
|---|---|---|
| Strange concrete hook available | abstract | an image nobody has seen |
| One-sentence cause | needs a lecture | "a hyphen", "pounds vs kilograms" |
| High-arousal emotion | mild | awe / anger / anxiety obvious |
| Real visual material (photos, documents, footage) | none | archive photos + report pages + data |
| Relevance to the audience (engineers, students, tech) | none | they could make the same mistake |

## Sources (in this order)

1. Official investigation reports (NTSB, TSB, AAIB, BEA, CSB, Coast Guard MBI, NASA, court documents).
2. Peer-reviewed papers, engineering case studies (ASCE, IEEE, university course notes).
3. Reputable press of the time (archive).
4. Wikipedia only as a map to the primary sources above.

## Research file per video (`research/<id>.md`)

```
STORY:
CORE CAUSE (1 sentence):
HOOK FACT + source:
KEY NUMBERS (value, unit, source, page):
PEOPLE (name, role, quote + source):
TIMELINE (date/time, event, source):
CONTESTED / UNCERTAIN POINTS (and how the script softens them):
VISUAL ASSETS (file, licence, credit line):
```

## Fact-check gate (before narration is recorded)

- Every sentence of the script is mapped to a line in the research file.
- Every on-screen number matches the source exactly (units, rounding, dates, time zones).
- No invented quotes; reconstructions are labelled.
- Images: licence checked (public domain, CC BY / BY-SA with credit, official government works, or licensed). Credit list saved in the video folder.
- Sensitive topics (deaths): respectful wording, no gore, no mocking victims.


## Reference-video breakdown: five aspects per shot [R/E]

(Structure adapted from OpenMontage's video-reference analyst and the CHAI five-aspect captioning; rewritten here.) When analysing a Short you want to learn from, use the contact sheet and the transcript to describe **every shot** in five labelled aspects. Write N/A when an aspect does not apply; leaving an aspect out silently is the most common analyst mistake.
1. **Subject**: what or who, how many, and how it changes across shots (revealed, disappears, switches).
2. **Subject motion**: actions in time order.
3. **Scene**: setting, time of day, POV (aerial, macro, top-down, handheld, locked-off), and **overlays as their own layer** (text, labels, arrows, watermark).
4. **Spatial framing**: shot size, subject position, foreground/mid/background use, and how these change.
5. **Camera**: playback speed (real time, slow motion, time-lapse), lens, height, angle, focus/DOF, steadiness, move.

Then classify the **motion type** of each shot: real footage, an animated still (pan/zoom/parallax), a 3D render, a code-drawn diagram or a static image. Never guess. The mix tells you the production method you would need to match it. End with **what makes it work** (two or three specific things) and **how ours differs**: same structure with a different story, same story from a different angle, or a different visual treatment. Never copy.
