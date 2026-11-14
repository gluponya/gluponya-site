"""
The privacy policy and the terms in the landing's languages.

freshka/privacy/index.html and freshka/terms/index.html carry Ukrainian and
English side by side. A translated page is the English half of that page with
every phrase replaced from freshka/_i18n/legal/<lang>.json, whose keys are the
English phrases exactly as they stand on the page (see legal/README.md).
English itself stays where it is, behind #en on the original page.

    python -I freshka/_i18n/legal.py     prints the phrases as JSON, for a translator

build.py calls pages() and stops if a phrase has no translation.
"""

import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
FRESHKA = HERE.parent
PAGES = ("privacy", "terms")
LANGS = ("de", "es", "pt", "vi", "tr")  # en is the page's own second language

# what the head and the labels say in Ukrainian only
HEAD = {
    "Які дані збирає Фрешка, навіщо, кому вони передаються і як їх видалити": "What data Freshka collects, why, who it is shared with and how to delete it",
    "Конфіденційність Фрешки": "Freshka privacy policy",
    "Умови використання застосунку Фрешка: підписка, дати й поради, розпізнавання фото, спільний каталог": "Terms of use of the Freshka app: subscription, dates and advice, photo recognition, shared catalogue",
    "Умови використання Фрешки": "Freshka terms of use",
    "Підписка, дати й поради, розпізнавання фото, спільний каталог": "Subscription, dates and advice, photo recognition, shared catalogue",
    "Коротко": "In short",
}
# shown above the full text of every translated page
NOTE = "This is a translation made for your convenience. If it differs from the Ukrainian original, the Ukrainian text applies."
NOTE_LINK = "Ukrainian and English original"

UK_PART = re.compile(r'[ \t]*<(\w+) class="[^"]*\buk"[^>]*>.*?</\1>\n?', re.S)
# an element holding nothing but text and plain links
PHRASE = re.compile(r"<(\w+)([^>]*)>((?:[^<]|<a [^>]*>[^<]*</a>)+)</\1>")
ATTR = re.compile(r'(content|aria-label)="([^"]*)"')


def english(page, name):
    """The page with its Ukrainian half and the language switch taken out."""
    page = UK_PART.sub("", page)
    page = re.sub(r'[ \t]*<div class="seg".*?</div>\n', "", page, count=1, flags=re.S)
    page = re.sub(r"<script>\(function\(\)\{if\(location\.hash.*?</script>\n", "", page, count=1)
    page = page.replace('<script src="/freshka/_lang.js"></script>\n', "")
    page = page.replace(' data-lang="uk"', "").replace(' lang="en"', "").replace("#en-", "#").replace('id="en-', 'id="')
    for uk, en in HEAD.items():
        page = page.replace(uk, en)
    head = '  <div class="full-head" id="full">'
    if head not in page:
        raise SystemExit(f"{name}: no full-text heading")
    note = f'  <p class="soft" style="margin-bottom:18px">{NOTE} <a href="/freshka/{name}/">{NOTE_LINK}</a></p>\n\n'
    end = page.index("</div>\n", page.index(head)) + len("</div>\n")
    return page[:end] + "\n" + note.rstrip("\n") + "\n" + page[end:]


def worded(text):
    return any(ch.isalpha() for ch in text)


def phrases(page):
    found = []
    for m in PHRASE.finditer(page):
        if m.group(1) not in ("script", "style") and worded(m.group(3)):
            found.append(m.group(3))
    for m in ATTR.finditer(page):
        if m.group(2) in HEAD.values():
            found.append(m.group(2))
    return found


def source():
    """{page: [phrases in page order, no repeats]} for the two pages."""
    out = {}
    for name in PAGES:
        page = english((FRESHKA / name / "index.html").read_text(encoding="utf-8"), name)
        out[name] = list(dict.fromkeys(phrases(page)))
    return out


def translate(page, name, lang, words, shared, meta):
    """`words`: English phrase -> translation. `shared`: Ukrainian phrase -> translation, from the landing."""
    base = f"https://gluponya.tv/freshka/{lang}/"
    page = english(page, name)
    missing = []

    def put(text):
        if text in words:
            return words[text]
        if text in shared:
            return shared[text]
        if "@" in text and " " not in text:
            return text
        missing.append(text)
        return text

    page = PHRASE.sub(lambda m: m.group(0) if m.group(1) in ("script", "style") or not worded(m.group(3)) else f"<{m.group(1)}{m.group(2)}>{put(m.group(3))}</{m.group(1)}>", page)
    page = ATTR.sub(lambda m: f'{m.group(1)}="{put(m.group(2))}"' if m.group(2) in HEAD.values() or m.group(2) in shared else m.group(0), page)
    if missing:
        raise SystemExit(f"{lang}/{name}: no translation for:\n  " + "\n  ".join(dict.fromkeys(missing)))
    page = page.replace('<html lang="uk">', f'<html lang="{lang}">')
    page = page.replace('content="https://gluponya.tv/freshka/og.jpg"', f'content="{base}og.jpg"')
    page = page.replace('content="uk_UA"', f'content="{meta[lang][1]}"')
    page = page.replace(f"https://gluponya.tv/freshka/{name}/", f"{base}{name}/")
    page = page.replace('href="/freshka/"', f'href="/freshka/{lang}/"')
    for part in ("privacy", "terms", "support"):
        if part != name:
            page = page.replace(f'href="/freshka/{part}/"', f'href="/freshka/{lang}/{part}/"')
    return page.replace(">Фрешка</a>", ">Freshka</a>")


def pages(lang, shared, meta):
    """{page name: html} for one language."""
    file = HERE / "legal" / f"{lang}.json"
    words = json.loads(file.read_text(encoding="utf-8"))
    out = {}
    for name in PAGES:
        page = (FRESHKA / name / "index.html").read_text(encoding="utf-8")
        out[name] = translate(page, name, lang, words, shared, meta)
    return out


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    print(json.dumps(source(), ensure_ascii=False, indent=1))
