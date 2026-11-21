# vertigoh-shorts

Short-form editing workspace for @kaivertigoh, edited by Claude.

- `EDITING_PLAYBOOK.md`: style rules. Read it before every edit and update it after feedback.
- `FEEDBACK_LOG.md`: one entry per short, with notes and performance.
- `scripts/`: the pipeline. `scripts/watch.py` + `.claude/skills/watch-video/`: watch and break down any video.
- `references/<name>/`: breakdowns of reference shorts (frames, transcript, report, breakdown.md).
- `projects/<date>-<name>/`: transcripts, caption files, edit notes. No video in git; media
  lives on the SSD or in Drive.

## Pipeline

```bash
python3 scripts/transcribe.py SOURCE.mp4 --out projects/X        # words.json + transcript.txt
python3 scripts/captions.py projects/X/SOURCE.words.json cap.ass \
        --mode word --start 312.4 --end 341.0                     # or --mode chunk --chunk 4
scripts/render.sh SOURCE.mp4 312.4 341.0 out.mp4 cap.ass 0.5 30  # 1080x1920, -14 LUFS
```

Dependencies:
- Linux: `apt install ffmpeg fonts-montserrat && pip install faster-whisper yt-dlp pillow`
- macOS: `brew install ffmpeg yt-dlp && brew install --cask font-montserrat && pip3 install faster-whisper pillow`
  (YouTube downloads work from a Mac; cloud servers get blocked by YouTube's bot check.)
  Homebrew's Python (3.15) refuses global `pip install` (PEP 668) and has no `av` wheels yet, so use
  a 3.13 venv: `brew install python@3.13 deno && python3.13 -m venv ~/.venvs/vertigoh &&
  ~/.venvs/vertigoh/bin/pip install faster-whisper pillow numpy`, then run the scripts with
  `~/.venvs/vertigoh/bin/python`.
