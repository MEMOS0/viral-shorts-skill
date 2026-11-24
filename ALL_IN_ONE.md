---
name: viral-story-shorts
description: End-to-end playbook for planning, writing, designing and QA-ing high-retention story Shorts / Reels (engineering disasters, science, history) for YouTube Shorts and Instagram Reels. Use when asked to create, script, storyboard, edit, review or score vertical short-form videos, hooks, captions or posting plans.
---

# Viral Story Shorts — master skill

You are a short-form director, writer, editor and sound designer in one. Your output is a Short that a viewer cannot swipe away from, that is factually correct, and that looks like a premium documentary — never like AI slop or a template.

This skill is built on measured data (76 top-performing Shorts from 16 channels analysed second by second — `data/`), frame-level study of Zack D. Films and Fern, peer-reviewed psychology (Loewenstein, Berger & Milkman, Heath, Kahneman, McKee, Murch), platform guidance (YouTube, Mosseri), and lessons from producing 60 Shorts and a long-form documentary for FirstEngineer.

## Read in this order

| File | Use it for |
|---|---|
| `references/01-platforms.md` | what YouTube and Instagram reward; formats, safe areas, metrics |
| `references/02-psychology.md` | why people stop, stay, rewatch, share |
| `references/03-hooks.md` | hook taxonomy + measured hook library + 60 templates |
| `references/04-second-by-second.md` | the time grid and the per-shot spec line |
| `references/05-script-writing.md` | writing the VO: hook, turn, payoff, banned phrases |
| `references/06-visual-language.md` | shot vocabulary, rhythm, camera, typography, evidence |
| `references/07-sound-design.md` | 4-layer sound, sync hits, silence beat, loudness |
| `references/08-endings-loops-cta.md` | payoff, loops, CTA, product bridge without ad feel |
| `references/09-research-factcheck.md` | story scoring, sources, fact-check gate |
| `references/10-qa-checklist.md` | 100-point rubric + technical and human-eye gates |
| `data/analysis_summary.md` | the numbers: durations, cut rates, WPM, first-word timing, hooks |
| `templates/` | the exact deliverable formats |
| `examples/` | two fully worked Shorts |

## Non-negotiable rules

1. Words start ≤ 0.3 s; frame 0 is already moving and is the most interesting image of the first 10 s.
2. Hook line = strange concrete fact, in medias res, ≤ 12 words, cause hidden.
3. Every shot explains the words spoken over it; one-line PURPOSE or it's cut.
4. No asset twice in a video; no static composition > 3 s; environment changes every 2–3 s.
5. ≥ 3 overlapping open loops; never 6 s without an open question.
6. A "You see," / "But here's the thing" turn at 55–70 %.
7. Peak visual at 85–95 %, payoff line last, video ends ≤ 1 s after the payoff word.
8. Real evidence only (archive, documents, data, maps) with source labels; reconstructions labelled; **no AI-generated images or footage**.
9. Typography: one sans + one mono, captions 1–3 words, no glow/gradients/emoji.
10. Sound: narration + music + ambience + sync hits; −14…−16 LUFS; silence beat at the turn.
11. Facts: every number/name/date sourced; no invented quotes.
12. Variation: no two consecutive videos share hook type + look + ending pattern.
13. Product mention: story first; bridge in ≤ 1 of 4 videos, as a lesson, never a pitch.

## Workflow (do every step, in order)

1. **Pick the story** with the 25-point score (`09`). Reject < 20.
2. **Research file** with sources for every fact (`09`).
3. **Write the payoff line, then the hook, then the turn** (`05`). Generate 10 hooks from `03`, score each with the hook score in `03`, keep the best; keep the runner-up for an A/B trial reel.
4. **Full script** 80–120 words; read aloud with a timer; fit 35–45 s.
5. **Beat map** on the time grid (`04`): loops L1–L4, emotion, turn, peak.
6. **Shot list**: one spec line per shot (`04` format) using the shot vocabulary (`06`); rotate types; check for repeats.
7. **Sound plan** per shot (`07`).
8. **Title, caption, hashtags, cover frame, pinned comment** (`01`, `08`).
9. **Score with the rubric** (`10`). < 85 → revise the weakest dimension and re-score.
10. **Deliver** using `templates/short_plan.md` (one file per video) and `templates/batch_plan.md` (for a batch).
11. After publishing: log the metrics (`01`) and update `data/` and the hook library every 10 videos.

## When asked for N videos

Produce a batch plan table first (story, emotion, hook type, length, look, structure, ending pattern) and make sure the variation rule holds, then produce N complete `short_plan.md` deliverables. Never shorten later videos in the batch: video 10 gets the same depth as video 1.


---
<!-- references/01-platforms.md -->

# 01 — Platform mechanics: YouTube Shorts and Instagram Reels

Treat these as the scoreboard. Every creative decision should move at least one of these signals.

## YouTube Shorts

| Signal | What it means | Creative lever |
|---|---|---|
| **Viewed vs. swiped away** (Shorts feed, YouTube Studio > Analytics > Content > Shorts) | % of feed impressions where the viewer did not swipe away immediately. The first gate. Good story Shorts sit roughly 70–85 %; under 60 % the Short usually stalls. | frame 0, first 1.5 s of audio, first sentence |
| **Average % viewed / retention curve** | Can exceed 100 % because replays loop. A flat line (no "cliff") is the goal. | open-loop ladder, shot rhythm, no dead air |
| **Replays / loops** | Since 31 Mar 2025 a Shorts "view" counts every start or replay; "engaged views" is the old metric. Loops therefore lift both reach and the view counter. | seamless last→first frame, last line that completes the first line |
| **Likes, comments, shares, subscribes from the Short** | Secondary signals; shares carry the most weight for reaching new viewers. | debate-worthy final line, social-currency fact |

Format facts:
- Vertical 9:16, 1080×1920, up to 3 minutes (since 15 Oct 2024). Story Shorts that go viral cluster at **25–60 s**; see `data/analysis_summary.md` for measured durations.
- Title: ≤ 60 characters, concrete, curiosity gap, no clickbait lies. The title appears small in the feed: the first 3–4 words carry it.
- Description: 1–2 lines + 3–5 hashtags. (Project rule for FirstEngineer: **no links in YouTube descriptions**.)
- Upload natively; do not upload files with another platform's watermark.

## Instagram Reels

Adam Mosseri (Head of Instagram) has repeatedly named the three most important Reels ranking signals:
1. **Watch time** (does the viewer watch past the first seconds, do they rewatch).
2. **Likes per reach**.
3. **Sends per reach** (DM shares) — the strongest signal for reaching *non-followers*.

Other published guidance:
- Original content is favoured; reposted / aggregated content and visible watermarks are down-ranked.
- Reels up to 3 minutes are recommended to non-followers; the hook still decides everything.
- Use on-screen text and captions (most people watch muted at first glance).
- "Trial reels" can test a hook on non-followers before showing it to followers — use it to A/B two hooks of the same video.

Format facts:
- 1080×1920, keep important content inside the **safe area**: top ~250 px and bottom ~400 px are covered by UI (username, caption, buttons); right ~140 px is covered by the action rail.
- Caption: first line = the hook restated as a question or bold claim (it shows before "more"); then 2–4 short lines; then a single CTA; then 3–8 hashtags.
- Cover frame: choose the strongest visual frame with ≤ 4 large words; the grid crops to 3:4 (1080×1440) on the profile.

## Shared rules for both

- Upload the same master to both platforms, never with a watermark from the other.
- Captions (burned-in) are mandatory: 1–3 words per chunk, high contrast, inside the safe area.
- Loudness: integrated −14 to −16 LUFS, true peak ≤ −1 dBTP. Narration always on top; music ducks 8–12 dB under voice.
- Post 30–60 min before the audience is most active (Mosseri). Measured windows for a European audience in our research: weekdays 12:00–13:00 CET and 18:00–21:00 CET; Thursday morning and Wednesday midday/evening strongest (Buffer, 9.6M posts, 2026); weakest Friday/Saturday.
- Consistency beats volume: 1–2 Shorts per day per platform, every day, with varied formats.
- Judge a Short after 48–72 h, not 2 h. Shorts frequently get a second wave days later.

## Metrics to log per video (for the feedback loop)

`viewed_vs_swiped`, `avg_pct_viewed`, `avg_view_duration`, `retention_at_3s`, `retention_at_50pct`, `loops`, `shares`, `sends_per_reach` (IG), `comments`, `subs_gained`, `profile_visits`, `waitlist_signups` (via UTM'd bio link). After every 10 videos, compare hooks, durations and emotions against these numbers and update `data/` and `references/03-hooks.md`.


---
<!-- references/02-psychology.md -->

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


---
<!-- references/03-hooks.md -->

# 03 — Hooks: taxonomy, scoring, templates

A hook is three things at once, all inside 0–2 s: **the first frame**, **the first sound**, **the first sentence**. Write all three together.

## A. Hook types (measured in `data/` — see section E for real examples)

| # | Type | Formula | Engineering example |
|---|---|---|---|
| 1 | In medias res | [Person] [did/found strange concrete thing] | "The pilot looked down and both engines were silent." |
| 2 | Impossible result | [Object] [did something objects can't] | "A London skyscraper melted a parked car." |
| 3 | Tiny cause, huge effect | [Tiny thing] [destroyed huge thing] | "One missing hyphen destroyed an $18 million rocket." |
| 4 | Number shock | [Precise number] + [unit] + [consequence] | "54 centimetres. That's how far apart the two halves of this bridge were." |
| 5 | Ignored warning | [Someone] warned [them] [time] before | "Three years before the roof fell, an engineer wrote this letter." |
| 6 | You-POV / stakes | "You're [role]. [Situation]. You have [time]." | "You're the only engineer awake. The alarm says five missiles are coming." |
| 7 | How it works (Zack D. title format) | "How [familiar thing] actually works" + immediate visual | "This is how a lake disappears in three hours." |
| 8 | Myth flip | "[Common belief] is wrong." | "The Titanic wasn't sunk by the iceberg alone." |
| 9 | Countdown / time pressure | [Time] until [disaster] | "The building had 72 hours before a hurricane could knock it down." |
| 10 | Mystery object | show object + "This [object] [killed/saved/cost] [X]." | "This 11-line piece of code broke half the internet." |
| 11 | Comparison | "[A] vs [B]: one of them [failed]" | "Same bridge design. One stood for 100 years. One fell in four months." |
| 12 | Still happening | "[Danger] is still [present]" | "This bug is still in millions of devices." |

## B. Hook score (score every candidate, keep ≥ 24/30)

| Test | 0 | 3 | 5 |
|---|---|---|---|
| Concreteness (noun + number/place/time) | abstract | one concrete | noun + number + place |
| Gap size (cause hidden, outcome clear) | no gap / all told | wide vague gap | narrow precise gap |
| Arousal (awe/anger/anxiety/surprise) | neutral | mild | strong |
| Visual literalness (can frame 0 show it?) | nothing to show | generic image | the exact moment/object |
| Speed (spoken length) | > 4 s | 2.5–4 s | ≤ 2.5 s |
| Novelty (not seen in the last 50 Shorts) | common | known twist | genuinely new angle |

## C. First-frame recipes

- **Mid-action freeze → motion**: start 0.2 s before the impact so motion happens in the first 10 frames.
- **Push-in on the cause**: frame 0 is a macro shot of the bolt / line of code / gauge; camera pushes; cut on the noun.
- **Wrong picture**: an image that looks wrong (bridge halves misaligned, car melted) — the eye stops to resolve it.
- **Face + reaction**: real archive face of the person at the moment.
- **Number on evidence**: the critical number on a real document, highlighted on the first stressed word.
Never: logo, title card, black, slow fade, a narrator greeting, generic stock skyline.

## D. First-sound recipes

- Hit + ambience in at 0.0 s, first word at 0.0–0.3 s.
- Diegetic sound of the event (alarm, creak, crack, splash) under the first word.
- No music intro. Music enters under the first word or at the first cut.

## E. Measured hook library

See `data/hooks_library.md` — first 3 seconds (spoken words), first-word time, first-cut time and view counts of 76 top Shorts. Patterns extracted from it are summarised in `data/analysis_summary.md`.

## F. 60 fill-in templates

1. "[Person] [verb]ed [object] and [unexpected result]."
2. "This is the only [thing] that ever [impossible outcome]."
3. "[Number] [unit]. That's all it took to [disaster]."
4. "In [year], [place] [lost/built/sank] [thing] in [short time]."
5. "Engineers built [thing] perfectly. Then [one mistake]."
6. "Nobody noticed [flaw] for [time]."
7. "[Thing] passed every test. It failed on day one."
8. "The fix made it worse."
9. "[Person] had [time] to stop [disaster]. He didn't know."
10. "This [object] cost [amount] and lasted [time]."
11. "They tested everything except [one thing]."
12. "[Two groups] used different [units/standards]."
13. "The warning was written down. On page [N]."
14. "A [junior/student/intern] found the flaw. Nobody listened."
15. "[Thing] was designed for [X]. It got [Y]."
16. "The computer said [X]. The truth was [Y]."
17. "This is what [event] looked like from [unusual POV]."
18. "[Big thing] was brought down by [tiny thing]."
19. "They called it [nickname] after it [incident]."
20. "[Place] woke up to [strange sight]."
21. "For [time], [thing] was the safest in the world. Until [event]."
22. "If you [everyday action], you're using [failed thing]'s fix."
23. "Why [famous object] has [strange feature]."
24. "One line of code. [Consequence]."
25. "[Number] people walked across it. Then it started to sway."
26. "The [object] was [N] times [stronger/weaker] than they thought."
27. "This photo was taken [time] before [event]."
28. "[Agency] still doesn't know exactly why."
29. "The engineer signed it. Then he [action]."
30. "Imagine [concrete scenario]. That really happened in [year]."
31. "It took [long time] to build and [short time] to destroy."
32. "[Material] doesn't do that. Except here."
33. "Every [unit of time], [thing] got [worse]. Nobody measured it."
34. "This [thing] almost started a [war/collapse]."
35. "[Company] lost [amount] in [minutes]."
36. "The [part] was reused from [old system]. That was the problem."
37. "They moved one [bolt/rod/decimal]. [Number] people died."
38. "[Object] was upside down. For [time]."
39. "The pilots had no fuel, no engines, and [X] minutes."
40. "A [animal/person] noticed before the engineers did."
41. "The simulation said it was safe."
42. "It wasn't the [obvious cause]. It was [surprising cause]."
43. "[Thing] is still [there/running/in use] today."
44. "Here's why [familiar thing] is shaped like this."
45. "The only survivor was [unexpected]."
46. "[Thing] was built [measurement] off. On purpose."
47. "They fixed it at night, in secret."
48. "[N] seconds. That's how long [thing] lasted."
49. "[Thing] worked in [place A]. In [place B] it [failed]."
50. "The manual said [X]. The [person] did [Y]."
51. "This [object] is why [rule] exists."
52. "[Number] alarms went off. They were all ignored."
53. "A spelling mistake / a unit / a rounding error [consequence]."
54. "No one died. That's the strangest part."
55. "They knew. [Time] before."
56. "The [thing] was too [safe/strong/good]. That was the problem."
57. "This is the most expensive [typo/bolt/line] in history."
58. "[Thing] flew/stood/ran perfectly — in the wrong direction."
59. "He found it by accident while [everyday action]."
60. "[Thing] made a sound nobody had ever heard."

Templates are starting points only; every final hook must pass section B and use the story's real concrete details.


---
<!-- references/04-second-by-second.md -->

# 04 — Second-by-second blueprint

Plan every Short on a time grid before writing visuals. Times below are for a **35–45 s** story Short (the sweet spot measured in `data/`). Scale proportionally for 25 s or 60 s.

## Master grid (40 s example)

| Time | % | Beat | Narration job | Visual job | Sound job | Loop state |
|---|---|---|---|---|---|---|
| 0.0–0.3 | 0 | **Frame 0** | first word starts ≤ 0.3 s | strongest image, already moving | transient hit + ambience in | — |
| 0.0–2.0 | 0–5 | **Hook line** | strangest concrete fact, ≤ 12 words | literal image of that fact; first cut 0.8–2.0 s | music cue starts under | L1 opens |
| 2.0–5.0 | 5–12 | **Hook confirm** | second line makes it worse / specific ("And no one noticed for 3 years.") | 2nd and 3rd shot: new angle, evidence | spot effect on each cut | L1 widened |
| 5–12 | 12–30 | **Context in motion** | who / where / when, told as action, not exposition | 3–4 shots: archive, map, person | ambience establishes place | L2 opens ("They had checked everything.") |
| 12–20 | 30–50 | **Escalation** | stakes rise each sentence; concrete numbers | diagram / mechanism / counter | tension builds, rhythmic hits | L3 opens ("Then it got worse.") |
| 20–23 | 50–58 | **Mini-payoff** | answer L2 partially, reward the viewer | evidence close-up, highlighted line | hit + short riser | L2 closes, L3 still open |
| 23–25 | 58–63 | **Turn** (second value flip; the first "but" already came at ~40 %, measured) | "You see, …" / "But here's the thing:" | black beat or freeze ≤ 1.5 s, then a new look | music drops out → silence → heavier cue | L4 opens |
| 25–34 | 63–85 | **Reveal / mechanism** | the real cause, in plain words + 1 number | cutaway / reconstruction / exploded view | sync effects on each part | L3 closes |
| 34–38 | 85–95 | **Consequence / scale** | cost, lives, what changed | scale reveal (pull-back) or the aftermath photo | biggest hit of the video | — |
| 38–40 | 95–100 | **Payoff line** | twist or punch line, ≤ 10 words, ends on the strongest word | final image that can loop into frame 0 | tail ≤ 1 s, blends into the first sound | L1 closes / L4 closes |
| 40–41.5 | — | **Brand card** (optional) | none or 3 words | logo + one line, ≤ 1.5 s | soft tail | — |

## Rules that apply on every second

- No second without either a word, a cut, a move, or a sound event.
- Never more than 3 s on one composition; never more than 6 s without an open question.
- The viewer must be able to say what the video is about by 3 s.
- The narrator never explains what the viewer can already see; the screen never shows something the narrator does not need.
- Put the **highest-arousal visual** at 85–95 % (peak) and the best line at the end (peak-end rule).

## Length variants

| Length | Use for | Adjustments |
|---|---|---|
| 20–28 s | single-image shocks, one-number twists | hook 0–2 s, one escalation, turn at ~55 %, payoff; aim for a perfect loop |
| 30–45 s | standard engineering story | grid above |
| 50–60 s | multi-step mechanism or two-twist stories | add a second escalation at 40–55 %; second turn at 70 %; keep median shot ≤ 2.5 s |
| 61–180 s | only with proven audience retention | treat as 2–3 chapters each with its own loop; title cards ≤ 1 s |

## Per-shot spec line (fill for every shot)

```
#07  12.4–14.6 s  (2.2 s)
VO:     "The computer said he had enough fuel."
STRESS: "enough"  -> cut lands at 13.9 s
VISUAL: real 767 fuel gauge photo (SOURCE: TSB Canada), push-in to needle, accent ring on "22,300"
MOVE:   push 100→112 %, ease in-out, focus on needle
TEXT:   "22,300 kg?" (mono, 5 words max), on at 13.9, off at 14.6
SFX:    gauge tick ×3, low sub hit at 13.9
LOOP:   L2 open ("enough?")
PURPOSE: shows the wrong number the whole story turns on
```
If the PURPOSE field can't be written in one line, the shot is cut.


---
<!-- references/05-script-writing.md -->

# 05 — Script writing

## Format

- 80–120 spoken words for 35–45 s (150–170 wpm). Count before recording.
- Sentences 4–12 words, active voice, past tense for the story, present tense for the lesson.
- Plain spoken English (or the target language); a 12-year-old must understand every sentence on first hearing.
- Numbers: one per sentence max, always with unit. Prefer the human-scale version ("as tall as a 10-storey building").

## Structure (write in this order)

1. **Payoff line first.** Write the last sentence before anything else. If it isn't great, pick another story.
2. **Hook line.** The strangest concrete moment, in medias res. It must make the payoff necessary.
3. **Turn line.** The "You see," sentence that re-frames everything.
4. Fill escalation beats in between, each one flipping a value.
5. Cut 20 %. Then read aloud with a timer.

## Hook line tests (all must pass)

- Has a concrete noun AND a concrete number/time/place.
- Contains a contradiction or impossibility (built wrong, warned but ignored, tiny cause → huge effect).
- Doesn't reveal the cause.
- Is under 12 words / 2.5 s spoken.
- Would make sense to someone who has never heard of the topic.
- Could be the first line of a conversation with a friend: "Did you know a …"

## Banned openers

"In this video…", "Have you ever wondered…", "Today we're going to…", "Hey guys", "This is the story of…", "Let me tell you…", "Did you know…" as the literal first words, any greeting, any channel name.

## Escalation verbs and connectors that keep momentum

then · but · so · until · and that's when · minutes later · nobody checked · it got worse · the problem was · here's the thing · you see

Avoid: "additionally", "furthermore", "it is important to note", "interestingly".

## Payoff line patterns

| Pattern | Example |
|---|---|
| Irony twist | "The fix made the error twice as big." |
| One-number reveal | "The whole difference was one hyphen." |
| Callback to hook | Hook: "A bridge 54 cm too high." → End: "…and they built it anyway." |
| Moral in 6 words | "The warning was in the report." |
| Present-day sting | "That same code is still running today." |
| Loop line | last words grammatically lead into the first words of the hook |

End the video on the stressed word. Cut the audio tail at ≤ 1 s.

## Fact rules

- Every number, name, date and quote has a source in the research file (`09-research-factcheck.md`).
- Contested numbers are softened ("about", "at least", "reportedly") — never rounded up for drama.
- Never invent dialogue. Real quotes only, attributed on screen.
- Deaths are stated respectfully, once, without gore.

## Variation (no template look)

Across a batch, vary at least 3 of: hook type, emotion, length, look/colour, structure (chronological / reverse / countdown / comparison / POV), narrator energy, ending pattern. Track them in the batch plan table so no two consecutive uploads share more than two.


---
<!-- references/06-visual-language.md -->

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


---
<!-- references/07-sound-design.md -->

# 07 — Sound design for Shorts

Sound is half of retention. Many viewers start muted, but the ones who unmute decide on the first transient.

## Layers (always all four)

1. **Narration** — dry, close, intelligible; −16 LUFS integrated target for the full mix; narration peaks ~ −6 dBFS.
2. **Music bed** — one cue matched to the emotion (dread / tense / wonder / drive). Ducks 8–12 dB under voice. Changes or drops at the turn.
3. **Ambience** — the place: wind on a bridge, control-room hum, underwater rumble, newsroom typewriters. Low, continuous, sells the environment.
4. **Spot effects (sync hits)** — on every cut that shows an action: impact, whoosh on camera moves, paper on document landings, keystrokes on typing, pin on board, beep on screens, creak on structures, splash on water.

## Timing rules

- 0.0 s: a transient (hit, cut-in ambience, riser tail) together with the first word. Never start from silence.
- Every 2–4 s a spot effect lands on screen action. No 6 s stretch without a sound event besides voice.
- At the turn ("You see,"): music drops out or filters for 0.5–1.5 s → silence beat → re-enter with a heavier cue.
- At the payoff word: final hit, then ≤ 1 s of tail; if looping, the tail must blend into the first frame's sound.
- Sub-bass impacts (40–60 Hz) for disasters, but keep them under the voice.

## Mix checks

- Integrated −14 to −16 LUFS, true peak ≤ −1 dBTP.
- Voice always intelligible on a phone speaker (check with a mono, 300 Hz–5 kHz band-limited listen).
- No clipping, no pumping from over-ducking, no music with vocals under narration.
- Use licensed or generated SFX/music you have rights to; no trending copyrighted songs on uploads meant for monetisation.

## Voice direction

- 150–175 words per minute for stories (measured: top story Shorts cluster here — see data), faster (180–200) for list/explainer energy, slower (130–150) for dread.
- Sentence length 4–12 words. One idea per sentence.
- Stress the concrete noun or number; cut on that word.
- Natural tone, a person telling a friend something unbelievable. Not an announcer.
- With ElevenLabs v3/v4 style models, use audio tags sparingly ([whispers] for the scary line, [sighs] for the lesson).


---
<!-- references/08-endings-loops-cta.md -->

# 08 — Endings, loops, CTA and the product bridge

## Ending

- The video ends ≤ 1 s after the payoff word. No "thanks for watching", no "subscribe for more" voice line.
- Last frame = a strong image (not black, not a logo-only frame) unless the brand card is used.
- Brand card: ≤ 1.5 s, logo + one short line, same position and design in every video so it becomes a signature, not an ad.

## Loop engineering (replays count as views on YouTube since March 2025)

1. **Visual loop**: last frame matches frame 0 in composition and colour (measure: mean absolute pixel difference of downscaled first/last frames; < 25/255 feels seamless).
2. **Audio loop**: the tail of the last sound continues naturally into the first hit; music cue length = video length.
3. **Sentence loop**: the last line flows into the first ("…and that's why" → "A bridge was built 54 cm too high.").
4. Use loops for ≤ 30 s Shorts mostly; for 40–60 s prefer a strong payoff over a forced loop.

## Comments engine

- End on a defensible judgement that invites disagreement, or ask the viewer to choose ("Would you have signed it?") in the **caption**, not in the VO.
- Pin a first comment with a source and one extra fact (people reply to extras).

## CTA (one per video, low friction)

| Goal | CTA (caption / end card only) |
|---|---|
| Follows | "Follow for one engineering disaster a day." |
| Comments | "Comment the year you think it was fixed." |
| Sends | "Send this to the engineer who always says 'it's fine'." |
| Waitlist | profile link only on Instagram; on YouTube the channel bio/About. Never a link in YouTube descriptions if the project forbids it. |

## Product bridge (story first, product second)

- At most 1 in 4 videos. The other 3 are pure story + end card.
- The bridge line is the lesson of the story phrased so that the product is the obvious next thought, never a pitch:
  - "The junior engineer who spotted it was ignored. Good hiring should hear people like that."
  - "His CV said 'software'. His real skill was noticing what nobody tested."
- Never mention price, features or "sign up now" in the VO. The end card does the rest.
- Measure: waitlist sign-ups per 1,000 views for bridge vs. non-bridge videos; keep the bridge rate only if bridge videos don't lose retention.


---
<!-- references/09-research-factcheck.md -->

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


---
<!-- references/10-qa-checklist.md -->

# 10 — QA gates and scoring rubric

A Short ships only when every gate passes. Score it; under 85/100 → fix and re-score.

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
- No black frames (except the planned beat), no freezes > 0.5 s outside planned holds (`ffmpeg -vf freezedetect,blackdetect`).
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


---
<!-- templates/batch_plan.md -->

# BATCH PLAN — <batch name> (<N> videos)

| # | Story | Emotion | Hook type | Length | Look | Structure | Ending | Bridge | Slot |
|---|---|---|---|---|---|---|---|---|---|

Variation checks:
- No two consecutive rows share hook type + look + ending.
- Emotions mixed (awe / anger / anxiety) across the batch.
- Lengths vary (some 25–30 s, most 35–45 s, a few 50–60 s).
- ≤ 1 in 4 rows has a product bridge.
- Every story score ≥ 20/25.


---
<!-- templates/short_plan.md -->

# SHORT PLAN — <NN> <working title>

## 1. Card
| Field | Value |
|---|---|
| Story | |
| Core cause (1 sentence) | |
| Emotion target | awe / anger / anxiety + surprise |
| Hook type (from 03) | |
| Structure | chronological / reverse / countdown / comparison / POV |
| Look | newsprint / sepia / cold steel / terminal / night / space / deep ocean |
| Length target | __ s (__ words at __ wpm) |
| Ending pattern | irony / one-number / callback / moral / present-day sting / loop |
| Product bridge | none / lesson line (≤ 1 in 4 videos) |
| Story score (09) | __ /25 |

## 2. Hooks (10 candidates, scored)
| # | Hook line | Type | Score /30 |
|---|---|---|---|
Winner: … Runner-up for A/B trial reel: …

## 3. Script (final, with timing)
```
[0.0] Hook line…
[2.1] …
[24.0] You see, …
[39.2] Payoff line.
```
Word count: __ · Spoken duration (timer): __ s

## 4. Beat map
| Time | Beat | Loop opens/closes | Emotion level 1–10 |
|---|---|---|---|

## 5. Shot list (one spec line per shot)
```
#01  0.0–1.6 s (1.6 s)
VO:
STRESS:
VISUAL:            (source + label / RECONSTRUCTION)
MOVE:
TEXT:
SFX:
LOOP:
PURPOSE:
```
Checks: shots __ · median __ s · longest static __ s · repeats: none · shot types used: __

## 6. Sound plan
Music cue: … (mood, BPM, where it drops) · Ambience: … · Silence beat at __ s · Final hit at __ s

## 7. Packaging
- YouTube title (≤ 60 chars):
- YouTube description (1–2 lines + hashtags, no links):
- IG caption (hook line / 2–4 lines / CTA / hashtags):
- Cover frame: time __ s + ≤ 4 words:
- Pinned comment (source + extra fact):
- Posting slot (CET / local):

## 8. Sources & credits
| Claim / asset | Source | Licence / credit line |
|---|---|---|

## 9. QA score (10-qa-checklist)
| Dimension | Score | Note |
|---|---|---|
Total: __ /100 (ship ≥ 85)


---
<!-- examples/example_gimli_glider.md -->

# Worked example — "The Gimli Glider" (40 s, awe + anxiety, hook type 1 In medias res, look: night cockpit → daylight)

Facts (TSB Canada / Wikipedia map): Air Canada 143, 23 July 1983, Boeing 767; fuel calculated in pounds instead of kilograms with a failed fuel-quantity system; both engines stopped at 41,000 ft; Captain Pearson (glider pilot) glided to the former RCAF Gimli base, then a racetrack; no serious injuries.

## Script (104 words, ~40 s)
```
[0.0] At forty-one thousand feet, both engines went silent.
[2.4] The screens went black. Sixty-nine people on board.
[5.0] The fuel gauges had said they had plenty.
[7.6] They didn't. They had less than half.
[10.2] Someone had done the maths in pounds.
[12.6] The new jet used kilograms.
[14.8] Now a 132-tonne airliner was a glider.
[17.6] The nearest runway was too far.
[19.8] But the captain flew gliders on weekends.
[22.6] You see, there was one more runway.
[25.0] An old air force base. Closed.
[27.4] What nobody on board knew: it was now a racetrack.
[30.4] And that day, it was full of families.
[33.0] He side-slipped the jet to lose height, hit the runway hard, the nose gear collapsed —
[38.0] and it stopped just before the crowd.
```

## Beat map
L1 (0 s): why did the engines stop? → closes 12.6 s. L2 (14.8 s): where can a glider land? → 25 s. L3 (27.4 s): racetrack full of families → 38 s. Turn at 22.6 s (57 %). Peak visual at 33–38 s (88–95 %).

## Shot list (excerpt)
```
#01 0.0–1.4  VO "At forty-one thousand feet"  VISUAL reconstruction: cockpit at night, two engine N1 gauges spinning down (RECONSTRUCTION)  MOVE fast push to gauges  SFX engine spool-down + master caution  PURPOSE: the impossible moment
#02 1.4–2.4  VO "both engines went silent"  VISUAL real 767 photo, engines, slow drift  SFX wind only (engine noise cut)  PURPOSE: silence = danger
#05 7.6–10.2 VO "less than half"  VISUAL fuel bar draws to 100 %, then drains to 45 % (data counter)  TEXT "22,300 kg needed / 10,100 kg on board"  SFX tick ×4, sub hit on "half"  PURPOSE: the core number
#06 10.2–12.6 VO "in pounds"  VISUAL real refuelling form (source label), push to "1.77" conversion factor, marker wipe  SFX paper + pen  PURPOSE: the cause, as evidence
#10 22.6–24.0 VO "You see,"  VISUAL 0.8 s black + map snaps in  SFX music drop, silence, single low tone  PURPOSE: the turn
#12 27.4–30.4 VO "it was now a racetrack"  VISUAL aerial of Gimli strip with drag-race cars (archive), pull-back  SFX crowd + engines rev  PURPOSE: the twist
#14 33.0–38.0 VO landing  VISUAL archive photo of the 767 nose-down on the strip, push-in; then people standing next to it  SFX tyre screech, metal scrape, biggest impact  PURPOSE: peak + scale
```

## Packaging
Title: "The Jet That Ran Out of Fuel at 41,000 Feet" · IG first line: "Both engines stopped. The only runway was a racetrack." · Pinned comment: source (TSB report) + "The jet flew again for 25 more years."


---
<!-- examples/example_millennium_bridge.md -->

# Worked example — "London's Wobbly Bridge" (28 s loop, surprise + awe, hook type 2 Impossible result, look: cold steel)

Facts: Millennium Bridge, London, opened 10 June 2000; synchronous lateral excitation from pedestrians made it sway; closed 12 June; reopened 2002 after dampers were fitted.

## Script (72 words, ~28 s)
```
[0.0] Two days after it opened, this bridge started dancing.
[2.6] Thousands of people walked across it. It swayed sideways.
[5.4] And the more it swayed, the more they swayed with it.
[8.4] You see, when a floor moves, you widen your step to keep balance.
[12.0] Thousands of steps fell into the same rhythm.
[14.8] Their feet were pushing the bridge in time.
[17.4] London closed it after two days.
[19.6] It took two years and 91 shock absorbers to fix.
[23.0] Today, thousands cross it every day.
[25.4] And it doesn't dance anymore.
```
Loop: last frame = same wide shot as frame 0 (now still) → first line "started dancing" plays over the still bridge, creating a seamless loop.

Shot plan highlights: #01 real archive of the crowded bridge with lateral wobble (stabilised + speed ramp); #04 diagram: one pedestrian's centre of mass swinging, then 1,000 dots syncing (small multiples); #07 photo of the dampers (source label); #09 pull-back scale reveal over the Thames.


---
<!-- data/analysis_summary.md -->

# Measured analysis — 76 top story Shorts, 16 channels

Method: each Short downloaded (480p), transcribed with Whisper word timestamps, scene cuts with FFmpeg `scene>0.28`, momentary loudness (EBU R128) per second, contact sheets at 2 fps, first-vs-last frame difference (loop). Script: `tools/analyze_shorts.py`. Selection: the 5 most-viewed Shorts of each channel.

## 1. Global distributions

| Metric | Median | P25 | P75 | Min | Max |
|---|---|---|---|---|---|
| Duration (s) | 58.45 | 37.3 | 98.0 | 6.9 | 179.4 |
| Cuts per video | 8.0 | 3 | 23 | 0 | 104 |
| Median shot (s) | 4.99 | 2.4 | 8.3 | 0.13 | 40.87 |
| First cut (s) | 4.21 | 2.04 | 6.64 | 0.03 | 32.21 |
| Words per minute | 159.5 | 128 | 186 | 0 | 275 |
| First word (s) | 0.0 | 0.0 | 0.0 | 0.0 | 12.06 |
| Integrated loudness (LUFS) | -15.7 | -19.3 | -12.7 | -25.8 | -8.2 |
| First/last frame diff (0–255) | 53.5 | 41.5 | 68.3 | 4.1 | 153.0 |
| Cuts per second | 0.13 | 0.07 | 0.29 | 0.0 | 1.74 |

## 2. Per channel (medians)

| Channel | n | Views med | Dur | Cuts | Med shot | First word | WPM | LUFS |
|---|---|---|---|---|---|---|---|---|
| MarkRober | 5 | 638,000,000 | 44.5 | 22 | 1.83 | 0.0 | 111 | -12.5 |
| NileRed | 5 | 127,000,000 | 55.5 | 6 | 6.77 | 0.0 | 128 | -17.8 |
| veritasium | 5 | 53,000,000 | 58.1 | 18 | 2.4 | 0.0 | 141 | -18.0 |
| zackdfilms | 5 | 22,000,000 | 35.3 | 0 | 35.19 | 0.0 | 177 | -10.3 |
| RealEngineering | 5 | 15,000,000 | 58.0 | 10 | 3.92 | 0.0 | 159 | -20.1 |
| Kurzgesagt | 5 | 11,000,000 | 57.4 | 7 | 6.5 | 0.0 | 197 | -14.2 |
| MrBallen | 5 | 4,300,000 | 167.7 | 31 | 4.63 | 0.0 | 243 | -11.6 |
| DailyDoseOfInternet | 5 | 3,500,000 | 15.8 | 1 | 8.23 | 0.0 | 22 | -19.3 |
| TheInfographicsShow | 1 | 3,000,000 | 29.0 | 3 | 6.06 | 0.92 | 159 | -13.7 |
| HistoryLegends | 5 | 2,700,000 | 54.1 | 4 | 10.91 | 0.0 | 157 | -11.3 |
| PracticalEngineeringChannel | 5 | 971,000 | 59.6 | 3 | 7.46 | 0.0 | 177 | -18.9 |
| simplehistory | 5 | 841,000 | 141.3 | 11 | 9.85 | 0.0 | 159 | -14.1 |
| bigthink | 5 | 820,000 | 178.9 | 51 | 2.54 | 0.0 | 150 | -20.9 |
| TheB1M | 5 | 671,000 | 65.0 | 21 | 2.55 | 0.0 | 174 | -20.1 |
| EmergencyAwesome | 5 | 182,000 | 59.7 | 41 | 0.2 | 0.0 | 181 | -19.0 |
| Mustard | 5 | 12,000 | 22.7 | 5 | 1.84 | 0.0 | 40 | -13.7 |

## 3. Full-runtime profile (normalised to 10 % bins of each video)

Cut rate = cuts per second inside the bin; word rate = words per second; loudness = mean momentary LUFS relative to that video's mean.

| Runtime bin | Cut rate | Word rate | Loudness Δ dB | Silence share (>1 s gaps) |
|---|---|---|---|---|
| 0–10 % | 0.11 | 3.11 | 1.4 | 22 % |
| 10–20 % | 0.17 | 2.81 | 0.7 | 20 % |
| 20–30 % | 0.12 | 2.8 | 0.7 | 13 % |
| 30–40 % | 0.17 | 2.92 | 0.2 | 17 % |
| 40–50 % | 0.11 | 2.72 | 0.7 | 12 % |
| 50–60 % | 0.14 | 2.9 | 1.2 | 11 % |
| 60–70 % | 0.11 | 2.77 | 0.8 | 12 % |
| 70–80 % | 0.11 | 2.6 | -0.3 | 14 % |
| 80–90 % | 0.09 | 2.73 | -0.3 | 13 % |
| 90–100 % | 0.09 | 2.21 | -1.3 | 5 % |

## 4. First 5 seconds, second by second (share of videos)

| Second | has a cut | has speech |
|---|---|---|
| 0–1 s | 8 % | 97 % |
| 1–2 s | 17 % | 92 % |
| 2–3 s | 16 % | 84 % |
| 3–4 s | 17 % | 88 % |
| 4–5 s | 22 % | 82 % |

## 5. Where the turn happens

Position (as % of runtime) of the first occurrence after 25 % of runtime of each turn marker.

| Marker | Videos using it | Median position |
|---|---|---|
| but | 47 | 40 % |
| you see | 1 | 71 % |
| turns out | 1 | 93 % |
| however | 4 | 53 % |
| instead | 1 | 31 % |
| actually | 21 | 45 % |
| until | 6 | 71 % |
| that's when | 0 |  % |
| so | 36 | 48 % |
| then | 29 | 62 % |

## 6. Spoken-hook features (first 3 s)

| Feature | Share |
|---|---|
| statement | 29 % |
| you | 24 % |
| number | 22 % |
| question | 21 % |
| first person | 18 % |
| superlative | 16 % |
| this/demonstrative | 9 % |

## 7. Loops

12 of 76 videos end on a frame within 25/255 of their first frame (visual loop).

## 8. What the numbers mean (rules derived for the skill)

1. **Speech starts at 0.0 s in the median video and in 97 % of videos within the first second.** A silent or music-only opening is an outlier among top Shorts → rule: first word ≤ 0.3 s.
2. **Word rate is highest in the first 10 % (3.1 words/s ≈ 187 wpm) and lowest in the last 10 % (2.2 words/s).** Top Shorts open fast and land slower: the payoff gets air. Plan the hook at ~180 wpm and the payoff line slower, with a ≤ 1 s tail.
3. **Loudness is +1.4 dB above the video's mean in the first 10 % and −1.3 dB in the last 10 %.** Start with a hit; don't end on the loudest moment unless it is the payoff impact.
4. **The first "but" after the set-up arrives at a median 40 % of runtime; "then" at 62 %; "until" at 71 %.** Successful Shorts flip direction early and again later — at least two value changes (≈ 40 % and ≈ 65–70 %), not one twist at the end.
5. **Hard cuts are fewer than you'd think (median 8 per video, first cut at 4.2 s).** Zack D. Films has a median of 0 detected cuts and a 35 s single "shot": the change comes from continuous camera moves through a 3D world, not from cutting. MarkRober and Veritasium cut every ~2 s. Rule: something must *change* every 1.5–3 s — a cut, a camera move to a new subject, a new object entering, or an environment change. Cuts are only one way to do it.
6. **Duration clusters at 37–98 s (median 58 s).** Story channels: Zack 35 s, Mark Rober 44 s, Veritasium/Real Engineering/Kurzgesagt ~57 s. For a new channel, 35–45 s is the safest; go to 55–60 s only with a two-twist story.
7. **WPM median 160 (P25 128, P75 186).** Story narration: 150–175. Demo/talking-head channels are slower because the action carries the story.
8. **Only 16 % of the top videos are true visual loops.** Loops help but aren't required; a strong payoff beats a forced loop.
9. **Spoken hooks: 29 % plain statement, 24 % address "you", 22 % contain a number, 21 % are questions, 18 % first person, 16 % superlatives.** The most-viewed hooks combine two of these (statement + number, you + superlative).
10. **Visual hooks (contact sheets):** frame 0 is almost always the subject already in action (a person mid-experiment, the object already moving, the strange object in close-up) — never a title, logo or establishing landscape. Text on frame 0 appears in < 1/3 of videos and is at most a short label.

Caveat: scene-cut detection at threshold 0.28 under-counts soft transitions and continuous camera moves; treat cut counts as a lower bound.
