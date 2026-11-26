"""MCP server exposing the viral-shorts production gates to AI agents.
Run: python tools/mcp_server.py  (stdio MCP transport). Requires `mcp<2`.
"""
import json, os, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mcp.server.fastmcp import FastMCP
import calibrate, check_storyboard, hookscore_story, package_lint, schema_validate, semantic_search, topic_gate, trend_scan
from skill_root import skill_root

ROOT = skill_root()
mcp = FastMCP("viral-shorts-skill")

@mcp.tool()
def validate_json(kind: str, document: dict) -> dict:
    """Validate a discovery, storyboard, or package document against its JSON schema."""
    errors = schema_validate.validate(kind, document)
    return {"pass": not errors, "errors": errors}

@mcp.tool()
def evaluate_topic_gate(discovery: dict, critic: dict | None = None) -> dict:
    """Run the non-compensatory discovery gate; PASS is required before production."""
    return topic_gate.evaluate(discovery, critic or {})

@mcp.tool()
def validate_storyboard(storyboard: dict, words: list | None = None, gate: dict | None = None) -> dict:
    """Run the pre-render storyboard gate and return errors, warnings and declared holds."""
    errors, warnings = check_storyboard.check(storyboard, words, gate)
    return {"pass": not errors, "errors": errors, "warnings": warnings, "holds": check_storyboard.holds(storyboard)}

@mcp.tool()
def lint_package(package: dict) -> dict:
    """Lint YouTube/Instagram title, description/caption, hashtags, tags and cover metadata."""
    errors, warnings = package_lint.lint(package)
    return {"pass": not errors, "errors": errors, "warnings": warnings}

@mcp.tool()
def score_hook(text: str) -> dict:
    """Score a story hook with the local heuristic model."""
    props, score = hookscore_story.score(text)
    return {"score": score, "properties": props}

@mcp.tool()
def calibrate_scores(rows: list[dict]) -> dict:
    """Measure whether topic/critic scores actually predict published-video outcomes."""
    res = calibrate.run([dict(r) for r in rows])
    return {"results": [{"predictor": p, "outcome": o, "n": n, "rho": rho, "ci95": ci} for (p, o), (n, rho, ci) in res.items()], "minimum_videos": 8}

@mcp.tool()
def search_skill(query: str, limit: int = 5) -> list:
    """Semantically retrieve relevant skill rules, examples and measured hook evidence."""
    return semantic_search.search(query, max(1, min(20, int(limit))))


@mcp.tool()
def scan_topic_demand(topics: list[dict], days: int = 90, youtube_n: int = 8, reddit_limit: int = 5) -> dict:
    """Collect live Wikipedia/YouTube/Reddit demand evidence for Story Scout topics; never fills judgment scores."""
    return trend_scan.scan_topics(topics, days=max(7, min(365, int(days))), youtube_n=max(1, min(20, int(youtube_n))), reddit_limit=max(1, min(10, int(reddit_limit))))

def _read_markdown(*parts: str) -> str:
    p = os.path.abspath(os.path.join(ROOT, *parts))
    if not p.startswith(os.path.abspath(ROOT) + os.sep) or not p.endswith(".md") or not os.path.isfile(p): raise ValueError("not a markdown file inside the skill")
    return open(p, encoding="utf-8").read()

@mcp.tool()
def build_critic_pack(video: str, outdir: str, holds: list | None = None, model: str = "base.en", lang: str = "en", freeze: float = 0.5, no_whisper: bool = False) -> dict:
    """Build the post-render critic evidence pack from a local video with ffmpeg; gate_pass must be true before critic review."""
    if not os.path.isfile(video): return {"pass": False, "errors": [f"no such video: {video}"]}
    os.makedirs(outdir, exist_ok=True)
    cmd = [sys.executable, os.path.join(os.path.dirname(os.path.abspath(__file__)), "critic_pack.py"), video, outdir, "--model", model, "--lang", lang, "--freeze", str(freeze)]
    if no_whisper: cmd.append("--no-whisper")
    holds_path = None
    if holds is not None:
        holds_path = os.path.join(outdir, "holds.mcp.json")
        json.dump(holds, open(holds_path, "w"))
        cmd.extend(["--holds", holds_path])
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=600, stdin=subprocess.DEVNULL)
    except Exception as e:
        return {"pass": False, "errors": [str(e)]}
    metrics = None
    try: metrics = json.loads((r.stdout or "").strip().splitlines()[-1])
    except Exception: pass
    errors = [] if r.returncode == 0 and metrics else [((r.stderr or r.stdout or "critic pack failed").strip()[-500:])]
    return {"pass": not errors and bool(metrics.get("gate_pass")), "errors": errors, "metrics": metrics, "gate_pass": bool(metrics and metrics.get("gate_pass")), "outdir": os.path.abspath(outdir)}

@mcp.resource("skill://{path}")
def read_skill_file(path: str) -> str:
    """Read a root markdown file inside the skill repository; path traversal is rejected."""
    return _read_markdown(path)

@mcp.resource("skill://{directory}/{path}")
def read_skill_nested_file(directory: str, path: str) -> str:
    """Read a markdown file one level inside the skill repository; path traversal is rejected."""
    return _read_markdown(directory, path)

def main():
    mcp.run()

if __name__ == "__main__":
    main()
