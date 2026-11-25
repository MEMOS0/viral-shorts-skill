import trend_scan


def test_scan_topics_aggregates_public_demand_evidence(monkeypatch):
    monkeypatch.setattr(trend_scan, "wiki_pageviews", lambda article, days=90: {
        "url": "https://en.wikipedia.org/wiki/Test_article", "api_url": "https://api", "article": article,
        "days": days, "pageviews_90d": 9000, "pageviews_window": 9000, "daily_average": 100.0,
    })
    monkeypatch.setattr(trend_scan, "youtube_search", lambda query, n=8: [
        {"url": "https://www.youtube.com/watch?v=a", "title": "short", "channel": "c", "views": 1000, "duration": 45},
        {"url": "https://www.youtube.com/watch?v=b", "title": "long", "channel": "c", "views": 5000, "duration": 500},
    ])
    monkeypatch.setattr(trend_scan, "reddit_top", lambda query, limit=5: [
        {"url": "https://www.reddit.com/r/x/comments/1", "title": "thread", "subreddit": "x", "score": 200, "comments": 30}
    ])
    scan = trend_scan.scan_topics([{"id": "t1", "title": "Test disaster", "wikipedia": "Test article", "query": "test disaster"}], days=90)
    t = scan["topics"][0]
    assert t["summary"]["evidence_types"] == 3
    assert t["summary"]["best_youtube_views"] == 5000
    assert t["trends"]["direction"] == "not_measured"
    patch = trend_scan.evidence_patch(scan)["t1"]["evidence"]
    assert patch["wikipedia"][0]["pageviews_90d"] == 9000
    assert len(patch["existing_shorts"]) == 1 and len(patch["long_form"]) == 1
    assert patch["reddit"][0]["score"] == 200


def test_scan_records_source_errors_without_fabricating(monkeypatch):
    def broken(*a, **k):
        raise RuntimeError("offline")
    monkeypatch.setattr(trend_scan, "wiki_pageviews", broken)
    monkeypatch.setattr(trend_scan, "youtube_search", broken)
    monkeypatch.setattr(trend_scan, "reddit_top", broken)
    t = trend_scan.scan_topic({"id": "t", "title": "Offline", "query": "offline"})
    assert t["summary"]["evidence_types"] == 0
    assert {e["source"] for e in t["errors"]} == {"wikipedia", "youtube", "reddit"}
    assert t["trends"]["direction"] == "not_measured"
