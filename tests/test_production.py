import copy, csv, json, os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import blind_pairs, calibrate, check_storyboard as C, topic_gate

SB = json.load(open(os.path.join(ROOT, "templates", "storyboard.json"), encoding="utf-8"))

def test_template_storyboard_passes():
    E, W = C.check(SB, words=[{"w": "one", "s": 0.05}], gate={"status": "PASS"})
    assert E == []

def test_storyboard_catches_production_errors():
    sb = copy.deepcopy(SB)
    sb["shots"][0]["purpose"] = ""; sb["shots"][0]["label"] = ""; sb["shots"][1]["badge"] = ""
    sb["shots"][1]["assets"] = ["a01_0"]; sb["shots"][1]["moves"] = []
    E, _ = C.check(sb, gate={"status": "BLOCK"})
    txt = " ".join(E)
    for needle in ("gate", "purpose", "label", "RECONSTRUCTION", "already used", "no move"):
        assert needle in txt, needle

def test_caption_drift_is_an_error():
    E, _ = C.check(SB, words=[{"w": "one", "s": 0.9}])
    assert any("caption" in e for e in E)

def test_holds_export():
    sb = copy.deepcopy(SB); sb["shots"][1]["hold"] = True
    assert C.holds(sb) == [[2.0, 6.0]]

def test_discovery_template_is_blocked_as_is():
    d = json.load(open(os.path.join(ROOT, "templates", "discovery.json"), encoding="utf-8"))
    assert topic_gate.evaluate(d)["status"] != "PASS"

def test_calibrate_detects_signal():
    rows = [dict(topic_score=i, views_7d=1000 * (i + 1), channel_median_7d=1000, critic_qa=50) for i in range(12)]
    res = calibrate.run(rows)
    n, rho, ci = res[("topic_score", "multiple")]
    assert rho > 0.9 and ci[0] > 0

def test_blind_pairs_roundtrip(tmp_path):
    n = blind_pairs.make(os.path.join(ROOT, "data", "pick2.json"), os.path.join(ROOT, "data", "shorts_full_analysis_v2.json"), str(tmp_path))
    assert n >= 80
    key = json.load(open(tmp_path / "key.json"))
    assert all(v["top"] in (v["A"], v["B"]) for v in key.values())
    md = (tmp_path / "pairs.md").read_text(encoding="utf-8")
    assert "top" not in md.lower().split("rate each video")[1][:5]
    with open(tmp_path / "r.csv", "w", newline="", encoding="utf-8") as f:  # an oracle rater must score 100 %
        w = csv.writer(f); w.writerow(["pair", "video"] + list(blind_pairs.FACTORS))
        for p, k in key.items():
            for lab in "AB": w.writerow([p, lab] + [5 if k[lab] == k["top"] else 1] * len(blind_pairs.FACTORS))
    rows = blind_pairs.score(str(tmp_path), str(tmp_path / "r.csv"))
    assert all(h == n_ for _, n_, h, _ in rows)
