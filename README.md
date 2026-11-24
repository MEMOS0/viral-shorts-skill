# viral-shorts-skill

A complete, data-backed skill for creating high-retention **story Shorts and Reels** (engineering disasters, science, history), written for AI agents and human editors.

- `SKILL.md` — entry point: rules and workflow.
- `references/` — platforms, psychology, hooks, second-by-second grid, script, visuals, sound, endings/CTA, research, QA.
- `data/` — second-by-second measurements of 80 top story Shorts from 16 channels (durations, cuts, words per minute, first-word timing, hooks, loudness).
- `templates/` — per-video plan and batch plan formats.
- `examples/` — fully worked Shorts.
- `tools/` — the analysis script used to build the dataset.

Usage with any LLM: give it `SKILL.md` plus the `references/` files (or the single-file `ALL_IN_ONE.md`) and ask for a batch, e.g. "Using this skill, plan 10 engineering-disaster Shorts for YouTube and Instagram."


## v2 changes
- The dataset grew from 76 top-only Shorts to 302 tiered Shorts. The wrong Mustard channel is removed. Findings are tagged measured, research or editorial (`data/analysis_summary.md` §5).
- Added: story discovery and viral-potential score (11), an independent critic agent (12), camera direction (13), `find_archive.py` (licensed real archive), `critic_pack.py`, `hookscore_story.py`, and reproducible `scout.py`, `analyze_shorts.py` and `aggregate.py`.
- Integrated ideas from Jakeschincariol/youtube-agent-skill (MIT, tools vendored), AustinZ21/cinematic-skills (MIT, tools vendored) and OpenMontage (AGPL, ideas only, no code).
