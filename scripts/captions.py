#!/usr/bin/env python3
"""Build an .ass caption file from words.json.

Usage: captions.py WORDS_JSON OUT_ASS [--mode word|chunk] [--chunk 4]
                   [--offset SEC] [--start SEC --end SEC] [--y 1250] [--size 82]
  --mode word   one word at a time, pop-in (Landon-style; use when screen is busy-free)
  --mode chunk  3-5 words per line (use when lots is happening on screen)
  --start/--end keep only words inside this window of the source; times are
                re-based so the clip starts at 0.
Style defaults come from EDITING_PLAYBOOK.md (Montserrat SemiBold, white, soft shadow,
kept out of the platform UI zones).
"""
import argparse, json, re

ap = argparse.ArgumentParser()
ap.add_argument("words"); ap.add_argument("out")
ap.add_argument("--mode", choices=["word", "chunk"], default="word")
ap.add_argument("--chunk", type=int, default=4)
ap.add_argument("--start", type=float, default=0.0)
ap.add_argument("--end", type=float, default=1e9)
ap.add_argument("--y", type=int, default=1250, help="caption baseline (px from top)")
ap.add_argument("--size", type=int, default=82)
ap.add_argument("--font", default="Montserrat SemiBold")
ap.add_argument("--upper", action="store_true", help="UPPERCASE captions")
a = ap.parse_args()

words = [w for w in json.load(open(a.words)) if a.start <= w["start"] < a.end]
for w in words:
    w["start"] -= a.start; w["end"] -= a.start

def ts(t):
    t = max(t, 0); h = int(t // 3600); m = int(t % 3600 // 60); s = t % 60
    return f"{h}:{m:02d}:{s:05.2f}"

def clean(txt):
    txt = re.sub(r"[{}\\]", "", txt)
    return txt.upper() if a.upper else txt

header = f"""[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Cap,{a.font},{a.size},&H00FFFFFF,&H00FFFFFF,&H00000000,&H80000000,0,0,0,0,100,100,0,0,1,2.5,3,5,120,160,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
POP = r"{\fscx85\fscy85\t(0,80,\fscx100\fscy100)}"  # quick scale-up pop
pos = rf"{{\pos(540,{a.y})}}"
events = []

if a.mode == "word":
    for i, w in enumerate(words):
        nxt = words[i + 1]["start"] if i + 1 < len(words) else w["end"] + 0.4
        end = min(nxt, w["end"] + 0.5)          # hold through tiny gaps, clear on pauses
        events.append((w["start"], max(end, w["start"] + 0.12), pos + POP + clean(w["word"])))
else:
    chunks, cur = [], []
    for w in words:
        cur.append(w)
        brk = len(cur) >= a.chunk or re.search(r"[.?!,]$", w["word"])
        if brk: chunks.append(cur); cur = []
    if cur: chunks.append(cur)
    for c in chunks:
        events.append((c[0]["start"], c[-1]["end"] + 0.15,
                       pos + POP + " ".join(clean(w["word"]) for w in c)))

with open(a.out, "w") as f:
    f.write(header)
    for s, e, txt in events:
        f.write(f"Dialogue: 0,{ts(s)},{ts(e)},Cap,,0,0,0,,{txt}\n")
print(f"{len(events)} caption events -> {a.out}")
