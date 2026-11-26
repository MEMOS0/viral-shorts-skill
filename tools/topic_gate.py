"""Topic gate: turns a Story Scout discovery file (+ an independent Topic Critic file) into a
PASS / BLOCK decision. Production must not start without gate.json status PASS.

usage: python topic_gate.py discovery.json [--critic critic.json] [--out outdir]
Schema: templates/discovery.json. Scoring is NON-COMPENSATORY: hard gates first, every component
has a floor, low-confidence or evidence-free scores are penalised/capped, and the final rank uses
the weaker of topic and angle, so a great angle cannot rescue a weak topic and vice versa.
"""
import argparse, json, math, os, statistics as S

TOPIC_KEYS = ("demand", "gap", "visual", "clarity", "emotion", "facts", "fit")
ANGLE_KEYS = ("surprise", "stakes", "specificity", "visual_hook", "payoff", "novelty")
DEMAND_TYPES = ("existing_shorts", "long_form", "wikipedia", "trends", "reddit", "comments")
PENALTY = {"high": 0.0, "medium": 0.5, "low": 1.0}
FLOOR, MIN_TOPICS, MIN_ANGLES, PASS_SCORE = 2, 5, 3, 60
# Demand and facts are make-or-break: weak demand cannot be bought back by visuals or emotion.
TOPIC_FLOORS = dict(demand=3, facts=3)

def has_url(x): return isinstance(x, dict) and str(x.get("url", "")).startswith("http")

def demand_evidence(ev):
    """Return (n distinct demand-evidence types with URLs, best outlier multiple, n saturated Shorts)."""
    types = set(); best = 0.0; sat = 0
    for k in DEMAND_TYPES:
        items = ev.get(k) or []
        items = items if isinstance(items, list) else [items]
        if any(has_url(i) for i in items): types.add(k)
    for v in (ev.get("existing_shorts") or []) + (ev.get("long_form") or []):
        if v.get("views") and v.get("channel_median"):
            best = max(best, v["views"] / v["channel_median"])
    sat = sum(1 for v in ev.get("existing_shorts") or [] if (v.get("views") or 0) >= 1_000_000)
    return len(types), round(best, 1), sat

def effective(scores, conf, keys):
    out = {}
    for k in keys:
        s = float(scores.get(k, 0)); out[k] = max(0.0, s - PENALTY.get(conf.get(k, "low"), 1.0))
    return out

def geo100(v):
    """Geometric mean on 0-5 mapped to 0-100: one weak component drags the whole score down."""
    v = list(v)
    if any(x <= 0 for x in v): return 0
    return round(20 * math.exp(S.mean(math.log(x) for x in v)))

def gate_topic(t, critic_view=None):
    ev = t.get("evidence", {}); sc = t.get("scores", {}); cf = t.get("confidence", {}); fails = []
    nd, best, sat = demand_evidence(ev)
    src = [s for s in ev.get("sources", []) if has_url(s)]
    arch = [a for a in ev.get("archive", []) if has_url(a) and a.get("licence")]
    eff = effective(sc, cf, TOPIC_KEYS)
    corrected = (critic_view or {}).get("corrected_scores") or {}
    applied_corrections = {}
    for k in TOPIC_KEYS:
        try:
            if k in corrected and corrected[k] is not None:
                v = max(0.0, min(5.0, float(corrected[k])))
                if v < eff[k]: applied_corrections[k] = v
                eff[k] = min(eff[k], v)
        except (TypeError, ValueError):
            fails.append(f"Topic Critic corrected_scores.{k} is not numeric")
    if nd < 2: eff["demand"] = min(eff["demand"], 2); fails.append(f"demand: {nd} evidence type(s) with URLs, need 2 of {DEMAND_TYPES}")
    if not src or not any(s.get("type") == "primary" for s in src) or len(src) < 2: fails.append("facts: need >= 2 sources incl. 1 primary (report, court record, paper)")
    if len(arch) < 2: eff["visual"] = min(eff["visual"], 2); fails.append(f"visual: {len(arch)} licensed archive item(s), need 2")
    if sat >= 5: eff["gap"] = min(eff["gap"], 2)
    if nd == 0 and eff["gap"] >= 3: fails.append("gap claimed without demand evidence: absence of videos is not a gap if nobody searches for it")
    for k in TOPIC_KEYS:
        fl = TOPIC_FLOORS.get(k, FLOOR)
        if eff[k] < fl: fails.append(f"{k}: effective {eff[k]} < floor {fl}")
    for k in ("facts", "clarity"):
        if eff[k] < 3: fails.append(f"{k}: effective {eff[k]} < 3 (hard gate)")
    return dict(score=geo100(eff.values()), eff=eff, fails=fails, demand_types=nd, best_outlier=best, saturated_shorts=sat, critic_corrected=applied_corrections)

def gate_angle(a, saturated):
    sc = a.get("scores", {}); cf = a.get("confidence", {}); fails = []
    eff = effective(sc, cf, ANGLE_KEYS)
    for k in ANGLE_KEYS:
        if eff[k] < FLOOR: fails.append(f"{k}: effective {eff[k]} < floor {FLOOR}")
    if not a.get("hook") or not a.get("payoff"): fails.append("hook and payoff lines are required")
    if saturated >= 5 and eff["novelty"] < 4: fails.append(f"{saturated} Shorts >= 1M views exist: novelty must be >= 4")
    if saturated >= 1 and not has_url({"url": a.get("closest_existing", "")}): fails.append("closest_existing URL required (prove the angle differs)")
    return dict(score=geo100(eff.values()), eff=eff, fails=fails)

def evaluate(disc, critic=None):
    topics = disc.get("topics", []); critic = critic or {}; rows = []; block = []
    if len(topics) < MIN_TOPICS: block.append(f"only {len(topics)} candidate topics, need >= {MIN_TOPICS}")
    for t in topics:
        cv = critic.get(t.get("id"), {})
        g = gate_topic(t, cv); angles = t.get("angles", [])
        if len(angles) < MIN_ANGLES: g["fails"].append(f"only {len(angles)} angles, need >= {MIN_ANGLES}")
        ar = sorted(((a, gate_angle(a, g["saturated_shorts"])) for a in angles), key=lambda x: (not x[1]["fails"], x[1]["score"]), reverse=True)
        best = ar[0] if ar else (None, dict(score=0, fails=["no angle"], eff={}))
        crit = cv.get("verdict")
        if crit != "pass": g["fails"].append("Topic Critic: " + ("no independent review" if not crit else "rejected: " + "; ".join(cv.get("reasons", []))))
        ok = not g["fails"] and not best[1]["fails"] and g["score"] >= PASS_SCORE and best[1]["score"] >= PASS_SCORE
        rows.append(dict(id=t.get("id"), title=t.get("title"), topic=g, angle_id=(best[0] or {}).get("id"), angle=best[1],
                         rank=min(g["score"], best[1]["score"]), ok=ok, angles=[(a.get("id"), r["score"], r["fails"]) for a, r in ar]))
    rows.sort(key=lambda r: (r["ok"], r["rank"], r["topic"]["score"] + r["angle"]["score"]), reverse=True)
    passing = [r for r in rows if r["ok"]]
    if not passing: block.append("no topic passes every gate")
    status = "PASS" if not block else ("AWAITING_CRITIC" if not critic and topics else "BLOCK")
    return dict(status=status, block=block, selected=passing[0] if passing and not block else None,
                runner_up=passing[1] if len(passing) > 1 and not block else None, ranking=rows)

def report(res):
    L = [f"# Discovery gate: {res['status']}\n"] + [f"- BLOCK: {b}" for b in res["block"]]
    L += ["\n| Rank | Topic | Topic score | Best angle | Angle score | Demand evidence types | Best outlier x | Saturated Shorts | Gate |", "|---|---|---|---|---|---|---|---|---|"]
    for i, r in enumerate(res["ranking"], 1):
        t = r["topic"]
        L.append(f"| {i} | {r['title']} | {t['score']} | {r['angle_id']} | {r['angle']['score']} | {t['demand_types']} | {t['best_outlier']} | {t['saturated_shorts']} | {'PASS' if r['ok'] else 'fail'} |")
    for r in res["ranking"]:
        fs = r["topic"]["fails"] + [f"angle {r['angle_id']}: {f}" for f in r["angle"]["fails"]]
        if fs: L += [f"\n**{r['title']}** fails:"] + [f"- {f}" for f in fs]
    return "\n".join(L) + "\n"

def main(argv=None):
    ap = argparse.ArgumentParser(); ap.add_argument("discovery"); ap.add_argument("--critic"); ap.add_argument("--out", default=".")
    a = ap.parse_args(argv)
    res = evaluate(json.load(open(a.discovery, encoding="utf-8")), json.load(open(a.critic, encoding="utf-8")) if a.critic else None)
    os.makedirs(a.out, exist_ok=True)
    json.dump(res, open(os.path.join(a.out, "gate.json"), "w", encoding="utf-8"), indent=1)
    open(os.path.join(a.out, "discovery_report.md"), "w", encoding="utf-8").write(report(res))
    print(res["status"], (res["selected"] or {}).get("title"))
    return 0 if res["status"] == "PASS" else 2

if __name__ == "__main__":
    raise SystemExit(main())
