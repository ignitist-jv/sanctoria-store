#!/usr/bin/env python3
"""Batch 2: four 30 second films, each opening on a recipient we have never used.

Built from four new b-roll clips plus the three from batch 1, reused and
reordered the way build_variants.py does. The thing being tested is the
recipient and the occasion, so each film opens on its own scene and its own
name card.

    python3 prayer-song/creative/build_batch2.py
"""
import os, subprocess, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_ad_v2 import caption_png, namecard_png, A, WORK, W, H, SONG

B = "broll/"

VARIANTS = [
    {
        "slug": "V7_FontAndTheName_30s",
        "song_start": 0,
        "shots": [(B+"clip_christening_gown.mp4", 5), (B+"clip_confirmation.mp4", 5),
                  (B+"clip_christening_gown.mp4", 5), (B+"clip_vow_renewal.mp4", 5),
                  (B+"clip_christening_gown.mp4", 5), (B+"clip_confirmation.mp4", 5)],
        "captions": [
            (2.0, 7.0,   "Water on his head, a name said twice", None),
            (7.5, 12.0,  "The whole church heard it, Lord, and so did You", None),
            (12.5, 16.0, "Michael", "NAME"),
            (16.5, 22.0, "Keep Michael in Your hand", "Michael"),
            (22.5, 27.0, "Guard the name You gave him", None),
            (27.5, 29.8, "All his life, and after", None),
        ],
    },
    {
        "slug": "V8_NobodySaysHers_30s",
        "song_start": 62,
        "shots": [(B+"clip_elderly_mother.mp4", 5), (B+"clip_mother_daughter.mp4", 5),
                  (B+"clip_elderly_mother.mp4", 5), (B+"clip_older_couple.mp4", 5),
                  (B+"clip_elderly_mother.mp4", 5), (B+"clip_mother_daughter.mp4", 5)],
        "captions": [
            (2.0, 7.0,   "She says our names before she sleeps", None),
            (7.5, 12.0,  "Every one of us, out loud, to You", None),
            (12.5, 16.0, "Nora", "NAME"),
            (16.5, 22.0, "Tonight, Lord, hear hers", None),
            (22.5, 27.0, "Bless Nora, who has prayed for all of us", "Nora"),
            (27.5, 29.8, "Give her peace, and rest", None),
        ],
    },
    {
        "slug": "V9_FiftyYearsTwoNames_30s",
        "song_start": 100,
        "shots": [(B+"clip_vow_renewal.mp4", 5), (B+"clip_older_couple.mp4", 5),
                  (B+"clip_vow_renewal.mp4", 5), (B+"clip_elderly_mother.mp4", 5),
                  (B+"clip_vow_renewal.mp4", 5), (B+"clip_older_couple.mp4", 5)],
        "captions": [
            (2.0, 7.0,   "Fifty years since the vow was made", None),
            (7.5, 12.0,  "The same church, the same two hands", None),
            (12.5, 16.0, "John and Eileen", "NAME"),
            (16.5, 22.0, "Lord, bless John and Eileen", None),
            (22.5, 27.0, "What You joined, keep joined", None),
            (27.5, 29.8, "All the years still to come", None),
        ],
    },
    {
        "slug": "V10_GodmothersPromise_30s",
        "song_start": 150,
        "shots": [(B+"clip_confirmation.mp4", 5), (B+"clip_mother_daughter.mp4", 5),
                  (B+"clip_confirmation.mp4", 5), (B+"clip_christening_gown.mp4", 5),
                  (B+"clip_confirmation.mp4", 5), (B+"clip_older_couple.mp4", 5)],
        "captions": [
            (2.0, 7.0,   "I held her at the font and promised", None),
            (7.5, 12.0,  "To bring her up in the faith, Lord", None),
            (12.5, 16.0, "Clare", "NAME"),
            (16.5, 22.0, "Seal Clare with Your Spirit", "Clare"),
            (22.5, 27.0, "Keep the promise I made for her", None),
            (27.5, 29.8, "Hold her, all her life", None),
        ],
    },
]


def build(v):
    os.makedirs(WORK, exist_ok=True)
    slug = v["slug"]
    total = sum(s for _, s in v["shots"])

    parts = []
    for i, (clip, secs) in enumerate(v["shots"]):
        src = os.path.join(A, clip)
        if not os.path.exists(src):
            raise SystemExit(f"missing clip: {src}")
        p = os.path.join(WORK, f"{slug}_s{i}.mp4")
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-stream_loop", "-1", "-i", src,
                        "-t", str(secs),
                        "-vf", f"scale={W}:-2:flags=lanczos,crop={W}:{H},setsar=1,fps=30",
                        "-an", "-c:v", "libx264", "-pix_fmt", "yuv420p", p], check=True)
        parts.append(p)
    lst = os.path.join(WORK, f"{slug}.txt")
    open(lst, "w").write("".join(f"file '{p}'\n" for p in parts))
    spine = os.path.join(WORK, f"{slug}_spine.mp4")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0",
                    "-i", lst, "-c", "copy", spine], check=True)

    bottom = 150
    inputs = ["-i", spine]
    chain, last, idx = [], "0:v", 1
    for i, (tin, tout, text, kind) in enumerate(v["captions"]):
        p = os.path.join(WORK, f"{slug}_c{i}.png")
        if kind == "NAME":
            # two names need a smaller face so the card still fits the frame
            size = 110 if len(text) > 8 else 170
            ch = namecard_png(p, text, size=size)
            y = int(H * 0.40)
        else:
            ch = caption_png(p, text, kind)
            y = H - bottom - ch
        inputs += ["-i", p]
        chain.append(f"[{last}][{idx}:v]overlay=0:{y}:enable='between(t,{tin},{tout})'[v{idx}]")
        last = f"v{idx}"
        idx += 1

    inputs += ["-ss", str(v["song_start"]), "-i", SONG]
    chain.append(f"[{idx}:a]atrim=0:{total},afade=t=out:st={total-1.5}:d=1.5[a]")

    out = os.path.join(A, f"{slug}.mp4")
    subprocess.run(["ffmpeg", "-v", "error", "-y"] + inputs +
                   ["-filter_complex", ";".join(chain),
                    "-map", f"[{last}]", "-map", "[a]",
                    "-c:v", "libx264", "-profile:v", "high", "-pix_fmt", "yuv420p",
                    "-r", "30", "-b:v", "5M", "-c:a", "aac", "-b:a", "128k",
                    "-movflags", "+faststart", "-t", str(total), out], check=True)
    print(f"built {slug}.mp4  ({total}s, opens on {v['shots'][0][0].split('/')[-1]})")


if __name__ == "__main__":
    for v in VARIANTS:
        build(v)
