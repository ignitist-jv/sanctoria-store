#!/usr/bin/env python3
"""Batch 2, rebuilt 2026-10-13 after TS's review.

Three things changed from the first cut:
  1. NO CLIP REPEATS INSIDE A FILM. Each 25s film is five DISTINCT clips from
     the seven-clip pool. The first cut reused one scene three times in 30s.
  2. Nicer captions: a soft bottom scrim so white type sits on something, a
     lighter shadow, better leading, and the name in gold.
  3. Captions now read as four consecutive lines of one sung prayer instead of
     disconnected lines. Film C uses four VERBATIM lines from the real sample
     song "Hold Anna and Tomasz Near".

    python3 prayer-song/creative/build_batch2.py
"""
import os, subprocess, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_ad_v2 import font, wrap, namecard_png, A, WORK, W, H, SONG, WHITE, GOLD
from PIL import Image, ImageDraw

B = "broll/"
SCRIM_H = 430          # height of the bottom gradient
CAP_SIZE = 56


def scrim_png(path):
    """Soft bottom gradient so white type always has something to sit on."""
    img = Image.new("RGBA", (W, SCRIM_H), (0, 0, 0, 0))
    px = img.load()
    for y in range(SCRIM_H):
        t = y / (SCRIM_H - 1)
        a = int(205 * (t ** 1.7))        # eased, so the top edge is invisible
        for x in range(W):
            px[x, y] = (12, 9, 7, a)
    img.save(path)
    return SCRIM_H


def caption_png(path, text, name=None, size=CAP_SIZE):
    fnt = font("Inter-Bold.ttf", size, 700)
    probe = ImageDraw.Draw(Image.new("RGBA", (10, 10)))
    lines = wrap(probe, text, fnt, W - 180)
    lead = int(size * 1.34)
    img = Image.new("RGBA", (W, lead * len(lines) + 36), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    y = 18
    for ln in lines:
        # softer, tighter shadow than the first cut; the scrim does the heavy lifting
        for dx, dy in ((0, 3), (2, 2), (-2, 2)):
            d.text((W / 2 + dx, y + dy), ln, font=fnt, fill=(0, 0, 0, 120), anchor="ma")
        if name and name in ln:
            b, _, a2 = ln.partition(name)
            wb, wn, wa = (d.textlength(x, font=fnt) for x in (b, name, a2))
            x = W / 2 - (wb + wn + wa) / 2
            d.text((x, y), b, font=fnt, fill=WHITE)
            d.text((x + wb, y), name, font=fnt, fill=GOLD)
            d.text((x + wb + wn, y), a2, font=fnt, fill=WHITE)
        else:
            d.text((W / 2, y), ln, font=fnt, fill=WHITE, anchor="ma")
        y += lead
    img.save(path)
    return img.height


# five beats across 25s; beat 3 is the name card
BEATS = [(1.5, 6.0), (6.5, 11.0), (11.5, 14.5), (15.0, 19.5), (20.0, 24.6)]

VARIANTS = [
    {
        "slug": "V7_FontAndTheName_25s",
        "song_start": 0,
        "shots": [B+"clip_christening_gown.mp4", B+"clip_mother_daughter.mp4",
                  B+"clip_confirmation.mp4", B+"clip_older_couple.mp4",
                  B+"clip_elderly_mother.mp4"],
        "lines": [("I fold the christening gown away,", None),
                  ("Water and a name, one spring day,", None),
                  ("Michael", "NAME"),
                  ("Lord, keep Michael in that grace,", "Michael"),
                  ("I cannot hold him, so I pray.", None)],
    },
    {
        "slug": "V8_NobodySaysHers_25s",
        "song_start": 62,
        "shots": [B+"clip_elderly_mother.mp4", B+"clip_mother_daughter.mp4",
                  B+"clip_christening_gown.mp4", B+"clip_vow_renewal.mp4",
                  B+"clip_mother_son.mp4"],
        "lines": [("She prays for all of us by name,", None),
                  ("And no one prays for her by name,", None),
                  ("Nora", "NAME"),
                  ("Lord, look at Nora in that chair,", "Nora"),
                  ("Hold the hands that held us there.", None)],
    },
    {
        # four VERBATIM consecutive chorus lines from the real sample song
        # "Hold Anna and Tomasz Near" (1 Corinthians 13:7).
        "slug": "V9_HoldThemNear_25s",
        "song_start": 100,
        "shots": [B+"clip_vow_renewal.mp4", B+"clip_older_couple.mp4",
                  B+"clip_mother_daughter.mp4", B+"clip_christening_gown.mp4",
                  B+"clip_elderly_mother.mp4"],
        "lines": [("Father, hold Anna and Tomasz near,", None),
                  ("Give them grace when the road is long,", None),
                  ("Anna and Tomasz", "NAME"),
                  ("Soften the words that are hard to hear,", None),
                  ("Let their love be kind and strong.", None)],
    },
    {
        "slug": "V10_GodmothersPromise_25s",
        "song_start": 150,
        "shots": [B+"clip_confirmation.mp4", B+"clip_christening_gown.mp4",
                  B+"clip_mother_son.mp4", B+"clip_older_couple.mp4",
                  B+"clip_vow_renewal.mp4"],
        "lines": [("I answered for her at the font,", None),
                  ("Today she answers for herself,", None),
                  ("Clare", "NAME"),
                  ("Our Lady, keep Clare in her word,", "Clare"),
                  ("I lift my hand, Lord. She is Yours.", None)],
    },
]


def build(v):
    os.makedirs(WORK, exist_ok=True)
    slug = v["slug"]
    shots = v["shots"]
    assert len(shots) == len(set(shots)), f"{slug}: a clip repeats inside the film"
    secs = 5
    total = secs * len(shots)

    parts = []
    for i, clip in enumerate(shots):
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

    sp = os.path.join(WORK, f"{slug}_scrim.png")
    scrim_png(sp)

    inputs = ["-i", spine, "-i", sp]
    chain = [f"[0:v][1:v]overlay=0:{H-SCRIM_H}[v1]"]
    last, idx = "v1", 2

    for i, ((tin, tout), (text, kind)) in enumerate(zip(BEATS, v["lines"])):
        p = os.path.join(WORK, f"{slug}_c{i}.png")
        if kind == "NAME":
            size = 108 if len(text) > 8 else 162
            ch = namecard_png(p, text, size=size)
            y = int(H * 0.40)
        else:
            ch = caption_png(p, text, kind)
            y = H - 150 - ch
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
    print(f"built {slug}.mp4  {total}s, {len(shots)} distinct clips, opens on {shots[0].split('/')[-1]}")


if __name__ == "__main__":
    for v in VARIANTS:
        build(v)
