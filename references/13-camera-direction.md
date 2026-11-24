# 13 — Camera direction and shot specification

Adapted and extended from AustinZ21/cinematic-skills (`shot-director`, `still-to-film`, MIT), rewritten for vertical story Shorts built from real archive + code-drawn animation + Blender. Evidence level: **[E]** craft rules from film practice, not measured on Shorts.

> An adjective makes the model (or you) guess. A camera instruction says what to do. "Make it cinematic" is not a note. "Start on the gauge, push in at steady speed, stop when the needle hits zero, background never moves" is.

## 1. Three questions before any shot

1. **What do we look at?** The one piece of information that must land first.
2. **Where do we stand?** Shot size, height, angle.
3. **How do we approach?** Stay still, turn in place, travel, or shift focus.

Then four checks: Why does the subject move? Why does the camera move? What does the move reveal? **Would it be better if the camera did not move at all?** A move with a story job pulls the viewer along; a move added "to look expensive" becomes the endless forward float that makes video look AI-made.

## 2. Every shot is written in six layers

| Layer | Answers | Words |
|---|---|---|
| 1 Subject + action (blocking) | who/what does what, when | the needle drops, the beam buckles, the crowd steps |
| 2 Shot size | how much fits | extreme wide · wide · medium · close-up · extreme close-up (insert) |
| 3 Angle + height | from where | eye level · low · high · overhead · ground level |
| 4 Lens + focus | how space looks | wide lens · long lens · shallow DOF · deep focus · rack focus |
| 5 Camera move | how it travels | one main move (§3) |
| 6 Pace + limits | how it starts and ends | speed, ease, start frame → end frame, what stays still |

Add to the shot list (`templates/short_plan.md`): **Start → end frame**, **Holds** (what must not change, scale reference, screen direction), **Cut cue** (the word, beat or sound the cut lands on).

## 3. Move rules

- **One main move per shot.** Two at most, joined by a trigger ("when the counter hits 0, the push stops and focus racks to the crack"). Everything else is a cut.
- **Every move is sealed:** start, end, speed, what does not change. "Pan right" alone pans until the clip ends.
- **Never mix zoom and dolly by accident.** Zoom = optical, everything scales evenly (flat). Dolly/push = camera travels, near things grow faster than far (parallax). Opposite directions together = dolly zoom (shock), only deliberately.
- **Static first when unsure.** If composition and action don't work still, no move saves them.
- **Not every shot moves.** Constant motion removes the reference point; a held static shot makes the next move hit harder. Budget per Short: ≥ 1 held near-static beat (usually the turn or right before the payoff).
- **Camera moves only when the subject or the information moves, and exactly as much** (Fincher rule).
- **Handheld is a controlled strength**, not random shake: "slight footstep bob" by default, more only on impact.
- **Ease:** smoothstep `u*u*(3-2u)` for in/out; constant log-zoom rate feels like a steady dolly; accelerating dive `k*u^2.3`. Speed must stay continuous across cuts that are meant to flow.
- **Motion blur on fast moves** (~6 sub-frames over ~1 frame of shutter) or the push strobes.

### Look-alike pairs (write the right one)

Pan (turn head) vs **truck** (step sideways: near things race past) · tilt (look up) vs **pedestal** (rise, lens level) · **zoom** vs **dolly** · handheld (breath) vs gimbal (smooth inertia) · crane (arc: height + distance + angle together) vs pedestal (straight up) · POV (whose eyes) vs FPV (flight route) · barrel roll (keeps rotating) vs Dutch angle (tilts once, holds) · long take (no cut) vs slow motion (playback speed).

## 4. Choose the move by the feeling or the job

| Feeling / job in a disaster Short | First choice | Watch out |
|---|---|---|
| Objective record, evidence, a document | static or very slow push | text must be readable for ≥ 1.2 s at rest |
| Realisation ("they knew") | slow push in, stop on the key line | stop exactly on the stressed word |
| Danger off-screen / still to come | slow pan or tilt toward it | write what is hidden first, where it stops |
| A detail suddenly matters (crack, bolt, gauge) | rack focus or fast push | settle instantly |
| Shock / sudden failure | crash zoom, whip pan, impact shake | one per Short; clear start/end |
| Scale, size, power (bridge, dam, ship) | tilt up / pedestal up / pull back | must contain a scale ruler (person, car, bus) |
| Loneliness, aftermath, loss | slow pull out | end frame shows the empty space around |
| Mechanism in 3D (how it failed) | small orbit (≤ 90°) around the part | one axis; label stays readable |
| Journey / timeline progress | truck along a timeline or a map | one screen direction for the whole sequence |
| Falling / losing control | barrel roll (small = unease, large = fall) | once |
| Panic closing in | dolly zoom | centred subject, deep background (corridor, girders) |

Fastest path: performance/evidence strong on its own → **static**; something changes inside a person → **push in**; the surroundings change the meaning → **pull out**; new info is off-frame → **pan/tilt**; new info is in frame at another depth → **rack focus**; crossing space → **truck/track**; need 3D form → **orbit**; just bigger → **zoom**.

## 5. Real archive photos with real camera moves (2.5D depth parallax)

A real photo that is only zoomed reads as a slideshow (Ken Burns). Give it depth instead:
1. Make a depth map of the photo (`tools/third_party/cinematic-skills/prep_plate.py`, Depth Anything V2). **Do not use its AI super-resolution step on archive evidence** — it invents detail; upscale with Lanczos. The depth map changes only geometry, not content; still label the shot `ARCHIVE · <source>`.
2. Render with `depthshot.js` (or the same maths in Blender: photo on a displaced plane). Push = zoom `lz` + depth magnification `pz` (the `pz` is what sells "the camera moved"). Truck/pedestal = `px/py` ≤ ±0.05. Pan/tilt beyond ~10 % of the frame or orbit beyond a few degrees: impossible from one still — cut instead.
3. Failure modes: near edges tear into "melted glass" (reduce px/pz, dilate depth); thin flat things (signs, glass, water from above, documents) get false relief → `pz: 0`; cables crossing depth edges kink; plate borders show at move extremes → check first/last frame.
4. **Something moves inside every frame**, not only the camera: dust/particles in light, water, smoke, a blinking indicator, a counter, a highlight wiping a line.

Decision: depth shot if the move stays within the picture (push/pull/small truck). Blender if something must enter, turn, or be seen from another side. Code-drawn 2D if the shot is a diagram, number or map.

## 6. Time and space (sequence level)

- **Scale needs a ruler.** Every wide shot of something huge has a known-size object in it.
- **Geography before action.** One layout shot (map, plan, cutaway) before the failure, so the viewer knows where the threat and the safety are.
- **Hold the line.** A moving thing keeps one screen direction per sequence (e.g. the plane always flies toward frame right until it falls).
- **Stage in depth.** Foreground, subject and background layers let one moving shot replace three cuts.
- **Shrink shot length toward the climax**, then **hold one beat longer than comfortable before the reveal**. Speed is only felt against stillness.
- **One near-silent held moment** before the biggest beat (the turn-point silence in `07-sound-design.md`).
- **Match cuts** jump time or place by shape, motion or sound (rivet to bolt, ripple to sound wave, crack in the model to crack in the archive photo).
- **Let sound do the cutting:** cut on a sound, bridge into the next scene with sound, drop to silence before impact.
- **Moves in time:** slow motion at most once per Short; speed ramp for impact; time-lapse to compress years; reverse to show how it should have been; freeze on the frame of failure while the camera keeps moving.
- **Light has a source** the viewer could point to (window, screen, sun, fire). One strong source and deep shadow beats "cinematic lighting".
- **Colour carries point of view:** one grade for the record/evidence (neutral, slightly cool), another for reconstruction (warmer, grain), used consistently.
- **Withhold, then reveal:** start on the detail before the context, or the reaction before the cause.
- **Every shot changes what the viewer knows or feels.** If not, it is decoration: cut it.
