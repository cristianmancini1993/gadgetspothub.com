#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Apply Google Ads audit fixes across live HTML (NETM-002, 4 Sep 2026)."""
from __future__ import annotations

import re
from collections import defaultdict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IT_HOOK = "https://hook.eu2.make.com/i7pmea9fmpnepx94e5z6dxfwvl1bnnlh"
EU_HOOK = "https://hook.eu2.make.com/7nudarijfrsvnhnwfnpqfh2t8vqt109i"
TODO_ENDPOINT = "https://TODO-network-endpoint.com/api/lead"

VOID_TAGS = {
    "area", "base", "br", "col", "embed", "hr", "img", "input", "link",
    "meta", "param", "source", "track", "wbr",
}

SKIP_DIR_NAMES = {".git", "node_modules", "assets"}
LEGAL_SLUGS = {
    "about-us", "contact-us", "privacy-policy", "terms-conditions",
    "cookie-policy", "shipping-policy", "refund-policy",
}

CLASS_REMOVE = [
    "rating-strip",
    "countdown-row",
    "stock-row",
    "live-row",
    "countdown-bar",
    "c4x-sale-badge",
    "c4x-old-price",
    "c4x-stock-bar",
    "c4x-stock-text",
    "c4x-order-stock-section",
    "hero-headline__rating",
    "price-discount__label",
    "price-anchor__old",
    "price-anchor__discount",
    "featured__discount-badge",
    "featured__rating",
    "reviews-summary",
    "cod-form__rating",
    "watching-now",
    "reviews-grid",
    "limited-offer__stock-bar",
]

CLASS_ATTR = re.compile(
    r"""<(?P<tag>[a-zA-Z][a-zA-Z0-9]*)\b(?P<attrs>[^>]*\bclass\s*=\s*(?P<q>['"])(?P<cls>.*?)(?P=q)[^>]*)>""",
    re.I | re.S,
)


def class_tokens(raw: str) -> set[str]:
    return {t for t in re.split(r"\s+", raw.strip()) if t}


def element_end(html: str, start: int) -> int | None:
    m = re.match(r"<([a-zA-Z][a-zA-Z0-9]*)\b([^>]*)>", html[start:])
    if not m:
        return None
    tag = m.group(1).lower()
    raw = m.group(0)
    if tag in VOID_TAGS or raw.rstrip().endswith("/>"):
        return start + len(raw)
    depth = 0
    i = start
    open_re = re.compile(rf"<{re.escape(tag)}\b[^>]*>", re.I)
    close_re = re.compile(rf"</{re.escape(tag)}\s*>", re.I)
    n = len(html)
    while i < n:
        if html.startswith("<!--", i):
            end = html.find("-->", i + 4)
            i = n if end == -1 else end + 3
            continue
        if html[i:i + 7].lower() == "<script":
            end = re.search(r"</script\s*>", html[i:], re.I)
            if not end:
                break
            i += end.end()
            continue
        if html[i:i + 6].lower() == "<style":
            end = re.search(r"</style\s*>", html[i:], re.I)
            if not end:
                break
            i += end.end()
            continue
        om = open_re.match(html, i)
        cm = close_re.match(html, i)
        if om and (cm is None or om.start() == i):
            chunk = om.group(0)
            if tag in VOID_TAGS or chunk.rstrip().endswith("/>"):
                i = om.end()
                continue
            depth += 1
            i = om.end()
            continue
        if cm:
            depth -= 1
            i = cm.end()
            if depth == 0:
                return i
            continue
        i += 1
    return None


def remove_by_class(html: str, class_name: str) -> str:
    while True:
        found = None
        for m in CLASS_ATTR.finditer(html):
            if class_name in class_tokens(m.group("cls")):
                found = m
                break
        if found is None:
            return html
        end = element_end(html, found.start())
        if end is None:
            return html
        html = html[: found.start()] + html[end:]


def remove_tag_if_contains(html: str, tag: str, pattern: re.Pattern) -> str:
    open_re = re.compile(rf"<{re.escape(tag)}\b[^>]*>", re.I)
    while True:
        hit = None
        for m in open_re.finditer(html):
            end = element_end(html, m.start())
            if end is None:
                continue
            chunk = html[m.start() : end]
            if pattern.search(chunk):
                hit = (m.start(), end)
                break
        if hit is None:
            return html
        html = html[: hit[0]] + html[hit[1] :]


def protect_spans(html: str) -> tuple[str, list[str]]:
    held: list[str] = []

    def stash(m: re.Match) -> str:
        held.append(m.group(0))
        return f"__HOLD{len(held) - 1}__"

    html = re.sub(
        r"https://gadgetspothub\.com/[a-z]{2}/kemppi(?:-[0-9]+)?(?:/[^\"'\s<]*)?",
        stash,
        html,
    )
    html = re.sub(r"/[a-z]{2}/kemppi(?:-[0-9]+)?(?:/[^\"'\s<]*)?", stash, html)
    html = re.sub(r"/assets/img/products/kemppi/[^\"'\s<]*", stash, html)
    html = re.sub(r"PRODUCT_SLUG:\s*'kemppi(?:-[0-9]+)?'", stash, html)
    html = re.sub(r'"slug":\s*"kemppi(?:-[0-9]+)?"', stash, html)
    html = re.sub(r"'slug':\s*'kemppi(?:-[0-9]+)?'", stash, html)
    html = re.sub(r"\bkemppi-\d+\b", stash, html)
    return html, held


def restore_spans(html: str, held: list[str]) -> str:
    for i, val in enumerate(held):
        html = html.replace(f"__HOLD{i}__", val)
    return html


def rename_kemppi(html: str) -> str:
    html = html.replace("Kemppi™", "ForgeX™")
    html = html.replace("kemppi™", "ForgeX™")
    html, held = protect_spans(html)
    html = html.replace("Kemppi", "ForgeX")
    html = re.sub(r"(?<![A-Za-z0-9_/])kemppi(?![A-Za-z0-9_-])", "forgex", html)
    return restore_spans(html, held)


def extract_geo(html: str) -> str:
    m = re.search(r"GEO:\s*'([a-z]{2})'", html)
    if m:
        return m.group(1)
    m = re.search(r'<html[^>]*\blang="([a-z]{2})"', html, re.I)
    if not m:
        return "en"
    lang = m.group(1).lower()
    return {"cs": "cz", "el": "gr", "sl": "si", "uk": "en"}.get(lang, lang)


def replace_form_endpoint(html: str) -> str:
    if TODO_ENDPOINT not in html:
        return html
    hook = IT_HOOK if extract_geo(html) == "it" else EU_HOOK
    return html.replace(TODO_ENDPOINT, hook)


def strip_discounts_and_scarcity(html: str) -> str:
    for cls in CLASS_REMOVE:
        html = remove_by_class(html, cls)
    html = re.sub(r'<span class="was">[^<]*</span>\s*', "", html)
    html = re.sub(r'<span class="pct">[^<]*</span>\s*', "", html)
    html = re.sub(r'<div class="urgency-strip">\s*</div>', "", html)
    html = re.sub(
        r"window\.POPUP_PURCHASES\s*=\s*\[.*?\];",
        "window.POPUP_PURCHASES = [];",
        html,
        flags=re.S,
    )
    html = re.sub(r',?\s*"aggregateRating"\s*:\s*\{[^{}]*\}', "", html)
    html = re.sub(r"\s*\|\s*-\d+%(?:\s+today)?", "", html, flags=re.I)
    html = re.sub(
        r"(?:SCONTO|DESCUENTO|DESCONTO|RABATT|ZĽAVA|Sleva|ZNIŻKA|ZNÍŽKA)\s+\d+%\s*\+\s*",
        "",
        html,
        flags=re.I,
    )
    html = re.sub(
        r"(?:OFFERTA|OFERTA|OFFER|AKCE|AKCIA)\s+-\d+%\s*:\s*",
        "",
        html,
        flags=re.I,
    )
    html = re.sub(
        r"\s*(?:invece di|instead of|en vez de|en lugar de|em vez de|statt)\s+[\d\s\.,]+(?:\s*(?:€|EUR|Kč|zł|lei|Ft|RON|Ft\.))?",
        "",
        html,
        flags=re.I,
    )
    html = re.sub(r",\s*con\s+[−\-]\d+%", "", html, flags=re.I)
    html = re.sub(r"\s+con\s+[−\-]\d+%\.", ".", html, flags=re.I)
    html = re.sub(r"<strong>4[,.]9/5[^<]*</strong>\s*", "", html)
    html = remove_tag_if_contains(
        html,
        "li",
        re.compile(r"4[,.][89]/5.{0,80}(?:8[.\s]?730|9[.\s]?480|3[.,\s]?842)", re.I | re.S),
    )
    html = remove_tag_if_contains(
        html,
        "p",
        re.compile(r"(?:4[,.]8/5|3[.,\s]?842).{0,60}(?:clienti|reviews|recensioni|buyers|verificat)", re.I | re.S),
    )
    html = re.sub(
        r"<p class=\"section__subtitle\">[^<]*(?:3[.,\s]?842|4[,.]8)[^<]*</p>\s*",
        "",
        html,
    )
    html = re.sub(
        r"Over <strong>4,000 garden owners</strong>",
        "Garden owners",
        html,
    )
    html = re.sub(r"Oltre <strong>4\.000[^<]*</strong>", "Chi ha un giardino", html)
    html = re.sub(r" · -70%", "", html)
    html = re.sub(r" · -\d+%", "", html)
    html = remove_by_class(html, "banner-urgency")
    html = re.sub(
        r'<div class="c4x-warning(?:-box)?">.*?</div>\s*</div>\s*</section>',
        "</section>",
        html,
        flags=re.S,
    )
    # If the warning box sits in its own section, drop leftover inner markup later via class.
    html = remove_by_class(html, "c4x-warning-box")
    return html


AC_REPLACEMENTS = [
    # Italian
    ("senza unità esterna", "senza installazione a muro"),
    ("senza un'unità esterna", "senza installazione a muro"),
    ("senza un’unità esterna", "senza installazione a muro"),
    ("né unità esterna", "né fori nel muro"),
    ("nè unità esterna", "né fori nel muro"),
    ("ni unità esterna", "né fori nel muro"),
    ("un'unità esterna", "un'installazione a muro"),
    ("un’unità esterna", "un’installazione a muro"),
    ("unità esterna", "installazione a muro"),
    ("circuito chiuso interno", "sistema portatile da pavimento"),
    # Spanish
    ("sin unidad exterior", "sin instalación en la pared"),
    ("ninguna unidad exterior", "ninguna instalación en la pared"),
    ("cero unidad exterior", "cero instalación en la pared"),
    ("ni unidad exterior", "ni instalación en la pared"),
    ("unidad exterior", "instalación en la pared"),
    ("circuito cerrado interno", "sistema portátil de suelo"),
    # Portuguese
    ("sem unidade exterior", "sem instalação na parede"),
    ("nem unidade exterior", "nem instalação na parede"),
    ("unidade exterior", "instalação na parede"),
    # Czech
    ("bez venkovní jednotky", "bez stavebních úprav ve zdi"),
    ("žádná venkovní jednotka", "žádné stavební úpravy ve zdi"),
    ("venkovní jednotkou", "stavebními úpravami ve zdi"),
    ("venkovní jednotku", "stavební úpravy ve zdi"),
    ("venkovní jednotka", "stavební úpravy ve zdi"),
    ("vnitřním uzavřeným okruhem", "přenosným podlahovým systémem"),
    # Slovak
    ("bez vonkajšej jednotky", "bez stavebných úprav v stene"),
    ("vonkajšou jednotkou", "stavebnými úpravami v stene"),
    ("vonkajšiu jednotku", "stavebné úpravy v stene"),
    ("vonkajšia jednotka", "stavebné úpravy v stene"),
    # Polish
    ("bez jednostki zewnętrznej", "bez montażu w ścianie"),
    ("jednostką zewnętrzną", "montażem w ścianie"),
    ("jednostki zewnętrznej", "montażu w ścianie"),
    ("jednostka zewnętrzna", "montaż w ścianie"),
    # Hungarian
    ("különálló kültéri egység nélkül", "falbontás nélkül"),
    ("kültéri egység nélkül", "falbontás nélkül"),
    ("kültéri egységet", "falbontást"),
    ("kültéri egység", "falbontás"),
    # Romanian
    ("fără unitate exterioară", "fără montaj în perete"),
    ("nici unitate exterioară", "nici montaj în perete"),
    ("unitate exterioară", "montaj în perete"),
    ("unitatea exterioară", "montajul în perete"),
    # Slovenian
    ("brez zunanje enote", "brez vgradnje v steno"),
    ("zunanje enote", "vgradnje v steno"),
    ("zunanjo enoto", "vgradnjo v steno"),
    ("zunanja enota", "vgradnja v steno"),
    # German
    ("ohne Außeneinheit", "ohne Wandmontage"),
    ("keine Außeneinheit", "keine Wandmontage"),
    ("Außeneinheit", "Wandmontage"),
    # French
    ("sans unité extérieure", "sans installation murale"),
    ("aucune unité extérieure", "aucune installation murale"),
    ("unité extérieure", "installation murale"),
    # Greek
    ("χωρίς εξωτερική μονάδα", "χωρίς εγκατάσταση στον τοίχο"),
    ("ούτε εξωτερική μονάδα", "ούτε εγκατάσταση στον τοίχο"),
    ("εξωτερική μονάδα", "εγκατάσταση στον τοίχο"),
    # English
    ("without an outdoor unit", "without wall installation"),
    ("without outdoor unit", "without wall installation"),
    ("no outdoor unit", "no wall installation"),
    ("outdoor unit", "wall installation"),
    ("internal closed circuit", "portable floor-standing system"),
]


def fix_ac_claims(html: str) -> str:
    for src, dst in AC_REPLACEMENTS:
        html = html.replace(src, dst)
        html = html.replace(src.capitalize(), dst[:1].upper() + dst[1:] if dst else dst)
    return html


def process_html(text: str, rel: str) -> str:
    original = text
    if "kemppi" in rel.lower() or "Kemppi" in text or "Kemppi™" in text:
        text = rename_kemppi(text)
    text = replace_form_endpoint(text)
    text = strip_discounts_and_scarcity(text)
    if any(
        key in rel.lower()
        or key in text.lower()
        for key in (
            "clima", "glacierair", "column-air", "condizionat", "climatiz",
            "air conditioner", "aire acondicionado",
        )
    ) or any(src in text for src, _ in AC_REPLACEMENTS):
        text = fix_ac_claims(text)
    return text if text != original else original


def html_files() -> list[Path]:
    out: list[Path] = []
    for p in ROOT.rglob("*.html"):
        if any(part in SKIP_DIR_NAMES for part in p.parts):
            continue
        out.append(p)
    return sorted(out)


def family_for(path: str) -> tuple[str, str]:
    slug = path.strip("/")
    if slug.endswith("/landing.html"):
        slug = slug[: -len("/landing.html")]
    if slug.endswith("/index.html"):
        slug = slug[: -len("/index.html")]
    low = slug.lower()
    mapping = [
        ("mini-saw", "Garden", "Saw 3000X"),
        ("grass-trimmer", "Garden", "T77 PRO"),
        ("hypertrimmer", "Garden", "HyperTrimmer 3000"),
        ("smartwatch", "Tech", "Nordvel"),
        ("orvyn", "Tech", "Orvyn"),
        ("fold360", "Tech", "Fold360"),
        ("clima-pro", "Climate", "Clima PRO"),
        ("climaair", "Climate", "ClimaAir"),
        ("glacierair", "Climate", "GlacierAir"),
        ("column-air", "Climate", "Polar PRO Max"),
        ("kemppi", "Tools", "ForgeX"),
        ("steamix", "Home", "SteaMix"),
        ("sprayvex", "Home", "SprayVex"),
        ("signalix", "Home", "SignaliX"),
    ]
    for needle, cat, name in mapping:
        if needle in low:
            return cat, name
    return "Other", slug.split("/")[-1] or slug


def parse_sitemap_products() -> list[str]:
    sm = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
    locs = re.findall(r"<loc>([^<]+)</loc>", sm)
    products: list[str] = []
    seen: set[str] = set()
    for loc in locs:
        path = loc.replace("https://gadgetspothub.com", "") or "/"
        if path == "/":
            continue
        if "thank-you" in path:
            continue
        leaf = path.rstrip("/").rsplit("/", 1)[-1]
        if leaf.replace(".html", "") in LEGAL_SLUGS:
            continue
        if path in seen:
            continue
        seen.add(path)
        products.append(path)
    # Prefer landing.html over the bare folder when both exist
    folders = {p for p in products if p.endswith("/")}
    filtered = []
    for p in products:
        if p.endswith("/") and (p + "landing.html") in seen:
            continue
        filtered.append(p)
    return filtered


def write_products_page(urls: list[str]) -> None:
    groups: dict[str, dict[str, list[str]]] = defaultdict(lambda: defaultdict(list))
    for url in urls:
        cat, name = family_for(url)
        groups[cat][name].append(url)

    cat_order = ["Garden", "Climate", "Tools", "Tech", "Home", "Other"]
    sections = []
    for cat in cat_order:
        if cat not in groups:
            continue
        cards = []
        for name, links in sorted(groups[cat].items()):
            items = "\n".join(
                f'          <li><a href="{href}">{href}</a></li>'
                for href in sorted(links)
            )
            cards.append(
                f"""      <article class="product-family" id="{name.lower().replace(' ', '-')}">
        <h3>{name}</h3>
        <ul>
{items}
        </ul>
      </article>"""
            )
        sections.append(
            f"""  <section class="catalog-section" id="{cat.lower()}">
    <h2>{cat}</h2>
    <div class="family-grid">
{chr(10).join(cards)}
    </div>
  </section>"""
        )

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Products — gadgetspothub.com</title>
<meta name="description" content="Full catalog of gadgetspothub.com products available with cash on delivery across Europe.">
<link rel="canonical" href="https://gadgetspothub.com/products.html">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800&display=swap">
<link rel="stylesheet" href="/assets/css/variables.css">
<link rel="stylesheet" href="/assets/css/reset.css">
<link rel="stylesheet" href="/assets/css/components.css">
<style>
.catalog {{ padding: 3rem 1rem 4rem; max-width: 1100px; margin: 0 auto; }}
.catalog h1 {{ font-size: 2rem; margin-bottom: 0.5rem; }}
.catalog .lede {{ color: var(--color-text-muted); margin-bottom: 2rem; }}
.catalog-section {{ margin-bottom: 2.5rem; }}
.catalog-section h2 {{ font-size: 1.35rem; margin-bottom: 1rem; padding-bottom: 0.35rem; border-bottom: 1px solid var(--color-border); }}
.family-grid {{ display: grid; grid-template-columns: 1fr; gap: 1rem; }}
@media (min-width: 768px) {{ .family-grid {{ grid-template-columns: 1fr 1fr; }} }}
.product-family {{ background: white; border: 1px solid var(--color-border); border-radius: 0.75rem; padding: 1.1rem 1.2rem; }}
.product-family h3 {{ margin-bottom: 0.6rem; font-size: 1.05rem; }}
.product-family ul {{ list-style: none; padding: 0; margin: 0; }}
.product-family li {{ margin: 0.25rem 0; font-size: 0.9rem; }}
.product-family a {{ color: var(--color-primary); }}
</style>
<script src="/assets/js/main.js" defer></script>
</head>
<body>
<header class="site-header">
  <div class="site-header__inner">
    <a href="/" class="site-logo" aria-label="gadgetspothub.com home">
      <span class="site-logo__text"><span class="site-logo__text-primary">gadgetspothub</span><span class="site-logo__text-accent">.com</span></span>
    </a>
    <nav class="site-header__nav" aria-label="primary">
      <a href="/products.html">Products</a>
      <a href="/#why">Why us</a>
      <a href="/en/about-us.html">About</a>
    </nav>
  </div>
</header>
<main class="catalog">
  <h1>Product catalog</h1>
  <p class="lede">Every live product page on gadgetspothub.com, grouped by category. Cash on delivery across Europe.</p>
{chr(10).join(sections)}
</main>
<footer class="site-footer">
  <div class="container">
    <div class="site-footer__bottom">
      © <span data-year>2026</span> <strong>Netmart LLC</strong> — All rights reserved. <a href="/">gadgetspothub.com</a>
    </div>
  </div>
</footer>
</body>
</html>
"""
    (ROOT / "products.html").write_text(html, encoding="utf-8")


def ensure_sitemap_products() -> None:
    path = ROOT / "sitemap.xml"
    text = path.read_text(encoding="utf-8")
    loc = "https://gadgetspothub.com/products.html"
    if loc in text:
        return
    entry = (
        f"  <url><loc>{loc}</loc><lastmod>{date.today().isoformat()}</lastmod>"
        f"<changefreq>weekly</changefreq><priority>0.9</priority></url>\n"
    )
    text = text.replace("<urlset", "<urlset", 1)
    # Insert after the homepage url block
    text = re.sub(
        r"(<url><loc>https://gadgetspothub.com/</loc>.*?</url>\n)",
        r"\1" + entry,
        text,
        count=1,
        flags=re.S,
    )
    path.write_text(text, encoding="utf-8")


def patch_generators() -> None:
    for rel in (
        "scripts/gen_climaair_geos.py",
        "scripts/gen_column_ac_geos.py",
        "scripts/gen_kemppi_geos.py",
        "scripts/gen_glacierair_geos.py",
    ):
        p = ROOT / rel
        if not p.exists():
            continue
        text = p.read_text(encoding="utf-8")
        text = text.replace(TODO_ENDPOINT, EU_HOOK)
        if "kemppi" in rel:
            text = rename_kemppi(text)
        p.write_text(text, encoding="utf-8")


def main() -> None:
    changed = 0
    for path in html_files():
        rel = str(path.relative_to(ROOT))
        original = path.read_text(encoding="utf-8")
        updated = process_html(original, rel)
        if updated != original:
            path.write_text(updated, encoding="utf-8")
            changed += 1
            print("updated", rel)
    urls = parse_sitemap_products()
    write_products_page(urls)
    ensure_sitemap_products()
    patch_generators()
    print(f"done html_changed={changed} catalog_urls={len(urls)}")


if __name__ == "__main__":
    main()
