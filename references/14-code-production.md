# 14 — Code production: turn every planned visual into code that renders

Goal: an AI model (or a person) turns a `short_plan.md` into **runnable code** that outputs the finished 1080×1920 MP4, with no GUI work. Every shot type in this skill (code-drawn diagram, archive evidence, 2.5D photo parallax, Blender reconstruction, kinetic type, captions, sound) maps to code below. If a shot can't be expressed this way, redesign the shot, don't fake it.

## 1. Environment contract (state it at the top of build.py)
- Python 3.11+, Pillow ≥ 10, numpy, FFmpeg ≥ 6 on PATH. Optional: Blender 4.2+ run headless (`blender -b -P shot.py -- args`), or any sandbox that has Python + FFmpeg.
- If the sandbox has no Blender, render reconstructions with numpy/Pillow (orthographic or simple perspective projection of a mesh you define in code, flat shading with one key light, a fill light and fog), or a pre-rendered PNG sequence. Never substitute AI images.
- Fonts: IBM Plex Sans and IBM Plex Mono (OFL). Bundle the TTFs in `fonts/` or download them from github.com/IBM/plex at build time. Fall back to DejaVu only for previews.
- Deterministic: fixed seeds; no network access during render except a declared asset fetch step.

## 2. Folder layout per video
```
NN_slug/
  plan.md          # from templates/short_plan.md
  vo.txt           # narration text exactly as spoken
  vo.wav           # TTS or recorded narration (optional at first; see 5)
  words.json       # [{"w":"word","s":0.00,"e":0.31}, ...]  (Whisper/Vosk alignment)
  assets/          # archive files + credits.csv (tools/find_archive.py)
  build.py         # renders frames, composes, mixes, encodes
  blender/shot_XX.py  # optional bpy scenes, each renders a PNG sequence
  out/NN_slug.mp4
```

## 3. Timeline as data
`build.py` holds the shot list as a Python list. Every row comes straight from the plan:
```python
SHOTS = [
  # id, start, end, kind, params (six layers: subject, framing, move, light, text, sound)
  ("s01", 0.00, 1.20, "archive_push", dict(src="assets/a01.jpg", a=(0.50,0.45,1.00), b=(0.52,0.42,1.12),
       label="NBS BSS 143, Fig. 5.7", ease="inout", hold_end=0.25)),
  ("s02", 1.20, 3.40, "diagram", dict(fn="draw_rod_detail", reveal=[(1.4,"rod"),(2.1,"nut"),(2.8,"load")])),
  ("s03", 3.40, 6.00, "blender", dict(seq="renders/s03_%04d.png", label="RECONSTRUCTION: FIRSTENGINEER")),
]
```
Bind start and end times to `words.json` ("cut on the word 'stamp'"): `t = word_time("stamp")`. Don't hard-code times once the narration exists.

## 4. Shot kinds (each is a function `render(kind, t_local, dur, p) -> PIL.Image 1080×1920`)
- **archive_push / archive_pan**: crop window interpolated from `a` to `b` (cx, cy, zoom) with ease-in-out, ending in a hold. Lanczos resample, never AI upscaling. Grain ≤ 3 %. The source label (mono, 26–30 px) stays inside the safe area for the whole shot.
- **parallax_2_5d**: split the photo into 2–3 layers by hand-drawn polygon masks (defined in code). Move the layers at different speeds (foreground 1.0, mid 0.6, back 0.3); max travel 4 % of the width. Inpaint behind the foreground with a blur of the surrounding area, not with generated content.
- **document_reveal**: render the page on a desk plane (perspective warp with Pillow `Image.transform(PERSPECTIVE)`). The camera eases to the key line, a highlighter draws under it left to right at 40–60 chars/s, and the page is held for 0.4 s.
- **diagram**: vector drawing in Pillow at 2× size, then downscaled (antialiasing). Parts appear on word cues. Lines draw on with stroke length interpolation. Colours from one palette (≤ 4 + neutrals). Arrows only point at something the narration names.
- **graph**: an axis appears first, the line draws over 0.8–1.5 s, the key value pops with a counter (ease-out). The axis label always shows units and source.
- **timeline / map**: a 2D camera (translate + scale matrix) moving over a large canvas that you draw once. Markers appear on cues. A scale bar and a north arrow on maps.
- **blender**: `blender/shot_XX.py` builds the scene with bpy only (primitives, modifiers, procedural materials, no add-ons), keyframes one sealed camera move (13-camera-direction), Eevee at 1080×1920, 30 fps, and writes PNGs. 2D labels are added in `build.py`, not in Blender.
- **kinetic_type**: ≤ 5 words, IBM Plex Sans 600–700. Words enter on their spoken time (words.json) with a 6–10 frame ease. No bouncing, no rainbow, no emoji.
- **held_frame**: a deliberate still of 0.6–1.2 s before the payoff, with a slow push of ≤ 2 %. Silence or a single sustained tone.

## 5. Captions, narration, sound (all code)
- Captions: build from words.json in chunks of 1–4 words, centred at y≈1280–1400, the current word in the accent colour, a 3 px dark stroke, inside the 900×1400 safe area. Never put them over a source label.
- Narration: if `vo.wav` is missing, the build writes `vo.txt` and makes a **timing-only preview**: word times estimated at 165 WPM, plus silence. Final renders need real narration and alignment.
- SFX synthesised with numpy (no licences needed): paper slide = band-passed noise with a 120 ms envelope; stamp = a 60 Hz sine with a noise click and 200 ms decay; impact = a low sine sweep 80→35 Hz plus noise and 0.6 s decay; riser = noise with a rising band-pass over 1.5–3 s; tick = a 2 kHz 8 ms click; underwater = low-passed brown noise. Place each SFX on its shot cue.
- Music bed: a slow pad from detuned sines or saws (low-passed, 2–4 chords), or a licensed track listed in credits. Duck it under the voice by 8–10 dB (sidechain from the VO envelope).
- Mix with FFmpeg: VO −16 LUFS short-term, music ≈ −30 LUFS under the VO, SFX peaks ≤ −6 dBFS. Final `loudnorm` two-pass to I = −14 ±1, TP ≤ −1.0, LRA ≤ 9.

## 6. Encode
Pipe frames to FFmpeg rather than writing thousands of PNGs: `ffmpeg -f rawvideo -pix_fmt rgb24 -s 1080x1920 -r 30 -i - -i mix.wav -c:v libx264 -preset slow -crf 17 -pix_fmt yuv420p -profile:v high -c:a aac -b:a 192k -movflags +faststart out.mp4`. Check that the frame count equals duration × 30.

## 7. Self-checks that build.py must run
- `--preview`: renders at 540×960, every 2nd frame, plus `contact_2fps.jpg` (tools/critic_pack.py).
- Asserts: no shot without a purpose field; no asset used twice; every archive shot has a label; nothing outside the safe area; ≥ 1 visual change every 2.5 s (a move, a reveal or a cut); the first cut before 4 s [M]; LUFS and true peak within spec; no black frame over 0.3 s and no unplanned frozen frame of 0.5 s or more (planned holds are listed in `holds.json`).
- Then run `python tools/critic_pack.py out.mp4 critic/ --holds holds.json` and give `critic/` (proxy.mp4, contact sheets, pack.md) to an independent critic (12-critic-agent). FIX at most twice.

## 8. What the model must deliver per video
`plan.md`, `vo.txt`, `build.py` (complete, runnable, no placeholders except the narration audio), `blender/*.py` if used, an asset list with URLs and licences (or the `find_archive.py` query file), and the expected runtime. If the model can run code, it renders `--preview` first, inspects the contact sheet itself, fixes it, then renders the final.
