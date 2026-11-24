"""Small, dependency-free statistics used by aggregate.py (seeded, so results are reproducible)."""
import math, random, statistics as S

def cliffs_delta(a, b):
    """P(a > b) - P(a < b). 0 = no difference; |d| < 0.147 negligible, < 0.33 small, < 0.474 medium (Romano et al. 2006)."""
    if not a or not b: return None
    gt = lt = 0
    for x in a:
        for y in b:
            gt += x > y; lt += x < y
    return (gt - lt) / (len(a) * len(b))

def bootstrap_ci(fn, groups, n=2000, seed=7, alpha=0.05):
    """Percentile CI of fn(*resampled_groups); each group is resampled with replacement independently."""
    rng = random.Random(seed); vals = []
    for _ in range(n):
        g = [[rng.choice(x) for _ in x] for x in groups]
        v = fn(*g)
        if v is not None: vals.append(v)
    if not vals: return (None, None)
    vals.sort()
    return (vals[int(alpha / 2 * len(vals))], vals[int((1 - alpha / 2) * len(vals)) - 1])

def sign_test(diffs):
    """Two-sided exact binomial sign test, ties dropped."""
    pos = sum(d > 0 for d in diffs); neg = sum(d < 0 for d in diffs); n = pos + neg
    if n == 0: return 1.0
    k = min(pos, neg)
    p = sum(math.comb(n, i) for i in range(k + 1)) / 2 ** n * 2
    return min(1.0, p)

def bh(pvals):
    """Benjamini-Hochberg adjusted p-values (false discovery rate across many metrics)."""
    m = len(pvals); order = sorted(range(m), key=lambda i: pvals[i]); adj = [0.0] * m; prev = 1.0
    for rank, i in reversed(list(enumerate(order, 1))):
        prev = min(prev, pvals[i] * m / rank); adj[i] = prev
    return adj

def spearman(x, y):
    pairs = [(a, b) for a, b in zip(x, y) if a is not None and b is not None]
    if len(pairs) < 5: return None
    def rank(v):
        o = sorted(range(len(v)), key=lambda i: v[i]); r = [0.0] * len(v); i = 0
        while i < len(o):
            j = i
            while j + 1 < len(o) and v[o[j + 1]] == v[o[i]]: j += 1
            for k in range(i, j + 1): r[o[k]] = (i + j) / 2
            i = j + 1
        return r
    rx, ry = rank([p[0] for p in pairs]), rank([p[1] for p in pairs])
    if S.pstdev(rx) == 0 or S.pstdev(ry) == 0: return None
    mx, my = S.mean(rx), S.mean(ry)
    return sum((a - mx) * (b - my) for a, b in zip(rx, ry)) / (len(rx) * S.pstdev(rx) * S.pstdev(ry))

def magnitude(d):
    if d is None: return ""
    a = abs(d)
    return "negligible" if a < 0.147 else "small" if a < 0.33 else "medium" if a < 0.474 else "large"
