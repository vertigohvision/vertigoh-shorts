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

Dependencies: ffmpeg, `pip install faster-whisper`, Montserrat (`apt install fonts-montserrat`).
