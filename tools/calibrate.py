"""Does the gate / critic / QA score predict real results? Run on your own published videos.

usage: python calibrate.py data/calibration.csv
CSV columns (header required): video_id, publish_date, topic_score, angle_score, critic_qa, critic_viral,
views_7d, channel_median_7d, viewed_vs_swiped, avg_pct_viewed   (empty cells allowed)
Outcome = views_7d ÷ channel_median_7d (outlier multiple at the same age, so videos of different age compare).
"""
import csv, math, os, statistics as S, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from stats_util import bootstrap_ci, spearman

PRED = ("topic_score", "angle_score", "critic_qa", "critic_viral")
OUT = ("multiple", "viewed_vs_swiped", "avg_pct_viewed")

def num(x):
    try: return float(x)
    except (TypeError, ValueError): return None

def run(rows):
    for r in rows:
        v, m = num(r.get("views_7d")), num(r.get("channel_median_7d"))
        r["multiple"] = math.log(v / m) if v and m else None
    res = {}
    for p in PRED:
        for o in OUT:
            pairs = [(num(r.get(p)), num(r.get(o))) for r in rows]
            pairs = [(x, y) for x, y in pairs if x is not None and y is not None]
            if len(pairs) < 8: continue
            rho = spearman(*zip(*pairs))
            ci = bootstrap_ci(lambda z: spearman([a for a, _ in z], [b for _, b in z]), [pairs])
            res[(p, o)] = (len(pairs), rho, ci)
    return res

def main():
    rows = list(csv.DictReader(open(sys.argv[1], encoding="utf-8")))
    res = run(rows)
    print("| Predictor | Outcome | n | Spearman rho | 95 % CI | Reading |\n|---|---|---|---|---|---|")
    for (p, o), (n, rho, ci) in res.items():
        ok = ci[0] is not None and ci[0] > 0
        print(f"| {p} | {o} | {n} | {rho:+.2f} | [{ci[0]:+.2f}, {ci[1]:+.2f}] | {'predicts (keep weights)' if ok else 'no evidence it predicts: revise or stop using for selection'} |")
    if not res: print("need >= 8 videos with both a score and an outcome")

if __name__ == "__main__":
    main()
