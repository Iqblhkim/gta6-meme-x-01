#!/usr/bin/env python3
"""gta6-meme-x-01 v3 — Rockstar Games invoice (formal receipt).

Drawn with PIL + DejaVu fonts so every letter is exact (no AI-image typos).
Layout: 1200x1200, formal white-paper invoice, monospace itemised table,
red PAID stamp, official make.fun ghost mark as the payment seal.
Differentiates from v2 (WANTED poster) and from the current #1 (Leonida
Mart customer display) / #2 (Steam purchase invoice): this is a formal
INVOICE from Rockstar Games billing one patient gamer for the wait.
"""
import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter

REPO = "/home/hatch/workspace/makefun/gta6-meme-x-01-repo"
MARK = f"{REPO}/tools/makefun-mark.png"
OUT = f"{REPO}/meme-v3-invoice.png"

W = H = 1200
PAPER = (250, 249, 245)
INK = (28, 28, 32)
INK_SOFT = (88, 84, 80)
RED = (200, 16, 46)
MAGENTA = (231, 0, 149)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
MONO_B = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def fit(draw, text, path, size, max_w):
    """Largest font size <= `size` that fits `max_w`."""
    while size > 10:
        f = font(path, size)
        if draw.textlength(text, font=f) <= max_w:
            return f
        size -= 2
    return font(path, 10)


def right(draw, x, y, text, f, fill=INK):
    w = draw.textlength(text, font=f)
    draw.text((x - w, y), text, font=f, fill=fill)
    return x - w


img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img, "RGBA")

# ---- subtle paper grain -------------------------------------------------------
random.seed(4811)
for _ in range(1500):
    x, y = random.randint(0, W - 1), random.randint(0, H - 1)
    a = random.randint(5, 14)
    d.point((x, y), fill=(120, 110, 90, a))

# ---- magenta brand bar + double border ----------------------------------------
d.rectangle([28, 28, W - 29, 40], fill=MAGENTA)
d.rectangle([28, 28, W - 29, H - 29], outline=INK, width=4)
d.rectangle([44, 44, W - 45, H - 45], outline=INK, width=1)

# ---- header -------------------------------------------------------------------
d.text((64, 62), "ROCKSTAR GAMES", font=font(SERIF_B, 46), fill=INK)
d.text((64, 116), "VICE CITY, LEONIDA", font=font(SANS_B, 24), fill=INK_SOFT)
right(d, 1136, 56, "INVOICE", font(SERIF_B, 74), INK)
right(d, 1136, 136, "No. 4811", font(SANS_B, 30), RED)
d.line([64, 178, 1136, 178], fill=INK, width=3)

# ---- bill-to / dates ------------------------------------------------------------
d.text((64, 200), "BILL TO", font=font(SANS_B, 22), fill=INK_SOFT)
d.text((64, 230), "ONE PATIENT GAMER", font=font(SANS_B, 34), fill=INK)
d.text((64, 272), "JASON & LUCIA FAN CLUB", font=font(SANS, 26), fill=INK)
d.text((64, 304), "VICE CITY, LEONIDA", font=font(SANS, 26), fill=INK)
right(d, 1136, 200, "INVOICE DATE — 20 NOV 2026", font(SANS, 26), INK)
right(d, 1136, 234, "DUE DATE — 19 NOV 2026", font(SANS, 26), INK)
right(d, 1136, 268, "TERMS — 13 YEARS NET", font(SANS_B, 26), INK)
right(d, 1136, 302, "CUSTOMER SINCE 17 SEP 2013", font(SANS, 24), INK_SOFT)
d.line([64, 338, 1136, 338], fill=INK, width=2)

# ---- itemised table ---------------------------------------------------------------
d.text((64, 354), "DESCRIPTION", font=font(SANS_B, 26), fill=INK)
right(d, 1136, 354, "AMOUNT", font(SANS_B, 26), INK)
d.line([64, 390, 1136, 390], fill=INK, width=2)

ROWS = [
    ("GTA VI PRE-ORDER — 17 SEP 2013", "$79.99"),
    ("WAITING — 4,811 DAYS", "$0.00"),
    ("DELAY No. 1 — FALL 2025 → MAY 2026", "WAIVED"),
    ("DELAY No. 2 — MAY → NOV 2026", "WAIVED"),
    ("PATIENCE — EXHAUSTED", "$0.00"),
    ("HYPE — OVERDUE", "$0.00"),
    ("TRAILER REWATCHES — 1,337", "$0.00"),
    ("DOWNLOAD — 214 GB", "$0.00"),
]
f_desc = font(MONO, 28)
f_amt = font(MONO_B, 28)
y = 406
for desc, amt in ROWS:
    d.text((64, y), desc, font=f_desc, fill=INK)
    aw = d.textlength(amt, font=f_amt)
    d.text((1136 - aw, y), amt, font=f_amt, fill=INK)
    # dotted leader between description and amount
    x0 = 64 + d.textlength(desc, font=f_desc) + 14
    x1 = 1136 - aw - 14
    cy = y + 20
    x = x0
    while x < x1:
        d.ellipse([x, cy - 2, x + 4, cy + 2], fill=INK_SOFT)
        x += 12
    y += 48

# ---- total ------------------------------------------------------------------------
d.line([64, y + 6, 1136, y + 6], fill=INK, width=3)
d.line([64, y + 12, 1136, y + 12], fill=INK, width=1)
d.text((64, y + 28), "TOTAL DUE", font=font(SERIF_B, 44), fill=INK)
right(d, 1136, y + 20, "$79.99", font(SERIF_B, 56), MAGENTA)
total_bottom = y + 28 + 56

# ---- note (left, clear of the stamp) ----------------------------------------------
d.text((64, total_bottom + 34), "JASON & LUCIA ARE", font=font(SANS_B, 24), fill=INK_SOFT)
d.text((64, total_bottom + 64), "STILL WAITING.", font=font(SANS_B, 24), fill=INK_SOFT)

# ---- red PAID stamp (own layer, rotated) -------------------------------------------
sw, sh = 540, 112
stamp = Image.new("RGBA", (sw, sh), (0, 0, 0, 0))
sd = ImageDraw.Draw(stamp)
sd.rectangle([4, 4, sw - 5, sh - 5], outline=RED + (235,), width=5)
sd.rectangle([16, 16, sw - 17, sh - 17], outline=RED + (235,), width=2)
f1 = fit(sd, "PAID IN FULL", SANS_B, 52, sw - 48)
w1 = sd.textlength("PAID IN FULL", font=f1)
sd.text(((sw - w1) / 2, 10), "PAID IN FULL", font=f1, fill=RED + (235,))
f2 = fit(sd, "BY MY AI AGENT ON MAKE.FUN", SANS_B, 25, sw - 48)
w2 = sd.textlength("BY MY AI AGENT ON MAKE.FUN", font=f2)
sd.text(((sw - w2) / 2, 70), "BY MY AI AGENT ON MAKE.FUN",
        font=f2, fill=RED + (235,))
stamp = stamp.rotate(-9, expand=True, resample=Image.BICUBIC)
# placed high enough that the rotated stamp stays clear of the bottom band
img.paste(stamp, (1136 - stamp.width - 40, total_bottom - 48), stamp)
d = ImageDraw.Draw(img, "RGBA")

# ---- bottom band: ghost payment seal + barcode --------------------------------------
band_y = 1052
d.line([64, band_y - 14, 1136, band_y - 14], fill=INK, width=2)
mark = Image.open(MARK).convert("RGBA").resize((96, 96), Image.LANCZOS)
img.paste(mark, (64, band_y + 6), mark)
d = ImageDraw.Draw(img, "RGBA")
d.text((188, band_y + 6), "PAYMENT PROCESSED BY", font=font(SANS_B, 20), fill=INK_SOFT)
d.text((188, band_y + 32), "make.fun", font=font(SANS_B, 36), fill=MAGENTA)
d.text((188, band_y + 74), "WHERE AI AGENTS EARN REAL MONEY", font=font(SANS_B, 18), fill=INK_SOFT)

# barcode for "4811 2026" (deterministic)
random.seed(4811)
bx, by, bw, bh = 880, band_y + 2, 256, 62
x = bx
while x < bx + bw:
    wbar = random.choice([2, 3, 3, 4, 5])
    if random.random() < 0.55:
        d.rectangle([x, by, x + wbar - 1, by + bh], fill=INK)
    x += wbar + random.choice([2, 3, 4])
btxt = "4 8 1 1  2 0 2 6"
d.text((bx + (bw - d.textlength(btxt, font=font(MONO, 20))) / 2, by + bh + 6),
       btxt, font=font(MONO, 20), fill=INK)

img.save(OUT, "PNG", optimize=True)
print("saved", OUT)
