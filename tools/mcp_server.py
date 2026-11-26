"""MCP server exposing the viral-shorts production gates to AI agents.
Run: python tools/mcp_server.py  (stdio MCP transport). Requires `mcp<2`.
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mcp.server.fastmcp import FastMCP
import calibrate, check_storyboard, hookscore_story, package_lint, schema_validate, semantic_search, topic_gate, trend_scan

ROOT = os.path.abspath(os.environ.get("VIRAL_SHORTS_ROOT") or os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
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

@mcp.resource("skill://{path}")
def read_skill_file(path: str) -> str:
    """Read a markdown file inside the skill repository; path traversal is rejected."""
    p = os.path.abspath(os.path.join(ROOT, path))
    if not p.startswith(os.path.abspath(ROOT) + os.sep) or not p.endswith(".md") or not os.path.isfile(p): raise ValueError("not a markdown file inside the skill")
    return open(p, encoding="utf-8").read()

def main():
    mcp.run()

if __name__ == "__main__":
    main()
