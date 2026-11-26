"""Draw the promo photo for the post-x-promote-make-your-own-bounty-01 entry.

Original composition drawn with Pillow on a light make.fun canvas
(#FAF8FA). The ghost is make.fun's official mark (press kit
mark-1024.png, for light grounds), pasted unmodified: never redrawn,
recoloured, stretched, rotated or cropped. All other text and shapes
are drawn here, in the press kit palette (ink #191419, magenta
#BC0C7C, secondary #5A5359).

Output: promo.png, 1200 x 675 (X landscape photo).
"""
import math
import random

from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 675
CANVAS = (250, 248, 250)
INK = (25, 20, 25)
MAGENTA = (188, 12, 124)
PINK = (255, 136, 196)
SECONDARY = (90, 83, 89)
HAIRLINE = (226, 222, 225)

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def main():
    img = Image.new("RGB", (W, H), CANVAS)
    d = ImageDraw.Draw(img, "RGBA")

    # Faint dotted grid, like a bounty board.
    for x in range(40, W, 46):
        for y in range(40, H - 110, 46):
            d.ellipse([x, y, x + 3, y + 3], fill=(233, 229, 232))

    # Magenta corner glow, top left.
    for r in range(260, 0, -4):
        alpha = int(10 * (1 - r / 260))
        d.ellipse([-r, -r, r, r], fill=(196, 28, 131, alpha))

    # Scattered bounty coins (plain magenta discs with a $ cut).
    random.seed(20261126)
    coin_font = font(BOLD, 34)
    for _ in range(9):
        cx = random.randint(60, 1120)
        cy = random.randint(30, 540)
        if 640 < cx < 1180 and 60 < cy < 560:
            continue  # keep the ghost's clear space free
        if cx < 700 and cy < 480:
            continue  # keep the headline readable
        r = random.randint(16, 26)
        d.ellipse([cx - r, cy - r, cx + r, cy + r],
                  fill=(196, 28, 131, 255),
                  outline=(255, 255, 255, 255), width=2)
        d.text((cx, cy), "$", font=coin_font, fill=(255, 255, 255),
               anchor="mm")

    # Headline, left side.
    x0 = 64
    d.text((x0, 108), "GOT A TASK?", font=font(BOLD, 84), fill=INK)
    d.text((x0, 196), "PUT A", font=font(BOLD, 84), fill=INK)
    d.text((x0, 284), "BOUNTY ON IT.", font=font(BOLD, 84), fill=MAGENTA)

    # Supporting line.
    d.text((x0, 396),
           "Describe it. Set the reward.",
           font=font(BOLD, 30), fill=INK)
    d.text((x0, 436),
           "Agents compete. Best work gets paid.",
           font=font(REG, 30), fill=SECONDARY)

    # Official ghost mark, unmodified, on the right with clear space.
    ghost = Image.open(
        "/home/hatch/workspace/make-fun/entries/gta6-meme-x-01/"
        "press-kit/make-fun-press-kit/mark-1024.png").convert("RGBA")
    ghost = ghost.resize((400, 400), Image.LANCZOS)
    img.paste(ghost, (760, 92), ghost)

    # Bottom magenta band with the call to action.
    d.rectangle([0, H - 88, W, H], fill=MAGENTA)
    d.text((64, H - 66), "make your own bounty  →  make.fun/sponsor/new",
           font=font(BOLD, 34), fill=(255, 255, 255))

    img.save("/home/hatch/workspace/make-fun/entries/"
             "post-x-promote-make-your-own-bounty-01/assets/promo.png")
    print("saved promo.png", img.size)


if __name__ == "__main__":
    main()
