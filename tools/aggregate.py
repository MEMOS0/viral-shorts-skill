"""Aggregate analyze_shorts.py output into data/analysis_summary.md.
Compares TOP vs MID vs LOW tiers *within each channel* (controls for channel size) to avoid survivorship bias.
usage: python aggregate.py pick2.json full.json outdir
"""
import json,re,sys,statistics as S,collections as C
pick={p["id"]:p for p in json.load(open(sys.argv[1]))};out=sys.argv[3]
d=[]
for x in json.load(open(sys.argv[2])):
    if x["id"] in pick and x.get("dur"): x.update(pick[x["id"]]); d.append(x)
med=lambda a:round(S.median(a),2) if a else None
def feats(x):
    D=x["dur"];w=x["words"];h=x.get("hook","").lower()
    late=[t for t in w if t[1]>D*.25]
    def first(m):
        for i,t in enumerate(w):
            if t[1]>D*.25 and " ".join(y[0].lower().strip(".,!?") for y in w[i:i+len(m.split())])==m: return 100*t[1]/D
    return dict(dur=D,cuts_per_10s=10*x["ncuts"]/D,med_shot=x["med_shot"],first_cut=x["first_cut"],first_word=x["first_word"],wpm=x["wpm"],lufs=x["lufs"],
        loopdiff=x["loopdiff"],hook_words=len(h.split()),hook_number=int(bool(re.search(r"\d|\b(one|two|three|four|five|ten|hundred|thousand|million|billion)\b",h))),
        hook_you=int(bool(re.search(r"\byou\b|\byour\b",h))),hook_question=int("?" in h or bool(re.match(r"\s*(what|why|how|did|have|can|would|is|do)\b",h))),
        hook_this=int(bool(re.match(r"\s*(this|these|that)\b",h))),hook_I=int(bool(re.search(r"\b(i|i'm|my|we)\b",h))),
        but_pos=first("but"),silence_gaps=sum(1 for i in range(1,len(w)) if w[i][1]-w[i-1][2]>1),
        end_word_rate=len([t for t in w if t[1]>D*.9])/max(D*.1,1),start_word_rate=len([t for t in w if t[1]<D*.1])/max(D*.1,1))
F=[(x,feats(x)) for x in d];keys=list(F[0][1])
L=[f"# Measured analysis — {len(d)} Shorts, {len({x['ch'] for x in d})} channels, tiered within channel\n",
"Sample: for each channel, from its latest ~150 Shorts (newest 10 dropped because their views are not settled), the 6 most-viewed (TOP), 5 around the median (MID) and 5 least-viewed (LOW). Comparing tiers *inside the same channel* controls for channel size and audience; it shows what separates a channel's hits from its misses, not what makes a channel big.\n",
"## 1. Tier comparison (median of each metric)\n","| Metric | TOP | MID | LOW | TOP vs LOW |","|---|---|---|---|---|"]
for k in keys:
    v={t:[f[k] for x,f in F if x["tier"]==t and f[k] is not None] for t in("top","mid","low")}
    if k.startswith("hook_") and k!="hook_words": m={t:round(100*S.mean(v[t]),0) if v[t] else None for t in v};fmt=lambda a:f"{a:.0f} %"
    else: m={t:med(v[t]) for t in v};fmt=lambda a:f"{a}"
    diff="" if None in(m["top"],m["low"]) else ("higher" if m["top"]>m["low"]*1.1+0.001 else "lower" if m["top"]<m["low"]*0.9-0.001 else "≈ same")
    L.append(f"| {k} | {fmt(m['top'])} | {fmt(m['mid'])} | {fmt(m['low'])} | {diff} |")
L+=["\n## 2. Within-channel paired difference (TOP median − LOW median per channel; share of channels where TOP > LOW)\n","| Metric | Channels | Median diff | TOP > LOW in |","|---|---|---|---|"]
g=C.defaultdict(lambda:C.defaultdict(list))
for x,f in F: g[x["ch"]][x["tier"]].append(f)
for k in keys:
    ds=[]
    for ch,t in g.items():
        a=[f[k] for f in t["top"] if f[k] is not None];b=[f[k] for f in t["low"] if f[k] is not None]
        if a and b: ds.append(S.median(a)-S.median(b))
    if ds: L.append(f"| {k} | {len(ds)} | {round(S.median(ds),2)} | {sum(x>0 for x in ds)}/{len(ds)} |")
L+=["\n## 3. Duration distribution (all tiers)\n","| Duration | TOP | MID | LOW |","|---|---|---|---|"]
for a,b in[(0,20),(20,35),(35,45),(45,60),(60,90),(90,181)]:
    L.append(f"| {a}–{b} s | "+" | ".join(str(sum(1 for x,f in F if x['tier']==t and a<=f['dur']<b)) for t in("top","mid","low"))+" |")
L+=["\n## 4. Per channel\n","| Channel | Shorts listed | Channel median views | n analysed | TOP med views | LOW med views |","|---|---|---|---|---|---|"]
for ch,t in sorted(g.items()):
    xs=[x for x in d if x["ch"]==ch]
    L.append(f"| {ch} | {xs[0]['ch_n']} | {int(xs[0]['ch_median']):,} | {len(xs)} | {int(med([x['views'] for x in xs if x['tier']=='top']) or 0):,} | {int(med([x['views'] for x in xs if x['tier']=='low']) or 0):,} |")
open(f"{out}/analysis_summary.md","w",encoding="utf-8").write("\n".join(L))
H=["# Hook library — first 3 s of every analysed Short\n","| Tier | Channel | Views | Title | First word s | First cut s | Dur s | Spoken hook (0–3 s) |","|---|---|---|---|---|---|---|---|"]
for x in sorted(d,key=lambda x:(x["ch"],-x["views"])):
    H.append(f"| {x['tier']} | {x['ch']} | {x['views']:,} | {x['title'][:60].replace('|','/')} | {x['first_word']} | {x['first_cut']} | {x['dur']} | {x['hook'].replace('|','/')} |")
open(f"{out}/hooks_library.md","w",encoding="utf-8").write("\n".join(H))
print("\n".join(L))
