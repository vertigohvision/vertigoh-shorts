---
name: watch-video
description: Watch and break down a short-form video (Instagram/TikTok URL, or a local/Drive/SSD file incl. YouTube Shorts) — extracts hook frames, timeline, per-shot contact sheets, word-timed transcript and pacing stats, then writes an editor's breakdown and feeds lessons into EDITING_PLAYBOOK.md. Use whenever Kai shares a reference, a competitor short, one of his own shorts, or a draft to review.
---

# Watch a video like an editor

## 1. Get the material
```bash
python3 scripts/watch.py "<url or path>" --out references/<creator>_<id>
```
- **Instagram / TikTok URLs:** download directly.
- **YouTube:** YouTube blocks cloud servers with a bot check. Do not try to get around it. Use
  one of these instead:
  - the file from Kai's Drive or SSD (pass the path), or
  - run this skill in a session on Kai's Mac, where yt-dlp works normally.
- Re-running is cheap: `--no-transcribe` reuses the existing transcript.
- Lower `--scene` (e.g. 0.2) if cuts are being missed. Raise it (0.35) if camera motion or
  FPV gets counted as cuts.

## 2. Watch it
Read, in order:
1. `report.md`: metadata, pacing stats, transcript.
2. `hook.jpg`: the first 3s. This matters most.
3. `timeline.jpg`: the whole arc.
4. `shots_*.jpg`: every shot, if it's cut-heavy.

If a moment needs a closer look, grab extra frames:
`ffmpeg -ss T -i video.mp4 -frames:v 1 -vf scale=540:-2 /tmp/f.jpg`, then Read it.

The stats cover what the frames can't show: when the first word lands, cut rate, how much of
the runtime is speech, and loudness.

## 3. Write `breakdown.md` in that folder
Use these headings:
- **Hook (0–3s):**
  - The first frame: would it stop the scroll with the sound off?
  - The first spoken line, any on-screen text, and the first visual change.
- **Format & structure:** list the beats with timestamps.
- **Retention devices:** re-hooks, open loops, reveals, pattern breaks, and where they land.
- **Captions:** font, size, colour, position, words per caption, animation, sound-effect
  labels.
- **Pacing:** cut rate and how it changes through the video, use of silence, speed of speech.
- **Audio:** music, sound effects, natural sound, voiceover.
- **Ending:** CTA, loop, or payoff.
- **Platform context:** the post caption or title, numbers, upload date.
- **Why it worked / didn't:** separate what you can see in the video from what you're
  guessing.
- **Steal / avoid:** specific, testable rules.

## 4. Close the loop
- Add the "steal / avoid" rules to `EDITING_PLAYBOOK.md`:
  - Tag a rule `[HYPOTHESIS · ref <folder>]` when it's new.
  - Promote an existing hypothesis to `[RULE]` when Kai confirms it or 3+ references agree.
- For Kai's own shorts, add or extend the entry in `FEEDBACK_LOG.md`.
- Commit `breakdown.md`, `report.md`, the sheets and the transcript. `video.mp4` is
  gitignored.
