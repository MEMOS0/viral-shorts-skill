"""Frame-difference features that do not depend on the scene-cut detector.

FFmpeg's scene score (used for `cuts`) misses dissolves, whip-pans and continuous animation, so a
video with constant motion can show 0 cuts. This script measures motion directly from downscaled
grey frames, which works for both cut-based and continuous edits.

usage: python motion_features.py VIDEO_DIR pick.json out.json [--fps 10]
Per video: motion_mean, motion_p90, static_share (seconds with almost no change), longest_static_s,
soft_cuts (diff peaks between the soft and hard thresholds), hard_cuts, first15_motion (0-1.5 s),
first_frame stats (brightness, contrast, colourfulness, edge density) and first3_changes.
"""
import argparse, json, os, subprocess, sys
import numpy as np

W, H = 72, 128

def frames(path, fps):
    cmd = ["ffmpeg", "-v", "error", "-i", path, "-vf", f"fps={fps},scale={W}:{H}", "-f", "rawvideo", "-pix_fmt", "rgb24", "-"]
    r = subprocess.run(cmd, capture_output=True)
    if r.returncode != 0 or not r.stdout:
        raise RuntimeError(r.stderr.decode(errors="replace")[-300:] or "ffmpeg produced no frames")
    a = np.frombuffer(r.stdout, np.uint8)
    n = a.size // (W * H * 3)
    return a[: n * W * H * 3].reshape(n, H, W, 3).astype(np.float32)

def first_frame_stats(f):
    g = f.mean(axis=2)
    rg, yb = f[..., 0] - f[..., 1], 0.5 * (f[..., 0] + f[..., 1]) - f[..., 2]
    colourful = float(np.hypot(rg.std(), yb.std()) + 0.3 * np.hypot(rg.mean(), yb.mean()))
    gy, gx = np.gradient(g)
    return dict(ff_brightness=round(float(g.mean()), 1), ff_contrast=round(float(g.std()), 1),
                ff_colourful=round(colourful, 1), ff_edges=round(float((np.hypot(gx, gy) > 20).mean()), 3))

def features(fr, fps, static_thr=1.5, soft_thr=12.0, hard_thr=30.0):
    g = fr.mean(axis=3)
    d = np.abs(np.diff(g, axis=0)).mean(axis=(1, 2)) if len(g) > 1 else np.zeros(1)
    sec = [d[i:i + fps].mean() for i in range(0, len(d), fps)]
    static = [s < static_thr for s in sec]
    longest = run = 0
    for s in static:
        run = run + 1 if s else 0
        longest = max(longest, run)
    peaks = [i for i in range(1, len(d) - 1) if d[i] >= d[i - 1] and d[i] >= d[i + 1]]
    hard = [i for i in peaks if d[i] >= hard_thr]
    soft = [i for i in peaks if soft_thr <= d[i] < hard_thr]
    first3 = [i for i in peaks if d[i] >= soft_thr and i < 3 * fps]
    out = dict(motion_mean=round(float(d.mean()), 2), motion_p90=round(float(np.percentile(d, 90)), 2),
               static_share=round(sum(static) / max(len(static), 1), 3), longest_static_s=longest,
               hard_cuts=len(hard), soft_cuts=len(soft), first3_changes=len(first3),
               first15_motion=round(float(d[: int(1.5 * fps)].mean()), 2))
    out.update(first_frame_stats(fr[0]))
    return out

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("video_dir"); ap.add_argument("pick"); ap.add_argument("out")
    ap.add_argument("--fps", type=int, default=10)
    a = ap.parse_args()
    ids = [p["id"] for p in json.load(open(a.pick, encoding="utf-8"))]
    res = json.load(open(a.out, encoding="utf-8")) if os.path.exists(a.out) else {}
    for i in dict.fromkeys(ids):
        if i in res: continue
        f = os.path.join(a.video_dir, i + ".mp4")
        if not os.path.exists(f): print("MISSING", i, file=sys.stderr); continue
        try: res[i] = features(frames(f, a.fps), a.fps)
        except Exception as e: print("ERR", i, e, file=sys.stderr); continue
        json.dump(res, open(a.out, "w", encoding="utf-8"), indent=0)
        print(i, res[i]["motion_mean"], res[i]["hard_cuts"], res[i]["soft_cuts"], flush=True)
    print("MOTIONDONE", len(res))

if __name__ == "__main__":
    main()
