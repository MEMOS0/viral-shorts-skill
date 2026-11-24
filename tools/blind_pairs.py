"""Label-blind story-factor test: pairs one TOP and one LOW Short from the same channel, hides which is
which, and lets a human or a model rate story factors. Then scores whether the ratings pick the hit.

usage: python blind_pairs.py make data/pick2.json data/shorts_full_analysis_v2.json pairs/ [--seed 1]
         -> pairs/pairs.md (raters see this: titles hidden by default, first 25 s transcript per video),
            pairs/key.json (DO NOT give to raters), pairs/ratings_template.csv
       python blind_pairs.py score pairs/ ratings.csv
Rate each video 1–5 on: topic, angle, first_frame (from the contact sheet if available), emotion,
originality, payoff, clarity. The score step reports, per factor, how often the higher-rated video was
the TOP one (50 % = no signal) with an exact binomial p-value.
"""
import argparse, csv, json, math, os, random

FACTORS = ("topic", "angle", "first_frame", "emotion", "originality", "payoff", "clarity")

def make(pick, full, out, seed=1, titles=False, seconds=25):
    P = {}; [P.setdefault(p["id"], p) for p in json.load(open(pick, encoding="utf-8"))]
    A = {x["id"]: x for x in json.load(open(full, encoding="utf-8")) if x["id"] in P}
    rng = random.Random(seed); by = {}
    for i, x in A.items(): by.setdefault(P[i]["ch"], {}).setdefault(P[i]["tier"], []).append(i)
    os.makedirs(out, exist_ok=True); key = {}; md = ["# Blind pairs — rate each video; you are not told which performed better\n"]
    n = 0
    for ch in sorted(by):
        tops, lows = by[ch].get("top", []), by[ch].get("low", [])
        rng.shuffle(tops); rng.shuffle(lows)
        for t, l in zip(tops, lows):
            n += 1; pair = [t, l]; rng.shuffle(pair); key[f"p{n}"] = dict(A=pair[0], B=pair[1], top=t)
            md.append(f"## p{n}")
            for lab, vid in zip("AB", pair):
                x = A[vid]; txt = " ".join(w[0] for w in x["words"] if w[1] < seconds)
                md.append(f"**{lab}** ({x['dur']} s){' — ' + x['title'] if titles else ''}: {txt}\n")
    open(os.path.join(out, "pairs.md"), "w", encoding="utf-8").write("\n".join(md))
    json.dump(key, open(os.path.join(out, "key.json"), "w"), indent=1)
    with open(os.path.join(out, "ratings_template.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f); w.writerow(["pair", "video"] + list(FACTORS))
        for p in key: w.writerow([p, "A"] + [""] * len(FACTORS)); w.writerow([p, "B"] + [""] * len(FACTORS))
    return n

def score(out, ratings):
    key = json.load(open(os.path.join(out, "key.json")))
    R = {}
    for r in csv.DictReader(open(ratings, encoding="utf-8")): R[(r["pair"], r["video"])] = r
    rows = []
    for fct in FACTORS:
        hit = miss = 0
        for p, k in key.items():
            try: a, b = float(R[(p, "A")][fct]), float(R[(p, "B")][fct])
            except (KeyError, ValueError): continue
            if a == b: continue
            hit += (k["A"] if a > b else k["B"]) == k["top"]; miss += (k["A"] if a > b else k["B"]) != k["top"]
        n = hit + miss
        p = min(1.0, 2 * sum(math.comb(n, i) for i in range(min(hit, miss) + 1)) / 2 ** n) if n else 1.0
        rows.append((fct, n, hit, p))
    print("| Factor | decided pairs | picked the TOP | p |\n|---|---|---|---|")
    for f, n, h, p in rows: print(f"| {f} | {n} | {h} ({100 * h / max(n, 1):.0f} %) | {p:.3f} |")
    return rows

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("cmd", choices=["make", "score"]); ap.add_argument("args", nargs="+")
    ap.add_argument("--seed", type=int, default=1); ap.add_argument("--titles", action="store_true")
    a = ap.parse_args()
    if a.cmd == "make": print(make(*a.args[:3], seed=a.seed, titles=a.titles), "pairs")
    else: score(*a.args[:2])
