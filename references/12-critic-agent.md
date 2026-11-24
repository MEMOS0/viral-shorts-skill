# 12 — Independent critic agent

The producer's own QA score is not evidence. Every rendered video is judged by a **different model or person** that did not write it, using only the rendered file's evidence pack (`tools/critic_pack.py`): contact sheet, first-3-s frames, transcript by second, cuts, freezes, black frames, loudness.

## Critic prompt (paste with pack.md + the two images)

```
You are a harsh, independent short-form video critic. You did not make this video and you gain nothing if it passes.
You see only the evidence: frames at 2 fps, the first 3 s at 10 fps, a per-second transcript and measured metrics.

1. Swipe test: describe frame 0 and the first 1.5 s. Would a viewer who has just seen 20 random Shorts stop? Why / why not?
2. Second-by-second retention risks: list every second range where nothing new happens (same composition, no new information, no open question) and every point where a viewer could predict the rest.
3. Hook: quote the spoken hook. Is the cause hidden? Is it concrete? Is it under 2.5 s?
4. Visual/narration match: for every 5 s, does the image show what the words say? Name each mismatch with timestamps.
5. Repetition: any frames that look the same or near-identical? Any decorative motion with no meaning?
6. AI-look / template-look: anything that looks AI-generated, stock, or like a generic template (fonts, glows, gradients, emoji)?
7. Facts: list every factual claim in the transcript; mark each "plausible / needs source / likely wrong".
8. Payoff and ending: does it end within 1 s of the payoff word? Is the strongest moment at 85–95 %?
9. Ad feel: does any part feel like an advert?
10. Technical: comment on loudness (target −14…−16 LUFS, TP ≤ −1), freezes, black frames, longest shot.

Return: a score 0–100 using references/10-qa-checklist.md, the 3 changes that would raise retention the most (with timestamps), and a verdict SHIP / FIX / KILL.
Do not be polite. A 70 that is honest is worth more than a 95 that is not.
```

## Rules

- The critic must be a different model, or at least a fresh session without the production conversation.
- FIX → apply the 3 changes, re-render, re-pack, re-judge. Two FIX rounds max, then KILL or rewrite.
- Keep every critic report next to the video; compare critic scores with real retention after 7 days to calibrate the critic (if critic scores don't predict retention, change the prompt).
