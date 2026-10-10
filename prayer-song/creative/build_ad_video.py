#!/usr/bin/env python3
"""Build a Prayer Song video ad from a still, a song and a caption schedule.

ffmpeg on this machine has no drawtext filter, so every piece of burned-in text is
rendered to a transparent PNG with Pillow (using the brand faces) and composited
with ffmpeg's overlay filter.

    python3 prayer-song/creative/build_ad_video.py <slug>

Output: output/ads/2026-10-08-prayer-song-batch1/assets/<slug>.mp4, 1080x1350.
"""
import json, os, subprocess, sys, textwrap
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FONTS = os.path.join(ROOT, "prayer-song/creative/fonts")
OUT = os.path.join(ROOT, "output/ads/2026-10-08-prayer-song-batch1/assets")
WORK = os.path.join(OUT, "_work")
W, H = 1080, 1350

GOLD = (242, 194, 48, 255)
WHITE = (255, 255, 255, 255)
INK = (28, 23, 19, 255)


def font(name, size, weight=None):
    f = ImageFont.truetype(os.path.join(FONTS, name), size)
    if weight:
        try:
            f.set_variation_by_axes([weight])
        except Exception:
            pass
    return f


def wrap(draw, text, fnt, maxw):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= maxw:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def hook_png(path, lines, size=44):
    """Top caption bar: white slab, dark text. The competitor's scroll-stop."""
    fnt = font("Inter-Bold.ttf", size, 600)
    pad_x, pad_y, lead = 46, 34, int(size * 1.38)
    img = Image.new("RGBA", (W, pad_y * 2 + lead * len(lines)), (255, 255, 255, 247))
    d = ImageDraw.Draw(img)
    y = pad_y
    for ln in lines:
        d.text((W / 2, y), ln, font=fnt, fill=INK, anchor="ma")
        y += lead
    img.save(path)
    return img.height


def caption_png(path, text, name=None, size=56):
    """One lyric card. The name, if present, is set in gold so it reads as the variable."""
    fnt = font("Inter-Bold.ttf", size, 700)
    tmp = ImageDraw.Draw(Image.new("RGBA", (10, 10)))
    lines = wrap(tmp, text, fnt, W - 150)
    lead = int(size * 1.3)
    img = Image.new("RGBA", (W, lead * len(lines) + 40), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    y = 20
    for ln in lines:
        # a soft shadow so white type holds on any frame
        for dx, dy in ((0, 3), (2, 2), (-2, 2)):
            d.text((W / 2 + dx, y + dy), ln, font=fnt, fill=(0, 0, 0, 150), anchor="ma")
        if name and name in ln:
            before, _, after = ln.partition(name)
            wb = d.textlength(before, font=fnt)
            wn = d.textlength(name, font=fnt)
            wa = d.textlength(after, font=fnt)
            x = W / 2 - (wb + wn + wa) / 2
            d.text((x, y), before, font=fnt, fill=WHITE)
            d.text((x + wb, y), name, font=fnt, fill=GOLD)
            d.text((x + wb + wn, y), after, font=fnt, fill=WHITE)
        else:
            d.text((W / 2, y), ln, font=fnt, fill=WHITE, anchor="ma")
        y += lead
    img.save(path)
    return img.height


def namecard_png(path, name, size=150):
    fnt = font("Fraunces.ttf", size, 700)
    img = Image.new("RGBA", (W, int(size * 1.5)), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    for dx, dy in ((0, 5), (3, 3), (-3, 3)):
        d.text((W / 2 + dx, 10 + dy), name, font=fnt, fill=(0, 0, 0, 160), anchor="ma")
    d.text((W / 2, 10), name, font=fnt, fill=WHITE, anchor="ma")
    img.save(path)
    return img.height


def disclosure_png(path, lines, size=25):
    fnt = font("Inter-Bold.ttf", size, 500)
    lead = int(size * 1.45)
    h = lead * len(lines) + 34
    img = Image.new("RGBA", (W, h), (28, 23, 19, 205))
    d = ImageDraw.Draw(img)
    y = 17
    for ln in lines:
        d.text((W / 2, y), ln, font=fnt, fill=(255, 255, 255, 225), anchor="ma")
        y += lead
    img.save(path)
    return h


def build(cfg):
    os.makedirs(WORK, exist_ok=True)
    slug = cfg["slug"]
    dur = cfg["duration"]
    still = os.path.join(ROOT, cfg["still"])
    song = os.path.join(ROOT, cfg["song"])

    inputs = ["-loop", "1", "-framerate", "30", "-t", str(dur), "-i", still]
    # slow push, then the overlays are composited on top of it
    # a slow handheld drift. zoompan would not animate off a single looped still,
    # so the movement comes from a time varying crop window instead.
    chain = [f"[0:v]scale=-2:{int(H*1.16)},"
             f"crop={W}:{H}:"
             f"x='(in_w-{W})/2+22*sin(t/13)':"
             f"y='(in_h-{H})/2+15*sin(t/17)',"
             f"setsar=1,fps=30[bg]"]
    last = "bg"
    idx = 1

    if cfg.get("hook"):
        p = os.path.join(WORK, f"{slug}-hook.png")
        hh = hook_png(p, cfg["hook"])
        inputs += ["-i", p]
        chain.append(f"[{last}][{idx}:v]overlay=0:0[v{idx}]")
        last = f"v{idx}"
        idx += 1
        hook_h = hh
    else:
        hook_h = 0

    disc_h = 0
    if cfg.get("disclosure"):
        p = os.path.join(WORK, f"{slug}-disc.png")
        disc_h = disclosure_png(p, cfg["disclosure"])
        disc_path, disc_idx = p, None  # composited last so nothing covers it

    cap_bottom = H - disc_h - 42
    for i, c in enumerate(cfg["captions"]):
        p = os.path.join(WORK, f"{slug}-cap{i}.png")
        if c.get("namecard"):
            ch = namecard_png(p, c["text"])
            y = int(H * 0.42)
        else:
            ch = caption_png(p, c["text"], c.get("name"))
            y = cap_bottom - ch
        inputs += ["-i", p]
        chain.append(
            f"[{last}][{idx}:v]overlay=0:{y}:enable='between(t,{c['in']},{c['out']})'[v{idx}]")
        last = f"v{idx}"
        idx += 1

    if disc_h:
        inputs += ["-i", disc_path]
        chain.append(f"[{last}][{idx}:v]overlay=0:{H-disc_h}[v{idx}]")
        last = f"v{idx}"
        idx += 1

    inputs += ["-ss", str(cfg.get("song_start", 0)), "-t", str(dur), "-i", song]
    audio_idx = idx
    chain.append(f"[{audio_idx}:a]afade=t=out:st={dur-2}:d=2[a]")

    cmd = ["ffmpeg", "-v", "error", "-y"] + inputs + [
        "-filter_complex", ";".join(chain),
        "-map", f"[{last}]", "-map", "[a]",
        "-c:v", "libx264", "-profile:v", "high", "-pix_fmt", "yuv420p",
        "-r", "30", "-b:v", "4M", "-c:a", "aac", "-b:a", "128k", "-ar", "44100",
        "-movflags", "+faststart", "-t", str(dur),
        os.path.join(OUT, f"{slug}.mp4")]
    subprocess.run(cmd, check=True)
    return os.path.join(OUT, f"{slug}.mp4")


if __name__ == "__main__":
    cfgs = json.load(open(os.path.join(ROOT, "prayer-song/creative/ad-video-specs.json")))
    want = sys.argv[1] if len(sys.argv) > 1 else None
    for c in cfgs:
        if want and c["slug"] != want:
            continue
        out = build(c)
        print("built", out)
