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
