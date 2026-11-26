"""Build an evidence pack from a RENDERED video so an independent critic can judge it without
trusting the producer's own score.

usage: python critic_pack.py VIDEO OUTDIR [--holds holds.json] [--model base.en] [--lang en] [--freeze 0.5]
holds.json (optional): [[start_s, end_s], ...] planned held frames; freezes inside them are reported
as "planned", everything else as "unplanned". The QA gate (references/10) fails on any unplanned
freeze >= --freeze seconds (default 0.5 s, the same number as the QA checklist).

Produces in OUTDIR: proxy.mp4 (540x960, with audio — give this to a model that can watch video),
contact_2fps.jpg, first3s_10fps.jpg, cut_frames.jpg (one frame after every cut), metrics.json and
pack.md (metrics + per-second transcript + per-second motion and loudness).
"""
import argparse, json, os, re, subprocess, sys

def sh(*a):
    r = subprocess.run(a, capture_output=True, text=True, errors="replace", stdin=subprocess.DEVNULL)
    if r.returncode != 0:
        raise RuntimeError(f"{a[0]} failed ({r.returncode}): {r.stderr[-400:]}")
    return r

def parse_freezes(text):
    starts = [float(x) for x in re.findall(r"freeze_start: ([\d.]+)", text)]
    durs = [float(x) for x in re.findall(r"freeze_duration: ([\d.]+)", text)]
    out = []
    for i, s in enumerate(starts):
        d = durs[i] if i < len(durs) else None
        out.append((round(s, 2), round(d, 2) if d is not None else None))
    return out

def classify_freezes(freezes, holds, min_d, total=None):
    planned, unplanned = [], []
    for s, d in freezes:
        dd = d if d is not None else ((total - s) if total else min_d)
        e = s + dd
        (planned if any(a - 0.05 <= s and e <= b + 0.05 for a, b in holds) else unplanned).append([s, round(dd, 2)])
    return planned, unplanned

def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("video"); ap.add_argument("outdir")
    ap.add_argument("--holds"); ap.add_argument("--model", default="base.en"); ap.add_argument("--lang", default="en")
    ap.add_argument("--freeze", type=float, default=0.5); ap.add_argument("--no-whisper", action="store_true")
    a = ap.parse_args(argv)
    f, out = a.video, a.outdir
    if not os.path.exists(f): sys.exit(f"no such video: {f}")
    os.makedirs(out, exist_ok=True)
    holds = json.load(open(a.holds)) if a.holds else []
    D = float(sh("ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f).stdout.strip() or 0)
    rows = int(D * 2 / 10) + 1
    sh("ffmpeg", "-y", "-v", "error", "-i", f, "-vf", f"fps=2,scale=180:320,tile=10x{rows}", "-frames:v", "1", f"{out}/contact_2fps.jpg")
    sh("ffmpeg", "-y", "-v", "error", "-t", "3", "-i", f, "-vf", "fps=10,scale=270:480,tile=10x3", "-frames:v", "1", f"{out}/first3s_10fps.jpg")
    sh("ffmpeg", "-y", "-v", "error", "-i", f, "-vf", "scale=540:960", "-c:v", "libx264", "-crf", "28", "-preset", "veryfast", "-c:a", "aac", "-b:a", "96k", f"{out}/proxy.mp4")
    cuts = [round(float(x), 2) for x in re.findall(r"pts_time:([\d.]+)", sh("ffmpeg", "-i", f, "-vf", "select='gt(scene,0.28)',showinfo", "-an", "-f", "null", "-").stderr)]
    if cuts:
        sh("ffmpeg", "-y", "-v", "error", "-i", f, "-vf", f"select='gt(scene,0.28)',scale=180:320,tile=10x{len(cuts) // 10 + 1}", "-fps_mode", "vfr", "-frames:v", "1", f"{out}/cut_frames.jpg")
    fd = sh("ffmpeg", "-i", f, "-vf", f"freezedetect=n=0.003:d={a.freeze},blackdetect=d=0.3", "-an", "-f", "null", "-").stderr
    planned, unplanned = classify_freezes(parse_freezes(fd), holds, a.freeze, D)
    blacks = [round(float(x), 2) for x in re.findall(r"black_start:([\d.]+)", fd)]
    lo = sh("ffmpeg", "-i", f, "-af", "ebur128=peak=true:metadata=1,ametadata=print:key=lavfi.r128.M", "-f", "null", "-").stderr
    I = re.findall(r"I:\s+(-?[\d.]+) LUFS", lo); TP = re.findall(r"Peak:\s+(-?[\d.]+) dBFS", lo)
    M = [float(x) for x in re.findall(r"lavfi.r128.M=(-?[\d.]+)", lo)]
    loud_s = [round(max(M[k * 10:(k + 1) * 10] or [-70]), 1) for k in range(int(D) + 1)]
    motion_s = []
    try:
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        from motion_features import frames, features
        import numpy as np
        fr = frames(f, 10); g = fr.mean(axis=3); dd = np.abs(np.diff(g, axis=0)).mean(axis=(1, 2))
        motion_s = [round(float(dd[i:i + 10].mean()), 1) for i in range(0, len(dd), 10)]
        mf = features(fr, 10)
    except Exception as e:
        mf = {"error": str(e)[:200]}
    words = []
    if not a.no_whisper:
        try:
            import whisper
            r = whisper.load_model(a.model).transcribe(f, word_timestamps=True, language=None if a.lang == "auto" else a.lang)
            words = [(w["word"].strip(), round(w["start"], 2)) for s in r["segments"] for w in s.get("words", [])]
        except Exception as e:
            print("whisper skipped:", e, file=sys.stderr)
    shots = [round(b - x, 2) for x, b in zip([0] + cuts, cuts + [D])]
    met = dict(duration=round(D, 2), cuts=cuts, longest_shot=max(shots) if shots else D, freeze_threshold_s=a.freeze,
               freezes_planned=planned, freezes_unplanned=unplanned, black_frames=blacks,
               lufs=float(I[-1]) if I else None, true_peak=float(TP[-1]) if TP else None,
               first_word=words[0][1] if words else None, motion=mf,
               gate_pass=not unplanned and (not TP or float(TP[-1]) <= -1.0))
    json.dump(dict(metrics=met, words=words, motion_per_s=motion_s, loudness_per_s=loud_s), open(f"{out}/metrics.json", "w"), indent=1)
    line = lambda x, b: " ".join(w for w, t in words if x <= t < b)
    with open(f"{out}/pack.md", "w", encoding="utf-8") as o:
        o.write("# Critic pack\n\nWatch proxy.mp4 if you can play video. Otherwise use contact_2fps.jpg (2 fps, left to right, top to bottom), "
                "first3s_10fps.jpg and cut_frames.jpg. Frame sampling can hide flicker, caption/voice drift and audio problems: say so when you could not check them.\n\n")
        o.write("## Metrics\n```json\n" + json.dumps(met, indent=1) + "\n```\n\n## Per second: motion | loudness (LUFS M) | words\n")
        for s in range(int(D) + 1):
            mo = motion_s[s] if s < len(motion_s) else ""; lu = loud_s[s] if s < len(loud_s) else ""
            o.write(f"- {s:>3}s  m={mo}  L={lu}  {line(s, s + 1)}\n")
    print(json.dumps(met))
    return met

if __name__ == "__main__":
    main()
