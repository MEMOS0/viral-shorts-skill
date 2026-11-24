# data/

| File | What |
|---|---|
| `pick2.json` | v2 sample: per channel, the 6 most-viewed, 5 median and 5 least-viewed Shorts from the latest ~150 (newest 10 dropped). It holds the video id, title, views, tier, the channel median and the number of Shorts listed. |
| `shorts_full_analysis_v2.json` | per-video measurements: duration, word timestamps (Whisper base.en), FFmpeg scene cuts (threshold 0.28), median shot, first cut, WPM, first word, 0–3 s hook, integrated and per-second LUFS, first/last frame difference |
| `analysis_summary.md` | tier comparison, within-channel paired differences, duration bins, per-channel table, interpretation and limits |
| `hooks_library.md` | the 0–3 s spoken hook of every analysed Short with its tier |
| `motion_features.json` | per-video motion features at 10 fps (`tools/motion_features.py`): mean/p90 frame change, static share, longest static run, hard and soft changes (catches fades and continuous animation that the scene detector misses), first-frame brightness/contrast/colourfulness/edges |
| `video_meta.json` | upload date, current views, likes, comments, subscriber count, fetch date (`tools/fetch_meta.py`); used for views/day |
| `interpretation.md` | the hand-written reading of the numbers; `aggregate.py` appends it to `analysis_summary.md` |
| `v1_rows_not_in_pick2.json` | v1 rows outside the v2 sample (wrong Mustard channel removed) |
| `analysis_v1_76_top_only.md`, `shorts_full_analysis.json` | the first (v1) run: top 5 per channel only, survivorship-biased, kept for transparency |

The videos themselves are not redistributed (copyright). Re-download them by id with `tools/scout.py` (yt-dlp, 360p).

**Channel identity check:** before analysing a channel, confirm that the handle resolves to the intended creator (look at the channel title and three video titles). The v1 run used `@Mustard`, which is a rap artist and not the aviation documentary channel; those rows are deleted from the v2 analysis file. Tiers are disjoint since this version (`scout.tiers`); two old overlaps are resolved to TOP by `aggregate.load_pick`.
