#!/usr/bin/env python3
"""Generate Saw 3000X landings + thank-you pages from the Italian template."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IT_LP = ROOT / "mini-saw" / "index.html"
IT_TY = ROOT / "mini-saw" / "thank-you.html"
SITEMAP = ROOT / "sitemap.xml"

UID_NEW = "0198c21d-3f64-7778-ab2d-90527716c341"
WH_NEW = "https://hook.eu2.make.com/7nudarijfrsvnhnwfnpqfh2t8vqt109i"

GEOS = {
    "cz": dict(
        lang="cs", price=1799, now="1 799 Kč", was="5 990 Kč", currency="CZK",
        offer="1945", lp="1965", key="58a99b5fd0a2d651c8eb47e8f70e5be568b69e62",
        uid=UID_NEW, webhook=WH_NEW, country="České republice",
        btn="Objednat nyní",
        fields=[
            ("name", "Jméno Příjmení*", "Jméno Příjmení"),
            ("street-address", "Adresa*", "Adresa"),
            ("tel", "Telefon*", "Telefon"),
        ],
    ),
    "es": dict(
        lang="es", price=69, now="69,00€", was="230,00€", currency="EUR",
        offer="1013", lp="1032", key="a961f90a8e79db837d16b3b00aa2cc6e2fdf9e18",
        uid=UID_NEW, webhook=WH_NEW, country="España",
        btn="Envía tu pedido",
        fields=[
            ("name", "Nombre completo*", "Nombre completo"),
            ("tel", "Número de teléfono*", "Número de teléfono"),
            ("street-address", "Dirección*", "Dirección"),
        ],
    ),
    "lt": dict(
        lang="lt", price=64, now="64,00€", was="213,00€", currency="EUR",
        offer="1427", lp="1447", key="c771c5f7b9ab17faa0d654fc0322917fd2ca7c53",
        uid=UID_NEW, webhook=WH_NEW, country="Lietuvoje",
        btn="Užsisakykite dabar",
        fields=[
            ("name", "Vardas Pavardė*", "Vardas Pavardė"),
            ("tel", "Telefonas*", "Telefonas"),
            ("street-address", "Adresas*", "Adresas"),
        ],
    ),
    "pl": dict(
        lang="pl", price=399, now="399 zł", was="1 330 zł", currency="PLN",
        offer="1429", lp="1449", key="a0252837115b00b1bc24856e441623c86a75bb28",
        uid=UID_NEW, webhook=WH_NEW, country="Polsce",
        btn="Zamów teraz",
        fields=[
            ("name", "Imię Nazwisko*", "Imię Nazwisko"),
            ("tel", "Telefon*", "Telefon"),
            ("street-address", "Adres*", "Adres"),
        ],
    ),
    "pt": dict(
        lang="pt", price=79, now="79,00€", was="263,00€", currency="EUR",
        offer="1014", lp="1033", key="629ae0c6c5cef1a64b90eef863905760e741e981",
        uid=UID_NEW, webhook=WH_NEW, country="Portugal",
        btn="Enviar o pedido",
        fields=[
            ("name", "Nome e sobrenome*", "Nome e sobrenome"),
            ("tel", "Telefone*", "Telefone"),
            ("street-address", "Endereço*", "Endereço"),
        ],
    ),
}


def D(**langs: str) -> dict[str, str]:
    return langs


def form_html(geo: str, g: dict, suffix: str) -> str:
    ids = {name: (name if not suffix else f"{name}{suffix}") for name, _, _ in g["fields"]}
    rows = []
    for name, label, ph in g["fields"]:
        fid = ids[name]
        itype = "tel" if name == "tel" else "text"
        auto = {"name": "name", "tel": "tel", "street-address": "street-address"}[name]
        rows.append(
            f'      <label for="{fid}">{label}</label>\n'
            f'      <input id="{fid}" type="{itype}" name="{name}" autocomplete="{auto}" placeholder="{ph}" required>'
        )
    fields = "\n".join(rows)
    ty = f"https://gadgetspothub.com/mini-saw-{geo}/thank-you.html"
    return f"""    <form class="tm-order-form order-form" action="https://offers.adricenetwork.com/forms/html/" method="post">
{fields}
      <input name="uid" type="hidden" value="{g['uid']}" />
      <input name="offer" type="hidden" value="{g['offer']}" />
      <input name="lp" type="hidden" value="{g['lp']}" />
      <input name="thankyoupage" type="hidden" value="{ty}"/>
      <input name="webhook" type="hidden" value="{g['webhook']}"/>
      <input name="_key" type="hidden" value="{g['key']}" />
      <div style="margin-top: 10px; text-align: center">
        <button name="submit" type="submit">{g['btn']}</button>
      </div>"""


PACK: list[tuple[str, dict[str, str]]] = [
    ("Saw 3000X — Motosega elettrica telescopica | 59,00€", D(
        cz="Saw 3000X — Elektrická teleskopická pila | 1 799 Kč",
        es="Saw 3000X — Motosierra eléctrica telescópica | 69,00€",
        lt="Saw 3000X — Elektrinis teleskopinis pjūklas | 64,00€",
        pl="Saw 3000X — Elektryczna pilarka teleskopowa | 399 zł",
        pt="Saw 3000X — Motosserra elétrica telescópica | 79,00€",
    )),
    ("Saw 3000X: taglia i rami a 5 metri e il legno fino a 35 cm, senza scala e senza benzina. 2 batterie 48 V. Pagamento alla consegna. Oggi 59,00€ invece di 196,00€.", D(
        cz="Saw 3000X: řeže větve v 5 metrech a dřevo až do 35 cm, bez žebříku a bez benzínu. 2 baterie 48 V. Platba na dobírku. Dnes 1 799 Kč místo 5 990 Kč.",
        es="Saw 3000X: corta ramas a 5 metros y madera de hasta 35 cm, sin escalera y sin gasolina. 2 baterías 48 V. Pago contra reembolso. Hoy 69,00€ en lugar de 230,00€.",
        lt="Saw 3000X: pjauna šakas 5 metrų aukštyje ir medieną iki 35 cm, be kopėčių ir be benzino. 2 baterijos 48 V. Mokėjimas pristatymo metu. Šiandien 64,00€ vietoj 213,00€.",
        pl="Saw 3000X: tnie gałęzie na 5 metrach i drewno do 35 cm, bez drabiny i bez benzyny. 2 baterie 48 V. Płatność przy odbiorze. Dziś 399 zł zamiast 1 330 zł.",
        pt="Saw 3000X: corta ramos a 5 metros e madeira até 35 cm, sem escada e sem gasolina. 2 baterias 48 V. Pagamento na entrega. Hoje 79,00€ em vez de 263,00€.",
    )),
    ("✅ Pagamento alla consegna · Spedizione gratuita 24/48h", D(
        cz="✅ Platba na dobírku · Doprava zdarma 24/48 h",
        es="✅ Pago contra reembolso · Envío gratis 24/48h",
        lt="✅ Mokėjimas pristatymo metu · Nemokamas pristatymas 24/48 val.",
        pl="✅ Płatność przy odbiorze · Darmowa dostawa 24/48h",
        pt="✅ Pagamento na entrega · Envio grátis 24/48h",
    )),
    ("Taglia i rami più alti e i tronchi più grossi senza scala.", D(
        cz="Řežte nejvyšší větve a nejsilnější kmeny bez žebříku.",
        es="Corta las ramas más altas y los troncos más gruesos sin escalera.",
        lt="Nupjaukite aukščiausias šakas ir storiausius kamienus be kopėčių.",
        pl="Tnij najwyższe gałęzie i najgrubsze pnie bez drabiny.",
        pt="Corta os ramos mais altos e os troncos mais grossos sem escada.",
    )),
    ("Senza benzina. Senza fatica. Fino a 5 metri.", D(
        cz="Bez benzínu. Bez dřiny. Až 5 metrů.",
        es="Sin gasolina. Sin esfuerzo. Hasta 5 metros.",
        lt="Be benzino. Be vargo. Iki 5 metrų.",
        pl="Bez benzyny. Bez wysiłku. Do 5 metrów.",
        pt="Sem gasolina. Sem esforço. Até 5 metros.",
    )),
    ("Saw 3000X: motosega elettrica telescopica. In pochi secondi passa dal modo manuale compatto all’asta. Taglia il legno fino a <b>35 cm</b> di diametro, arriva a <b>5 metri</b> e pesa solo <b>700 g</b>. Fatta per il giardino, gli alberi da frutto e lo spazio intorno a casa.", D(
        cz="Saw 3000X: elektrická teleskopická pila. Během pár sekund přepnete z kompaktního ručního režimu na tyč. Řeže dřevo až do průměru <b>35 cm</b>, dosáhne <b>5 metrů</b> a váží jen <b>700 g</b>. Pro zahradu, ovocné stromy a prostor kolem domu.",
        es="Saw 3000X: motosierra eléctrica telescópica. En pocos segundos pasa del modo manual compacto al asta. Corta madera de hasta <b>35 cm</b> de diámetro, llega a <b>5 metros</b> y pesa solo <b>700 g</b>. Hecha para el jardín, los frutales y el entorno de casa.",
        lt="Saw 3000X: elektrinis teleskopinis pjūklas. Per kelias sekundes pereina iš kompaktiško rankinio režimo į kotą. Pjauna medieną iki <b>35 cm</b> skersmens, pasiekia <b>5 metrus</b> ir sveria tik <b>700 g</b>. Skirta sodui, vaismedžiams ir erdvei aplink namus.",
        pl="Saw 3000X: elektryczna pilarka teleskopowa. W kilka sekund przechodzi z trybu ręcznego na wysięgnik. Tnie drewno o średnicy do <b>35 cm</b>, sięga <b>5 metrów</b> i waży tylko <b>700 g</b>. Stworzona do ogrodu, drzew owocowych i przestrzeni wokół domu.",
        pt="Saw 3000X: motosserra elétrica telescópica. Em poucos segundos passa do modo manual compacto para a haste. Corta madeira até <b>35 cm</b> de diâmetro, chega a <b>5 metros</b> e pesa só <b>700 g</b>. Feita para o jardim, as árvores de fruto e o espaço em volta de casa.",
    )),
    ("Kit completo Saw 3000X — tutto quello che c’è nel pacco", D(
        cz="Kompletní sada Saw 3000X — vše, co je v balení",
        es="Kit completo Saw 3000X — todo lo que hay en el paquete",
        lt="Pilnas Saw 3000X rinkinys — viskas, kas yra pakuotėje",
        pl="Kompletny zestaw Saw 3000X — wszystko, co jest w paczce",
        pt="Kit completo Saw 3000X — tudo o que vai na caixa",
    )),
    ("Kit completo Saw 3000X", D(
        cz="Kompletní sada Saw 3000X",
        es="Kit completo Saw 3000X",
        lt="Pilnas Saw 3000X rinkinys",
        pl="Kompletny zestaw Saw 3000X",
        pt="Kit completo Saw 3000X",
    )),
    ("🔥 Restano solo <strong>4 kit</strong> a questo prezzo", D(
        cz="🔥 Zbývají jen <strong>4 sady</strong> za tuto cenu",
        es="🔥 Solo quedan <strong>4 kits</strong> a este precio",
        lt="🔥 Šia kaina liko tik <strong>4 rinkiniai</strong>",
        pl="🔥 Zostały tylko <strong>4 zestawy</strong> w tej cenie",
        pt="🔥 Restam só <strong>4 kits</strong> a este preço",
    )),
    ("3.000 W e asta telescopica fino a 5 metri.", D(
        cz="3 000 W a teleskopická tyč až 5 metrů.",
        es="3.000 W y asta telescópica hasta 5 metros.",
        lt="3 000 W ir teleskopinis kotas iki 5 metrų.",
        pl="3 000 W i wysięgnik teleskopowy do 5 metrów.",
        pt="3.000 W e haste telescópica até 5 metros.",
    )),
    ("Dove un decespugliatore normale si ferma, la Saw 3000X continua. Attraversa legno verde o secco, rami grossi e tronchi fino a 35 cm.", D(
        cz="Kde běžný křovinořez skončí, Saw 3000X pokračuje. Projde zeleným i suchým dřevem, silnými větvemi a kmeny až do 35 cm.",
        es="Donde una desbrozadora normal se para, la Saw 3000X sigue. Atraviesa madera verde o seca, ramas gruesas y troncos de hasta 35 cm.",
        lt="Kur paprastas trimeris stoja, Saw 3000X tęsia. Kerta žalią ir sausą medieną, storas šakas ir kamienus iki 35 cm.",
        pl="Gdzie zwykła podkaszarka się zatrzymuje, Saw 3000X jedzie dalej. Przechodzi przez drewno zielone i suche, grube gałęzie i pnie do 35 cm.",
        pt="Onde uma roçadora normal pára, a Saw 3000X continua. Atravessa madeira verde ou seca, ramos grossos e troncos até 35 cm.",
    )),
    ("2 batterie da 48 V e 8.000 mAh.", D(
        cz="2 baterie 48 V a 8 000 mAh.",
        es="2 baterías de 48 V y 8.000 mAh.",
        lt="2 baterijos 48 V ir 8 000 mAh.",
        pl="2 baterie 48 V i 8 000 mAh.",
        pt="2 baterias de 48 V e 8.000 mAh.",
    )),
    ("Una al lavoro, l’altra in carica in 45 min. Niente benzina, niente miscela, niente cavi tra i piedi.", D(
        cz="Jedna v akci, druhá se nabíjí za 45 min. Žádný benzín, žádná směs, žádné kabely pod nohama.",
        es="Una trabajando, la otra cargando en 45 min. Sin gasolina, sin mezcla, sin cables entre los pies.",
        lt="Viena dirba, kita kraunasi per 45 min. Jokių benzino, jokių mišinių, jokių laidų po kojjomis.",
        pl="Jedna w robocie, druga ładuje się w 45 min. Bez benzyny, bez mieszanki, bez kabli pod nogami.",
        pt="Uma a trabalhar, a outra a carregar em 45 min. Sem gasolina, sem mistura, sem cabos pelos pés.",
    )),
    ("Pesa 700 g — la controlli con una mano.", D(
        cz="Váží 700 g — ovládáte ji jednou rukou.",
        es="Pesa 700 g — la controlas con una mano.",
        lt="Sveria 700 g — valdote viena ranka.",
        pl="Waży 700 g — sterujesz jedną ręką.",
        pt="Pesa 700 g — controlas com uma mão.",
    )),
    ("Meno fatica su braccia, spalle e schiena, anche nei lavori più lunghi. Freno istantaneo.", D(
        cz="Méně námahy na paže, ramena i záda, i při delší práci. Okamžitá brzda.",
        es="Menos fatiga en brazos, hombros y espalda, también en los trabajos más largos. Freno instantáneo.",
        lt="Mažiau nuovargio rankoms, pečiams ir nugarai, net ir ilgesniuose darbuose. Momentinis stabdys.",
        pl="Mniej zmęczenia ramion, barków i pleców, nawet przy dłuższej pracy. Hamulec natychmiastowy.",
        pt="Menos cansaço nos braços, ombros e costas, mesmo nos trabalhos mais longos. Travão instantâneo.",
    )),
    ("AutoChain X™ lubrifica e tende da sola.", D(
        cz="AutoChain X™ maže a napíná sama.",
        es="AutoChain X™ lubrica y tensa sola.",
        lt="AutoChain X™ tepa ir įtempia savaime.",
        pl="AutoChain X™ smaruje i napina sama.",
        pt="AutoChain X™ lubrifica e tensiona sozinha.",
    )),
    ("Olio sempre al posto giusto, tensione corretta, zero pause per regolare la catena.", D(
        cz="Olej vždy tam, kde má být, správné napnutí, žádné pauzy na seřízení řetězu.",
        es="Aceite siempre en su sitio, tensión correcta, cero pausas para regular la cadena.",
        lt="Alyva visada ten, kur reikia, tinkama įtemptis, jokių pauzių grandinei reguliuoti.",
        pl="Olej zawsze tam, gdzie trzeba, właściwe napięcie, zero przerw na regulację łańcucha.",
        pt="Óleo sempre no sítio certo, tensão correta, zero pausas para afinar a corrente.",
    )),
    ("4,9/5 — più di 8.730 giardini già sistemati.", D(
        cz="4,9/5 — více než 8 730 už upravených zahrad.",
        es="4,9/5 — más de 8.730 jardines ya puestos a punto.",
        lt="4,9/5 — daugiau nei 8 730 jau sutvarkytų sodų.",
        pl="4,9/5 — ponad 8 730 uporządkowanych ogrodów.",
        pt="4,9/5 — mais de 8.730 jardins já tratados.",
    )),
    ("Garanzia ufficiale 2 anni. 30 giorni per rese. Paghi solo quando arriva il corriere.", D(
        cz="Oficiální záruka 2 roky. 30 dní na vrácení. Platíte, až přijede kurýr.",
        es="Garantía oficial 2 años. 30 días para devoluciones. Pagas solo cuando llega el repartidor.",
        lt="Oficiali 2 metų garantija. 30 dienų grąžinimui. Mokate tik atvykus kurjeriui.",
        pl="Oficjalna gwarancja 2 lata. 30 dni na zwrot. Płacisz dopiero, gdy przyjedzie kurier.",
        pt="Garantia oficial 2 anos. 30 dias para devolução. Pagas só quando chega o estafeta.",
    )),
    ("Sì, voglio la Saw 3000X ↓", D(
        cz="Ano, chci Saw 3000X ↓",
        es="Sí, quiero la Saw 3000X ↓",
        lt="Taip, noriu Saw 3000X ↓",
        pl="Tak, chcę Saw 3000X ↓",
        pt="Sim, quero a Saw 3000X ↓",
    )),
    ("Sì, voglio la Saw 3000X", D(
        cz="Ano, chci Saw 3000X",
        es="Sí, quiero la Saw 3000X",
        lt="Taip, noriu Saw 3000X",
        pl="Tak, chcę Saw 3000X",
        pt="Sim, quero a Saw 3000X",
    )),
    ("💵 Paghi alla consegna", D(
        cz="💵 Platíte na dobírku",
        es="💵 Pagas al recibir",
        lt="💵 Mokate pristatymo metu",
        pl="💵 Płacisz przy odbiorze",
        pt="💵 Pagas na entrega",
    )),
    ("↩️ 30 giorni di prova", D(
        cz="↩️ 30 dní na vyzkoušení",
        es="↩️ 30 días de prueba",
        lt="↩️ 30 dienų išbandymui",
        pl="↩️ 30 dni na test",
        pt="↩️ 30 dias de teste",
    )),
    ("🚚 Spedizione gratuita", D(
        cz="🚚 Doprava zdarma",
        es="🚚 Envío gratis",
        lt="🚚 Nemokamas pristatymas",
        pl="🚚 Darmowa dostawa",
        pt="🚚 Envio grátis",
    )),
    ("ACQUISTO SICURO • SPEDIZIONE GRATUITA • GARANZIA COMPLETA", D(
        cz="BEZPEČNÝ NÁKUP • DOPRAVA ZDARMA • PLNÁ ZÁRUKA",
        es="COMPRA SEGURA • ENVÍO GRATIS • GARANTÍA COMPLETA",
        lt="SAUGUS PIRKIMAS • NEMOKAMAS PRISTATYMAS • PILNA GARANTIJA",
        pl="BEZPIECZNY ZAKUP • DARMOWA DOSTAWA • PEŁNA GWARANCJA",
        pt="COMPRA SEGURA • ENVIO GRÁTIS • GARANTIA COMPLETA",
    )),
    ("Spedizione gratuita", D(
        cz="Doprava zdarma",
        es="Envío gratis",
        lt="Nemokamas pristatymas",
        pl="Darmowa dostawa",
        pt="Envio grátis",
    )),
    ("Consegna in tutta Italia, in 24–48 ore.", D(
        cz="Doručení po celé České republice do 24–48 hodin.",
        es="Entrega en toda España, en 24–48 horas.",
        lt="Pristatymas visoje Lietuvoje per 24–48 val.",
        pl="Dostawa w całej Polsce w 24–48 godzin.",
        pt="Entrega em todo o Portugal, em 24–48 horas.",
    )),
    ("Pagamento alla consegna", D(
        cz="Platba na dobírku",
        es="Pago contra reembolso",
        lt="Mokėjimas pristatymo metu",
        pl="Płatność przy odbiorze",
        pt="Pagamento na entrega",
    )),
    ("Niente carta e niente anticipo: paghi solo quando arriva il pacco", D(
        cz="Bez karty a bez zálohy: platíte, až dorazí balík",
        es="Sin tarjeta y sin anticipo: pagas solo cuando llega el paquete",
        lt="Be kortelės ir be avanso: mokate tik atvykus siuntiniui",
        pl="Bez karty i bez zaliczki: płacisz dopiero, gdy dotrze paczka",
        pt="Sem cartão e sem adiantamento: pagas só quando chega o pacote",
    )),
    ("Acquisto protetto", D(
        cz="Chráněný nákup",
        es="Compra protegida",
        lt="Apsaugotas pirkimas",
        pl="Zakup chroniony",
        pt="Compra protegida",
    )),
    ("I tuoi dati personali sono protetti al 100%", D(
        cz="Vaše osobní údaje jsou 100% chráněny",
        es="Tus datos personales están protegidos al 100%",
        lt="Jūsų asmens duomenys apsaugoti 100 %",
        pl="Twoje dane osobowe są chronione w 100%",
        pt="Os teus dados pessoais estão protegidos a 100%",
    )),
    ("Garanzia 2 anni", D(
        cz="Záruka 2 roky",
        es="Garantía 2 años",
        lt="2 metų garantija",
        pl="Gwarancja 2 lata",
        pt="Garantia 2 anos",
    )),
    ("Puoi restituirlo senza pensieri entro 30 giorni", D(
        cz="Můžete ho bez obav vrátit do 30 dnů",
        es="Puedes devolverlo sin preocupaciones en 30 días",
        lt="Galite be rūpesčių grąžinti per 30 dienų",
        pl="Możesz zwrócić bez stresu w ciągu 30 dni",
        pt="Podes devolver sem preocupações em 30 dias",
    )),
    ("Disponibilità in magazzino", D(
        cz="Dostupnost na skladě",
        es="Disponibilidad en almacén",
        lt="Likučiai sandėlyje",
        pl="Dostępność w magazynie",
        pt="Disponibilidade em armazém",
    )),
    ("RESTANO SOLO <span>4</span> KIT", D(
        cz="ZBÝVAJÍ JEN <span>4</span> SADY",
        es="SOLO QUEDAN <span>4</span> KITS",
        lt="LIKO TIK <span>4</span> RINKINIAI",
        pl="ZOSTAŁY TYLKO <span>4</span> ZESTAWY",
        pt="RESTAM SÓ <span>4</span> KITS",
    )),
    ("Importante!", D(
        cz="Důležité!",
        es="¡Importante!",
        lt="Svarbu!",
        pl="Ważne!",
        pt="Importante!",
    )),
    ("Il magazzino si sta svuotando in fretta!", D(
        cz="Sklad se rychle vyprazdňuje!",
        es="¡El almacén se está vaciando rápido!",
        lt="Sandėlis tuštėja greitai!",
        pl="Magazyn szybko się opróżnia!",
        pt="O armazém está a esvaziar depressa!",
    )),
    ("In questo momento tante altre persone stanno guardando la Saw 3000X: per questo i kit disponibili scendono così in fretta.", D(
        cz="Právě teď si Saw 3000X prohlíží spousta dalších lidí: proto sady mizí tak rychle.",
        es="Ahora mismo mucha más gente está mirando la Saw 3000X: por eso los kits bajan tan rápido.",
        lt="Šiuo metu Saw 3000X žiūri daugybė kitų žmonių: todėl rinkiniai senka taip greitai.",
        pl="W tej chwili Saw 3000X ogląda mnóstwo innych osób: dlatego zestawy schodzą tak szybko.",
        pt="Neste momento muita gente está a ver a Saw 3000X: por isso os kits descem tão depressa.",
    )),
    ("Ordina ora e assicurati uno degli ultimi kit al prezzo di oggi, con −70%.", D(
        cz="Objednejte teď a zajistěte si jednu z posledních sad za dnešní cenu s −70 %.",
        es="Pide ahora y asegúrate uno de los últimos kits al precio de hoy, con −70%.",
        lt="Užsisakykite dabar ir užsitikrinkite vieną iš paskutinių rinkinių už šiandienos kainą su −70 %.",
        pl="Zamów teraz i zagwarantuj sobie jeden z ostatnich zestawów w dzisiejszej cenie, z −70%.",
        pt="Encomenda agora e garante um dos últimos kits ao preço de hoje, com −70%.",
    )),
    ("Prenota la Saw 3000X a soli 59 €", D(
        cz="Rezervujte Saw 3000X za pouhých 1 799 Kč",
        es="Reserva la Saw 3000X por solo 69,00€",
        lt="Rezervuokite Saw 3000X vos už 64,00€",
        pl="Zarezerwuj Saw 3000X za jedyne 399 zł",
        pt="Reserva a Saw 3000X por apenas 79,00€",
    )),
    ("Compila i tre campi. Ti chiamiamo entro 24 ore per confermare l’ordine e fissare la consegna. Paghi solo quando arriva il corriere.", D(
        cz="Vyplňte tři pole. Do 24 hodin zavoláme, potvrdíme objednávku a domluvíme doručení. Platíte, až přijede kurýr.",
        es="Rellena los tres campos. Te llamamos en 24 horas para confirmar el pedido y fijar la entrega. Pagas solo cuando llega el repartidor.",
        lt="Užpildykite tris laukus. Per 24 val. paskambinsime patvirtinti užsakymą ir suderinti pristatymą. Mokate tik atvykus kurjeriui.",
        pl="Wypełnij trzy pola. Zadzwonimy w 24 godziny, potwierdzimy zamówienie i ustalimy dostawę. Płacisz dopiero, gdy przyjedzie kurier.",
        pt="Preenche os três campos. Ligamos em 24 horas para confirmar a encomenda e combinar a entrega. Pagas só quando chega o estafeta.",
    )),
    ("🔒 Nessun anticipo · Niente carta · Paghi solo alla consegna", D(
        cz="🔒 Bez zálohy · Bez karty · Platíte až při doručení",
        es="🔒 Sin anticipo · Sin tarjeta · Pagas solo al recibir",
        lt="🔒 Be avanso · Be kortelės · Mokate tik pristatymo metu",
        pl="🔒 Bez zaliczki · Bez karty · Płacisz dopiero przy odbiorze",
        pt="🔒 Sem adiantamento · Sem cartão · Pagas só na entrega",
    )),
    ("Scala instabile e motosega a benzina: il rischio di ogni potatura", D(
        cz="Vratký žebřík a benzínová pila: riziko každého řezu",
        es="Escalera inestable y motosierra de gasolina: el riesgo de cada poda",
        lt="Nestabilios kopėčios ir benzininis pjūklas: kiekvieno genėjimo rizika",
        pl="Niestabilna drabina i pilarka spalinowa: ryzyko każdego cięcia",
        pt="Escada instável e motosserra a gasolina: o risco de cada poda",
    )),
    ("Quante volte sei già salito su una scala instabile solo per tagliare un ramo?", D(
        cz="Kolikrát jste už lezli na vratký žebřík jen kvůli jedné větvi?",
        es="¿Cuántas veces has subido ya a una escalera inestable solo para cortar una rama?",
        lt="Kiek kartų jau lipote nestabiliomis kopėčiomis tik tam, kad nupjautumėte šaką?",
        pl="Ile razy wchodziłeś już na chwiejną drabinę tylko po to, by obciąć gałąź?",
        pt="Quantas vezes já subiste a uma escada instável só para cortar um ramo?",
    )),
    ("Conosci la storia. La motosega a benzina fa un rumore assurdo, puzza di carburante e pesa 4 o 5 kg. Quella economica a batteria si blocca al primo tronco grosso. E per arrivare in cima all’albero da frutto… di nuovo la scala.", D(
        cz="Ten příběh znáte. Benzínová pila řve, smrdí palivem a váží 4 až 5 kg. Levná aku se zasekne u prvního silného kmene. A na vrchol ovocného stromu… zase žebřík.",
        es="Conoces la historia. La motosierra de gasolina hace un ruido absurdo, huele a combustible y pesa 4 o 5 kg. La barata a batería se atasca en el primer tronco gordo. Y para llegar a la copa del frutal… otra vez la escalera.",
        lt="Pažįstate istoriją. Benzininis pjūklas kaukia, dvokia degalais ir sveria 4–5 kg. Pigus akumuliatorinis stoja prie pirmo storesnio kamieno. O iki vaismedžio viršūnės… vėl kopėčios.",
        pl="Znasz tę historię. Pilarka spalinowa ryczy, śmierdzi paliwem i waży 4–5 kg. Tania akumulatorowa zacina się na pierwszym grubym pniu. A żeby dojść do czubka drzewa owocowego… znowu drabina.",
        pt="Conheces a história. A motosserra a gasolina faz um barulho absurdo, cheira a combustível e pesa 4 ou 5 kg. A barata a bateria trava no primeiro tronco grosso. E para chegar ao cimo da árvore de fruto… outra vez a escada.",
    )),
    ("Allora ne compri un’altra. E il ciclo ricomincia.", D(
        cz="Tak koupíte další. A cyklus začíná znovu.",
        es="Entonces compras otra. Y el ciclo vuelve a empezar.",
        lt="Tada perkate kitą. Ir ciklas prasideda iš naujo.",
        pl="Więc kupujesz następną. I cykl zaczyna się od nowa.",
        pt="Então compras outra. E o ciclo recomeça.",
    )),
    ("Nemmeno la versione a benzina ti salva: rumore, fumi, miscela, cavo di avviamento. Ogni potatura diventa una mattinata intera — e un rischio inutile in cima alla scala.", D(
        cz="Ani benzínová verze vás nezachrání: hluk, zplodiny, směs, startovací šňůra. Každý řez je celé dopoledne — a zbytečné riziko nahoře na žebříku.",
        es="Ni la de gasolina te salva: ruido, humos, mezcla, cuerda de arranque. Cada poda se come una mañana entera — y un riesgo inútil arriba de la escalera.",
        lt="Nė benzininis variantas neišgelbsti: triukšmas, dūmai, mišinys, starterio virvė. Kiekvienas genėjimas virsta visa rytine — ir bereikalinga rizika kopėčių viršuje.",
        pl="Nawet spalinowa cię nie ratuje: hałas, spaliny, mieszanka, linka rozrusznika. Każde cięcie zjada cały poranek — i zbędne ryzyko na szczycie drabiny.",
        pt="Nem a versão a gasolina te salva: ruído, fumos, mistura, cabo de arranque. Cada poda vira uma manhã inteira — e um risco inútil no cimo da escada.",
    )),
    ("Non è sfortuna.<br>", D(
        cz="Není to smůla.<br>",
        es="No es mala suerte.<br>",
        lt="Tai ne nesėkmė.<br>",
        pl="To nie pech.<br>",
        pt="Não é azar.<br>",
    )),
    ("La verità è che la motosega tradizionale è nata per il suolo, non per la cima dell’albero — e quelle da pochi euro nascono per essere ricomprate.", D(
        cz="Pravda je, že klasická pila vznikla pro zem, ne pro korunu stromu — a ty za pár korun se rodí k opětovnému nákupu.",
        es="La verdad es que la motosierra tradicional nació para el suelo, no para la copa del árbol — y las de pocos euros nacen para volver a comprarse.",
        lt="Tiesa ta, kad tradicinis pjūklas gimė žemei, ne medžio viršūnei — o pigieji gimsta tam, kad būtų perkami iš naujo.",
        pl="Prawda jest taka, że tradycyjna pilarka powstała do pracy na ziemi, nie na czubku drzewa — a te za parę złotych rodzą się po to, by kupować je od nowa.",
        pt="A verdade é que a motosserra tradicional nasceu para o chão, não para o cimo da árvore — e as de poucos euros nascem para se voltar a comprar.",
    )),
    ("Lubrificazione automatica della catena Saw 3000X", D(
        cz="Automatické mazání řetězu Saw 3000X",
        es="Lubricación automática de la cadena Saw 3000X",
        lt="Automatinis Saw 3000X grandinės tepimas",
        pl="Automatyczne smarowanie łańcucha Saw 3000X",
        pt="Lubrificação automática da corrente Saw 3000X",
    )),
    ("La manutenzione che non devi più fare", D(
        cz="Údržba, kterou už dělat nemusíte",
        es="El mantenimiento que ya no tienes que hacer",
        lt="Priežiūra, kurios nebereikia daryti",
        pl="Konserwacja, której już nie musisz robić",
        pt="A manutenção que já não tens de fazer",
    )),
    ("AutoChain X™ cambia le regole della catena", D(
        cz="AutoChain X™ mění pravidla řetězu",
        es="AutoChain X™ cambia las reglas de la cadena",
        lt="AutoChain X™ keičia grandinės taisykles",
        pl="AutoChain X™ zmienia zasady łańcucha",
        pt="AutoChain X™ muda as regras da corrente",
    )),
    ("Con una motosega tradizionale passi il tempo a lubrificare e a tendere la catena. Senza olio, si surriscalda. Senza tensione, salta o si blocca. E il taglio si ferma a metà ramo.", D(
        cz="U klasické pily pořád mažete a napínáte řetěz. Bez oleje se přehřeje. Bez napnutí vyskočí nebo se zasekne. A řez skončí v půlce větve.",
        es="Con una motosierra tradicional te pasas el rato lubricando y tensando la cadena. Sin aceite, se calienta. Sin tensión, salta o se atasca. Y el corte se para a mitad de rama.",
        lt="Su tradiciniu pjūklu laiką leidžiate tepdami ir įtempdami grandinę. Be alyvos kaista. Be įtempties šokinėja arba stringa. Ir pjūvis stoja vidury šakos.",
        pl="Przy tradycyjnej pilarce tracisz czas na smarowanie i napinanie łańcucha. Bez oleju się przegrzewa. Bez napięcia spada albo zacina. I cięcie staje w połowie gałęzi.",
        pt="Com uma motosserra tradicional passas o tempo a lubrificar e a tensionar a corrente. Sem óleo, aquece. Sem tensão, salta ou trava. E o corte pára a meio do ramo.",
    )),
    ("Il sistema distribuisce l’olio senza sosta e tiene la tensione giusta. Le prestazioni restano stabili dal primo all’ultimo taglio.", D(
        cz="Systém pořád dávkuje olej a drží správné napnutí. Výkon drží od prvního do posledního řezu.",
        es="El sistema reparte el aceite sin parar y mantiene la tensión justa. El rendimiento se mantiene del primer al último corte.",
        lt="Sistema nuolat dalija alyvą ir laiko tinkamą įtemptį. Našumas stabilus nuo pirmo iki paskutinio pjūvio.",
        pl="System non stop podaje olej i trzyma właściwe napięcie. Wydajność jest stała od pierwszego do ostatniego cięcia.",
        pt="O sistema reparte o óleo sem parar e mantém a tensão certa. O desempenho fica estável do primeiro ao último corte.",
    )),
    ("È esattamente il sistema montato sulla Saw 3000X.", D(
        cz="Přesně tento systém je v Saw 3000X.",
        es="Es exactamente el sistema montado en la Saw 3000X.",
        lt="Būtent tokia sistema sumontuota Saw 3000X.",
        pl="To dokładnie ten system w Saw 3000X.",
        pt="É exactamente o sistema montado na Saw 3000X.",
    )),
    ("Per questo continui a tagliare senza pause e senza regolazioni ogni dieci minuti.", D(
        cz="Proto řežete dál bez pauz a bez seřizování každých deset minut.",
        es="Por eso sigues cortando sin pausas ni ajustes cada diez minutos.",
        lt="Todėl pjaunate be pauzių ir be reguliavimo kas dešimt minučių.",
        pl="Dlatego tniesz dalej bez przerw i bez regulacji co dziesięć minut.",
        pt="Por isso continuas a cortar sem pausas nem afinações a cada dez minutos.",
    )),
    ("È lo stesso ragionamento che separa un attrezzo che chiede attenzione continua da uno che semplicemente lavora: meno regolazioni, più taglio, meno manutenzione.", D(
        cz="Stejná logika odděluje nářadí, které chce neustálou péči, od toho, které prostě pracuje: méně seřizování, víc řezu, méně údržby.",
        es="Es el mismo razonamiento que separa una herramienta que pide atención constante de una que simplemente trabaja: menos ajustes, más corte, menos mantenimiento.",
        lt="Tas pats skirtumas tarp įrankio, kuris reikalauja nuolatinio dėmesio, ir to, kuris tiesiog dirba: mažiau reguliavimo, daugiau pjovimo, mažiau priežiūros.",
        pl="To ta sama logika, która oddziela narzędzie wymagające ciągłej opieki od takiego, które po prostu pracuje: mniej regulacji, więcej cięcia, mniej konserwacji.",
        pt="É o mesmo raciocínio que separa uma ferramenta que pede atenção constante de uma que simplesmente trabalha: menos afinações, mais corte, menos manutenção.",
    )),
    ("Qui non è pubblicità. <b>È il sistema che fa il lavoro.</b>", D(
        cz="Tady nejde o reklamu. <b>Systém odvádí práci.</b>",
        es="Aquí no es publicidad. <b>Es el sistema el que hace el trabajo.</b>",
        lt="Čia ne reklama. <b>Sistema atlieka darbą.</b>",
        pl="Tu nie ma reklamy. <b>To system wykonuje robotę.</b>",
        pt="Aqui não é publicidade. <b>É o sistema a fazer o trabalho.</b>",
    )),
    ("✅ I vantaggi concreti", D(
        cz="✅ Konkrétní výhody",
        es="✅ Las ventajas concretas",
        lt="✅ Konkretūs pranašumai",
        pl="✅ Konkretne zalety",
        pt="✅ As vantagens concretas",
    )),
    ("Questa è la motosega che ti toglie la scala dal giardino", D(
        cz="Tohle je pila, která vám ze zahrady sebere žebřík",
        es="Esta es la motosierra que te quita la escalera del jardín",
        lt="Tai pjūklas, kuris iš sodo pašalina kopėčias",
        pl="To pilarka, która zabiera drabinę z ogrodu",
        pt="Esta é a motosserra que te tira a escada do jardim",
    )),
    ("Più potenza sui rami grossi, zero benzina, meno peso sulle braccia. E il giardino torna in ordine in un solo giorno.", D(
        cz="Víc síly na silné větve, nula benzínu, méně váhy na rukou. A zahrada je za jeden den v pořádku.",
        es="Más potencia en ramas gordas, cero gasolina, menos peso en los brazos. Y el jardín vuelve a estar en orden en un solo día.",
        lt="Daugiau galios storaoms šakoms, nulis benzino, mažiau svorio rankoms. Ir sodas sutvarkomas per vieną dieną.",
        pl="Więcej mocy na grubych gałęziach, zero benzyny, mniej wagi na ramionach. A ogród wraca do porządku w jeden dzień.",
        pt="Mais potência nos ramos grossos, zero gasolina, menos peso nos braços. E o jardim volta a ficar em ordem num só dia.",
    )),
    ("Saw 3000X con asta telescopica fino a 5 metri", D(
        cz="Saw 3000X s teleskopickou tyčí až 5 metrů",
        es="Saw 3000X con asta telescópica hasta 5 metros",
        lt="Saw 3000X su teleskopiniu kotu iki 5 metrų",
        pl="Saw 3000X z wysięgnikiem teleskopowym do 5 metrów",
        pt="Saw 3000X com haste telescópica até 5 metros",
    )),
    ("3.000 W e 5 metri — la cima dell’albero smette di essere un problema", D(
        cz="3 000 W a 5 metrů — koruna stromu přestane být problém",
        es="3.000 W y 5 metros — la copa del árbol deja de ser un problema",
        lt="3 000 W ir 5 metrai — medžio viršūnė nustoja būti problema",
        pl="3 000 W i 5 metrów — czubek drzewa przestaje być problemem",
        pt="3.000 W e 5 metros — o cimo da árvore deixa de ser um problema",
    )),
    ("Dove un decespugliatore normale si ferma, la Saw 3000X continua. La lama attraversa legno verde e secco, rami grossi e tronchi fino a 35 cm. Vicino al suolo usi il modo manuale compatto. In cima, monti l’asta telescopica.", D(
        cz="Kde běžný křovinořez skončí, Saw 3000X pokračuje. Lišta projde zeleným i suchým dřevem, silnými větvemi a kmeny až do 35 cm. U země použijete kompaktní ruční režim. Nahoře nasadíte teleskopickou tyč.",
        es="Donde una desbrozadora normal se para, la Saw 3000X sigue. La espada atraviesa madera verde y seca, ramas gruesas y troncos de hasta 35 cm. Cerca del suelo usas el modo manual compacto. Arriba, montas el asta telescópica.",
        lt="Kur paprastas trimeris stoja, Saw 3000X tęsia. Juosta kerta žalią ir sausą medieną, storas šakas ir kamienus iki 35 cm. Prie žemės naudojate kompaktišką rankinį režimą. Viršuje uždedate teleskopinį kotą.",
        pl="Gdzie zwykła podkaszarka staje, Saw 3000X jedzie dalej. Prowadnica przechodzi przez drewno zielone i suche, grube gałęzie i pnie do 35 cm. Przy ziemi używasz trybu ręcznego. Na górze montujesz wysięgnik.",
        pt="Onde uma roçadora normal pára, a Saw 3000X continua. A lâmina atravessa madeira verde e seca, ramos grossos e troncos até 35 cm. Perto do solo usas o modo manual compacto. No cimo, montas a haste telescópica.",
    )),
    ("Taglio da 35 cm. Potenza da 3.000 W. Altezza fino a 5 metri.", D(
        cz="Řez 35 cm. Výkon 3 000 W. Výška až 5 metrů.",
        es="Corte de 35 cm. Potencia de 3.000 W. Altura hasta 5 metros.",
        lt="Pjūvis 35 cm. Galia 3 000 W. Aukštis iki 5 metrų.",
        pl="Cięcie 35 cm. Moc 3 000 W. Wysokość do 5 metrów.",
        pt="Corte de 35 cm. Potência de 3.000 W. Altura até 5 metros.",
    )),
    ("I lavori più pesanti stanno in un solo giorno.", D(
        cz="Nejtěžší práce zvládnete za jeden den.",
        es="Los trabajos más duros caben en un solo día.",
        lt="Sunkiausius darbus sutvarkote per vieną dieną.",
        pl="Najcięższe prace mieszczą się w jeden dzień.",
        pt="Os trabalhos mais pesados cabem num só dia.",
    )),
    ("Saw 3000X a batteria che taglia un tronco senza cavi", D(
        cz="Aku Saw 3000X řeže kmen bez kabelů",
        es="Saw 3000X a batería cortando un tronco sin cables",
        lt="Akumuliatorinis Saw 3000X pjauna kamieną be laidų",
        pl="Akumulatorowa Saw 3000X tnie pień bez kabli",
        pt="Saw 3000X a bateria a cortar um tronco sem cabos",
    )),
    ("Due batterie da 48 V. Senza benzina e senza cavi", D(
        cz="Dvě baterie 48 V. Bez benzínu a bez kabelů",
        es="Dos baterías de 48 V. Sin gasolina y sin cables",
        lt="Dvi 48 V baterijos. Be benzino ir be laidų",
        pl="Dwie baterie 48 V. Bez benzyny i bez kabli",
        pt="Duas baterias de 48 V. Sem gasolina e sem cabos",
    )),
    ("Dimentica benzina, miscela e prolunghe che limitano i movimenti e si avvolgono ai piedi. Quando una batteria finisce, metti la seconda e vai avanti. Ricarica in 45 minuti.", D(
        cz="Zapomeňte na benzín, směs a prodlužovačky, které se motají u nohou. Až jedna baterie dojde, nasadíte druhou a jedete dál. Nabití za 45 minut.",
        es="Olvida gasolina, mezcla y alargadores que limitan el movimiento y se enredan en los pies. Cuando una batería se acaba, pones la segunda y sigues. Carga en 45 minutos.",
        lt="Pamirškite benziną, mišinį ir ilgintuvus, kurie riboja judesius ir vyniojasi apie kojjas. Kai viena baterija baigiasi, įstatote antrą ir tęsiate. Įkrova per 45 minutes.",
        pl="Zapomnij o benzynie, mieszance i przedłużaczach, które krępują ruchy i plączą się pod nogami. Gdy jedna bateria pada, wkładasz drugą i jedziesz dalej. Ładowanie w 45 minut.",
        pt="Esquece gasolina, mistura e extensões que limitam os movimentos e se enrolam nos pés. Quando uma bateria acaba, pões a segunda e segues. Carga em 45 minutos.",
    )),
    ("48 V · 8.000 mAh · senza fili · carica in 45 min.", D(
        cz="48 V · 8 000 mAh · bez kabelu · nabití za 45 min.",
        es="48 V · 8.000 mAh · sin cables · carga en 45 min.",
        lt="48 V · 8 000 mAh · be laidų · įkrova per 45 min.",
        pl="48 V · 8 000 mAh · bez kabli · ładowanie w 45 min.",
        pt="48 V · 8.000 mAh · sem fios · carga em 45 min.",
    )),
    ("Ti muovi in tutta la proprietà senza dipendere da una presa.", D(
        cz="Pohybujete se po celém pozemku bez závislosti na zásuvce.",
        es="Te mueves por toda la finca sin depender de un enchufe.",
        lt="Judate po visą sklypą nepriklausydami nuo rozetės.",
        pl="Poruszasz się po całej posesji bez gniazdka.",
        pt="Andas por toda a propriedade sem depender de uma tomada.",
    )),
    ("Saw 3000X in una mano: 700 g, 48 V", D(
        cz="Saw 3000X v jedné ruce: 700 g, 48 V",
        es="Saw 3000X en una mano: 700 g, 48 V",
        lt="Saw 3000X vienoje rankoje: 700 g, 48 V",
        pl="Saw 3000X w jednej ręce: 700 g, 48 V",
        pt="Saw 3000X numa mão: 700 g, 48 V",
    )),
    ("700 g. La controlli con una mano, senza distruggerti la schiena", D(
        cz="700 g. Ovládáte ji jednou rukou, bez zničených zad",
        es="700 g. La controlas con una mano, sin destrozarte la espalda",
        lt="700 g. Valdote viena ranka, nenaikindami nugaros",
        pl="700 g. Sterujesz jedną ręką, bez rujnowania pleców",
        pt="700 g. Controlas com uma mão, sem destroçar as costas",
    )),
    ("Una motosega tradizionale pesa 4–5 kg. La Saw 3000X pesa 700 g e riduce la fatica di braccia, spalle e schiena, anche nei lavori più lunghi. Il corpo compatto entra negli spazi stretti. Freno istantaneo.", D(
        cz="Klasická pila váží 4–5 kg. Saw 3000X váží 700 g a šetří paže, ramena i záda i při delší práci. Kompaktní tělo se vejde do úzkých míst. Okamžitá brzda.",
        es="Una motosierra tradicional pesa 4–5 kg. La Saw 3000X pesa 700 g y reduce la fatiga de brazos, hombros y espalda, también en los trabajos más largos. El cuerpo compacto entra en sitios estrechos. Freno instantáneo.",
        lt="Tradicinis pjūklas sveria 4–5 kg. Saw 3000X sveria 700 g ir mažina rankų, pečių ir nugaros nuovargį net ilgesniuose darbuose. Kompaktiškas korpusas telpa į siauras vietas. Momentinis stabdys.",
        pl="Tradycyjna pilarka waży 4–5 kg. Saw 3000X waży 700 g i odciąża ramiona, barki i plecy nawet przy dłuższej pracy. Kompaktowy korpus wchodzi w ciasne miejsca. Hamulec natychmiastowy.",
        pt="Uma motosserra tradicional pesa 4–5 kg. A Saw 3000X pesa 700 g e reduz o cansaço de braços, ombros e costas, mesmo nos trabalhos mais longos. O corpo compacto entra em espaços estreitos. Travão instantâneo.",
    )),
    ("700 g · una mano · freno istantaneo.", D(
        cz="700 g · jedna ruka · okamžitá brzda.",
        es="700 g · una mano · freno instantáneo.",
        lt="700 g · viena ranka · momentinis stabdys.",
        pl="700 g · jedna ręka · hamulec natychmiastowy.",
        pt="700 g · uma mão · travão instantâneo.",
    )),
    ("Tagli con precisione dove l’attrezzo pesante non arriva nemmeno.", D(
        cz="Řežete přesně tam, kam těžké nářadí ani nedosáhne.",
        es="Cortas con precisión donde la herramienta pesada ni siquiera llega.",
        lt="Pjaunate tiksliai ten, kur sunkus įrankis net nepasiekia.",
        pl="Tniesz precyzyjnie tam, dokąd ciężkie narzędzie nawet nie dosięga.",
        pt="Cortas com precisão onde a ferramenta pesada nem chega.",
    )),
    ("💵 Paghi quando arriva", D(
        cz="💵 Platíte, až dorazí",
        es="💵 Pagas cuando llega",
        lt="💵 Mokate, kai atvyksta",
        pl="💵 Płacisz, gdy dotrze",
        pt="💵 Pagas quando chega",
    )),
    ("🚚 Consegna in 24/48h", D(
        cz="🚚 Doručení 24/48 h",
        es="🚚 Entrega en 24/48h",
        lt="🚚 Pristatymas per 24/48 val.",
        pl="🚚 Dostawa w 24/48h",
        pt="🚚 Entrega em 24/48h",
    )),
    ("↩️ Provalo 30 giorni", D(
        cz="↩️ Vyzkoušejte 30 dní",
        es="↩️ Pruébalo 30 días",
        lt="↩️ Išbandykite 30 dienų",
        pl="↩️ Przetestuj 30 dni",
        pt="↩️ Experimenta 30 dias",
    )),
    ("Confronto senza filtri", D(
        cz="Srovnání bez příkras",
        es="Comparación sin filtros",
        lt="Palyginimas be filtrų",
        pl="Porównanie bez filtra",
        pt="Comparação sem filtros",
    )),
    ("Motosega tradizionale o Saw 3000X?", D(
        cz="Klasická pila, nebo Saw 3000X?",
        es="¿Motosierra tradicional o Saw 3000X?",
        lt="Tradicinis pjūklas ar Saw 3000X?",
        pl="Tradycyjna pilarka czy Saw 3000X?",
        pt="Motosserra tradicional ou Saw 3000X?",
    )),
    ("Gli stessi criteri. Senza fronzoli.", D(
        cz="Stejná kritéria. Bez omáčky.",
        es="Los mismos criterios. Sin florituras.",
        lt="Tie patys kriterijai. Be pagražinimų.",
        pl="Te same kryteria. Bez ozdobników.",
        pt="Os mesmos critérios. Sem floreados.",
    )),
    ("Tradizionale", D(
        cz="Klasická",
        es="Tradicional",
        lt="Tradicinis",
        pl="Tradycyjna",
        pt="Tradicional",
    )),
    ("⛽ Benzina, rumore e fumi", D(
        cz="⛽ Benzín, hluk a zplodiny",
        es="⛽ Gasolina, ruido y humos",
        lt="⛽ Benzinas, triukšmas ir dūmai",
        pl="⛽ Benzyna, hałas i spaliny",
        pt="⛽ Gasolina, ruído e fumos",
    )),
    ("Batteria, senza benzina", D(
        cz="Baterie, bez benzínu",
        es="Batería, sin gasolina",
        lt="Baterija, be benzino",
        pl="Bateria, bez benzyny",
        pt="Bateria, sem gasolina",
    )),
    ("Solo 700 g", D(
        cz="Jen 700 g",
        es="Solo 700 g",
        lt="Tik 700 g",
        pl="Tylko 700 g",
        pt="Apenas 700 g",
    )),
    ("🪜 Ti serve una scala", D(
        cz="🪜 Potřebujete žebřík",
        es="🪜 Necesitas una escalera",
        lt="🪜 Reikia kopėčių",
        pl="🪜 Potrzebujesz drabiny",
        pt="🪜 Precisas de uma escada",
    )),
    ("Asta fino a 5 metri", D(
        cz="Tyč až 5 metrů",
        es="Asta hasta 5 metros",
        lt="Kotas iki 5 metrų",
        pl="Wysięgnik do 5 metrów",
        pt="Haste até 5 metros",
    )),
    ("🔧 Regolazioni continue", D(
        cz="🔧 Neustálé seřizování",
        es="🔧 Ajustes constantes",
        lt="🔧 Nuolatinis reguliavimas",
        pl="🔧 Ciągłe regulacje",
        pt="🔧 Afinações constantes",
    )),
    ("🛢️ Rifornimento di benzina", D(
        cz="🛢️ Doplňování benzínu",
        es="🛢️ Repostar gasolina",
        lt="🛢️ Benzino pildymas",
        pl="🛢️ Tankowanie benzyny",
        pt="🛢️ Abastecimento de gasolina",
    )),
    ("Due batterie da 48 V", D(
        cz="Dvě baterie 48 V",
        es="Dos baterías de 48 V",
        lt="Dvi 48 V baterijos",
        pl="Dwie baterie 48 V",
        pt="Duas baterias de 48 V",
    )),
    ("⭐ Più di 8.730 giardini", D(
        cz="⭐ Více než 8 730 zahrad",
        es="⭐ Más de 8.730 jardines",
        lt="⭐ Daugiau nei 8 730 sodų",
        pl="⭐ Ponad 8 730 ogrodów",
        pt="⭐ Mais de 8.730 jardins",
    )),
    ("Chi la prova non la molla più", D(
        cz="Kdo ji zkusí, už ji nepustí",
        es="Quien la prueba ya no la suelta",
        lt="Kas išbando, nebepaleidžia",
        pl="Kto spróbuje, już nie odda",
        pt="Quem experimenta já não larga",
    )),
    ("C’è chi lascia la benzina e chi ha già bruciato soldi su versioni economiche: è questo che li porta a scegliere la Saw 3000X.", D(
        cz="Někdo odkládá benzín, někdo už spálil peníze na levných verzích: proto volí Saw 3000X.",
        es="Hay quien deja la gasolina y quien ya ha quemado dinero en versiones baratas: eso es lo que les lleva a elegir la Saw 3000X.",
        lt="Vieni palieka benziną, kiti jau sudegino pinigus ant pigių versijų: todėl renkasi Saw 3000X.",
        pl="Jedni odkładają benzynę, inni spalili już pieniądze na tanich wersjach: dlatego wybierają Saw 3000X.",
        pt="Há quem deixe a gasolina e quem já tenha queimado dinheiro em versões baratas: é isto que os leva a escolher a Saw 3000X.",
    )),
    ("Roberto G. — Saw 3000X in uso", D(
        cz="Roberto G. — Saw 3000X v akci",
        es="Roberto G. — Saw 3000X en uso",
        lt="Roberto G. — Saw 3000X darbe",
        pl="Roberto G. — Saw 3000X w użyciu",
        pt="Roberto G. — Saw 3000X em uso",
    )),
    ("“La catena attraversa in fretta anche i rami secchi più grossi, senza fatica e senza bloccarsi. Pensavo di dover usare molta più forza, invece basta guidarla con una mano.”", D(
        cz="„Řetěz projde i nejsilnějšími suchými větvemi, bez dřiny a bez zasekávání. Čekal jsem víc síly, ale stačí ji vést jednou rukou.“",
        es="“La cadena atraviesa enseguida hasta las ramas secas más gruesas, sin esfuerzo y sin atascarse. Pensaba que haría falta más fuerza, pero basta con guiarla con una mano.”",
        lt="„Grandinė greitai kerta net storiausias sausas šakas, be vargo ir be strigimo. Maniau, reikės daug daugiau jėgos, o užtenka vesti viena ranka.“",
        pl="„Łańcuch szybko przechodzi nawet przez najgrubsze suche gałęzie, bez wysiłku i bez zacinania. Myślałem, że trzeba więcej siły, a wystarczy prowadzić jedną ręką.”",
        pt="“A corrente atravessa depressa até os ramos secos mais grossos, sem esforço e sem travar. Pensei que ia precisar de muito mais força, mas basta guiá-la com uma mão.”",
    )),
    ("✅ Una potenza sorprendente", D(
        cz="✅ Překvapivá síla",
        es="✅ Una potencia sorprendente",
        lt="✅ Stulbinanti galia",
        pl="✅ Zaskakująca moc",
        pt="✅ Uma potência surpreendente",
    )),
    ("David M. — Saw 3000X in mano", D(
        cz="David M. — Saw 3000X v ruce",
        es="David M. — Saw 3000X en la mano",
        lt="David M. — Saw 3000X rankoje",
        pl="David M. — Saw 3000X w ręku",
        pt="David M. — Saw 3000X na mão",
    )),
    ("“È potente, comoda da tenere in mano e facile da usare, anche per chi non aveva mai preso una motosega. In un pomeriggio ho potato tutti gli alberi da frutto del giardino.”", D(
        cz="„Je silná, pohodlně se drží a snadno se používá, i když jste pilu nikdy neměli v ruce. Za odpoledne jsem ostříhal všechny ovocné stromy na zahradě.“",
        es="“Es potente, cómoda de sostener y fácil de usar, incluso para quien nunca había cogido una motosierra. En una tarde podé todos los frutales del jardín.”",
        lt="„Galinga, patogi laikyti ir paprasta naudoti net tam, kas niekada nebuvo ėmęs pjūklo. Per popietę nugenėjau visus sodo vaismedžius.“",
        pl="„Jest mocna, wygodna w dłoni i łatwa w użyciu, nawet dla kogoś, kto nigdy nie brał pilarki. W jedno popołudnie obciąłem wszystkie drzewa owocowe w ogrodzie.”",
        pt="“É potente, confortável de agarrar e fácil de usar, mesmo para quem nunca tinha pego numa motosserra. Numa tarde podei todas as árvores de fruto do jardim.”",
    )),
    ("✅ Fa il suo lavoro", D(
        cz="✅ Dělá, co má",
        es="✅ Hace su trabajo",
        lt="✅ Atlieka savo darbą",
        pl="✅ Robi swoje",
        pt="✅ Faz o seu trabalho",
    )),
    ("Miguel T. — Saw 3000X con asta telescopica", D(
        cz="Miguel T. — Saw 3000X s teleskopickou tyčí",
        es="Miguel T. — Saw 3000X con asta telescópica",
        lt="Miguel T. — Saw 3000X su teleskopiniu kotu",
        pl="Miguel T. — Saw 3000X z wysięgnikiem",
        pt="Miguel T. — Saw 3000X com haste telescópica",
    )),
    ("“L’asta telescopica arriva senza fatica ai rami più alti, quindi non devo più salire su una scala instabile. Ho finito in metà tempo e mi sono sentito molto più sicuro.”", D(
        cz="„Teleskopická tyč dosáhne bez námahy na nejvyšší větve, takže už nemusím lézt na vratký žebřík. Skončil jsem za poloviční čas a cítil jsem se mnohem bezpečněji.“",
        es="“El asta telescópica llega sin esfuerzo a las ramas más altas, así que ya no subo a una escalera inestable. Terminé en la mitad de tiempo y me sentí mucho más seguro.”",
        lt="„Teleskopinis kotas be vargo pasiekia aukščiausias šakas, todėl nebereikia lipti nestabiliomis kopėčiomis. Baigiau perpus greičiau ir jaučiausi daug saugiau.“",
        pl="„Wysięgnik teleskopowy bez wysiłku sięga najwyższych gałęzi, więc nie muszę już wchodzić na chwiejną drabinę. Skończyłem w połowę czasu i czułem się dużo bezpieczniej.”",
        pt="“A haste telescópica chega sem esforço aos ramos mais altos, por isso já não preciso de subir a uma escada instável. Acabei em metade do tempo e senti-me muito mais seguro.”",
    )),
    ("✅ Più veloce e più sicura", D(
        cz="✅ Rychlejší a bezpečnější",
        es="✅ Más rápida y más segura",
        lt="✅ Greičiau ir saugiau",
        pl="✅ Szybciej i bezpieczniej",
        pt="✅ Mais rápida e mais segura",
    )),
    ("📦 Tutto incluso", D(
        cz="📦 Vše v balení",
        es="📦 Todo incluido",
        lt="📦 Viskas įskaičiuota",
        pl="📦 Wszystko w zestawie",
        pt="📦 Tudo incluído",
    )),
    ("Niente extra. Niente sorprese.", D(
        cz="Žádné příplatky. Žádná překvapení.",
        es="Nada extra. Ninguna sorpresa.",
        lt="Jokių priedų. Jokių staigmenų.",
        pl="Bez dopłat. Bez niespodzianek.",
        pt="Sem extras. Sem surpresas.",
    )),
    ("Apri la scatola, monti e inizi a tagliare. Non manca niente.", D(
        cz="Otevřete krabici, složíte a začnete řezat. Nic nechybí.",
        es="Abres la caja, montas y empiezas a cortar. No falta nada.",
        lt="Atidarote dėžę, surenkate ir pradedate pjauti. Nieko netrūksta.",
        pl="Otwierasz pudełko, składasz i zaczynasz ciąć. Nic nie brakuje.",
        pt="Abres a caixa, montas e começas a cortar. Não falta nada.",
    )),
    ("Cosa c’è nella scatola", D(
        cz="Co je v krabici",
        es="Qué hay en la caja",
        lt="Kas yra dėžėje",
        pl="Co jest w pudełku",
        pt="O que vai na caixa",
    )),
    ("A cosa serve davvero", D(
        cz="K čemu to opravdu je",
        es="Para qué sirve de verdad",
        lt="Kam to iš tikrųjų reikia",
        pl="Do czego to naprawdę jest",
        pt="Para que serve de verdade",
    )),
    ("⚙️ Motosega elettrica Saw 3000X", D(
        cz="⚙️ Elektrická pila Saw 3000X",
        es="⚙️ Motosierra eléctrica Saw 3000X",
        lt="⚙️ Elektrinis pjūklas Saw 3000X",
        pl="⚙️ Elektryczna pilarka Saw 3000X",
        pt="⚙️ Motosserra elétrica Saw 3000X",
    )),
    ("3.000 W in modalità compatta — il cuore del kit", D(
        cz="3 000 W v kompaktním režimu — srdce sady",
        es="3.000 W en modo compacto — el corazón del kit",
        lt="3 000 W kompaktiškame režime — rinkinio širdis",
        pl="3 000 W w trybie kompaktowym — serce zestawu",
        pt="3.000 W no modo compacto — o coração do kit",
    )),
    ("🪜 Asta telescopica fino a 5 metri", D(
        cz="🪜 Teleskopická tyč až 5 metrů",
        es="🪜 Asta telescópica hasta 5 metros",
        lt="🪜 Teleskopinis kotas iki 5 metrų",
        pl="🪜 Wysięgnik teleskopowy do 5 metrów",
        pt="🪜 Haste telescópica até 5 metros",
    )),
    ("Arrivi in cima all’albero senza scala", D(
        cz="Dosáhnete na korunu stromu bez žebříku",
        es="Llegas a la copa del árbol sin escalera",
        lt="Pasiekiate medžio viršūnę be kopėčių",
        pl="Sięgasz czubka drzewa bez drabiny",
        pt="Chegas ao cimo da árvore sem escada",
    )),
    ("🔋 2 batterie da 48 V e 8.000 mAh", D(
        cz="🔋 2 baterie 48 V a 8 000 mAh",
        es="🔋 2 baterías de 48 V y 8.000 mAh",
        lt="🔋 2 baterijos 48 V ir 8 000 mAh",
        pl="🔋 2 baterie 48 V i 8 000 mAh",
        pt="🔋 2 baterias de 48 V e 8.000 mAh",
    )),
    ("Una al lavoro, l’altra in carica — non ti fermi", D(
        cz="Jedna v akci, druhá se nabíjí — nezastavíte se",
        es="Una trabajando, la otra cargando — no paras",
        lt="Viena dirba, kita kraunasi — nestojate",
        pl="Jedna w robocie, druga się ładuje — nie stajesz",
        pt="Uma a trabalhar, a outra a carregar — não paras",
    )),
    ("⚡ Caricabatterie rapido", D(
        cz="⚡ Rychlonabíječka",
        es="⚡ Cargador rápido",
        lt="⚡ Greitas kroviklis",
        pl="⚡ Szybka ładowarka",
        pt="⚡ Carregador rápido",
    )),
    ("45 minuti e torni a tagliare", D(
        cz="45 minut a jdete znovu řezat",
        es="45 minutos y vuelves a cortar",
        lt="45 minutės ir vėl pjaunate",
        pl="45 minut i wracasz do cięcia",
        pt="45 minutos e voltas a cortar",
    )),
    ("⛓️ 2 catene di ricambio", D(
        cz="⛓️ 2 náhradní řetězy",
        es="⛓️ 2 cadenas de recambio",
        lt="⛓️ 2 atsarginės grandinės",
        pl="⛓️ 2 łańcuchy zapasowe",
        pt="⛓️ 2 correntes de reserva",
    )),
    ("Non resti a metà ramo senza catena", D(
        cz="Nezůstanete v půlce větve bez řetězu",
        es="No te quedas a mitad de rama sin cadena",
        lt="Neliekate vidury šakos be grandinės",
        pl="Nie zostajesz w połowie gałęzi bez łańcucha",
        pt="Não ficas a meio do ramo sem corrente",
    )),
    ("🛢️ Serbatoio olio + AutoChain X™", D(
        cz="🛢️ Nádrž na olej + AutoChain X™",
        es="🛢️ Depósito de aceite + AutoChain X™",
        lt="🛢️ Alyvos bakelis + AutoChain X™",
        pl="🛢️ Zbiornik oleju + AutoChain X™",
        pt="🛢️ Depósito de óleo + AutoChain X™",
    )),
    ("Lubrifica e tende da sola — manutenzione minima", D(
        cz="Maže a napíná sama — minimální údržba",
        es="Lubrica y tensa sola — mantenimiento mínimo",
        lt="Tepa ir įtempia savaime — minimali priežiūra",
        pl="Smaruje i napina sama — minimalna konserwacja",
        pt="Lubrifica e tensiona sozinha — manutenção mínima",
    )),
    ("🧰 Set di attrezzi e valigetta", D(
        cz="🧰 Sada nářadí a kufr",
        es="🧰 Juego de herramientas y maletín",
        lt="🧰 Įrankių rinkinys ir lagaminėlis",
        pl="🧰 Zestaw narzędzi i walizka",
        pt="🧰 Conjunto de ferramentas e mala",
    )),
    ("Tutto al suo posto, pronto da riporre", D(
        cz="Vše na svém místě, připraveno k uložení",
        es="Todo en su sitio, listo para guardar",
        lt="Viskas savo vietoje, paruošta padėti",
        pl="Wszystko na swoim miejscu, gotowe do schowania",
        pt="Tudo no sítio, pronto a guardar",
    )),
    ("🛡️ Garanzia ufficiale 2 anni", D(
        cz="🛡️ Oficiální záruka 2 roky",
        es="🛡️ Garantía oficial 2 años",
        lt="🛡️ Oficialiai 2 metų garantija",
        pl="🛡️ Oficjalna gwarancja 2 lata",
        pt="🛡️ Garantia oficial 2 anos",
    )),
    ("Assistenza inclusa — 30 giorni per il reso", D(
        cz="Servis v ceně — 30 dní na vrácení",
        es="Asistencia incluida — 30 días para el retorno",
        lt="Pagalba įskaičiuota — 30 dienų grąžinimui",
        pl="Wsparcie w cenie — 30 dni na zwrot",
        pt="Assistência incluída — 30 dias para devolução",
    )),
    ("❓ Le domande più frequenti", D(
        cz="❓ Nejčastější otázky",
        es="❓ Las preguntas más frecuentes",
        lt="❓ Dažniausi klausimai",
        pl="❓ Najczęstsze pytania",
        pt="❓ As perguntas mais frequentes",
    )),
    ("Qualche dubbio? È normale.<br>", D(
        cz="Nějaké pochybnosti? To je v pořádku.<br>",
        es="¿Alguna duda? Es normal.<br>",
        lt="Abejonių? Tai normalu.<br>",
        pl="Jakieś wątpliwości? To normalne.<br>",
        pt="Alguma dúvida? É normal.<br>",
    )),
    ("Lo chiarisco tutto qui.", D(
        cz="Vše vysvětlíme tady.",
        es="Lo aclaramos todo aquí.",
        lt="Viską paaiškiname čia.",
        pl="Wszystko wyjaśniamy tutaj.",
        pt="Esclarecemos tudo aqui.",
    )),
    ("Prima di ordinare, le risposte alle domande di sempre: consegna, pagamento, benzina, rami alti e reso.", D(
        cz="Než objednáte, odpovědi na obvyklé otázky: doručení, platba, benzín, vysoké větve a vrácení.",
        es="Antes de pedir, las respuestas de siempre: entrega, pago, gasolina, ramas altas y devolución.",
        lt="Prieš užsakant — atsakymai į įprastus klausimus: pristatymas, mokėjimas, benzinas, aukštos šakos ir grąžinimas.",
        pl="Zanim zamówisz, odpowiedzi na stałe pytania: dostawa, płatność, benzyna, wysokie gałęzie i zwrot.",
        pt="Antes de encomendar, as respostas de sempre: entrega, pagamento, gasolina, ramos altos e devolução.",
    )),
    ("Quando arriva l’ordine?", D(
        cz="Kdy objednávka dorazí?",
        es="¿Cuándo llega el pedido?",
        lt="Kada atvyks užsakymas?",
        pl="Kiedy dojdzie zamówienie?",
        pt="Quando chega a encomenda?",
    )),
    ("La consegna richiede circa 1–2 giorni lavorativi. Spedizione gratuita in tutta Italia.", D(
        cz="Doručení trvá přibližně 1–2 pracovní dny. Doprava zdarma po celé České republice.",
        es="La entrega tarda unos 1–2 días laborables. Envío gratis en toda España.",
        lt="Pristatymas trunka apie 1–2 darbo dienas. Nemokamas pristatymas visoje Lietuvoje.",
        pl="Dostawa trwa około 1–2 dni robocze. Darmowa wysyłka w całej Polsce.",
        pt="A entrega demora cerca de 1–2 dias úteis. Envio grátis em todo o Portugal.",
    )),
    ("Devo pagare in anticipo?", D(
        cz="Musím platit předem?",
        es="¿Tengo que pagar por adelantado?",
        lt="Ar reikia mokėti iš anksto?",
        pl="Czy muszę płacić z góry?",
        pt="Tenho de pagar adiantado?",
    )),
    ("No. Paghi direttamente al corriere al momento della consegna. Niente carta. Niente anticipo.", D(
        cz="Ne. Platíte kurýrovi až při doručení. Bez karty. Bez zálohy.",
        es="No. Pagas al repartidor en el momento de la entrega. Sin tarjeta. Sin anticipo.",
        lt="Ne. Mokate kurjeriui pristatymo metu. Be kortelės. Be avanso.",
        pl="Nie. Płacisz kurierowi w chwili dostawy. Bez karty. Bez zaliczki.",
        pt="Não. Pagas ao estafeta no momento da entrega. Sem cartão. Sem adiantamento.",
    )),
    ("Serve la benzina?", D(
        cz="Potřebuji benzín?",
        es="¿Hace falta gasolina?",
        lt="Ar reikia benzino?",
        pl="Czy potrzebna benzyna?",
        pt="É precisa gasolina?",
    )),
    ("No. La Saw 3000X funziona solo a batteria: due da 48 V e 8.000 mAh. Niente miscela, niente fumi, niente cavo di avviamento.", D(
        cz="Ne. Saw 3000X běží jen na baterie: dvě 48 V a 8 000 mAh. Žádná směs, žádné zplodiny, žádná startovací šňůra.",
        es="No. La Saw 3000X funciona solo a batería: dos de 48 V y 8.000 mAh. Sin mezcla, sin humos, sin cuerda de arranque.",
        lt="Ne. Saw 3000X veikia tik baterijomis: dvi 48 V ir 8 000 mAh. Jokio mišinio, jokių dūmų, jokios starterio virvės.",
        pl="Nie. Saw 3000X działa tylko na baterie: dwie 48 V i 8 000 mAh. Bez mieszanki, bez spalin, bez linki rozrusznika.",
        pt="Não. A Saw 3000X funciona só a bateria: duas de 48 V e 8.000 mAh. Sem mistura, sem fumos, sem cabo de arranque.",
    )),
    ("Riesco a tagliare i rami alti senza scala?", D(
        cz="Zvládnu vysoké větve bez žebříku?",
        es="¿Puedo cortar las ramas altas sin escalera?",
        lt="Ar nupjausiu aukštas šakas be kopėčių?",
        pl="Czy zetnę wysokie gałęzie bez drabiny?",
        pt="Consigo cortar os ramos altos sem escada?",
    )),
    ("Sì. L’asta telescopica arriva fino a 5 metri. Vicino al suolo usi il modo manuale compatto. In cima all’albero, monti l’asta.", D(
        cz="Ano. Teleskopická tyč dosáhne až 5 metrů. U země použijete kompaktní ruční režim. V koruně nasadíte tyč.",
        es="Sí. El asta telescópica llega hasta 5 metros. Cerca del suelo usas el modo manual compacto. En lo alto, montas el asta.",
        lt="Taip. Teleskopinis kotas siekia iki 5 metrų. Prie žemės naudojate kompaktišką rankinį režimą. Viršūnėje uždedate kotą.",
        pl="Tak. Wysięgnik teleskopowy sięga do 5 metrów. Przy ziemi używasz trybu ręcznego. Na czubku montujesz wysięgnik.",
        pt="Sim. A haste telescópica chega até 5 metros. Perto do solo usas o modo manual compacto. No cimo da árvore, montas a haste.",
    )),
    ("E se poi non mi convince?", D(
        cz="A co když mě to nepřesvědčí?",
        es="¿Y si luego no me convence?",
        lt="O jei neįtikins?",
        pl="A jeśli potem mnie nie przekona?",
        pt="E se depois não me convencer?",
    )),
    ("Hai 30 giorni per chiedere il reso, secondo le condizioni di rimborso. Non rischi niente.", D(
        cz="Máte 30 dní na vrácení dle podmínek refundace. Nic neriskujete.",
        es="Tienes 30 días para pedir la devolución, según las condiciones de reembolso. No arriesgas nada.",
        lt="Turite 30 dienų grąžinimui pagal kompensavimo sąlygas. Niekuo nerizikuojate.",
        pl="Masz 30 dni na zwrot zgodnie z warunkami refundacji. Nic nie ryzykujesz.",
        pt="Tens 30 dias para pedir a devolução, segundo as condições de reembolso. Não arriscas nada.",
    )),
    ("✅ Paghi quando arriva", D(
        cz="✅ Platíte, až dorazí",
        es="✅ Pagas cuando llega",
        lt="✅ Mokate, kai atvyksta",
        pl="✅ Płacisz, gdy dotrze",
        pt="✅ Pagas quando chega",
    )),
    ("INSERISCI I DATI DI CONSEGNA", D(
        cz="ZADEJTE DORUČOVACÍ ÚDAJE",
        es="INTRODUCE LOS DATOS DE ENTREGA",
        lt="ĮVESKITE PRISTATYMO DUOMENIS",
        pl="WPROWADŹ DANE DOSTAWY",
        pt="INTRODUZ OS DADOS DE ENTREGA",
    )),
    ("L’ordine parte subito. Paghi solo alla consegna, direttamente al corriere.", D(
        cz="Objednávka jde hned ven. Platíte až při doručení, přímo kurýrovi.",
        es="El pedido sale de inmediato. Pagas solo al recibirlo, directamente al repartidor.",
        lt="Užsakymas išvažiuoja iš karto. Mokate tik pristatymo metu, tiesiai kurjeriui.",
        pl="Zamówienie wychodzi od razu. Płacisz dopiero przy odbiorze, bezpośrednio kurierowi.",
        pt="A encomenda parte já. Pagas só na entrega, diretamente ao estafeta.",
    )),
    ("Prodotti utili per la vita quotidiana, consegna in 24–48 ore con pagamento alla consegna.", D(
        cz="Užitečné produkty pro každodenní život, doručení do 24–48 hodin s platbou na dobírku.",
        es="Productos útiles para el día a día, entrega en 24–48 horas con pago contra reembolso.",
        lt="Naudingi kasdieniai produktai, pristatymas per 24–48 val. mokant pristatymo metu.",
        pl="Przydatne produkty na co dzień, dostawa w 24–48 godzin z płatnością przy odbiorze.",
        pt="Produtos úteis para o dia a dia, entrega em 24–48 horas com pagamento à cobrança.",
    )),
    ("Informazioni", D(cz="Informace", es="Información", lt="Informacija", pl="Informacje", pt="Informação")),
    ("Chi siamo", D(cz="O nás", es="Sobre nosotros", lt="Apie mus", pl="O nas", pt="Sobre nós")),
    ("Contattaci", D(cz="Kontaktujte nás", es="Contáctanos", lt="Susisiekite", pl="Kontakt", pt="Contacte-nos")),
    ("Termini e Condizioni", D(cz="Smluvní podmínky", es="Términos y condiciones", lt="Taisyklės ir sąlygos", pl="Regulamin", pt="Termos e Condições")),
    ("Politica di spedizione", D(cz="Zásady dopravy", es="Política de envío", lt="Siuntimo politika", pl="Polityka wysyłki", pt="Política de envio")),
    ("Politica di reso", D(cz="Zásady vrácení peněz", es="Política de reembolso", lt="Grąžinimo politika", pl="Polityka zwrotów", pt="Política de reembolso")),
    ("Politica di Spedizione", D(cz="Zásady dopravy", es="Política de envío", lt="Pristatymo politika", pl="Polityka wysyłki", pt="Política de Envio")),
    ("Politica di Rimborso", D(cz="Zásady vrácení peněz", es="Política de reembolso", lt="Grąžinimo politika", pl="Polityka zwrotów", pt="Política de reembolso")),
    ("Privacy Policy", D(cz="Zásady ochrany osobních údajů", es="Política de privacidad", lt="Privatumo politika", pl="Polityka prywatności", pt="Política de Privacidade")),
    ("Cookie Policy", D(cz="Zásady používání souborů cookie", es="Política de cookies", lt="Slapukų politika", pl="Polityka cookies", pt="Política de Cookies")),
    ("Contatti", D(cz="Kontakt", es="Contacto", lt="Kontaktai", pl="Kontakt", pt="Contacto")),
    ("Tutti i diritti riservati.", D(
        cz="Všechna práva vyhrazena.",
        es="Todos los derechos reservados.",
        lt="Visos teisės saugomos.",
        pl="Wszelkie prawa zastrzeżone.",
        pt="Todos os direitos reservados.",
    )),
    ("Usiamo cookie tecnici e di terze parti per migliorare la tua esperienza e per analisi.", D(
        cz="Používáme technické cookies a cookies třetích stran ke zlepšení vašeho zážitku a pro analytiku.",
        es="Usamos cookies técnicas y de terceros para mejorar tu experiencia y para análisis.",
        lt="Naudojame techninius ir trečiųjų šalių slapukus patirčiai gerinti ir analitikai.",
        pl="Używamy plików cookie technicznych i stron trzecich, aby poprawić Twoje doświadczenie i do analityki.",
        pt="Usamos cookies técnicos e de terceiros para melhorar a tua experiência e para análises.",
    )),
    ("Scopri di più", D(cz="Zjistit více", es="Más información", lt="Sužinoti daugiau", pl="Dowiedz się więcej", pt="Saber mais")),
    ("Accetta", D(cz="Přijmout", es="Aceptar", lt="Priimti", pl="Akceptuję", pt="Aceitar")),
    ("Invio...", D(cz="Odesílám...", es="Enviando...", lt="Siunčiama...", pl="Wysyłanie...", pt="A enviar...")),
]

TY_PACK: list[tuple[str, dict[str, str]]] = [
    ("Ordine ricevuto — Attendi la chiamata di conferma | Saw 3000X", D(
        cz="Objednávka přijata — Počkejte na potvrzovací hovor | Saw 3000X",
        es="Pedido recibido — Espera la llamada de confirmación | Saw 3000X",
        lt="Užsakymas gautas — Palaukite patvirtinimo skambučio | Saw 3000X",
        pl="Zamówienie przyjęte — Poczekaj na telefon potwierdzający | Saw 3000X",
        pt="Encomenda recebida — Aguarde a chamada de confirmação | Saw 3000X",
    )),
    ("Il tuo ordine Saw 3000X è stato registrato. Manca solo un ultimo passaggio: rispondi alla chiamata di conferma del nostro operatore.", D(
        cz="Vaše objednávka Saw 3000X byla zaznamenána. Zbývá poslední krok: přijměte potvrzovací hovor od našeho operátora.",
        es="Tu pedido Saw 3000X ha sido registrado. Solo falta un último paso: responde a la llamada de confirmación de nuestro operador.",
        lt="Jūsų Saw 3000X užsakymas užregistruotas. Liko paskutinis žingsnis: atsiliepkite į operatoriaus patvirtinimo skambutį.",
        pl="Twoje zamówienie Saw 3000X zostało zapisane. Został ostatni krok: odbierz telefon potwierdzający od naszego operatora.",
        pt="A tua encomenda Saw 3000X foi registada. Falta só um último passo: atende a chamada de confirmação do nosso operador.",
    )),
    ("Il tuo ordine Saw 3000X è stato registrato!", D(
        cz="Vaše objednávka Saw 3000X byla zaznamenána!",
        es="¡Tu pedido Saw 3000X se ha registrado!",
        lt="Jūsų Saw 3000X užsakymas užregistruotas!",
        pl="Twoje zamówienie Saw 3000X zostało zapisane!",
        pt="A tua encomenda Saw 3000X foi registada!",
    )),
    ("Perfetto — il tuo ordine è in elaborazione. Manca solo <strong>un ultimo passaggio</strong> per completarlo e far partire la spedizione.", D(
        cz="Skvělé — objednávka se zpracovává. Zbývá už jen <strong>poslední krok</strong> k dokončení a odeslání.",
        es="Perfecto — tu pedido está en proceso. Solo falta <strong>un último paso</strong> para completarlo y enviar.",
        lt="Puiku — užsakymas apdorojamas. Liko tik <strong>paskutinis žingsnis</strong>, kad užbaigtume ir išsiųstume.",
        pl="Świetnie — zamówienie jest przetwarzane. Został tylko <strong>ostatni krok</strong>, żeby je dokończyć i nadać przesyłkę.",
        pt="Perfeito — a encomenda está a ser processada. Falta só <strong>um último passo</strong> para a concluir e enviar.",
    )),
    ("Saw 3000X — motosega elettrica telescopica", D(
        cz="Saw 3000X — elektrická teleskopická pila",
        es="Saw 3000X — motosierra eléctrica telescópica",
        lt="Saw 3000X — elektrinis teleskopinis pjūklas",
        pl="Saw 3000X — elektryczna pilarka teleskopowa",
        pt="Saw 3000X — motosserra elétrica telescópica",
    )),
    ("Kit completo · Pagamento alla consegna", D(
        cz="Kompletní sada · Platba na dobírku",
        es="Kit completo · Pago contra reembolso",
        lt="Pilnas rinkinys · Mokėjimas pristatymo metu",
        pl="Zestaw kompletny · Płatność przy odbiorze",
        pt="Kit completo · Pagamento à cobrança",
    )),
    ("👇 Cosa devi fare adesso", D(
        cz="👇 Co máte udělat teď",
        es="👇 Qué debes hacer ahora",
        lt="👇 Ką dabar daryti",
        pl="👇 Co musisz zrobić teraz",
        pt="👇 O que deves fazer agora",
    )),
    ("📞 Rispondi alla chiamata di conferma", D(
        cz="📞 Přijměte potvrzovací hovor",
        es="📞 Responde a la llamada de confirmación",
        lt="📞 Atsiliepkite į patvirtinimo skambutį",
        pl="📞 Odbierz telefon potwierdzający",
        pt="📞 Atende a chamada de confirmação",
    )),
    ("Un nostro operatore ti contatterà <strong>nelle prossime ore</strong> per confermare il tuo ordine Saw 3000X.", D(
        cz="Náš operátor vás bude kontaktovat <strong>v příštích hodinách</strong>, aby potvrdil objednávku Saw 3000X.",
        es="Un operador te contactará <strong>en las próximas horas</strong> para confirmar tu pedido Saw 3000X.",
        lt="Mūsų operatorius susisieks <strong>per artimiausias valandas</strong>, kad patvirtintų Saw 3000X užsakymą.",
        pl="Nasz operator skontaktuje się <strong>w ciągu najbliższych godzin</strong>, aby potwierdzić zamówienie Saw 3000X.",
        pt="Um operador vai contactar-te <strong>nas próximas horas</strong> para confirmar a encomenda Saw 3000X.",
    )),
    ("Se non rispondi alla chiamata, l'ordine verrà automaticamente annullato.", D(
        cz="Pokud hovor nepřijmete, objednávka bude automaticky zrušena.",
        es="Si no respondes a la llamada, el pedido se cancelará automáticamente.",
        lt="Jei neatsiliepsite, užsakymas bus automatiškai atšauktas.",
        pl="Jeśli nie odbierzesz telefonu, zamówienie zostanie automatycznie anulowane.",
        pt="Se não atenderes a chamada, a encomenda será cancelada automaticamente.",
    )),
    ("🕒 Orari di contatto", D(
        cz="🕒 Kontaktní hodiny",
        es="🕒 Horario de contacto",
        lt="🕒 Kontaktų valandos",
        pl="🕒 Godziny kontaktu",
        pt="🕒 Horário de contacto",
    )),
    ("Lunedì – Sabato · 9:00 – 18:00", D(
        cz="Pondělí – Sobota · 9:00 – 18:00",
        es="Lunes – Sábado · 9:00 – 18:00",
        lt="Pirmadienis – Šeštadienis · 9:00 – 18:00",
        pl="Poniedziałek – Sobota · 9:00 – 18:00",
        pt="Segunda – Sábado · 9:00 – 18:00",
    )),
    ("📋 Cosa succede dopo", D(
        cz="📋 Co se stane dál",
        es="📋 Qué ocurre después",
        lt="📋 Kas toliau",
        pl="📋 Co dalej",
        pt="📋 O que acontece a seguir",
    )),
    ("Rispondi alla chiamata e <strong>conferma i tuoi dati</strong>", D(
        cz="Přijměte hovor a <strong>potvrďte své údaje</strong>",
        es="Responde a la llamada y <strong>confirma tus datos</strong>",
        lt="Atsiliepkite ir <strong>patvirtinkite duomenis</strong>",
        pl="Odbierz telefon i <strong>potwierdź swoje dane</strong>",
        pt="Atende a chamada e <strong>confirma os teus dados</strong>",
    )),
    ("La tua Saw 3000X verrà spedita entro <strong>24–48 ore</strong>", D(
        cz="Vaše Saw 3000X odešleme do <strong>24–48 hodin</strong>",
        es="Tu Saw 3000X se enviará en <strong>24–48 horas</strong>",
        lt="Jūsų Saw 3000X išsiųsime per <strong>24–48 val.</strong>",
        pl="Twoja Saw 3000X zostanie wysłana w ciągu <strong>24–48 godzin</strong>",
        pt="A tua Saw 3000X será enviada em <strong>24–48 horas</strong>",
    )),
    ("Consegna a domicilio e <strong>pagamento alla consegna</strong>", D(
        cz="Doručení domů a <strong>platba na dobírku</strong>",
        es="Entrega a domicilio y <strong>pago contra reembolso</strong>",
        lt="Pristatymas į namus ir <strong>mokėjimas pristatymo metu</strong>",
        pl="Dostawa do domu i <strong>płatność przy odbiorze</strong>",
        pt="Entrega ao domicílio e <strong>pagamento à cobrança</strong>",
    )),
    ("🔒 Pagamento alla consegna", D(
        cz="🔒 Platba na dobírku",
        es="🔒 Pago contra reembolso",
        lt="🔒 Mokėjimas pristatymo metu",
        pl="🔒 Płatność przy odbiorze",
        pt="🔒 Pagamento à cobrança",
    )),
    ("🛡️ Garanzia 2 anni", D(
        cz="🛡️ Záruka 2 roky",
        es="🛡️ Garantía 2 años",
        lt="🛡️ 2 metų garantija",
        pl="🛡️ Gwarancja 2 lata",
        pt="🛡️ Garantia 2 anos",
    )),
]


def apply(text: str, geo: str, pack: list[tuple[str, dict[str, str]]]) -> str:
    for src, langs in sorted(pack, key=lambda x: len(x[0]), reverse=True):
        text = text.replace(src, langs[geo])
    return text


def replace_form(html: str, geo: str, g: dict) -> str:
    forms = list(re.finditer(r'<form class="tm-order-form order-form".*?</form>', html, re.S))
    if len(forms) != 2:
        raise SystemExit(f"expected 2 forms, found {len(forms)}")
    first = form_html(geo, g, "") + "\n      <p class=\"form-note\">🔒"
    # keep form-note + script from original by grafting after button block
    # Simpler: replace each full form including note via capturing note
    out = html
    for i, m in enumerate(reversed(forms)):
        suffix = "" if i == 1 else "-2"
        block = m.group(0)
        note = re.search(r'<p class="form-note">.*?</p>', block, re.S)
        script = re.search(r'<script src="https://offers.adricenetwork.com/forms/html/js-v2/" async></script>', block)
        new = form_html(geo, g, suffix)
        if note:
            new += "\n      " + note.group(0)
        if script:
            new += "\n      " + script.group(0)
        new += "\n    </form>"
        out = out[: m.start()] + new + out[m.end() :]
    return out


def build_lp(geo: str, g: dict, src: str) -> str:
    html = src
    html = html.replace('<html lang="it">', f'<html lang="{g["lang"]}">')
    html = html.replace("https://gadgetspothub.com/mini-saw/", f"https://gadgetspothub.com/mini-saw-{geo}/")
    html = html.replace("/it/", f"/{geo}/")
    html = replace_form(html, geo, g)
    html = apply(html, geo, PACK)
    html = html.replace("59,00€", g["now"]).replace("196,00€", g["was"])
    html = re.sub(
        r"window\.SITE_CONFIG = \{.*?\};",
        (
            "window.SITE_CONFIG = {\n"
            f"  GEO: '{geo}',\n"
            "  PRODUCT_SLUG: 'saw3000x',\n"
            f"  CURRENCY: '{g['currency']}',\n"
            f"  PRICE: {g['price']},\n"
            f"  OFFER_NAME: 'Saw 3000X {g['offer']}',\n"
            f"  LP_ID: '{geo}-{g['lp']}',\n"
            f"  SUBMITTING_LABEL: {json_submit(geo)},\n"
            f"  COOKIE_TEXT: {json_cookie(geo, 'text')},\n"
            f"  COOKIE_ACCEPT: {json_cookie(geo, 'accept')},\n"
            f"  COOKIE_LEARN: {json_cookie(geo, 'learn')}\n"
            "};"
        ),
        html,
        count=1,
        flags=re.S,
    )
    return html


def json_submit(geo: str) -> str:
    return {
        "cz": "'Odesílám...'",
        "es": "'Enviando...'",
        "lt": "'Siunčiama...'",
        "pl": "'Wysyłanie...'",
        "pt": "'A enviar...'",
    }[geo]


def json_cookie(geo: str, which: str) -> str:
    vals = {
        "cz": dict(text="'Používáme technické cookies a cookies třetích stran ke zlepšení vašeho zážitku a pro analytiku.'", accept="'Přijmout'", learn="'Zjistit více'"),
        "es": dict(text="'Usamos cookies técnicas y de terceros para mejorar tu experiencia y para análisis.'", accept="'Aceptar'", learn="'Más información'"),
        "lt": dict(text="'Naudojame techninius ir trečiųjų šalių slapukus patirčiai gerinti ir analitikai.'", accept="'Priimti'", learn="'Sužinoti daugiau'"),
        "pl": dict(text="'Używamy plików cookie technicznych i stron trzecich, aby poprawić Twoje doświadczenie i do analityki.'", accept="'Akceptuję'", learn="'Dowiedz się więcej'"),
        "pt": dict(text="'Usamos cookies técnicos e de terceiros para melhorar a tua experiência e para análises.'", accept="'Aceitar'", learn="'Saber mais'"),
    }
    return vals[geo][which]


def build_ty(geo: str, g: dict, src: str) -> str:
    html = src
    html = html.replace('<html lang="it">', f'<html lang="{g["lang"]}">')
    html = html.replace("/it/", f"/{geo}/")
    html = apply(html, geo, TY_PACK)
    html = apply(html, geo, PACK)
    html = html.replace("59,00€", g["now"])
    html = re.sub(
        r"  GEO: 'it',",
        f"  GEO: '{geo}',",
        html,
        count=1,
    )
    html = re.sub(r"  PRICE: 59,", f"  PRICE: {g['price']},", html, count=1)
    html = re.sub(r"  CURRENCY: 'EUR',", f"  CURRENCY: '{g['currency']}',", html, count=1)
    return html


def update_sitemap() -> None:
    text = SITEMAP.read_text()
    block = []
    for geo in GEOS:
        loc = f"https://gadgetspothub.com/mini-saw-{geo}/"
        line = f'  <url><loc>{loc}</loc><lastmod>2026-08-31</lastmod><changefreq>weekly</changefreq><priority>0.95</priority></url>\n'
        if loc not in text:
            block.append(line)
        else:
            text = re.sub(
                rf"  <url><loc>{re.escape(loc)}</loc><lastmod>[^<]+</lastmod>",
                f'  <url><loc>{loc}</loc><lastmod>2026-08-31</lastmod>',
                text,
            )
    marker = '  <url><loc>https://gadgetspothub.com/mini-saw/</loc>'
    insert = "".join(block)
    if insert and marker in text:
        # put geos right after IT mini-saw
        idx = text.find(marker)
        end = text.find("\n", idx) + 1
        text = text[:end] + insert + text[end:]
        # drop old mini-saw-pt duplicate if we re-added
        # keep single pt line from GEOS
        pass
    SITEMAP.write_text(text)


def main() -> None:
    lp_src = IT_LP.read_text()
    ty_src = IT_TY.read_text()
    for geo, g in GEOS.items():
        folder = ROOT / f"mini-saw-{geo}"
        folder.mkdir(exist_ok=True)
        (folder / "index.html").write_text(build_lp(geo, g, lp_src))
        (folder / "thank-you.html").write_text(build_ty(geo, g, ty_src))
        print("wrote", folder)
    update_sitemap()
    print("sitemap updated")


if __name__ == "__main__":
    main()
