# Kai Vertigoh — Short-Form Editing Playbook

> The living rulebook. Claude reads this at the start of every editing session and updates it
> after every feedback round. Every rule carries a source tag so we know *why* it exists.
>
> **Confidence tags:** `[RULE]` confirmed by Kai or by performance data · `[HYPOTHESIS]` our best
> guess, to be tested · `[RETIRED]` tried and dropped (kept so we don't repeat it)
>
> Version: v0.4 — 2026-11-21 (10 references reviewed: Kai #1, Adrian Per, Ludwig, Landon, and Kai's
> 6 YouTube shorts. Winners vs flops analysis in `references/WINNERS_VS_FLOPS.md`)

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

- **Kai's craft is in frame 1.** The pilot, rig or builder *doing the thing*, at a readable size, at
  0.0s (3.0s at the latest). A talking head at a desk doesn't count.
  `[RULE · 3 winners agree: kai_yt_wQsN3IJga6I 0.0s (10.7M), kai_yt_L9LfkWkKeqE 0.0s (547K),
  kai_DDsMDPgyzJJ ~3.0s (84.9M YT); all 3 flops miss it: China craft only at 7.1s, 2-cam never,
  Avata 2.5s then cut away]`
- **A concrete stake in the first line AND the title**: a number, a brand, "1 take", a deadline. Not
  an abstract question, a mood or context ("I had 10 seconds to…", not "So last week I went to…").
  `[RULE · winners 4/4 (1 take ×2, "Netflix's first ever", "$800,000") vs flops 0/3 ("is there a
  point of creating?", no line, "impossible" only in title); Landon agrees]`
- **Speech or text starts within 0.3s of frame 1.** No logo, no intro, no slow fade-in.
  `[RULE · 3/3 refs agree: Kai #1 0.00s, Adrian 0.11s, Ludwig 0.00s]` This is necessary, not
  sufficient: the China and Avata flops both speak at 0.00s. `[ref WINNERS_VS_FLOPS]`
- **Sound-off check:** frame 1 + on-screen text must say what's happening and why it matters with no
  audio. `[HYPOTHESIS · ref kai_yt_LDtUDGfn4KE (no text at all), landon_QREHkXXokrs]`
- **Frame 1 = an incongruity**: something that shouldn't be there (a kid at a pro edit bay, a drone
  aimed at a host's face). `[HYPOTHESIS · ref landon_QREHkXXokrs, kai_yt_wQsN3IJga6I]`
- **The setup sentence carries its own danger** ("…and then I left for a week").
  `[HYPOTHESIS · ref landon_QREHkXXokrs]`
- **Never letterbox.** Fill 9:16 from frame 1. `[HYPOTHESIS · ref kai_yt_L9RJX-rQ0_E: half the
  screen black at 0.0s, 6.6K views]`
- Open on the **viewer's goal or a question**, then the **promise**, then an **open loop**
  ("and the crazy part?…"). That's up to 3 hooks in the first 10s. `[HYPOTHESIS · ref omgadrian]`
- **"Everything is X… except one"** is a reusable hook-and-reveal shape for experiments and tool
  tests. `[HYPOTHESIS · ref ludwig]`
- FPV split screen: open with a **countdown or "action" moment** ("3, 2, 1, ACTION!"). It builds
  anticipation in under 2s. `[HYPOTHESIS · ref kai_DDsMDPgyzJJ]`
- Show the **live person doing it** (the BTS half of the split) from frame 1. *(Merged into the
  "craft in frame 1" RULE above.)*
- Put the **concrete stake** in on-screen text as well as the title (e.g. "$800,000" in big green
  text). *(See the stake RULE above.)* `[ref kai_DDsMDPgyzJJ, kai_yt_EVGZjg0l6_s]`
- **Title = topic + stake or brand.** Never a mood ("Idk what's happening anymore") or model numbers
  ("Osmo Pocket 4P vs Insta360 Luna Ultra"). `[RULE · winner titles 4/4 name a stake or brand;
  flop titles 0/3]`

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
  `[RULE · Kai #1 + kai_yt_wQsN3IJga6I + ludwig agree]` The halves must be **BTS and result of
  the same action**. A split of unrelated footage (China: robots + desk) doesn't help.
- **The BTS format is a simultaneous split for the whole runtime, never BTS-then-result.**
  `[RULE · kai_yt_wQsN3IJga6I (split 0.0s, 10.7M) + kai_DDsMDPgyzJJ (split 3.0s, 84.9M) vs
  kai_yt_LDtUDGfn4KE (BTS 0–3.3s then result only, 3.5K)]` *Test:* recut the Avata short as a split.
- **Storytime needs 2+ obstacles or failures before the payoff.**
  `[RULE · kai_yt_L9LfkWkKeqE (3 obstacles in 8s: 5-day notice, no-fly zone, 7-day permit) +
  kai_yt_EVGZjg0l6_s (2 failed prototypes) + landon_QREHkXXokrs (problem → 3 bots)]`
- **Promise a visual payoff in the first 3s; deliver it in the last 3s.** It must look impressive to
  non-pilots, not just be hard to fly. `[HYPOTHESIS · ref kai_yt_LDtUDGfn4KE, kai_yt_EVGZjg0l6_s
  (payoff = Ludwig holding a can), kai_yt_zfKBLxp6I_g (no payoff)]`
- **Show the builder by 3s** in build stories (a cutaway to Kai at CAD or in goggles).
  `[HYPOTHESIS · ref kai_yt_EVGZjg0l6_s: Kai first clearly on screen at ~28.8s]`
- **Name tools/rigs like characters** ("Theo", "Scout"; "my drone, Clanker") so each becomes a beat,
  and **re-open the loop at about 40%** ("but that's not the only one").
  `[HYPOTHESIS · ref landon_QREHkXXokrs]`
- **Cut rate isn't the lever.** Winners range from 0 to 7.6 cuts/10s; the China flop cuts 6.2/10s. What
  changes on screen (space, stakes, reveal) matters more than how often you cut.
  `[ref WINNERS_VS_FLOPS]`
- Re-hook every 5–8s: a new visual, a question or a reveal. Nothing static for more than about
  2.5s. `[HYPOTHESIS · Adrian Per reference]`
- Cut every breath, filler word and false start, but keep a natural rhythm. Don't jump-cut so
  hard the speech sounds robotic. `[HYPOTHESIS]`
- Target length 20–45s; go longer only if retention data supports it. `[HYPOTHESIS]` Exception:
  a one-take FPV holds for 79s because the tension never lets up. `[ref kai_DDsMDPgyzJJ]`
  Short alone doesn't save a short: the two 13–14s gear shorts flopped. Length follows story.
  `[ref kai_yt_L9RJX-rQ0_E, kai_yt_LDtUDGfn4KE]`
- **Change the environment or visual every ≤10s**, even in one-takes with no cuts.
  `[HYPOTHESIS · ref kai_DDsMDPgyzJJ]`
- **Keep imperfect, human moments** ("blew out a lot of stuff, but it's okay"). They make it
  authentic. `[HYPOTHESIS · ref kai_DDsMDPgyzJJ]`

## 6. Formats — what we know

| Format | Status | Notes |
|---|---|---|
| FPV split screen, BTS + result | Top performer (YT: 84.9M, 10.7M) | Proven. Keep making it. BTS and result together for the whole runtime. |
| Storytime / experiment, problem → creative solution | Strong (547K Netflix; 281K Ludwig), and Kai's preferred direction | Main growth bet. Needs a brand/number stake, 2+ obstacles, Kai on screen early and a visual payoff. |
| Travel recap / reflective essay (China) | Flop (1.5K) | Confirmed from the video: abstract hook, craft visible for only ~1s at 7.1s, no payoff, 76s, mood title. Belongs in long form or a carousel, or recut around one concrete moment. |
| Process vs result, gear comparison | Flop ×2 (6.6K, 3.5K) | Confirmed: no person (2-cam) or BTS cut away at 3.3s (Avata), no verdict, no on-screen claim, letterboxed opener, model-number titles. |

**Confound:** all 3 flops were posted 2026-10-15 → 11-06; all winners are from 2023–2025. Check YouTube
Studio (impressions, viewed-vs-swiped %) to rule out a channel-wide distribution dip.

## 7. Reference creators — what to take

- **Landon Bytheway (@Landonbtw).** One-word pop captions, very strong hooks, tight pacing.
  Mixes polished cinema shots with casual iPhone footage that feels organic.
- **Adrian Per (@omgadrian).** Image quality, scripting, storytelling, keeping you hooked
  start to finish, teaching something simply, talking to the camera, consistent branding and
  captions.
- **Ludwig (@ludwig).** Story hooks and vocal hooks, how clips are structured, audio,
  captions. Also a model for streams that are planned to produce shorts.

Full breakdowns are in `references/<name>/breakdown.md`. Done: `kai_DDsMDPgyzJJ`,
`omgadrian_DTF8yLpEceI`, `ludwig_DfWRz_Cvo8R`, `landon_QREHkXXokrs`, `kai_yt_wQsN3IJga6I`,
`kai_yt_L9LfkWkKeqE`, `kai_yt_EVGZjg0l6_s`, `kai_yt_zfKBLxp6I_g`, `kai_yt_L9RJX-rQ0_E`,
`kai_yt_LDtUDGfn4KE`. The comparison is in `references/WINNERS_VS_FLOPS.md`.
Landon's reference is a **sponsored** post (58M views at a 0.23% like rate). Benchmark his craft, not
his reach.

## 8. CTA & long-form funnel

- Keep CTAs soft and in voice; never a generic "follow for more". Tie them to a series or a
  promise ("part 2 of the build is on my channel"). `[HYPOTHESIS]`
- Where possible, end on a loop so the last frame leads back into the first. `[HYPOTHESIS]`
- **End within 2–3s of the payoff.** No outro. `[RULE · ref ludwig, Kai #1, kai_yt_wQsN3IJga6I
  (ends ~1s after "That was pretty good")]` No footage-only tail longer than 3s after the last line
  (Netflix runs 12s of tail). `[HYPOTHESIS · ref kai_yt_L9LfkWkKeqE]`
- **Comment-keyword CTA** ("comment BOT and I'll send you a link") as an alternative when there's a
  resource to give. `[HYPOTHESIS · ref landon_QREHkXXokrs]`
- **Make the follow CTA visual** (a screen recording of the profile with the cursor on Follow),
  paired with a promise of what's next. `[HYPOTHESIS · ref omgadrian]`

## 9. Glossary / proper nouns (for caption correction)

FPV · Ludwig · Kai Vertigoh · Audiio · DJI · DJI Avata 360 · Osmo Pocket 4P · Insta360 Luna Ultra ·
BetaFPV Pavo25 · TBS Tango II · Hollyland · Red Bull · Streamer Games · Poguelandia · Netflix

## 10. Don'ts

- Don't open on an abstract question or a mood. `[ref kai_yt_zfKBLxp6I_g]`
- Don't letterbox, and don't open on a frame where the drone or person is too small to read.
  `[ref kai_yt_L9RJX-rQ0_E, kai_yt_LDtUDGfn4KE]`
- Don't post a comparison without an on-screen verdict and a difference visible on a phone.
  `[ref kai_yt_L9RJX-rQ0_E]`
- Don't cut away from the BTS. Keep it on screen with the result. `[ref kai_yt_LDtUDGfn4KE]`
- Don't use mood or model-number titles. `[ref WINNERS_VS_FLOPS]`
- Don't export below −15 LUFS (China −19.8, Ludwig −18.8). Run QC on every render.
  `[ref kai_yt_zfKBLxp6I_g, kai_yt_EVGZjg0l6_s]`

---

## Change log

- **v0.4 (2026-11-21):** Watched Kai's 6 YouTube shorts + Landon on Kai's Mac, and wrote
  `WINNERS_VS_FLOPS.md`. Promoted to RULE: craft in frame 1, concrete stake in line 1 + title, title =
  topic + stake, split grammar, simultaneous BTS split, 2+ obstacles in storytime, end ≤3s after
  payoff. Added: sound-off check, incongruous first frame, never letterbox, visual payoff promise, show
  the builder by 3s, named tools as characters, comment-keyword CTA, a Don'ts list. Noted that speech
  by 0.3s and cut rate don't separate winners from flops, and the recency confound on the flops.

- **v0.3 (2026-11-21):** Adrian + Ludwig breakdowns. Promoted "speech by 0.3s" to RULE (3/3 refs).
  Added: question→promise→loop hook, two-layer type system, show every noun, two-line emphasis captions,
  end ≤3s after the payoff, visual follow CTA.

- **v0.2 (2026-11-21):** Added the watch-video skill. Rules from the first breakdown (Kai's #1 FPV split
  screen): countdown hook, split screen by 3s, change the visual every ≤10s, keep human moments, split-screen caption style.

- **v0.1 (2026-11-21):** Initial playbook from Kai's brief. Everything not stated directly by
  Kai is a hypothesis.
