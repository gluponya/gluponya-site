"""
Link-preview pictures (Open Graph, 1200x630) and the English app screens for
the translated landings, in the look of the store screenshots: the cloth,
headline type and phone come from the app repo's tools/store-screenshots/compose.py.

    python -I freshka/_i18n/og.py <app repo>

Writes freshka/og.jpg, freshka/<lang>/og.jpg and freshka/home/img/en/*.webp.
Nothing raster is enlarged (compose's rule zero).
"""

import importlib.util
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from strings import LANGS, OG_HEADLINE  # noqa: E402

APP = Path(sys.argv[1])
FRESHKA = HERE.parent
spec = importlib.util.spec_from_file_location("compose", APP / "tools/store-screenshots/compose.py")
c = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c)

W, H = 1200, 630
SHOTS = APP / "tools/store-screenshots"
LEFT = 72          # the text column's left edge
MARK = 60          # the icon's side in the wordmark
MARK_GAP = 40      # from the wordmark to the headline
PITCH = 1.14


def small(im, scale, what):
    if scale > 1.0:
        raise SystemExit(f"{what}: would be enlarged x{scale:.2f}")
    return im.resize((round(im.width * scale), round(im.height * scale)), Image.LANCZOS)


def text_column(canvas, ground, wordmark, lines, size, width):
    """The wordmark and the headline as one block, centred by height. `lines` carry *accents*."""
    _, ink, accent = c.GROUNDS[ground]
    draw = ImageDraw.Draw(canvas)
    font = ImageFont.truetype(str(c.HEADING), size)
    while max(draw.textlength(line.replace("*", ""), font=font) for line in lines) > width:
        size -= 1
        font = ImageFont.truetype(str(c.HEADING), size)
    pitch = size * PITCH
    cap = 0.70 * size
    block = MARK + MARK_GAP + cap + pitch * (len(lines) - 1)
    top = round((H - block) / 2)

    icon = c.rounded(small(Image.open(APP / "assets/icon.png").convert("RGB"), MARK / 1024, "icon"), round(MARK * 0.23))
    canvas.paste(icon, (LEFT, top), icon)
    name = ImageFont.truetype(str(c.HEADING), 40)
    draw.text((LEFT + MARK + 16, top + MARK / 2), wordmark, font=name, fill=ink, anchor="lm")

    baseline = top + MARK + MARK_GAP + cap
    for line in lines:
        x = LEFT
        for i, part in enumerate(line.split("*")):
            draw.text((x, baseline), part, font=font, fill=accent if i % 2 else ink, anchor="ls")
            x += draw.textlength(part, font=font)
        baseline += pitch
    return size


def phone(canvas, shot, x0, y0, width):
    """The screen as a phone whose bottom runs off the picture."""
    shot = c.paper_over_bars(Image.open(shot).convert("RGB"))
    piece = small(shot, width / shot.width, "screen")
    radius = round(width * c.PHONE_RADIUS)
    box = (x0, y0, x0 + width, y0 + piece.height)
    c.drop_shadow(canvas, box, radius, 26, 85, 18)
    framed = c.rounded(piece, radius)
    canvas.paste(framed, (x0, y0), framed)
    ImageDraw.Draw(canvas).rounded_rectangle((x0, y0, x0 + width - 1, y0 + piece.height - 1), radius, outline=c.LINE, width=3)


def preview(lang):
    app = "uk" if lang == "uk" else "en"
    canvas = c.cloth((W, H), c.GROUNDS["mint"][0], 2)
    size = text_column(canvas, "mint", "Фрешка" if lang == "uk" else "Freshka", OG_HEADLINE[lang], 84, 570)
    phone(canvas, SHOTS / "raw-hires" / app / "1.png", 737, 40, 350)  # the main screen: the kitchen with the cats, the first row of food below
    out = (FRESHKA if lang == "uk" else FRESHKA / lang) / "og.jpg"
    out.parent.mkdir(exist_ok=True)
    canvas.convert("RGB").save(out, quality=88)
    print(lang, "headline", size, "px,", out.stat().st_size // 1024, "KB")


def screens():
    """The landing's four app pictures from the English app: screens 1, 2, 4 whole and the room cut from 1."""
    out = FRESHKA / "home/img/en"
    out.mkdir(parents=True, exist_ok=True)
    for name, n in (("shot-fridge", 1), ("shot-photo", 2), ("shot-add", 4)):
        im = Image.open(SHOTS / "raw-hires/en" / f"{n}.png").convert("RGB")
        small(im, 540 / im.width, name).save(out / f"{name}.webp", quality=84, method=6)
    room = Image.open(SHOTS / "raw/en/1.png").convert("RGB")
    room.crop((0, 288, 1080, 288 + 980)).save(out / "scene.webp", quality=88, method=6)
    for f in sorted(out.iterdir()):
        print(f.name, Image.open(f).size, f.stat().st_size // 1024, "KB")


if "--screens" in sys.argv or len(sys.argv) == 2:
    screens()
for lang in ("uk",) + LANGS:
    preview(lang)
