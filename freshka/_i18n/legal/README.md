# Translations of the privacy policy and the terms

`source.json` holds the English phrases of `freshka/privacy/` and `freshka/terms/`
exactly as they stand on the pages: `{"privacy": [...], "terms": [...]}`.
Refresh it with `python -I freshka/_i18n/legal.py > freshka/_i18n/legal/source.json`.

Each language has one file, `<lang>.json` (de, es, pt, vi, tr, fr, it, pl, nl): a single flat JSON
object `{"English phrase": "translation"}` with every phrase from both lists of
`source.json` as a key, character for character. `build.py` stops if one is missing.
When the English text of a page changes, the changed phrases need new entries here.

## Rules for the translator

1. This is legal text. Translate the meaning exactly: add nothing, drop nothing,
   soften nothing. Keep every condition, number, period, company and country.
2. Tone: plain and friendly, addressing the reader informally (de du, es tú,
   pt você as in Brazil, vi bạn, tr sen), the same as the app's site. No
   gendered forms for the reader where the language lets you avoid them.
3. Names stay as they are: Freshka, Gluponya, Supabase, OpenRouter, Qwen, Alibaba
   Cloud, Expo, Apple, Google, Gmail, Spacemail, Open Food Facts, DeepL, RevenueCat,
   Telegram, Sentry, Cloudflare Web Analytics, App Store, Google Play, iPhone,
   Android, iOS. A phrase that is only such names is translated to itself.
4. The app speaks Ukrainian and English only. Names of its screens, buttons and
   switches stay in English, in the same quotes as the source: Settings, Me,
   Delete account, “Send photos to AI”, “Send crash reports”, “Contact us”,
   Catalogue. The three phrases that are exactly `Settings`, `Me` and
   `Delete account` are translated to themselves.
5. Drop the Ukrainian in brackets: `(«Налаштування» → «Я» → …)`, `(«Каталог»)`,
   `(«Написати нам»)`, and `Freshka (Фрешка)` becomes `Freshka`. A translation
   has no Cyrillic letters at all.
6. HTML inside a phrase stays intact: the same `<a href="…">` tags with the same
   attributes, wrapped around the matching words.
7. Dates in the language's own form (14 November 2026, 5 November 2026).
8. Typographic quotes of the language, never the ASCII `'` as an apostrophe
   outside HTML attributes (use ’).
9. Short labels (chips, table cells, buttons) stay short: about as long as the
   English, lower case where the English is lower case, no full stop where the
   English has none.
10. The same English phrase always gets the same translation; terms used in both
    pages (subscription, shared fridge, catalogue, consent, crash reports) are
    translated the same way throughout.
