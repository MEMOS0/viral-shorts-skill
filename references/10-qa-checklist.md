# 10 — QA gates and scoring rubric

A Short ships only when every gate passes. Pre-render, `tools/check_storyboard.py` must pass and the producer scores the plan (< 85 → fix). This rubric is **production quality, not viral potential**: a 95 can still flop if the topic gate was weak. After render, the **independent critic** (`12-critic-agent.md`) scores the actual video; only the critic's SHIP verdict ships it.

## Scoring rubric (100)

| Dimension | Points | Pass criteria |
|---|---|---|
| Frame 0 + first 1.5 s | 15 | motion at frame 0, word ≤ 0.3 s, literal strange image, understandable muted |
| Hook line | 15 | passes all hook tests in `05-script-writing.md` |
| Open-loop ladder | 10 | ≥ 3 overlapping loops, no 6 s without an open question |
| Shot rhythm | 10 | median 1.5–3 s, no static > 3 s, environment change every 2–3 s |
| Shot meaning | 10 | every shot has a one-line PURPOSE, no repeats, no decoration |
| Evidence & credibility | 10 | real artefact every 5–7 s, source labels, reconstruction labels |
| Sound | 10 | 4 layers, sync hits, silence beat at the turn, −14…−16 LUFS |
| Payoff / ending | 10 | ends ≤ 1 s after payoff word, peak at 85–95 %, loop or strong final image |
| Typography & look | 5 | 2 families, ≤ 5 words, safe area, no AI/template look |
| Shareability | 5 | social currency or warning or debate trigger identified |

## Technical gate

- 1080×1920, 30 fps (or 60), H.264 High, yuv420p, AAC 48 kHz stereo, faststart.
- Duration matches the plan ±0.5 s; video and audio stream lengths equal.
- No black frames > 0.3 s (except the planned beat), no freeze ≥ 0.5 s outside the holds listed in `holds.json` (`tools/critic_pack.py VIDEO OUTDIR --holds holds.json`; the same 0.5 s threshold is the tool default).
- Loudness −14…−16 LUFS integrated, TP ≤ −1 dBTP (`ebur128`).
- Captions inside safe area; nothing important under the IG/YT UI.

## Human-eye gate (watch 3 times)

1. Muted on a phone-size window: is the story clear from visuals + captions alone?
2. Audio only: is the story clear and does it keep pulling?
3. Normal, then swipe test: would you stop at frame 0 if it came after 20 random Shorts?

Any "no" → fix before export.

## Batch gate

- No two consecutive uploads share the same hook type, look, and ending pattern.
- No asset reused across the batch unless it's the brand card.
- Titles and first lines are all different in structure.
