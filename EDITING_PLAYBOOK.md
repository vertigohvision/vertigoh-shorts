# Kai Vertigoh — Short-Form Editing Playbook

> The living rulebook. Claude reads this at the start of every editing session and updates it
> after every feedback round. Every rule carries a source tag so we know *why* it exists.
>
> **Confidence tags:** `[RULE]` confirmed by Kai or by performance data · `[HYPOTHESIS]` our best
> guess, to be tested · `[RETIRED]` tried and dropped (kept so we don't repeat it)
>
> Version: v0.3 — 2026-11-21 (3 references reviewed: Kai #1, Adrian Per, Ludwig)

---

## 1. Channel identity

- **Handle:** @kaivertigoh on Instagram, TikTok and YouTube Shorts. `[RULE · Kai 11/21]`
- **Direction:** creative technology, tools and how they're used, experiments, and vlog-style
  experiences. Move toward problem → creative tech solution stories, e.g. the Ludwig drone
  BTS. `[RULE · Kai 11/21]`
- **Goals, in priority order:**
  1. **Follower conversion.** A viewer should finish the short knowing what Kai does, so
     following feels obvious.
  2. **Push viewers to long form.** `[RULE · Kai 11/21]`
- **What makes Kai credible:** pro filmmaking and FPV skill, plus the willingness to build
  solutions. Every short should show one of the two. `[HYPOTHESIS]`

## 2. Technical specs

| Item | Spec | Source |
|---|---|---|
| Resolution | 1080×1920 | `[RULE · Kai]` |
| Frame rate | 30fps default; 24fps for cinematic-only pieces | `[RULE · Kai]` |
| Codec | H.264 High, CRF 17, yuv420p, faststart | default |
| Audio | AAC 256k / 48kHz, loudness −14 LUFS, true peak −1 dB | platform norm (the #1 short shipped at −16.3) |
| Font | Montserrat SemiBold (Medium for long chunks) | `[RULE · Kai]` |
| Music | Audiio.com library only | `[RULE · Kai]` |

**Safe zones (1080×1920):** keep text and key action out of:
- the top ~220px (handle, search bar)
- the bottom ~420px (caption, audio, CTA)
- the right ~160px (like/comment/share buttons)

Default caption baseline: y≈1250. `[RULE · platform UI]`

## 3. Captions

- Two modes, picked per shot: `[RULE · Kai 11/21]`
  - **One word at a time, pop-in** (Landon style): for talking heads and clean frames, when
    the words carry the moment.
  - **3–5 words at a time**: when a lot is happening on screen (FPV, split screen, busy B-roll),
    so the eye isn't pulled away from the action.
- White text, 2.5px black outline, soft shadow, sentence case. `[HYPOTHESIS]` Test ALL CAPS on
  hooks only.
- The hook line can be larger and placed higher (y≈700) as on-screen title text, separate from
  the spoken captions. `[HYPOTHESIS]`
- FPV split-screen look (from Kai's #1): small italic, teal or white, 1–3 words with
  commas/ellipses, placed on the split seam; reads like overheard dialogue. Sound-effect labels
  in asterisks (*Crew clapping*). Keep this as the split-screen caption style; A/B it against
  Montserrat. `[HYPOTHESIS · ref kai_DDsMDPgyzJJ]`
- **Mode 3, two-line emphasis:** 2–5 words, with the keyword larger on line 2. A middle ground
  for stream, screen and BTS clips. `[HYPOTHESIS · ref ludwig]`
- **Emphasis layer:** small subtitles plus ONE giant keyword per beat in a single brand colour,
  animated in (blur or scale), sometimes placed behind the subject. Kai needs a brand accent
  colour; the teal from the #1 reel is a candidate. `[HYPOTHESIS · ref omgadrian]`
- Fix Whisper's errors on names and gear before rendering (FPV, Ludwig, DJI, specific
  products). Keep a word list in §9.

## 4. Hook (0–3s)

- Frame 1 has to be visually interesting by itself, with no sound needed. The FPV split screen
  works because BTS and result are on screen together from frame 1. `[HYPOTHESIS · from Kai's
  top performers, references not yet reviewed]`
- The first spoken line states a stake, a problem or a promise, not context ("I had 10 seconds
  to…", not "So last week I went to…"). `[HYPOTHESIS]`
- **Speech or text starts within 0.3s of frame 1.** No logo, no intro, no slow fade-in.
  `[RULE · 3/3 refs agree: Kai #1 0.00s, Adrian 0.11s, Ludwig 0.00s]`
- Open on the **viewer's goal or a question**, then the **promise**, then an **open loop**
  ("and the crazy part?…"). That's up to 3 hooks in the first 10s. `[HYPOTHESIS · ref omgadrian]`
- **"Everything is X… except one"** is a reusable hook-and-reveal shape for experiments and tool
  tests. `[HYPOTHESIS · ref ludwig]`
- FPV split screen: open with a **countdown or "action" moment** ("3, 2, 1, ACTION!"). It builds
  anticipation in under 2s. `[HYPOTHESIS · ref kai_DDsMDPgyzJJ]`
- Show the **live person doing it** (the BTS half of the split) by 3s at the latest. Test showing
  it from frame 1. `[HYPOTHESIS · ref kai_DDsMDPgyzJJ]`
- Put a **concrete stake** (a dollar figure, "1 take", a deadline) in on-screen text and/or the
  post caption. `[HYPOTHESIS · ref kai_DDsMDPgyzJJ]`

## 5. Story structure & pacing

- **Storytime template** (the direction Kai wants, e.g. the Ludwig drone BTS):
  1. Hook: the problem or stakes.
  2. Context, in one line at most.
  3. Attempt or build. Show the tech, since that's what makes it creative-tech content.
  4. Twist or obstacle.
  5. Payoff: the shot or result.
  6. Loop or CTA. `[HYPOTHESIS]`
- **Show every noun.** When the script lists things, cut to a visual of each one.
  `[HYPOTHESIS · ref omgadrian: 24 shots / 66s, avg 2.75s]`
- In talking heads, a **camera move or punch-in can stand in for a cut**. `[HYPOTHESIS · ref omgadrian]`
- **Split layout grammar: action/screen on top, face below, captions on the seam.**
  `[HYPOTHESIS · Kai #1 + ludwig agree]`
- Re-hook every 5–8s: a new visual, a question or a reveal. Nothing static for more than about
  2.5s. `[HYPOTHESIS · Adrian Per reference]`
- Cut every breath, filler word and false start, but keep a natural rhythm. Don't jump-cut so
  hard the speech sounds robotic. `[HYPOTHESIS]`
- Target length 20–45s; go longer only if retention data supports it. `[HYPOTHESIS]` Exception:
  a one-take FPV holds for 79s because the tension never lets up. `[ref kai_DDsMDPgyzJJ]`
- **Change the environment or visual every ≤10s**, even in one-takes with no cuts.
  `[HYPOTHESIS · ref kai_DDsMDPgyzJJ]`
- **Keep imperfect, human moments** ("blew out a lot of stuff, but it's okay"). They make it
  authentic. `[HYPOTHESIS · ref kai_DDsMDPgyzJJ]`

## 6. Formats — what we know

| Format | Status | Notes |
|---|---|---|
| FPV split screen, BTS + result | Top performer (IG + YT) | Proven. Keep making it. |
| Storytime / experiment, problem → creative solution | Strong performer, and Kai's preferred direction | Main growth bet. |
| Travel recap montage (China) | Flop | Hypothesis: no stakes or hook, and off-niche for the audience. To verify. |
| Process vs result, gear comparison | Flop ×2 | Hypothesis: the payoff only matters to people who already care about the gear, there's no story, and quality differences don't show on a compressed phone screen. To verify. |

## 7. Reference creators — what to take

- **Landon Bytheway (@Landonbtw).** One-word pop captions, very strong hooks, tight pacing.
  Mixes polished cinema shots with casual iPhone footage that feels organic.
- **Adrian Per (@omgadrian).** Image quality, scripting, storytelling, keeping you hooked
  start to finish, teaching something simply, talking to the camera, consistent branding and
  captions.
- **Ludwig (@ludwig).** Story hooks and vocal hooks, how clips are structured, audio,
  captions. Also a model for streams that are planned to produce shorts.

Full breakdowns are in `references/<name>/breakdown.md`. Done: `kai_DDsMDPgyzJJ`,
`omgadrian_DTF8yLpEceI`, `ludwig_DfWRz_Cvo8R`. Still to do: Landon and Kai's YouTube shorts.

## 8. CTA & long-form funnel

- Keep CTAs soft and in voice; never a generic "follow for more". Tie them to a series or a
  promise ("part 2 of the build is on my channel"). `[HYPOTHESIS]`
- Where possible, end on a loop so the last frame leads back into the first. `[HYPOTHESIS]`
- **End within 2–3s of the payoff.** No outro. `[HYPOTHESIS · ref ludwig, Kai #1]`
- **Make the follow CTA visual** (a screen recording of the profile with the cursor on Follow),
  paired with a promise of what's next. `[HYPOTHESIS · ref omgadrian]`

## 9. Glossary / proper nouns (for caption correction)

FPV · Ludwig · Kai Vertigoh · Audiio · DJI

## 10. Don'ts

*(Filled in from feedback.)*

---

## Change log

- **v0.3 (2026-11-21):** Adrian + Ludwig breakdowns. Promoted "speech by 0.3s" to RULE (3/3 refs).
  Added: question→promise→loop hook, two-layer type system, show every noun, two-line emphasis captions,
  end ≤3s after the payoff, visual follow CTA.

- **v0.2 (2026-11-21):** Added the watch-video skill. Rules from the first breakdown (Kai's #1 FPV split
  screen): countdown hook, split screen by 3s, change the visual every ≤10s, keep human moments, split-screen caption style.

- **v0.1 (2026-11-21):** Initial playbook from Kai's brief. Everything not stated directly by
  Kai is a hypothesis.
