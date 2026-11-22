#!/usr/bin/env python3
"""Snapshot public YouTube channel stats (titles + view counts) for Shorts and long-form.

Usage: channel_stats.py [@handle]   (default @KaiVertigoh)
Writes: channel/youtube_shorts.csv, channel/youtube_videos.csv, channel/STATS.md
Only public numbers (views, titles, durations, upload dates for long-form). Retention,
impressions and swipe-away rates need YouTube Studio exports from Kai.
"""
import csv, datetime, json, pathlib, statistics, subprocess, sys

handle = sys.argv[1] if len(sys.argv) > 1 else "@KaiVertigoh"
root = pathlib.Path(__file__).resolve().parent.parent / "channel"
root.mkdir(exist_ok=True)
today = datetime.date.today().isoformat()

def tab(name):
    r = subprocess.run(["yt-dlp", "--no-warnings", "--flat-playlist", "-J",
                        f"https://www.youtube.com/{handle}/{name}"], capture_output=True, text=True)
    if r.returncode:
        sys.exit(f"failed on {name}: {r.stderr[-400:]}")
    return json.loads(r.stdout)

S, V = tab("shorts"), tab("videos")
shorts = [{"rank_newest": i + 1, "id": e["id"], "views": e.get("view_count") or 0,
           "title": e.get("title") or ""} for i, e in enumerate(S["entries"])]
videos = [{"rank_newest": i + 1, "id": e["id"], "views": e.get("view_count") or 0,
           "minutes": round((e.get("duration") or 0) / 60, 1),
           "date": datetime.date.fromtimestamp(e["timestamp"]).isoformat() if e.get("timestamp") else "",
           "title": e.get("title") or ""} for i, e in enumerate(V["entries"])]

for name, rows in (("youtube_shorts.csv", shorts), ("youtube_videos.csv", videos)):
    with open(root / name, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)

def med(rows): return int(statistics.median(r["views"] for r in rows)) if rows else 0
def fmt(n): return f"{n:,}"
def top(rows, n, extra=""):
    out = []
    for r in sorted(rows, key=lambda r: -r["views"])[:n]:
        x = (f" · {r['date']}" if r.get("date") else "") + f" · {r['minutes']}min" if extra else ""
        out.append(f"| {fmt(r['views'])} | {r['title'][:80]}{x} | `{r['id']}` |")
    return out

L = [f"# {S.get('channel')} — public YouTube stats (snapshot {today})", "",
     f"- Subscribers: **{fmt(S.get('channel_follower_count') or 0)}** · Shorts: **{len(shorts)}** · Long-form: **{len(videos)}**",
     f"- Refresh: `python3 scripts/channel_stats.py`", "",
     "## Shorts", "",
     "| Window (newest first) | Median views |", "|---|---|",
     f"| Latest 10 | {fmt(med(shorts[:10]))} |", f"| Latest 30 | {fmt(med(shorts[:30]))} |",
     f"| 31–80 | {fmt(med(shorts[30:80]))} |", f"| All | {fmt(med(shorts))} |", "",
     f"Shorts over 1M views: **{sum(r['views'] >= 1_000_000 for r in shorts)}** · over 100K: **{sum(r['views'] >= 100_000 for r in shorts)}**", "",
     "### Top 20 shorts", "| Views | Title | ID |", "|---|---|---|", *top(shorts, 20), "",
     "### Latest 15 shorts", "| Views | Title | ID |", "|---|---|---|",
     *[f"| {fmt(r['views'])} | {r['title'][:80]} | `{r['id']}` |" for r in shorts[:15]], "",
     "## Long-form", "",
     f"Median views — latest 10: **{fmt(med(videos[:10]))}** · all: **{fmt(med(videos))}**", "",
     "### Top 15 long-form", "| Views | Title | ID |", "|---|---|---|", *top(videos, 15, extra=True), "",
     "### Latest 10 long-form", "| Views | Title · length | ID |", "|---|---|---|",
     *[f"| {fmt(r['views'])} | {r['title'][:70]}{' · ' + r['date'] if r['date'] else ''} · {r['minutes']}min | `{r['id']}` |" for r in videos[:10]], ""]
(root / "STATS.md").write_text("\n".join(L))
print(f"ok -> {root}/STATS.md ({len(shorts)} shorts, {len(videos)} videos)")
