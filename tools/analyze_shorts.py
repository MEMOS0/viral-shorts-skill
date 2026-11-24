"""Second-by-second measurements of downloaded Shorts (Whisper words, FFmpeg cuts, loudness, loop diff).

usage: python analyze_shorts.py --pick pick.json --videos v --out full.json [--model base.en] [--lang en]
Use the same Whisper model for every video you compare: WPM differs between models (base.en vs small.en).
For non-English channels pass --model base (multilingual) and --lang <code> or --lang auto.
"""
import argparse, glob, json, os, re, subprocess, sys, tempfile
import numpy as np
from PIL import Image

def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True, errors="replace")
    if r.returncode != 0:
        raise RuntimeError(f"{cmd[0]} failed: {r.stderr[-300:]}")
    return r

def duration(f):
    return float(run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f]).stdout.strip() or 0)

def scene_cuts(f, thr=0.28):
    return [round(float(x), 2) for x in re.findall(r"pts_time:([\d.]+)", run(["ffmpeg", "-i", f, "-vf", f"select='gt(scene,{thr})',showinfo", "-an", "-f", "null", "-"]).stderr)]

def loudness(f, D):
    lo = run(["ffmpeg", "-i", f, "-af", "ebur128=metadata=1,ametadata=print:key=lavfi.r128.M", "-f", "null", "-"]).stderr
    M = [float(x) for x in re.findall(r"lavfi.r128.M=(-?[\d.]+)", lo)]
    persec = [round(max(M[k * 10:(k + 1) * 10] or [-70]), 1) for k in range(int(D) + 1)] if M else []
    I = re.findall(r"I:\s+(-?[\d.]+) LUFS", lo)
    return (float(I[-1]) if I else None), persec

def loop_diff(f, tmp):
    a, b = os.path.join(tmp, "a.png"), os.path.join(tmp, "b.png")
    run(["ffmpeg", "-y", "-v", "error", "-ss", "0.1", "-i", f, "-frames:v", "1", "-vf", "scale=64:114", a])
    run(["ffmpeg", "-y", "-v", "error", "-sseof", "-0.2", "-i", f, "-frames:v", "1", "-vf", "scale=64:114", b])
    A, B = (np.asarray(Image.open(p).convert("L"), float) for p in (a, b))
    return round(float(np.abs(A - B).mean()), 1)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pick", default=os.environ.get("PICK", "pick.json")); ap.add_argument("--videos", default="v")
    ap.add_argument("--out", default="full.json"); ap.add_argument("--model", default="base.en"); ap.add_argument("--lang", default="en")
    ap.add_argument("--sheets", default="sheets")
    a = ap.parse_args()
    import whisper, torch
    P = {p["id"]: p for p in json.load(open(a.pick, encoding="utf-8"))}
    m = whisper.load_model(a.model)
    out = json.load(open(a.out, encoding="utf-8")) if os.path.exists(a.out) else []
    done = {o["id"] for o in out}; os.makedirs(a.sheets, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        for f in sorted(glob.glob(os.path.join(a.videos, "*.mp4"))):
            i = os.path.basename(f)[:-4]
            if i in done or i not in P: continue
            try:
                p = dict(P[i]); D = duration(f)
                r = m.transcribe(f, word_timestamps=True, fp16=torch.cuda.is_available(), language=None if a.lang == "auto" else a.lang)
                words = [(w["word"].strip(), round(w["start"], 2), round(w["end"], 2)) for s in r["segments"] for w in s.get("words", [])]
                cuts = scene_cuts(f); I, persec = loudness(f, D)
                subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", f, "-vf", "fps=2,scale=135:240,tile=10x%d" % max(1, int(D * 2 / 10) + 1),
                                "-frames:v", "1", os.path.join(a.sheets, i + ".jpg")])
                try: loop = loop_diff(f, tmp)
                except Exception: loop = None
                sl = np.diff([0] + cuts + [D]) if D else []
                p.update(dur=round(D, 1), text=r["text"].strip(), words=words, cuts=cuts, ncuts=len(cuts), whisper_model=a.model,
                         med_shot=round(float(np.median(sl)), 2) if len(sl) else None, first_cut=cuts[0] if cuts else None,
                         wpm=round(len(words) / max(D, 1) * 60), first_word=words[0][1] if words else None,
                         hook=" ".join(w[0] for w in words if w[1] < 3.0), lufs=I, persec=persec, loopdiff=loop)
            except Exception as e:
                print("ERR", i, e, file=sys.stderr); continue
            out.append(p); json.dump(out, open(a.out, "w", encoding="utf-8"), indent=1)
            print(i, p["dur"], p["ncuts"], p["hook"][:80], flush=True)
    print("ANDONE")

if __name__ == "__main__":
    main()
