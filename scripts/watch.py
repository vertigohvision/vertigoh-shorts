#!/usr/bin/env python3
"""Turn a short-form video into something Claude can "watch": frames, shots, transcript, stats.

Usage: watch.py URL_OR_FILE [--out references/<name>] [--max-shots 40] [--scene 0.27]

Accepts Instagram / TikTok URLs (downloaded with yt-dlp) or any local video file
(e.g. a YouTube short pulled from Drive or the SSD).

Writes to OUT:
  video.mp4            the source (gitignored)
  meta.json            platform metadata (title, caption, views, likes, upload date) when a URL
  words.json / transcript.txt   word-timed transcript (Whisper)
  hook.jpg             contact sheet of the first 3 seconds (0.0-3.0s, 8 frames)
  timeline.jpg         16 evenly spaced frames across the whole video
  shots_NN.jpg         contact sheets: one frame per shot, labelled with time + shot length
  report.md            pacing stats, shot list, transcript — the starting point for a breakdown
"""
import argparse, json, pathlib, re, subprocess, sys, statistics
from PIL import Image, ImageDraw, ImageFont

HERE = pathlib.Path(__file__).resolve().parent
FONT = "/usr/share/fonts/opentype/montserrat/Montserrat-Bold.otf"

ap = argparse.ArgumentParser()
ap.add_argument("src")
ap.add_argument("--out")
ap.add_argument("--max-shots", type=int, default=40)
ap.add_argument("--scene", type=float, default=0.27, help="scene-change threshold (lower = more cuts)")
ap.add_argument("--no-transcribe", action="store_true")
a = ap.parse_args()

def run(cmd, **kw):
    return subprocess.run(cmd, capture_output=True, text=True, **kw)

is_url = re.match(r"https?://", a.src) is not None
out = pathlib.Path(a.out or (HERE.parent / "references" /
                   (re.sub(r"\W+", "_", a.src.rstrip("/").split("/")[-1].split("?")[0]) if is_url
                    else pathlib.Path(a.src).stem)))
out.mkdir(parents=True, exist_ok=True)
video = out / "video.mp4"
meta = {}

# ---- 1. get the video -------------------------------------------------------------
if is_url:
    if not video.exists():
        r = run(["yt-dlp", "--no-warnings", "--no-playlist", "-f", "bv*[height<=1920]+ba/b",
                 "--merge-output-format", "mp4", "--write-info-json", "-o", str(out / "video.%(ext)s"), a.src])
        if r.returncode:
            sys.exit(f"download failed:\n{r.stderr[-800:]}\n"
                     "YouTube blocks cloud servers: get the file via Drive/SSD and pass the path instead.")
    info = out / "video.info.json"
    if info.exists():
        j = json.loads(info.read_text())
        meta = {k: j.get(k) for k in ("title", "description", "uploader", "upload_date", "duration",
                                       "view_count", "like_count", "comment_count", "webpage_url")}
        info.unlink()
else:
    if not video.exists():
        video.symlink_to(pathlib.Path(a.src).resolve())
(out / "meta.json").write_text(json.dumps(meta, indent=1))

# ---- 2. probe ---------------------------------------------------------------------
p = json.loads(run(["ffprobe", "-v", "error", "-show_entries",
                    "format=duration:stream=codec_type,width,height,r_frame_rate",
                    "-of", "json", str(video)]).stdout)
dur = float(p["format"]["duration"])
vs = next(s for s in p["streams"] if s["codec_type"] == "video")
num, den = map(int, vs["r_frame_rate"].split("/")); fps = num / den

# ---- 3. shot detection ------------------------------------------------------------
r = run(["ffmpeg", "-hide_banner", "-i", str(video), "-vf",
         f"scale=320:-2,select='gt(scene,{a.scene})',showinfo", "-an", "-f", "null", "-"])
cuts = [float(m) for m in re.findall(r"pts_time:([\d.]+)", r.stderr)]
cuts = [c for i, c in enumerate(cuts) if c > 0.15 and (i == 0 or c - cuts[i - 1] > 0.15)]
bounds = [0.0] + cuts + [dur]
shots = [(bounds[i], bounds[i + 1]) for i in range(len(bounds) - 1)]
lens = [e - s for s, e in shots]

# ---- 4. frames + contact sheets ---------------------------------------------------
def grab(t, w=270):
    r = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{max(t,0):.3f}", "-i", str(video),
                        "-frames:v", "1", "-vf", f"scale={w}:-2", "-f", "image2pipe",
                        "-vcodec", "png", "-"], capture_output=True)
    from io import BytesIO
    return Image.open(BytesIO(r.stdout)).convert("RGB")

def sheet(items, path, cols=4):
    """items: list of (image, label)."""
    w, h = items[0][0].size; lab = 34
    rows = (len(items) + cols - 1) // cols
    S = Image.new("RGB", (cols * w, rows * (h + lab)), (18, 18, 18))
    d = ImageDraw.Draw(S); f = ImageFont.truetype(FONT, 20)
    for i, (im, label) in enumerate(items):
        x, y = (i % cols) * w, (i // cols) * (h + lab)
        S.paste(im, (x, y + lab)); d.text((x + 8, y + 6), label, font=f, fill=(255, 220, 90))
    S.save(path, quality=88)

hook_ts = [0.0, 0.3, 0.7, 1.0, 1.5, 2.0, 2.5, 3.0]
sheet([(grab(t), f"{t:.1f}s") for t in hook_ts if t < dur], out / "hook.jpg")

tl = [dur * (i + 0.5) / 16 for i in range(16)]       # even timeline, catches one-takes / long shots
sheet([(grab(t), f"{t:.1f}s") for t in tl], out / "timeline.jpg")

pick = shots
if len(shots) > a.max_shots:                       # sample evenly if very cut-heavy
    step = len(shots) / a.max_shots
    pick = [shots[int(i * step)] for i in range(a.max_shots)]
items = [(grab((s + e) / 2), f"#{shots.index((s,e))+1} {s:.1f}s ({e-s:.1f}s)") for s, e in pick]
sheets = []
for k in range(0, len(items), 16):
    pth = out / f"shots_{k//16+1:02d}.jpg"; sheet(items[k:k + 16], pth); sheets.append(pth.name)

# ---- 5. transcript + audio --------------------------------------------------------
words = []
if a.no_transcribe and (out / "words.json").exists():   # reuse an earlier transcript
    words = json.loads((out / "words.json").read_text())
elif not a.no_transcribe:
    run([sys.executable, str(HERE / "transcribe.py"), str(video), "--out", str(out)])
    wj, tt = out / "video.words.json", out / "video.transcript.txt"
    if wj.exists():
        wj.rename(out / "words.json"); tt.rename(out / "transcript.txt")
        words = json.loads((out / "words.json").read_text())
lufs = re.findall(r"I:\s+(-?[\d.]+) LUFS",
                  run(["ffmpeg", "-hide_banner", "-i", str(video), "-af", "ebur128", "-f", "null", "-"]).stderr)

# ---- 6. report --------------------------------------------------------------------
speech = sum(w["end"] - w["start"] for w in words)
first_word = words[0]["start"] if words else None
wpm = len(words) / (dur / 60) if words else 0
early = [c for c in cuts if c <= 3.0]

R = [f"# Watch report: {meta.get('title') or a.src}", ""]
if meta:
    R += [f"- **URL:** {meta.get('webpage_url')}", f"- **Uploader:** {meta.get('uploader')} · {meta.get('upload_date')}",
          f"- **Views / likes / comments:** {meta.get('view_count')} / {meta.get('like_count')} / {meta.get('comment_count')}",
          f"- **Post caption:** {(meta.get('description') or '').strip()[:500]}", ""]
R += ["## Technical", f"- {vs['width']}x{vs['height']} @ {fps:.2f}fps · {dur:.1f}s · loudness {lufs[-1] if lufs else '?'} LUFS", "",
      "## Pacing",
      f"- Shots: **{len(shots)}** · avg **{statistics.mean(lens):.2f}s** · median {statistics.median(lens):.2f}s · longest {max(lens):.1f}s",
      f"- Cuts per 10s: **{len(cuts)/dur*10:.1f}** · cuts in first 3s: **{len(early)}**",
      f"- First spoken word at: **{first_word:.2f}s**" if words else "- No speech detected",
      f"- Words/min: **{wpm:.0f}** · speech covers {speech/dur*100:.0f}% of runtime" if words else "", "",
      "## Contact sheets (Read these images)", "- `hook.jpg` — first 3 seconds", "- `timeline.jpg` — 16 evenly spaced frames",*[f"- `{s}`" for s in sheets], "",
      "## Shot list", "| # | start | len |", "|---|---|---|",
      *[f"| {i+1} | {s:.2f}s | {e-s:.2f}s |" for i, (s, e) in enumerate(shots)], "",
      "## Transcript", "```", (out / "transcript.txt").read_text().strip() if words else "(none)", "```"]
(out / "report.md").write_text("\n".join(R) + "\n")
print(f"ok -> {out}/report.md  ({len(shots)} shots, {len(words)} words, {len(sheets)} sheets)")
