#!/usr/bin/env bash
# Cut a clip from a source, reframe to 1080x1920, burn captions, normalize loudness.
# Usage: render.sh SRC START END OUT.mp4 [CAPTIONS.ass] [CROP_X_CENTER 0-1] [FPS]
#   CROP_X_CENTER: horizontal center of the 9:16 crop as a fraction (0.5 = middle)
#   Vertical sources (already 9:16) are just scaled.
set -euo pipefail
SRC=$1; START=$2; END=$3; OUT=$4; ASS=${5:-}; CX=${6:-0.5}; FPS=${7:-30}

IFS=x read W H < <(ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=p=0:s=x "$SRC")
if (( W * 16 > H * 9 )); then   # wider than 9:16 -> crop horizontally
  VF="crop=ih*9/16:ih:max(0\,min(iw-ih*9/16\,iw*${CX}-ih*9/32)):0,scale=1080:1920:flags=lanczos"
else
  VF="scale=1080:1920:force_original_aspect_ratio=increase:flags=lanczos,crop=1080:1920"
fi
VF="$VF,fps=${FPS},setsar=1"
[[ -n "$ASS" ]] && VF="$VF,ass=${ASS}"

ffmpeg -hide_banner -loglevel error -y -ss "$START" -to "$END" -i "$SRC" \
  -vf "$VF" \
  -af "loudnorm=I=-14:TP=-1.0:LRA=11" \
  -c:v libx264 -preset slow -crf 17 -profile:v high -pix_fmt yuv420p -movflags +faststart \
  -c:a aac -b:a 256k -ar 48000 "$OUT"
echo "rendered -> $OUT"
