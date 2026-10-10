#!/usr/bin/env python3
"""Sanctoria social images, built not generated.

Deterministic: same input, same output, every time. No seeds, no model drift,
and no "AI content" label from Facebook, because the only photography used is
the real supplier photography already on the site.

Brand system read straight off the live site: cream #F7F3EC, bronze #9A7B4F,
ink #2A1F1A, Fraunces headlines, Inter body.

    python3 social/build_images.py
"""
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT   = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT    = os.path.join(ROOT, 'site', 'social')   # inside site/ so the existing FTPS deploy
                                               # publishes them and Instagram gets a public URL
FONTS  = os.path.join(ROOT, 'social', 'fonts')
FR     = os.path.join(FONTS, 'Fraunces.ttf')
IN     = os.path.join(FONTS, 'Inter.ttf')

W, H   = 1080, 1350
CREAM  = (247, 243, 236)
INK    = (42, 31, 26)
BRONZE = (154, 123, 79)
MUTED  = (138, 124, 106)

# Crops into the real rosary photograph (695 x 695).
CROPS = {
    'full':     None,
    'crucifix': (330, 410, 695, 695),
    'beads':    (40,  40,  560, 420),
}


def keyed(path, target_w, crop=None):
    """Load a supplier photo and turn its white studio ground into brand cream.

    Every near-white pixel is recoloured on a soft ramp, so the ground outside
    the product and the gaps enclosed inside it are treated identically. No
    connected-component threshold, so nothing can accidentally eat a silver
    medal or the corpus.
    """
    im = Image.open(path).convert('RGB')
    if crop:
        im = im.crop(crop)
    a = np.asarray(im).astype(np.float32)
    w = np.clip((a.min(axis=-1) - 232.0) / 16.0, 0.0, 1.0)
    w = np.asarray(Image.fromarray((w * 255).astype(np.uint8))
                   .filter(ImageFilter.GaussianBlur(0.8))).astype(np.float32) / 255.0
    flat = a * (1 - w)[..., None] + np.array(CREAM, dtype=np.float32) * w[..., None]
    img  = Image.fromarray(np.clip(flat, 0, 255).astype(np.uint8))
    subj = Image.fromarray(((w < 0.5) * 255).astype(np.uint8))
    bb = subj.getbbox()
    img, subj = img.crop(bb), subj.crop(bb)
    sc = target_w / img.width
    size = (target_w, round(img.height * sc))
    return img.resize(size, Image.LANCZOS), subj.resize(size, Image.LANCZOS)


def tracked(d, cx, y, text, font, fill, track):
    """Letterspaced centred text, for the small-caps eyebrow."""
    widths = [d.textlength(c, font=font) for c in text]
    x = cx - (sum(widths) + track * (len(text) - 1)) / 2
    for c, wd in zip(text, widths):
        d.text((x, y), c, font=font, fill=fill)
        x += wd + track


def build(name, eyebrow, lines, mode='hero', photo='rosary-1.jpg', crop='full',
          size=74, foot=None):
    c = Image.new('RGB', (W, H), CREAM)
    d = ImageDraw.Draw(c)

    lg = Image.open(os.path.join(ROOT, 'site/images/logo.png')).convert('RGBA')
    lg = lg.resize((round(lg.width * 76 / lg.height), 76), Image.LANCZOS)
    c.paste(lg, ((W - lg.width) // 2, 74), lg)

    if eyebrow:
        tracked(d, W / 2, 196, eyebrow.upper(), ImageFont.truetype(IN, 19), BRONZE, 7)

    f_h = ImageFont.truetype(FR, size)
    lead = round(size * 1.24)
    y = 248 if mode != 'type' else 330
    for ln in lines:
        d.text((W / 2, y), ln, font=f_h, fill=INK, anchor="ma")
        y += lead

    if mode == 'type':
        d.line([(W / 2 - 54, y + 46), (W / 2 + 54, y + 46)], fill=BRONZE, width=2)
        if foot:
            d.text((W / 2, y + 96), foot, font=ImageFont.truetype(IN, 25),
                   fill=MUTED, anchor="ma")
    else:
        img, subj = keyed(os.path.join(ROOT, 'site/images', photo),
                          720 if mode == 'hero' else 640, CROPS[crop])
        x, yp = (W - img.width) // 2, H - img.height - 64
        sh = Image.new('L', (W, H), 0)
        sh.paste(subj, (x + 8, yp + 14))
        sh = sh.filter(ImageFilter.GaussianBlur(24)).point(lambda v: int(v * 0.22))
        c.paste(Image.new('RGB', (W, H), (203, 192, 174)), (0, 0), sh)
        c.paste(img, (x, yp))
        if y + 40 > yp:
            print(f'  ! {name}: headline runs into the photo, shorten it or drop the size')

    path = os.path.join(OUT, name + '.jpg')
    c.save(path, quality=92, optimize=True, progressive=True)
    print(f'  {name}.jpg  {os.path.getsize(path)//1024} KB  mode={mode}')
    return c


# The week. Headlines are short pull lines; the prayer itself lives in the caption.
WEEK = [
    dict(name='01-thu-reopening',  eyebrow='October',        mode='hero',
         lines=['One decade,', 'in a parked car,', 'still counts.']),
    dict(name='02-fri-prayer',     eyebrow='A short prayer', mode='detail', crop='crucifix',
         lines=['Jesus, mercy.', 'Father, hold us.']),
    dict(name='03-sat-our-lady',   eyebrow='Saturday',       mode='type', size=80,
         lines=['Say our names', 'to your Son.'], foot='Saturday has belonged to Our Lady a long time'),
    dict(name='04-sun-sunday',     eyebrow='Sunday',         mode='type', size=72,
         lines=['Bless this house,', 'and everyone', 'who comes in.'], foot='Mass, and then rest'),
    dict(name='05-mon-joyful',     eyebrow='Monday',         mode='detail', crop='beads',
         lines=['The Joyful', 'Mysteries.']),
    dict(name='06-tue-engagement', eyebrow='First names only', mode='type', size=72,
         lines=['Who are you', 'praying for', 'this week?'], foot='Three words is plenty'),
    dict(name='07-wed-cord-rosary', eyebrow='Hand-blessed',  mode='hero',
         lines=['Someone missing', 'from this table.']),
]

if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    print(f'Building {len(WEEK)} images at {W}x{H} into social/images/')
    for spec in WEEK:
        build(**spec)
    print('Done. All real photography, no generated imagery.')
