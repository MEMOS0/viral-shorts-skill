"""Lint a package.json (title, description/caption, hashtags, tags, cover) against platform limits and
the packaging rules in references/16-packaging.md. usage: python package_lint.py package.json  (exit 1 on errors)"""
import json, re, sys

GENERIC = {"#reels", "#reel", "#viral", "#fyp", "#foryou", "#foryoupage", "#explore", "#explorepage", "#trending", "#shorts"}
BAIT = re.compile(r"you won'?t believe|gone wrong|must see|shocking|insane|comment (yes|below if)|like if|smash (the )?like|tag a friend who", re.I)

def lint(p):
    E, W = [], []
    plat = p.get("platform", "youtube"); tags = p.get("hashtags", [])
    text = p.get("caption", "") if plat == "instagram" else p.get("title", "") + "\n" + p.get("description", "")
    if plat == "youtube":
        t = p.get("title", "")
        if not t: E.append("title missing")
        if len(t) > 100: E.append(f"title {len(t)} chars > 100")
        if re.search(r"[<>]", t + p.get("description", "")): E.append("< or > not allowed in title/description")
        if len(p.get("description", "")) > 5000: E.append("description > 5000 chars")
        if len(t) > 60: W.append("title > 60 chars: the meaning must be in the first ~40")
        if len(tags) > 15: W.append(f"{len(tags)} hashtags: keep 3–5 (> 60 makes YouTube ignore all)")
        if len(tags) > 60: E.append("> 60 hashtags: YouTube ignores all of them")
        tl = sum(len(x) + (2 if " " in x else 0) for x in p.get("tags", [])) + max(0, len(p.get("tags", [])) - 1)
        if tl > 500: E.append(f"tags {tl} chars > 500")
        if sum(1 for w in re.findall(r"\b[A-Z]{3,}\b", t) if w not in ("NASA", "USA", "NTSB", "MAX", "USS", "UK", "BBC")) > 1: W.append("more than one ALL-CAPS word in title")
        if re.search(r"https?://", p.get("description", "")): W.append("URLs in Shorts descriptions are not clickable: use the Related-video link")
    else:
        if not p.get("caption"): E.append("caption missing")
        if len(p.get("caption", "")) > 2200: E.append("caption > 2200 chars")
        if len(tags) > 5: E.append(f"{len(tags)} hashtags > 5 (Instagram limit since Dec 2025)")
    for h in tags:
        if " " in h or not h.startswith("#"): E.append(f"bad hashtag {h!r}")
        if h.lower() in GENERIC: W.append(f"generic hashtag {h} does not help discovery")
    if BAIT.search(text): E.append("clickbait / engagement-bait phrase (misleading-metadata and bait policies)")
    wc = (p.get("withheld_cause") or "").lower()
    if wc and wc in (p.get("title", "") + " " + (p.get("caption", "").split("\n")[0])).lower(): E.append("title/first line reveals the cause the video withholds")
    kw = p.get("keywords", [])
    if kw and not any(k.lower() in text.lower() for k in kw): W.append("no search keyword appears in the title/description/caption")
    if p.get("hook_line") and p.get("title", "").strip().lower() == p["hook_line"].strip().lower(): W.append("title repeats the hook word for word: complement it")
    if len(p.get("alt_titles", [])) < 4 and plat == "youtube": W.append("write 5 titles (alt_titles >= 4) and keep a second one for testing")
    if p.get("cover_text") and len(p["cover_text"].split()) > 4: W.append("cover text > 4 words")
    return E, W

if __name__ == "__main__":
    E, W = lint(json.load(open(sys.argv[1], encoding="utf-8")))
    for w in W: print("WARN", w)
    for e in E: print("ERROR", e)
    print("PASS" if not E else "FAIL"); sys.exit(1 if E else 0)
