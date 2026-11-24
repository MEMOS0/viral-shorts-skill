import copy, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "tools"))
import topic_gate as G

U = "https://example.org/"
def angle(i, s=4, **kw):
    a = dict(id=f"a{i}", hook="h", payoff="p", closest_existing=U + "x", scores={k: s for k in G.ANGLE_KEYS}, confidence={k: "high" for k in G.ANGLE_KEYS})
    a.update(kw); return a
def topic(i, s=4, **kw):
    t = dict(id=f"t{i}", title=f"T{i}", scores={k: s for k in G.TOPIC_KEYS}, confidence={k: "high" for k in G.TOPIC_KEYS},
             evidence=dict(existing_shorts=[dict(url=U + "s", views=900_000, channel_median=90_000)], long_form=[dict(url=U + "l", views=2_000_000, channel_median=400_000)],
                           sources=[dict(url=U + "r", type="primary"), dict(url=U + "n", type="secondary")],
                           archive=[dict(url=U + "a", licence="PD"), dict(url=U + "b", licence="CC BY")]),
             angles=[angle(j) for j in range(3)])
    t.update(kw); return t
def disc(n=5): return dict(topics=[topic(i) for i in range(n)])
CRIT = {f"t{i}": dict(verdict="pass") for i in range(6)}

def test_passes_with_evidence_and_critic():
    r = G.evaluate(disc(), CRIT)
    assert r["status"] == "PASS" and r["selected"]["id"] and r["runner_up"]

def test_blocks_without_critic():
    assert G.evaluate(disc())["status"] == "AWAITING_CRITIC"

def test_blocks_with_too_few_topics_or_angles():
    assert G.evaluate(disc(4), CRIT)["status"] == "BLOCK"
    d = disc(); [t.update(angles=t["angles"][:2]) for t in d["topics"]]
    assert G.evaluate(d, CRIT)["status"] == "BLOCK"

def test_non_compensatory_one_weak_component_fails():
    d = disc(); d["topics"][0]["scores"]["facts"] = 2  # everything else 4: an average would still pass
    row = [r for r in G.evaluate(d, CRIT)["ranking"] if r["id"] == "t0"][0]
    assert not row["ok"] and any("facts" in f for f in row["topic"]["fails"])

def test_low_confidence_is_penalised():
    d = disc(); d["topics"][0]["confidence"] = {k: "low" for k in G.TOPIC_KEYS}
    row = [r for r in G.evaluate(d, CRIT)["ranking"] if r["id"] == "t0"][0]
    assert row["topic"]["score"] < [r for r in G.evaluate(disc(), CRIT)["ranking"] if r["id"] == "t1"][0]["topic"]["score"]

def test_demand_needs_two_evidence_types_with_urls():
    d = disc(); d["topics"][0]["evidence"]["long_form"] = []
    row = [r for r in G.evaluate(d, CRIT)["ranking"] if r["id"] == "t0"][0]
    assert not row["ok"] and row["topic"]["eff"]["demand"] <= 2

def test_gap_without_demand_is_not_a_gap():
    d = disc(); ev = d["topics"][0]["evidence"]; ev["existing_shorts"] = []; ev["long_form"] = []
    row = [r for r in G.evaluate(d, CRIT)["ranking"] if r["id"] == "t0"][0]
    assert any("not a gap" in f for f in row["topic"]["fails"])

def test_saturated_topic_needs_novel_angle():
    d = disc(); d["topics"][0]["evidence"]["existing_shorts"] = [dict(url=U + str(i), views=2_000_000, channel_median=1e6) for i in range(5)]
    for a in d["topics"][0]["angles"]: a["scores"]["novelty"] = 3
    row = [r for r in G.evaluate(d, CRIT)["ranking"] if r["id"] == "t0"][0]
    assert not row["ok"] and row["topic"]["eff"]["gap"] <= 2
    for a in d["topics"][0]["angles"]: a["scores"]["novelty"] = 5
    d["topics"][0]["scores"]["gap"] = 5
    row = [r for r in G.evaluate(d, CRIT)["ranking"] if r["id"] == "t0"][0]
    assert not any("novelty" in f for f in row["angle"]["fails"])

def test_critic_rejection_blocks_topic():
    c = copy.deepcopy(CRIT); c["t0"] = dict(verdict="reject", reasons=["already viral last month"])
    row = [r for r in G.evaluate(disc(), c)["ranking"] if r["id"] == "t0"][0]
    assert not row["ok"]

def test_cli_exit_code(tmp_path):
    import json
    p = tmp_path / "d.json"; p.write_text(json.dumps(disc(3)))
    assert G.main([str(p), "--out", str(tmp_path)]) == 2 and (tmp_path / "discovery_report.md").exists()

def test_low_demand_blocks_even_if_everything_else_is_perfect():
    for dem in (1, 2):
        d = disc(); d["topics"][0]["scores"] = {k: 5 for k in G.TOPIC_KEYS}; d["topics"][0]["scores"]["demand"] = dem
        row = [r for r in G.evaluate(d, CRIT)["ranking"] if r["id"] == "t0"][0]
        assert not row["ok"] and any("demand" in f for f in row["topic"]["fails"])
    d = disc(); [t["scores"].update(demand=1) for t in d["topics"]]
    assert G.evaluate(d, CRIT)["status"] == "BLOCK"
