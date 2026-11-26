"""Validate a machine-readable storyboard (templates/storyboard.json) BEFORE rendering.

usage: python check_storyboard.py storyboard.json [--words words.json] [--gate gate.json]
Checks: discovery gate PASS; contiguous shots covering the narration; every shot has purpose, type,
visual and asset ids; no asset reused; archive shots carry a source label and a licence; Blender /
reconstruction shots carry the RECONSTRUCTION badge; no shot longer than max_static_s without a
move or reveal; first visual change before first_change_s; captions align with word timestamps;
holds are declared (they become holds.json for critic_pack.py). Exit 0 = pass, 1 = errors.
"""
import argparse, json, os, sys

TYPES = {"archive", "document", "blender", "diagram", "map", "graph", "text", "brand"}
BEATS = {"hook", "context", "escalation", "turn", "payoff", "cta"}
RECON = "RECONSTRUCTION: FIRSTENGINEER"

def check(sb, words=None, gate=None):
    E, W = [], []
    rules = dict(max_static_s=3.0, first_change_s=4.0, caption_tol_s=0.15, max_text_share=0.3); rules.update(sb.get("rules", {}))
    if gate is not None and gate.get("status") != "PASS": E.append(f"discovery gate is {gate.get('status')}, not PASS: no production")
    shots = sb.get("shots", []); dur = sb.get("duration")
    if not shots: return ["no shots"], W
    t = 0.0; seen = {}; text = 0.0
    for s in shots:
        sid = s.get("id", "?"); a, b = s.get("start"), s.get("end")
        if a is None or b is None or b <= a: E.append(f"{sid}: bad start/end"); continue
        if abs(a - t) > 0.04: E.append(f"{sid}: gap/overlap at {t:.2f}–{a:.2f}")
        t = b
        if not str(s.get("purpose", "")).strip(): E.append(f"{sid}: no purpose (what the viewer learns or feels)")
        if s.get("type") not in TYPES: E.append(f"{sid}: type {s.get('type')!r} not in {sorted(TYPES)}")
        for asset in s.get("assets", []):
            if asset in seen and not s.get("callback"): E.append(f"{sid}: asset {asset} already used in {seen[asset]} (mark callback=true only for a deliberate loop)")
            seen.setdefault(asset, sid)
        if s.get("type") in ("archive", "document"):
            if not s.get("label"): E.append(f"{sid}: archive shot without on-screen source label")
            if not s.get("licence"): E.append(f"{sid}: archive shot without licence")
        if s.get("type") == "blender" or s.get("reconstruction"):
            if RECON not in (s.get("badge") or ""): E.append(f"{sid}: reconstruction without badge '{RECON}'")
        moves = s.get("moves") or []
        if b - a > rules["max_static_s"] and not moves and not s.get("hold"):
            E.append(f"{sid}: {b - a:.1f} s with no move/reveal (max {rules['max_static_s']} s) — add a motivated move or split")
        if s.get("type") == "text": text += b - a
    beats = [s.get("retention_beat") for s in shots]
    if any(beat is not None for beat in beats):
        for s, beat in zip(shots, beats):
            if beat not in BEATS: E.append(f"{s.get('id', '?')}: retention_beat must be one of {sorted(BEATS)}")
        if beats and beats[0] != "hook": E.append("retention map: first shot must be the hook beat")
        if beats and beats[-1] not in ("payoff", "cta"): E.append("retention map: final shot must be payoff or cta")
        if not any(beat in ("escalation", "turn") for beat in beats): E.append("retention map: needs at least one escalation or turn beat")
        ending = len(shots) - (2 if beats and beats[-1] == "cta" else 1)
        payoff_indexes = [i for i, beat in enumerate(beats) if beat == "payoff"]
        if payoff_indexes and min(payoff_indexes) < ending: E.append("retention map: payoff arrives before the ending; later shots would deflate retention")
    if dur and abs(t - dur) > 0.1: E.append(f"shots end at {t:.2f} s, duration is {dur}")
    if shots[0]["end"] > rules["first_change_s"] and not shots[0].get("moves"): E.append(f"first visual change after {rules['first_change_s']} s")
    if t and text / t > rules["max_text_share"]: W.append(f"text cards are {100 * text / t:.0f} % of runtime (slideshow risk)")
    if words:
        starts = [w["s"] if isinstance(w, dict) else w[1] for w in words]
        for c in sb.get("captions", []):
            near = min((abs(c["start"] - x) for x in starts), default=9)
            if near > rules["caption_tol_s"]: E.append(f"caption '{c.get('text', '')[:20]}' at {c['start']} s is {near:.2f} s from any spoken word")
        if starts and starts[0] > 0.3: W.append(f"first word at {starts[0]:.2f} s (target ≤ 0.3 s)")
    return E, W

def holds(sb):
    return [[s["start"], s["end"]] for s in sb.get("shots", []) if s.get("hold")]

def main(argv=None):
    ap = argparse.ArgumentParser(); ap.add_argument("storyboard"); ap.add_argument("--words"); ap.add_argument("--gate")
    a = ap.parse_args(argv)
    sb = json.load(open(a.storyboard, encoding="utf-8"))
    E, W = check(sb, json.load(open(a.words, encoding="utf-8")) if a.words else None, json.load(open(a.gate, encoding="utf-8")) if a.gate else None)
    json.dump(holds(sb), open(os.path.join(os.path.dirname(os.path.abspath(a.storyboard)), "holds.json"), "w"))
    for w in W: print("WARN", w)
    for e in E: print("ERROR", e)
    print("PASS" if not E else f"FAIL ({len(E)} errors)")
    return 0 if not E else 1

if __name__ == "__main__":
    raise SystemExit(main())
