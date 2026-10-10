#!/usr/bin/env python3
"""Three more ad variants cut from the clips we already have.

The thing being tested is the first second, so each variant opens on a
different face and a different structure. No new generation.

    python3 prayer-song/creative/build_variants.py
"""
import os, subprocess, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_ad_v2 import (caption_png, namecard_png, disclosure_png, A, WORK, W, H, SONG)
from PIL import Image


def scrim_png(path, alpha=165):
    """Full frame darkener, so the opening name reads as a title card."""
    Image.new("RGBA", (W, H), (18, 14, 11, alpha)).save(path)


DISC = ["An illustration made by Sanctoria. Not a customer.",
        "A sample prayer song. Not a customer's song."]

VARIANTS = [
    {
        # opens on the crying mother. The conventional emotional opener, and
        # the control against the two odder ones below.
        "slug": "V4_DaughterOpen_25s",
        "song_start": 62,
        "shots": [("broll/clip_mother_daughter.mp4", 5), ("broll/clip_mother_son.mp4", 5),
                  ("broll/clip_older_couple.mp4", 5), ("broll/clip_mother_daughter.mp4", 5),
                  ("broll/clip_mother_son.mp4", 5)],
        "captions": [
            (1.0, 5.5,  "Still every Sunday the telephone rings", None),
            (6.0, 10.5, "He asks how I am and tells me small things", None),
            (11.0, 14.0, "Daniel", "NAME"),
            (14.5, 19.0, "Hold my Daniel close to Thee", "Daniel"),
            (19.5, 24.0, "Mary, pray for him tonight", None),
        ],
    },
    {
        # half the length, three shots, no repeats. Tests whether 15s beats 25s.
        "slug": "V5_CoupleOpen_15s",
        "song_start": 0,
        "shots": [("broll/clip_older_couple.mp4", 5), ("broll/clip_mother_son.mp4", 5),
                  ("broll/clip_mother_daughter.mp4", 5)],
        "captions": [
            (0.8, 5.0,  "Lord, call Daniel home to You", "Daniel"),
            (5.5, 8.5,  "Daniel", "NAME"),
            (9.0, 14.0, "I cannot walk his road for him", None),
        ],
    },
    {
        # the name lands in the first second. Nobody scrolling expects a
        # specific first name, so the pattern interrupt leads instead of
        # arriving halfway through.
        "slug": "V6_NameFirst_25s",
        "song_start": 100,
        "shots": [("broll/clip_mother_son.mp4", 5), ("broll/clip_older_couple.mp4", 5),
                  ("broll/clip_mother_daughter.mp4", 5), ("broll/clip_older_couple.mp4", 5),
                  ("broll/clip_mother_son.mp4", 5)],
        "scrim": (0.0, 3.5),
        "captions": [
            (0.4, 3.5,  "Daniel", "NAME"),
            (4.0, 9.0,  "He's wandered far from where we pray", None),
            (9.5, 15.0, "Father, hear a mother's plea", None),
            (15.5, 20.0, "Keep the door of mercy wide", None),
            (20.5, 24.0, "So into Your hands I let him go", None),
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

    disc_p = os.path.join(WORK, f"{slug}_disc.png")
    disc_h = disclosure_png(disc_p, DISC)

    inputs = ["-i", spine]
    chain, last, idx = [], "0:v", 1
    if v.get("scrim"):
        sp = os.path.join(WORK, f"{slug}_scrim.png")
        scrim_png(sp)
        sin, sout = v["scrim"]
        inputs += ["-i", sp]
        chain.append(f"[{last}][{idx}:v]overlay=0:0:enable='between(t,{sin},{sout})'[v{idx}]")
        last = f"v{idx}"
        idx += 1
    for i, (tin, tout, text, kind) in enumerate(v["captions"]):
        p = os.path.join(WORK, f"{slug}_c{i}.png")
        if kind == "NAME":
            ch = namecard_png(p, text)
            y = int(H * 0.40)
        else:
            ch = caption_png(p, text, kind)
            y = H - disc_h - 50 - ch
        inputs += ["-i", p]
        chain.append(f"[{last}][{idx}:v]overlay=0:{y}:enable='between(t,{tin},{tout})'[v{idx}]")
        last = f"v{idx}"
        idx += 1
    inputs += ["-i", disc_p]
    chain.append(f"[{last}][{idx}:v]overlay=0:{H-disc_h}[v{idx}]")
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
    want = sys.argv[1] if len(sys.argv) > 1 else None
    for v in VARIANTS:
        if want and v["slug"] != want:
            continue
        build(v)
