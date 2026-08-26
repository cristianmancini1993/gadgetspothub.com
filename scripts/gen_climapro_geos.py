#!/usr/bin/env python3
"""Generate Clima PRO landings + thank-you pages for CZ ES PT SK HU LV from IT copy."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_climaair_geos import GEOS, LANDING_TMPL, SafeDict, TR, UID, WEBHOOK  # noqa: E402
from gen_climaair_ty import CONVERSION_FALLBACK, TMPL as TY_TMPL, TY, js_str  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]

PRO_COPY = {
    "cz": dict(
        title="Clima PRO — Sloupová klimatizace 4 v 1 bez instalace | -50%",
        description="Clima PRO: sloupová klimatizace 4 v 1 bez instalace a bez venkovní jednotky. Chladí, topí, odvlhčuje a čistí až 120 m². Platba na dobírku.",
        sale="DNES SLEVA 50 % · ",
        h1="Sloupová klimatizace 4 v 1 bez instalace a bez venkovní jednotky",
        lead="Chladí, topí, odvlhčuje a čistí vzduch v místnostech až do <strong>120 m²</strong> a přinese komfort během několika minut. Snižte spotřebu a zapomeňte na vysoké účty! Díky úsporné technologii a <strong>energetické třídě A+++</strong> spotřebuje jen <strong>4,50 Kč denně</strong>.",
    ),
    "es": dict(
        title="Clima PRO — Aire acondicionado de columna 4 en 1 sin instalación | -50%",
        description="Clima PRO: aire acondicionado de columna 4 en 1 sin instalación y sin unidad exterior. Enfría, calienta, deshumidifica y purifica hasta 120 m². Pago contra reembolso.",
        sale="HOY 50% DE DESCUENTO · ",
        h1="Aire acondicionado de columna 4 en 1 sin instalación y sin unidad exterior",
        lead="Enfría, calienta, deshumidifica y purifica el aire en espacios de hasta <strong>120 m²</strong>, con confort en pocos minutos. Reduce el consumo y olvídate de las facturas altas. Gracias a la tecnología de bajo consumo y a la <strong>clase energética A+++</strong>, consume solo <strong>0,18€ al día</strong>.",
    ),
    "pt": dict(
        title="Clima PRO — Ar condicionado de coluna 4 em 1 sem instalação | -50%",
        description="Clima PRO: ar condicionado de coluna 4 em 1 sem instalação e sem unidade exterior. Arrefece, aquece, desumidifica e purifica até 120 m². Pagamento à cobrança.",
        sale="HOJE COM 50% DE DESCONTO · ",
        h1="Ar condicionado de coluna 4 em 1 sem instalação e sem unidade exterior",
        lead="Arrefece, aquece, desumidifica e purifica o ar em espaços até <strong>120 m²</strong>, com conforto em poucos minutos. Reduza o consumo e esqueça as faturas altas. Graças à tecnologia de baixo consumo e à <strong>classe energética A+++</strong>, consome apenas <strong>0,18€ por dia</strong>.",
    ),
    "sk": dict(
        title="Clima PRO — Stĺpová klimatizácia 4 v 1 bez inštalácie | -50%",
        description="Clima PRO: stĺpová klimatizácia 4 v 1 bez inštalácie a bez vonkajšej jednotky. Chladí, kúri, odvlhčuje a čistí až 120 m². Platba na dobierku.",
        sale="DNES ZĽAVA 50 % · ",
        h1="Stĺpová klimatizácia 4 v 1 bez inštalácie a bez vonkajšej jednotky",
        lead="Chladí, kúri, odvlhčuje a čistí vzduch v miestnostiach až do <strong>120 m²</strong> a prinesie komfort v priebehu niekoľkých minút. Znížte spotrebu a zabudnite na vysoké účty. Vďaka úspornej technológii a <strong>energetickej triede A+++</strong> spotrebuje len <strong>0,18€ denne</strong>.",
    ),
    "hu": dict(
        title="Clima PRO — Oszlopklíma 4 az 1-ben telepítés nélkül | -50%",
        description="Clima PRO: oszlopklíma 4 az 1-ben telepítés és külső egység nélkül. Hűt, fűt, párátlanít és tisztít akár 120 m²-en. Utánvét.",
        sale="MA 50% KEDVEZMÉNY · ",
        h1="Oszlopklíma 4 az 1-ben telepítés és külső egység nélkül",
        lead="Hűt, fűt, párátlanít és tisztítja a levegőt akár <strong>120 m²</strong>-es terekben, perceken belül kényelmet adva. Csökkentse a fogyasztást, és felejtse el a magas számlákat. Az energiatakarékos technológiának és az <strong>A+++ energiaosztálynak</strong> köszönhetően napi fogyasztása csak <strong>70 Ft</strong>.",
    ),
    "lv": dict(
        title="Clima PRO — Kolonnas kondicionieris 4 vienā bez uzstādīšanas | -50%",
        description="Clima PRO: kolonnas gaisa kondicionieris 4 vienā bez uzstādīšanas un bez āra bloka. Dzesē, silda, sausina un attīra līdz 120 m². Maksa pēc saņemšanas.",
        sale="ŠODIEN 50% ATLAIDE · ",
        h1="Kolonnas gaisa kondicionieris 4 vienā bez uzstādīšanas un bez āra bloka",
        lead="Dzesē, silda, sausina un attīra gaisu telpās līdz <strong>120 m²</strong>, sniedzot komfortu dažu minūšu laikā. Samaziniet patēriņu un aizmirstiet par augstiem rēķiniem. Pateicoties energoefektīvai tehnoloģijai un <strong>enerģijas klasei A+++</strong>, patērē tikai <strong>0,18€ dienā</strong>.",
    ),
}


def rebrand(s: str) -> str:
    return (
        s.replace("ClimaAirt", "Clima PRO-t")
        .replace("ClimaAir™", "Clima PRO™")
        .replace("ClimaAir", "Clima PRO")
    )


def landing_template() -> str:
    t = LANDING_TMPL
    t = t.replace("/assets/img/products/climaair/", "/assets/img/products/climapro/")
    t = t.replace("/assets/img/reviews/climaair/", "/assets/img/reviews/climapro/")
    t = t.replace("https://gadgetspothub.com/{geo}/climaair/landing.html", "https://gadgetspothub.com/clima-pro-{geo}/")
    t = t.replace("https://gadgetspothub.com/{geo}/climaair/thank-you.html", "https://gadgetspothub.com/clima-pro-{geo}/thank-you.html")
    t = t.replace("PRODUCT_SLUG: 'climaair'", "PRODUCT_SLUG: 'climapro'")
    t = t.replace("ClimaAir Colonna {offer}", "Clima PRO {offer}")
    t = t.replace('<span class="gift-strip">{topbar}</span>', '<span class="gift-strip">{gift_strip}</span>')
    t = t.replace('alt="ClimaAir — FlowCore"', 'alt="Clima PRO — FlowCore"')
    t = t.replace('alt="ClimaAir — 4in1"', 'alt="Clima PRO — 4in1"')
    t = t.replace('alt="ClimaAir — A+++"', 'alt="Clima PRO — A+++"')
    t = t.replace('alt="ClimaAir"', 'alt="Clima PRO"')
    t = t.replace('<th class="highlight">ClimaAir</th>', '<th class="highlight">Clima PRO</th>')
    return t


def ty_template() -> str:
    t = TY_TMPL
    t = t.replace("/assets/img/products/climaair/", "/assets/img/products/climapro/")
    t = t.replace("PRODUCT_SLUG: 'climaair'", "PRODUCT_SLUG: 'climapro'")
    return t


def main() -> None:
    tmpl = landing_template()
    ty_tmpl = ty_template()
    conversion = CONVERSION_FALLBACK

    for geo, g in GEOS.items():
        dest = ROOT / f"clima-pro-{geo}"
        dest.mkdir(parents=True, exist_ok=True)

        t = {k: rebrand(v) if isinstance(v, str) else v for k, v in TR[geo].items()}
        pro = PRO_COPY[geo]
        t["title"] = pro["title"]
        t["description"] = pro["description"]
        t["h1"] = pro["h1"]
        t["lead"] = pro["lead"]
        t["gift_strip"] = t["topbar"]
        t["topbar"] = pro["sale"] + t["topbar"]
        t["cta_price"] = t["cta_price"].format(now=g["now"])
        payload = SafeDict({**t, **g, "geo": geo, "uid": UID, "webhook": WEBHOOK})
        (dest / "index.html").write_text(tmpl.format_map(payload), encoding="utf-8")

        ty = {k: rebrand(v) if isinstance(v, str) else v for k, v in TY[geo].items()}
        ty["cookie_text"] = js_str(ty["cookie_text"])
        ty["cookie_accept"] = js_str(ty["cookie_accept"])
        ty["cookie_learn"] = js_str(ty["cookie_learn"])
        ty_payload = {**ty, **g, "geo": geo, "conversion": "__CONVERSION__"}
        html = ty_tmpl.format_map(ty_payload).replace("__CONVERSION__", conversion)
        (dest / "thank-you.html").write_text(html, encoding="utf-8")
        print(f"wrote clima-pro-{geo}/  {g['now']}")


if __name__ == "__main__":
    main()
