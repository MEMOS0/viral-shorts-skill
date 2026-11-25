"""Deterministic local semantic-ish search over the skill's references, examples and hook library.
No network or external embedding API: lowercase word/character-ngram hashing + cosine. It is meant
for retrieval inside the skill, not as a claim of state-of-the-art embeddings."""
import math, os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILES = []
for d in ("references", "examples", "data"):
    for n in os.listdir(os.path.join(ROOT, d)):
        if n.endswith(".md") and (d != "data" or n in ("hooks_library.md", "analysis_summary.md")): FILES.append(os.path.join(ROOT, d, n))
def tokens(s): return re.findall(r"[a-z0-9]{2,}", s.lower())
def vec(s):
    v = {}
    for w in tokens(s):
        for x in (w, *(w[i:i+3] for i in range(max(0, len(w)-2)))):
            v[x] = v.get(x, 0.0) + (1.0 if x == w else 0.35)
    n = math.sqrt(sum(x*x for x in v.values())) or 1
    return {k:x/n for k,x in v.items()}
def cos(a,b):
    small,large=(a,b) if len(a)<len(b) else (b,a)
    return sum(x*large.get(k,0) for k,x in small.items())
def chunks():
    for path in FILES:
        rel=os.path.relpath(path,ROOT).replace(os.sep,'/')
        parts=re.split(r"\n(?=#+\s)|\n\s*\n",open(path,encoding='utf8').read())
        for i,p in enumerate(parts):
            p=re.sub(r"\s+"," ",p).strip()
            if len(p)>45: yield dict(source=rel,section=i,text=p[:900],vec=vec(p))
def search(query,limit=5):
    q=vec(query); rows=[]
    for c in chunks(): rows.append(dict(score=round(cos(q,c['vec']),4),source=c['source'],section=c['section'],excerpt=c['text'][:420]))
    return sorted(rows,key=lambda x:x['score'],reverse=True)[:limit]
