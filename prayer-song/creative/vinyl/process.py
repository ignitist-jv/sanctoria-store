"""Cut a generated record out as a true centred circle so it can be rotated in CSS.
Finds the disc from the alpha channel (or from non-white pixels), centres on it, masks to a circle, writes webp."""
import sys
from PIL import Image, ImageDraw, ImageChops
import numpy as np

def process(src, dst=None, size=640):
    im = Image.open(src).convert("RGBA")
    a = np.array(im)
    alpha = a[..., 3]
    if alpha.min() > 250:                       # no transparency: treat near white as background
        mask = (a[..., :3].min(axis=2) < 235)
    else:
        mask = alpha > 128
    ys, xs = np.nonzero(mask)
    x0, x1, y0, y1 = xs.min(), xs.max(), ys.min(), ys.max()
    w, h = x1 - x0 + 1, y1 - y0 + 1
    cx, cy, r = (x0 + x1) / 2, (y0 + y1) / 2, max(w, h) / 2
    info = dict(size=im.size, has_alpha=bool(alpha.min() < 250), bbox=(int(x0), int(y0), int(x1), int(y1)),
                width=int(w), height=int(h), roundness=round(min(w, h) / max(w, h), 4),
                centre_offset=(round(cx - im.width / 2, 1), round(cy - im.height / 2, 1)))
    if dst:
        # crop to the disc's own bounding box, then resize that to a square: this squashes the
        # slight ellipse the model draws into a true circle, so it does not wobble when it turns
        crop = im.crop((int(x0) + 2, int(y0) + 2, int(x1) - 1, int(y1) - 1)).resize((size, size), Image.LANCZOS)
        m = Image.new("L", (size * 4, size * 4), 0)
        ImageDraw.Draw(m).ellipse((2, 2, size * 4 - 3, size * 4 - 3), fill=255)
        m = m.resize((size, size), Image.LANCZOS)
        crop.putalpha(ImageChops.multiply(crop.getchannel("A"), m))
        crop.save(dst, "WEBP", quality=86, method=6)
    return info

if __name__ == "__main__":
    for s in sys.argv[1:]:
        print(s, process(s, s.replace(".png", ".webp")))
