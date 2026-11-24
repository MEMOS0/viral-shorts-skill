"""Outlier finder for discovery evidence: lists a channel's Shorts or long-form videos and ranks them by
views ÷ channel median (outlier multiple). Optional --search finds videos on a topic across channels.

usage: python outliers.py --channels a,b --tab shorts|videos [--min 3] [--json out.json]
       python outliers.py --search "hyatt regency walkway" [--n 20]
The newest 10 uploads of each channel are excluded (views not settled). Add views/day with fetch_meta.py.
"""
import argparse, json, statistics, subprocess, sys

YT = [sys.executable, "-m", "yt_dlp", "--flat-playlist", "-J", "--no-warnings"]

def channel(h, tab="shorts", limit=200):
    r = subprocess.run(YT + ["--playlist-end", str(limit), f"https://www.youtube.com/@{h}/{tab}"], capture_output=True, text=True, timeout=300)
    if r.returncode != 0: raise RuntimeError(r.stderr[-300:])
    E = [e for e in json.loads(r.stdout).get("entries", []) if e.get("view_count")]
    return E[10:] if len(E) > 40 else E

def rank(E, ch, min_x=0.0):
    if len(E) < 4: return []
    med = statistics.median(e["view_count"] for e in E)
    out = [dict(channel=ch, id=e["id"], title=e.get("title", ""), views=e["view_count"], channel_median=med,
                multiple=round(e["view_count"] / med, 2), url="https://www.youtube.com/watch?v=" + e["id"]) for e in E]
    return sorted([o for o in out if o["multiple"] >= min_x], key=lambda o: -o["multiple"])

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--channels"); ap.add_argument("--tab", default="shorts")
    ap.add_argument("--search"); ap.add_argument("--n", type=int, default=20); ap.add_argument("--min", type=float, default=0.0); ap.add_argument("--json")
    a = ap.parse_args(); res = []
    if a.channels:
        for h in a.channels.split(","):
            try: res += rank(channel(h.strip(), a.tab), h.strip(), a.min)
            except Exception as e: print("FAIL", h, e, file=sys.stderr)
    if a.search:
        r = subprocess.run(YT + [f"ytsearch{a.n}:{a.search}"], capture_output=True, text=True, timeout=300)
        for e in json.loads(r.stdout or "{}").get("entries", []):
            res.append(dict(channel=e.get("channel"), id=e["id"], title=e.get("title"), views=e.get("view_count"), duration=e.get("duration"),
                            url="https://www.youtube.com/watch?v=" + e["id"], note="channel median: run --channels on this channel"))
    for o in res[:50]: print(o.get("multiple", ""), o.get("views"), o["channel"], o["title"][:70], o["url"])
    if a.json: json.dump(res, open(a.json, "w", encoding="utf-8"), indent=1)

if __name__ == "__main__":
    main()
