import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "tools"))

def test_schema_validation_and_mcp_tools_import():
    import mcp_server, schema_validate
    assert schema_validate.validate("package", {"platform": "youtube", "title": "x", "hashtags": ["#engineering"]}) == []
    assert schema_validate.validate("package", {"platform": "youtube", "hashtags": ["bad tag"]})
    assert mcp_server.validate_json("package", {"platform": "youtube", "title": "x"})["pass"]
    bad = mcp_server.validate_json("storyboard", {"duration": 0, "shots": []})
    assert not bad["pass"] and bad["errors"]

def test_semantic_search_returns_deterministic_relevant_skill_evidence():
    import semantic_search
    a = semantic_search.search("opening hook cause hidden rocket failure", 3)
    b = semantic_search.search("opening hook cause hidden rocket failure", 3)
    assert a == b and len(a) == 3 and a[0]["score"] > 0 and a[0]["source"].endswith(".md")

def test_mcp_hook_and_package_tools():
    import mcp_server
    h = mcp_server.score_hook("One missing hyphen destroyed an $18 million rocket.")
    assert 0 <= h["score"] <= 100
    p = mcp_server.lint_package({"platform": "youtube", "title": "The hyphen that doomed a rocket", "description": "sources", "hashtags": ["#engineering"], "alt_titles": ["a","b","c","d"]})
    assert p["pass"]


def test_mcp_calibration_is_machine_readable():
    import mcp_server
    rows = [dict(topic_score=i, views_7d=1000 * (i + 1), channel_median_7d=1000, critic_qa=50) for i in range(12)]
    r = mcp_server.calibrate_scores(rows)
    hit = next(x for x in r["results"] if x["predictor"] == "topic_score" and x["outcome"] == "multiple")
    assert hit["n"] == 12 and hit["rho"] > 0.9


def test_scan_topic_demand_is_machine_readable(monkeypatch):
    import mcp_server, trend_scan
    monkeypatch.setattr(trend_scan, "scan_topics", lambda topics, **kw: {"topics": [{"id": topics[0]["id"], "summary": {"evidence_types": 3}}]})
    r = mcp_server.scan_topic_demand([{"id": "t", "title": "x"}], days=90)
    assert r["topics"][0]["summary"]["evidence_types"] == 3


def test_console_entrypoint_and_root_override(monkeypatch):
    import importlib, mcp_server
    assert callable(mcp_server.main)
    monkeypatch.setenv("VIRAL_SHORTS_ROOT", "/tmp/skill-root")
    reloaded = importlib.reload(mcp_server)
    assert reloaded.ROOT == reloaded.os.path.abspath("/tmp/skill-root")
    monkeypatch.delenv("VIRAL_SHORTS_ROOT")
    importlib.reload(reloaded)
