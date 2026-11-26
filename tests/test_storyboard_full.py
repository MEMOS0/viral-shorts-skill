import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "tools"))
import check_storyboard as C

def sb():
    return json.load(open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "templates", "storyboard.json"), encoding="utf8"))

def test_retention_map_template_passes_shape():
    errors, warnings = C.check(sb())
    assert not any("retention map" in e or "retention_beat" in e for e in errors)

def test_partial_or_wrong_retention_map_fails():
    x = sb(); x["shots"][1].pop("retention_beat")
    errors, warnings = C.check(x)
    assert any("retention_beat" in e for e in errors)
    x = sb(); x["shots"][0]["retention_beat"] = "context"
    errors, warnings = C.check(x)
    assert any("first shot must be the hook" in e for e in errors)

def test_payoff_must_not_arrive_before_later_deflation():
    x = sb(); x["shots"][0]["retention_beat"] = "payoff"
    errors, warnings = C.check(x)
    assert any("first shot must be the hook" in e for e in errors)
