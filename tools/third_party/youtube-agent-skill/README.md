Vendored from https://github.com/Jakeschincariol/youtube-agent-skill (MIT, see LICENSE). Unmodified except swipe.py's hooks.json path.
- `swipe.py` — rank videos by multiple over their own channel's median (needs ≥4 videos per channel).
- `hookscore.py` + `hooks.json` — weakest-link hook score (60 % mean + 40 % weakest property) and 21 formulas with failure modes. Written for long-form talking-head YouTube; use `../hookscore_story.py` for story Shorts.
- `retention.py` — reads a YouTube Studio audience-retention CSV: hook leak, cliffs (with `--transcript`, prints what was said there), slide.
- `title.py` — title + thumbnail lint: 60/40-char truncation, thumbnail ≠ title, ≤ 3 thumbnail words, ≤ 2 all-caps words, number/name/date.
