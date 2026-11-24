# 01 — Platform mechanics: YouTube Shorts and Instagram Reels

Treat these as the scoreboard. Every creative decision should move at least one of these signals.

## YouTube Shorts

| Signal | What it means | Creative lever |
|---|---|---|
| **Viewed vs. swiped away** (Shorts feed, YouTube Studio > Analytics > Content > Shorts) | % of feed impressions where the viewer did not swipe away immediately. The first gate. Good story Shorts sit roughly 70–85 %; under 60 % the Short usually stalls. | frame 0, first 1.5 s of audio, first sentence |
| **Average % viewed / retention curve** | Can exceed 100 % because replays loop. A flat line (no "cliff") is the goal. | open-loop ladder, shot rhythm, no dead air |
| **Replays / loops** | Since 31 Mar 2025 a Shorts "view" counts every start or replay; "engaged views" is the old metric. Loops therefore lift both reach and the view counter. | seamless last→first frame, last line that completes the first line |
| **Likes, comments, shares, subscribes from the Short** | Secondary signals; shares carry the most weight for reaching new viewers. | debate-worthy final line, social-currency fact |

Format facts:
- Vertical 9:16, 1080×1920, up to 3 minutes (since 15 Oct 2024). Story Shorts that go viral cluster at **25–60 s**; see `data/analysis_summary.md` for measured durations.
- Title: ≤ 60 characters, concrete, curiosity gap, no clickbait lies. The title appears small in the feed: the first 3–4 words carry it.
- Description: 1–2 lines + 3–5 hashtags. (Project rule for FirstEngineer: **no links in YouTube descriptions**.)
- Upload natively; do not upload files with another platform's watermark.

## Instagram Reels

Adam Mosseri (Head of Instagram) has repeatedly named the three most important Reels ranking signals:
1. **Watch time** (does the viewer watch past the first seconds, do they rewatch).
2. **Likes per reach**.
3. **Sends per reach** (DM shares) — the strongest signal for reaching *non-followers*.

Other published guidance:
- Original content is favoured; reposted / aggregated content and visible watermarks are down-ranked.
- Reels up to 3 minutes are recommended to non-followers; the hook still decides everything.
- Use on-screen text and captions (most people watch muted at first glance).
- "Trial reels" can test a hook on non-followers before showing it to followers — use it to A/B two hooks of the same video.

Format facts:
- 1080×1920, keep important content inside the **safe area**: top ~250 px and bottom ~400 px are covered by UI (username, caption, buttons); right ~140 px is covered by the action rail.
- Caption: first line = the hook restated as a question or bold claim (it shows before "more"); then 2–4 short lines; then a single CTA; then 3–8 hashtags.
- Cover frame: choose the strongest visual frame with ≤ 4 large words; the grid crops to 3:4 (1080×1440) on the profile.

## Shared rules for both

- Upload the same master to both platforms, never with a watermark from the other.
- Captions (burned-in) are mandatory: 1–3 words per chunk, high contrast, inside the safe area.
- Loudness: integrated −14 to −16 LUFS, true peak ≤ −1 dBTP. Narration always on top; music ducks 8–12 dB under voice.
- Post 30–60 min before the audience is most active (Mosseri). Measured windows for a European audience in our research: weekdays 12:00–13:00 CET and 18:00–21:00 CET; Thursday morning and Wednesday midday/evening strongest (Buffer, 9.6M posts, 2026); weakest Friday/Saturday.
- Consistency beats volume: 1–2 Shorts per day per platform, every day, with varied formats.
- Judge a Short after 48–72 h, not 2 h. Shorts frequently get a second wave days later.

## Metrics to log per video (for the feedback loop)

`viewed_vs_swiped`, `avg_pct_viewed`, `avg_view_duration`, `retention_at_3s`, `retention_at_50pct`, `loops`, `shares`, `sends_per_reach` (IG), `comments`, `subs_gained`, `profile_visits`, `waitlist_signups` (via UTM'd bio link). After every 10 videos, compare hooks, durations and emotions against these numbers and update `data/` and `references/03-hooks.md`.

## Reading the retention graph [R/E]

(Adapted from youtube-agent-skill `retention.py`, MIT.) Export: Studio → video → Analytics → Engagement → audience-retention chart → download. Then `python tools/third_party/youtube-agent-skill/retention.py retention.csv --duration 41 --transcript words.srt`.

Three different problems — fix only the biggest:
- **Hook leak** — loss in the opening. For a Short, read it as *viewed vs swiped* plus the drop in the first 3 s. Always a script/frame-0 fix, never the edit.
- **Cliffs** — single steep drops at a moment (topic change without signpost, a slow setup, the product bridge, a static shot). With the transcript you see the exact words spoken at the cliff; that is the actionable part.
- **Slide** — steady bleed across the middle. That is pacing: cut, don't rewrite.

If the hook is healthy and the slide is flat, the video is fine and the problem is packaging (title, first frame as thumbnail, topic).

## Title lint [R/E]

`python tools/third_party/youtube-agent-skill/title.py --title "..."` — desktop truncates around 60 characters and the mobile feed around 40, so the subject must sit in the first 40. Not more than two ALL-CAPS words. A number, a name or a date beats any adjective. The on-screen text in frame 0 must not repeat the title word for word: different words, same promise. Write ten titles, keep two.

## Search query test (long-form and evergreen Shorts) [E]

Before publishing, write the three queries a real person would type to find this story ("gimli glider", "plane ran out of fuel"). The title and the first two description lines must contain those words. The first two description lines are the only ones read (above "...more").

## Audit = one fix [E]

When reviewing the channel: read the last ten titles as a set (same shape = a format problem), look at first frames at feed size, score the hooks of the three latest, check upload consistency, read retention. Hand back ONE fix for this week, three specific things that already work (so they are not broken) and what NOT to change yet.


## Third-party "Shorts statistics": check them before you trust them [M]

Guides on the internet (including OpenMontage's short-form guide, which cites marketing blogs) repeat numbers like "180–200 WPM", "no static hold over 3 s", "15–30 s gets the most completion" or "3-second retention above 85 % gives 2.8× views". Most of them can't be checked. Test each one against `data/analysis_summary.md` before you use it:
- **Narration speed**: our successful story Shorts have a median of ~160 WPM, not 180–200. Clarity beats speed for story content.
- **Length**: our dataset spreads from 20 s to over 90 s across all tiers (section 3). No single length band is proven best. Choose the length the story needs, and treat "15–30 s" as a hypothesis to A/B test on your own channel.
- **Visual change every 1–3 s**: this is plausible as *visual change* (moves, labels, rack focus), which is not the same as a *cut*. The measured median cut interval is ~5 s, and the detector misses soft transitions.
- Useful and verifiable: platform UI safe zones. Keep text inside a centred ~900×1400 px area of 1080×1920. The bottom ~300 px (captions, buttons) and right ~100 px are covered on every platform. Instagram also covers ~210 px at the top. Upload H.264 at 8–15 Mbps; below ~5 Mbps platforms may re-compress visibly.

## Sample first [E]

Before you produce a batch, take ONE Short all the way to final: render, critic, fix. Lock the look, the sound bed and the caption style on that one. Building ten Shorts on an unproven look multiplies one mistake by ten.
