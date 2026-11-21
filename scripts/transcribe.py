#!/usr/bin/env python3
"""Transcribe a video/audio file to word-level JSON + readable transcript.

Usage: transcribe.py INPUT [--model small.en] [--out DIR]
Writes: <out>/<stem>.words.json  (list of {word,start,end,prob})
        <out>/<stem>.transcript.txt (timestamped lines, for picking clips)
"""
import argparse, json, pathlib, subprocess
import numpy as np
from faster_whisper import WhisperModel

ap = argparse.ArgumentParser()
ap.add_argument("input")
ap.add_argument("--model", default="small.en")
ap.add_argument("--out", default=None)
a = ap.parse_args()

src = pathlib.Path(a.input)
out = pathlib.Path(a.out or src.parent)
out.mkdir(parents=True, exist_ok=True)

model = WhisperModel(a.model, device="cpu", compute_type="int8")
# decode with ffmpeg (robust to any codec/container the camera produces)
pcm = subprocess.run(["ffmpeg", "-nostdin", "-loglevel", "error", "-i", str(src), "-vn", "-ac", "1",
                      "-ar", "16000", "-f", "s16le", "-"], capture_output=True, check=True).stdout
audio = np.frombuffer(pcm, np.int16).astype(np.float32) / 32768.0
segments, info = model.transcribe(audio, word_timestamps=True, vad_filter=True)

words, lines = [], []
for seg in segments:
    m, s = divmod(seg.start, 60)
    lines.append(f"[{int(m):02d}:{s:05.2f}] {seg.text.strip()}")
    for w in seg.words or []:
        words.append({"word": w.word.strip(), "start": round(w.start, 3),
                      "end": round(w.end, 3), "prob": round(w.probability, 3)})

(out / f"{src.stem}.words.json").write_text(json.dumps(words, indent=1))
(out / f"{src.stem}.transcript.txt").write_text("\n".join(lines) + "\n")
print(f"{len(words)} words, {info.duration:.1f}s -> {out}")
