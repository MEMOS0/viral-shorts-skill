# viral-shorts-skill

A complete, data-backed skill for creating high-retention **story Shorts and Reels** (engineering disasters, science, history), written for AI agents and human editors.

- `SKILL.md` — entry point: rules and workflow.
- `references/` — platforms, psychology, hooks, second-by-second grid, script, visuals, sound, endings/CTA, research, QA.
- `data/` — second-by-second measurements of 302 Shorts (TOP/MID/LOW within each of 19 channels): words, cuts, motion, first frame, loudness, views/day; effect sizes, CIs, split-half replication and an honest interpretation (`data/analysis_summary.md`).
- `templates/` — per-video plan and batch plan formats.
- `examples/` — fully worked Shorts.
- `tools/` — discovery gate, outlier finder, archive finder, live trend scanner, storyboard checker, render critic pack, calibration, blind pair test and the full dataset chain. `tests/` — regression tests (`python -m pytest -q tests`).
- `AGENTS.md` — stage files, hand-offs and hard stops for agents. Install: `pip install -r requirements.txt` + FFmpeg.

## MCP/server use

AI agents can call the production gates directly over stdio MCP:

```bash
pip install -e .[test]
viral-shorts-mcp
# or without installing: python tools/mcp_server.py
```

The Markdown references and measured data are part of the package corpus. A normal wheel install includes them; use an editable install for development, or set `VIRAL_SHORTS_ROOT` to a checkout when launching against a separate working copy. Client configuration shape:

```json
{"mcpServers":{"viral-shorts":{"command":"viral-shorts-mcp","env":{"VIRAL_SHORTS_ROOT":"/absolute/path/to/viral-shorts-skill"}}}}
```

Tools expose schema validation, topic-gate evaluation, live demand scanning, storyboard validation, package linting, hook scoring, post-render critic-pack generation, calibration and deterministic local semantic retrieval. Markdown references are available as `skill://...` resources; path traversal outside the repository is rejected. The server never overrides hard gates.

Usage with any LLM: give it `SKILL.md` plus the `references/` files (or the single-file `ALL_IN_ONE.md`) and ask for a batch, e.g. "Using this skill, plan 10 engineering-disaster Shorts for YouTube and Instagram."


## v2 changes
- The dataset grew from 76 top-only Shorts to 302 tiered Shorts. The wrong Mustard channel is removed. Findings are tagged measured, research or editorial (`data/analysis_summary.md` §5).
- Added: story discovery and viral-potential score (11), an independent critic agent (12), camera direction (13), `find_archive.py` (licensed real archive), `critic_pack.py`, `hookscore_story.py`, and reproducible `scout.py`, `analyze_shorts.py` and `aggregate.py`.
- Integrated ideas from Jakeschincariol/youtube-agent-skill (MIT, tools vendored), AustinZ21/cinematic-skills (MIT, tools vendored) and OpenMontage (AGPL, ideas only, no code).

## v3 changes (audit)
- **Bugs fixed, each with a regression test:** scout put 2 videos in both TOP and MID (tiers now disjoint); aggregate compared negative LUFS with ×1.1 (the "hits are louder" claim is withdrawn); binary hook features were summarised with medians (now shares); critic freeze threshold 1.5 s vs QA 0.5 s (now 0.5 s with declared holds); critic command lacked the output dir; licence filter accepted CC BY-ND and free text (now PD/CC0/CC BY/CC BY-SA only, NASA flagged for review); Internet Archive was documented but missing (added); five wrong-channel Mustard rows were still in the data (removed).
- **Statistics:** Cliff's delta with bootstrap CIs, within-channel sign tests with Benjamini–Hochberg correction, within-channel Spearman against views/day (age-normalised), split-half replication, motion features that catch soft transitions. Result: no editing metric survives correction; only an information-dense opening replicates. The hook scorer does not predict hits and says so.
- **Discovery:** Story Scout → independent Topic Critic → `topic_gate.py` with hard gates, floors, uncertainty penalties, geometric-mean scoring, topic vs angle, demand vs gap. Production is blocked without PASS.
- **Production:** machine-readable `storyboard.json` + `check_storyboard.py`; critic watches `proxy.mp4` and returns QA and viral estimates separately; `calibrate.py` checks whether scores predict real results; general-audience storytelling guide (15).
