# viral-shorts-skill v2: all files in one


<!-- ===== SKILL.md ===== -->

---
name: viral-story-shorts
description: End-to-end playbook for planning, writing, designing and QA-ing high-retention story Shorts / Reels (engineering disasters, science, history) for YouTube Shorts and Instagram Reels. Use when asked to create, script, storyboard, edit, review or score vertical short-form videos, hooks, captions or posting plans.
---

# Viral Story Shorts — master skill

You are a short-form director, writer, editor and sound designer in one. Your output is a Short that a viewer cannot swipe away from, that is factually correct, and that looks like a premium documentary — never like AI slop or a template.

This skill is built on measured data (~300 Shorts from 19 channels, each channel's hits, median videos and misses analysed second by second and compared within the channel — `data/`), frame-level study of Zack D. Films and Fern, peer-reviewed psychology (Loewenstein, Berger & Milkman, Heath, Kahneman, McKee, Murch), platform guidance (YouTube, Mosseri), and lessons from producing 60 Shorts and a long-form documentary for FirstEngineer.

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
| `references/11-story-discovery.md` | finding stories with proven demand; 40-point viral-potential score |
| `references/12-critic-agent.md` | independent critic that judges the rendered video |
| `references/13-camera-direction.md` | six-layer shot spec, sealed camera moves, move by feeling, 2.5D archive parallax, time/space, finishing |
| `tools/find_archive.py` | automatic real-archive image finder with licence + credits |
| `tools/critic_pack.py` | evidence pack from a rendered mp4 for the critic |
| `tools/scout.py`, `tools/analyze_shorts.py`, `tools/aggregate.py` | reproduce the dataset |
| `data/analysis_summary.md` | the numbers: durations, cut rates, WPM, first-word timing, hooks |
| `templates/` | the exact deliverable formats |
| `examples/` | two fully worked Shorts |

## Evidence levels

Every rule in this skill is one of: **[M] measured** in `data/` (with the tier comparison), **[R] research** (published psychology/platform sources), or **[E] editorial** (house style from producing 60+ Shorts and documentaries; sensible but not proven to cause virality). Don't present [E] rules as measured success formulas.

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

1. **Find and pick the story** with the 40-point viral-potential score (`11`) and the 25-point story score (`09`). Reject < 28/40 or < 20/25.
2. **Research file** with sources for every fact (`09`).
3. **Write the payoff line, then the hook, then the turn** (`05`). Generate 10 hooks from `03`, score each with the hook score in `03`, keep the best; keep the runner-up for an A/B trial reel.
4. **Full script** 80–120 words; read aloud with a timer; fit 35–45 s.
5. **Beat map** on the time grid (`04`): loops L1–L4, emotion, turn, peak.
6. **Shot list**: one spec line per shot (`04` format) using the shot vocabulary (`06`); rotate types; check for repeats.
7. **Sound plan** per shot (`07`).
7a. **Direct every shot** in six layers with one sealed move (`13`).
7b. **Find real visuals** with `tools/find_archive.py` (licence + credit per file), then review every file by eye.
8. **Title, caption, hashtags, cover frame, pinned comment** (`01`, `08`).
9. **Score with the rubric** (`10`). < 85 → revise the weakest dimension and re-score.
9b. **After render: independent critic** (`12`) on the `critic_pack.py` output. The producer's own score never ships a video.
10. **Deliver** using `templates/short_plan.md` (one file per video) and `templates/batch_plan.md` (for a batch).
11. After publishing: log the metrics (`01`) and update `data/` and the hook library every 10 videos.

## When asked for N videos

Produce a batch plan table first (story, emotion, hook type, length, look, structure, ending pattern) and make sure the variation rule holds, then produce N complete `short_plan.md` deliverables. Never shorten later videos in the batch: video 10 gets the same depth as video 1.

## Code production
To produce the video with code instead of hand editing, follow `references/14-code-production.md`. It maps every shot type to a renderable function and defines the per-video build.py contract, the self-checks and the encode settings.


<!-- ===== references\01-platforms.md ===== -->

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

## Reading the retention graph [R/E]

(Adapted from youtube-agent-skill `retention.py`, MIT.) Export: Studio → video → Analytics → Engagement → audience-retention chart → download. Then `python tools/third_party/youtube-agent-skill/retention.py retention.csv --duration 41 --transcript words.srt`.

Three different problems — fix only the biggest:
- **Hook leak** — loss in the opening. For a Short, read it as *viewed vs swiped* plus the drop in the first 3 s. Always a script/frame-0 fix, never the edit.
- **Cliffs** — single steep drops at a moment (topic change without signpost, a slow setup, the product bridge, a static shot). With the transcript you see the exact words spoken at the cliff; that is the actionable part.
- **Slide** — steady bleed across the middle. That is pacing: cut, don't rewrite.

If the hook is healthy and the slide is flat, the video is fine and the problem is packaging (title, first frame as thumbnail, topic).

## Title lint [R/E]

`python tools/third_party/youtube-agent-skill/title.py --title "..."` — desktop truncates around 60 characters and the mobile feed around 40, so the subject must sit in the first 40. Not more than two ALL-CAPS words. A number, a name or a date beats any adjective. The on-screen text in frame 0 must not repeat the title word for word: different words, same promise. Write ten titles, keep two.

## Search query test (long-form and evergreen Shorts) [E]

Before publishing, write the three queries a real person would type to find this story ("gimli glider", "plane ran out of fuel"). The title and the first two description lines must contain those words. The first two description lines are the only ones read (above "...more").

## Audit = one fix [E]

When reviewing the channel: read the last ten titles as a set (same shape = a format problem), look at first frames at feed size, score the hooks of the three latest, check upload consistency, read retention. Hand back ONE fix for this week, three specific things that already work (so they are not broken) and what NOT to change yet.


## Third-party "Shorts statistics": check them before you trust them [M]

Guides on the internet (including OpenMontage's short-form guide, which cites marketing blogs) repeat numbers like "180–200 WPM", "no static hold over 3 s", "15–30 s gets the most completion" or "3-second retention above 85 % gives 2.8× views". Most of them can't be checked. Test each one against `data/analysis_summary.md` before you use it:
- **Narration speed**: the v2 dataset shows ~177–179 WPM in every tier (Whisper base.en), so speed doesn't separate hits from misses. 160–185 WPM is the normal range; clarity beats speed.
- **Length**: 45–60 s is the most common band among hits in our dataset, 20–35 s is over-represented among misses, and 35–45 s shows no advantage (section 3 and 5). Choose the length the story needs, and treat "15–30 s" as a hypothesis to A/B test on your own channel.
- **Visual change every 1–3 s**: this is plausible as *visual change* (moves, labels, rack focus), which is not the same as a *cut*. The measured median cut interval is ~5 s, and the detector misses soft transitions.
- Useful and verifiable: platform UI safe zones. Keep text inside a centred ~900×1400 px area of 1080×1920. The bottom ~300 px (captions, buttons) and right ~100 px are covered on every platform. Instagram also covers ~210 px at the top. Upload H.264 at 8–15 Mbps; below ~5 Mbps platforms may re-compress visibly.

## Sample first [E]

Before you produce a batch, take ONE Short all the way to final: render, critic, fix. Lock the look, the sound bed and the caption style on that one. Building ten Shorts on an unproven look multiplies one mistake by ten.


<!-- ===== references\02-psychology.md ===== -->

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


<!-- ===== references\03-hooks.md ===== -->

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

See `data/hooks_library.md` — first 3 seconds (spoken words), first-word time, first-cut time and view counts and TOP/MID/LOW tier of 302 Shorts from 19 channels. Patterns extracted from it are summarised in `data/analysis_summary.md`.

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

## Weakest-link hook scoring [R/E]

(Adapted from Jakeschincariol/youtube-agent-skill `hookscore.py`, MIT.) Score each hook option on five properties 0–100 — **specificity** (number, name, date; no vague adjectives), **stakes** (what is lost: lives, money, a city), **curiosity gap** (a question it raises and does not answer; "because…" in the hook closes the gap), **concreteness of the first visual** (can frame 0 *show* it?), **brevity** (story Shorts: 6–14 spoken words before the first comma-pause). Verdict = 0.6 × mean + 0.4 × weakest. A hook with four strong properties and one dead one leaks at the dead one; averaging hides that.

Run `python tools/hookscore_story.py hooks.txt` on the ten options, keep the top two, test both against frame 0. **Honesty note:** the original tool, tested on 74 real hooks, separated deliberately bad hooks from real ones but barely separated a creator's hits from their own misses. `data/analysis_summary.md` reports how our version does on TOP vs LOW tiers. A low score is a reason to rewrite; a high score is not a promise.

## Every hook type has a failure mode

| Hook type | Fails when |
|---|---|
| Number / statistic | the number is vague, unverifiable, or not shown on screen |
| Impossible result | the proof does not start within ~5 s of a Short |
| Wrong belief / mistake | the viewer cannot check the belief in one second |
| Contrarian flip | no evidence follows immediately → reads as contrarian for its own sake |
| "This is…" receipt | there is no real artefact on screen (a described receipt is not a receipt) |
| Warning / stakes | the cost is small — then the hook is a lie and trust is spent |
| Question | it is the producer's question, not the viewer's |
| Superlative ("the deadliest") | it does not name what it beat |
| Clock / countdown | the clock is not true to the runtime |
| Insider / hidden | it claims access the channel does not have |

## Rules for cutting a Short out of a long video [E]

A Short is not the best moment of a long video; it is a moment that **survives without the video around it**. A span qualifies only if: (1) it opens on a complete thought, (2) it contains a turn, (3) it ends on a line, not a trail-off. Then write a NEW first line (the long-form line assumes context), on-screen text for the first 2 s in *different words* from the spoken line, and a loop point (the last line sets up the first). Note what a 9:16 crop of the 16:9 frame loses.


<!-- ===== references\04-second-by-second.md ===== -->

# 04 — Second-by-second blueprint

Plan every Short on a time grid before writing visuals. Times below are for a **35–45 s** story Short. This length is an *editorial default* for a new channel (short enough to finish, long enough for two value flips), not a measured optimum — in the v2 data, 45–60 s is the most common band among hits, 20–35 s is over-represented among misses, and 35–45 s shows no edge (`data/analysis_summary.md` sections 3 and 5). Measured hygiene: first cut before ~4 s. Scale proportionally for 25 s or 60 s.

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


<!-- ===== references\05-script-writing.md ===== -->

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


<!-- ===== references\06-visual-language.md ===== -->

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


<!-- ===== references\07-sound-design.md ===== -->

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


<!-- ===== references\08-endings-loops-cta.md ===== -->

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


<!-- ===== references\09-research-factcheck.md ===== -->

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


<!-- ===== references\10-qa-checklist.md ===== -->

# 10 — QA gates and scoring rubric

A Short ships only when every gate passes. Pre-render, the producer scores the plan (< 85 → fix). After render, the **independent critic** (`12-critic-agent.md`) scores the actual video; only the critic's SHIP verdict ships it.

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


<!-- ===== references\11-story-discovery.md ===== -->

# 11 — Story discovery and viral-potential scoring

Pick stories by evidence, not taste. Run this as an independent step before any writing.

## 1. Sources to mine (rotate)

| Source | What to pull |
|---|---|
| Investigation reports (NTSB, TSB, AAIB, BEA, CSB, NASA, Coast Guard, national rail/structural boards) | findings with a single concrete cause |
| Wikipedia lists: "List of structural failures and collapses", "List of software bugs", "Engineering disasters", "Category:Industrial accidents", "List of aviation accidents by cause" | candidate pool |
| Engineering case studies (ASCE, IEEE Spectrum "Risk Factor", Hackaday failures, Ars Technica) | modern and tech-era stories |
| Reddit r/engineering, r/CatastrophicFailure, r/EngineeringPorn top of year | what people already share |
| Anniversaries in the next 30 days | timely angle |
| Comments on your own top videos ("do X next") | demand signal |

## 2. Demand check (outside evidence that people want the story)

For each candidate, record:
- **YouTube search**: views of the top 5 Shorts on the topic and their age (views/day). High views/day for *other* creators on the same story = proven demand; if > 5 Shorts already exist with > 1 M views, you need a new angle.
- **Long-form proof**: a long video on the topic with > 1 M views but few Shorts = gap.
- **Google Trends / Wikipedia pageviews** (pageviews API) for the last 90 days — rising interest is a bonus.
- **Novelty**: has *your* audience seen it? (search your own uploads and your top 10 competitors).

## 3. Viral potential score (0–40) — use together with the 25-point story score in `09`

| Factor | 0 | 5 |
|---|---|---|
| Proven demand (views/day of existing coverage) | none | many viral pieces |
| Gap (few Shorts, or a new angle) | saturated | untouched angle |
| Visual availability (real, licensed material) | none | strong photos/footage/documents |
| One-sentence cause | complex | one word / number |
| Emotion strength | flat | awe / anger / anxiety obvious |
| Social currency ("send this to…") | none | obvious person to send to |
| Timeliness | none | anniversary / in the news |
| Audience fit (engineers, students, tech) | none | direct |

Rule: produce only stories ≥ 28/40 AND ≥ 20/25.

## 4. Learn from your own results

After each batch, tag each video with its hook type, emotion, length, structure and story category, and compare *within your own channel* (top third vs. bottom third by viewed-vs-swiped and average % viewed). Update the weights above with what actually separated them.

## Outlier multiple, not raw views [M/R]

Raw views rank channel size, not ideas. Score every candidate reference video as **views ÷ its own channel's median** (≥ 4 videos per channel, preferably ≥ 30, newest ~10 excluded because their views are not settled). A 400 k Short on a channel whose median is 30 k (13×) is worth studying; a 4 M Short on a channel whose median is 3 M (1.3×) is a normal day. `tools/third_party/youtube-agent-skill/swipe.py collected.json --min 2.0` ranks a `yt-dlp --flat-playlist -J` export this way. When you present outliers: the top five with multiples, the hook formula each used (a judgement about the title, not a proven cause), the ONE structural thing they share, and which one this channel can make this week with real archive.

Small/new channels matter more than giants here: a 10× outlier on a 5 k-subscriber channel shows the *topic and packaging* carried it, not the audience.


<!-- ===== references\12-critic-agent.md ===== -->

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


<!-- ===== references\13-camera-direction.md ===== -->

# 13 — Camera direction and shot specification

Adapted and extended from AustinZ21/cinematic-skills (`shot-director`, `still-to-film`, MIT), rewritten for vertical story Shorts built from real archive + code-drawn animation + Blender. Evidence level: **[E]** craft rules from film practice, not measured on Shorts.

> An adjective makes the model (or you) guess. A camera instruction says what to do. "Make it cinematic" is not a note. "Start on the gauge, push in at steady speed, stop when the needle hits zero, background never moves" is.

## 1. Three questions before any shot

1. **What do we look at?** The one piece of information that must land first.
2. **Where do we stand?** Shot size, height, angle.
3. **How do we approach?** Stay still, turn in place, travel, or shift focus.

Then four checks: Why does the subject move? Why does the camera move? What does the move reveal? **Would it be better if the camera did not move at all?** A move with a story job pulls the viewer along; a move added "to look expensive" becomes the endless forward float that makes video look AI-made.

## 2. Every shot is written in six layers

| Layer | Answers | Words |
|---|---|---|
| 1 Subject + action (blocking) | who/what does what, when | the needle drops, the beam buckles, the crowd steps |
| 2 Shot size | how much fits | extreme wide · wide · medium · close-up · extreme close-up (insert) |
| 3 Angle + height | from where | eye level · low · high · overhead · ground level |
| 4 Lens + focus | how space looks | wide lens · long lens · shallow DOF · deep focus · rack focus |
| 5 Camera move | how it travels | one main move (§3) |
| 6 Pace + limits | how it starts and ends | speed, ease, start frame → end frame, what stays still |

Add to the shot list (`templates/short_plan.md`): **Start → end frame**, **Holds** (what must not change, scale reference, screen direction), **Cut cue** (the word, beat or sound the cut lands on).

## 3. Move rules

- **One main move per shot.** Two at most, joined by a trigger ("when the counter hits 0, the push stops and focus racks to the crack"). Everything else is a cut.
- **Every move is sealed:** start, end, speed, what does not change. "Pan right" alone pans until the clip ends.
- **Never mix zoom and dolly by accident.** Zoom = optical, everything scales evenly (flat). Dolly/push = camera travels, near things grow faster than far (parallax). Opposite directions together = dolly zoom (shock), only deliberately.
- **Static first when unsure.** If composition and action don't work still, no move saves them.
- **Not every shot moves.** Constant motion removes the reference point; a held static shot makes the next move hit harder. Budget per Short: ≥ 1 held near-static beat (usually the turn or right before the payoff).
- **Camera moves only when the subject or the information moves, and exactly as much** (Fincher rule).
- **Handheld is a controlled strength**, not random shake: "slight footstep bob" by default, more only on impact.
- **Ease:** smoothstep `u*u*(3-2u)` for in/out; constant log-zoom rate feels like a steady dolly; accelerating dive `k*u^2.3`. Speed must stay continuous across cuts that are meant to flow.
- **Motion blur on fast moves** (~6 sub-frames over ~1 frame of shutter) or the push strobes.

### Look-alike pairs (write the right one)

Pan (turn head) vs **truck** (step sideways: near things race past) · tilt (look up) vs **pedestal** (rise, lens level) · **zoom** vs **dolly** · handheld (breath) vs gimbal (smooth inertia) · crane (arc: height + distance + angle together) vs pedestal (straight up) · POV (whose eyes) vs FPV (flight route) · barrel roll (keeps rotating) vs Dutch angle (tilts once, holds) · long take (no cut) vs slow motion (playback speed).

## 4. Choose the move by the feeling or the job

| Feeling / job in a disaster Short | First choice | Watch out |
|---|---|---|
| Objective record, evidence, a document | static or very slow push | text must be readable for ≥ 1.2 s at rest |
| Realisation ("they knew") | slow push in, stop on the key line | stop exactly on the stressed word |
| Danger off-screen / still to come | slow pan or tilt toward it | write what is hidden first, where it stops |
| A detail suddenly matters (crack, bolt, gauge) | rack focus or fast push | settle instantly |
| Shock / sudden failure | crash zoom, whip pan, impact shake | one per Short; clear start/end |
| Scale, size, power (bridge, dam, ship) | tilt up / pedestal up / pull back | must contain a scale ruler (person, car, bus) |
| Loneliness, aftermath, loss | slow pull out | end frame shows the empty space around |
| Mechanism in 3D (how it failed) | small orbit (≤ 90°) around the part | one axis; label stays readable |
| Journey / timeline progress | truck along a timeline or a map | one screen direction for the whole sequence |
| Falling / losing control | barrel roll (small = unease, large = fall) | once |
| Panic closing in | dolly zoom | centred subject, deep background (corridor, girders) |

Fastest path: performance/evidence strong on its own → **static**; something changes inside a person → **push in**; the surroundings change the meaning → **pull out**; new info is off-frame → **pan/tilt**; new info is in frame at another depth → **rack focus**; crossing space → **truck/track**; need 3D form → **orbit**; just bigger → **zoom**.

## 5. Real archive photos with real camera moves (2.5D depth parallax)

A real photo that is only zoomed reads as a slideshow (Ken Burns). Give it depth instead:
1. Make a depth map of the photo (`tools/third_party/cinematic-skills/prep_plate.py`, Depth Anything V2). **Do not use its AI super-resolution step on archive evidence** — it invents detail; upscale with Lanczos. The depth map changes only geometry, not content; still label the shot `ARCHIVE · <source>`.
2. Render with `depthshot.js` (or the same maths in Blender: photo on a displaced plane). Push = zoom `lz` + depth magnification `pz` (the `pz` is what sells "the camera moved"). Truck/pedestal = `px/py` ≤ ±0.05. Pan/tilt beyond ~10 % of the frame or orbit beyond a few degrees: impossible from one still — cut instead.
3. Failure modes: near edges tear into "melted glass" (reduce px/pz, dilate depth); thin flat things (signs, glass, water from above, documents) get false relief → `pz: 0`; cables crossing depth edges kink; plate borders show at move extremes → check first/last frame.
4. **Something moves inside every frame**, not only the camera: dust/particles in light, water, smoke, a blinking indicator, a counter, a highlight wiping a line.

Decision: depth shot if the move stays within the picture (push/pull/small truck). Blender if something must enter, turn, or be seen from another side. Code-drawn 2D if the shot is a diagram, number or map.

## 6. Time and space (sequence level)

- **Scale needs a ruler.** Every wide shot of something huge has a known-size object in it.
- **Geography before action.** One layout shot (map, plan, cutaway) before the failure, so the viewer knows where the threat and the safety are.
- **Hold the line.** A moving thing keeps one screen direction per sequence (e.g. the plane always flies toward frame right until it falls).
- **Stage in depth.** Foreground, subject and background layers let one moving shot replace three cuts.
- **Shrink shot length toward the climax**, then **hold one beat longer than comfortable before the reveal**. Speed is only felt against stillness.
- **One near-silent held moment** before the biggest beat (the turn-point silence in `07-sound-design.md`).
- **Match cuts** jump time or place by shape, motion or sound (rivet to bolt, ripple to sound wave, crack in the model to crack in the archive photo).
- **Let sound do the cutting:** cut on a sound, bridge into the next scene with sound, drop to silence before impact.
- **Moves in time:** slow motion at most once per Short; speed ramp for impact; time-lapse to compress years; reverse to show how it should have been; freeze on the frame of failure while the camera keeps moving.
- **Light has a source** the viewer could point to (window, screen, sun, fire). One strong source and deep shadow beats "cinematic lighting".
- **Colour carries point of view:** one grade for the record/evidence (neutral, slightly cool), another for reconstruction (warmer, grain), used consistently.
- **Withhold, then reveal:** start on the detail before the context, or the reaction before the cause.
- **Every shot changes what the viewer knows or feels.** If not, it is decoration: cut it.


<!-- ===== references\14-code-production.md ===== -->

# 14 — Code production: turn every planned visual into code that renders

Goal: an AI model (or a person) turns a `short_plan.md` into **runnable code** that outputs the finished 1080×1920 MP4, with no GUI work. Every shot type in this skill (code-drawn diagram, archive evidence, 2.5D photo parallax, Blender reconstruction, kinetic type, captions, sound) maps to code below. If a shot can't be expressed this way, redesign the shot, don't fake it.

## 1. Environment contract (state it at the top of build.py)
- Python 3.11+, Pillow ≥ 10, numpy, FFmpeg ≥ 6 on PATH. Optional: Blender 4.2+ run headless (`blender -b -P shot.py -- args`), or any sandbox that has Python + FFmpeg.
- If the sandbox has no Blender, render reconstructions with numpy/Pillow (orthographic or simple perspective projection of a mesh you define in code, flat shading with one key light, a fill light and fog), or a pre-rendered PNG sequence. Never substitute AI images.
- Fonts: IBM Plex Sans and IBM Plex Mono (OFL). Bundle the TTFs in `fonts/` or download them from github.com/IBM/plex at build time. Fall back to DejaVu only for previews.
- Deterministic: fixed seeds; no network access during render except a declared asset fetch step.

## 2. Folder layout per video
```
NN_slug/
  plan.md          # from templates/short_plan.md
  vo.txt           # narration text exactly as spoken
  vo.wav           # TTS or recorded narration (optional at first; see 5)
  words.json       # [{"w":"word","s":0.00,"e":0.31}, ...]  (Whisper/Vosk alignment)
  assets/          # archive files + credits.csv (tools/find_archive.py)
  build.py         # renders frames, composes, mixes, encodes
  blender/shot_XX.py  # optional bpy scenes, each renders a PNG sequence
  out/NN_slug.mp4
```

## 3. Timeline as data
`build.py` holds the shot list as a Python list. Every row comes straight from the plan:
```python
SHOTS = [
  # id, start, end, kind, params (six layers: subject, framing, move, light, text, sound)
  ("s01", 0.00, 1.20, "archive_push", dict(src="assets/a01.jpg", a=(0.50,0.45,1.00), b=(0.52,0.42,1.12),
       label="NBS BSS 143, Fig. 5.7", ease="inout", hold_end=0.25)),
  ("s02", 1.20, 3.40, "diagram", dict(fn="draw_rod_detail", reveal=[(1.4,"rod"),(2.1,"nut"),(2.8,"load")])),
  ("s03", 3.40, 6.00, "blender", dict(seq="renders/s03_%04d.png", label="RECONSTRUCTION: FIRSTENGINEER")),
]
```
Bind start and end times to `words.json` ("cut on the word 'stamp'"): `t = word_time("stamp")`. Don't hard-code times once the narration exists.

## 4. Shot kinds (each is a function `render(kind, t_local, dur, p) -> PIL.Image 1080×1920`)
- **archive_push / archive_pan**: crop window interpolated from `a` to `b` (cx, cy, zoom) with ease-in-out, ending in a hold. Lanczos resample, never AI upscaling. Grain ≤ 3 %. The source label (mono, 26–30 px) stays inside the safe area for the whole shot.
- **parallax_2_5d**: split the photo into 2–3 layers by hand-drawn polygon masks (defined in code). Move the layers at different speeds (foreground 1.0, mid 0.6, back 0.3); max travel 4 % of the width. Inpaint behind the foreground with a blur of the surrounding area, not with generated content.
- **document_reveal**: render the page on a desk plane (perspective warp with Pillow `Image.transform(PERSPECTIVE)`). The camera eases to the key line, a highlighter draws under it left to right at 40–60 chars/s, and the page is held for 0.4 s.
- **diagram**: vector drawing in Pillow at 2× size, then downscaled (antialiasing). Parts appear on word cues. Lines draw on with stroke length interpolation. Colours from one palette (≤ 4 + neutrals). Arrows only point at something the narration names.
- **graph**: an axis appears first, the line draws over 0.8–1.5 s, the key value pops with a counter (ease-out). The axis label always shows units and source.
- **timeline / map**: a 2D camera (translate + scale matrix) moving over a large canvas that you draw once. Markers appear on cues. A scale bar and a north arrow on maps.
- **blender**: `blender/shot_XX.py` builds the scene with bpy only (primitives, modifiers, procedural materials, no add-ons), keyframes one sealed camera move (13-camera-direction), Eevee at 1080×1920, 30 fps, and writes PNGs. 2D labels are added in `build.py`, not in Blender.
- **kinetic_type**: ≤ 5 words, IBM Plex Sans 600–700. Words enter on their spoken time (words.json) with a 6–10 frame ease. No bouncing, no rainbow, no emoji.
- **held_frame**: a deliberate still of 0.6–1.2 s before the payoff, with a slow push of ≤ 2 %. Silence or a single sustained tone.

## 5. Captions, narration, sound (all code)
- Captions: build from words.json in chunks of 1–4 words, centred at y≈1280–1400, the current word in the accent colour, a 3 px dark stroke, inside the 900×1400 safe area. Never put them over a source label.
- Narration: if `vo.wav` is missing, the build writes `vo.txt` and makes a **timing-only preview**: word times estimated at 165 WPM, plus silence. Final renders need real narration and alignment.
- SFX synthesised with numpy (no licences needed): paper slide = band-passed noise with a 120 ms envelope; stamp = a 60 Hz sine with a noise click and 200 ms decay; impact = a low sine sweep 80→35 Hz plus noise and 0.6 s decay; riser = noise with a rising band-pass over 1.5–3 s; tick = a 2 kHz 8 ms click; underwater = low-passed brown noise. Place each SFX on its shot cue.
- Music bed: a slow pad from detuned sines or saws (low-passed, 2–4 chords), or a licensed track listed in credits. Duck it under the voice by 8–10 dB (sidechain from the VO envelope).
- Mix with FFmpeg: VO −16 LUFS short-term, music ≈ −30 LUFS under the VO, SFX peaks ≤ −6 dBFS. Final `loudnorm` two-pass to I = −14 ±1, TP ≤ −1.0, LRA ≤ 9.

## 6. Encode
Pipe frames to FFmpeg rather than writing thousands of PNGs: `ffmpeg -f rawvideo -pix_fmt rgb24 -s 1080x1920 -r 30 -i - -i mix.wav -c:v libx264 -preset slow -crf 17 -pix_fmt yuv420p -profile:v high -c:a aac -b:a 192k -movflags +faststart out.mp4`. Check that the frame count equals duration × 30.

## 7. Self-checks that build.py must run
- `--preview`: renders at 540×960, every 2nd frame, plus `contact_2fps.jpg` (tools/critic_pack.py).
- Asserts: no shot without a purpose field; no asset used twice; every archive shot has a label; nothing outside the safe area; ≥ 1 visual change every 2.5 s (a move, a reveal or a cut); the first cut before 4 s [M]; LUFS and true peak within spec; no black or frozen frames over 1.5 s unless the shot is a planned held frame.
- Then run `tools/critic_pack.py out.mp4` and an independent critic (12-critic-agent). FIX at most twice.

## 8. What the model must deliver per video
`plan.md`, `vo.txt`, `build.py` (complete, runnable, no placeholders except the narration audio), `blender/*.py` if used, an asset list with URLs and licences (or the `find_archive.py` query file), and the expected runtime. If the model can run code, it renders `--preview` first, inspects the contact sheet itself, fixes it, then renders the final.


<!-- ===== templates\batch_plan.md ===== -->

# BATCH PLAN — <batch name> (<N> videos)

| # | Story | Emotion | Hook type | Length | Look | Structure | Ending | Bridge | Slot |
|---|---|---|---|---|---|---|---|---|---|

Variation checks:
- No two consecutive rows share hook type + look + ending.
- Emotions mixed (awe / anger / anxiety) across the batch.
- Lengths vary (some 25–30 s, most 35–45 s, a few 50–60 s).
- ≤ 1 in 4 rows has a product bridge.
- Every story score ≥ 20/25.


<!-- ===== templates\short_plan.md ===== -->

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


<!-- ===== examples\example_gimli_glider.md ===== -->

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

## Shot list (complete — 16 shots, median 2.4 s)
```
#01 0.0–1.4  VO "At forty-one thousand feet,"  STRESS "forty-one"  VISUAL RECONSTRUCTION: FIRSTENGINEER — 767 cockpit at night, both N1 gauges spinning down  MOVE fast push 100→118 % to gauges  TEXT none  SFX engine spool-down + master caution chime at 0.0  LOOP L1 opens  PURPOSE: the impossible moment, in action at frame 0
#02 1.4–2.4  VO "both engines went silent."  STRESS "silent"  VISUAL real photo C-GAUN 767 (SOURCE: Wikimedia Commons, CC BY-SA, credit on screen)  MOVE slow drift left  TEXT "AIR CANADA 143 · 23 JUL 1983" mono, small  SFX engine noise hard-cut to wind  LOOP L1  PURPOSE: real aircraft + silence = danger
#03 2.4–5.0  VO "The screens went black. Sixty-nine people on board."  STRESS "black", "sixty-nine"  VISUAL RECONSTRUCTION cockpit EFIS screens blinking off one by one, then cabin wide  MOVE pull back through cockpit door into cabin  TEXT "69 ON BOARD"  SFX relay clicks ×3, low hum dies  LOOP L1  PURPOSE: stakes (people)
#04 5.0–7.6  VO "The fuel gauges had said they had plenty."  STRESS "plenty"  VISUAL code-drawn fuel bar fills to 100 % on a 767 silhouette  MOVE tilt down from silhouette to bar  TEXT "FUEL: OK"  SFX soft fill tone  LOOP L1  PURPOSE: the false belief
#05 7.6–10.2 VO "They didn't. They had less than half."  STRESS "half"  VISUAL same bar drains to 45 %, red  MOVE micro shake on "didn't"  TEXT "22,300 kg needed / 10,100 kg on board" (SOURCE: Board of Inquiry)  SFX tick ×4, sub hit on "half"  LOOP L1 narrows  PURPOSE: the core number
#06 10.2–12.6 VO "Someone had done the maths in pounds."  STRESS "pounds"  VISUAL real refuelling-sheet scan / Board of Inquiry page (SOURCE label), push to 1.77 conversion factor, marker wipe  MOVE push-in 100→140 %  TEXT "1.77 lb/L" highlighted  SFX paper slide + pen  LOOP L1 closes partly  PURPOSE: the cause as evidence
#07 12.6–14.8 VO "The new jet used kilograms."  STRESS "kilograms"  VISUAL split: "lb" crossed out, "kg" in its place (code-drawn on paper texture)  MOVE whip-pan between halves on the stressed word  TEXT "lb ≠ kg"  SFX whoosh + stamp  LOOP L1 closed  PURPOSE: makes the mistake understandable in 1 s
#08 14.8–17.6 VO "Now a 132-tonne airliner was a glider."  STRESS "glider"  VISUAL RECONSTRUCTION side view of the 767 gliding over cloud tops at dusk, altitude counter falling  MOVE tracking alongside, slow  TEXT altitude counter 35,000→28,000 ft  SFX wind rising  LOOP L2 opens  PURPOSE: new situation
#09 17.6–19.8 VO "The nearest runway was too far."  STRESS "too far"  VISUAL code-drawn map Manitoba: Winnipeg circle, glide-range ring that falls short  MOVE map zoom out  TEXT "WINNIPEG · 65 NM" (⚠ verify)  SFX map tick, tension pulse  LOOP L2  PURPOSE: shows why the obvious answer fails
#10 19.8–22.6 VO "But the captain flew gliders on weekends."  STRESS "gliders"  VISUAL real archive photo of Capt. Bob Pearson (SOURCE label) or, if unlicensed, glider photo + name card  MOVE slow push to face  TEXT "CAPT. ROBERT PEARSON"  SFX music lifts one step  LOOP L2  PURPOSE: the human edge (first value flip at ~50 %)
#11 22.6–24.0 VO "You see, there was one more runway."  STRESS "one more"  VISUAL 0.8 s black, then map snaps to Gimli  MOVE none during black, then snap zoom  TEXT "GIMLI" mono  SFX music drop → silence → single low tone  LOOP L3 opens  PURPOSE: the turn
#12 24.0–27.4 VO "An old air force base. Closed."  STRESS "closed"  VISUAL real archive aerial of RCAF Station Gimli (SOURCE label)  MOVE slow drift down  TEXT "RCAF GIMLI · CLOSED 1971"  SFX distant wind  LOOP L3  PURPOSE: hope with a doubt
#13 27.4–30.4 VO "What nobody on board knew: it was now a racetrack."  STRESS "racetrack"  VISUAL archive drag-racing photo at Gimli Motorsport Park (SOURCE label)  MOVE pull back to reveal strip  TEXT none  SFX car engines rev, crowd  LOOP L4 opens  PURPOSE: the twist
#14 30.4–33.0 VO "And that day, it was full of families."  STRESS "families"  VISUAL archive / reconstruction: campers and families on the strip, view from the approaching jet  MOVE descending POV, accelerating  SFX crowd + rising whine of air over the fuselage  LOOP L4  PURPOSE: maximum anxiety
#15 33.0–36.2 VO "He side-slipped the jet to lose height, hit the runway hard, the nose gear collapsed —"  STRESS "hard", "collapsed"  VISUAL RECONSTRUCTION side-slip from behind, then touchdown low angle  MOVE handheld follow, shake on impact  SFX tyre screech, metal scrape (biggest hit, 88–92 %)  LOOP L4  PURPOSE: peak
#16 36.2–38.6 VO "and it stopped just before the crowd."  STRESS "crowd"  VISUAL real photo of the 767 nose-down on the Gimli strip with people around it (SOURCE label)  MOVE slow push-in, stop on last word  SFX scrape stops → silence → crowd murmur tail 0.8 s  LOOP L1–L4 closed  PURPOSE: payoff + scale
```
Checks: 16 shots · median 2.6 s · longest 3.4 s · no repeated asset · shot types used: reconstruction, archive photo, document, diagram/data, map, portrait, black beat.

## Packaging
Title: "The Jet That Ran Out of Fuel at 41,000 Feet" · IG first line: "Both engines stopped. The only runway was a racetrack." · Pinned comment: source (TSB report) + "The jet flew again for 25 more years."


<!-- ===== examples\example_millennium_bridge.md ===== -->

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

## Shot list (complete — 12 shots)
```
#01 0.0–2.6  VO "Two days after it opened, this bridge started dancing."  VISUAL real archive footage/photo of the crowded bridge 10 Jun 2000 (SOURCE label)  MOVE handheld push, lateral sway emphasised  SFX crowd + steel creak  PURPOSE: impossible result at frame 0
#02 2.6–4.0  VO "Thousands of people walked across it."  VISUAL wide of the deck crowd from bankside  MOVE slow pan  TEXT "10 JUNE 2000"  SFX footsteps bed
#03 4.0–5.4  VO "It swayed sideways."  VISUAL code-drawn top view, deck outline oscillating ±7 cm (⚠ verify amplitude)  MOVE locked  TEXT "SIDEWAYS ↔"  SFX low pulse each swing
#04 5.4–8.4  VO "And the more it swayed, the more they swayed with it."  VISUAL one pedestrian figure, centre of mass swinging with the deck  MOVE push in  SFX pulse speeds up
#05 8.4–10.2 VO "You see, when a floor moves,"  VISUAL 0.6 s black → close-up feet on a moving deck (diagram)  SFX music drops out
#06 10.2–12.0 VO "you widen your step to keep balance."  VISUAL feet diagram, step width arrows  SFX single footstep
#07 12.0–14.8 VO "Thousands of steps fell into the same rhythm."  VISUAL 1,000 dots start random, lock into phase (small multiples)  SFX scattered steps → unison stomp
#08 14.8–17.4 VO "Their feet were pushing the bridge in time."  VISUAL force arrows from dots onto deck, amplitude graph growing  SFX bass swell (peak builds)
#09 17.4–19.6 VO "London closed it after two days."  VISUAL archive newspaper headline (SOURCE label), paper slides in on desk  SFX paper + stamp
#10 19.6–23.0 VO "It took two years and 91 shock absorbers to fix."  VISUAL real photo of the viscous dampers under the deck (SOURCE label), counter 0→91  SFX hydraulic hiss ×3
#11 23.0–25.4 VO "Today, thousands cross it every day."  VISUAL present-day photo, St Paul's behind  MOVE pull-back scale reveal over the Thames (peak visual)  SFX city ambience
#12 25.4–28.0 VO "And it doesn't dance anymore."  VISUAL same framing as #01, bridge still  MOVE matches #01 start position → loops  SFX tail blends into #01 creak
```


<!-- ===== data/analysis_summary.md ===== -->

# Measured analysis — 302 Shorts, 19 channels, tiered within channel

Sample: for each channel, from its latest ~150 Shorts (newest 10 dropped because their views are not settled), the 6 most-viewed (TOP), 5 around the median (MID) and 5 least-viewed (LOW). Comparing tiers *inside the same channel* controls for channel size and audience; it shows what separates a channel's hits from its misses, not what makes a channel big.

## 1. Tier comparison (median of each metric)

| Metric | TOP | MID | LOW | TOP vs LOW |
|---|---|---|---|---|
| dur | 57.9 | 59.6 | 53.3 | ≈ same |
| cuts_per_10s | 1.38 | 1.24 | 1.22 | higher |
| med_shot | 4.67 | 5.34 | 4.37 | ≈ same |
| first_cut | 4.27 | 4.79 | 5.0 | lower |
| first_word | 0.0 | 0.0 | 0.0 | ≈ same |
| wpm | 177.0 | 179 | 179 | ≈ same |
| lufs | -15.15 | -17.1 | -16.0 | higher |
| loopdiff | 57.95 | 54.2 | 55.2 | ≈ same |
| hook_words | 10.0 | 10 | 10 | ≈ same |
| hook_number | 25 % | 26 % | 16 % | higher |
| hook_you | 26 % | 19 % | 24 % | ≈ same |
| hook_question | 21 % | 20 % | 23 % | ≈ same |
| hook_this | 18 % | 7 % | 12 % | higher |
| hook_I | 14 % | 16 % | 19 % | lower |
| but_pos | 44.74 | 44.19 | 44.03 | ≈ same |
| silence_gaps | 0.0 | 0 | 0 | ≈ same |
| end_word_rate | 2.64 | 2.78 | 2.65 | ≈ same |
| start_word_rate | 3.34 | 3.14 | 3.1 | ≈ same |

## 2. Within-channel paired difference (TOP median − LOW median per channel; share of channels where TOP > LOW)

| Metric | Channels | Median diff | TOP > LOW in |
|---|---|---|---|
| dur | 19 | 1.25 | 11/19 |
| cuts_per_10s | 19 | -0.13 | 7/19 |
| med_shot | 19 | 0.62 | 12/19 |
| first_cut | 19 | -1.54 | 4/19 |
| first_word | 19 | 0.0 | 0/19 |
| wpm | 19 | 3.5 | 13/19 |
| lufs | 19 | 0.75 | 13/19 |
| loopdiff | 19 | -9.5 | 9/19 |
| hook_words | 19 | 1 | 11/19 |
| hook_number | 19 | 0.0 | 3/19 |
| hook_you | 19 | 0.0 | 4/19 |
| hook_question | 19 | 0.0 | 3/19 |
| hook_this | 19 | 0.0 | 5/19 |
| hook_I | 19 | 0.0 | 1/19 |
| but_pos | 19 | -2.66 | 9/19 |
| silence_gaps | 19 | 0.0 | 5/19 |
| end_word_rate | 19 | 0.11 | 10/19 |
| start_word_rate | 19 | 0.23 | 14/19 |

## 3. Duration distribution (all tiers)

| Duration | TOP | MID | LOW |
|---|---|---|---|
| 0–20 s | 1 | 0 | 0 |
| 20–35 s | 6 | 6 | 14 |
| 35–45 s | 16 | 12 | 17 |
| 45–60 s | 55 | 39 | 34 |
| 60–90 s | 8 | 15 | 22 |
| 90–181 s | 26 | 23 | 8 |

## 4. Per channel

| Channel | Shorts listed | Channel median views | n analysed | TOP med views | LOW med views |
|---|---|---|---|---|---|
| EngineeringExplained | 61 | 2,300,000 | 16 | 23,000,000 | 196,000 |
| HistoryLegends | 150 | 211,500 | 16 | 3,900,000 | 14,000 |
| MagnatesMedia | 29 | 68,000 | 16 | 242,500 | 24,000 |
| MarkRober | 127 | 59,000,000 | 16 | 629,000,000 | 3,200,000 |
| MentourPilot | 80 | 495,500 | 16 | 3,550,000 | 39,000 |
| MrBallen | 150 | 388,500 | 16 | 4,600,000 | 54,000 |
| NEOexplains | 15 | 3,700,000 | 15 | 11,000,000 | 1,100,000 |
| NileRed | 138 | 16,000,000 | 16 | 154,000,000 | 2,500,000 |
| PlainlyDifficult | 15 | 41,000 | 15 | 85,000 | 18,000 |
| PracticalEngineeringChannel | 17 | 560,000 | 16 | 901,000 | 193,000 |
| RealEngineering | 79 | 453,000 | 16 | 12,500,000 | 74,000 |
| Sideprojects | 150 | 24,500 | 16 | 3,850,000 | 5,700 |
| TheB1M | 150 | 104,000 | 16 | 907,000 | 21,000 |
| TheInfographicsShow | 150 | 572,500 | 16 | 6,100,000 | 78,000 |
| bigthink | 150 | 33,500 | 16 | 804,500 | 11,000 |
| kurzgesagt | 135 | 2,900,000 | 16 | 14,000,000 | 681,000 |
| simplehistory | 150 | 37,500 | 16 | 1,250,000 | 9,100 |
| veritasium | 89 | 6,000,000 | 16 | 52,500,000 | 965,000 |
| zackdfilms | 150 | 8,950,000 | 16 | 26,000,000 | 2,600,000 |

## 5. What the tier comparison says (read this before using any number)

Measured on 302 Shorts (113 TOP, 95 MID, 93 LOW) from 19 channels. A "difference" only counts here if it shows up both in the pooled medians and inside most channels.

**Consistent but small differences [M]:**
- **The first cut comes earlier in hits.** TOP median 4.3 s vs LOW 5.0 s; TOP was earlier in 15 of 19 channels (median −1.5 s). This is the most consistent signal in the data: change the picture before ~4 s.
- **The opening is denser.** Words per second in the first 10 % were higher in TOP in 14 of 19 channels.
- **Hits are mixed slightly louder.** −15.2 vs −16.0 LUFS; louder in 13 of 19 channels. Master to about −14 to −15 LUFS and don't ship quiet.
- **Length:** 45–60 s is the most common TOP band (55 of 113). LOW has more 20–35 s videos (14 vs 6) and more 60–90 s videos (22 vs 8). 35–45 s is **not** better than other bands (16 TOP vs 17 LOW). Long story Shorts of 90 s or more appear more often in TOP (26 vs 8) but mostly on established channels.

**No meaningful difference [M]:** hook length (10 words), first word at 0.0 s (everyone does it, so it is table stakes, not an edge), narration speed (about 177–179 WPM in every tier; this run used Whisper base.en, while the v1 top-only run measured 159 with small.en, so compare speeds only within the same model), the position of the first "but" (~44 %), the loop difference and silence gaps.

**Hook-wording features don't separate hits from misses inside a channel.** Numbers, "you", questions and "this…" in the hook show some pooled differences (a number in 25 % of TOP vs 16 % of LOW hooks; "This…" in 18 % vs 12 %), but the paired median difference is 0 in every channel. Our `hookscore_story.py` scored TOP 40, MID 39 and LOW 39 on average, so it does **not** predict hits. Use it only to catch weak drafts.

**Conclusion:** inside a channel, what separates hits from misses is mostly **the story/topic and the packaging**, not measurable editing rhythm. Editing metrics (first cut, opening density, loudness) are hygiene: get them right, but they won't make a weak story go viral. This is why `11-story-discovery.md` (topic demand, outlier multiples) is the biggest lever, and why every rule in the skill that is not in this section is tagged [E] or [R].

**Limits:** 19 channels, mostly large or mid-size. View counts are a proxy (the age, the topic and the algorithm all affect them). Whisper and the FFmpeg scene detector are imperfect: the detector undercounts soft transitions and continuous moves. Channels that failed or were excluded: the wrong "Mustard" (a rap artist, removed), MustardChannel (only 6 Shorts listed, below the minimum), and several channels whose Shorts tab returned no list. Reproduce with `tools/scout.py` → `tools/analyze_shorts.py` (PICK=pick2.json) → `tools/aggregate.py data/pick2.json data/shorts_full_analysis_v2.json data`.


<!-- ===== data/README.md ===== -->

# data/

| File | What |
|---|---|
| `pick2.json` | v2 sample: per channel, the 6 most-viewed, 5 median and 5 least-viewed Shorts from the latest ~150 (newest 10 dropped). It holds the video id, title, views, tier, the channel median and the number of Shorts listed. |
| `shorts_full_analysis_v2.json` | per-video measurements: duration, word timestamps (Whisper base.en), FFmpeg scene cuts (threshold 0.28), median shot, first cut, WPM, first word, 0–3 s hook, integrated and per-second LUFS, first/last frame difference |
| `analysis_summary.md` | tier comparison, within-channel paired differences, duration bins, per-channel table, interpretation and limits |
| `hooks_library.md` | the 0–3 s spoken hook of every analysed Short with its tier |
| `analysis_v1_76_top_only.md`, `shorts_full_analysis.json` | the first (v1) run: top 5 per channel only, survivorship-biased, kept for transparency |

The videos themselves are not redistributed (copyright). Re-download them by id with `tools/scout.py` (yt-dlp, 360p).

**Channel identity check:** before analysing a channel, confirm that the handle resolves to the intended creator (look at the channel title and three video titles). The v1 run used `@Mustard`, which is a rap artist and not the aviation documentary channel; those rows are excluded from v2.
