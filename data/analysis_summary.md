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
