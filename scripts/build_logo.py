#!/usr/bin/env python3
"""
Rebuild the Sanctoria logo files from the high resolution artwork TS supplied on 2026-10-07
(images-originals/logo/logo-source-1111.jpg: gold cross, black lettering, underline, on cream inside a gold ring).

The old site/images/logo.png was a small export with a grey checker pattern baked into the centres of the "o" and "a".
This cuts the three parts out of the new artwork, drops the ring and the cream ground, and lays them out in the same
proportions as the old file, so every page that uses the logo keeps its layout.

  python3 scripts/build_logo.py        -> site/images/logo.png (dark lettering, for light pages)
                                          site/prayer-song/img/logo-light.png (cream lettering, for the dark footer)
"""
import math
from collections import deque
from pathlib import Path
from PIL import Image, ImageFilter

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "images-originals/logo/logo-source-1111.jpg"
W, H = 956, 440                      # twice the old 478 x 220


def cut(im, box, fill_small_only, tight=False, skip=None):
    """One part of the artwork as RGBA: cream ground removed, edges soft, glossy highlights kept solid."""
    x0, y0, x1, y1 = box
    part = im.crop(box)
    w, h = part.size
    px = part.load()
    bg = (254, 247, 231)
    cx, cy = 555.5, 555.5
    solid = [[False] * w for _ in range(h)]
    dist = [[0.0] * w for _ in range(h)]
    for y in range(h):
        for x in range(w):
            r, g, b = px[x, y]
            d = math.sqrt((r - bg[0]) ** 2 + (g - bg[1]) ** 2 + (b - bg[2]) ** 2)
            if math.hypot(x + x0 - cx, y + y0 - cy) > 515:        # the ring, and everything outside it (the lettering comes within a few pixels of it)
                d = 0.0
            if skip and skip[0] <= x + x0 <= skip[2] and skip[1] <= y + y0 <= skip[3]:   # a neighbouring part that pokes into this box
                d = 0.0
            dist[y][x] = d
            # tight: only the lettering itself, without the soft embossed shadow around it (for recolouring on a dark ground)
            solid[y][x] = d > (120 if tight else 34)
    # enclosed light patches: glossy highlights are small and get filled; the centres of o and a are large and stay open
    seen = [[False] * w for _ in range(h)]
    q = deque()
    for x in range(w):
        for y in (0, h - 1):
            if not solid[y][x] and not seen[y][x]:
                seen[y][x] = True; q.append((x, y))
    for y in range(h):
        for x in (0, w - 1):
            if not solid[y][x] and not seen[y][x]:
                seen[y][x] = True; q.append((x, y))
    while q:
        x, y = q.popleft()
        for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if 0 <= nx < w and 0 <= ny < h and not solid[ny][nx] and not seen[ny][nx]:
                seen[ny][nx] = True; q.append((nx, ny))
    fill = [[False] * w for _ in range(h)]
    for y in range(h):
        for x in range(w):
            if not solid[y][x] and not seen[y][x]:
                comp = [(x, y)]; seen[y][x] = True; i = 0
                while i < len(comp):
                    ax, ay = comp[i]; i += 1
                    for nx, ny in ((ax + 1, ay), (ax - 1, ay), (ax, ay + 1), (ax, ay - 1)):
                        if 0 <= nx < w and 0 <= ny < h and not solid[ny][nx] and not seen[ny][nx]:
                            seen[ny][nx] = True; comp.append((nx, ny))
                if not fill_small_only or len(comp) < 700:
                    for ax, ay in comp:
                        fill[ay][ax] = True
    alpha = Image.new("L", (w, h), 0)
    ap = alpha.load()
    for y in range(h):
        for x in range(w):
            if solid[y][x] or fill[y][x]:
                ap[x, y] = 255
            else:
                lo, span = (96, 24) if tight else (14, 20)
                ap[x, y] = max(0, min(255, int((dist[y][x] - lo) / span * 255)))   # the soft edge
    alpha = alpha.filter(ImageFilter.GaussianBlur(0.7))
    out = part.convert("RGBA")
    out.putalpha(alpha)
    bbox = alpha.point(lambda v: 255 if v > 40 else 0).getbbox()
    cut.last_bbox = bbox
    return out.crop(bbox)


def lettering_flat(im, box, rgb, like, skip):
    """The lettering as one flat colour for a dark ground: taken from its black body only (no gold rim, no shadow),
    thickened by the width of the rim and smoothed, then cropped to the same box as the full colour lettering."""
    part = im.crop(box)
    part.paste((254, 247, 231), (skip[0] - box[0], skip[1] - box[1], skip[2] - box[0], skip[3] - box[1]))   # the foot of the cross
    pp = part.load()
    for yy in range(part.height):                                   # and the ring, which passes just outside the first and last letters
        for xx in range(part.width):
            if math.hypot(xx + box[0] - 555.5, yy + box[1] - 555.5) > 515:
                pp[xx, yy] = (254, 247, 231)
    body = part.convert("RGB").point(lambda v: 255 if v < 100 else 0).convert("L")      # dark in every channel
    r, g, b = part.split()
    body = Image.merge("RGB", (r.point(lambda v: 255 if v < 100 else 0), g.point(lambda v: 255 if v < 100 else 0),
                               b.point(lambda v: 255 if v < 100 else 0))).convert("L").point(lambda v: 255 if v > 250 else 0)
    body = body.filter(ImageFilter.MaxFilter(7)).filter(ImageFilter.MinFilter(3))        # close the glossy streaks, add the rim's width
    body = body.filter(ImageFilter.GaussianBlur(1.1))
    flat = Image.new("RGBA", part.size, rgb + (0,))
    flat.putalpha(body)
    return flat.crop(like)


def place(canvas, part, width, centre_x, top):
    scale = width / part.width
    p = part.resize((round(part.width * scale), round(part.height * scale)), Image.LANCZOS)
    canvas.alpha_composite(p, (round(centre_x - p.width / 2), round(top)))
    return p.height


def recolour(part, rgb):
    """Lettering in one flat colour, for a dark ground."""
    flat = Image.new("RGBA", part.size, rgb + (0,))
    flat.putalpha(part.getchannel("A"))
    return flat


def main():
    im = Image.open(SRC).convert("RGB")
    cross = cut(im, (380, 150, 735, 600), fill_small_only=False)
    under_cross = (470, 560, 640, 603)                                   # the foot of the cross dips into the lettering's box
    word = cut(im, (60, 575, 1055, 800), fill_small_only=True, skip=under_cross)
    word_box = cut.last_bbox
    word_light = lettering_flat(im, (60, 575, 1055, 800), (246, 238, 223), word_box, under_cross)
    cross_tight = cut(im, (380, 150, 735, 600), fill_small_only=False, tight=True)      # no soft shadow: it would show as a pale halo on dark
    line_tight = cut(im, (160, 805, 950, 915), fill_small_only=False, tight=True)
    line = cut(im, (160, 805, 950, 915), fill_small_only=False)
    for name, lettering, cross, line in (("site/images/logo.png", word, cross, line), ("site/prayer-song/img/logo-light.png", word_light, cross_tight, line_tight)):
        canvas = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        place(canvas, lettering, W - 10, W / 2, 152)
        place(canvas, cross, 146, W * 0.487, 0)
        place(canvas, line, 640, W / 2, 364)
        # Saved at 478 x 220, the size of the old file: still three times the largest size it is shown at, and a
        # fraction of the weight. An adaptive palette keeps the gold smooth; the alpha channel is kept in full.
        small = canvas.resize((W // 2, H // 2), Image.LANCZOS)
        rgb = small.convert("RGB").quantize(colors=192, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE).convert("RGB")
        small = Image.merge("RGBA", (*rgb.split(), small.getchannel("A")))
        small.save(ROOT / name, optimize=True)
        print("wrote", name, small.size, (ROOT / name).stat().st_size // 1024, "KB")


if __name__ == "__main__":
    main()
