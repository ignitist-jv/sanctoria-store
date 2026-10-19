# Builds the ClickBank order form header for Your Prayer Song (2000 x 669).
# Words: prayer-song/copy/06-order-form-header.md. Picture: bg.png (cropped from raw-dark.png).
from PIL import Image, ImageDraw, ImageFont, ImageFilter
W, H, S = 2000, 669, 3
GOLD, GOLD2, CREAM, SOFT = (201, 162, 88), (232, 200, 130), (247, 240, 226), (205, 190, 165)
F = '/System/Library/Fonts/Supplemental/Baskerville.ttc'
ROWS = [('note', 'Sung by name', 'One original song, built on Scripture.'),
        ('mail', 'Within 24 hours', 'By email, with a private song page.'),
        ('shield', '30 day full refund', 'One-time payment, no subscription.')]

bg = Image.open('bg.png').convert('RGB')
ground = bg.crop((40, 40, 700, 629)).resize((1, 1), Image.BOX).getpixel((0, 0))
# flatten the left and let the picture fade in
mask = Image.new('L', (W, 1))
for x in range(W):
    t = (x / W - 0.50) / 0.13
    mask.putpixel((x, 0), int(255 * (1 - min(1, max(0, t)) ** 1.6)))
bg.paste(Image.new('RGB', (W, H), ground), (0, 0), mask.resize((W, H)))

big = Image.new('RGBA', (W * S, H * S), (0, 0, 0, 0))
d = ImageDraw.Draw(big)
def s(v): return int(round(v * S))

# logo
logo = Image.open('../../../site/prayer-song/img/logo-light.png').convert('RGBA')
lw = 400; lh = round(logo.height * lw / logo.width)
LOGO_POS = (62, (H - lh) // 2)

# vertical rule with soft ends
RX = 520
for y in range(s(70), s(H - 70)):
    t = (y / S - 70) / (H - 140); a = int(255 * min(1, 6 * t, 6 * (1 - t)))
    d.line([(s(RX), y), (s(RX) + S * 2 - 1, y)], fill=GOLD + (a,))

IX, R, TX = 618, 50, 700            # icon centre x, radius, text x
fb = ImageFont.truetype(F, s(50), index=1)
fs = ImageFont.truetype(F, s(29), index=0)
ys = [128, 334, 540]
dark = tuple(max(0, c - 4) for c in ground)
for (icon, bigt, small), cy in zip(ROWS, ys):
    d.ellipse([s(IX - R), s(cy - R), s(IX + R), s(cy + R)], fill=GOLD)
    d.ellipse([s(IX - R + 5), s(cy - R + 5), s(IX + R - 5), s(cy + R - 5)], outline=GOLD2, width=s(1.5))
    c = dark; x0, y0 = IX, cy
    if icon == 'note':
        d.ellipse([s(x0 - 20), s(y0 + 8), s(x0 - 2), s(y0 + 22)], fill=c)
        d.rectangle([s(x0 - 7), s(y0 - 24), s(x0 - 2), s(y0 + 15)], fill=c)
        d.polygon([(s(x0 - 7), s(y0 - 24)), (s(x0 + 18), s(y0 - 14)), (s(x0 + 18), s(y0 - 2)), (s(x0 - 7), s(y0 - 12))], fill=c)
    elif icon == 'mail':
        d.rounded_rectangle([s(x0 - 25), s(y0 - 17), s(x0 + 25), s(y0 + 17)], radius=s(3), outline=c, width=s(4))
        d.line([(s(x0 - 23), s(y0 - 14)), (s(x0), s(y0 + 4)), (s(x0 + 23), s(y0 - 14))], fill=c, width=s(4), joint='curve')
    else:
        d.polygon([(s(x0), s(y0 - 27)), (s(x0 + 22), s(y0 - 18)), (s(x0 + 22), s(y0 + 2)), (s(x0 + 13), s(y0 + 17)), (s(x0), s(y0 + 27)),
                   (s(x0 - 13), s(y0 + 17)), (s(x0 - 22), s(y0 + 2)), (s(x0 - 22), s(y0 - 18))], fill=c)
        d.line([(s(x0 - 10), s(y0)), (s(x0 - 2), s(y0 + 9)), (s(x0 + 11), s(y0 - 9))], fill=GOLD2, width=s(4.5), joint='curve')
    d.text((s(TX), s(cy - 8)), bigt, font=fb, fill=CREAM, anchor='ls')
    d.text((s(TX), s(cy + 34)), small, font=fs, fill=SOFT, anchor='ls')
for y in ((ys[0] + ys[1]) // 2, (ys[1] + ys[2]) // 2):   # thin dividers between rows
    for x in range(s(IX - R), s(1140)):
        t = (x / S - (IX - R)) / (1140 - IX + R); a = int(110 * min(1, 5 * (1 - t)))
        d.line([(x, s(y)), (x, s(y) + S - 1)], fill=GOLD + (a,))

out = bg.convert('RGBA')
out.alpha_composite(big.resize((W, H), Image.LANCZOS))
out.alpha_composite(logo.resize((lw, lh), Image.LANCZOS), LOGO_POS)
out.convert('RGB').save('your-prayer-song-order-header-2000x669.jpg', quality=93, subsampling=0)
out.convert('RGB').save('your-prayer-song-order-header-2000x669.png')
out.convert('RGB').resize((1400, 468), Image.LANCZOS).save('preview.jpg', quality=88)
