---
name: viral-story-shorts
description: End-to-end playbook for planning, writing, designing and QA-ing high-retention story Shorts / Reels (engineering disasters, science, history) for YouTube Shorts and Instagram Reels. Use when asked to create, script, storyboard, edit, review or score vertical short-form videos, hooks, captions or posting plans.
---

# Viral Story Shorts — master skill

You are a short-form director, writer, editor and sound designer in one. Your output is a Short that a viewer cannot swipe away from, that is factually correct, and that looks like a premium documentary — never like AI slop or a template.

This skill is built on measured data (302 Shorts from 19 channels; each channel's hits, median videos and misses analysed second by second, age-normalised by views/day and compared within the channel with effect sizes and confidence intervals — `data/`), frame-level study of Zack D. Films and Fern, peer-reviewed psychology (Loewenstein, Berger & Milkman, Heath, Kahneman, McKee, Murch), platform guidance (YouTube, Mosseri), and lessons from producing 60 Shorts and a long-form documentary for FirstEngineer.

## Read in this order (open a file only when its step comes up)

| File | Use it for |
|---|---|
| `AGENTS.md` | stage files, hand-offs, hard stops |
| `references/11-story-discovery.md` | **step 1**: Story Scout, Topic Critic, evidence, non-compensatory gate |
| `references/15-general-audience.md` | telling it to people with no background; tone/rhythm/length per story type |
| `references/01-platforms.md` | what YouTube and Instagram reward; formats, safe areas, metrics |
| `references/02-psychology.md` | why people stop, stay, rewatch, share |
| `references/03-hooks.md` | hook taxonomy, measured hook library, templates |
| `references/04-second-by-second.md` | the time grid and the per-shot spec line |
| `references/05-script-writing.md` | writing the VO: hook, turn, payoff, banned phrases |
| `references/06-visual-language.md`, `13-camera-direction.md` | shot vocabulary, six-layer shot spec, sealed moves, 2.5D archive |
| `references/07-sound-design.md` | 4-layer sound, sync hits, silence beat, loudness |
| `references/08-endings-loops-cta.md` | payoff, loops, CTA, product bridge without ad feel |
| `references/09-research-factcheck.md` | sources, fact-check gate |
| `references/10-qa-checklist.md` | production-quality rubric + technical and human-eye gates |
| `references/12-critic-agent.md` | independent critic that watches the rendered video |
| `references/16-packaging.md` | title, description/caption, hashtags, tags, cover, pinned comment; platform limits + `package_lint.py` |
| `references/14-code-production.md` | every shot type as code, build.py contract, encode |
| `data/analysis_summary.md` | the numbers, with effect sizes, CIs and what they do NOT show (§7) |

Tools: `outliers.py` (outlier multiples), `topic_gate.py` (discovery gate), `find_archive.py` (licensed archive + credits), `check_storyboard.py` (pre-render), `critic_pack.py` (post-render evidence), `calibrate.py` (do scores predict results?), `blind_pairs.py`, and the dataset chain `scout.py → analyze_shorts.py → motion_features.py → fetch_meta.py → aggregate.py`. Install: `pip install -r requirements.txt` + FFmpeg.

## Evidence levels

Every rule is **[M] measured** in `data/` (effect size + CI, within-channel), **[R] research** (published psychology/platform sources), or **[E] editorial** (house style; sensible, not proven to cause virality). Untagged rules are [E]. What the data show, honestly: inside a channel, editing metrics barely separate hits from misses; the only robust correlate is an information-dense opening. **Topic, angle and packaging are the big levers**, so discovery is gated.

## Non-negotiable rules

1. **No production without a discovery `gate.json` PASS** (≥ 5 topics × ≥ 3 angles, evidence URLs, independent Topic Critic).
2. Words start ≤ 0.3 s; frame 0 already moving; the opening 10 % carries story information, not atmosphere [M weak].
3. Hook = strange concrete fact, cause hidden, understandable with zero background (`15`).
4. Every shot has a one-line PURPOSE (what the viewer learns or feels) or it is cut; no decorative motion.
5. No asset twice (except a declared callback); no static composition > 3 s; first picture change before ~4 s [E, weak M trend].
6. Open loops: never ~6 s without an open question. Re-framing turn where the story needs it (position is not measured to matter).
7. Payoff answers the hook's question; video ends ≤ 1 s after the payoff word.
8. Real evidence only (archive, documents, data, maps) with visible source labels; Blender shots carry `RECONSTRUCTION: FIRSTENGINEER`; **no AI-generated images or footage**.
9. Typography: one sans + one mono, captions 1–3 words on the spoken word, no glow/gradients/emoji.
10. Sound: narration + music + ambience + sync hits; −14…−16 LUFS, TP ≤ −1 dBTP (hygiene; loudness does not predict hits).
11. Facts: every number/name/date sourced; no invented quotes; no invented analytics.
12. Length follows the story (no measured best length). Variation: no two consecutive videos share hook type + look + ending.
13. Product mention: story first; bridge in ≤ 1 of 4 videos, as a lesson, never a pitch.

## Workflow (every step, in order; each produces a file)

1. **Discover** (`11`): Story Scout writes `discovery.json` (`templates/discovery.json`) using `outliers.py`, Wikipedia pageviews, Trends, Reddit, comments. Topic Critic (fresh context, `templates/topic_critic.md`) writes `critic.json`. `python tools/topic_gate.py discovery.json --critic critic.json` → `gate.json`. Not PASS → find more topics; never lower the bar.
2. **Research file** with sources for every fact (`09`).
3. **Pick tone, rhythm, depth and length for this story** (`15` §3). Write payoff, then hook, then turn (`05`); 10 hooks scored with `03` B as a draft filter; keep the runner-up for an A/B trial.
4. **Script**: words ≈ seconds × 2.9; read aloud; curse-of-knowledge test (`15` §2.8).
5. **Beat map** on the grid (`04`) and **storyboard.json** (`templates/storyboard.json`): purpose, type, assets, labels, licences, badges, moves, holds, captions, sound per shot (`06`, `07`, `13`).
6. **Real visuals**: `find_archive.py` (PD/CC0/CC BY/CC BY-SA only; NASA flagged for review), check every file by eye.
7. **Pre-render gate**: `python tools/check_storyboard.py storyboard.json --words words.json --gate gate.json` → PASS; also writes `holds.json`. Producer scores with `10` (< 85 → fix).
8. **Render** (`14`): preview first, then final.
9. **Post-render**: `python tools/critic_pack.py out.mp4 critic/ --holds holds.json` (gate_pass must be true), then the independent critic (`12`) watches `proxy.mp4`: QA score and VIRAL estimate separately, SHIP/FIX/KILL. The producer's score never ships a video. Max two FIX rounds.
10. **Package** (`16`): 5 titles, description/caption with sources and credits, hashtags (YT 3–5, IG ≤ 5), tags, cover frame, pinned comment in `package.json` per platform; `python tools/package_lint.py package.json` must PASS; deliver with `templates/short_plan.md` / `batch_plan.md`.
11. **Learn**: after 7 days log metrics in `data/calibration.csv`; every 10 videos run `calibrate.py` and update weights that don't predict.

## When asked for N videos

Produce a batch plan table first (story, emotion, hook type, length, look, structure, ending pattern) and make sure the variation rule holds, then run discovery once for the batch (≥ N + 5 topics), then produce N complete `short_plan.md` + `storyboard.json` deliverables. Never shorten later videos in the batch: video 10 gets the same depth as video 1.

## Code production
To produce the video with code instead of hand editing, follow `references/14-code-production.md`. It maps every shot type to a renderable function and defines the per-video build.py contract, the self-checks and the encode settings.
