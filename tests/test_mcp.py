import json, os, subprocess, sys
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
    assert reloaded.semantic_search.root() == reloaded.os.path.abspath("/tmp/skill-root")
    assert reloaded.schema_validate.root() == reloaded.os.path.abspath("/tmp/skill-root")
    monkeypatch.delenv("VIRAL_SHORTS_ROOT")
    importlib.reload(reloaded)

def test_mcp_server_stdio_initialize_and_call_tool():
    import asyncio
    from mcp import ClientSession
    from mcp.client.stdio import StdioServerParameters, stdio_client

    async def run():
        script = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "tools", "mcp_server.py")
        params = StdioServerParameters(command=sys.executable, args=[script])
        async with stdio_client(params) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                tools = await session.list_tools()
                result = await session.call_tool("lint_package", {"package": {"platform": "youtube", "title": "x", "description": "sources", "hashtags": ["#engineering"], "alt_titles": ["a", "b", "c", "d"]}})
                return tools, result

    tools, result = asyncio.run(run())
    assert "lint_package" in {t.name for t in tools.tools}
    assert json.loads(result.content[0].text)["pass"]


def test_mcp_server_reads_nested_markdown_resource():
    import asyncio
    from mcp import ClientSession
    from mcp.client.stdio import StdioServerParameters, stdio_client
    from pydantic import AnyUrl

    async def run():
        script = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "tools", "mcp_server.py")
        params = StdioServerParameters(command=sys.executable, args=[script])
        async with stdio_client(params) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                return await session.read_resource(AnyUrl("skill://references/01-platforms.md"))

    result = asyncio.run(run())
    assert "YouTube" in result.contents[0].text

def test_mcp_critic_pack_builds_real_postrender_evidence(tmp_path):
    import subprocess
    import mcp_server

    video = tmp_path / "in.mp4"
    outdir = tmp_path / "critic"
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "lavfi", "-i", "testsrc=duration=1:size=64x64:rate=10", "-pix_fmt", "yuv420p", str(video)], check=True)
    result = mcp_server.build_critic_pack(str(video), str(outdir), no_whisper=True)
    assert result["pass"] and result["gate_pass"] and result["metrics"]["duration"] == 1.0
    assert (outdir / "proxy.mp4").exists() and (outdir / "metrics.json").exists()

def test_critic_pack_subprocesses_do_not_inherit_stdio(monkeypatch):
    import subprocess
    import critic_pack

    calls = []
    class Result:
        returncode = 0
        stdout = ""
        stderr = ""
    def fake_run(*args, **kwargs):
        calls.append(kwargs)
        return Result()
    monkeypatch.setattr(subprocess, "run", fake_run)
    critic_pack.sh("ffmpeg", "-version")
    assert calls[0]["stdin"] is subprocess.DEVNULL



def test_mcp_critic_pack_subprocess_does_not_inherit_stdio(monkeypatch, tmp_path):
    import mcp_server
    video = tmp_path / "in.mp4"
    video.write_bytes(b"x")
    calls = []
    class Result:
        returncode = 0
        stdout = '{"gate_pass": true, "duration": 1.0}\n'
        stderr = ""
    def fake_run(*args, **kwargs):
        calls.append(kwargs)
        return Result()
    monkeypatch.setattr(subprocess, "run", fake_run)
    result = mcp_server.build_critic_pack(str(video), str(tmp_path / "critic"), no_whisper=True)
    assert result["pass"]
    assert calls[0]["stdin"] is subprocess.DEVNULL


def test_installed_wheel_corpus_root_fallback(monkeypatch, tmp_path):
    import skill_root
    package = tmp_path / "site-packages" / "viral_shorts"
    corpus = package / "corpus"
    corpus.mkdir(parents=True)
    (corpus / "SKILL.md").write_text("# skill", encoding="utf-8")
    monkeypatch.delenv("VIRAL_SHORTS_ROOT", raising=False)
    monkeypatch.setattr(skill_root, "__file__", str(package / "skill_root.py"))
    assert skill_root.skill_root() == str(corpus)


def test_corpus_copy_removes_stale_deleted_files(tmp_path):
    import build_corpus
    root = tmp_path / "repo"
    root.mkdir()
    for name in build_corpus.ROOT_FILES:
        (root / name).write_text("# x", encoding="utf-8")
    for name in build_corpus.CORPUS_DIRS:
        (root / name).mkdir()
        (root / name / "stale.md").write_text("old", encoding="utf-8")
    build = tmp_path / "build"
    first = build_corpus.copy_corpus(root, build)
    assert (first / "references" / "stale.md").exists()
    (root / "references" / "stale.md").unlink()
    second = build_corpus.copy_corpus(root, build)
    assert not (second / "references" / "stale.md").exists()
    assert (second / "data" / "stale.md").exists()
