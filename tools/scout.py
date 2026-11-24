"""Build a TOP / MID / LOW sample per channel from its Shorts tab, then download the videos.

Tiers are disjoint by construction: TOP = the n_top most-viewed, LOW = the n_low least-viewed, MID =
n_mid around the median of what remains. Channels with fewer than n_top+n_mid+n_low eligible Shorts
are skipped (the v2 run let 15-video channels overlap TOP and MID; see data/README.md).

usage: python scout.py [--channels a,b,c] [--pick pick.json] [--videos v] [--no-download]
Before trusting a channel, confirm the handle is the intended creator (title + 3 video titles).
"""
import argparse, json, os, statistics, subprocess, sys

DEFAULT_CH = ["zackdfilms", "MarkRober", "veritasium", "NileRed", "RealEngineering", "kurzgesagt", "MrBallen",
              "PracticalEngineeringChannel", "TheB1M", "HistoryLegends", "simplehistory", "bigthink",
              "WendoverProductions", "InterestingEngineering", "TheInfographicsShow", "Fern-TV", "PlainlyDifficult",
              "NEOexplains", "MentourPilot", "MagnatesMedia", "Sideprojects", "EngineeringExplained"]
YT = [sys.executable, "-m", "yt_dlp", "--js-runtimes", "node"]

def tiers(entries, n_top=6, n_mid=5, n_low=5):
    """Return [(tier, entry)] with no entry in two tiers, or [] if the channel is too small."""
    E = sorted(entries, key=lambda e: -e["view_count"])
    if len(E) < n_top + n_mid + n_low:
        return []
    top, low, rest = E[:n_top], E[len(E) - n_low:], E[n_top:len(E) - n_low]
    m = len(rest) // 2
    a = max(0, m - n_mid // 2)
    mid = rest[a:a + n_mid]
    return [("top", e) for e in top] + [("mid", e) for e in mid] + [("low", e) for e in low]

def list_channel(h, limit=160, drop_newest=10):
    r = subprocess.run(YT + ["--flat-playlist", "-J", "--playlist-end", str(limit), f"https://www.youtube.com/@{h}/shorts"],
                       capture_output=True, text=True, timeout=300)
    if r.returncode != 0:
        raise RuntimeError(r.stderr[-300:])
    E = [e for e in json.loads(r.stdout).get("entries", []) if e.get("view_count")]
    return E[drop_newest:] if len(E) > 40 else E  # newest videos: views not settled yet

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--channels", default=",".join(DEFAULT_CH)); ap.add_argument("--pick", default="pick.json")
    ap.add_argument("--videos", default="v"); ap.add_argument("--no-download", action="store_true")
    a = ap.parse_args()
    pick = []
    for h in [c.strip() for c in a.channels.split(",") if c.strip()]:
        try: E = list_channel(h)
        except Exception as ex: print("FAIL", h, ex, flush=True); continue
        sel = tiers(E)
        if not sel: print("SKIP (too few Shorts)", h, len(E), flush=True); continue
        med = statistics.median(e["view_count"] for e in E)
        for tier, e in sel:
            pick.append(dict(ch=h, views=e["view_count"], title=e.get("title", ""), id=e["id"], tier=tier,
                             ch_median=med, ch_n=len(E), timestamp=e.get("timestamp"), upload_date=e.get("upload_date")))
        print("OK", h, len(E), int(med), flush=True)
    assert len({p["id"] for p in pick}) == len(pick), "an id landed in two tiers"
    json.dump(pick, open(a.pick, "w", encoding="utf-8"), indent=1); print("PICKED", len(pick), flush=True)
    if a.no_download: return
    os.makedirs(a.videos, exist_ok=True)
    for p in pick:
        f = os.path.join(a.videos, p["id"] + ".mp4")
        if os.path.exists(f): continue
        r = subprocess.run(YT + ["-q", "-f", "bv*[height<=360]+ba/b[height<=360]/b", "--merge-output-format", "mp4", "-o", f,
                                 "https://www.youtube.com/shorts/" + p["id"]], timeout=300)
        if r.returncode != 0: print("DLFAIL", p["id"], flush=True)
    print("DLDONE", flush=True)

if __name__ == "__main__":
    main()
