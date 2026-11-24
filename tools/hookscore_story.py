"""Weakest-link hook score for story Shorts (adapted from youtube-agent-skill hookscore.py, MIT).
usage: python hookscore_story.py hooks.txt | --hook "line" | --validate full.json pick2.json"""
import json,re,sys,statistics as S
VAGUE={"amazing","incredible","insane","crazy","huge","massive","secret","ultimate","unbelievable","shocking","mind","blowing","craziest","wild"}
FILLER={"so","basically","actually","literally","just","really","very","guys","hey","welcome","today","video","subscribe","channel","um","uh"}
NUM=re.compile(r"\b(\d[\d,.]*|one|two|three|four|five|six|seven|eight|nine|ten|twelve|hundred|thousand|million|billion)\b",re.I)
STAKE=re.compile(r"\b(die|died|dead|death|killed|kill|crash|crashed|collapse|collapsed|explode|exploded|sank|fail|failed|lost|lose|burn|fire|disaster|trapped|nobody|everyone|people|city|bomb|million|billion)\b",re.I)
GAP=re.compile(r"\b(but|why|how|until|nobody|only|never|still|except|what|this|then|turns out|wasn't|didn't|couldn't)\b",re.I)
VIS=re.compile(r"\b(this|these|here|look|watch|that)\b",re.I)
def w(t):return re.findall(r"[a-z0-9']+",t.lower())
def props(t):
    x=w(t);n=len(x)or 1;first=" ".join(x[:14])
    spec=34+22*len(NUM.findall(t))-16*sum(a in VAGUE for a in x)-5*sum(a in FILLER for a in x)+min(18,6*sum(1 for y in t.split()[1:] if y[:1].isupper()))
    stake=22+26*len(STAKE.findall(t))
    gap=24+17*len(GAP.findall(t))+(18 if t.strip().endswith("?") else 0)-(18 if re.search(r"\b(because|which means|so that)\b",t,re.I) else 0)
    vis=40+30*bool(VIS.search(first))+15*bool(NUM.search(first))
    k=len(x);brev=100 if 6<=k<=16 else max(30,100-(6-k)*12) if k<6 else max(10,100-(k-16)*6)
    c=lambda v:max(0,min(100,v))
    return dict(SPECIFICITY=c(spec),STAKES=c(stake),GAP=c(gap),VISUAL=c(vis),BREVITY=c(brev))
def score(t):
    p=props(t);v=list(p.values());return p,round(.6*S.mean(v)+.4*min(v))
if __name__=="__main__":
    a=sys.argv[1:]
    if a[:1]==["--validate"]:
        full={x["id"]:x for x in json.load(open(a[1]))};pick=json.load(open(a[2]));g={}
        for p in pick:
            if p["id"] in full and full[p["id"]].get("hook"):g.setdefault(p["tier"],[]).append(score(full[p["id"]]["hook"])[1])
        for t in("top","mid","low"):
            if t in g:print(t,len(g[t]),"median",S.median(g[t]),"mean",round(S.mean(g[t]),1))
        sys.exit()
    L=[a[1]] if a[:1]==["--hook"] else [l for l in open(a[0],encoding="utf-8").read().splitlines() if l.strip()]
    for t in sorted(L,key=lambda t:-score(t)[1]):
        p,v=score(t);lo=min(p,key=p.get)
