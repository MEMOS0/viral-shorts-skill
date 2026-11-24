# 16 — Packaging: title, description, tags, hashtags, cover, pinned comment

Packaging decides whether the right people find and choose the video; it can't rescue a weak story. Write it **after** the critic SHIPs, from the final cut, and lint it: `python tools/package_lint.py package.json`.

## 1. Platform facts (checked 2026-11; re-check yearly) [R]

| Item | YouTube Shorts | Instagram Reels |
|---|---|---|
| Title | ≤ 100 characters, no `<` `>` (YouTube Help "Edit video settings") | no title field; the first caption line acts as the title |
| Description / caption | ≤ 5,000 characters | ≤ 2,200 characters; **captions are what Search indexes** (keywords + hashtags in the caption, not in comments) |
| Hashtags | up to 3 most engaging shown by the title; **> 60 hashtags = all ignored**, over-tagging can remove the video from search (YouTube Help "hashtags") | **max 5 per post/Reel** since Dec 2025 (Mosseri); generic tags like #reels #explore don't help and may hurt |
| Tags | ≤ 500 characters in total; "useful if content is commonly misspelled, otherwise minimal role" (YouTube Help "tags") | — |
| Links | URLs in Shorts descriptions and comments are **not clickable**; use the single "Related video" link to a long-form or series video | links in captions are not clickable; use the bio / link sticker |
| Policy | spam & deceptive practices: no metadata that misleads about the content, no tag stuffing; thumbnail must not mislead (YouTube Help "Spam policy", "Thumbnails policy") | Recommendation guidelines: no engagement bait ("comment YES") |
| Search signals | title, description, spoken words and on-screen text | caption, on-screen text, spoken words, username/bio |

## 2. What our data say about titles [M]
Across 302 Shorts (within channel, `data/analysis_summary.md`): title length (median ~39 characters, ~7 words), numbers, questions, ALL-CAPS words, emoji, "you", "this/why/how" openers **do not separate hits from misses** (all CIs include 0, none replicates in both split halves). There is no title formula. Titles work through the idea they name, so:

## 3. Title rules [E unless tagged]
1. **Name the strange concrete thing, not the category**: "One rod changed. 114 people died." beats "Engineering disaster explained".
2. **Complement, don't repeat, the hook**: the title is read while the first line is heard; together they should open one gap. Never reveal the cause the video withholds.
3. **Truthful**: everything the title promises happens in the video (policy [R] + trust). No "you won't believe", no fake urgency, no ALL-CAPS shouting (max one capitalised word for emphasis).
4. **Searchable noun**: include the name people search (Hyatt Regency, Challenger, Tacoma Narrows) when the topic has demand evidence (Wikipedia pageviews/Trends from `11`).
5. **Length**: front-load the meaning in the first ~40 characters (what shows on phones); hard limit 100.
6. **Write 5, pick 2**: one for the upload, one for a later YouTube title test or an Instagram trial reel.
7. Same language as the narration; no emoji in titles for documentary-style channels.

## 4. Description (YouTube) / caption (Instagram)
- Line 1: a second hook sentence with the searchable keywords, in plain words ("In 1981 a hotel walkway in Kansas City fell because one design detail was changed.").
- Lines 2–3: one surprising fact the video didn't have room for, and the lesson in one line.
- Sources: "Sources: NBS report NBSIR 82-2465 (1982); …" — short names, no URLs needed in Shorts (not clickable); archive credits as required by the licence ("Photo: Lee Lowery Jr., NBS, public domain").
- Reconstruction disclosure: "3D reconstruction by FirstEngineer; not real footage." AI disclosure only if the platform's synthetic-media rule applies (this skill doesn't use AI imagery).
- Product bridge: at most one neutral line, never a link pitch (`08`).
- Hashtags last: YouTube 3–5 (topic, field, event; first three are the ones shown); Instagram ≤ 5, specific (#engineeringdisaster #structuralengineering #kansascity), never #reels #viral #fyp #explore.
- No questions designed only to bait comments; a genuine question tied to the story is fine.

## 5. Tags (YouTube)
5–12 tags, ≤ 500 characters: the event name, common misspellings ("hyatt regancy"), the people/places, the field. They barely affect discovery [R]; don't spend time beyond that.

## 6. Cover / thumbnail frame
Shorts: choose the frame in the YouTube app; Reels: upload a cover and set grid crop (center 1:1 / 3:4). Pick the frame that shows the strange object or moment from the hook, with ≤ 4 words of large text inside the centre safe area, real archive or a labelled reconstruction; consistent type and colour across the channel. Never a frame that isn't in the video.

## 7. Pinned comment
One line that adds value (a source detail, a correction, "the second walkway is why the death toll was so high"), or the link to the long-form via the Related-video feature. Pin your own correction if a fact is challenged.

## 8. Posting
Upload time matters less than consistency; post when your own analytics show the audience is active, and keep the cadence the channel can sustain. Log title, description first line, hashtags and cover choice in `data/calibration.csv` so packaging can be compared later.

## 9. Deliverable: `package.json`
```json
{"platform": "youtube", "title": "...", "alt_titles": ["...", "...", "...", "..."], "description": "...", "hashtags": ["#..."],
 "tags": ["..."], "cover_time_s": 1.2, "cover_text": "ONE ROD", "pinned_comment": "...", "related_video": "https://youtube.com/watch?v=...",
 "hook_line": "...", "withheld_cause": "two rods instead of one", "keywords": ["Hyatt Regency", "walkway collapse"]}
```
Make one per platform (`"platform": "instagram"` uses `caption` instead of `title`/`description`).
