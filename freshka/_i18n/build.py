"""
Builds the landing's translations from the Ukrainian page.

    python -I freshka/_i18n/build.py

freshka/index.html is the only page edited by hand. This writes
freshka/<lang>/index.html and freshka/<lang>/support/index.html (from
freshka/support/index.html) for every language in strings.py and refreshes the
two generated blocks inside the Ukrainian page itself (hreflang links in the
head, the language row in the footer), which sit between marker comments.
The row's CSS (footer .langs) is in the Ukrainian page like any other style.

It stops if a phrase from strings.py is not on the page, or if a translated
page still has Cyrillic in it.
"""

import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from strings import LANGS, META, T  # noqa: E402
from support_strings import S  # noqa: E402

FRESHKA = HERE.parent
SOURCE = FRESHKA / "index.html"
BASE = "https://gluponya.tv/freshka/"
ALL = ("uk",) + LANGS

HEAD_MARK = ("<!--langs:head-->", "<!--/langs:head-->")
FOOT_MARK = ("<!--langs:foot-->", "<!--/langs:foot-->")
HEAD_ANCHOR = '<link rel="canonical" href="https://gluponya.tv/freshka/">\n'
FOOT_ANCHOR = '  <div class="base">'


def url(lang):
    return BASE if lang == "uk" else f"{BASE}{lang}/"


def between(text, mark, block, anchor, before):
    """Put `block` between the markers, adding them next to `anchor` on the first run."""
    whole = f"{mark[0]}\n{block}{mark[1]}\n"
    if mark[0] in text:
        return re.sub(re.escape(mark[0]) + r".*?" + re.escape(mark[1]) + r"\n", lambda _: whole, text, flags=re.S)
    if anchor not in text:
        raise SystemExit(f"anchor not found: {anchor!r}")
    return text.replace(anchor, whole + anchor if before else anchor + whole, 1)


def head_block():
    rows = [f'<link rel="alternate" hreflang="{lang}" href="{url(lang)}">\n' for lang in ALL]
    rows.append(f'<link rel="alternate" hreflang="x-default" href="{url("en")}">\n')
    return "".join(rows)


def foot_block(current):
    links = []
    for lang in ALL:
        here = ' aria-current="page"' if lang == current else ""
        links.append(f'<a href="/freshka/{"" if lang == "uk" else lang + "/"}" lang="{lang}" hreflang="{lang}"{here}>{META[lang][0]}</a>')
    return '  <nav class="langs" aria-label="Language">' + "".join(links) + "</nav>\n"


def swap(text, old, new, count=None):
    if old not in text:
        raise SystemExit(f"not on the page: {old!r}")
    return text.replace(old, new) if count is None else text.replace(old, new, count)


def translate(page, lang):
    i = LANGS.index(lang)
    _, og_locale, tp_locale = META[lang]
    page = between(page, FOOT_MARK, foot_block(lang), FOOT_ANCHOR, True)
    page = swap(page, '<html lang="uk">', f'<html lang="{lang}">')
    page = swap(page, 'content="https://gluponya.tv/freshka/og.jpg"', f'content="{url(lang)}og.jpg"')
    page = swap(page, 'content="uk_UA"', f'content="{og_locale}"')
    page = swap(page, '<link rel="canonical" href="https://gluponya.tv/freshka/">', f'<link rel="canonical" href="{url(lang)}">')
    page = swap(page, '<meta property="og:url" content="https://gluponya.tv/freshka/">', f'<meta property="og:url" content="{url(lang)}">')
    page = swap(page, '"url": "https://gluponya.tv/freshka/",', f'"url": "{url(lang)}",')
    page = swap(page, 'data-locale="uk-UA"', f'data-locale="{tp_locale}"')
    for name in ("shot-fridge", "shot-photo", "shot-add", "scene"):
        page = swap(page, f"/freshka/home/img/{name}.webp", f"/freshka/home/img/en/{name}.webp")
    # the legal pages and support carry an English part behind #en
    for part in ("privacy", "terms"):
        page = swap(page, f'href="https://gluponya.tv/freshka/{part}/"', f'href="https://gluponya.tv/freshka/{part}/#en"')
    page = swap(page, 'href="https://gluponya.tv/freshka/support/"', f'href="{url(lang)}support/"')
    # Latin lines run longer than the Ukrainian ones and slide under the carrot sticker on a phone
    page = swap(page, "</style>", "@media (max-width:560px){.hero-text p{padding-right:34px}}\n</style>", 1)
    for uk in sorted(T, key=len, reverse=True):
        page = swap(page, uk, T[uk][i])
    cyrillic_left(page, lang)
    return page


def cyrillic_left(page, lang):
    own = page.replace(f">{META['uk'][0]}<", "><")  # the language row names Ukrainian in Ukrainian
    left = sorted(set(re.findall(r"[^<>\n]*[\u0400-\u04FF][^<>\n]*", own)))
    if left:
        raise SystemExit(f"{lang}: Cyrillic left:\n  " + "\n  ".join(s.strip()[:120] for s in left))


def support(page, lang):
    """freshka/support/index.html in `lang`, without its own English section."""
    i = LANGS.index(lang)
    page = re.sub(r'  <section class="en".*?</section>\n\n', "", page, count=1, flags=re.S)
    page = swap(page, '<html lang="uk">', f'<html lang="{lang}">')
    page = swap(page, 'content="https://gluponya.tv/freshka/og.jpg"', f'content="{url(lang)}og.jpg"')
    page = swap(page, 'content="uk_UA"', f'content="{META[lang][1]}"')
    page = swap(page, "https://gluponya.tv/freshka/support/", f"{url(lang)}support/")
    page = swap(page, 'href="/freshka/"', f'href="/freshka/{lang}/"')
    for part in ("privacy", "terms"):
        page = swap(page, f'href="/freshka/{part}/"', f'href="/freshka/{part}/#en"')
    for uk in S:
        if uk not in page:
            raise SystemExit(f"not on the support page: {uk!r}")
    words = {**T, **S}
    for uk in sorted(words, key=len, reverse=True):
        page = page.replace(uk, words[uk][i])
    cyrillic_left(page, lang)
    return page


def main():
    for uk, row in T.items():
        if len(row) != len(LANGS):
            raise SystemExit(f"{uk!r}: {len(row)} translations, need {len(LANGS)}")
        for text in row:
            if "'" in text or '"' in text.replace('<em>', '').replace('</em>', ''):
                raise SystemExit(f"ASCII quote in a translation: {text!r}")

    page = SOURCE.read_text(encoding="utf-8")
    page = between(page, HEAD_MARK, head_block(), HEAD_ANCHOR, False)
    bare = page
    page = between(page, FOOT_MARK, foot_block("uk"), FOOT_ANCHOR, True)
    SOURCE.write_text(page, encoding="utf-8", newline="\n")

    for lang in LANGS:
        out = FRESHKA / lang / "index.html"
        out.parent.mkdir(exist_ok=True)
        out.write_text(translate(bare, lang), encoding="utf-8", newline="\n")
        print(lang, out.stat().st_size // 1024, "KB")

    for uk, row in S.items():
        if len(row) != len(LANGS):
            raise SystemExit(f"{uk!r}: {len(row)} translations, need {len(LANGS)}")
    help_page = (FRESHKA / "support/index.html").read_text(encoding="utf-8")
    for lang in LANGS:
        out = FRESHKA / lang / "support/index.html"
        out.parent.mkdir(exist_ok=True)
        out.write_text(support(help_page, lang), encoding="utf-8", newline="\n")


main()
