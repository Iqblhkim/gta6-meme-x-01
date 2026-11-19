#!/usr/bin/env python3
"""Add meme text to the GTA 6 + make.fun ghost base image."""
from PIL import Image, ImageDraw, ImageFont

SRC = "base.webp"
OUT_JPG = "../meme.jpg"
OUT_PNG = "meme.png"

TOP = "WAITED 12 YEARS FOR GTA 6"
BOTTOM = "MY AI AGENT MADE $500 ON MAKE.FUN"

im = Image.open(SRC).convert("RGB")
W, H = im.size
draw = ImageDraw.Draw(im)

def load_font(size):
    for path in (
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/dejavu/DejaVuSans-Bold.ttf",
    ):
        try:
            return ImageFont.truetype(path, size)
        except Exception:
            continue
    return ImageFont.load_default()

def fit_font(text, max_w, start=140):
    size = start
    while size > 20:
        f = load_font(size)
        if draw.textlength(text, font=f) <= max_w:
            return f
        size -= 4
    return load_font(20)

def draw_meme_text(text, y_center, max_w):
    font = fit_font(text, max_w)
    tw = draw.textlength(text, font=font)
    x = (W - tw) / 2
    # black outline (stroke)
    draw.text((x, y_center), text, font=font, fill="white",
              stroke_width=max(4, font.size // 14), stroke_fill="black")

MARGIN = 70
TOP_Y = 55
BOTTOM_Y = H - 200

draw_meme_text(TOP, TOP_Y, W - 2 * MARGIN)
draw_meme_text(BOTTOM, BOTTOM_Y, W - 2 * MARGIN)

im.save(OUT_JPG, "JPEG", quality=92)
im.save(OUT_PNG, "PNG")
print("saved", OUT_JPG, "and", OUT_PNG, im.size)
