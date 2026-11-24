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
