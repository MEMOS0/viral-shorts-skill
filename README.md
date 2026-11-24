# viral-shorts-skill

A complete, data-backed skill for creating high-retention **story Shorts and Reels** (engineering disasters, science, history), written for AI agents and human editors.

- `SKILL.md` — entry point: rules and workflow.
- `references/` — platforms, psychology, hooks, second-by-second grid, script, visuals, sound, endings/CTA, research, QA.
- `data/` — second-by-second measurements of 80 top story Shorts from 16 channels (durations, cuts, words per minute, first-word timing, hooks, loudness).
- `templates/` — per-video plan and batch plan formats.
- `examples/` — fully worked Shorts.
- `tools/` — the analysis script used to build the dataset.

Usage with any LLM: give it `SKILL.md` plus the `references/` files (or the single-file `ALL_IN_ONE.md`) and ask for a batch, e.g. "Using this skill, plan 10 engineering-disaster Shorts for YouTube and Instagram."
