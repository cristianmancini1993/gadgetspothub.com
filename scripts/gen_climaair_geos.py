#!/usr/bin/env python3
"""Generate ClimaAir landings + thank-you pages for CZ, ES, PT, SK, HU, LV."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

UID = "018e3961-c73a-7965-8fc1-b1d91c869a42"
WEBHOOK = "https://hook.eu2.make.com/i7pmea9fmpnepx94e5z6dxfwvl1bnnlh"

GEOS = {
    "cz": {
        "lang": "cs",
        "price_num": 1799,
        "currency": "CZK",
        "now": "1 799 Kč",
        "was": "3 598 Kč",
        "offer": "3296",
        "lp": "3331",
        "key": "2e911573b43a938cd5f4e1ea7dd831ca09a55cb2",
        "ty_src": "cz/glacierair-3296/thank-you.html",
    },
    "es": {
        "lang": "es",
        "price_num": 79,
        "currency": "EUR",
        "now": "79,00€",
        "was": "158,00€",
        "offer": "3345",
        "lp": "3381",
        "key": "966f56691d89d38b31d7e0b66079940f7053b299",
        "ty_src": "es/glacierair-3345/thank-you.html",
    },
    "pt": {
        "lang": "pt",
        "price_num": 89,
        "currency": "EUR",
        "now": "89,00€",
        "was": "178,00€",
        "offer": "3344",
        "lp": "3380",
        "key": "18a640cca42e03c2080deafc1b9c8a2e080b827e",
        "ty_src": "pt/glacierair-3344/thank-you.html",
    },
    "sk": {
        "lang": "sk",
        "price_num": 69,
        "currency": "EUR",
        "now": "69,00€",
        "was": "138,00€",
        "offer": "4242",
        "lp": "4282",
        "key": "8394e527c08d4895581cafd27c1525af627df57e",
        "ty_src": "sk/glacierair-4242/thank-you.html",
    },
    "hu": {
        "lang": "hu",
        "price_num": 39900,
        "currency": "HUF",
        "now": "39 900 Ft",
        "was": "79 800 Ft",
        "offer": "3295",
        "lp": "3330",
        "key": "2cca5eb446c005b630e493e1d6881a3ad4049e87",
        "ty_src": "hu/glacierair-3295/thank-you.html",
    },
    "lv": {
        "lang": "lv",
        "price_num": 89,
        "currency": "EUR",
        "now": "89,00€",
        "was": "178,00€",
        "offer": "4243",
        "lp": "4283",
        "key": "c1061e58cf3bfd47bb5b66d084d7e09167b3c945",
        "ty_src": "lv/glacierair-4243/thank-you.html",
    },
}

TR = {
    "cz": dict(
        title="ClimaAir™ 4in1 — Sloupová klimatizace bez venkovní jednotky | -50%",
        description="ClimaAir™ 4in1: chladí, topí, odvlhčuje a čistí vzduch bez venkovní jednotky a bez technika. 18.000 BTU, 120 m², platba na dobírku v Česku.",
        submitting="Odesílání...",
        cookie_text="Používáme technické a cookies třetích stran ke zlepšení vašeho zážitku a pro analytiku.",
        cookie_accept="Přijmout",
        cookie_learn="Zjistit více",
        topbar="❄️ Platba na dobírku · Doručení 24/48 h",
        h1="ClimaAir™ 4in1: ochladí, vytopí, odvlhčí a vyčistí vzduch v celém domě za pouhých <span class=\"hl\">7 minut</span>, bez venkovní jednotky a bez volání technika!",
        lead="Postavíte ho na zem a zapojíte do běžné zásuvky: chladí, topí, ničí germy a bakterie a odvlhčuje vzduch — vše v jednom přístroji. Díky internímu systému <strong>FlowCore®</strong> ušetříte každý měsíc až <strong>87 %</strong> na účtech za energie!",
        alt_hero="ClimaAir přenosná sloupová klimatizace 4 v 1",
        stock_pill="🔥 Za tuto cenu zbývá jen <strong>7 kusů</strong>",
        b1_t="120 m² vychlazeno za 5 minut.",
        b1_d="Z ložnice do obýváku: přesunete ho na kolečkách a místnost změní teplotu dřív, než se stihnete připravit na noc.",
        b2_t="Ticho 18 dB — tišší než šepot.",
        b2_d="Usnete a ani nevíte, že běží: navrženo speciálně do ložnice.",
        b3_t="Žádné díry ve zdi, žádná venkovní jednotka, žádný technik.",
        b3_d="Vytáhnete ho z krabice, postavíte na zem, zapojíte šňůru a za 5 minut je připravený.",
        b4_t="Spotřeba jen 4,50 Kč denně.",
        b4_d="Inteligentní technologie snižuje spotřebu na minimum: žádná nepříjemná překvapení na účtu.",
        b5_t="4 funkce v 1, ovládání z telefonu.",
        b5_d="Chladí, topí, odvlhčuje a čistí: vše nastavíte, aniž byste vstali z postele.",
        cta_hero="Ano, chci spát v chládku: objednávám teď",
        secure="Bezpečný nákup • Expresní doručení • Kompletní záruka",
        t1_h="Rychlé doručení", t1_p="Balíček dorazí k vám domů do 24–48 hodin.",
        t2_h="Platíte při převzetí", t2_p="Žádná platba předem: zaplatíte, až balíček obdržíte",
        t3_h="Nákup pod ochranou", t3_p="Vaše osobní údaje jsou 100% chráněny",
        t4_h="Záruka 2 roky", t4_p="Můžete ho vrátit bez starostí do 60 dnů",
        pieces="ZBÝVÁ JEN 7 KUSŮ",
        warn_h="Důležité! Sklad se rychle vyprazdňuje!",
        warn_p="Právě teď má na tento produkt spousta dalších zákazníků oči. Proto dostupné kusy mizí tak rychle. Objednejte hned a zajistěte si jeden z posledních kusů za dnešní slevovou cenu.",
        countdown="⏰ Nabídka -50 % platí jen dnes",
        hours="Hod", mins="Min", secs="Sek",
        stock_l="Ještě dostupné kusy", stock_r="Zbývá jen pár kusů!",
        live="<strong>{n} lidí</strong> právě sleduje ClimaAir",
        live0="<strong>41 lidí</strong> právě sleduje ClimaAir",
        form_h="Vyplňte objednávkový formulář",
        form_p="Budeme vás kontaktovat kvůli potvrzení detailů doručení.",
        lab_name="Jméno a příjmení*", lab_tel="Telefon*", lab_addr="Doručovací adresa*",
        ph_name="Jan Novák", ph_tel="+420 601 123 456", ph_addr="Ulice 10, 110 00 Praha",
        buy="KOUPIT NYNÍ",
        form_note="🔒 Bez zálohy · Platíte až při doručení · Doprava 24/48 h",
        benefits_ey="✅ Skutečné výhody",
        benefits_h="Žádná instalace, žádná venkovní jednotka, žádný technik. Postavíte ho na zem, zapojíte šňůru a hotovo.",
        w1_ey="01 — Technologie FlowCore®",
        w1_h="FlowCore® nahrazuje kompresor a chladicí plyny",
        w1_t1="⏱️ Připraveno za 90 sekund", w1_t2="👉 Na kolečkách",
        w1_p="FlowCore® je vysoce účinný interní systém, který nahrazuje tradiční kompresor a chladiva. Funguje zapojený do domácí zásuvky: stojí volně na zemi, bez kotvení do zdi a bez venkovní jednotky.",
        w1_i="Spustí se do 90 sekund a nastavené teploty dosáhne zhruba za 5 minut. Na kolečkách ho přesunete z místnosti do místnosti za deset sekund: ložnice, obývák, kancelář — stále stejný přístroj. Bez nabídek, bez řemeslníků, bez čekání týdny.",
        w2_ey="02 — 4 funkce, jeden přístroj",
        w2_h="Chladí, topí, odvlhčuje a čistí",
        w2_t1="16°C – 40°C", w2_t2="99 % zárodků",
        w2_p="ClimaAir™ chladí, topí, čistí vzduch trojitým filtrem a automaticky odvlhčuje. Chladí až na <strong>16°C</strong>, topí až na <strong>40°C</strong>, odstraní až <strong>99 %</strong> zárodků a bakterií ze vzduchu.",
        w2_i="Už nemusíte kupovat zvlášť odvlhčovač, čističku a přímotop. Ušetříte místo v bytě i tisíce korun za další nákupy.",
        w3_ey="03 — Minimální spotřeba, maximální úspora",
        w3_h="Energetická třída A+++ a nižší účty",
        w3_t1="3 Kč / hod", w3_t2="Až -80 %",
        w3_p="Díky třídě A+++ ClimaAir™ automaticky ladí výkon a proudění podle teploty v místnosti. Spotřeba od <strong>3 Kč za hodinu</strong>, až o <strong>80 % méně</strong> než u klasické klimatizace s venkovní jednotkou.",
        w3_i="Můžete ho nechat běžet celou noc, každý den, aniž byste na konci měsíce s obavami koukali na účet.",
        cta_mid="Objednejte ClimaAir™ teď ↓",
        mid1="💵 Platba na dobírku", mid2="🚚 Doručení 24/48 h", mid3="↩️ 60 dní na vyzkoušení",
        cmp_ey="⚖️ Srovnání",
        cmp_h="Proč ClimaAir poráží klasickou klimatizaci",
        cmp_sub="Stejný chladný vzduch, žádná práce navíc.",
        cmp_trad="Klasická klimatizace",
        r1c="Instalace", r1a="Technik + venkovní jednotka", r1b="✅ Žádná: postavíte na zem a zapojíte",
        r2c="Čas", r2a="Dny nebo týdny", r2b="✅ Připraveno za 5 minut",
        r3c="Cena instalace", r3a="10 000–20 000 Kč", r3b="✅ 0 Kč",
        r4c="Noční hluk", r4a="35–45 dB, často ruší", r4b="✅ 18 dB, skoro neslyšitelné",
        r5c="Funkce", r5a="Jen chladí", r5b="✅ Chladí, topí, odvlhčuje, čistí",
        r6c="Můžete ho přemístit?", r6a="Ne: zůstane tam, kde ho namontovali", r6b="✅ Ano: je na kolečkách, odvezete ho kamkoli",
        cta_price="Ano, chci ClimaAir za {now} →",
        rev_ey="⭐ Kdo ho používá každý den",
        rev_h="Co říkají rodiny, které ho už vyzkoušely",
        rev_sub="★★★★★ 4,8/5 z více než 1 824 ověřených recenzí",
        rev1="„Byla jsem skeptická, myslela jsem, že je to další gadget, který skončí ve sklepě. Místo toho ho používám každý den od června: v ložnici večer je perfektní a s časovačem se sám vypne. Jediná vada: dálkový ovladač, občas ho ztratím v peřinách ahah“",
        a1="Jana T., Praha ✅ — Ověřený nákup",
        rev2="„Pořídili jsme ho do pracovny manžela, který pracuje z domova. V zimě ho ráno zapne a za pár sekund je teplo. Lednový účet byl nižší, než jsme čekali — a to byl ten pravý důvod, proč ho doporučujeme.“",
        a2="David P., Brno ✅ — Ověřený nákup",
        rev3="„Bydlím v nájmu a nemohla jsem nainstalovat pořádnou klimatizaci. S ClimaAir™ jsem to vyřešila za odpoledne: žádná díra, žádné povolení od majitele. V létě ho mám v ložnici, v zimě v obýváku. V tichém nočním režimu ho skoro neslyším.“",
        a3="Sara M., Ostrava ✅ — Ověřený nákup",
        kit_ey="📦 Co je v balení",
        kit_h="Všechno v krabici.<br>Žádné další nákupy. Žádná překvapení.",
        kit_p="Otevřete krabici, postavíte ho na zem, zapojíte šňůru a za 5 minut je v místnosti chladno. A to je vše.",
        k1="1× přenosná sloupová klimatizace ClimaAir 18.000 BTU",
        k2="4× otočná kolečka už namontovaná na základně",
        k3="1× dálkový ovladač v balení",
        k4="1× návod k použití v češtině",
        k5="Přístup k aplikaci pro ovládání z telefonu",
        k6="Doprava zdarma do 24–48 h",
        k7="Prodloužená záruka 2 roky",
        faq_ey="❓ Časté otázky",
        faq_h="Máte pochybnosti? To je v pořádku.<br>Vyjasníme je tady.",
        faq_lead="Než objednáte, najděte odpovědi na nejčastější otázky o hluku, instalaci, platbě a záruce.",
        q1="Je v noci hlučný?",
        a_q1="Ne: v nočním režimu klesne na 18 dB, tišší než šepot. Je navržený právě do ložnice.",
        q2="Musím ho instalovat nebo volat technika?",
        a_q2="Ne. ClimaAir se nepřipevňuje na zeď a nemá venkovní jednotku: postavíte ho na zem, zapojíte šňůru a za 5 minut funguje. Když chcete změnit místnost, odstrčíte ho na kolečkách.",
        q3="Opravdu pokryje 120 m²?",
        a_q3="Ano, díky výkonu 18.000 BTU. U velmi velkých prostor ho nechte v hlavní místnosti a nechte dveře otevřené, aby se vzduch rozložil.",
        q4="Umí jen chladit, nebo i topit?",
        a_q4="Obojí. V létě chladí, v zimě topí a navíc odvlhčuje a čistí vzduch: jeden přístroj na celý rok.",
        q5="Jak funguje platba?",
        a_q5="Zaplatíte v hotovosti kurýrovi, až balíček dorazí domů. Žádná platba předem, žádná karta.",
        q6="A když mě to nepřesvědčí?",
        a_q6="Máte 60 dní na vrácení a plnou náhradu. Bez otázek, bez komplikací.",
        bt1="💶 Platba na dobírku", bt2="🚚 Doručení 24/48 h", bt3="↩️ Vrácení 60 dní",
        foot_blurb="Užitečné produkty pro každodenní život, doručení do 24–48 hodin s platbou na dobírku.",
        foot_info="Informace", foot_contact="Kontakt",
        about="O nás", contact="Kontaktujte nás",
        privacy="Zásady ochrany osobních údajů", terms="Smluvní podmínky",
        cookies="Zásady používání souborů cookie", ship="Zásady dopravy", refund="Zásady vrácení peněz",
        rights="Všechna práva vyhrazena",
    ),
    "es": dict(
        title="ClimaAir™ 4in1 — Aire acondicionado de columna sin unidad exterior | -50%",
        description="ClimaAir™ 4in1: enfría, calienta, deshumidifica y purifica el aire sin unidad exterior y sin técnico. 18.000 BTU, 120 m², pago contra reembolso en España.",
        submitting="Enviando...",
        cookie_text="Usamos cookies técnicas y de terceros para mejorar tu experiencia y para análisis.",
        cookie_accept="Aceptar",
        cookie_learn="Más información",
        topbar="❄️ Pago contra reembolso · Envío 24/48 h",
        h1="ClimaAir™ 4in1: enfría, calienta, deshumidifica y purifica el aire de toda la casa en solo <span class=\"hl\">7 minutos</span>, sin unidad exterior y sin llamar a un técnico!",
        lead="Lo apoyas en el suelo y lo enchufas a un tomacorriente normal: enfría, calienta, elimina gérmenes y bacterias y deshumidifica el aire, todo con un solo aparato. Gracias al sistema interno <strong>FlowCore®</strong> cada mes ahorras hasta un <strong>87%</strong> en la factura!",
        alt_hero="ClimaAir climatizador de columna portátil 4 en 1",
        stock_pill="🔥 Solo quedan <strong>7 unidades</strong> a este precio",
        b1_t="120 m² refrigerados en 5 minutos.",
        b1_d="Del dormitorio al salón: lo mueves sobre ruedas y la habitación cambia de temperatura antes de que termines de prepararte para la noche.",
        b2_t="Silencio de 18 dB — menos que un susurro.",
        b2_d="Te duermes y ni te das cuenta de que está encendido: pensado para el dormitorio.",
        b3_t="Cero agujeros en la pared, cero unidad exterior, ningún técnico.",
        b3_d="Lo sacas de la caja, lo apoyas en el suelo, enchufas y está listo en 5 minutos.",
        b4_t="Consume solo 0,18€ al día.",
        b4_d="Tecnología inteligente que reduce el consumo al mínimo: cero sorpresas en la factura.",
        b5_t="4 funciones en 1, control desde el móvil.",
        b5_d="Enfría, calienta, deshumidifica y purifica: lo regulas sin levantarte de la cama.",
        cta_hero="Sí, quiero dormir fresco: pido ahora",
        secure="Compra segura • Envío exprés • Garantía completa",
        t1_h="Envío rápido", t1_p="El paquete llega a tu casa en 24–48 horas.",
        t2_h="Pagas al recibir", t2_p="Sin cargo anticipado: pagas solo cuando llega el paquete",
        t3_h="Compra protegida", t3_p="Tus datos personales están protegidos al 100%",
        t4_h="Garantía 2 años", t4_p="Puedes devolverlo sin preocupaciones en 60 días",
        pieces="SOLO QUEDAN 7 UNIDADES",
        warn_h="¡Importante! El almacén se está vaciando rápido!",
        warn_p="Ahora mismo muchos otros clientes tienen los ojos puestos en este producto: por eso las unidades disponibles bajan tan rápido. Compra ya y asegúrate una de las últimas unidades al precio de hoy.",
        countdown="⏰ Oferta -50% activa solo hoy",
        hours="Hrs", mins="Min", secs="Seg",
        stock_l="Unidades aún disponibles", stock_r="¡Quedan pocas unidades!",
        live="<strong>{n} personas</strong> están viendo ClimaAir ahora",
        live0="<strong>41 personas</strong> están viendo ClimaAir ahora",
        form_h="Completa el formulario de pedido",
        form_p="Te contactaremos para confirmar los datos de entrega.",
        lab_name="Nombre y apellidos*", lab_tel="Teléfono*", lab_addr="Dirección de entrega*",
        ph_name="Juan García", ph_tel="+34 612 345 678", ph_addr="Calle Mayor 10, 28013 Madrid",
        buy="COMPRAR AHORA",
        form_note="🔒 Sin anticipo · Pagas al recibir · Envío 24/48 h",
        benefits_ey="✅ Los beneficios reales",
        benefits_h="Ninguna instalación, ninguna unidad exterior, ningún técnico. Lo apoyas en el suelo, enchufas y listo.",
        w1_ey="01 — Tecnología FlowCore®",
        w1_h="FlowCore® sustituye el compresor y los gases refrigerantes",
        w1_t1="⏱️ Listo en 90 segundos", w1_t2="👉 Con ruedas",
        w1_p="FlowCore® es el sistema interno de alta eficiencia que sustituye el compresor y los refrigerantes tradicionales. Funciona enchufado a un tomacorriente de casa: se sostiene solo, apoyado en el suelo, sin fijaciones a la pared ni unidad exterior.",
        w1_i="Se activa en menos de 90 segundos y alcanza la temperatura en unos 5 minutos. Con las ruedas lo mueves de una habitación a otra en diez segundos: dormitorio, salón, oficina, siempre el mismo aparato. Sin presupuestos, sin operarios, sin esperar semanas.",
        w2_ey="02 — 4 funciones, un solo aparato",
        w2_h="Enfría, calienta, deshumidifica y purifica",
        w2_t1="16°C – 40°C", w2_t2="99% gérmenes",
        w2_p="ClimaAir™ enfría, calienta, purifica el aire con filtro de triple acción y deshumidifica en automático. Enfría hasta <strong>16°C</strong>, calienta hasta <strong>40°C</strong>, elimina hasta el <strong>99%</strong> de gérmenes y bacterias del aire.",
        w2_i="Ya no tendrás que comprar un deshumidificador, un purificador y un calefactor por separado. Ahorras espacio en casa y cientos de euros en compras múltiples.",
        w3_ey="03 — Consumo mínimo, ahorro máximo",
        w3_h="Clase energética A+++ y facturas más bajas",
        w3_t1="0,12€ / hora", w3_t2="Hasta -80%",
        w3_p="Gracias a la clase A+++, ClimaAir™ optimiza automáticamente potencia y flujo de aire según la temperatura de la habitación. Consumo desde <strong>0,12€ la hora</strong>, hasta un <strong>80% menos</strong> que un aire acondicionado tradicional con unidad exterior.",
        w3_i="Podrás dejarlo encendido toda la noche, todos los días, sin mirar la factura con ansiedad a fin de mes.",
        cta_mid="Pide ahora tu ClimaAir™ ↓",
        mid1="💵 Pago contra reembolso", mid2="🚚 Envío 24/48 h", mid3="↩️ 60 días de prueba",
        cmp_ey="⚖️ La comparación",
        cmp_h="Por qué ClimaAir gana al aire acondicionado tradicional",
        cmp_sub="El mismo aire fresco, ningún trabajo necesario.",
        cmp_trad="Aire acondicionado tradicional",
        r1c="Instalación", r1a="Técnico + unidad exterior", r1b="✅ Ninguna: lo apoyas en el suelo y enchufas",
        r2c="Tiempos", r2a="Días o semanas", r2b="✅ Listo en 5 minutos",
        r3c="Coste de instalación", r3a="400-800€", r3b="✅ 0€",
        r4c="Ruido nocturno", r4a="35-45 dB, a menudo molesta", r4b="✅ 18 dB, casi imperceptible",
        r5c="Funciones", r5a="Solo enfría", r5b="✅ Enfría, calienta, deshumidifica, purifica",
        r6c="¿Puedes moverlo?", r6a="No: queda fijo en la pared donde lo montaron", r6b="✅ Sí: va sobre ruedas, lo llevas a cualquier habitación",
        cta_price="Sí, quiero ClimaAir a {now} →",
        rev_ey="⭐ Quién lo usa cada día",
        rev_h="Qué dicen las familias que ya lo han probado",
        rev_sub="★★★★★ 4,8/5 en más de 1.824 reseñas verificadas",
        rev1="«Estaba escéptica, pensaba que era otro gadget que acaba en el trastero. En cambio lo uso cada día desde junio: en el dormitorio por la noche es perfecto, y con el temporizador se apaga solo. El único pero: el mando, a veces lo pierdo entre las sábanas jaja»",
        a1="Julia T., Madrid ✅ — Compra verificada",
        rev2="«Lo compramos para el despacho de mi marido, que trabaja desde casa. En invierno lo enciende por la mañana y ya está caliente en segundos. La factura de enero fue más baja de lo esperado, y ese fue el verdadero motivo para recomendarlo.»",
        a2="David P., Barcelona ✅ — Compra verificada",
        rev3="«Vivo de alquiler y no podía instalar un aire acondicionado de verdad. Con ClimaAir™ lo resolví en una tarde: ningún agujero, ningún permiso al casero. En verano lo tengo en el dormitorio, en invierno en el salón. De noche en modo silencioso ni lo oigo.»",
        a3="Sara M., Valencia ✅ — Compra verificada",
        kit_ey="📦 Qué hay en el paquete",
        kit_h="Todo en la caja.<br>Cero compras extra. Cero sorpresas.",
        kit_p="Abres la caja, lo apoyas en el suelo, enchufas y en 5 minutos la habitación ya está fresca. Eso es todo.",
        k1="1× climatizador de columna portátil ClimaAir 18.000 BTU",
        k2="4× ruedas giratorias ya montadas en la base",
        k3="1× mando a distancia incluido",
        k4="1× manual de uso en español",
        k5="Acceso a la app para control desde el smartphone",
        k6="Envío gratuito en 24-48 h",
        k7="Garantía ampliada 2 años",
        faq_ey="❓ Preguntas frecuentes",
        faq_h="¿Tienes dudas? Es normal.<br>Las aclaramos aquí.",
        faq_lead="Antes de pedir, encuentra respuestas sobre ruido, instalación, pago y garantía.",
        q1="¿Hace ruido por la noche?",
        a_q1="No: en modo noche baja a 18 dB, más bajo que un susurro. Está pensado para el dormitorio.",
        q2="¿Tengo que instalarlo o llamar a un técnico?",
        a_q2="No. ClimaAir no se fija a la pared y no tiene unidad exterior: lo apoyas en el suelo, enchufas y en 5 minutos está listo. Si quieres cambiar de habitación, lo empujas sobre las ruedas.",
        q3="¿Cubre de verdad 120 m²?",
        a_q3="Sí, gracias a la potencia de 18.000 BTU. En espacios muy grandes, déjalo en la habitación principal y abre las puertas para distribuir el aire.",
        q4="¿Solo enfría o también calienta?",
        a_q4="Ambos. Enfría en verano, calienta en invierno y además deshumidifica y purifica: un solo aparato para todo el año.",
        q5="¿Cómo funciona el pago?",
        a_q5="Pagas en efectivo al mensajero cuando llega el paquete a casa. Sin pago anticipado, sin tarjeta.",
        q6="¿Y si no me convence?",
        a_q6="Tienes 60 días para devolverlo y recibir el reembolso completo. Sin preguntas, sin complicaciones.",
        bt1="💶 Pago contra reembolso", bt2="🚚 Envío 24/48 h", bt3="↩️ Devolución 60 días",
        foot_blurb="Productos útiles para el día a día, entrega en 24–48 horas con pago contra reembolso.",
        foot_info="Información", foot_contact="Contacto",
        about="Sobre nosotros", contact="Contáctanos",
        privacy="Política de privacidad", terms="Términos y condiciones",
        cookies="Política de cookies", ship="Política de envío", refund="Política de reembolso",
        rights="Todos los derechos reservados",
    ),
    "pt": dict(
        title="ClimaAir™ 4in1 — Ar condicionado de coluna sem unidade exterior | -50%",
        description="ClimaAir™ 4in1: arrefece, aquece, desumidifica e purifica o ar sem unidade exterior e sem técnico. 18.000 BTU, 120 m², pagamento à cobrança em Portugal.",
        submitting="A enviar...",
        cookie_text="Usamos cookies técnicos e de terceiros para melhorar a sua experiência e para análises.",
        cookie_accept="Aceitar",
        cookie_learn="Saber mais",
        topbar="❄️ Pagamento à cobrança · Envio 24/48 h",
        h1="ClimaAir™ 4in1: arrefece, aquece, desumidifica e purifica o ar de toda a casa em apenas <span class=\"hl\">7 minutos</span>, sem unidade exterior e sem chamar um técnico!",
        lead="Pousa no chão e liga à tomada normal: arrefece, aquece, elimina germes e bactérias e desumidifica o ar, tudo num só aparelho. Graças ao sistema interno <strong>FlowCore®</strong> poupa até <strong>87%</strong> na fatura todos os meses!",
        alt_hero="ClimaAir climatizador de coluna portátil 4 em 1",
        stock_pill="🔥 Restam apenas <strong>7 unidades</strong> a este preço",
        b1_t="120 m² arrefecidos em 5 minutos.",
        b1_d="Do quarto à sala: move-o sobre rodas e a divisão muda de temperatura antes de acabares de te preparares para a noite.",
        b2_t="Silêncio de 18 dB — menos que um sussurro.",
        b2_d="Adormeces e nem reparas que está ligado: pensado para o quarto.",
        b3_t="Zero furos na parede, zero unidade exterior, nenhum técnico.",
        b3_d="Tiras da caixa, pousas no chão, ligas a ficha e está pronto em 5 minutos.",
        b4_t="Consome apenas 0,18€ por dia.",
        b4_d="Tecnologia inteligente que reduz o consumo ao mínimo: zero surpresas na fatura.",
        b5_t="4 funções em 1, controlo pelo smartphone.",
        b5_d="Arrefece, aquece, desumidifica e purifica: regulas tudo sem sair da cama.",
        cta_hero="Sim, quero dormir fresco: encomendo agora",
        secure="Compra segura • Envio expresso • Garantia completa",
        t1_h="Envio rápido", t1_p="A encomenda chega a casa em 24–48 horas.",
        t2_h="Paga na entrega", t2_p="Sem cobrança antecipada: paga só quando receber o pacote",
        t3_h="Compra protegida", t3_p="Os seus dados pessoais estão protegidos a 100%",
        t4_h="Garantia 2 anos", t4_p="Pode devolver sem preocupações em 60 dias",
        pieces="RESTAM APENAS 7 UNIDADES",
        warn_h="Importante! O armazém está a esvaziar-se depressa!",
        warn_p="Neste momento muitos outros clientes estão de olho neste produto: por isso as unidades disponíveis descem tão rápido. Compre já e garanta uma das últimas unidades ao preço de hoje.",
        countdown="⏰ Oferta -50% ativa só hoje",
        hours="Hrs", mins="Min", secs="Seg",
        stock_l="Unidades ainda disponíveis", stock_r="Restam poucas unidades!",
        live="<strong>{n} pessoas</strong> estão a ver ClimaAir agora",
        live0="<strong>41 pessoas</strong> estão a ver ClimaAir agora",
        form_h="Preencha o formulário de encomenda",
        form_p="Vamos contactá-lo para confirmar os dados de entrega.",
        lab_name="Nome e apelido*", lab_tel="Telefone*", lab_addr="Morada de entrega*",
        ph_name="João Silva", ph_tel="+351 912 345 678", ph_addr="Rua Augusta 10, 1100-053 Lisboa",
        buy="COMPRAR AGORA",
        form_note="🔒 Sem adiantamento · Paga na entrega · Envio 24/48 h",
        benefits_ey="✅ Os benefícios reais",
        benefits_h="Nenhuma instalação, nenhuma unidade exterior, nenhum técnico. Pousa no chão, liga a ficha e está feito.",
        w1_ey="01 — Tecnologia FlowCore®",
        w1_h="FlowCore® substitui o compressor e os gases refrigerantes",
        w1_t1="⏱️ Pronto em 90 segundos", w1_t2="👉 Com rodas",
        w1_p="FlowCore® é o sistema interno de alta eficiência que substitui o compressor e os refrigerantes tradicionais. Funciona ligado à tomada de casa: fica de pé sozinho, pousado no chão, sem fixações na parede nem unidade exterior.",
        w1_i="Ativa-se em menos de 90 segundos e atinge a temperatura em cerca de 5 minutos. Com as rodas move-o de uma divisão para outra em dez segundos: quarto, sala, escritório, sempre o mesmo aparelho. Sem orçamentos, sem operários, sem esperar semanas.",
        w2_ey="02 — 4 funções, um só aparelho",
        w2_h="Arrefece, aquece, desumidifica e purifica",
        w2_t1="16°C – 40°C", w2_t2="99% germes",
        w2_p="ClimaAir™ arrefece, aquece, purifica o ar com filtro de tripla ação e desumidifica em automático. Arrefece até <strong>16°C</strong>, aquece até <strong>40°C</strong>, elimina até <strong>99%</strong> de germes e bactérias no ar.",
        w2_i="Já não precisa de comprar um desumidificador, um purificador e um aquecedor em separado. Poupa espaço em casa e centenas de euros em compras múltiplas.",
        w3_ey="03 — Consumo mínimo, poupança máxima",
        w3_h="Classe energética A+++ e faturas mais leves",
        w3_t1="0,12€ / hora", w3_t2="Até -80%",
        w3_p="Graças à classe A+++, o ClimaAir™ otimiza automaticamente potência e fluxo de ar segundo a temperatura da divisão. Consumo desde <strong>0,12€ por hora</strong>, até <strong>80% menos</strong> do que um ar condicionado tradicional com unidade exterior.",
        w3_i="Pode deixá-lo ligado a noite toda, todos os dias, sem olhar para a fatura com ansiedade no fim do mês.",
        cta_mid="Encomende agora o seu ClimaAir™ ↓",
        mid1="💵 Pagamento à cobrança", mid2="🚚 Envio 24/48 h", mid3="↩️ 60 dias de prova",
        cmp_ey="⚖️ A comparação",
        cmp_h="Porque o ClimaAir vence o ar condicionado tradicional",
        cmp_sub="O mesmo ar fresco, nenhum trabalho necessário.",
        cmp_trad="Ar condicionado tradicional",
        r1c="Instalação", r1a="Técnico + unidade exterior", r1b="✅ Nenhuma: pousa no chão e liga a ficha",
        r2c="Tempos", r2a="Dias ou semanas", r2b="✅ Pronto em 5 minutos",
        r3c="Custo de instalação", r3a="400-800€", r3b="✅ 0€",
        r4c="Ruído noturno", r4a="35-45 dB, muitas vezes incomoda", r4b="✅ 18 dB, quase impercetível",
        r5c="Funções", r5a="Só arrefece", r5b="✅ Arrefece, aquece, desumidifica, purifica",
        r6c="Pode movê-lo?", r6a="Não: fica fixo na parede onde o montaram", r6b="✅ Sim: tem rodas, leva-o para qualquer divisão",
        cta_price="Sim, quero ClimaAir a {now} →",
        rev_ey="⭐ Quem o usa todos os dias",
        rev_h="O que dizem as famílias que já o experimentaram",
        rev_sub="★★★★★ 4,8/5 em mais de 1.824 avaliações verificadas",
        rev1="«Estava cética, pensava que era mais um gadget a acabar na arrecadação. Em vez disso uso-o todos os dias desde junho: no quarto à noite é perfeito, e com o temporizador desliga-se sozinho. O único senão: o comando, às vezes perco-o entre os lençóis ahah»",
        a1="Júlia T., Lisboa ✅ — Compra verificada",
        rev2="«Comprámos para o escritório do meu marido, que trabalha em casa. No inverno liga de manhã e já está quente em segundos. A fatura de janeiro foi mais baixa do que o esperado, e esse foi o verdadeiro motivo para o recomendar.»",
        a2="David P., Porto ✅ — Compra verificada",
        rev3="«Vivo de arrendamento e não podia instalar um ar condicionado a sério. Com o ClimaAir™ resolvi numa tarde: nenhum furo, nenhuma autorização do senhorio. No verão fica no quarto, no inverno na sala. À noite no modo silencioso nem o oiço.»",
        a3="Sara M., Faro ✅ — Compra verificada",
        kit_ey="📦 O que encontra na caixa",
        kit_h="Tudo na caixa.<br>Zero compras extra. Zero surpresas.",
        kit_p="Abre a caixa, pousa no chão, liga a ficha e em 5 minutos a divisão já está fresca. É só isto.",
        k1="1× climatizador de coluna portátil ClimaAir 18.000 BTU",
        k2="4× rodas giratórias já montadas na base",
        k3="1× comando incluído",
        k4="1× manual de utilização em português",
        k5="Acesso à app para controlo pelo smartphone",
        k6="Envio gratuito em 24-48 h",
        k7="Garantia alargada 2 anos",
        faq_ey="❓ Perguntas frequentes",
        faq_h="Tem dúvidas? É normal.<br>Esclarecemos aqui.",
        faq_lead="Antes de encomendar, encontre respostas sobre ruído, instalação, pagamento e garantia.",
        q1="Faz barulho à noite?",
        a_q1="Não: no modo noite desce para 18 dB, mais baixo do que um sussurro. Foi pensado para o quarto.",
        q2="Tenho de o instalar ou chamar um técnico?",
        a_q2="Não. O ClimaAir não se fixa à parede e não tem unidade exterior: pousa no chão, liga a ficha e em 5 minutos está a funcionar. Se quiser mudar de divisão, empurra-o sobre as rodas.",
        q3="Cobre mesmo 120 m²?",
        a_q3="Sim, graças à potência de 18.000 BTU. Em espaços muito grandes, deixe-o na divisão principal e abra as portas para distribuir o ar.",
        q4="Só arrefece ou também aquece?",
        a_q4="Ambos. Arrefece no verão, aquece no inverno e ainda desumidifica e purifica: um só aparelho para o ano todo.",
        q5="Como funciona o pagamento?",
        a_q5="Paga em numerário ao estafeta quando a encomenda chega a casa. Sem pagamento antecipado, sem cartão.",
        q6="E se não me convencer?",
        a_q6="Tem 60 dias para devolver e receber o reembolso completo. Sem perguntas, sem complicações.",
        bt1="💶 Pagamento à cobrança", bt2="🚚 Envio 24/48 h", bt3="↩️ Devolução 60 dias",
        foot_blurb="Produtos úteis para o dia a dia, entrega em 24–48 horas com pagamento à cobrança.",
        foot_info="Informação", foot_contact="Contacto",
        about="Sobre nós", contact="Contacte-nos",
        privacy="Política de Privacidade", terms="Termos e Condições",
        cookies="Política de Cookies", ship="Política de envio", refund="Política de reembolso",
        rights="Todos os direitos reservados",
    ),
    "sk": dict(
        title="ClimaAir™ 4in1 — Stĺpová klimatizácia bez vonkajšej jednotky | -50%",
        description="ClimaAir™ 4in1: chladí, kúri, odvlhčuje a čistí vzduch bez vonkajšej jednotky a bez technika. 18.000 BTU, 120 m², platba na dobierku na Slovensku.",
        submitting="Odosielanie...",
        cookie_text="Používame technické a cookies tretích strán na zlepšenie vášho zážitku a na analytiku.",
        cookie_accept="Prijať",
        cookie_learn="Zistiť viac",
        topbar="❄️ Platba na dobierku · Doručenie 24/48 h",
        h1="ClimaAir™ 4in1: ochladí, vykúri, odvlhčí a vyčistí vzduch v celom dome za iba <span class=\"hl\">7 minút</span>, bez vonkajšej jednotky a bez volania technika!",
        lead="Postavíte ho na zem a zapojíte do bežnej zásuvky: chladí, kúri, ničí zárodky a baktérie a odvlhčuje vzduch — všetko v jednom prístroji. Vďaka internému systému <strong>FlowCore®</strong> ušetríte každý mesiac až <strong>87 %</strong> na účtoch za energie!",
        alt_hero="ClimaAir prenosná stĺpová klimatizácia 4 v 1",
        stock_pill="🔥 Za túto cenu ostáva len <strong>7 kusov</strong>",
        b1_t="120 m² ochladených za 5 minút.",
        b1_d="Z spálne do obývačky: presuniete ho na kolieskach a miestnosť zmení teplotu skôr, než sa stihnete pripraviť na noc.",
        b2_t="Ticho 18 dB — tichšie ako šepot.",
        b2_d="Zaspete a ani neviete, že beží: navrhnuté špeciálne do spálne.",
        b3_t="Žiadne diery v stene, žiadna vonkajšia jednotka, žiadny technik.",
        b3_d="Vyberiete ho z krabice, postavíte na zem, zapojíte šnúru a za 5 minút je pripravený.",
        b4_t="Spotreba len 0,18€ denne.",
        b4_d="Inteligentná technológia znižuje spotrebu na minimum: žiadne nepríjemné prekvapenia na účte.",
        b5_t="4 funkcie v 1, ovládanie z telefónu.",
        b5_d="Chladí, kúri, odvlhčuje a čistí: všetko nastavíte, aniž by ste vstali z postele.",
        cta_hero="Áno, chcem spať v chládku: objednávam teraz",
        secure="Bezpečný nákup • Expresné doručenie • Kompletná záruka",
        t1_h="Rýchle doručenie", t1_p="Balík dorazí k vám domov do 24–48 hodín.",
        t2_h="Platíte pri prevzatí", t2_p="Žiadna platba vopred: zaplatíte, až keď balík dostanete",
        t3_h="Nákup pod ochranou", t3_p="Vaše osobné údaje sú 100% chránené",
        t4_h="Záruka 2 roky", t4_p="Môžete ho vrátiť bez starostí do 60 dní",
        pieces="OSTÁVA LEN 7 KUSOV",
        warn_h="Dôležité! Sklad sa rýchlo vyprázdňuje!",
        warn_p="Práve teraz má na tento produkt spústa ďalších zákazníkov oči. Preto dostupné kusy miznú tak rýchlo. Objednajte hneď a zabezpečte si jeden z posledných kusov za dnešnú zľavovú cenu.",
        countdown="⏰ Ponuka -50 % platí len dnes",
        hours="Hod", mins="Min", secs="Sek",
        stock_l="Ešte dostupné kusy", stock_r="Ostáva len pár kusov!",
        live="<strong>{n} ľudí</strong> práve sleduje ClimaAir",
        live0="<strong>41 ľudí</strong> práve sleduje ClimaAir",
        form_h="Vyplňte objednávkový formulár",
        form_p="Budeme vás kontaktovať kvôli potvrdeniu detailov doručenia.",
        lab_name="Meno a priezvisko*", lab_tel="Telefón*", lab_addr="Doručovacia adresa*",
        ph_name="Ján Novák", ph_tel="+421 901 123 456", ph_addr="Ulica 10, 811 01 Bratislava",
        buy="KÚPIŤ TERAZ",
        form_note="🔒 Bez zálohy · Platíte až pri doručení · Doprava 24/48 h",
        benefits_ey="✅ Skutočné výhody",
        benefits_h="Žiadna inštalácia, žiadna vonkajšia jednotka, žiadny technik. Postavíte ho na zem, zapojíte šnúru a hotovo.",
        w1_ey="01 — Technológia FlowCore®",
        w1_h="FlowCore® nahrádza kompresor a chladiace plyny",
        w1_t1="⏱️ Pripravené za 90 sekúnd", w1_t2="👉 Na kolieskach",
        w1_p="FlowCore® je vysoko účinný interný systém, ktorý nahrádza tradičný kompresor a chladivá. Funguje zapojený do domácej zásuvky: stojí voľne na zemi, bez kotvenia do steny a bez vonkajšej jednotky.",
        w1_i="Spustí sa do 90 sekúnd a nastavenej teploty dosiahne zhruba za 5 minút. Na kolieskach ho presuniete z izby do izby za desať sekúnd: spálňa, obývačka, kancelária — stále ten istý prístroj. Bez ponúk, bez remeselníkov, bez čakania týždne.",
        w2_ey="02 — 4 funkcie, jeden prístroj",
        w2_h="Chladí, kúri, odvlhčuje a čistí",
        w2_t1="16°C – 40°C", w2_t2="99 % zárodkov",
        w2_p="ClimaAir™ chladí, kúri, čistí vzduch trojitým filtrom a automaticky odvlhčuje. Chladí až na <strong>16°C</strong>, kúri až na <strong>40°C</strong>, odstráni až <strong>99 %</strong> zárodkov a baktérií zo vzduchu.",
        w2_i="Už nemusíte kupovať zvlášť odvlhčovač, čističku a ohrievač. Ušetríte miesto v byte aj stovky eur za ďalšie nákupy.",
        w3_ey="03 — Minimálna spotreba, maximálna úspora",
        w3_h="Energetická trieda A+++ a nižšie účty",
        w3_t1="0,12€ / hod", w3_t2="Až -80 %",
        w3_p="Vďaka triede A+++ ClimaAir™ automaticky ladí výkon a prúdenie podľa teploty v miestnosti. Spotreba od <strong>0,12€ za hodinu</strong>, až o <strong>80 % menej</strong> ako pri klasickej klimatizácii s vonkajšou jednotkou.",
        w3_i="Môžete ho nechať bežať celú noc, každý deň, bez toho, aby ste na konci mesiaca s obavami pozerali na účet.",
        cta_mid="Objednajte ClimaAir™ teraz ↓",
        mid1="💵 Platba na dobierku", mid2="🚚 Doručenie 24/48 h", mid3="↩️ 60 dní na vyskúšanie",
        cmp_ey="⚖️ Porovnanie",
        cmp_h="Prečo ClimaAir poráža klasickú klimatizáciu",
        cmp_sub="Rovnaký chladný vzduch, žiadna práca naviac.",
        cmp_trad="Klasická klimatizácia",
        r1c="Inštalácia", r1a="Technik + vonkajšia jednotka", r1b="✅ Žiadna: postavíte na zem a zapojíte",
        r2c="Čas", r2a="Dni alebo týždne", r2b="✅ Pripravené za 5 minút",
        r3c="Cena inštalácie", r3a="400-800€", r3b="✅ 0€",
        r4c="Nočný hluk", r4a="35–45 dB, často ruší", r4b="✅ 18 dB, skoro nepočuteľné",
        r5c="Funkcie", r5a="Len chladí", r5b="✅ Chladí, kúri, odvlhčuje, čistí",
        r6c="Môžete ho premiestniť?", r6a="Nie: ostane tam, kde ho namontovali", r6b="✅ Áno: je na kolieskach, odveziete ho kamkoľvek",
        cta_price="Áno, chcem ClimaAir za {now} →",
        rev_ey="⭐ Kto ho používa každý deň",
        rev_h="Čo hovoria rodiny, ktoré ho už vyskúšali",
        rev_sub="★★★★★ 4,8/5 z viac ako 1 824 overených recenzií",
        rev1="„Bola som skeptická, myslela som, že je to ďalší gadget, ktorý skončí v pivnici. Namiesto toho ho používam každý deň od júna: v spálni večer je perfektný a s časovačom sa sám vypne. Jediná vada: diaľkový ovládač, občas ho stratím v perinách ahah“",
        a1="Jana T., Bratislava ✅ — Overený nákup",
        rev2="„Kúpili sme ho do pracovne manžela, ktorý pracuje z domu. V zime ho ráno zapne a za pár sekúnd je teplo. Januárový účet bol nižší, než sme čakali — a to bol ten pravý dôvod, prečo ho odporúčame.“",
        a2="Dávid P., Košice ✅ — Overený nákup",
        rev3="„Bývam v nájme a nemohla som nainštalovať poriadnu klimatizáciu. S ClimaAir™ som to vyriešila za popoludnie: žiadna diera, žiadne povolenie od majiteľa. V lete ho mám v spálni, v zime v obývačke. V tichom nočnom režime ho skoro nepočujem.“",
        a3="Sara M., Žilina ✅ — Overený nákup",
        kit_ey="📦 Čo je v balení",
        kit_h="Všetko v krabici.<br>Žiadne ďalšie nákupy. Žiadne prekvapenia.",
        kit_p="Otvoríte krabicu, postavíte ho na zem, zapojíte šnúru a za 5 minút je v miestnosti chladno. A to je všetko.",
        k1="1× prenosná stĺpová klimatizácia ClimaAir 18.000 BTU",
        k2="4× otočné kolieska už namontované na základni",
        k3="1× diaľkový ovládač v balení",
        k4="1× návod na použitie v slovenčine",
        k5="Prístup k aplikácii na ovládanie z telefónu",
        k6="Doprava zadarmo do 24–48 h",
        k7="Predĺžená záruka 2 roky",
        faq_ey="❓ Časté otázky",
        faq_h="Máte pochybnosti? To je v poriadku.<br>Vyjasníme ich tu.",
        faq_lead="Než objednáte, nájdite odpovede na najčastejšie otázky o hluku, inštalácii, platbe a záruke.",
        q1="Je v noci hlučný?",
        a_q1="Nie: v nočnom režime klesne na 18 dB, tichšie ako šepot. Je navrhnutý práve do spálne.",
        q2="Musím ho inštalovať alebo volať technika?",
        a_q2="Nie. ClimaAir sa nepripevňuje na stenu a nemá vonkajšiu jednotku: postavíte ho na zem, zapojíte šnúru a za 5 minút funguje. Keď chcete zmeniť miestnosť, odstrčíte ho na kolieskach.",
        q3="Naozaj pokryje 120 m²?",
        a_q3="Áno, vďaka výkonu 18.000 BTU. Pri veľmi veľkých priestoroch ho nechajte v hlavnej miestnosti a nechajte dvere otvorené, aby sa vzduch rozložil.",
        q4="Vie len chladiť, alebo aj kúriť?",
        a_q4="Oboje. V lete chladí, v zime kúri a navyše odvlhčuje a čistí vzduch: jeden prístroj na celý rok.",
        q5="Ako funguje platba?",
        a_q5="Zaplatíte v hotovosti kuriérovi, keď balík dorazí domov. Žiadna platba vopred, žiadna karta.",
        q6="A keď ma to nepresvedčí?",
        a_q6="Máte 60 dní na vrátenie a plnú náhradu. Bez otázok, bez komplikácií.",
        bt1="💶 Platba na dobierku", bt2="🚚 Doručenie 24/48 h", bt3="↩️ Vrátenie 60 dní",
        foot_blurb="Užitočné produkty pre každodenný život, doručenie do 24–48 hodín s platbou na dobierku.",
        foot_info="Informácie", foot_contact="Kontaktovať",
        about="O nás", contact="Kontaktujte nás",
        privacy="Zásady ochrany osobných údajov", terms="Zmluvné podmienky",
        cookies="Zásady používania súborov cookie", ship="Pravidlá prepravy", refund="Pravidlá vrátenia peňazí",
        rights="Všetky práva vyhradené",
    ),
    "hu": dict(
        title="ClimaAir™ 4in1 — Oszlopklíma külső egység nélkül | -50%",
        description="ClimaAir™ 4in1: hűt, fűt, párátlanít és tisztítja a levegőt külső egység és szerelő nélkül. 18.000 BTU, 120 m², utánvét Magyarországon.",
        submitting="Küldés...",
        cookie_text="Technikai és harmadik féltől származó cookie-kat használunk a élmény javítására és elemzésre.",
        cookie_accept="Elfogadom",
        cookie_learn="Tudjon meg többet",
        topbar="❄️ Utánvét · Szállítás 24/48 óra",
        h1="ClimaAir™ 4in1: lehűti, felfűti, párátlanítja és megtisztítja az egész otthon levegőjét mindössze <span class=\"hl\">7 perc</span> alatt, külső egység és szerelőhívás nélkül!",
        lead="A földre állítja és bedugja a sima konnektorba: hűt, fűt, elpusztítja a kórokozókat és baktériumokat, és párátlanít — minden egyetlen készülékkel. A belső <strong>FlowCore®</strong> rendszernek köszönhetően havonta akár <strong>87%-ot</strong> spórol a számlán!",
        alt_hero="ClimaAir hordozható oszlopklíma 4 az 1-ben",
        stock_pill="🔥 Ezen az áron már csak <strong>7 darab</strong> maradt",
        b1_t="120 m² lehűtve 5 perc alatt.",
        b1_d="A hálószobától a nappaliig: kerekeken tolja, és a szoba hőmérséklete megváltozik, mielőtt felkészülne az éjszakára.",
        b2_t="18 dB csend — halkabb egy suttogásnál.",
        b2_d="Elalszik, és észre sem veszi, hogy be van kapcsolva: kifejezetten hálószobába tervezték.",
        b3_t="Nulla lyuk a falban, nulla külső egység, semmilyen szerelő.",
        b3_d="Kiveszi a dobozból, a földre állítja, bedugja, és 5 perc múlva kész.",
        b4_t="Napi fogyasztása csak 70 Ft.",
        b4_d="Intelligens technológia, ami a fogyasztást a minimumra csökkenti: semmi kellemetlen meglepetés a számlán.",
        b5_t="4 funkció 1-ben, vezérlés telefonról.",
        b5_d="Hűt, fűt, párátlanít és tisztít: mindent az ágyból állít.",
        cta_hero="Igen, hűvösen akarok aludni: most rendelek",
        secure="Biztonságos vásárlás • Expressz szállítás • Teljes garancia",
        t1_h="Gyors szállítás", t1_p="A csomag 24–48 órán belül megérkezik otthonába.",
        t2_h="Átvételkor fizet", t2_p="Nincs előzetes terhelés: csak a csomag átvételekor fizet",
        t3_h="Védett vásárlás", t3_p="Személyes adatai 100%-ban védettek",
        t4_h="2 év garancia", t4_p="60 napon belül gond nélkül visszaküldheti",
        pieces="MÁR CSAK 7 DARAB MARADT",
        warn_h="Fontos! A raktár gyorsan ürül!",
        warn_p="Éppen most sok más vásárló is ezt a terméket nézi: ezért fogynak ilyen gyorsan a darabok. Vásároljon azonnal, és biztosítson be egyet az utolsó darabok közül a mai akciós áron.",
        countdown="⏰ A -50% ajánlat csak ma él",
        hours="Óra", mins="Perc", secs="Mp",
        stock_l="Még elérhető darabok", stock_r="Már csak kevés darab maradt!",
        live="<strong>{n} ember</strong> nézi most a ClimaAirt",
        live0="<strong>41 ember</strong> nézi most a ClimaAirt",
        form_h="Töltse ki a rendelési űrlapot",
        form_p="Felvesszük Önnel a kapcsolatot a szállítási adatok megerősítéséhez.",
        lab_name="Teljes név*", lab_tel="Telefon*", lab_addr="Szállítási cím*",
        ph_name="Kovács János", ph_tel="+36 30 123 4567", ph_addr="Fő utca 10, 1051 Budapest",
        buy="MEGRENDELEM MOST",
        form_note="🔒 Nincs előleg · Fizetés átvételkor · Szállítás 24/48 óra",
        benefits_ey="✅ Valódi előnyök",
        benefits_h="Nincs telepítés, nincs külső egység, nincs szerelő. A földre állítja, bedugja, kész.",
        w1_ey="01 — FlowCore® technológia",
        w1_h="A FlowCore® kiváltja a kompresszort és a hűtőgázokat",
        w1_t1="⏱️ 90 másodperc alatt kész", w1_t2="👉 Kerekeken",
        w1_p="A FlowCore® nagy hatékonyságú belső rendszer, amely kiváltja a hagyományos kompresszort és hűtőközegeket. Otthoni konnektorról működik: magától áll a földön, falra rögzítés és külső egység nélkül.",
        w1_i="90 másodpercen belül elindul, és a beállított hőmérsékletet kb. 5 perc alatt eléri. Kerekeken tíz másodperc alatt viszi egyik szobából a másikba: háló, nappali, iroda, mindig ugyanaz a készülék. Ajánlatkérés, szakember és hetek várakozás nélkül.",
        w2_ey="02 — 4 funkció, egyetlen készülék",
        w2_h="Hűt, fűt, párátlanít és tisztít",
        w2_t1="16°C – 40°C", w2_t2="99% kórokozó",
        w2_p="A ClimaAir™ hűt, fűt, hármas szűrővel tisztítja a levegőt és automatikusan párátlanít. Akár <strong>16°C-ra</strong> hűt, <strong>40°C-ig</strong> fűt, a levegőben lévő kórokozók és baktériumok akár <strong>99%-át</strong> eltávolítja.",
        w2_i="Nem kell külön párátlanítót, légtisztítót és fűtőt vennie. Helyet spórol otthon, és több tízezer forintot a plusz vásárlásokon.",
        w3_ey="03 — Minimális fogyasztás, maximális megtakarítás",
        w3_h="A+++ energiaosztály és könnyebb számlák",
        w3_t1="50 Ft / óra", w3_t2="Akár -80%",
        w3_p="Az A+++ osztálynak köszönhetően a ClimaAir™ automatikusan hangolja a teljesítményt és a légáramot a szoba hőmérsékletéhez. Fogyasztás <strong>50 Ft/órától</strong>, akár <strong>80%-kal kevesebb</strong>, mint egy hagyományos, külső egységes klímánál.",
        w3_i="Egész éjjel, minden nap bekapcsolva hagyhatja, anélkül, hogy a hónap végén izgulna a számla miatt.",
        cta_mid="Rendelje meg most a ClimaAir™-t ↓",
        mid1="💵 Utánvét", mid2="🚚 Szállítás 24/48 óra", mid3="↩️ 60 napos próba",
        cmp_ey="⚖️ Összehasonlítás",
        cmp_h="Miért veri a ClimaAir a hagyományos klímát",
        cmp_sub="Ugyanaz a hűvös levegő, semmi munka.",
        cmp_trad="Hagyományos klíma",
        r1c="Telepítés", r1a="Szerelő + külső egység", r1b="✅ Semmi: földre állítja és bedugja",
        r2c="Idő", r2a="Napok vagy hetek", r2b="✅ 5 perc alatt kész",
        r3c="Telepítési költség", r3a="160 000–320 000 Ft", r3b="✅ 0 Ft",
        r4c="Éjszakai zaj", r4a="35–45 dB, gyakran zavar", r4b="✅ 18 dB, szinte észrevehetetlen",
        r5c="Funkciók", r5a="Csak hűt", r5b="✅ Hűt, fűt, párátlanít, tisztít",
        r6c="Átvihető?", r6a="Nem: ott marad, ahová felszerelték", r6b="✅ Igen: kerekeken bármelyik szobába viszi",
        cta_price="Igen, kérem a ClimaAirt {now} →",
        rev_ey="⭐ Aki minden nap használja",
        rev_h="Mit mondanak a családok, akik már kipróbálták",
        rev_sub="★★★★★ 4,8/5 több mint 1 824 ellenőrzött értékelés alapján",
        rev1="„Szkeptikus voltam, azt hittem, megint egy kütyü, ami a pincében landol. Ehelyett június óta minden nap használom: a hálóban este tökéletes, és az időzítővel magától kikapcsol. Egyetlen baj: a távirányító, néha elveszítem a paplan között ahah”",
        a1="Júlia T., Budapest ✅ — Ellenőrzött vásárlás",
        rev2="„A férjem home office-ához vettük. Télen reggel bekapcsolja, és másodpercek alatt meleg van. A januári számla alacsonyabb lett a vártnál — ez volt az igazi ok, hogy ajánljuk.”",
        a2="Dávid P., Debrecen ✅ — Ellenőrzött vásárlás",
        rev3="„Albérletben lakom, és nem szerelhettem fel igazi klímát. A ClimaAir™-rel egy délután alatt megoldottam: sem lyuk, sem engedély a tulajtól. Nyáron a hálóban van, télen a nappaliban. Éjjel csendes módban szinte nem hallom.”",
        a3="Sara M., Szeged ✅ — Ellenőrzött vásárlás",
        kit_ey="📦 Mi van a csomagban",
        kit_h="Minden a dobozban.<br>Semmi extra vásárlás. Semmi meglepetés.",
        kit_p="Kinyitja a dobozt, a földre állítja, bedugja, és 5 perc múlva a szoba már hűvös. Ennyi.",
        k1="1× hordozható oszlopklíma ClimaAir 18.000 BTU",
        k2="4× már a talpra szerelt guruló kerék",
        k3="1× távirányító a csomagban",
        k4="1× magyar használati útmutató",
        k5="Hozzáférés az apphoz okostelefonos vezérléshez",
        k6="Ingyenes szállítás 24–48 óra",
        k7="2 év meghosszabbított garancia",
        faq_ey="❓ Gyakori kérdések",
        faq_h="Kétségei vannak? Ez természetes.<br>Itt tisztázzuk.",
        faq_lead="Rendelés előtt találja meg a zajra, telepítésre, fizetésre és garanciára vonatkozó válaszokat.",
        q1="Zajos éjszaka?",
        a_q1="Nem: éjszakai módban 18 dB-re csökken, halkabb egy suttogásnál. Pont hálószobába tervezték.",
        q2="Telepítenem kell, vagy szerelőt hívni?",
        a_q2="Nem. A ClimaAir nem a falra kerül, és nincs külső egysége: a földre állítja, bedugja, és 5 perc múlva működik. Ha szobát váltana, kerekeken tolja.",
        q3="Tényleg 120 m²-t fed?",
        a_q3="Igen, a 18.000 BTU teljesítménynek köszönhetően. Nagyon nagy terekben a fő szobában tartsa, és nyissa ki az ajtókat, hogy a levegő szétoszoljon.",
        q4="Csak hűt, vagy fűt is?",
        a_q4="Mindkettő. Nyáron hűt, télen fűt, plusz párátlanít és tisztít: egy készülék egész évre.",
        q5="Hogyan működik a fizetés?",
        a_q5="Készpénzzel fizet a futárnak, amikor a csomag megérkezik. Nincs előre fizetés, nincs kártya.",
        q6="És ha nem győz meg?",
        a_q6="60 napja van visszaküldeni, és teljes visszatérítést kap. Kérdés nélkül, bonyodalom nélkül.",
        bt1="💶 Utánvét", bt2="🚚 Szállítás 24/48 óra", bt3="↩️ 60 napos visszaküldés",
        foot_blurb="Hasznos termékek a mindennapokra, szállítás 24–48 óra alatt utánvéttel.",
        foot_info="Információ", foot_contact="Elérhetőségek",
        about="Rólunk", contact="Kapcsolat",
        privacy="Adatvédelmi irányelvek", terms="Általános szerződési feltételek",
        cookies="Cookie szabályzat", ship="Szállítási feltételek", refund="Visszatérítési szabályzat",
        rights="Minden jog fenntartva",
    ),
    "lv": dict(
        title="ClimaAir™ 4in1 — Kolonnas gaisa kondicionieris bez āra bloka | -50%",
        description="ClimaAir™ 4in1: dzesē, silda, sausina un attīra gaisu bez āra bloka un bez tehniķa. 18.000 BTU, 120 m², maksa pēc saņemšanas Latvijā.",
        submitting="Nosūta...",
        cookie_text="Mēs izmantojam tehniskās un trešo pušu sīkdatnes, lai uzlabotu jūsu pieredzi un analītikai.",
        cookie_accept="Pieņemt",
        cookie_learn="Uzzināt vairāk",
        topbar="❄️ Maksa pēc saņemšanas · Piegāde 24/48 h",
        h1="ClimaAir™ 4in1: atdzesē, sasilda, nosusina un attīra gaisu visā mājā tikai <span class=\"hl\">7 minūtēs</span>, bez āra bloka un bez tehniķa izsaukuma!",
        lead="Noliek uz grīdas un iesprauž parastā rozetē: dzesē, silda, iznīcina mikrobus un baktērijas un sausina gaisu — viss vienā ierīcē. Pateicoties iekšējam <strong>FlowCore®</strong> sistēmai, katru mēnesi ietaupāt līdz <strong>87%</strong> rēķinā!",
        alt_hero="ClimaAir pārnēsājams kolonnas klimatizators 4 vienā",
        stock_pill="🔥 Šajā cenā palikušas tikai <strong>7 vienības</strong>",
        b1_t="120 m² atdzesēti 5 minūtēs.",
        b1_d="No guļamistabas uz dzīvojamo istabu: pārvietojat uz riteņiem, un telpa maina temperatūru, pirms paspējat sagatavoties naktij.",
        b2_t="Klusums 18 dB — klusāks par čukstu.",
        b2_d="Aizmigstat un pat nepamanāt, ka tas ir ieslēgts: radīts tieši guļamistabai.",
        b3_t="Nulle caurumu sienā, nulle āra bloka, neviens tehniķis.",
        b3_d="Izņemat no kastes, noliekat uz grīdas, iespraužat un pēc 5 minūtēm ir gatavs.",
        b4_t="Patērē tikai 0,18€ dienā.",
        b4_d="Vieda tehnoloģija, kas samazina patēriņu līdz minimumam: nekādi negaidīti rēķini.",
        b5_t="4 funkcijas 1, vadība no tālruņa.",
        b5_d="Dzesē, silda, sausina un attīra: visu regulējat, neizkāpjot no gultas.",
        cta_hero="Jā, gribu gulēt vēsumā: pasūtu tagad",
        secure="Drošs pirkums • Ātrā piegāde • Pilna garantija",
        t1_h="Ātra piegāde", t1_p="Paciņa nonāk pie jums mājās 24–48 stundās.",
        t2_h="Maksājat saņemot", t2_p="Nav avansa: maksājat tikai, kad saņemat sūtījumu",
        t3_h="Aizsargāts pirkums", t3_p="Jūsu personas dati ir 100% aizsargāti",
        t4_h="2 gadu garantija", t4_p="Varat to atdot bez raizēm 60 dienu laikā",
        pieces="PALIKUŠAS TIKAI 7 VIENĪBAS",
        warn_h="Svarīgi! Noliktava ātri tukšojas!",
        warn_p="Tieši tagad daudzi citi klienti skatās uz šo produktu: tāpēc pieejamās vienības samazinās tik ātri. Pērciet tūlīt un nodrošiniet vienu no pēdējām vienībām par šodienas akcijas cenu.",
        countdown="⏰ Piedāvājums -50% spēkā tikai šodien",
        hours="St", mins="Min", secs="Sek",
        stock_l="Vēl pieejamās vienības", stock_r="Palikušas tikai dažas vienības!",
        live="<strong>{n} cilvēki</strong> tagad skatās ClimaAir",
        live0="<strong>41 cilvēki</strong> tagad skatās ClimaAir",
        form_h="Aizpildiet pasūtījuma veidlapu",
        form_p="Sazināsimies, lai apstiprinātu piegādes datus.",
        lab_name="Vārds un uzvārds*", lab_tel="Tālrunis*", lab_addr="Piegādes adrese*",
        ph_name="Jānis Bērziņš", ph_tel="+371 21 234 567", ph_addr="Brīvības iela 10, LV-1010 Rīga",
        buy="PIRKT TAGAD",
        form_note="🔒 Bez avansa · Maksājat saņemot · Piegāde 24/48 h",
        benefits_ey="✅ Īstie ieguvumi",
        benefits_h="Nekāda uzstādīšana, nekāds āra bloks, nekāds tehniķis. Noliekat uz grīdas, iespraužat un gatavs.",
        w1_ey="01 — FlowCore® tehnoloģija",
        w1_h="FlowCore® aizstāj kompresoru un aukstumaģentus",
        w1_t1="⏱️ Gatavs 90 sekundēs", w1_t2="👉 Uz riteņiem",
        w1_p="FlowCore® ir iekšēja augstas efektivitātes sistēma, kas aizstāj tradicionālo kompresoru un aukstumaģentus. Darbojas, iesprausta mājas rozetē: stāv pats uz grīdas, bez stiprinājumiem pie sienas un bez āra bloka.",
        w1_i="Ieslēdzas mazāk nekā 90 sekundēs un sasniedz temperatūru aptuveni 5 minūtēs. Ar riteņiem pārvietojat no istabas uz istabu desmit sekundēs: guļamistaba, dzīvojamā, birojs — vienmēr tā pati ierīce. Bez tāmes, bez strādniekiem, bez gaidīšanas nedēļām.",
        w2_ey="02 — 4 funkcijas, viena ierīce",
        w2_h="Dzesē, silda, sausina un attīra",
        w2_t1="16°C – 40°C", w2_t2="99% mikrobu",
        w2_p="ClimaAir™ dzesē, silda, attīra gaisu ar trīskāršu filtru un automātiski sausina. Dzesē līdz <strong>16°C</strong>, silda līdz <strong>40°C</strong>, noņem līdz <strong>99%</strong> mikrobu un baktēriju no gaisa.",
        w2_i="Vairs nav jāpērk atsevišķi mitruma savācējs, gaisa attīrītājs un sildītājs. Ietaupāt vietu mājās un simtiem eiro papildu pirkumos.",
        w3_ey="03 — Minimāls patēriņš, maksimāls ietaupījums",
        w3_h="Energijas klase A+++ un vieglāki rēķini",
        w3_t1="0,12€ / stundā", w3_t2="Līdz -80%",
        w3_p="Pateicoties A+++ klasei, ClimaAir™ automātiski pielāgo jaudu un gaisa plūsmu telpas temperatūrai. Patēriņš no <strong>0,12€ stundā</strong>, līdz <strong>80% mazāk</strong> nekā tradicionālam kondicionierim ar āra bloku.",
        w3_i="Varat to atstāt ieslēgtu visu nakti, katru dienu, neskatoties uz rēķinu ar satraukumu mēneša beigās.",
        cta_mid="Pasūtiet savu ClimaAir™ tagad ↓",
        mid1="💵 Maksa pēc saņemšanas", mid2="🚚 Piegāde 24/48 h", mid3="↩️ 60 dienu izmēģinājums",
        cmp_ey="⚖️ Salīdzinājums",
        cmp_h="Kāpēc ClimaAir pārspēj tradicionālo kondicionieri",
        cmp_sub="Tas pats vēsais gaiss, nekāds darbs.",
        cmp_trad="Tradicionālais kondicionieris",
        r1c="Uzstādīšana", r1a="Tehniķis + āra bloks", r1b="✅ Nekāda: noliekat uz grīdas un iespraužat",
        r2c="Laiks", r2a="Dienas vai nedēļas", r2b="✅ Gatavs 5 minūtēs",
        r3c="Uzstādīšanas izmaksas", r3a="400-800€", r3b="✅ 0€",
        r4c="Nakts troksnis", r4a="35-45 dB, bieži traucē", r4b="✅ 18 dB, gandrīz nemanāms",
        r5c="Funkcijas", r5a="Tikai dzesē", r5b="✅ Dzesē, silda, sausina, attīra",
        r6c="Vai var pārvietot?", r6a="Nē: paliek pie sienas, kur to uzmontēja", r6b="✅ Jā: ir uz riteņiem, aizvedat uz jebkuru istabu",
        cta_price="Jā, gribu ClimaAir par {now} →",
        rev_ey="⭐ Kas to lieto katru dienu",
        rev_h="Ko saka ģimenes, kas jau ir izmēģinājušas",
        rev_sub="★★★★★ 4,8/5 no vairāk nekā 1 824 pārbaudītām atsauksmēm",
        rev1="«Biju skeptiska, domāju, ka tas ir kārtējais sīkrīks, kas nonāks pagrabā. Tā vietā lietoju katru dienu kopš jūnija: guļamistabā vakarā ir ideāli, un ar taimeri pats izslēdzas. Vienīgais mīnuss: pults, reizēm pazaudēju starp palagiem ahah»",
        a1="Jūlija T., Rīga ✅ — Pārbaudīts pirkums",
        rev2="«Nopirkām vīra kabinetam, viņš strādā no mājām. Ziemā no rīta ieslēdz, un pēc dažām sekundēm jau ir silts. Janvāra rēķins bija zemāks, nekā gaidījām — tas bija īstais iemesls to ieteikt.»",
        a2="Dāvids P., Liepāja ✅ — Pārbaudīts pirkums",
        rev3="«Dzīvoju īrētā dzīvoklī un nevarēju uzstādīt īstu kondicionieri. Ar ClimaAir™ atrisināju pēcpusdienā: ne cauruma, ne atļaujas no saimnieka. Vasarā tas ir guļamistabā, ziemā dzīvojamajā. Naktī klusajā režīmā gandrīz nedzirdu.»",
        a3="Sara M., Daugavpils ✅ — Pārbaudīts pirkums",
        kit_ey="📦 Kas ir paciņā",
        kit_h="Viss kastē.<br>Nulle papildu pirkumu. Nulle pārsteigumu.",
        kit_p="Atverat kasti, noliekat uz grīdas, iespraužat, un pēc 5 minūtēm telpa jau ir vēsa. Un tas arī viss.",
        k1="1× pārnēsājams kolonnas klimatizators ClimaAir 18.000 BTU",
        k2="4× grozāmi riteņi jau uzstādīti uz pamatnes",
        k3="1× tālvadības pults komplektā",
        k4="1× lietošanas instrukcija latviešu valodā",
        k5="Piekļuve lietotnei vadībai no viedtālruņa",
        k6="Bezmaksas piegāde 24–48 h",
        k7="Pagarināta 2 gadu garantija",
        faq_ey="❓ Biežākie jautājumi",
        faq_h="Ir šaubas? Tas ir normāli.<br>Noskaidrosim šeit.",
        faq_lead="Pirms pasūtīšanas atrodiet atbildes par troksni, uzstādīšanu, maksājumu un garantiju.",
        q1="Vai naktī ir skaļš?",
        a_q1="Nē: nakts režīmā nokrītas līdz 18 dB, klusāks par čukstu. Radīts tieši guļamistabai.",
        q2="Vai jāuzstāda vai jāizsauc tehniķis?",
        a_q2="Nē. ClimaAir nav jāstiprina pie sienas un tam nav āra bloka: noliekat uz grīdas, iespraužat, un pēc 5 minūtēm tas darbojas. Ja gribat mainīt istabu, palīdzat uz riteņiem.",
        q3="Vai tiešām nosedz 120 m²?",
        a_q3="Jā, pateicoties 18.000 BTU jaudai. Ļoti lielās telpās turiet to galvenajā istabā un atstājiet durvis vaļā, lai gaiss izplatītos.",
        q4="Tikai dzesē vai arī silda?",
        a_q4="Abi. Vasarā dzesē, ziemā silda, plus sausina un attīra: viena ierīce visam gadam.",
        q5="Kā darbojas maksājums?",
        a_q5="Maksājat skaidrā naudā kurjeram, kad sūtījums nonāk mājās. Nav avansa, nav kartes.",
        q6="Un ja nepārliecina?",
        a_q6="Jums ir 60 dienas, lai atdotu un saņemtu pilnu atmaksu. Bez jautājumiem, bez sarežģījumiem.",
        bt1="💶 Maksa pēc saņemšanas", bt2="🚚 Piegāde 24/48 h", bt3="↩️ Atgriešana 60 dienas",
        foot_blurb="Noderīgi produkti ikdienai, piegāde 24–48 stundu laikā ar maksu pēc saņemšanas.",
        foot_info="Informācija", foot_contact="Kontakti",
        about="Par mums", contact="Sazinieties ar mums",
        privacy="Privātuma politika", terms="Noteikumi un nosacījumi",
        cookies="Sīkdatņu politika", ship="Piegādes politika", refund="Atmaksas politika",
        rights="Visas tiesības aizsargātas",
    ),
}


INDEX_TMPL = """<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<title>Redirect…</title>
<script>
(function () {{
  var path = '/{geo}/climaair/landing.html';
  window.location.replace(path + window.location.search + window.location.hash);
}})();
</script>
<meta http-equiv="refresh" content="0;url=/{geo}/climaair/landing.html">
<link rel="canonical" href="https://gadgetspothub.com/{geo}/climaair/landing.html">
</head>
<body>
<p><a href="/{geo}/climaair/landing.html">ClimaAir™</a></p>
</body>
</html>
"""


def landing_html(geo: str, g: dict, t: dict) -> str:
    d = {**t, **g, "geo": geo, "uid": UID, "webhook": WEBHOOK}
    d["cta_price"] = t["cta_price"].format(now=g["now"])
    # live strings already contain {n} for JS — leave as-is
    return LANDING_TMPL.format_map(d)


LANDING_TMPL = r"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=AW-18358316754"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());

  gtag('config', 'AW-18358316754');
</script>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{description}">
<meta name="contact" content="info@gadgetspothub.com">
<meta name="theme-color" content="#0055ff">
<link rel="canonical" href="https://gadgetspothub.com/{geo}/climaair/landing.html">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/climaair-landing.css">
<script>
window.SITE_CONFIG = {{
  GEO: '{geo}',
  PRODUCT_SLUG: 'climaair',
  CURRENCY: '{currency}',
  PRICE: {price_num},
  OFFER_NAME: 'ClimaAir Colonna {offer}',
  LP_ID: '{geo}-{offer}',
  FORM_ENDPOINT: 'https://TODO-network-endpoint.com/api/lead',
  SUBMITTING_LABEL: '{submitting}',
  COOKIE_TEXT: '{cookie_text}',
  COOKIE_ACCEPT: '{cookie_accept}',
  COOKIE_LEARN: '{cookie_learn}'
}};
</script>
<script src="/assets/js/tracking.js" defer></script>
</head>
<body>

<div class="topbar">{topbar}</div>

<section class="hero wrap">
  <div class="hero-copy">
    <span class="gift-strip">{topbar}</span>
    <h1>{h1}</h1>
    <p class="lead">{lead}</p>
    <div class="hero-image hero-image-mobile-only">
      <img decoding="async" src="/assets/img/products/climaair/hero.webp" alt="{alt_hero}" width="900" height="900" loading="eager" fetchpriority="high">
    </div>
    <div class="price-block">
      <span class="was">{was}</span>
      <span class="now">{now}</span>
      <span class="pct">-50%</span>
    </div>
    <div class="stock-pill">{stock_pill}</div>
    <ul class="hero-bullets">
      <li><span class="ico" aria-hidden="true">❄️</span><span><strong>{b1_t}</strong> {b1_d}</span></li>
      <li><span class="ico" aria-hidden="true">🔇</span><span><strong>{b2_t}</strong> {b2_d}</span></li>
      <li><span class="ico" aria-hidden="true">🔌</span><span><strong>{b3_t}</strong> {b3_d}</span></li>
      <li><span class="ico" aria-hidden="true">💶</span><span><strong>{b4_t}</strong> {b4_d}</span></li>
      <li><span class="ico" aria-hidden="true">📱</span><span><strong>{b5_t}</strong> {b5_d}</span></li>
    </ul>
    <a href="#order-form" class="cta-btn">{cta_hero}</a>
    <p class="secure-line">{secure}</p>
  </div>
  <div class="hero-image hero-image-desktop-only">
    <img decoding="async" src="/assets/img/products/climaair/hero.webp" alt="{alt_hero}" width="900" height="900" loading="eager" fetchpriority="high">
  </div>
</section>

<div class="wrap">
  <div class="trust-grid">
    <div class="trust-card"><div class="ico">🚚</div><h4>{t1_h}</h4><p>{t1_p}</p></div>
    <div class="trust-card"><div class="ico">💰</div><h4>{t2_h}</h4><p>{t2_p}</p></div>
    <div class="trust-card"><div class="ico">🔒</div><h4>{t3_h}</h4><p>{t3_p}</p></div>
    <div class="trust-card"><div class="ico">🛡️</div><h4>{t4_h}</h4><p>{t4_p}</p></div>
  </div>
</div>

<section class="order-section" id="order-form">
  <div class="wrap">
    <div class="urgency-strip">
      <div class="pieces-left">{pieces}</div>
      <div class="warn-box">
        <h3>{warn_h}</h3>
        <p>{warn_p}</p>
      </div>
      <div class="countdown-row">
        <div class="countdown-label">{countdown}</div>
        <div class="countdown-timer" id="countdownTimer">
          <div class="box"><div class="num" id="cd-h">00</div><div class="lbl">{hours}</div></div>
          <div class="sep">:</div>
          <div class="box"><div class="num" id="cd-m">14</div><div class="lbl">{mins}</div></div>
          <div class="sep">:</div>
          <div class="box"><div class="num" id="cd-s">59</div><div class="lbl">{secs}</div></div>
        </div>
      </div>
      <div class="stock-row">
        <div class="stock-label"><span class="left">{stock_l}</span><span class="right">{stock_r}</span></div>
        <div class="stock-bar"><div class="stock-bar-fill"></div></div>
      </div>
      <div class="live-row">
        <span class="dot"></span>
        <span id="liveCount" data-live="{live}">{live0}</span>
      </div>
    </div>

    <div class="order-card">
      <h2>{form_h}</h2>
      <p>{form_p}</p>
      <form class="tm-order-form order-form" action="https://offers.adricenetwork.com/forms/html/" method="post">
        <label for="name">{lab_name}</label>
        <input id="name" type="text" name="name" autocomplete="name" placeholder="{ph_name}" required><br>
        <label for="tel">{lab_tel}</label>
        <input id="tel" type="tel" name="tel" autocomplete="tel" placeholder="{ph_tel}" required><br>
        <label for="street-address">{lab_addr}</label>
        <input id="street-address" type="text" name="street-address" autocomplete="street-address" placeholder="{ph_addr}" required><br>
        <input name="uid" type="hidden" value="{uid}" />
        <input name="offer" type="hidden" value="{offer}" />
        <input name="lp" type="hidden" value="{lp}" />
        <input name="thankyoupage" type="hidden" value="https://gadgetspothub.com/{geo}/climaair/thank-you.html"/>
        <input name="webhook" type="hidden" value="{webhook}"/>
        <input name="_key" type="hidden" value="{key}" />
        <div style="margin-top: 10px; text-align: center">
          <button name="submit" type="submit">{buy}</button>
        </div>
        <p class="form-note">{form_note}</p>
        <script src="https://offers.adricenetwork.com/forms/html/js-v2/" async></script>
      </form>
    </div>
  </div>
</section>

<section class="why-block wrap">
  <div class="section-heading" style="margin-bottom:28px;">
    <span class="eyebrow">{benefits_ey}</span>
    <h2>{benefits_h}</h2>
  </div>
  <div class="why-grid">
    <div class="why-img"><img decoding="async" src="/assets/img/products/climaair/benefit-1.webp" alt="ClimaAir — FlowCore" loading="lazy"></div>
    <div>
      <div class="num-eyebrow">{w1_ey}</div>
      <h3>{w1_h}</h3>
      <div class="tag-row"><span class="tag">{w1_t1}</span><span class="tag">{w1_t2}</span></div>
      <p>{w1_p}</p>
      <p class="italic">{w1_i}</p>
    </div>
  </div>
</section>

<section class="why-block wrap">
  <div class="why-grid">
    <div class="why-img"><img decoding="async" src="/assets/img/products/climaair/benefit-2.webp" alt="ClimaAir — 4in1" loading="lazy"></div>
    <div>
      <div class="num-eyebrow">{w2_ey}</div>
      <h3>{w2_h}</h3>
      <div class="tag-row"><span class="tag">{w2_t1}</span><span class="tag">{w2_t2}</span></div>
      <p>{w2_p}</p>
      <p class="italic">{w2_i}</p>
    </div>
  </div>
</section>

<section class="why-block wrap" style="border-bottom:none;">
  <div class="why-grid">
    <div class="why-img"><img decoding="async" src="/assets/img/products/climaair/benefit-3.webp" alt="ClimaAir — A+++" loading="lazy"></div>
    <div>
      <div class="num-eyebrow">{w3_ey}</div>
      <h3>{w3_h}</h3>
      <div class="tag-row"><span class="tag">{w3_t1}</span><span class="tag">{w3_t2}</span></div>
      <p>{w3_p}</p>
      <p class="italic">{w3_i}</p>
    </div>
  </div>
</section>

<div class="wrap" style="padding-bottom:12px;">
  <a href="#order-form" class="cta-btn">{cta_mid}</a>
  <div class="mid-cta-note">
    <span>{mid1}</span>
    <span>{mid2}</span>
    <span>{mid3}</span>
  </div>
</div>

<section class="compare wrap">
  <div class="section-label">{cmp_ey}</div>
  <h2>{cmp_h}</h2>
  <p style="text-align:center;color:var(--color-text-muted);margin:-8px 0 20px;font-size:14.5px;">{cmp_sub}</p>
  <table>
    <tr><th></th><th>{cmp_trad}</th><th class="highlight">ClimaAir</th></tr>
    <tr><td>{r1c}</td><td>{r1a}</td><td class="win">{r1b}</td></tr>
    <tr><td>{r2c}</td><td>{r2a}</td><td class="win">{r2b}</td></tr>
    <tr><td>{r3c}</td><td>{r3a}</td><td class="win">{r3b}</td></tr>
    <tr><td>{r4c}</td><td>{r4a}</td><td class="win">{r4b}</td></tr>
    <tr><td>{r5c}</td><td>{r5a}</td><td class="win">{r5b}</td></tr>
    <tr><td>{r6c}</td><td>{r6a}</td><td class="win">{r6b}</td></tr>
  </table>
  <a href="#order-form" class="cta-btn" style="margin-top:20px;">{cta_price}</a>
</section>

<section class="testimonials">
  <div class="wrap">
    <div class="section-heading">
      <span class="eyebrow">{rev_ey}</span>
      <h2>{rev_h}</h2>
      <span class="eyebrow" style="display:block;margin-top:8px;color:#5b6472;font-weight:600;text-transform:none;letter-spacing:0;font-size:14px;">{rev_sub}</span>
    </div>
    <div class="t-grid">
      <div class="testimonial">
        <img decoding="async" class="t-photo" src="/assets/img/reviews/climaair/review-1.webp" alt="ClimaAir" loading="lazy">
        <div class="t-body">
          <div class="stars">★★★★★ 4,8/5</div>
          <p>{rev1}</p>
          <div class="author-row"><div class="author">{a1}</div></div>
        </div>
      </div>
      <div class="testimonial">
        <img decoding="async" class="t-photo" src="/assets/img/reviews/climaair/review-2.webp" alt="ClimaAir" loading="lazy">
        <div class="t-body">
          <div class="stars">★★★★★ 4,7/5</div>
          <p>{rev2}</p>
          <div class="author-row"><div class="author">{a2}</div></div>
        </div>
      </div>
      <div class="testimonial">
        <img decoding="async" class="t-photo" src="/assets/img/reviews/climaair/review-3.webp" alt="ClimaAir" loading="lazy">
        <div class="t-body">
          <div class="stars">★★★★★ 4,8/5</div>
          <p>{rev3}</p>
          <div class="author-row"><div class="author">{a3}</div></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="kit-section wrap">
  <div class="section-heading">
    <span class="eyebrow">{kit_ey}</span>
    <h2>{kit_h}</h2>
  </div>
  <div class="kit-box">
    <img decoding="async" src="/assets/img/products/climaair/kit.webp" alt="{alt_hero}" loading="lazy">
    <div class="kit-content">
      <p style="margin-bottom:16px;color:var(--color-text-muted);">{kit_p}</p>
      <div class="price-block" style="margin-bottom:16px;">
        <span class="was">{was}</span>
        <span class="now">{now}</span>
        <span class="pct">-50%</span>
      </div>
      <ul>
        <li>{k1}</li>
        <li>{k2}</li>
        <li>{k3}</li>
        <li>{k4}</li>
        <li>{k5}</li>
        <li>{k6}</li>
        <li>{k7}</li>
      </ul>
      <a href="#order-form" class="cta-btn">{cta_price}</a>
    </div>
  </div>
</section>

<section class="faq wrap">
  <div class="section-heading">
    <span class="eyebrow">{faq_ey}</span>
    <h2>{faq_h}</h2>
  </div>
  <p class="faq-lead">{faq_lead}</p>
  <div class="faq-item"><button class="faq-q" type="button"><span>{q1}</span><span class="arrow">▾</span></button>
    <div class="faq-a"><p>{a_q1}</p></div></div>
  <div class="faq-item"><button class="faq-q" type="button"><span>{q2}</span><span class="arrow">▾</span></button>
    <div class="faq-a"><p>{a_q2}</p></div></div>
  <div class="faq-item"><button class="faq-q" type="button"><span>{q3}</span><span class="arrow">▾</span></button>
    <div class="faq-a"><p>{a_q3}</p></div></div>
  <div class="faq-item"><button class="faq-q" type="button"><span>{q4}</span><span class="arrow">▾</span></button>
    <div class="faq-a"><p>{a_q4}</p></div></div>
  <div class="faq-item"><button class="faq-q" type="button"><span>{q5}</span><span class="arrow">▾</span></button>
    <div class="faq-a"><p>{a_q5}</p></div></div>
  <div class="faq-item"><button class="faq-q" type="button"><span>{q6}</span><span class="arrow">▾</span></button>
    <div class="faq-a"><p>{a_q6}</p></div></div>
</section>

<div class="wrap bottom-trust">
  <span>{bt1}</span>
  <span>{bt2}</span>
  <span>{bt3}</span>
</div>

<footer class="site-footer">
  <div class="container">
    <div class="site-footer__grid">
      <div>
        <a href="/" class="site-logo" aria-label="gadgetspothub.com home">
          <span class="site-logo__text"><span class="site-logo__text-primary">gadgetspothub</span><span class="site-logo__text-accent">.com</span></span>
        </a>
        <p class="site-footer__blurb">{foot_blurb}</p>
      </div>
      <div>
        <h4 class="site-footer__heading">{foot_info}</h4>
        <ul class="site-footer__list">
          <li><a href="/{geo}/about-us.html">{about}</a></li>
          <li><a href="/{geo}/contact-us.html">{contact}</a></li>
          <li><a href="/{geo}/privacy-policy.html">{privacy}</a></li>
          <li><a href="/{geo}/terms-conditions.html">{terms}</a></li>
          <li><a href="/{geo}/cookie-policy.html">{cookies}</a></li>
          <li><a href="/{geo}/shipping-policy.html">{ship}</a></li>
          <li><a href="/{geo}/refund-policy.html">{refund}</a></li>
        </ul>
      </div>
      <div>
        <h4 class="site-footer__heading">{foot_contact}</h4>
        <ul class="site-footer__list">
          <li><strong>Netmart LLC</strong></li>
          <li>County of Sussex 16192 Coastal Hwy</li>
          <li>Lewes, DE 19958-3608, United States</li>
          <li><a href="mailto:info@gadgetspothub.com">info@gadgetspothub.com</a></li>
        </ul>
      </div>
    </div>
    <div class="site-footer__bottom">
      © <span data-year>2026</span> <strong>Netmart LLC</strong> — {rights}.
      <a href="/">gadgetspothub.com</a>
    </div>
  </div>
</footer>

<script src="/assets/js/glacierair-landing.js" defer></script>
<script>
  document.querySelectorAll('[data-year]').forEach(function (el) {{
    el.textContent = String(new Date().getFullYear());
  }});
</script>
</body>
</html>
"""


class SafeDict(dict):
    def __missing__(self, key):
        raise KeyError(f"Missing template key: {key}")


def write_thank_you(geo: str, g: dict) -> None:
    src = ROOT / g["ty_src"]
    text = src.read_text(encoding="utf-8")
    old_slug = Path(g["ty_src"]).parent.name  # glacierair-3296
    # Extract old PRICE from SITE_CONFIG
    m = re.search(r"PRICE:\s*([0-9.]+)", text)
    old_price = m.group(1) if m else None
    text = text.replace("GlacierAir™", "ClimaAir™")
    text = text.replace(f"PRODUCT_SLUG: '{old_slug}'", "PRODUCT_SLUG: 'climaair'")
    if old_price:
        text = text.replace(f"PRICE: {old_price}", f"PRICE: {g['price_num']}")
        text = re.sub(
            rf"trackPurchase\({re.escape(old_price)},\s*'{g['currency']}'\)",
            f"trackPurchase({g['price_num']}, '{g['currency']}')",
            text,
        )
    out = ROOT / geo / "climaair" / "thank-you.html"
    out.write_text(text, encoding="utf-8")


def patch_sitemap() -> None:
    path = ROOT / "sitemap.xml"
    xml = path.read_text(encoding="utf-8")
    block = []
    for geo in GEOS:
        for loc in (f"https://gadgetspothub.com/{geo}/climaair/", f"https://gadgetspothub.com/{geo}/climaair/landing.html"):
            entry = f'  <url><loc>{loc}</loc><lastmod>2026-08-26</lastmod><changefreq>weekly</changefreq><priority>0.95</priority></url>\n'
            if loc not in xml:
                block.append(entry)
    if not block:
        return
    needle = '  <url><loc>https://gadgetspothub.com/it/climaair/landing.html</loc><lastmod>2026-08-26</lastmod><changefreq>weekly</changefreq><priority>0.95</priority></url>\n'
    if needle in xml:
        xml = xml.replace(needle, needle + "".join(block), 1)
    else:
        xml = xml.replace("</urlset>", "".join(block) + "</urlset>")
    path.write_text(xml, encoding="utf-8")


def main() -> None:
    missing = set(GEOS) - set(TR)
    extra = set(TR) - set(GEOS)
    if missing or extra:
        raise SystemExit(f"Geo mismatch TR vs GEOS missing={missing} extra={extra}")

    for geo, g in GEOS.items():
        t = TR[geo]
        dest = ROOT / geo / "climaair"
        dest.mkdir(parents=True, exist_ok=True)
        payload = SafeDict({**t, **g, "geo": geo, "uid": UID, "webhook": WEBHOOK})
        payload["cta_price"] = t["cta_price"].format(now=g["now"])
        (dest / "landing.html").write_text(LANDING_TMPL.format_map(payload), encoding="utf-8")
        (dest / "index.html").write_text(INDEX_TMPL.format(lang=g["lang"], geo=geo), encoding="utf-8")
        write_thank_you(geo, g)
        print(f"wrote {geo}/climaair/  now={g['now']}")
    patch_sitemap()
    print("sitemap updated")


if __name__ == "__main__":
    main()

