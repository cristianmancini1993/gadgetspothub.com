#!/usr/bin/env python3
"""Generate Polar PRO Max column-AC landings for CZ ES GR HU IT PT RO."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
UID_NEW = "0198c21c-8430-751a-a450-d7f01a76c3ee"
WH_NEW = "https://hook.eu2.make.com/7nudarijfrsvnhnwfnpqfh2t8vqt109i"
UID_OLD = "018e3961-c73a-7965-8fc1-b1d91c869a42"
WH_OLD = "https://hook.eu2.make.com/i7pmea9fmpnepx94e5z6dxfwvl1bnnlh"

# Country Adrice codes from the latest AC campaigns on this domain.
GEOS = {
    "cz": dict(lang="cs", currency="CZK", price=1799, offer="3590", lp="3627",
               key="e5d307d9de4b10efb23d853246a0677d6b8c6f80", uid=UID_NEW, webhook=WH_NEW,
               now="1 799 Kč", was="3 598 Kč", now_long="1 799 Kč"),
    "es": dict(lang="es", currency="EUR", price=89, offer="3587", lp="3624",
               key="2af2c1ec0bbe33b257d37839f043b8beba23a806", uid=UID_NEW, webhook=WH_NEW,
               now="89 €", was="178 €", now_long="89,00 €"),
    "gr": dict(lang="el", currency="EUR", price=89, offer="3587", lp="3624",
               key="2af2c1ec0bbe33b257d37839f043b8beba23a806", uid=UID_NEW, webhook=WH_NEW,
               now="89 €", was="178 €", now_long="89,00 €"),
    "hu": dict(lang="hu", currency="HUF", price=29999, offer="3431", lp="3467",
               key="2a933fff3f54a5436980d423bd4fe776adb2d052", uid=UID_NEW, webhook=WH_NEW,
               now="29 999 Ft", was="59 998 Ft", now_long="29 999 Ft"),
    "it": dict(lang="it", currency="EUR", price=69, offer="1274", lp="1293",
               key="bb9bb46add2c9a64d7a6da26437ad8640be0540b", uid=UID_OLD, webhook=WH_OLD,
               now="69 €", was="138 €", now_long="69,00 €"),
    "pt": dict(lang="pt", currency="EUR", price=79, offer="3588", lp="3625",
               key="0f4b28c87f1287b7753a5379eabeb8581b83bb40", uid=UID_NEW, webhook=WH_NEW,
               now="79 €", was="158 €", now_long="79,00 €"),
    "ro": dict(lang="ro", currency="RON", price=379, offer="1298", lp="1317",
               key="dfa0121dc67d1076067284708b56bb71dcab03e0", uid=UID_OLD, webhook=WH_OLD,
               now="379 lei", was="758 lei", now_long="379 lei"),
}

TR = {
    "cz": dict(
        title="Polar PRO Max — Přenosná sloupová klimatizace 4 v 1 | 1 799 Kč",
        description="Přenosná sloupová klimatizace Polar PRO Max 4 v 1. Chladí, topí, odvlhčuje a čistí až 35 m². Bez instalace. Platba na dobírku. Dnes 1 799 Kč místo 3 598 Kč.",
        cookie_text="Používáme technické a cookies třetích stran ke zlepšení vašeho zážitku a pro analytiku.",
        cookie_accept="Přijmout", cookie_learn="Zjistit více", submitting="Odesílání...",
        sticky_cta="Aktivovat nabídku",
        rating="4,72/5 · Více než 3 100 ověřených recenzí",
        h1_pre="DOSLOVA VYKLÍZÍME SKLADY:",
        h1_mid="přenosná sloupová klimatizace za",
        h1_end="je dnes vaše za",
        h1_only=" pouhých {now}!",
        sub="Přenosná sloupová klimatizace, která za 5 minut skoncuje s letním vedrem. Postavte ji kam chcete, zapojte do zásuvky, stiskněte ON a pusťte si proud vyčištěného ledového vzduchu. Bez instalace, bez čekání, doručení domů do 24 hodin.",
        img_hero="Wallconvector Pro 4 v 1 — přenosná sloupová klimatizace",
        save="Ušetříte {now} — sleva 50 %",
        scarcity="⚠️ Likvidační kampaň: cena {now} platí, dokud nedojde zásoba z této kampaně.",
        cta_hero="Aktivovat nabídku — objednat nyní",
        trust="Platba na dobírku · Doprava zdarma · 4 roky záruka",
        order_h="Zásoba kampaně", order_hl=" omezená ", order_h2="— rezervujte si svou",
        order_p="Vyplňte formulář. Vaše objednávka se zpracuje okamžitě.",
        card_title="ZADEJTE DORUČOVACÍ ÚDAJE",
        card_sub="Objednávka se odešle ihned. Platíte až při doručení, přímo kurýrovi.",
        progress="KAMPAŇ BĚŽÍ",
        progress_note="Akční cena platí, dokud nedojde zásoba",
        pill="Platba na dobírku k dispozici",
        label_name="Jméno Příjmení*", label_addr="Adresa*", label_tel="Telefon*",
        btn="Objednat nyní",
        form_note="🔒 Bez zálohy · Platíte při doručení · Odeslání 24/48 h",
        feat_h="Není to obyčejný ventilátor.",
        feat_h2=" Je to přenosný systém 4 v 1, který nepotřebuje stavební práce ani venkovní jednotku",
        feat_lead="Multifunkční přenosný systém 4 v 1 nejnovější generace s 12 000 BTU. Díky kolečkům ho přemístíte z místnosti do místnosti. Chladí, topí, odvlhčuje a filtruje vzduch v místnostech do 35 m² během několika minut.",
        f1h="CHLADÍ", f1p="Sníží teplotu až na 16 °C během několika minut. Silný výkon pro celý prostor.",
        f2h="TOPÍ", f2p="V zimě zvýší teplotu až na 42 °C. Konec zimy i astronomických účtů.",
        f3h="ODVLHČUJE", f3p="Odstraní nadbytečnou vlhkost. Sbohem plísni, sbohem těžkému vzduchu. Zdravý a pohodlný domov.",
        f4h="ČISTÍ", f4p="Integrovaný HEPA filtr: zachytí prach a částice ve vzduchu.",
        secret_h="Tajemství, které výrobci klasických klimatizací nechtějí, abyste znali",
        secret_p1="Proč platit instalatérovi, žádat o povolení SVJ a věšet ošklivou hlučnou krabici ven z okna?",
        secret_p2="Naše sloupová Polar PRO Max ",
        secret_strong="NEMÁ VENKOVNÍ JEDNOTKU",
        secret_p3=". Používá vnitřní motor s uzavřeným cyklem. Postavte ji do jakékoli místnosti díky tichým kolečkům, zapojte do zásuvky a je hned připravená. ",
        secret_zero="Nulová instalace, nulová údržba, nulové extra náklady.",
        d1h="ŘÍZENÁ SPOTŘEBA", d1p="Systém reguluje výkon a po dosažení nastavené teploty přejde do pohotovosti — spotřebuje jen to, co je potřeba.",
        d2h="ČISTŠÍ VZDUCH", d2p="Integrovaný HEPA filtr zachytí prach a částice ve vzduchu místnosti.",
        d3h="NULOVÝ HLUK", d3p="Ultratichý noční režim umožní spát bez bzučení starých spotřebičů.",
        img_tech="Polar PRO Max — přenosná sloupová klimatizace bez venkovní jednotky",
        specs="TECHNICKÉ ÚDAJE",
        r_pow="Výkon", r_cov="Pokrytí", r_eco="Úsporný režim", r_con="Spotřeba",
        r_reg="Regulace", r_out="Venkovní jednotka", r_noi="Hlučnost", r_fil="Filtr",
        r_ctl="Ovládání", r_war="Záruka",
        v_pow="12 000 BTU", v_cov="Až 35 m²", v_eco="Termostat + automatický standby",
        v_con="Od 370 W do 1800 W (modulující)", v_reg="Automatický modulující výkon",
        v_out="NENÍ POTŘEBA", v_noi="Ultratichý (noční režim)", v_fil="Pratelný HEPA",
        v_ctl="LCD dálkový ovladač + aplikace", v_war="2 roky záruka výrobce",
        cta_price="🟢 Objednat nyní za {now}",
        incl_h="Co dnes dostanete v ceně",
        i1="Přenosná sloupová jednotka Polar PRO Max 4 v 1",
        i2="Multifunkční LCD dálkový ovladač",
        i3="Sada tichých koleček pro snadné přemístění",
        i4="Návod k použití v češtině",
        i5="Chytré ovládání přes vzdálenou aplikaci",
        i6="Prodloužená záruka výrobce na 2 roky",
        today="JEN DNES",
        i7="Vrácení zdarma do 60 dnů s okamžitou refundací",
        reviews_avg="Průměr ověřených recenzí našich zákazníků v Česku",
        rev1_alt="Polar PRO Max v obývacím pokoji",
        rev1_h="Kupoval jsem bez velkých očekávání",
        rev1_p="„Kvůli ceně jsem váhal. Používám ho v obýváku k večeru a rozdíl je znát. Účet zůstal v linii s předchozími měsíci. Rychlé doručení, platil jsem kurýrovi.“",
        rev1_n="— Jan Novotný, Praha",
        rev2_alt="Polar PRO Max v ložnici",
        rev2_h="Hluk byl můj největší strach",
        rev2_p="„Mám lehký spánek a už jsem na tyto přístroje zanevřel. V nočním režimu ho skoro neslyšíte. Vyndal jsem ho z krabice, zapojil do zásuvky a fungoval bez volání kohokoli.“",
        rev2_n="— Petra Svobodová, Brno",
        rev3_alt="Polar PRO Max přemístěný na kolečkách",
        rev3_h="Vozím ho z místnosti do místnosti",
        rev3_p="„Podle denní doby ho posouvám mezi pracovnou a ložnicí. Kolečka pomáhají a nic nerozebírám. Za tu cenu jsem s provedením spokojený.“",
        rev3_n="— Martin Dvořák, Ostrava",
        faq_h="Časté dotazy",
        q1="Potřebuje přístroj venkovní jednotku?",
        a1="Ne. To je právě jeho největší výhoda: bez vrtání, bez povolení, bez nákladů na instalaci. Funguje s vnitřním uzavřeným okruhem. Stačí ho postavit na kolečka a zapojit do běžné zásuvky.",
        q2="Kolik skutečně spotřebuje?",
        a2="Inteligentní systém automaticky reguluje výkon mezi 370 W a 1800 W. Jakmile dosáhne požadované teploty, sníží spotřebu na minimum, aby ji udržel. Udržováním teploty při sníženém výkonu spotřebuje méně, než kdyby běžel pořád na maximum.",
        q3="Jak velkou místnost dokáže zchladit?",
        a3="S 12 000 BTU je navržen pro místnosti do cca 35 m². Hodí se do obýváků, ložnic a středně velkých kanceláří.",
        q4="Jak funguje platba na dobírku?",
        a4="Vyplníte formulář, náš tým objednávku potvrdí a kurýr doručí balík k vám domů. Platíte až při převzetí, přímo kurýrovi. Zcela bez rizika.",
        q5="Mohu ho vrátit, pokud nebudu spokojen?",
        a5="Samozřejmě. Máte 60 dní na vyzkoušení. Pokud z jakéhokoli důvodu nebudete spokojeni, zajistíme bezplatné vyzvednutí a vrátíme kupní cenu.",
        final_h="Zajistěte si technologii budoucnosti za",
        final_only=" pouhých {now}",
        final_warn="⚠️ Akční cena {now_long} platí, dokud vydrží zásoba.",
        final_sub="Likvidační kampaň končí, jakmile dojde zásoba.",
        final_cta="🟢 Klikněte sem a aktivujte speciální nabídku",
        final_trust="Platba na dobírku · Vrácení zdarma 60 dní · 4 roky záruka",
        foot_blurb="Užitečné produkty pro každodenní život, doručení do 24–48 hodin s platbou na dobírku.",
        foot_info="Informace", foot_contact="Kontakt",
        about="O nás", contact="Kontaktujte nás",
        privacy="Zásady ochrany osobních údajů", terms="Smluvní podmínky",
        cookies="Zásady používání souborů cookie", ship="Zásady dopravy", refund="Zásady vrácení peněz",
        rights="Všechna práva vyhrazena",
        ty_title="Objednávka přijata — Počkejte na potvrzovací hovor | Polar PRO Max",
        ty_desc="Vaše objednávka Polar PRO Max byla zaznamenána. Zbývá poslední krok: přijměte potvrzovací hovor od našeho operátora.",
        ty_h="Vaše objednávka Polar PRO Max byla úspěšně zaznamenána!",
        ty_sub="Skvělé — objednávka se zpracovává. Zbývá už jen <strong>poslední krok</strong> k dokončení a odeslání.",
        ty_prod="Polar PRO Max 4 v 1 — sloupová klimatizace",
        ty_meta="12 000 BTU · Platba na dobírku",
        ty_ey="👇 Co máte udělat teď", ty_ah="📞 Přijměte potvrzovací hovor",
        ty_ap="Náš operátor vás bude kontaktovat <strong>v příštích hodinách</strong>, aby potvrdil objednávku Polar PRO Max.",
        ty_aw="Pokud hovor nepřijmete, objednávka bude automaticky zrušena.",
        ty_hh="🕒 Kontaktní hodiny", ty_hours="Pondělí – Sobota · 9:00 – 18:00",
        ty_nh="📋 Co se stane dál",
        ty_s1="Přijměte hovor a <strong>potvrďte své údaje</strong>",
        ty_s2="Vaši Polar PRO Max odešleme do <strong>24–48 hodin</strong>",
        ty_s3="Doručení domů a <strong>platba na dobírku</strong>",
        ty_b1="🔒 Platba na dobírku", ty_b2="🛡️ Záruka 2 roky", ty_b3="↩️ Vrácení 60 dní",
        ty_alt="Polar PRO Max přenosná sloupová klimatizace 4 v 1",
    ),
    "es": dict(
        title="Polar PRO Max — Aire acondicionado portátil de columna 4 en 1 | 89 €",
        description="Aire acondicionado portátil de columna Polar PRO Max 4 en 1. Enfría, calienta, deshumidifica y purifica hasta 35 m². Sin instalación. Pago contra reembolso. Hoy 89 € en lugar de 178 €.",
        cookie_text="Usamos cookies técnicas y de terceros para mejorar tu experiencia y para análisis.",
        cookie_accept="Aceptar", cookie_learn="Más información", submitting="Enviando...",
        sticky_cta="Activar la oferta",
        rating="4,72/5 · Más de 3 100 reseñas verificadas",
        h1_pre="ESTAMOS VACIANDO LITERALMENTE NUESTROS ALMACENES:",
        h1_mid="el aire acondicionado portátil de columna de",
        h1_end="hoy es tuyo por",
        h1_only=" solo {now}!",
        sub="El aire acondicionado portátil de columna que acaba con el calor del verano en 5 minutos. Colócalo donde quieras, enchúfalo, pulsa ON y recibe una ráfaga de frescura purificada y helada. Sin instalación, sin espera, entrega a domicilio en 24 horas.",
        img_hero="Wallconvector Pro 4 en 1 — aire acondicionado portátil de columna",
        save="Ahorra {now} — descuento del 50%",
        scarcity="⚠️ Campaña de liquidación: el precio de {now} es válido hasta agotar el stock de esta campaña.",
        cta_hero="Activa la oferta — pide ahora",
        trust="Pago contra reembolso · Envío gratis · 4 años de garantía",
        order_h="Stock de campaña", order_hl=" limitado ", order_h2="— reserva ya el tuyo",
        order_p="Rellena el formulario. Tu pedido se procesará de inmediato.",
        card_title="INTRODUCE LOS DATOS DE ENTREGA",
        card_sub="Tu pedido se enviará de inmediato. Solo pagas al recibirlo, directamente al repartidor.",
        progress="CAMPAÑA ACTIVA",
        progress_note="Precio de campaña válido hasta agotar stock",
        pill="Pago contra reembolso disponible",
        label_name="Nombre Apellidos*", label_addr="Dirección*", label_tel="Teléfono*",
        btn="Haz tu pedido",
        form_note="🔒 Sin adelanto · Pagas al recibir · Envío 24/48 h",
        feat_h="No es un simple ventilador.",
        feat_h2=" Es un sistema portátil 4 en 1 que no necesita obras ni unidad exterior",
        feat_lead="Sistema multifunción portátil 4 en 1 de última generación con 12.000 BTU. Se mueve de una habitación a otra gracias a las ruedas. Enfría, calienta, deshumidifica y filtra el aire en estancias de hasta 35 m², en pocos minutos.",
        f1h="ENFRÍA", f1p="Baja la temperatura hasta 16 °C en pocos minutos. Potencia fuerte para todo el ambiente.",
        f2h="CALIENTA", f2p="En invierno sube la temperatura hasta 42 °C. Se acabó el frío y las facturas astronómicas.",
        f3h="DESHUMIDIFICA", f3p="Elimina el exceso de humedad. Adiós moho, adiós aire pesado. Casa sana y cómoda.",
        f4h="PURIFICA", f4p="Filtro HEPA integrado: retiene polvo y partículas en suspensión.",
        secret_h="El secreto que los fabricantes de aire acondicionado tradicional no quieren que sepas",
        secret_p1="¿Por qué pagar a un instalador, pedir permiso a la comunidad y colgar una caja fea y ruidosa fuera de la ventana?",
        secret_p2="Nuestro Polar PRO Max de columna ",
        secret_strong="NO TIENE UNIDAD EXTERIOR",
        secret_p3=". Utiliza un motor interno de ciclo cerrado continuo. Colócalo en cualquier habitación gracias a las ruedas silenciosas, enchúfalo y queda listo. ",
        secret_zero="Cero instalación, cero mantenimiento, cero costes extra.",
        d1h="CONSUMO CONTROLADO", d1p="El sistema regula la potencia y entra en espera al alcanzar la temperatura marcada, consumiendo solo lo necesario.",
        d2h="AIRE MÁS LIMPIO", d2p="El filtro HEPA integrado retiene polvo y partículas en suspensión en la habitación.",
        d3h="CERO RUIDO", d3p="El modo nocturno ultrasilencioso permite dormir sin el zumbido de los aparatos antiguos.",
        img_tech="Polar PRO Max — aire acondicionado portátil de columna sin unidad exterior",
        specs="DATOS TÉCNICOS",
        r_pow="Potencia", r_cov="Cobertura", r_eco="Modo económico", r_con="Consumo",
        r_reg="Regulación", r_out="Unidad exterior", r_noi="Nivel de ruido", r_fil="Filtro",
        r_ctl="Control", r_war="Garantía",
        v_pow="12.000 BTU", v_cov="Hasta 35 m²", v_eco="Termostato + standby automático",
        v_con="De 370 W a 1800 W (modulante)", v_reg="Potencia modulante automática",
        v_out="NO NECESARIA", v_noi="Ultrasilencioso (modo nocturno)", v_fil="HEPA lavable",
        v_ctl="Mando LCD + app a distancia", v_war="2 años de garantía del fabricante",
        cta_price="🟢 Pide ahora por {now}",
        incl_h="Lo que recibes hoy incluido en el precio de",
        i1="Unidad portátil de columna Polar PRO Max 4 en 1",
        i2="Mando LCD multifunción",
        i3="Kit de ruedas silenciosas para moverlo con facilidad",
        i4="Manual de instrucciones en español",
        i5="Control inteligente a través de la app a distancia",
        i6="Garantía del fabricante ampliada a 2 años",
        today="SOLO HOY",
        i7="Devolución gratuita en 60 días con reembolso inmediato",
        reviews_avg="Media de las reseñas verificadas de nuestros clientes en España",
        rev1_alt="Polar PRO Max en el salón",
        rev1_h="Lo compré sin grandes expectativas",
        rev1_p="“Dudaba por el precio. Lo uso en el salón al final de la tarde y la diferencia se nota. La factura se mantuvo en línea con los meses anteriores. Entrega rápida y pagué al repartidor.”",
        rev1_n="— Carlos Ruiz, Valencia",
        rev2_alt="Polar PRO Max en el dormitorio",
        rev2_h="El ruido era mi mayor miedo",
        rev2_p="“Tengo el sueño ligero y ya había tirado la toalla con estos aparatos. En modo nocturno apenas se oye. Lo saqué de la caja, lo enchufé y funcionó sin llamar a nadie.”",
        rev2_n="— Marta López, Sevilla",
        rev3_alt="Polar PRO Max desplazado sobre ruedas",
        rev3_h="Lo llevo de habitación en habitación",
        rev3_p="“Lo muevo entre el despacho y el dormitorio según la hora. Las ruedas ayudan y no desmonto nada. Por lo que costó, estoy satisfecho con los acabados.”",
        rev3_n="— Javier Ortega, Zaragoza",
        faq_h="Preguntas frecuentes",
        q1="¿El aparato necesita una unidad exterior?",
        a1="No. Esa es precisamente su mayor ventaja: sin agujeros, sin permisos, sin costes de instalación. Funciona con un circuito cerrado interno. Basta colocarlo sobre las ruedas y enchufarlo a un enchufe normal.",
        q2="¿Cuánto consume de verdad?",
        a2="El sistema inteligente regula automáticamente la potencia entre 370 W y 1800 W. En cuanto alcanza la temperatura deseada, reduce el consumo al mínimo para mantenerla. Al mantener la temperatura con potencia reducida, consume menos que si funcionara siempre al máximo.",
        q3="¿Qué tamaño de habitación puede enfriar?",
        a3="Con 12.000 BTU está pensado para estancias de hasta unos 35 m². Sirve para salones, dormitorios y despachos de tamaño medio.",
        q4="¿Cómo funciona el pago contra reembolso?",
        a4="Rellenas el formulario, nuestro equipo confirma el pedido y el repartidor entrega el paquete en tu casa. El pago se hace solo al recibirlo, directamente al repartidor. Totalmente sin riesgos.",
        q5="¿Puedo devolverlo si no quedo satisfecho?",
        a5="Claro. Tienes 60 días para probar el aparato. Si por cualquier motivo no quedas satisfecho, organizamos la recogida gratuita y reembolsamos el precio de compra.",
        final_h="Asegura la tecnología del futuro por",
        final_only=" solo {now}",
        final_warn="⚠️ El precio de campaña de {now_long} es válido mientras dure el stock.",
        final_sub="La campaña de liquidación termina cuando se agote el stock.",
        final_cta="🟢 Pulsa aquí y activa la oferta especial",
        final_trust="Pago contra reembolso · Devolución gratuita 60 días · 4 años de garantía",
        foot_blurb="Productos útiles para el día a día, entrega en 24–48 horas con pago contra reembolso.",
        foot_info="Información", foot_contact="Contacto",
        about="Sobre nosotros", contact="Contáctanos",
        privacy="Política de privacidad", terms="Términos y condiciones",
        cookies="Política de cookies", ship="Política de envío", refund="Política de reembolso",
        rights="Todos los derechos reservados",
        ty_title="Pedido recibido — Espera la llamada de confirmación | Polar PRO Max",
        ty_desc="Tu pedido Polar PRO Max ha sido registrado. Solo falta un último paso: responde a la llamada de confirmación de nuestro operador.",
        ty_h="¡Tu pedido Polar PRO Max se ha registrado correctamente!",
        ty_sub="Perfecto — tu pedido está en proceso. Solo falta <strong>un último paso</strong> para completarlo y ponerlo en marcha.",
        ty_prod="Polar PRO Max 4 en 1 — aire acondicionado de columna",
        ty_meta="12.000 BTU · Pago contra reembolso",
        ty_ey="👇 Qué debes hacer ahora", ty_ah="📞 Responde a la llamada de confirmación",
        ty_ap="Un operador te contactará <strong>en las próximas horas</strong> para confirmar tu pedido Polar PRO Max.",
        ty_aw="Si no respondes a la llamada, el pedido se cancelará automáticamente.",
        ty_hh="🕒 Horario de contacto", ty_hours="Lunes – Sábado · 9:00 – 18:00",
        ty_nh="📋 Qué ocurre después",
        ty_s1="Responde a la llamada y <strong>confirma tus datos</strong>",
        ty_s2="Tu Polar PRO Max se enviará en <strong>24–48 horas</strong>",
        ty_s3="Entrega a domicilio y <strong>pago contra reembolso</strong>",
        ty_b1="🔒 Pago contra reembolso", ty_b2="🛡️ Garantía 2 años", ty_b3="↩️ Devolución 60 días",
        ty_alt="Polar PRO Max aire acondicionado portátil de columna 4 en 1",
    ),
    "gr": dict(
        title="Polar PRO Max — Φορητό κλιματιστικό στήλης 4 σε 1 | 89 €",
        description="Φορητό κλιματιστικό στήλης Polar PRO Max 4 σε 1. Ψύχει, θερμαίνει, αφυγραίνει και καθαρίζει έως 35 m². Χωρίς εγκατάσταση. Πληρωμή στην παράδοση. Σήμερα 89 € αντί 178 €.",
        cookie_text="Χρησιμοποιούμε τεχνικά cookies και cookies τρίτων για να βελτιώσουμε την εμπειρία σας και για ανάλυση.",
        cookie_accept="Αποδοχή", cookie_learn="Περισσότερα", submitting="Αποστολή...",
        sticky_cta="Ενεργοποίηση προσφοράς",
        rating="4,72/5 · Πάνω από 3 100 επαληθευμένες αξιολογήσεις",
        h1_pre="ΑΔΕΙΑΖΟΥΜΕ ΚΥΡΙΟΛΕΚΤΙΚΑ ΤΙΣ ΑΠΟΘΗΚΕΣ ΜΑΣ:",
        h1_mid="το φορητό κλιματιστικό στήλης των",
        h1_end="σήμερα είναι δικό σου για",
        h1_only=" μόλις {now}!",
        sub="Το φορητό κλιματιστικό στήλης που τελειώνει τη ζέστη του καλοκαιριού σε 5 λεπτά. Βάλ’ το όπου θέλεις, σύνδεσέ το στην πρίζα, πάτα ON και δέξου μια ριπή καθαρής, παγωμένης δροσιάς. Χωρίς εγκατάσταση, χωρίς αναμονή, παράδοση στο σπίτι σε 24 ώρες.",
        img_hero="Wallconvector Pro 4 σε 1 — φορητό κλιματιστικό στήλης",
        save="Εξοικονομείς {now} — έκπτωση 50%",
        scarcity="⚠️ Εκστρατεία εκκαθάρισης: η τιμή {now} ισχύει μέχρι εξαντλήσεως του αποθέματος αυτής της καμπάνιας.",
        cta_hero="Ενεργοποίησε την προσφορά — παρήγγειλε τώρα",
        trust="Πληρωμή στην παράδοση · Δωρεάν αποστολή · 4 χρόνια εγγύηση",
        order_h="Απόθεμα καμπάνιας", order_hl=" περιορισμένο ", order_h2="— κλείσε το δικό σου",
        order_p="Συμπλήρωσε τη φόρμα. Η παραγγελία σου θα επεξεργαστεί αμέσως.",
        card_title="ΣΥΜΠΛΗΡΩΣΕ ΤΑ ΣΤΟΙΧΕΙΑ ΠΑΡΑΔΟΣΗΣ",
        card_sub="Η παραγγελία αποστέλλεται αμέσως. Πληρώνεις μόνο στην παράδοση, απευθείας στον διανομέα.",
        progress="ΕΝΕΡΓΗ ΚΑΜΠΑΝΙΑ",
        progress_note="Η τιμή καμπάνιας ισχύει μέχρι εξαντλήσεως αποθέματος",
        pill="Διατίθεται πληρωμή στην παράδοση",
        label_name="Ονοματεπώνυμο*", label_addr="Διεύθυνση*", label_tel="Τηλέφωνο*",
        btn="Παραγγείλτε τώρα",
        form_note="🔒 Χωρίς προκαταβολή · Πληρώνεις στην παράδοση · Αποστολή 24/48 ώρες",
        feat_h="Δεν είναι ένας απλός ανεμιστήρας.",
        feat_h2=" Είναι ένα φορητό σύστημα 4 σε 1 που δεν χρειάζεται έργα ούτε εξωτερική μονάδα",
        feat_lead="Πολυλειτουργικό φορητό σύστημα 4 σε 1 τελευταίας γενιάς με 12.000 BTU. Μετακινείται από δωμάτιο σε δωμάτιο χάρη στους τροχούς. Ψύχει, θερμαίνει, αφύγρανση και φιλτράρει τον αέρα σε χώρους έως 35 m², σε λίγα λεπτά.",
        f1h="ΨΥΧΕΙ", f1p="Κατεβάζει τη θερμοκρασία έως 16 °C σε λίγα λεπτά. Ισχυρή απόδοση για όλο τον χώρο.",
        f2h="ΘΕΡΜΑΙΝΕΙ", f2p="Τον χειμώνα ανεβάζει τη θερμοκρασία έως 42 °C. Τέλος στο κρύο και στους υπέρογκους λογαριασμούς.",
        f3h="ΑΦΥΓΡΑΙΝΕΙ", f3p="Αφαιρεί την υπερβολική υγρασία. Αντίο μούχλα, αντίο βαρύς αέρας. Υγιές και άνετο σπίτι.",
        f4h="ΚΑΘΑΡΙΖΕΙ", f4p="Ενσωματωμένο φίλτρο HEPA: συγκρατεί σκόνη και αιωρούμενα σωματίδια.",
        secret_h="Το μυστικό που οι κατασκευαστές κλασικών κλιματιστικών δεν θέλουν να μάθεις",
        secret_p1="Γιατί να πληρώσεις τεχνικό, να ζητήσεις άδεια από την πολυκατοικία και να κρεμάσεις ένα άσχημο, θορυβώδες κουτί έξω από το παράθυρο;",
        secret_p2="Το Polar PRO Max στήλης ",
        secret_strong="ΔΕΝ ΕΧΕΙ ΕΞΩΤΕΡΙΚΗ ΜΟΝΑΔΑ",
        secret_p3=". Χρησιμοποιεί εσωτερικό μοτέρ κλειστού κύκλου. Το βάζεις σε οποιοδήποτε δωμάτιο χάρη στους αθόρυβους τροχούς, το συνδέεις στην πρίζα και είναι έτοιμο. ",
        secret_zero="Μηδενική εγκατάσταση, μηδενική συντήρηση, μηδενικά έξτρα κόστη.",
        d1h="ΕΛΕΓΧΟΜΕΝΗ ΚΑΤΑΝΑΛΩΣΗ", d1p="Το σύστημα ρυθμίζει την ισχύ και μπαίνει σε αναμονή μόλις φτάσει την επιλεγμένη θερμοκρασία, καταναλώνοντας μόνο ό,τι χρειάζεται.",
        d2h="ΚΑΘΑΡΟΤΕΡΟΣ ΑΕΡΑΣ", d2p="Το ενσωματωμένο φίλτρο HEPA συγκρατεί σκόνη και αιωρούμενα σωματίδια στον χώρο.",
        d3h="ΜΗΔΕΝΙΚΟΣ ΘΟΡΥΒΟΣ", d3p="Η υπερ-αθόρυβη νυχτερινή λειτουργία επιτρέπει ύπνο χωρίς το βουητό των παλιών συσκευών.",
        img_tech="Polar PRO Max — φορητό κλιματιστικό στήλης χωρίς εξωτερική μονάδα",
        specs="ΤΕΧΝΙΚΑ ΧΑΡΑΚΤΗΡΙΣΤΙΚΑ",
        r_pow="Ισχύς", r_cov="Κάλυψη", r_eco="Οικονομική λειτουργία", r_con="Κατανάλωση",
        r_reg="Ρύθμιση", r_out="Εξωτερική μονάδα", r_noi="Επίπεδο θορύβου", r_fil="Φίλτρο",
        r_ctl="Έλεγχος", r_war="Εγγύηση",
        v_pow="12.000 BTU", v_cov="Έως 35 m²", v_eco="Θερμοστάτης + αυτόματο standby",
        v_con="Από 370 W έως 1800 W (διαμορφούμενη)", v_reg="Αυτόματη διαμορφούμενη ισχύς",
        v_out="ΔΕΝ ΑΠΑΙΤΕΙΤΑΙ", v_noi="Υπερ-αθόρυβο (νυχτερινή λειτουργία)", v_fil="Πλενόμενο HEPA",
        v_ctl="Τηλεχειριστήριο LCD + εφαρμογή εξ αποστάσεως", v_war="2 χρόνια εγγύηση κατασκευαστή",
        cta_price="🟢 Παράγγειλε τώρα με {now}",
        incl_h="Τι λαμβάνεις σήμερα στην τιμή των",
        i1="Φορητή μονάδα στήλης Polar PRO Max 4 σε 1",
        i2="Πολυλειτουργικό τηλεχειριστήριο LCD",
        i3="Κιτ αθόρυβων τροχών για εύκολη μετακίνηση",
        i4="Εγχειρίδιο οδηγιών στα ελληνικά",
        i5="Έξυπνος έλεγχος μέσω εφαρμογής εξ αποστάσεως",
        i6="Επέκταση εγγύησης κατασκευαστή στα 2 χρόνια",
        today="ΜΟΝΟ ΣΗΜΕΡΑ",
        i7="Δωρεάν επιστροφή σε 60 ημέρες με άμεση επιστροφή χρημάτων",
        reviews_avg="Μέσος όρος επαληθευμένων αξιολογήσεων των πελατών μας στην Ελλάδα",
        rev1_alt="Polar PRO Max στο σαλόνι",
        rev1_h="Το πήρα χωρίς μεγάλες προσδοκίες",
        rev1_p="«Δίσταζα λόγω της τιμής. Το χρησιμοποιώ στο σαλόνι το απόγευμα και η διαφορά φαίνεται. Ο λογαριασμός έμεινε στα ίδια με τους προηγούμενους μήνες. Γρήγορη παράδοση και πλήρωσα στον διανομέα.»",
        rev1_n="— Γιώργος Παπαδόπουλος, Θεσσαλονίκη",
        rev2_alt="Polar PRO Max στην κρεβατοκάμαρα",
        rev2_h="Ο θόρυβος ήταν ο μεγαλύτερος φόβος μου",
        rev2_p="«Έχω ελαφρύ ύπνο και είχα ήδη εγκαταλείψει αυτές τις συσκευές. Στη νυχτερινή λειτουργία σχεδόν δεν ακούγεται. Το έβγαλα από το κουτί, το έβαλα στην πρίζα και δούλεψε χωρίς να καλέσω κανέναν.»",
        rev2_n="— Μαρία Νικολάου, Πάτρα",
        rev3_alt="Polar PRO Max μετακινούμενο με τροχούς",
        rev3_h="Το πάω από δωμάτιο σε δωμάτιο",
        rev3_p="«Το μεταφέρω μεταξύ γραφείου και κρεβατοκάμαρας ανάλογα με την ώρα. Οι τροχοί βοηθούν και δεν ξεμοντάρω τίποτα. Για την τιμή του, είμαι ικανοποιημένος με τα φινιρίσματα.»",
        rev3_n="— Νίκος Κωνσταντίνου, Ηράκλειο",
        faq_h="Συχνές ερωτήσεις",
        q1="Χρειάζεται η συσκευή εξωτερική μονάδα;",
        a1="Όχι. Αυτό είναι ακριβώς το μεγαλύτερο πλεονέκτημά της: χωρίς τρύπες, χωρίς άδειες, χωρίς κόστος εγκατάστασης. Λειτουργεί με εσωτερικό κλειστό κύκλωμα. Αρκεί να τη βάλεις πάνω στους τροχούς και να τη συνδέσεις σε κανονική πρίζα.",
        q2="Πόσο καταναλώνει πραγματικά;",
        a2="Το έξυπνο σύστημα ρυθμίζει αυτόματα την ισχύ μεταξύ 370 W και 1800 W. Μόλις φτάσει την επιθυμητή θερμοκρασία, μειώνει την κατανάλωση στο ελάχιστο για να τη διατηρήσει. Διατηρώντας τη θερμοκρασία με μειωμένη ισχύ, καταναλώνει λιγότερο από ό,τι αν λειτουργούσε συνεχώς στο μέγιστο.",
        q3="Τι μέγεθος δωματίου μπορεί να ψύξει;",
        a3="Με 12.000 BTU έχει σχεδιαστεί για χώρους έως περίπου 35 m². Κατάλληλο για σαλόνια, υπνοδωμάτια και γραφεία μεσαίου μεγέθους.",
        q4="Πώς λειτουργεί η πληρωμή στην παράδοση;",
        a4="Συμπληρώνεις τη φόρμα, η ομάδα μας επιβεβαιώνει την παραγγελία και ο διανομέας παραδίδει το δέμα στο σπίτι σου. Η πληρωμή γίνεται μόνο στην παραλαβή, απευθείας στον διανομέα. Χωρίς κανένα ρίσκο.",
        q5="Μπορώ να το επιστρέψω αν δεν μείνει ικανοποιημένος;",
        a5="Φυσικά. Έχεις 60 ημέρες να δοκιμάσεις τη συσκευή. Αν για οποιονδήποτε λόγο δεν μείνεις ικανοποιημένος, οργανώνουμε δωρεάν παραλαβή και επιστρέφουμε την τιμή αγοράς.",
        final_h="Εξασφάλισε την τεχνολογία του μέλλοντος για",
        final_only=" μόλις {now}",
        final_warn="⚠️ Η τιμή καμπάνιας {now_long} ισχύει όσο διαρκεί το απόθεμα.",
        final_sub="Η εκστρατεία εκκαθάρισης τελειώνει όταν εξαντληθεί το απόθεμα.",
        final_cta="🟢 Κάνε κλικ εδώ και ενεργοποίησε την ειδική προσφορά",
        final_trust="Πληρωμή στην παράδοση · Δωρεάν επιστροφή 60 ημέρες · 4 χρόνια εγγύηση",
        foot_blurb="Χρήσιμα προϊόντα για την καθημερινότητα, παράδοση σε 24–48 ώρες με πληρωμή στην παράδοση.",
        foot_info="Πληροφορίες", foot_contact="Επαφή",
        about="Σχετικά με εμάς", contact="Επικοινωνήστε μαζί μας",
        privacy="Πολιτική Απορρήτου", terms="Όροι & Προϋποθέσεις",
        cookies="Πολιτική cookie", ship="Πολιτική Αποστολής", refund="Πολιτική επιστροφής χρημάτων",
        rights="Με επιφύλαξη παντός δικαιώματος",
        ty_title="Η παραγγελία ελήφθη — Περιμένετε την κλήση επιβεβαίωσης | Polar PRO Max",
        ty_desc="Η παραγγελία Polar PRO Max καταχωρίστηκε. Μένει ένα τελευταίο βήμα: απαντήστε στην κλήση επιβεβαίωσης του χειριστή μας.",
        ty_h="Η παραγγελία Polar PRO Max καταχωρίστηκε με επιτυχία!",
        ty_sub="Τέλεια — η παραγγελία επεξεργάζεται. Μένει μόνο <strong>ένα τελευταίο βήμα</strong> για να ολοκληρωθεί και να σταλεί.",
        ty_prod="Polar PRO Max 4 σε 1 — κλιματιστικό στήλης",
        ty_meta="12.000 BTU · Πληρωμή στην παράδοση",
        ty_ey="👇 Τι πρέπει να κάνετε τώρα", ty_ah="📞 Απαντήστε στην κλήση επιβεβαίωσης",
        ty_ap="Ένας χειριστής θα επικοινωνήσει μαζί σας <strong>τις επόμενες ώρες</strong> για να επιβεβαιώσει την παραγγελία Polar PRO Max.",
        ty_aw="Αν δεν απαντήσετε στην κλήση, η παραγγελία ακυρώνεται αυτόματα.",
        ty_hh="🕒 Ώρες επικοινωνίας", ty_hours="Δευτέρα – Σάββατο · 9:00 – 18:00",
        ty_nh="📋 Τι ακολουθεί",
        ty_s1="Απαντήστε στην κλήση και <strong>επιβεβαιώστε τα στοιχεία σας</strong>",
        ty_s2="Το Polar PRO Max θα αποσταλεί σε <strong>24–48 ώρες</strong>",
        ty_s3="Παράδοση στο σπίτι και <strong>πληρωμή στην παράδοση</strong>",
        ty_b1="🔒 Πληρωμή στην παράδοση", ty_b2="🛡️ Εγγύηση 2 έτη", ty_b3="↩️ Επιστροφή 60 ημέρες",
        ty_alt="Polar PRO Max φορητό κλιματιστικό στήλης 4 σε 1",
    ),
    "hu": dict(
        title="Polar PRO Max — Hordozható oszlopklíma 4 az 1-ben | 29 999 Ft",
        description="Polar PRO Max hordozható oszlopklíma 4 az 1-ben. Hűt, fűt, párátlanít és tisztít akár 35 m²-en. Telepítés nélkül. Utánvét. Ma 29 999 Ft 59 998 Ft helyett.",
        cookie_text="Technikai és harmadik féltől származó cookie-kat használunk a élmény javítására és elemzésre.",
        cookie_accept="Elfogadom", cookie_learn="Tudjon meg többet", submitting="Küldés...",
        sticky_cta="Ajánlat aktiválása",
        rating="4,72/5 · Több mint 3 100 ellenőrzött értékelés",
        h1_pre="SZÓ SZERINT ÜRÍTJÜK A RAKTÁRAINKAT:",
        h1_mid="a hordozható oszlopklíma",
        h1_end="ma a tiéd",
        h1_only=" mindössze {now}!",
        sub="A hordozható oszlopklíma, amely 5 perc alatt végez a nyári hővel. Tedd oda, ahová szeretnéd, bedugod a konnektorba, megnyomod az ON gombot, és tiszta, jeges frissességet kapsz. Nincs telepítés, nincs várakozás, házhozszállítás 24 órán belül.",
        img_hero="Wallconvector Pro 4 az 1-ben — hordozható oszlopklíma",
        save="Megtakarítás {now} — 50% kedvezmény",
        scarcity="⚠️ Kiárusítási kampány: a {now} ár addig érvényes, amíg tart a kampány készlete.",
        cta_hero="Ajánlat aktiválása — rendeljen most",
        trust="Utánvét · Ingyenes szállítás · 4 év garancia",
        order_h="Kampánykészlet", order_hl=" korlátozott ", order_h2="— foglalja le a sajátját",
        order_p="Töltse ki az űrlapot. A rendelést azonnal feldolgozzuk.",
        card_title="ADD MEG A SZÁLLÍTÁSI ADATOKAT",
        card_sub="A rendelés azonnal elindul. Csak átvételkor fizetsz, közvetlenül a futárnak.",
        progress="KAMPÁNY AKTÍV",
        progress_note="A kampányár a készlet erejéig érvényes",
        pill="Utánvét elérhető",
        label_name="Keresztnév Vezetéknév*", label_addr="Cím*", label_tel="Telefon*",
        btn="Rendeljen most",
        form_note="🔒 Nincs előleg · Fizetés átvételkor · Szállítás 24/48 óra",
        feat_h="Nem egy sima ventilátor.",
        feat_h2=" Hordozható 4 az 1-ben rendszer, amelyhez nincs szükség felújításra és kültéri egységre",
        feat_lead="Legújabb generációs, 12.000 BTU-s multifunkciós hordozható rendszer. A kerekeknek köszönhetően szobáról szobára vihető. Hűt, fűt, párátlanít és szűri a levegőt akár 35 m²-es helyiségekben, percek alatt.",
        f1h="HŰT", f1p="Percen belül akár 16 °C-ra csökkenti a hőmérsékletet. Erős teljesítmény az egész térre.",
        f2h="FŰT", f2p="Télen akár 42 °C-ra emeli a hőmérsékletet. Vége a fázásnak és a csillagászati számláknak.",
        f3h="PÁRÁTLANÍT", f3p="Eltávolítja a felesleges nedvességet. Viszlát penész, viszlát nehéz levegő. Egészséges, kényelmes otthon.",
        f4h="TISZTÍT", f4p="Beépített HEPA szűrő: megköti a port és a lebegő részecskéket.",
        secret_h="A titok, amit a hagyományos klímagyártók nem akarnak, hogy tudj",
        secret_p1="Miért fizess szerelőt, kérj engedélyt a társasháztól, és akassz egy csúnya, zajos dobozt az ablakon kívülre?",
        secret_p2="Az oszlopos Polar PRO Max ",
        secret_strong="NEM IGÉNYEL KÜLTÉRI EGYSÉGET",
        secret_p3=". Belső, zárt ciklusú motort használ. A csendes kerekekkel bármelyik szobába teheted, bedugod a konnektorba, és azonnal kész. ",
        secret_zero="Nulla telepítés, nulla karbantartás, nulla extra költség.",
        d1h="KONTROLLÁLT FOGYASZTÁS", d1p="A rendszer szabályozza a teljesítményt, és a beállított hőmérséklet elérése után készenléti módba lép — csak annyit fogyaszt, amennyi kell.",
        d2h="TISZTÁBB LEVEGŐ", d2p="A beépített HEPA szűrő megköti a port és a helyiségben lebegő részecskéket.",
        d3h="NULLA ZAJ", d3p="Az ultranéma éjszakai mód lehetővé teszi az alvást a régi készülékek zümmögése nélkül.",
        img_tech="Polar PRO Max — hordozható oszlopklíma kültéri egység nélkül",
        specs="MŰSZAKI ADATOK",
        r_pow="Teljesítmény", r_cov="Lefedettség", r_eco="Takarékos mód", r_con="Fogyasztás",
        r_reg="Szabályozás", r_out="Kültéri egység", r_noi="Zajszint", r_fil="Szűrő",
        r_ctl="Vezérlés", r_war="Garancia",
        v_pow="12.000 BTU", v_cov="Akár 35 m²", v_eco="Termosztát + automatikus készenlét",
        v_con="370 W-tól 1800 W-ig (moduláló)", v_reg="Automatikus moduláló teljesítmény",
        v_out="NEM SZÜKSÉGES", v_noi="Ultranéma (éjszakai mód)", v_fil="Mosható HEPA",
        v_ctl="LCD távirányító + távoli app", v_war="2 év gyártói garancia",
        cta_price="🟢 Rendelje meg most {now}-ért",
        incl_h="Mit kapsz ma ebben az árban:",
        i1="Polar PRO Max 4 az 1-ben hordozható oszlopklíma",
        i2="Multifunkciós LCD távirányító",
        i3="Csendes kerékkészlet a könnyű mozgatáshoz",
        i4="Magyar nyelvű használati útmutató",
        i5="Okos vezérlés távoli alkalmazáson keresztül",
        i6="Gyártói garancia 2 évre meghosszabbítva",
        today="CSAK MA",
        i7="Ingyenes visszaküldés 60 napon belül, azonnali visszatérítéssel",
        reviews_avg="Magyarországi ügyfeleink ellenőrzött értékeléseinek átlaga",
        rev1_alt="Polar PRO Max a nappaliban",
        rev1_h="Nagy elvárások nélkül vettem",
        rev1_p="„Az ár miatt haboztam. Délután a nappaliban használom, és a különbség érezhető. A számla a korábbi hónapokhoz hasonló maradt. Gyors szállítás, a futárnak fizettem.”",
        rev1_n="— Kovács Péter, Debrecen",
        rev2_alt="Polar PRO Max a hálószobában",
        rev2_h="A zaj volt a legnagyobb félelmem",
        rev2_p="„Könnyű álmom van, és már lemondtam az ilyen készülékekről. Éjszakai módban alig hallani. Kivettem a dobozból, bedugtam, és senkit sem kellett hívnom.”",
        rev2_n="— Szabó Anna, Szeged",
        rev3_alt="Polar PRO Max kerekeken mozgatva",
        rev3_h="Szobáról szobára viszem",
        rev3_p="„A napszaktól függően a dolgozó és a hálószoba között tologatom. A kerekek segítenek, semmit sem kell szétszedni. Az árához képest elégedett vagyok a kidolgozással.”",
        rev3_n="— Nagy Gábor, Győr",
        faq_h="Gyakori kérdések",
        q1="Szüksége van a készüléknek kültéri egységre?",
        a1="Nem. Pont ez a legnagyobb előnye: nincs fúrás, nincs engedély, nincs telepítési költség. Belső zárt körrel működik. Elég kerekekre tenni és egy sima konnektorba dugni.",
        q2="Mennyit fogyaszt valójában?",
        a2="Az okos rendszer automatikusan 370 W és 1800 W között szabályozza a teljesítményt. Amint eléri a kívánt hőmérsékletet, a fogyasztást a minimumra csökkenti. Csökkentett teljesítménnyel tartva a hőfokot kevesebbet fogyaszt, mintha mindig maximumon menne.",
        q3="Mekkora szobát tud lehűteni?",
        a3="12.000 BTU-val körülbelül 35 m²-es helyiségekre tervezték. Nappalikhoz, hálószobákhoz és közepes irodákhoz alkalmas.",
        q4="Hogyan működik az utánvét?",
        a4="Kitöltöd az űrlapot, csapatunk megerősíti a rendelést, a futár házhoz viszi a csomagot. Fizetni csak átvételkor kell, közvetlenül a futárnak. Teljesen kockázatmentes.",
        q5="Visszaküldhetem, ha nem vagyok elégedett?",
        a5="Persze. 60 napod van kipróbálni a készüléket. Ha bármilyen okból nem vagy elégedett, ingyenes elszállítást szervezünk, és visszatérítjük a vételárat.",
        final_h="Biztosítsd a jövő technológiáját",
        final_only=" mindössze {now}-ért",
        final_warn="⚠️ A {now_long} kampányár a készlet erejéig érvényes.",
        final_sub="A kiárusítás akkor ér véget, amikor elfogy a készlet.",
        final_cta="🟢 Kattints ide és aktiváld a különleges ajánlatot",
        final_trust="Utánvét · Ingyenes 60 napos visszaküldés · 4 év garancia",
        foot_blurb="Hasznos termékek a mindennapokra, 24–48 órás szállítás utánvéttel.",
        foot_info="Információ", foot_contact="Kapcsolat",
        about="Rólunk", contact="Kapcsolat",
        privacy="Adatvédelmi szabályzat", terms="Általános szerződési feltételek",
        cookies="Cookie szabályzat", ship="Szállítási szabályzat", refund="Visszatérítési szabályzat",
        rights="Minden jog fenntartva",
        ty_title="Rendelés rögzítve — Várja a visszaigazoló hívást | Polar PRO Max",
        ty_desc="Polar PRO Max rendelése rögzítve. Már csak egy lépés van hátra: vegye fel a visszaigazoló hívást.",
        ty_h="Polar PRO Max rendelését sikeresen rögzítettük!",
        ty_sub="Tökéletes — a rendelés feldolgozás alatt. Már csak <strong>egy utolsó lépés</strong> kell a teljesítéshez és a szállítás indításához.",
        ty_prod="Polar PRO Max 4 az 1-ben — oszlopklíma",
        ty_meta="12.000 BTU · Utánvét",
        ty_ey="👇 Mit kell tennie most", ty_ah="📞 Vegye fel a visszaigazoló hívást",
        ty_ap="Operátorunk <strong>a következő órákban</strong> felhívja, hogy megerősítse a Polar PRO Max rendelést.",
        ty_aw="Ha nem veszi fel a hívást, a rendelés automatikusan törlődik.",
        ty_hh="🕒 Elérhetőség", ty_hours="Hétfő – Szombat · 9:00 – 18:00",
        ty_nh="📋 Mi történik ezután",
        ty_s1="Vegye fel a hívást és <strong>erősítse meg az adatait</strong>",
        ty_s2="Polar PRO Max készülékét <strong>24–48 órán belül</strong> feladjuk",
        ty_s3="Házhozszállítás és <strong>utánvét</strong>",
        ty_b1="🔒 Utánvét", ty_b2="🛡️ 2 év garancia", ty_b3="↩️ 60 napos visszaküldés",
        ty_alt="Polar PRO Max hordozható oszlopklíma 4 az 1-ben",
    ),
    "it": dict(
        title="Polar PRO Max — Condizionatore portatile a colonna 4 in 1 | 69 €",
        description="Condizionatore portatile a colonna Polar PRO Max 4 in 1. Raffredda, riscalda, deumidifica e purifica fino a 35 m². Senza installazione. Pagamento alla consegna. Oggi 69 € invece di 138 €.",
        cookie_text="Usiamo cookie tecnici e di terze parti per migliorare la tua esperienza e per analisi.",
        cookie_accept="Accetta", cookie_learn="Scopri di più", submitting="Invio...",
        sticky_cta="Attiva l'offerta",
        rating="4,72/5 · Oltre 3 100 recensioni verificate",
        h1_pre="STIAMO LETTERALMENTE SVUOTANDO I MAGAZZINI:",
        h1_mid="il condizionatore portatile a colonna da",
        h1_end="oggi è tuo a",
        h1_only=" soli {now}!",
        sub="Il condizionatore portatile a colonna che spegne il caldo estivo in 5 minuti. Mettilo dove vuoi, spina nella presa, premi ON e arriva una raffica di fresco purificato e gelato. Zero installazione, zero attesa, consegna a domicilio in 24 ore.",
        img_hero="Wallconvector Pro 4 in 1 — condizionatore portatile a colonna",
        save="Risparmi {now} — sconto del 50%",
        scarcity="⚠️ Campagna di liquidazione: il prezzo di {now} vale fino a esaurimento scorte di questa campagna.",
        cta_hero="Attiva l'offerta — ordina ora",
        trust="Pagamento alla consegna · Spedizione gratuita · 4 anni di garanzia",
        order_h="Scorte della campagna", order_hl=" limitate ", order_h2="— prenota il tuo",
        order_p="Compila il modulo. Il tuo ordine verrà elaborato subito.",
        card_title="INSERISCI I DATI DI CONSEGNA",
        card_sub="L'ordine parte subito. Paghi solo alla consegna, direttamente al corriere.",
        progress="CAMPAGNA ATTIVA",
        progress_note="Prezzo campagna valido fino a esaurimento scorte",
        pill="Pagamento alla consegna disponibile",
        label_name="Nome e Cognome*", label_addr="Indirizzo*", label_tel="Telefono*",
        btn="Acquista ora",
        form_note="🔒 Nessun anticipo · Paghi alla consegna · Spedizione 24/48 h",
        feat_h="Non è un semplice ventilatore.",
        feat_h2=" È un sistema portatile 4 in 1 che non richiede lavori né unità esterna",
        feat_lead="Sistema multifunzione portatile 4 in 1 di ultima generazione da 12.000 BTU. Si sposta da una stanza all'altra grazie alle ruote. Raffredda, riscalda, deumidifica e filtra l'aria in ambienti fino a 35 m², in pochi minuti.",
        f1h="RAFFREDDA", f1p="Abbassa la temperatura fino a 16 °C in pochi minuti. Potenza forte per tutto l'ambiente.",
        f2h="RISCALDA", f2p="In inverno alza la temperatura fino a 42 °C. Fine al freddo e alle bollette astronomiche.",
        f3h="DEUMIDIFICA", f3p="Elimina l'umidità in eccesso. Addio muffa, addio aria pesante. Casa sana e confortevole.",
        f4h="PURIFICA", f4p="Filtro HEPA integrato: trattiene polvere e particelle in sospensione.",
        secret_h="Il segreto che i produttori di condizionatori tradizionali non vogliono che tu sappia",
        secret_p1="Perché pagare un installatore, chiedere il permesso al condominio e appendere una cassa brutta e rumorosa fuori dalla finestra?",
        secret_p2="Il nostro Polar PRO Max a colonna ",
        secret_strong="NON HA UNITÀ ESTERNA",
        secret_p3=". Usa un motore interno a ciclo chiuso continuo. Lo metti in qualsiasi stanza grazie alle ruote silenziose, lo innesti alla presa ed è pronto. ",
        secret_zero="Zero installazione, zero manutenzione, zero costi extra.",
        d1h="CONSUMO CONTROLLATO", d1p="Il sistema regola la potenza e entra in stand-by appena raggiunge la temperatura impostata, consumando solo il necessario.",
        d2h="ARIA PIÙ PULITA", d2p="Il filtro HEPA integrato trattiene polvere e particelle in sospensione nella stanza.",
        d3h="ZERO RUMORE", d3p="La modalità notte ultra-silenziosa permette di dormire senza il ronzio dei vecchi apparecchi.",
        img_tech="Polar PRO Max — condizionatore portatile a colonna senza unità esterna",
        specs="DATI TECNICI",
        r_pow="Potenza", r_cov="Copertura", r_eco="Modalità eco", r_con="Consumo",
        r_reg="Regolazione", r_out="Unità esterna", r_noi="Livello di rumore", r_fil="Filtro",
        r_ctl="Controllo", r_war="Garanzia",
        v_pow="12.000 BTU", v_cov="Fino a 35 m²", v_eco="Termostato + standby automatico",
        v_con="Da 370 W a 1800 W (modulante)", v_reg="Potenza modulante automatica",
        v_out="NON NECESSARIA", v_noi="Ultra-silenzioso (modalità notte)", v_fil="HEPA lavabile",
        v_ctl="Telecomando LCD + app a distanza", v_war="2 anni di garanzia del produttore",
        cta_price="🟢 Ordina ora a {now}",
        incl_h="Cosa ricevi oggi incluso nel prezzo di",
        i1="Unità portatile a colonna Polar PRO Max 4 in 1",
        i2="Telecomando LCD multifunzione",
        i3="Kit ruote silenziose per spostarlo facilmente",
        i4="Manuale di istruzioni in italiano",
        i5="Controllo smart tramite app a distanza",
        i6="Garanzia del produttore estesa a 2 anni",
        today="SOLO OGGI",
        i7="Reso gratuito in 60 giorni con rimborso immediato",
        reviews_avg="Media delle recensioni verificate dei nostri clienti in Italia",
        rev1_alt="Polar PRO Max in soggiorno",
        rev1_h="L'ho comprato senza grandi aspettative",
        rev1_p="“Dubitavo per il prezzo. Lo uso in soggiorno a fine pomeriggio e la differenza si sente. La bolletta è restata in linea con i mesi precedenti. Consegna rapida e ho pagato al corriere.”",
        rev1_n="— Luca Bianchi, Bologna",
        rev2_alt="Polar PRO Max in camera",
        rev2_h="Il rumore era la mia paura più grande",
        rev2_p="“Ho il sonno leggero e avevo già mollato questi apparecchi. In modalità notte quasi non si sente. L'ho tirato fuori dalla scatola, messo in presa e ha funzionato senza chiamare nessuno.”",
        rev2_n="— Giulia Conti, Torino",
        rev3_alt="Polar PRO Max spostato sulle ruote",
        rev3_h="Lo porto da una stanza all'altra",
        rev3_p="“Lo sposto tra lo studio e la camera a seconda dell'ora. Le ruote aiutano e non smonto niente. Per quello che è costato, sono soddisfatto delle finiture.”",
        rev3_n="— Marco Ferrari, Bari",
        faq_h="Domande frequenti",
        q1="L'apparecchio ha bisogno di un'unità esterna?",
        a1="No. È proprio il suo vantaggio più grande: niente fori, niente permessi, niente costi di installazione. Funziona con un circuito chiuso interno. Basta metterlo sulle ruote e collegarlo a una presa normale.",
        q2="Quanto consuma davvero?",
        a2="Il sistema intelligente regola automaticamente la potenza tra 370 W e 1800 W. Appena raggiunge la temperatura desiderata, riduce il consumo al minimo per mantenerla. Tenendo la temperatura a potenza ridotta, consuma meno che se girasse sempre al massimo.",
        q3="Che dimensione di stanza riesce a raffreddare?",
        a3="Con 12.000 BTU è pensato per ambienti fino a circa 35 m². Va bene per soggiorni, camere e uffici di medie dimensioni.",
        q4="Come funziona il pagamento alla consegna?",
        a4="Compili il modulo, il nostro team conferma l'ordine e il corriere consegna il pacco a casa tua. Il pagamento avviene solo al ritiro, direttamente al corriere. Completamente senza rischi.",
        q5="Posso restituirlo se non resto soddisfatto?",
        a5="Certo. Hai 60 giorni per provare l'apparecchio. Se per qualsiasi motivo non resti soddisfatto, organizziamo il ritiro gratuito e rimborsiamo il prezzo di acquisto.",
        final_h="Assicurati la tecnologia del futuro a",
        final_only=" soli {now}",
        final_warn="⚠️ Il prezzo campagna di {now_long} vale finché durano le scorte.",
        final_sub="La campagna di liquidazione termina quando finisce lo stock.",
        final_cta="🟢 Clicca qui e attiva l'offerta speciale",
        final_trust="Pagamento alla consegna · Reso gratuito 60 giorni · 4 anni di garanzia",
        foot_blurb="Prodotti utili per la vita quotidiana, consegna in 24–48 ore con pagamento alla consegna.",
        foot_info="Informazioni", foot_contact="Contatti",
        about="Chi siamo", contact="Contattaci",
        privacy="Privacy Policy", terms="Termini e Condizioni",
        cookies="Cookie Policy", ship="Politica di spedizione", refund="Politica di reso",
        rights="Tutti i diritti riservati",
        ty_title="Ordine ricevuto — Attendi la chiamata di conferma | Polar PRO Max",
        ty_desc="Il tuo ordine Polar PRO Max è stato registrato. Manca solo un ultimo passaggio: rispondi alla chiamata di conferma del nostro operatore.",
        ty_h="Il tuo ordine Polar PRO Max è stato registrato con successo!",
        ty_sub="Perfetto — l'ordine è in elaborazione. Manca solo <strong>un ultimo passaggio</strong> per completarlo e spedirlo.",
        ty_prod="Polar PRO Max 4 in 1 — condizionatore a colonna",
        ty_meta="12.000 BTU · Pagamento alla consegna",
        ty_ey="👇 Cosa devi fare adesso", ty_ah="📞 Rispondi alla chiamata di conferma",
        ty_ap="Un operatore ti contatterà <strong>nelle prossime ore</strong> per confermare l'ordine Polar PRO Max.",
        ty_aw="Se non rispondi alla chiamata, l'ordine verrà automaticamente annullato.",
        ty_hh="🕒 Orari di contatto", ty_hours="Lunedì – Sabato · 9:00 – 18:00",
        ty_nh="📋 Cosa succede dopo",
        ty_s1="Rispondi alla chiamata e <strong>conferma i tuoi dati</strong>",
        ty_s2="Il tuo Polar PRO Max verrà spedito entro <strong>24–48 ore</strong>",
        ty_s3="Consegna a domicilio e <strong>pagamento alla consegna</strong>",
        ty_b1="🔒 Pagamento alla consegna", ty_b2="🛡️ Garanzia 2 anni", ty_b3="↩️ Reso 60 giorni",
        ty_alt="Polar PRO Max condizionatore portatile a colonna 4 in 1",
    ),
    "pt": dict(
        title="Polar PRO Max — Ar condicionado portátil de coluna 4 em 1 | 79 €",
        description="Ar condicionado portátil de coluna Polar PRO Max 4 em 1. Arrefece, aquece, desumidifica e purifica até 35 m². Sem instalação. Pagamento na entrega. Hoje 79 € em vez de 158 €.",
        cookie_text="Usamos cookies técnicos e de terceiros para melhorar a sua experiência e para análises.",
        cookie_accept="Aceitar", cookie_learn="Saber mais", submitting="A enviar...",
        sticky_cta="Ativa a oferta",
        rating="4,72/5 · Mais de 3 100 avaliações verificadas",
        h1_pre="ESTAMOS LITERALMENTE A ESVAZIAR OS NOSSOS ARMAZÉNS:",
        h1_mid="o ar condicionado portátil de coluna de",
        h1_end="hoje é teu por",
        h1_only=" apenas {now}!",
        sub="O ar condicionado portátil de coluna que acaba com o calor do verão em 5 minutos. Coloca-o onde quiseres, liga-o à tomada, carrega em ON e recebe uma rajada de frescura purificada e gelada. Sem instalação, sem espera, entrega ao domicílio em 24 horas.",
        img_hero="Wallconvector Pro 4 em 1 — ar condicionado portátil de coluna",
        save="Poupa {now} — desconto de 50%",
        scarcity="⚠️ Campanha de liquidação: o preço de {now} é válido até esgotar o stock desta campanha.",
        cta_hero="Ativa a oferta — encomenda agora",
        trust="Pagamento na entrega · Envio gratuito · 4 anos de garantia",
        order_h="Stock de campanha", order_hl=" limitado ", order_h2="— reserva já o teu",
        order_p="Preenche o formulário. A tua encomenda será processada imediatamente.",
        card_title="INTRODUZ OS DADOS DE ENTREGA",
        card_sub="A tua encomenda será enviada imediatamente. Só pagas na entrega, diretamente ao estafeta.",
        progress="CAMPANHA ATIVA",
        progress_note="Preço de campanha válido até esgotar o stock",
        pill="Pagamento na entrega disponível",
        label_name="Nome Sobrenome*", label_addr="Endereço*", label_tel="Telefone*",
        btn="Encomendar agora",
        form_note="🔒 Sem adiantamento · Paga na entrega · Envio 24/48 h",
        feat_h="Não é uma simples ventoinha.",
        feat_h2=" É um sistema portátil 4 em 1 que dispensa obras e unidade exterior",
        feat_lead="Sistema multifunções portátil 4 em 1 de última geração com 12 000 BTU. Desloca-se de uma divisão para outra graças às rodas. Arrefece, aquece, desumidifica e filtra o ar em divisões até 35 m², em poucos minutos.",
        f1h="ARREFECE", f1p="Baixa a temperatura até 16 °C em poucos minutos. Potência forte para todo o ambiente.",
        f2h="AQUECE", f2p="No inverno, aumenta a temperatura até 42 °C. Acaba com o frio e com contas astronómicas.",
        f3h="DESUMIDIFICA", f3p="Elimina a humidade em excesso. Adeus bolor, adeus ar pesado. Casa saudável e confortável.",
        f4h="PURIFICA", f4p="Filtro HEPA integrado: retém pó e partículas em suspensão no ar.",
        secret_h="O segredo que os fabricantes de ar condicionado tradicionais não querem que saibas",
        secret_p1="Porque haverias de pagar a um instalador, pedir autorização ao condomínio e pendurar uma caixa feia e barulhenta fora da janela?",
        secret_p2="O nosso Polar PRO Max de coluna ",
        secret_strong="NÃO TEM UNIDADE EXTERIOR",
        secret_p3=". Utiliza um motor interno de ciclo fechado contínuo. Coloca-o em qualquer divisão graças às rodas silenciosas, liga-o à tomada e fica logo pronto. ",
        secret_zero="Zero instalação, zero manutenção, zero custos extra.",
        d1h="CONSUMO CONTROLADO", d1p="O sistema regula a potência e entra em modo de espera assim que atinge a temperatura definida, consumindo apenas o necessário.",
        d2h="AR MAIS LIMPO", d2p="O filtro HEPA integrado retém pó e partículas em suspensão no ar da divisão.",
        d3h="ZERO RUÍDO", d3p="O modo noturno ultra-silencioso permite dormir sem o zumbido incómodo dos aparelhos antigos.",
        img_tech="Polar PRO Max — ar condicionado portátil de coluna sem unidade exterior",
        specs="DADOS TÉCNICOS",
        r_pow="Potência", r_cov="Cobertura", r_eco="Modo económico", r_con="Consumo",
        r_reg="Regulação", r_out="Unidade exterior", r_noi="Nível de ruído", r_fil="Filtro",
        r_ctl="Controlo", r_war="Garantia",
        v_pow="12.000 BTU", v_cov="Até 35 m²", v_eco="Termóstato + standby automático",
        v_con="De 370 W a 1800 W (modulante)", v_reg="Potência modulante automática",
        v_out="NÃO NECESSÁRIA", v_noi="Ultra-silencioso (modo noturno)", v_fil="HEPA lavável",
        v_ctl="Comando LCD + app à distância", v_war="2 anos de garantia do fabricante",
        cta_price="🟢 Encomenda agora por {now}",
        incl_h="O que recebes hoje incluído no preço de",
        i1="Unidade portátil de coluna Polar PRO Max 4 em 1",
        i2="Comando LCD multifunções",
        i3="Kit de rodas silenciosas para deslocar facilmente",
        i4="Manual de instruções em português",
        i5="Controlo inteligente através da app à distância",
        i6="Garantia do fabricante alargada para 2 anos",
        today="SÓ HOJE",
        i7="Devolução gratuita em 60 dias com reembolso imediato",
        reviews_avg="Média das avaliações verificadas dos nossos clientes em Portugal",
        rev1_alt="Polar PRO Max na sala",
        rev1_h="Comprei sem grandes expectativas",
        rev1_p="“Duvidava por causa do preço. Uso-o na sala ao fim da tarde e a diferença nota-se bem. A fatura manteve-se em linha com os meses anteriores. Entrega rápida e paguei ao estafeta.”",
        rev1_n="— Rui Cardoso, Setúbal",
        rev2_alt="Polar PRO Max no quarto",
        rev2_h="O ruído era o meu maior receio",
        rev2_p="“Tenho o sono leve e já tinha desistido destes aparelhos. No modo noturno mal se ouve. Tirei-o da caixa, liguei à tomada e ficou a funcionar sem chamar ninguém.”",
        rev2_n="— Marta Figueiredo, Braga",
        rev3_alt="Polar PRO Max deslocado sobre rodas",
        rev3_h="Levo-o de divisão em divisão",
        rev3_p="“Ando com ele entre o escritório e o quarto conforme a hora do dia. As rodas ajudam e não preciso de desmontar nada. Pelo que custou, estou satisfeito com os acabamentos.”",
        rev3_n="— Nuno Teixeira, Aveiro",
        faq_h="Perguntas frequentes",
        q1="O aparelho precisa de uma unidade exterior?",
        a1="Não. Esse é precisamente o seu maior benefício: sem furos, sem autorizações, sem custos de instalação. Funciona com um circuito fechado interno. Basta colocá-lo sobre as rodas e ligá-lo a uma tomada normal.",
        q2="Quanto consome realmente?",
        a2="O sistema inteligente regula automaticamente a potência entre 370 W e 1800 W. Assim que atinge a temperatura desejada, reduz o consumo ao mínimo para a manter constante. Ao manter a temperatura com potência reduzida, consome menos do que se funcionasse sempre no máximo.",
        q3="Que tamanho de divisão consegue arrefecer?",
        a3="Com 12 000 BTU, foi concebido para divisões até cerca de 35 m². É adequado para salas, quartos e escritórios de dimensão média.",
        q4="Como funciona o pagamento na entrega?",
        a4="Preenches o formulário, a nossa equipa confirma a encomenda e o estafeta entrega a embalagem diretamente em tua casa. O pagamento é feito apenas no recebimento, diretamente ao estafeta. Totalmente sem riscos.",
        q5="Posso devolvê-lo se não ficar satisfeito?",
        a5="Claro. Tens 60 dias para experimentar o aparelho. Se por qualquer motivo não ficares satisfeito, organizamos a recolha gratuita e reembolsamos o preço de compra.",
        final_h="Garante a tecnologia do futuro por",
        final_only=" apenas {now}",
        final_warn="⚠️ O preço de campanha de {now_long} é válido enquanto durar o stock.",
        final_sub="A campanha de liquidação termina quando o stock esgotar.",
        final_cta="🟢 Clica aqui e ativa a oferta especial",
        final_trust="Pagamento na entrega · Devolução gratuita em 60 dias · 4 anos de garantia",
        foot_blurb="Produtos úteis para o dia a dia, entrega em 24–48 horas com pagamento à cobrança.",
        foot_info="Informação", foot_contact="Contacto",
        about="Sobre nós", contact="Contacte-nos",
        privacy="Política de Privacidade", terms="Termos e Condições",
        cookies="Política de Cookies", ship="Política de envio", refund="Política de reembolso",
        rights="Todos os direitos reservados",
        ty_title="Encomenda recebida — Aguarde a chamada de confirmação | Polar PRO Max",
        ty_desc="A sua encomenda Polar PRO Max foi registada. Falta apenas um último passo: atenda a chamada de confirmação do nosso operador.",
        ty_h="A sua encomenda Polar PRO Max foi registada com sucesso!",
        ty_sub="Perfeito — a encomenda está a ser processada. Falta só <strong>um último passo</strong> para a concluir e enviar.",
        ty_prod="Polar PRO Max 4 em 1 — ar condicionado de coluna",
        ty_meta="12.000 BTU · Pagamento à cobrança",
        ty_ey="👇 O que deve fazer agora", ty_ah="📞 Atenda a chamada de confirmação",
        ty_ap="Um operador vai contactá-lo <strong>nas próximas horas</strong> para confirmar a encomenda Polar PRO Max.",
        ty_aw="Se não atender a chamada, a encomenda será cancelada automaticamente.",
        ty_hh="🕒 Horário de contacto", ty_hours="Segunda – Sábado · 9:00 – 18:00",
        ty_nh="📋 O que acontece a seguir",
        ty_s1="Atenda a chamada e <strong>confirme os seus dados</strong>",
        ty_s2="O seu Polar PRO Max será enviado em <strong>24–48 horas</strong>",
        ty_s3="Entrega ao domicílio e <strong>pagamento à cobrança</strong>",
        ty_b1="🔒 Pagamento à cobrança", ty_b2="🛡️ Garantia 2 anos", ty_b3="↩️ Devolução 60 dias",
        ty_alt="Polar PRO Max ar condicionado portátil de coluna 4 em 1",
    ),
    "ro": dict(
        title="Polar PRO Max — Aer condiționat portabil pe coloană 4 în 1 | 379 lei",
        description="Aer condiționat portabil pe coloană Polar PRO Max 4 în 1. Răcește, încălzește, dezumidifică și purifică până la 35 m². Fără instalare. Plata ramburs. Azi 379 lei în loc de 758 lei.",
        cookie_text="Folosim cookie-uri tehnice și de terți pentru a îmbunătăți experiența ta și pentru analiză.",
        cookie_accept="Acceptă", cookie_learn="Află mai multe", submitting="Se trimite...",
        sticky_cta="Activează oferta",
        rating="4,72/5 · Peste 3 100 de recenzii verificate",
        h1_pre="GOLIM LA PROPRIU DEPOZITELE:",
        h1_mid="aerul condiționat portabil pe coloană de",
        h1_end="astăzi e al tău la",
        h1_only=" doar {now}!",
        sub="Aerul condiționat portabil pe coloană care termină cu căldura verii în 5 minute. Pune-l unde vrei, bagă-l în priză, apasă ON și primești o rafală de prospețime purificată și rece. Fără instalare, fără așteptare, livrare la domiciliu în 24 de ore.",
        img_hero="Wallconvector Pro 4 în 1 — aer condiționat portabil pe coloană",
        save="Economisești {now} — reducere 50%",
        scarcity="⚠️ Campanie de lichidare: prețul de {now} este valabil până se epuizează stocul acestei campanii.",
        cta_hero="Activează oferta — comandă acum",
        trust="Plata ramburs · Livrare gratuită · 4 ani garanție",
        order_h="Stoc de campanie", order_hl=" limitat ", order_h2="— rezervă-l pe al tău",
        order_p="Completează formularul. Comanda ta va fi procesată imediat.",
        card_title="INTRODU DATELE DE LIVRARE",
        card_sub="Comanda pleacă imediat. Plătești doar la livrare, direct curierului.",
        progress="CAMPANIE ACTIVĂ",
        progress_note="Prețul de campanie este valabil până la epuizarea stocului",
        pill="Plata ramburs disponibilă",
        label_name="Nume și prenume*", label_addr="Adresa*", label_tel="Telefon*",
        btn="Comandă acum",
        form_note="🔒 Fără avans · Plătești la livrare · Expediere 24/48 h",
        feat_h="Nu e un simplu ventilator.",
        feat_h2=" Este un sistem portabil 4 în 1 care nu cere lucrări și nici unitate exterioară",
        feat_lead="Sistem multifuncțional portabil 4 în 1 de ultimă generație cu 12.000 BTU. Se mută dintr-o încăpere în alta grație rotițelor. Răcește, încălzește, dezumidifică și filtrează aerul în camere de până la 35 m², în câteva minute.",
        f1h="RĂCEȘTE", f1p="Scade temperatura până la 16 °C în câteva minute. Putere puternică pentru tot ambientul.",
        f2h="ÎNCĂLZEȘTE", f2p="Iarna, crește temperatura până la 42 °C. Gata cu frigul și cu facturile astronomice.",
        f3h="DEZUMIDIFICĂ", f3p="Elimină umiditatea în exces. Adio mucegai, adio aer greu. Casă sănătoasă și confortabilă.",
        f4h="PURIFICĂ", f4p="Filtru HEPA integrat: reține praful și particulele în suspensie.",
        secret_h="Secretul pe care producătorii de aer condiționat clasic nu vor să-l știi",
        secret_p1="De ce ai plăti un instalator, ai cere acordul asociației și ai agăța o cutie urâtă și zgomotoasă în afara ferestrei?",
        secret_p2="Polar PRO Max pe coloană ",
        secret_strong="NU ARE UNITATE EXTERIOARĂ",
        secret_p3=". Folosește un motor intern cu ciclu închis continuu. Îl pui în orice cameră grație rotițelor silențioase, îl bagi în priză și e gata. ",
        secret_zero="Zero instalare, zero întreținere, zero costuri extra.",
        d1h="CONSUM CONTROLAT", d1p="Sistemul reglează puterea și trece în standby imediat ce atinge temperatura setată, consumând doar cât e nevoie.",
        d2h="AER MAI CURAT", d2p="Filtrul HEPA integrat reține praful și particulele în suspensie din cameră.",
        d3h="ZERO ZGOMOT", d3p="Modul noapte ultra-silențios permite somnul fără zumzetul aparatelor vechi.",
        img_tech="Polar PRO Max — aer condiționat portabil pe coloană fără unitate exterioară",
        specs="DATE TEHNICE",
        r_pow="Putere", r_cov="Acoperire", r_eco="Mod economic", r_con="Consum",
        r_reg="Reglare", r_out="Unitate exterioară", r_noi="Nivel de zgomot", r_fil="Filtru",
        r_ctl="Control", r_war="Garanție",
        v_pow="12.000 BTU", v_cov="Până la 35 m²", v_eco="Termostat + standby automat",
        v_con="De la 370 W la 1800 W (modulant)", v_reg="Putere modulantă automată",
        v_out="NU ESTE NECESARĂ", v_noi="Ultra-silențios (mod noapte)", v_fil="HEPA lavabil",
        v_ctl="Telecomandă LCD + aplicație la distanță", v_war="2 ani garanție de la producător",
        cta_price="🟢 Comandă acum la {now}",
        incl_h="Ce primești astăzi inclus în prețul de",
        i1="Unitate portabilă pe coloană Polar PRO Max 4 în 1",
        i2="Telecomandă LCD multifuncțională",
        i3="Kit de rotițe silențioase pentru mutare ușoară",
        i4="Manual de instrucțiuni în română",
        i5="Control inteligent prin aplicația la distanță",
        i6="Garanție de producător extinsă la 2 ani",
        today="DOAR AZI",
        i7="Returnare gratuită în 60 de zile cu rambursare imediată",
        reviews_avg="Media recenziilor verificate ale clienților noștri din România",
        rev1_alt="Polar PRO Max în living",
        rev1_h="L-am cumpărat fără așteptări mari",
        rev1_p="„Eram sceptic din cauza prețului. Îl folosesc în living seara și diferența se simte. Factura a rămas în linie cu lunile anterioare. Livrare rapidă și am plătit curierului.”",
        rev1_n="— Andrei Popescu, Cluj-Napoca",
        rev2_alt="Polar PRO Max în dormitor",
        rev2_h="Zgomotul era cea mai mare teamă a mea",
        rev2_p="„Am somnul ușor și deja renunțasem la aceste aparate. În modul noapte abia se aude. L-am scos din cutie, l-am băgat în priză și a funcționat fără să sun pe nimeni.”",
        rev2_n="— Elena Ionescu, Iași",
        rev3_alt="Polar PRO Max mutat pe rotițe",
        rev3_h="Îl duc din cameră în cameră",
        rev3_p="„Îl mut între birou și dormitor în funcție de oră. Rotițele ajută și nu demontez nimic. Pentru cât a costat, sunt mulțumit de finisaje.”",
        rev3_n="— Mihai Stan, Timișoara",
        faq_h="Întrebări frecvente",
        q1="Aparatul are nevoie de o unitate exterioară?",
        a1="Nu. Acesta este tocmai cel mai mare avantaj: fără găuri, fără autorizații, fără costuri de instalare. Funcționează cu un circuit închis intern. E suficient să-l pui pe rotițe și să-l bagi într-o priză normală.",
        q2="Cât consumă cu adevărat?",
        a2="Sistemul inteligent reglează automat puterea între 370 W și 1800 W. De îndată ce atinge temperatura dorită, reduce consumul la minim ca să o mențină. Menținând temperatura cu putere redusă, consumă mai puțin decât dacă ar funcționa mereu la maxim.",
        q3="Ce dimensiune de cameră poate răci?",
        a3="Cu 12.000 BTU este conceput pentru camere de până la circa 35 m². Potrivit pentru livinguri, dormitoare și birouri de dimensiune medie.",
        q4="Cum funcționează plata ramburs?",
        a4="Completezi formularul, echipa noastră confirmă comanda, iar curierul livrează coletul acasă. Plata se face doar la primire, direct curierului. Complet fără riscuri.",
        q5="Pot să-l returnez dacă nu sunt mulțumit?",
        a5="Sigur. Ai 60 de zile să testezi aparatul. Dacă din orice motiv nu ești mulțumit, organizăm ridicarea gratuită și rambursăm prețul de achiziție.",
        final_h="Asigură-ți tehnologia viitorului la",
        final_only=" doar {now}",
        final_warn="⚠️ Prețul de campanie de {now_long} este valabil cât durează stocul.",
        final_sub="Campania de lichidare se încheie când se epuizează stocul.",
        final_cta="🟢 Click aici și activează oferta specială",
        final_trust="Plata ramburs · Returnare gratuită 60 de zile · 4 ani garanție",
        foot_blurb="Produse utile pentru fiecare zi, livrare în 24–48 de ore cu plata ramburs.",
        foot_info="Informaţii", foot_contact="Contact",
        about="Despre noi", contact="Contactaţi-ne",
        privacy="Politica de confidențialitate", terms="Termeni și condiții",
        cookies="Politica cookie", ship="Politica de livrare", refund="Politica de rambursare",
        rights="Toate drepturile rezervate",
        ty_title="Comanda a fost primită — Așteptați apelul de confirmare | Polar PRO Max",
        ty_desc="Comanda Polar PRO Max a fost înregistrată. Mai rămâne un ultim pas: răspundeți la apelul de confirmare al operatorului nostru.",
        ty_h="Comanda Polar PRO Max a fost înregistrată cu succes!",
        ty_sub="Perfect — comanda este în procesare. Mai lipsește doar <strong>un ultim pas</strong> pentru a o finaliza și a o expedia.",
        ty_prod="Polar PRO Max 4 în 1 — aer condiționat pe coloană",
        ty_meta="12.000 BTU · Plata ramburs",
        ty_ey="👇 Ce trebuie să faceți acum", ty_ah="📞 Răspundeți la apelul de confirmare",
        ty_ap="Un operator vă va contacta <strong>în următoarele ore</strong> pentru a confirma comanda Polar PRO Max.",
        ty_aw="Dacă nu răspundeți la apel, comanda va fi anulată automat.",
        ty_hh="🕒 Program de contact", ty_hours="Luni – Sâmbătă · 9:00 – 18:00",
        ty_nh="📋 Ce urmează",
        ty_s1="Răspundeți la apel și <strong>confirmați datele</strong>",
        ty_s2="Polar PRO Max va fi expediat în <strong>24–48 de ore</strong>",
        ty_s3="Livrare la domiciliu și <strong>plata ramburs</strong>",
        ty_b1="🔒 Plata ramburs", ty_b2="🛡️ Garanție 2 ani", ty_b3="↩️ Returnare 60 de zile",
        ty_alt="Polar PRO Max aer condiționat portabil pe coloană 4 în 1",
    ),
}


class D(dict):
    def __missing__(self, k):
        raise KeyError(k)


def slug(geo: str) -> str:
    return f"column-air-conditioner-{geo}-2"


def order_form(d: dict, suffix: str = "") -> str:
    sid = suffix
    return f'''    <form class="tm-order-form order-form" action="https://offers.adricenetwork.com/forms/html/" method="post">
      <label for="name{sid}">{d["label_name"]}</label>
      <input id="name{sid}" type="text" name="name" autocomplete="name" placeholder="{d["label_name"].rstrip("*")}" required>
      <label for="street-address{sid}">{d["label_addr"]}</label>
      <input id="street-address{sid}" type="text" name="street-address" autocomplete="street-address" placeholder="{d["label_addr"].rstrip("*")}" required>
      <label for="tel{sid}">{d["label_tel"]}</label>
      <input id="tel{sid}" type="tel" name="tel" autocomplete="tel" placeholder="{d["label_tel"].rstrip("*")}" required>
      <input name="uid" type="hidden" value="{d["uid"]}" />
      <input name="offer" type="hidden" value="{d["offer"]}" />
      <input name="lp" type="hidden" value="{d["lp"]}" />
      <input name="thankyoupage" type="hidden" value="https://gadgetspothub.com/{d["path"]}/thank-you.html"/>
      <input name="webhook" type="hidden" value="{d["webhook"]}"/>
      <input name="_key" type="hidden" value="{d["key"]}" />
      <div style="margin-top: 10px; text-align: center">
        <button name="submit" type="submit">{d["btn"]}</button>
      </div>
      <p class="form-note">{d["form_note"]}</p>
      <script src="https://offers.adricenetwork.com/forms/html/js-v2/" async></script>
    </form>'''


def order_section(d: dict, anchor: str, suffix: str = "") -> str:
    return f'''<section class="zt-order-section" id="{anchor}">
  <h2 class="zt-order-title">
    <span class="zt-order-title__icon">⏱️</span>{d["order_h"]}<span class="zt-hl">{d["order_hl"]}</span>{d["order_h2"]}
  </h2>
  <p class="zt-order-text">{d["order_p"]}</p>
  <div class="zt-form-card">
    <h3 class="zt-card-title">{d["card_title"]}</h3>
    <p class="zt-card-sub">{d["card_sub"]}</p>
    <div class="zt-progress">
      <div class="zt-progress__fill">
        <span class="zt-progress__label">{d["progress"]}</span>
      </div>
    </div>
    <p class="zt-progress__note">{d["progress_note"]}</p>
    <div class="zt-order-pill">
      <span class="zt-order-pill__icon">💰</span>
      <span>{d["pill"]}</span>
    </div>
{order_form(d, suffix)}
  </div>
</section>'''


def footer(d: dict) -> str:
    g = d["geo"]
    return f'''<footer class="site-footer">
  <div class="container">
    <div class="site-footer__grid">
      <div>
        <a href="/" class="site-logo" aria-label="gadgetspothub.com home">
          <span class="site-logo__text"><span class="site-logo__text-primary">gadgetspothub</span><span class="site-logo__text-accent">.com</span></span>
        </a>
        <p class="site-footer__blurb">{d["foot_blurb"]}</p>
      </div>
      <div>
        <h4 class="site-footer__heading">{d["foot_info"]}</h4>
        <ul class="site-footer__list">
          <li><a href="/{g}/about-us.html">{d["about"]}</a></li>
          <li><a href="/{g}/contact-us.html">{d["contact"]}</a></li>
          <li><a href="/{g}/privacy-policy.html">{d["privacy"]}</a></li>
          <li><a href="/{g}/terms-conditions.html">{d["terms"]}</a></li>
          <li><a href="/{g}/cookie-policy.html">{d["cookies"]}</a></li>
          <li><a href="/{g}/shipping-policy.html">{d["ship"]}</a></li>
          <li><a href="/{g}/refund-policy.html">{d["refund"]}</a></li>
        </ul>
      </div>
      <div>
        <h4 class="site-footer__heading">{d["foot_contact"]}</h4>
        <ul class="site-footer__list">
          <li><strong>Netmart LLC</strong></li>
          <li>County of Sussex 16192 Coastal Hwy</li>
          <li>Lewes, DE 19958-3608, United States</li>
          <li><a href="mailto:info@gadgetspothub.com">info@gadgetspothub.com</a></li>
        </ul>
      </div>
    </div>
    <div class="site-footer__bottom">
      © <span data-year>2026</span> <strong>Netmart LLC</strong> — {d["rights"]}.
      <a href="/">gadgetspothub.com</a>
    </div>
  </div>
</footer>'''


def landing(d: dict) -> str:
    now, was = d["now"], d["was"]
    return f'''<!DOCTYPE html>
<html lang="{d["lang"]}">
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
<title>{d["title"]}</title>
<meta name="description" content="{d["description"]}">
<meta name="contact" content="info@gadgetspothub.com">
<meta name="theme-color" content="#0055FF">
<link rel="canonical" href="https://gadgetspothub.com/{d["path"]}/">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@600;700;800;900&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/column-ac-pt.css">
<script>
window.SITE_CONFIG = {{
  GEO: '{d["geo"]}',
  PRODUCT_SLUG: 'column-ac',
  CURRENCY: '{d["currency"]}',
  PRICE: {d["price"]},
  OFFER_NAME: 'Polar PRO Max {d["offer"]}',
  LP_ID: '{d["geo"]}-{d["offer"]}',
  FORM_ENDPOINT: 'https://TODO-network-endpoint.com/api/lead',
  SUBMITTING_LABEL: '{d["submitting"]}',
  COOKIE_TEXT: '{d["cookie_text"]}',
  COOKIE_ACCEPT: '{d["cookie_accept"]}',
  COOKIE_LEARN: '{d["cookie_learn"]}'
}};
</script>
<script src="/assets/js/tracking.js" defer></script>
<script crossorigin="anonymous" defer src="https://offers.adricenetwork.com/forms/tmfp/"></script>
</head>
<body>

<div class="wc-hero">
  <div class="wc-stickybar">
    <div class="wc-stickybar-price"><span class="now">{now}</span><span class="old">{was}</span></div>
    <a class="wc-stickybar-cta" href="#form"><span class="dot"></span>{d["sticky_cta"]}</a>
  </div>
  <div class="wc-rating">
    <span>⭐</span>
    <span>{d["rating"]}</span>
  </div>
  <div class="wc-grid">
    <div class="wc-col-text">
      <h1 class="wc-headline">{d["h1_pre"]}
        {d["h1_mid"]}<span class="price-old"> {was} </span>{d["h1_end"]}<span class="hot">{d["h1_only"]}</span>
      </h1>
      <p class="wc-sub">{d["sub"]}</p>
      <div class="wc-media-mobile">
        <img decoding="async" alt="{d["img_hero"]}" loading="eager" fetchpriority="high" width="1024" height="1024" src="/assets/img/products/column-ac/hero.webp"/>
      </div>
      <div class="wc-pricebox">
        <span class="wc-price-now">{now}</span>
        <span class="wc-price-old">{was}</span>
        <span class="wc-badge">-50%</span>
      </div>
      <div class="wc-save">{d["save"]}</div>
      <div class="wc-scarcity">{d["scarcity"]}</div>
      <a class="wc-cta" href="#form">
        <span class="dot"></span>{d["cta_hero"]}
      </a>
      <div class="wc-trust">{d["trust"]}</div>
    </div>
    <div class="wc-col-media wc-media">
      <img decoding="async" alt="{d["img_hero"]}" loading="eager" fetchpriority="high" width="1024" height="1024" src="/assets/img/products/column-ac/hero.webp"/>
    </div>
  </div>
</div>

{order_section(d, "form")}

<div class="wcp">
  <section class="wcp-sec">
    <h2 class="wcp-h2">{d["feat_h"]}<span class="wcp-red">{d["feat_h2"]}</span></h2>
    <p class="wcp-lead">{d["feat_lead"]}</p>
    <div class="wcp-feat">
      <div class="wcp-feat-card"><span class="wcp-feat-ico">❄️</span><h3>{d["f1h"]}</h3><p>{d["f1p"]}</p></div>
      <div class="wcp-feat-card"><span class="wcp-feat-ico">🔥</span><h3>{d["f2h"]}</h3><p>{d["f2p"]}</p></div>
      <div class="wcp-feat-card"><span class="wcp-feat-ico">💧</span><h3>{d["f3h"]}</h3><p>{d["f3p"]}</p></div>
      <div class="wcp-feat-card"><span class="wcp-feat-ico">🫧</span><h3>{d["f4h"]}</h3><p>{d["f4p"]}</p></div>
    </div>
  </section>

  <section class="wcp-dark">
    <h2 class="wcp-h2 wcp-h2--light"><span class="wcp-x">✕</span>{d["secret_h"]}</h2>
    <p class="wcp-dark-lead">{d["secret_p1"]}</p>
    <p class="wcp-dark-lead">{d["secret_p2"]}<strong>{d["secret_strong"]}</strong>{d["secret_p3"]}<span class="wcp-orange">{d["secret_zero"]}</span></p>
    <div class="wcp-dark-card"><span class="wcp-dark-ico">💎</span><h3 class="wcp-orange">{d["d1h"]}</h3><p>{d["d1p"]}</p></div>
    <div class="wcp-dark-card"><span class="wcp-dark-ico">🫁</span><h3 class="wcp-orange">{d["d2h"]}</h3><p>{d["d2p"]}</p></div>
    <div class="wcp-dark-card"><span class="wcp-dark-ico">🌙</span><h3 class="wcp-orange">{d["d3h"]}</h3><p>{d["d3p"]}</p></div>
  </section>

  <section class="wcp-sec">
    <div class="wcp-tech-img">
      <img decoding="async" alt="{d["img_tech"]}" loading="lazy" width="1024" height="1024" src="/assets/img/products/column-ac/tech.webp"/>
    </div>
    <h2 class="wcp-h2 wcp-center">{d["specs"]}</h2>
    <div class="wcp-table">
      <div class="wcp-row"><span>{d["r_pow"]}</span><strong>{d["v_pow"]}</strong></div>
      <div class="wcp-row"><span>{d["r_cov"]}</span><strong>{d["v_cov"]}</strong></div>
      <div class="wcp-row"><span>{d["r_eco"]}</span><strong>{d["v_eco"]}</strong></div>
      <div class="wcp-row"><span>{d["r_con"]}</span><strong>{d["v_con"]}</strong></div>
      <div class="wcp-row"><span>{d["r_reg"]}</span><strong>{d["v_reg"]}</strong></div>
      <div class="wcp-row"><span>{d["r_out"]}</span><strong>{d["v_out"]}</strong></div>
      <div class="wcp-row"><span>{d["r_noi"]}</span><strong>{d["v_noi"]}</strong></div>
      <div class="wcp-row"><span>{d["r_fil"]}</span><strong>{d["v_fil"]}</strong></div>
      <div class="wcp-row"><span>{d["r_ctl"]}</span><strong>{d["v_ctl"]}</strong></div>
      <div class="wcp-row"><span>{d["r_war"]}</span><strong>{d["v_war"]}</strong></div>
    </div>
    <div class="wcp-cta-wrap"><a class="wcp-cta" href="#modulo-ordine">{d["cta_price"]}</a></div>
  </section>

  <section class="wcp-soft">
    <h2 class="wcp-h2 wcp-center">{d["incl_h"]}<span class="wcp-red"> {now}</span></h2>
    <div class="wcp-incl">
      <div class="wcp-incl-row"><span class="wcp-check">✓</span><span class="wcp-incl-txt">{d["i1"]}</span></div>
      <div class="wcp-incl-row"><span class="wcp-check">✓</span><span class="wcp-incl-txt">{d["i2"]}</span></div>
      <div class="wcp-incl-row"><span class="wcp-check">✓</span><span class="wcp-incl-txt">{d["i3"]}</span></div>
      <div class="wcp-incl-row"><span class="wcp-check">✓</span><span class="wcp-incl-txt">{d["i4"]}</span></div>
      <div class="wcp-incl-row"><span class="wcp-check">✓</span><span class="wcp-incl-txt">{d["i5"]}</span></div>
      <div class="wcp-incl-row"><span class="wcp-check">✓</span><span class="wcp-incl-txt">{d["i6"]}</span><span class="wcp-tag wcp-tag--today">{d["today"]}</span></div>
      <div class="wcp-incl-row"><span class="wcp-check">✓</span><span class="wcp-incl-txt">{d["i7"]}</span></div>
    </div>
    <div class="wcp-cta-wrap"><a class="wcp-cta" href="#modulo-ordine">{d["cta_price"]}</a></div>
  </section>

  <section class="wcp-sec">
    <div class="wcp-rate"><span class="wcp-rate-stars">★★★★★</span><span class="wcp-rate-num">4,72/5</span></div>
    <p class="wcp-lead wcp-center">{d["reviews_avg"]}</p>
    <div class="wcp-reviews">
      <article class="wcp-rev">
        <img decoding="async" alt="{d["rev1_alt"]}" class="wcp-rev-img" loading="lazy" width="1024" height="1024" src="/assets/img/products/column-ac/review-1.webp"/>
        <div class="wcp-rev-body">
          <span class="wcp-rev-stars">★★★★★</span>
          <h3>{d["rev1_h"]}</h3>
          <p>{d["rev1_p"]}</p>
          <span class="wcp-rev-name">{d["rev1_n"]}</span>
        </div>
      </article>
      <article class="wcp-rev">
        <img decoding="async" alt="{d["rev2_alt"]}" class="wcp-rev-img" loading="lazy" width="1024" height="1024" src="/assets/img/products/column-ac/review-2.webp"/>
        <div class="wcp-rev-body">
          <span class="wcp-rev-stars">★★★★★</span>
          <h3>{d["rev2_h"]}</h3>
          <p>{d["rev2_p"]}</p>
          <span class="wcp-rev-name">{d["rev2_n"]}</span>
        </div>
      </article>
      <article class="wcp-rev">
        <img decoding="async" alt="{d["rev3_alt"]}" class="wcp-rev-img" loading="lazy" width="1024" height="1024" src="/assets/img/products/column-ac/review-3.webp"/>
        <div class="wcp-rev-body">
          <span class="wcp-rev-stars">★★★★★</span>
          <h3>{d["rev3_h"]}</h3>
          <p>{d["rev3_p"]}</p>
          <span class="wcp-rev-name">{d["rev3_n"]}</span>
        </div>
      </article>
    </div>
  </section>

  <section class="wcp-soft">
    <h2 class="wcp-h2 wcp-center">{d["faq_h"]}</h2>
    <div class="wcp-faq">
      <details class="wcp-faq-item"><summary>{d["q1"]}</summary><p>{d["a1"]}</p></details>
      <details class="wcp-faq-item"><summary>{d["q2"]}</summary><p>{d["a2"]}</p></details>
      <details class="wcp-faq-item"><summary>{d["q3"]}</summary><p>{d["a3"]}</p></details>
      <details class="wcp-faq-item"><summary>{d["q4"]}</summary><p>{d["a4"]}</p></details>
      <details class="wcp-faq-item"><summary>{d["q5"]}</summary><p>{d["a5"]}</p></details>
    </div>
  </section>

  <section class="wcp-final">
    <h2 class="wcp-final-h">{d["final_h"]}<span class="wcp-red">{d["final_only"]}</span></h2>
    <p class="wcp-final-warn">{d["final_warn"]}</p>
    <p class="wcp-final-sub">{d["final_sub"]}</p>
    <div class="wcp-cta-wrap"><a class="wcp-cta wcp-cta--xl" href="#modulo-ordine">{d["final_cta"]}</a></div>
    <p class="wcp-final-trust">{d["final_trust"]}</p>
  </section>
</div>

{order_section(d, "modulo-ordine", "-2")}

{footer(d)}

<script>
  document.querySelectorAll('[data-year]').forEach(function (el) {{
    el.textContent = String(new Date().getFullYear());
  }});
</script>
</body>
</html>
'''


def thankyou(d: dict) -> str:
    return f'''<!DOCTYPE html>
<html lang="{d["lang"]}">
<head>
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=AW-18358316754"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', 'AW-18358316754');
</script>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{d["ty_title"]}</title>
<meta name="description" content="{d["ty_desc"]}">
<meta name="contact" content="info@gadgetspothub.com">
<meta name="theme-color" content="#0055FF">
<meta name="robots" content="noindex, nofollow">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800;900&display=swap">
<link rel="stylesheet" href="/assets/css/variables.css">
<link rel="stylesheet" href="/assets/css/reset.css">
<link rel="stylesheet" href="/assets/css/components.css">
<style>
body {{ background: #f8fafc; }}
.ty-page {{ max-width: 540px; margin: 0 auto; padding: 1.5rem 1rem 3rem; }}
.ty-check {{
  width: 64px; height: 64px; border-radius: 9999px; background: #fff;
  border: 2px solid #0055ff; display: flex; align-items: center; justify-content: center;
  margin: 1rem auto 1.5rem; font-size: 2rem; color: #0055ff; font-weight: 800;
  box-shadow: 0 4px 12px -4px rgba(0,85,255,.25);
}}
.ty-headline {{ font-size: 1.625rem; font-weight: 800; line-height: 1.2; text-align: center; margin-bottom: .875rem; letter-spacing: -.02em; }}
.ty-subhead {{ text-align: center; color: var(--color-text-muted); font-size: 1rem; line-height: 1.5; margin-bottom: 1.5rem; max-width: 440px; margin-left: auto; margin-right: auto; }}
@media (min-width: 480px) {{ .ty-headline {{ font-size: 1.875rem; }} }}
.ty-product {{
  display: flex; gap: 1rem; align-items: center; background: #fff;
  border: 1px solid var(--color-border); border-radius: .75rem; padding: .875rem 1rem;
  margin-bottom: 1.25rem; box-shadow: 0 4px 16px -8px rgba(0,0,0,.12);
}}
.ty-product img {{ width: 88px; height: 88px; object-fit: contain; flex-shrink: 0; }}
.ty-product__name {{ font-weight: 800; font-size: .95rem; margin-bottom: .25rem; }}
.ty-product__meta {{ font-size: .8rem; color: var(--color-text-muted); margin-bottom: .35rem; }}
.ty-product__price {{ font-size: 1.25rem; font-weight: 800; color: #0055ff; }}
.ty-action {{ background: #eef4ff; border: 1.5px solid #b6d0ff; border-radius: .75rem; padding: 1.25rem 1.25rem 1.5rem; margin-bottom: 1rem; }}
.ty-action__eyebrow {{ font-size: .7rem; font-weight: 800; letter-spacing: .15em; text-transform: uppercase; color: #003fcc; margin-bottom: .625rem; text-align: center; }}
.ty-action__title {{ font-size: 1.25rem; font-weight: 800; text-align: center; margin-bottom: .625rem; }}
.ty-action__body {{ text-align: center; color: var(--color-text-muted); font-size: .95rem; line-height: 1.5; margin-bottom: .75rem; }}
.ty-action__warning {{ text-align: center; color: #b91c1c; font-weight: 700; font-size: .9rem; line-height: 1.45; }}
.ty-box {{ background: #fff; border: 1px solid var(--color-border); border-radius: .5rem; margin-bottom: .75rem; overflow: hidden; }}
.ty-box__header {{ padding: .625rem 1rem; background: #f8fafc; border-bottom: 1px solid var(--color-border); font-size: .7rem; font-weight: 800; letter-spacing: .12em; text-transform: uppercase; color: var(--color-text-muted); }}
.ty-box__body {{ padding: .75rem 1rem; font-size: .95rem; }}
.ty-hours-line {{ font-size: .95rem; }}
.ty-steps-list {{ list-style: none; padding: 0; margin: 0; counter-reset: ty-step; }}
.ty-steps-list li {{ display: flex; gap: .625rem; padding: .625rem 0; border-bottom: 1px solid var(--color-border); font-size: .9rem; line-height: 1.45; counter-increment: ty-step; }}
.ty-steps-list li:last-child {{ border-bottom: none; padding-bottom: 0; }}
.ty-steps-list li::before {{ content: counter(ty-step) "."; font-weight: 800; color: #0055ff; flex-shrink: 0; min-width: 1.25rem; }}
.ty-trust {{ display: flex; gap: .5rem; flex-wrap: wrap; justify-content: center; margin-top: 1.25rem; }}
.ty-trust__badge {{ background: #fff; border: 1px solid var(--color-border); border-radius: 9999px; padding: .4rem .875rem; font-size: .75rem; font-weight: 600; color: var(--color-text-muted); white-space: nowrap; }}
</style>
<script>
window.SITE_CONFIG = {{
  GEO: '{d["geo"]}',
  PRODUCT_SLUG: 'column-ac',
  CURRENCY: '{d["currency"]}',
  PRICE: {d["price"]},
  META_PIXEL_ID: '',
  GOOGLE_TAG_ID: '',
  GOOGLE_ADS_CONVERSION_ID: '',
  TY_CONVERSION_LABEL: '',
  COOKIE_TEXT: '{d["cookie_text"]}',
  COOKIE_ACCEPT: '{d["cookie_accept"]}',
  COOKIE_LEARN: '{d["cookie_learn"]}'
}};
</script>
<script src="/assets/js/tracking.js" defer></script>
<script src="/assets/js/main.js" defer></script>
</head>
<body>
<header class="site-header">
  <div class="site-header__inner">
    <a href="/" class="site-logo" aria-label="gadgetspothub.com home">
      <span class="site-logo__text"><span class="site-logo__text-primary">gadgetspothub</span><span class="site-logo__text-accent">.com</span></span>
    </a>
  </div>
</header>

<main class="ty-page">
  <div class="ty-check" aria-hidden="true">✓</div>
  <h1 class="ty-headline">{d["ty_h"]}</h1>
  <p class="ty-subhead">{d["ty_sub"]}</p>

  <div class="ty-product">
    <img src="/assets/img/products/column-ac/hero.webp" alt="{d["ty_alt"]}" width="88" height="88">
    <div>
      <div class="ty-product__name">{d["ty_prod"]}</div>
      <div class="ty-product__meta">{d["ty_meta"]}</div>
      <div class="ty-product__price">{d["now"]}</div>
    </div>
  </div>

  <section class="ty-action">
    <div class="ty-action__eyebrow">{d["ty_ey"]}</div>
    <h2 class="ty-action__title">{d["ty_ah"]}</h2>
    <p class="ty-action__body">{d["ty_ap"]}</p>
    <p class="ty-action__warning">{d["ty_aw"]}</p>
  </section>

  <section class="ty-box">
    <div class="ty-box__header">{d["ty_hh"]}</div>
    <div class="ty-box__body"><div class="ty-hours-line"><strong>{d["ty_hours"]}</strong></div></div>
  </section>

  <section class="ty-box">
    <div class="ty-box__header">{d["ty_nh"]}</div>
    <div class="ty-box__body">
      <ol class="ty-steps-list">
        <li>{d["ty_s1"]}</li>
        <li>{d["ty_s2"]}</li>
        <li>{d["ty_s3"]}</li>
      </ol>
    </div>
  </section>

  <div class="ty-trust">
    <span class="ty-trust__badge">{d["ty_b1"]}</span>
    <span class="ty-trust__badge">{d["ty_b2"]}</span>
    <span class="ty-trust__badge">{d["ty_b3"]}</span>
  </div>
</main>

{footer(d)}

<!-- Event snippet for Purchase conversion page -->
<script>
  gtag('event', 'conversion', {{
      'send_to': 'AW-18358316754/8U5lCMOvn90cENLd9rFE',
      'transaction_id': ''
  }});
</script>

<script>
  document.querySelectorAll('[data-year]').forEach(function (el) {{
    el.textContent = String(new Date().getFullYear());
  }});
</script>
</body>
</html>
'''


def fill(geo: str) -> dict:
    g = GEOS[geo]
    t = dict(TR[geo])
    d = {**g, **t, "geo": geo, "path": slug(geo)}
    for k, v in list(d.items()):
        if isinstance(v, str) and "{" in v:
            d[k] = v.format(now=g["now"], was=g["was"], now_long=g["now_long"])
    return d


def update_sitemap(geos: list[str]) -> None:
    sm = ROOT / "sitemap.xml"
    text = sm.read_text(encoding="utf-8")
    marker = '  <url><loc>https://gadgetspothub.com/column-air-conditioner-pt-2/</loc><lastmod>2026-08-26</lastmod><changefreq>weekly</changefreq><priority>0.95</priority></url>\n'
    block = "".join(
        f'  <url><loc>https://gadgetspothub.com/{slug(geo)}/</loc><lastmod>2026-08-26</lastmod><changefreq>weekly</changefreq><priority>0.95</priority></url>\n'
        for geo in geos
    )
    # Replace the single PT entry with the full geo block (PT first to keep existing URL).
    if marker not in text:
        raise SystemExit("sitemap marker not found")
    # Drop previously generated extra column-ac urls if re-running.
    import re
    text = re.sub(
        r"  <url><loc>https://gadgetspothub.com/column-air-conditioner-(?:cz|es|gr|hu|it|pt|ro)-2/</loc>.*?</url>\n",
        "",
        text,
    )
    text = text.replace(
        '  <url><loc>https://gadgetspothub.com/clima-pro-pt/</loc><lastmod>2026-08-26</lastmod><changefreq>weekly</changefreq><priority>0.95</priority></url>\n',
        '  <url><loc>https://gadgetspothub.com/clima-pro-pt/</loc><lastmod>2026-08-26</lastmod><changefreq>weekly</changefreq><priority>0.95</priority></url>\n' + block,
        1,
    )
    sm.write_text(text, encoding="utf-8")


def main() -> None:
    order = ["cz", "es", "gr", "hu", "it", "pt", "ro"]
    for geo in order:
        d = fill(geo)
        dest = ROOT / slug(geo)
        dest.mkdir(exist_ok=True)
        (dest / "index.html").write_text(landing(d), encoding="utf-8")
        (dest / "thank-you.html").write_text(thankyou(d), encoding="utf-8")
        print("wrote", dest)
    update_sitemap(order)
    print("sitemap ok")


if __name__ == "__main__":
    main()
