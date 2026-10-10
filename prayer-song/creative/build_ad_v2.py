#!/usr/bin/env python3
"""Prayer Song ad, version 2.

What changed from v1, and why: v1 was a single still with a 22px drift for 75
seconds, which on mute was a photograph with slow subtitles. The client was
right to reject it. v2 uses real generated motion, cuts between three scenes so
something changes every few seconds, and runs 25 seconds instead of 75.

Each source clip is 5s and loops cleanly (start_image == end_image), so a scene
can be repeated without a visible jump.

    python3 prayer-song/creative/build_ad_v2.py
"""
import os, subprocess
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FONTS = os.path.join(ROOT, "prayer-song/creative/fonts")
A = os.path.join(ROOT, "output/ads/2026-10-08-prayer-song-batch1/assets")
WORK = os.path.join(A, "_v2")
W, H = 1080, 1350
GOLD = (242, 194, 48, 255)
WHITE = (255, 255, 255, 255)

SONG = os.path.join(ROOT, "prayer-song/demo-data/songs/4e076f8a5f6d6e07cd766084dac7ae82.mp3")

# scene, seconds. Something changes every 5s, which is the whole point of v2.
# v3: the people b-roll leads. Opening on a grown man quietly moved is the
# scroll stop; the empty rooms are gone.
SHOTS = [("broll/clip_mother_son.mp4", 5), ("broll/clip_mother_daughter.mp4", 5),
         ("broll/clip_older_couple.mp4", 5), ("broll/clip_mother_son.mp4", 5),
         ("broll/clip_mother_daughter.mp4", 5)]

# every line verbatim from Call Daniel Home
CAPTIONS = [
    (1.0,  5.0,  "He's wandered far from where we pray", None),
    (5.5,  9.5,  "Still every Sunday the telephone rings", None),
    (10.0, 13.0, "Daniel", "NAME"),
    (13.5, 18.0, "Lord, call Daniel home to You", "Daniel"),
    (18.5, 23.5, "I cannot walk his road for him", None),
]
# The burned-in "not a customer" label was removed at TS's direction on
# 2026-10-10. Nothing in these films claims a testimonial: nobody looks at the
# camera and no mouth is open. Keep the primary text clear of anything that
# implies these people bought the product. Put the lines back by filling this
# list in again; BOTTOM below keeps the captions in the same place either way.
DISCLOSURE = []


def font(name, size, weight=None):
    f = ImageFont.truetype(os.path.join(FONTS, name), size)
    if weight:
        try:
            f.set_variation_by_axes([weight])
        except Exception:
            pass
    return f


def wrap(d, text, fnt, maxw):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=fnt) <= maxw:
            cur = t
        else:
            lines.append(cur) if cur else None
            cur = w
    if cur:
        lines.append(cur)
    return lines


def caption_png(path, text, name=None, size=60):
    fnt = font("Inter-Bold.ttf", size, 700)
    probe = ImageDraw.Draw(Image.new("RGBA", (10, 10)))
    lines = wrap(probe, text, fnt, W - 140)
    lead = int(size * 1.28)
    img = Image.new("RGBA", (W, lead * len(lines) + 40), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    y = 20
    for ln in lines:
        for dx, dy in ((0, 4), (3, 3), (-3, 3), (0, 0)):
            if (dx, dy) != (0, 0):
                d.text((W / 2 + dx, y + dy), ln, font=fnt, fill=(0, 0, 0, 165), anchor="ma")
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


def namecard_png(path, name, size=170):
    fnt = font("Fraunces.ttf", size, 700)
    img = Image.new("RGBA", (W, int(size * 1.5)), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    for dx, dy in ((0, 6), (4, 4), (-4, 4)):
        d.text((W / 2 + dx, 10 + dy), name, font=fnt, fill=(0, 0, 0, 170), anchor="ma")
    d.text((W / 2, 10), name, font=fnt, fill=GOLD, anchor="ma")
    img.save(path)
    return img.height


def disclosure_png(path, lines, size=24):
    fnt = font("Inter-Bold.ttf", size, 500)
    lead = int(size * 1.45)
    h = lead * len(lines) + 30
    img = Image.new("RGBA", (W, h), (28, 23, 19, 200))
    d = ImageDraw.Draw(img)
    y = 15
    for ln in lines:
        d.text((W / 2, y), ln, font=fnt, fill=(255, 255, 255, 220), anchor="ma")
        y += lead
    img.save(path)
    return h


def main():
    os.makedirs(WORK, exist_ok=True)
    total = sum(s for _, s in SHOTS)

    # 1. normalise every shot to 1080x1350 and concat into the spine
    parts = []
    for i, (clip, secs) in enumerate(SHOTS):
        src = os.path.join(A, clip)
        if not os.path.exists(src):
            raise SystemExit(f"missing clip: {src}")
        p = os.path.join(WORK, f"shot{i}.mp4")
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-stream_loop", "-1", "-i", src,
                        "-t", str(secs),
                        "-vf", f"scale={W}:-2:flags=lanczos,crop={W}:{H},setsar=1,fps=30",
                        "-an", "-c:v", "libx264", "-pix_fmt", "yuv420p", p], check=True)
        parts.append(p)
    lst = os.path.join(WORK, "list.txt")
    open(lst, "w").write("".join(f"file '{p}'\n" for p in parts))
    spine = os.path.join(WORK, "spine.mp4")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0",
                    "-i", lst, "-c", "copy", spine], check=True)

    # 2. overlays
    disc_h = disclosure_png(os.path.join(WORK, "disc.png"), DISCLOSURE) if DISCLOSURE else 0
    bottom = disc_h + 50 if DISCLOSURE else 150
    inputs = ["-i", spine]
    chain, last, idx = [], "0:v", 1
    for i, (tin, tout, text, kind) in enumerate(CAPTIONS):
        p = os.path.join(WORK, f"cap{i}.png")
        if kind == "NAME":
            ch = namecard_png(p, text)
            y = int(H * 0.40)
        else:
            ch = caption_png(p, text, kind)
            y = H - bottom - ch
        inputs += ["-i", p]
        chain.append(f"[{last}][{idx}:v]overlay=0:{y}:enable='between(t,{tin},{tout})'[v{idx}]")
        last = f"v{idx}"
        idx += 1
    if DISCLOSURE:
        inputs += ["-i", os.path.join(WORK, "disc.png")]
        chain.append(f"[{last}][{idx}:v]overlay=0:{H-disc_h}[v{idx}]")
        last = f"v{idx}"
        idx += 1

    inputs += ["-i", SONG]
    chain.append(f"[{idx}:a]atrim=0:{total},afade=t=out:st={total-1.5}:d=1.5[a]")

    out = os.path.join(A, "V3_SungByName_Broll_25s.mp4")
    subprocess.run(["ffmpeg", "-v", "error", "-y"] + inputs +
                   ["-filter_complex", ";".join(chain),
                    "-map", f"[{last}]", "-map", "[a]",
                    "-c:v", "libx264", "-profile:v", "high", "-pix_fmt", "yuv420p",
                    "-r", "30", "-b:v", "5M", "-c:a", "aac", "-b:a", "128k",
                    "-movflags", "+faststart", "-t", str(total), out], check=True)
    print("built", out, f"({total}s)")


if __name__ == "__main__":
    main()
