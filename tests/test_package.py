import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "tools"))
from package_lint import lint

OK = dict(platform="youtube", title="One rod changed. 114 people died.", alt_titles=["a", "b", "c", "d"],
          description="In 1981 a Hyatt Regency walkway in Kansas City fell.\nSources: NBS report (1982).", hashtags=["#engineering", "#hyattregency", "#structuralengineering"],
          tags=["hyatt regency walkway collapse", "hyatt regancy"], keywords=["Hyatt Regency"], withheld_cause="two rods instead of one", cover_text="ONE ROD")

def test_ok_package_passes():
    E, W = lint(OK); assert E == [] and W == []

def test_limits_and_policy():
    E, _ = lint(dict(OK, title="x" * 101)); assert any("100" in e for e in E)
    E, _ = lint(dict(OK, title="You won't believe this bridge")); assert any("bait" in e for e in E)
    E, _ = lint(dict(OK, title="Two rods instead of one killed 114")); assert any("reveals" in e for e in E)
    E, _ = lint(dict(OK, hashtags=["#a"] * 61)); assert any("60" in e for e in E)

def test_instagram_five_hashtags_and_generic():
    p = dict(platform="instagram", caption="Hyatt Regency walkway collapse, 1981.", hashtags=["#a", "#b", "#c", "#d", "#e", "#f"])
    E, _ = lint(p); assert any("> 5" in e for e in E)
    _, W = lint(dict(p, hashtags=["#reels"])); assert any("generic" in w for w in W)
