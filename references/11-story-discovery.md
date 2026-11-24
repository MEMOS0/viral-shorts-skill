# 11 — Story discovery: Story Scout, Topic Critic, evidence gate

Pick stories by evidence, not taste, and never by "first idea that is easy to make". Discovery is two
independent roles and one machine gate. **No discovery report with `gate.json` status PASS = no script, no render.**

```
Story Scout ──► discovery.json ──► Topic Critic (fresh context) ──► critic.json ──► tools/topic_gate.py ──► gate.json (PASS/BLOCK)
```

## 1. Why people watch and share a story [R]

| Driver | What it means for topic choice | Source |
|---|---|---|
| Curiosity gap | the viewer knows the outcome is strange but not why | Loewenstein 1994 |
| High-arousal emotion | awe, anger, anxiety get shared; sadness and calm do not | Berger & Milkman 2012 |
| Social currency / practical value | "send this to the engineer you know"; "this is in your house" | Berger 2013 (*Contagious*) |
| Concreteness | a single object, number, person beats a system | Heath & Heath 2007 |
| Identification | a person who had to decide under pressure | narrative transportation, Green & Brock 2000 |
These explain why people *can* care. They do not tell you which topic will beat another this month: only demand evidence does.

## 2. Story Scout (role 1)

Produce **≥ 5 candidate topics, each with ≥ 3 angles**, from at least three source families:

| Source family | Pull |
|---|---|
| Investigation reports (NTSB, AAIB, BEA, TSB, CSB, NASA, NIST, court records) | single concrete cause, primary source |
| Wikipedia lists + pageviews API (`wikimedia.org/api/rest_v1/metrics/pageviews/per-article/...`) | candidate pool + 90-day interest |
| YouTube Shorts and long-form on the topic (`tools/outliers.py`) | demand, saturation, outlier multiples |
| Google Trends (5-year and 90-day) | rising / flat / falling; spikes from news |
| Reddit (r/CatastrophicFailure, r/engineering, r/todayilearned; top of year) | what people already share and argue about |
| Comments on competitors' and your own top videos | explicit "do X next", confusion, debate |
| Anniversaries in the next 30–60 days, current news | timeliness |

For every topic record **evidence with URLs** (schema `templates/discovery.json`):
- `existing_shorts` / `long_form`: views, age, channel median → **outlier multiple = views ÷ channel median** and **views/day**. Raw views rank channel size, not ideas. Exclude each channel's newest ~10 uploads (views not settled).
- `wikipedia`, `trends`, `reddit`, `comments`: at least the URL and the number you read.
- `sources`: ≥ 2, at least one primary. `archive`: ≥ 2 licensed real items (`tools/find_archive.py`).
- `scores` 0–5 and `confidence` high/medium/low for: demand, gap, visual, clarity (one-sentence cause a 12-year-old gets), emotion, facts, fit.

### Demand vs gap (the classic mistake)
| Evidence | Meaning | Action |
|---|---|---|
| Long-form ≥ 1 M views or ≥ 3× its channel median, few Shorts | **gap** | strong candidate |
| Many Shorts ≥ 1 M views (≥ 5) | saturated | only with an angle of novelty ≥ 4 and a `closest_existing` URL that proves it differs |
| Few videos *and* low pageviews / flat Trends / no Reddit | **no demand**, not a gap | reject or park |
| One viral Short, nothing else | single outlier; packaging may have carried it | need a second evidence type |
Small channels count more than giants: a 10× outlier on a 5 k-subscriber channel shows the topic and packaging carried it.

### Topic ≠ angle
The **topic** is the event (Hyatt Regency walkway collapse). The **angle** is the story you tell about it
("one rod was changed to two"; "the engineer who signed it"; "why the second walkway made it worse"). Score angles on:
surprise, stakes, specificity, visual_hook (can frame 0 show it?), payoff, novelty (vs `closest_existing`). Every angle needs a hook line and a payoff line.

## 3. Topic Critic (role 2, independent)

A different model or a fresh session with **only** `discovery.json` (not the Scout's reasoning). Its job is to kill topics. For each topic:
1. Open every URL. Mark evidence that is missing, misread, stale or irrelevant.
2. Search for the three strongest existing Shorts on the topic; if the Scout missed them, saturation is understated.
3. Attack the best angle: "Would a viewer who has seen the top existing Short learn anything new?"
4. Attack clarity: explain the cause in one sentence to a non-engineer; if you can't, it fails.
5. Name the bias: did the Scout prefer this because it is easy to produce (assets already on disk)?
Return `critic.json`: `{ "<topic id>": {"verdict": "pass|reject", "reasons": [...], "attacks": [...]} }` (`templates/topic_critic.md`).

## 4. The gate (`tools/topic_gate.py`) — non-compensatory

1. **Hard gates (any fail = topic out):** ≥ 2 demand-evidence types with URLs; ≥ 2 sources incl. 1 primary; ≥ 2 licensed archive items; facts ≥ 3 and clarity ≥ 3; Topic Critic verdict pass; ≥ 3 angles.
2. **Floors:** every component ≥ 2 after penalties.
3. **Uncertainty penalty:** confidence medium −0.5, low (or missing) −1. Demand without evidence is capped at 2.
4. **Score:** geometric mean of components → 0–100 (one weak part drags everything down; an average would hide it). Topic ≥ 60 and best angle ≥ 60.
5. **Rank** by the weaker of topic and angle. Selected + runner-up are written to `gate.json` and `discovery_report.md`.
6. **Report-level block:** < 5 topics, or no topic passes.

The numbers 60 / floor 2 / 2 evidence types are [E] defaults. Recalibrate them with `tools/calibrate.py` once you have ≥ 30 published videos.

## 5. Learn from your own results
After each batch log, per video, topic id, angle id, gate scores, critic score and 7-day metrics (views/day, viewed-vs-swiped, average % viewed) in `data/calibration.csv`, then run `tools/calibrate.py`. If gate scores do not rank your own results (Spearman ρ CI includes 0), change the weights — and say so.
