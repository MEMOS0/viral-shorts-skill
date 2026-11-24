# 12 — Independent critic agent

The producer's own QA score is not evidence. Every rendered video is judged by a **different model or person** that did not write it, using only the rendered file and its evidence pack (`python tools/critic_pack.py VIDEO OUTDIR --holds holds.json`): `proxy.mp4` (540×960 with audio), contact sheet, first-3-s frames, a frame after every cut, per-second transcript, motion and loudness, freezes, black frames.

## Watch the video, not the plan

- If the critic model can play video+audio, it **watches `proxy.mp4` at least twice** (once normally, once muted) before reading any metric. Frame sheets miss flicker, caption/voice drift, mumbled words, music masking the narration and SFX that land late.
- If it cannot, it says which checks it could not do (audio, sync, flicker) and marks them *not checked*; it never assumes they pass.
- It never sees the producer's own score, plan rationale or chat. It may see `storyboard.json` (to check that each shot's stated purpose is visible) and `research.md` (to check facts).
- Sound: judge narration intelligibility over music on a phone speaker, music and ambience support, silence beats, SFX timing against the picture, loudness/peak from metrics.
- Captions: readable at phone size, inside the safe area, on the spoken word (±0.15 s), no misspelt names.
- Sources: every archive label legible and matching the image; reconstructions labelled; no claim on screen that research.md does not support.
- Hook ↔ payoff: does the ending answer exactly the question the first line opened?


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

Return two separate numbers: QA 0–100 using references/10-qa-checklist.md (production quality: errors, sync, sound, clarity), and VIRAL 0–10 (your prediction of feed performance: topic, angle, first frame, payoff; say how confident you are). Never let one raise the other. Then the 3 changes that would raise retention the most (with timestamps), the list of checks you could not do, and a verdict SHIP / FIX / KILL (based on QA gates; a low VIRAL number is a topic problem, send it back to 11).
Do not be polite. A 70 that is honest is worth more than a 95 that is not.
```

## Rules

- The critic must be a different model, or at least a fresh session without the production conversation.
- FIX → apply the 3 changes, re-render, re-pack, re-judge. Two FIX rounds max, then KILL or rewrite.
- Keep every critic report next to the video. After 7 days add `critic_qa`, `critic_viral` and the real metrics to `data/calibration.csv` and run `python tools/calibrate.py data/calibration.csv` (needs ≥ 8 videos; meaningful at ≥ 30). If the CI of ρ includes 0, the critic does not predict results: change the prompt, and stop using VIRAL for decisions until it does.
- For calibration without your own channel yet: `tools/blind_pairs.py` builds label-blind TOP/LOW pairs from `data/`; a critic that can't beat 50 % on them has no measured skill at spotting hits.


## Critique quality: Accurate, Complete, Constructive [R]

(Idea adapted from OpenMontage's reviewer skill, which cites the CMU/Harvard CHAI study on video-language critique; rewritten here.) A finding names a problem; a critique tells the producer how to fix it. Every critic note must be:
- **Accurate**: points at a timestamp, a shot number, a word in the transcript or a frame in the contact sheet. No location means a guess, so delete the note.
- **Complete**: when you find one problem, scan the whole video for the same class of problem ("#07 repeats #03's photo" means check every pair).
- **Constructive**: every critical note carries a concrete fix ("#11 0:23.4: the push ends 0.6 s after 'closed'; stop it on the word"). If you cannot propose a fix, label it *investigate*, not *critical*.

Severity: **critical** (blocks SHIP: a factual error, a repeated asset, an unreadable label, a dead first second, clipping), **suggestion**, **nitpick**. Don't inflate severity. **Two FIX rounds maximum**, then SHIP with the remaining warnings listed or KILL. Perfectionism stops the batch.

## Slideshow-risk score (0–5 per dimension, average ≥ 3 = FIX, ≥ 4 = KILL/replan) [E]

| Dimension | Score high when |
|---|---|
| Repetition | several shots share the same layout, shot size, asset or move |
| Decorative visuals | a shot has no stated purpose (what the viewer learns or feels) |
| Weak motion | moves exist but none is motivated by the subject or the information |
| Missing shot intent | no start/end frame, no hold, no cut cue in the plan |
| Text overreliance | more than ~30 % of shots are text, stat or title cards |
| Unearned "cinematic" | claims cinematic but has no hero shot, no light source, no held moment |
