# 02 — Viewer psychology for Shorts / Reels

Every rule here maps to a concrete edit decision. If a rule cannot change a frame, a word or a sound, it does not belong in the plan.

## 1. The scroll decision (0.0–1.5 s)

A viewer on a vertical feed decides to stay or swipe before they consciously "watch". Three systems fire, in this order:

| Order | System | What it reacts to | What you must give it in the first frame |
|---|---|---|---|
| 1 | Orienting response (pre-attentive) | motion onset, sudden contrast, a face, a human hand, a loud transient | something already moving at frame 0; never a fade-in from black, never a logo |
| 2 | Pattern recognition | "is this the same as the last 50 things I scrolled?" | an image that does NOT look like generic stock / template content |
| 3 | Information gap (Loewenstein 1994) | "I know a bit, I don't know the rest" | one concrete, strange, specific fact the brain cannot finish on its own |

Rules:
- Frame 0 is the thumbnail of the feed. It must already be the most interesting image in the video's first 10 seconds.
- Words start at 0.0–0.3 s. A silent first second is a swipe.
- The first sentence names a concrete object + an impossible-sounding outcome ("A bridge was built 54 centimetres too high."), not a topic ("Today we talk about bridges.").

## 2. Curiosity: Loewenstein's information-gap theory

Curiosity is a feeling of deprivation caused by a perceived gap between what one knows and what one wants to know. Practical consequences:
- The gap must be **small and specific**. "Something went wrong" is too wide (no pull). "The pilot had 22,300 kg of fuel, the computer said he had enough. He had less than half." is a narrow gap with a clear missing piece.
- Curiosity needs a **little prior knowledge**: show the viewer enough that they feel they could almost solve it.
- Curiosity is **refreshable**: answer one gap and open the next one in the same sentence ("…and that was not the worst part.") — this is the open-loop ladder (section 6).
- Never fully close the main gap before 75–85 % of runtime.

## 3. Emotion and sharing (Berger & Milkman 2012, NYT most-emailed study)

Content that evokes **high-arousal** emotions is shared more; low-arousal emotions are shared less.

| Emotion | Arousal | Effect on sharing | How to use it in an engineering story |
|---|---|---|---|
| Awe | high | strongly positive (the single strongest predictor) | scale reveals: "the lake drained in three hours", the 3D pull-back that shows the real size |
| Anger / moral outrage | high | positive | "they were warned in 2018" — documented ignored warnings, cost-cutting, cover-ups |
| Anxiety | high | positive | "this software is still in use", "your phone does this too" |
| Surprise / interest | — | positive | counter-intuitive mechanism, the one-number twist |
| Practical value | — | positive | one sentence of transferable lesson ("check units", "test the reused code") |
| Sadness | low | negative | never end on pure grief; convert loss into a lesson, a twist or awe |

Rule: every Short must deliberately target ONE high-arousal emotion (awe, anger, or anxiety) plus surprise. Write it in the plan as `EMOTION: awe+surprise`.

## 4. Made to Stick (Heath & Heath) — SUCCESs checklist per script

- **Simple**: one core idea; if you need "and" to state it, cut one half.
- **Unexpected**: break a schema in the first sentence (bridges meet in the middle — this one didn't).
- **Concrete**: numbers, objects, names, places, times: "11 barges", "10:47 a.m.", "a 16-bit integer".
- **Credible**: one visible source per key claim (report page, archive photo with source label).
- **Emotional**: a person, not a system — "the pilot", "the engineer who signed it".
- **Story**: chronological action verbs; a protagonist doing things.

## 5. Narrative structure that survives a swipe feed

Shorts are not mini-documentaries. They are a single turn of a story.

- **In medias res**: open at the strangest moment, not the beginning (Zack D. Films pattern: "She woke up and found a bullet under her pillow").
- **Value change (McKee)**: each beat must flip a value — safe→danger, known→unknown, success→failure. A beat that changes nothing is cut.
- **The "You see," turn**: around 55–70 % of runtime, a backstory reveal re-frames everything shown so far ("You see, his ship had been torpedoed…"). It is the second hook.
- **Payoff at the end, not before**: the final line delivers the reveal or twist and the video ends within ~0.5–1.0 s of the payoff word. No outro, no "thanks for watching".
- **Peak-end rule (Kahneman)**: viewers judge the whole video by its peak and its final second. Put the best visual at the peak and the best line at the end.

## 6. The open-loop ladder (retention mechanics)

Retention drops whenever the viewer feels "I get it now". Prevent that with a ladder of loops:

| Loop | Opens at | Closes at | Example phrasing |
|---|---|---|---|
| L1 main question | 0–2 s | 80–95 % | "A bridge built 54 cm too high." → why? |
| L2 mechanism | 15–30 % | 55–70 % | "The engineers had done the maths correctly." → then how? |
| L3 escalation | 35–50 % | 70–85 % | "And it got worse." |
| L4 twist / stakes | 60–75 % | last line | "The fix doubled the error." |

Each loop opens **before** the previous one closes ("Overlapping loops"). Never have more than ~6 s without an open question.

## 7. Attention mechanics inside each second

- **Pattern interrupts** every 2–3 s: a cut, a reframe, a zoom, a new object entering, a sound hit. Measured on top story Shorts: median shot 1.5–3 s (see `data/analysis_summary.md`).
- **Prediction error**: the brain rewards being slightly wrong. Make one visual go somewhere unexpected per 10 s (a number that counts past where it "should" stop, a camera that pulls back to reveal scale).
- **Gaze direction**: put the next important element where the eye already is (centre, slightly above middle for vertical). Do not make the eye hunt.
- **Cognitive load**: one new piece of information per shot. Text on screen ≤ 3–5 words at a time; never read text the narrator isn't saying.
- **Faces and hands**: humans orient to faces and to hands manipulating objects; use archive photos of the real people and hands-on-object moments.
- **Zeigarnik effect**: unfinished sequences are remembered — interrupt a counter or a progress bar and resume it later.

## 8. Credibility in a world of AI slop

Audiences in 2025–2026 swipe content that looks AI-generated or templated.
- Use real archive photos, documents, report pages with a visible source label.
- Reconstructions are labelled ("RECONSTRUCTION").
- Typography restrained and consistent (one sans + one mono). No glows, no rainbow gradients, no emoji spam.
- Specific numbers with units and dates read as truth; round adjectives ("massive", "insane") read as clickbait.

## 9. Sharing triggers (why someone sends it)

People share to look smart, to warn, or to make someone feel something. Engineer at least one of these into each Short:
- **Social currency**: "I bet you didn't know…" fact the viewer can repeat at dinner.
- **Warning**: "this still happens".
- **Identity**: speaks to engineers, students, people who've had a bad boss.
- **Argument starter**: a defensible but debatable judgement in the last line ("It wasn't the software that failed.") → comments.

## 10. Bridging to a product without feeling like an ad

- The story is 100 % story. No product mention in the first 85 % of runtime.
- The bridge, if any, is a single sentence that is a *lesson* first and a *product* second: "The engineer who flagged it was ignored. Hiring should notice people like that." — then the brand card for ≤ 1.5 s.
- Maximum 1 in 4 Shorts carries an explicit bridge; the rest only the end card.
- CTA asks for one low-friction action (follow / comment a word), never "link in bio" in YouTube descriptions if links are forbidden.
