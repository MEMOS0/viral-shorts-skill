import json, os, subprocess, sys
import numpy as np
import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import aggregate, critic_pack, find_archive, hookscore_story, motion_features, scout, stats_util

def ent(n):
    return [dict(id=f"v{i}", view_count=1000 * (n - i)) for i in range(n)]

@pytest.mark.parametrize("n", [16, 17, 25, 150])
def test_scout_tiers_disjoint(n):
    sel = scout.tiers(ent(n))
    ids = [e["id"] for _, e in sel]
    assert len(ids) == len(set(ids)) == 16
    top = {e["id"] for t, e in sel if t == "top"}; low = {e["id"] for t, e in sel if t == "low"}
    assert min(e["view_count"] for t, e in sel if t == "top") > max(e["view_count"] for t, e in sel if t == "mid") > max(e["view_count"] for t, e in sel if t == "low")
    assert len(top) == 6 and len(low) == 5

def test_scout_skips_small_channel():
    assert scout.tiers(ent(15)) == []

def test_shipped_pick_overlap_is_resolved_to_first_tier():
    pick, conflicts = aggregate.load_pick(os.path.join(ROOT, "data", "pick2.json"))
    assert {c[0] for c in conflicts} <= {"v_GaWFQ0H7s", "00_dmzXpCco"}
    for i, first, _ in conflicts:
        assert pick[i]["tier"] == first == "top"

def test_negative_values_compare_correctly():
    # louder (-12 LUFS) must be "higher" than quieter (-16 LUFS); the old x1.1 rule inverted this
    d = stats_util.cliffs_delta([-12, -12.5, -13], [-16, -16.5, -17])
    assert d == 1.0

def test_binary_features_use_share_not_median():
    assert aggregate.stat([1, 0, 0, 0], "hook_number") == 0.25
    assert aggregate.stat([1, 0, 0, 0], "wpm") == 0

def test_bootstrap_ci_is_seeded_and_brackets_effect():
    a, b = list(range(10, 30)), list(range(0, 20))
    ci1 = stats_util.bootstrap_ci(stats_util.cliffs_delta, [a, b]); ci2 = stats_util.bootstrap_ci(stats_util.cliffs_delta, [a, b])
    assert ci1 == ci2 and ci1[0] < stats_util.cliffs_delta(a, b) < ci1[1]

def test_sign_test_and_bh():
    assert stats_util.sign_test([1] * 10) < 0.01
    assert stats_util.sign_test([1, -1] * 5) == 1.0
    q = stats_util.bh([0.01, 0.02, 0.5])
    assert q[0] <= q[1] <= q[2] <= 1

@pytest.mark.parametrize("lic,ok", [("CC BY-ND 2.0", False), ("CC BY-NC-SA 3.0", False), ("CC BY 2.0", True), ("CC BY-SA 4.0", True),
                                    ("Public domain", True), ("PD-USGov", True), ("CC cc0 1.0", True), ("CC pdm 1.0", True),
                                    ("CC by-nd 4.0", False), ("", False), ("Copyrighted, used under fair use", False),
                                    ("No known restrictions on publication.", True), ("Permission required", False)])
def test_licence_classifier(lic, ok):
    assert (find_archive.classify_licence(lic) is not None) == ok

def test_internet_archive_is_a_source():
    assert "internet_archive" in [f.__name__ for f in find_archive.SRC]

def test_freeze_parsing_and_classification():
    txt = "lavfi.freezedetect.freeze_start: 2.0\nfreeze_duration: 0.7\nfreeze_start: 10.0\nfreeze_duration: 3.0\nfreeze_start: 20.5"
    fr = critic_pack.parse_freezes(txt)
    assert fr == [(2.0, 0.7), (10.0, 3.0), (20.5, None)]
    planned, unplanned = critic_pack.classify_freezes(fr, [[9.9, 13.1]], 0.5, total=22.0)
    assert planned == [[10.0, 3.0]] and unplanned == [[2.0, 0.7], [20.5, 1.5]]

def test_hookscore_returns_props_and_int():
    p, s = hookscore_story.score("One missing hyphen destroyed an $18 million rocket.")
    assert isinstance(p, dict) and 0 <= s <= 100

def test_motion_features_detects_soft_change_without_cut():
    fps = 10; n = 40
    fr = np.zeros((n, 32, 18, 3), np.float32)
    for i in range(n): fr[i] += min(255, i * 4)  # slow fade: no hard cut, but visible change
    f = motion_features.features(fr, fps)
    assert f["hard_cuts"] == 0 and f["static_share"] < 1

FF = subprocess.run(["ffmpeg", "-version"], capture_output=True).returncode == 0 if os.system("ffmpeg -version >" + os.devnull + " 2>&1") == 0 else False

@pytest.mark.skipif(not FF, reason="ffmpeg not installed")
def test_critic_pack_end_to_end(tmp_path):
    v = tmp_path / "t.mp4"
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "lavfi", "-i", "color=c=red:s=1080x1920:d=2", "-f", "lavfi", "-i", "color=c=blue:s=1080x1920:d=2",
                    "-f", "lavfi", "-i", "sine=f=440:d=4", "-filter_complex", "[0][1]concat=n=2:v=1[v]", "-map", "[v]", "-map", "2", "-shortest",
                    "-c:v", "libx264", "-pix_fmt", "yuv420p", "-c:a", "aac", str(v)], check=True)
    met = critic_pack.main([str(v), str(tmp_path / "c"), "--no-whisper"])
    assert 1.8 < met["cuts"][0] < 2.2
    assert met["freezes_unplanned"]  # static colour = frozen; must be reported, not hidden
    for f in ("proxy.mp4", "contact_2fps.jpg", "first3s_10fps.jpg", "metrics.json", "pack.md"):
        assert (tmp_path / "c" / f).exists()
