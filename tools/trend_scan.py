"""Live demand scanner for Story Scout.

Collects current, linkable demand evidence from public sources without inventing scores:
- Wikipedia pageviews over a trailing window (official Wikimedia REST metrics)
- YouTube search results through yt-dlp
- Reddit top-of-year public search JSON when reachable
- a Google Trends exploration URL, explicitly marked not measured unless the caller verifies it

usage: python trend_scan.py topics.json --out scan.json --discovery-out evidence.json
Input: [{"id":"t1","title":"Hyatt walkway collapse","wikipedia":"Hyatt Regency walkway collapse","query":"hyatt walkway collapse"}]
The output is evidence for a human/agent Story Scout; it never fills discovery scores automatically.
"""
import argparse, datetime as dt, json, subprocess, sys, urllib.parse, urllib.request
from typing import Any

UA = "viral-shorts-skill/1.0 (research; contact: local-user)"
WIKI = "https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/all-agents/{article}/daily/{start}/{end}"
YT = [sys.executable, "-m", "yt_dlp", "--flat-playlist", "-J", "--no-warnings"]


def http_json(url: str, timeout: int = 20) -> dict[str, Any]:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8"))


def wiki_pageviews(article: str, days: int = 90, end: dt.date | None = None) -> dict[str, Any]:
    end = end or dt.date.today()
    start = end - dt.timedelta(days=days - 1)
    slug = urllib.parse.quote(article.replace(" ", "_"), safe="")
    url = WIKI.format(article=slug, start=start.strftime("%Y%m%d"), end=end.strftime("%Y%m%d"))
    data = http_json(url)
    items = data.get("items", [])
    total = sum(int(x.get("views", 0)) for x in items)
    return {
        "url": "https://en.wikipedia.org/wiki/" + slug,
        "api_url": url,
        "article": article,
        "days": days,
        "pageviews_90d": total if days == 90 else total,
        "pageviews_window": total,
        "daily_average": round(total / max(1, len(items)), 1),
    }


def youtube_search(query: str, n: int = 8) -> list[dict[str, Any]]:
    r = subprocess.run(YT + [f"ytsearch{n}:{query}"], capture_output=True, text=True, timeout=180)
    if r.returncode != 0:
        raise RuntimeError(r.stderr[-300:] or "yt-dlp search failed")
    out = []
    for e in json.loads(r.stdout or "{}").get("entries", []):
        if not e.get("id"):
            continue
        out.append({
            "url": "https://www.youtube.com/watch?v=" + e["id"],
            "title": e.get("title", ""),
            "channel": e.get("channel"),
            "views": e.get("view_count"),
            "duration": e.get("duration"),
        })
    return out


def reddit_top(query: str, limit: int = 5) -> list[dict[str, Any]]:
    q = urllib.parse.urlencode({"q": query, "sort": "top", "t": "year", "limit": str(limit), "restrict_sr": "false"})
    data = http_json("https://www.reddit.com/search.json?" + q)
    out = []
    for child in data.get("data", {}).get("children", []):
        d = child.get("data", {})
        if not d.get("permalink"):
            continue
        out.append({
            "url": "https://www.reddit.com" + d["permalink"],
            "title": d.get("title", ""),
            "subreddit": d.get("subreddit"),
            "score": d.get("score", 0),
            "comments": d.get("num_comments", 0),
        })
    return out


def scan_topic(topic: dict[str, Any], days: int = 90, youtube_n: int = 8, reddit_limit: int = 5) -> dict[str, Any]:
    title = str(topic.get("title") or topic.get("id") or "").strip()
    query = str(topic.get("query") or title).strip()
    article = str(topic.get("wikipedia") or title).strip()
    res: dict[str, Any] = {
        "id": topic.get("id") or title.lower().replace(" ", "-"),
        "title": title,
        "query": query,
        "wikipedia": None,
        "youtube": [],
        "reddit": [],
        "trends": {"url": "https://trends.google.com/trends/explore?q=" + urllib.parse.quote(query), "direction": "not_measured"},
        "errors": [],
    }
    if article:
        try:
            res["wikipedia"] = wiki_pageviews(article, days)
        except Exception as e:
            res["errors"].append({"source": "wikipedia", "error": str(e)[:240]})
    if query:
        try:
            res["youtube"] = youtube_search(query, youtube_n)
        except Exception as e:
            res["errors"].append({"source": "youtube", "error": str(e)[:240]})
        try:
            res["reddit"] = reddit_top(query, reddit_limit)
        except Exception as e:
            res["errors"].append({"source": "reddit", "error": str(e)[:240]})
    yt_views = [x.get("views") or 0 for x in res["youtube"]]
    res["summary"] = {
        "evidence_types": sum(bool(res[k]) for k in ("wikipedia", "youtube", "reddit")),
        "best_youtube_views": max(yt_views) if yt_views else 0,
        "youtube_results": len(res["youtube"]),
        "reddit_results": len(res["reddit"]),
        "pageviews_window": (res["wikipedia"] or {}).get("pageviews_window", 0),
    }
    return res


def scan_topics(topics: list[dict[str, Any]], **kw: Any) -> dict[str, Any]:
    return {"generated_at": dt.datetime.now(dt.timezone.utc).isoformat(), "topics": [scan_topic(t, **kw) for t in topics]}


def evidence_patch(scan: dict[str, Any]) -> dict[str, Any]:
    """Convert scan output into discovery.json-shaped evidence fragments; scores are deliberately absent."""
    out = {}
    for t in scan.get("topics", []):
        ev: dict[str, Any] = {"existing_shorts": [], "long_form": [], "wikipedia": [], "trends": [], "reddit": []}
        if t.get("wikipedia"):
            w = t["wikipedia"]
            ev["wikipedia"].append({"url": w["url"], "pageviews_90d": w.get("pageviews_90d", w.get("pageviews_window", 0)), "daily_average": w.get("daily_average")})
        for y in t.get("youtube", []):
            target = "existing_shorts" if (y.get("duration") or 999) <= 60 else "long_form"
            ev[target].append({"url": y["url"], "views": y.get("views"), "title": y.get("title"), "channel": y.get("channel")})
        for r in t.get("reddit", []):
            ev["reddit"].append({"url": r["url"], "score": r.get("score", 0), "comments": r.get("comments", 0), "title": r.get("title")})
        if t.get("trends"):
            ev["trends"].append(t["trends"])
        out[t["id"]] = {"title": t.get("title"), "evidence": ev, "scan_summary": t.get("summary"), "scan_errors": t.get("errors")}
    return out


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("topics", help="JSON list of {id,title,wikipedia,query}")
    ap.add_argument("--out", default="trend_scan.json")
    ap.add_argument("--discovery-out", help="write discovery evidence fragments here")
    ap.add_argument("--days", type=int, default=90)
    ap.add_argument("--youtube-n", type=int, default=8)
    ap.add_argument("--reddit-limit", type=int, default=5)
    a = ap.parse_args(argv)
    topics = json.load(open(a.topics, encoding="utf-8"))
    scan = scan_topics(topics, days=a.days, youtube_n=a.youtube_n, reddit_limit=a.reddit_limit)
    json.dump(scan, open(a.out, "w", encoding="utf-8"), indent=1)
    if a.discovery_out:
        json.dump(evidence_patch(scan), open(a.discovery_out, "w", encoding="utf-8"), indent=1)
    for t in scan["topics"]:
        s = t["summary"]
        print(t["id"], "types", s["evidence_types"], "wiki", s["pageviews_window"], "yt", s["best_youtube_views"], "errors", len(t["errors"]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
