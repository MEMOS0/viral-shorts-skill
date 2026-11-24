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
