"""Fetch upload date, current views, likes and comments for every id in a pick file (yt-dlp, no download).
Needed to normalise views by video age (views/day) and to compute engagement ratios.

usage: python fetch_meta.py pick.json meta.json [--workers 4]
"""
import argparse, json, os, subprocess, sys, datetime as dt
from concurrent.futures import ThreadPoolExecutor

YT = [sys.executable, "-m", "yt_dlp", "--skip-download", "--no-warnings", "-j"]

def one(i):
    try:
        r = subprocess.run(YT + ["https://www.youtube.com/shorts/" + i], capture_output=True, text=True, timeout=120)
        j = json.loads(r.stdout)
    except Exception as e:
        return i, {"error": str(e)[:200]}
    return i, dict(upload_date=j.get("upload_date"), views_now=j.get("view_count"), likes=j.get("like_count"),
                   comments=j.get("comment_count"), duration=j.get("duration"), channel=j.get("channel"),
                   channel_followers=j.get("channel_follower_count"), fetched=dt.date.today().isoformat())

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("pick"); ap.add_argument("out"); ap.add_argument("--workers", type=int, default=4)
    a = ap.parse_args()
    ids = list(dict.fromkeys(p["id"] for p in json.load(open(a.pick, encoding="utf-8"))))
    res = json.load(open(a.out, encoding="utf-8")) if os.path.exists(a.out) else {}
    todo = [i for i in ids if i not in res or "error" in res[i]]
    with ThreadPoolExecutor(a.workers) as ex:
        for k, (i, m) in enumerate(ex.map(one, todo)):
            res[i] = m
            if k % 10 == 0: json.dump(res, open(a.out, "w", encoding="utf-8"), indent=0); print(k, len(todo), flush=True)
    json.dump(res, open(a.out, "w", encoding="utf-8"), indent=0)
    print("METADONE", sum("error" not in v for v in res.values()), "/", len(ids))

if __name__ == "__main__":
    main()
