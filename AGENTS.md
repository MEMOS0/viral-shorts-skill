# AGENTS.md — how an agent should use and change this repo

## Use (making Shorts)
1. Read `SKILL.md` only; open a reference file when its step comes up (progressive disclosure: don't load all 15 references up front).
2. Stage outputs are files, and each stage starts from the previous file, not from chat memory:
   `discovery.json` → `critic.json` → `gate.json` (PASS) → `research.md` → `short_plan.md` + `storyboard.json` (check passes) → render → `critic/` pack → critic verdict → publish → `data/calibration.csv`.
3. Hand-offs between roles (Story Scout, Topic Critic, Producer, Video Critic) go through those files. The two critics run in a fresh context that has never seen the producer's reasoning.
4. Hard stops: `topic_gate.py` exit ≠ 0, `check_storyboard.py` exit ≠ 0, critic_pack `gate_pass: false`, critic verdict FIX/KILL. Do not override a stop by rewording the score.
5. Never present an [E] rule as measured. Never invent retention or analytics numbers.

## Change (developing the skill)
- `python -m pytest -q tests` must pass. Add a regression test with every bug fix.
- After changing data or `tools/aggregate.py`: rerun the reproduce chain in `data/interpretation.md`, then update `data/interpretation.md` by hand if any conclusion changed.
- After changing any .md: `python tools/build_all_in_one.py` (regenerates `ALL_IN_ONE.md`; CI-style check: `--check`).
- Third-party code lives in `tools/third_party/<name>/` with its LICENSE; OpenMontage code is not copied (licence), only ideas.
- No hardcoded paths, no secrets, no downloaded videos in git.
