#!/usr/bin/env python3
"""Generate T77 PRO landings + thank-you pages for ES HU PL PT RO."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IT_LP = ROOT / "grass-trimmer-t77-pro" / "index.html"
IT_TY = ROOT / "grass-trimmer-t77-pro" / "thank-you.html"
SITEMAP = ROOT / "sitemap.xml"

UID_NEW = "0198c21d-3f64-7778-ab2d-90527716c341"
WH_NEW = "https://hook.eu2.make.com/7nudarijfrsvnhnwfnpqfh2t8vqt109i"

GEOS = {
    "es": dict(
        lang="es", price=74, now="74,00€", was="148,00€", now_ty="74,00€", currency="EUR",
        offer="1815", lp="1835", key="856b5671fbfa784b3d05bd41fb8a08636ee63d9e",
        uid=UID_NEW, webhook=WH_NEW,
        ph_name="Nombre Apellido", ph_tel="Teléfono",
        ph_addr="Dirección",
    ),
    "hu": dict(
        lang="hu", price=24900, now="24 900 Ft", was="49 800 Ft", now_ty="24 900 Ft", currency="HUF",
        offer="1820", lp="1840", key="82ebeb35b70348d39060fbe4912f04a72fca930b",
        uid=UID_NEW, webhook=WH_NEW,
        ph_name="Vezetéknév Vezetéknév", ph_tel="Telefon",
        ph_addr="Cím",
    ),
    "pl": dict(
        lang="pl", price=299, now="299 zł", was="598 zł", now_ty="299 zł", currency="PLN",
        offer="24", lp="32", key="cb6fb56ff381be6bd671f97c905c8033d02b02e3",
        uid=UID_NEW, webhook=WH_NEW,
        ph_name="Imię i nazwisko", ph_tel="Numer telefonnu",
        ph_addr="Adres",
    ),
    "pt": dict(
        lang="pt", price=79, now="79,00€", was="158,00€", now_ty="79,00€", currency="EUR",
        offer="1816", lp="1836", key="b16a4e56818e45570a31677d2358cd9094c04df2",
        uid=UID_NEW, webhook=WH_NEW,
        ph_name="Nome Sobrenome", ph_tel="Telefone",
        ph_addr="Endereço",
    ),
    "ro": dict(
        lang="ro", price=399, now="399 lei", was="798 lei", now_ty="399 lei", currency="RON",
        offer="2637", lp="2664", key="632b67823616823cf0755d177dcb976890e893a7",
        uid=UID_NEW, webhook=WH_NEW,
        ph_name="Nome e cognome", ph_tel="Telefono",
        ph_addr="Indirizzo",
    ),
}


def D(**langs: str) -> dict[str, str]:
    return langs


# Longer Italian strings first is applied at runtime.
PACK: list[tuple[str, dict[str, str]]] = [
    ("T77 PRO™: taglia, rifila e sagoma con 2 batterie e motore brushless. 300 m² con una ricarica. Pagamento alla consegna. Oggi 99 € invece di 200 €.", D(
        es="T77 PRO™: corta, recorta y perfila con 2 baterías y motor brushless. 300 m² con una carga. Pago contra reembolso. Hoy 74,00€ en lugar de 148,00€.",
        hu="T77 PRO™: vág, szegélyez és formáz 2 akkumulátorral és brushless motorral. 300 m² egy töltéssel. Utánvét. Ma 24 900 Ft 49 800 Ft helyett.",
        pl="T77 PRO™: tnie, przycina i kształtuje z 2 bateriami i silnikiem brushless. 300 m² na jednym ładowaniu. Płatność przy odbiorze. Dziś 299 zł zamiast 598 zł.",
        pt="T77 PRO™: corta, apara e perfila com 2 baterias e motor brushless. 300 m² com uma carga. Pagamento à cobrança. Hoje 79,00€ em vez de 158,00€.",
        ro="T77 PRO™: taie, tunde și profilează cu 2 baterii și motor brushless. 300 m² cu o încărcare. Plata ramburs. Azi 399 lei în loc de 798 lei.",
    )),
    ("T77 PRO — Decespugliatore a batteria brushless | 99 €", D(
        es="T77 PRO — Desbrozadora a batería brushless | 74,00€",
        hu="T77 PRO — Akkus szegélynyíró brushless | 24 900 Ft",
        pl="T77 PRO — Podkaszarka akumulatorowa brushless | 299 zł",
        pt="T77 PRO — Roçadora a bateria brushless | 79,00€",
        ro="T77 PRO — Motocoasă cu baterie brushless | 399 lei",
    )),
    ("T77 PRO™: Taglia, rifila e sagoma con precisione millimetrica. Dimentica le seccature degli attrezzi vecchi: con soli <b>1,2 kg</b> e la potenza di <b>2 batterie agli ioni di litio da 60V</b>, prendersi cura del prato diventa un piacere rapido e leggero. Pura potenza, zero ostacoli.", D(
        es="T77 PRO™: Corta, recorta y perfila con precisión milimétrica. Olvídate de las molestias de las herramientas viejas: con solo <b>1,2 kg</b> y la potencia de <b>2 baterías de iones de litio de 60V</b>, cuidar el césped se vuelve rápido y ligero. Pura potencia, cero obstáculos.",
        hu="T77 PRO™: Vág, szegélyez és formáz milliméteres pontossággal. Felejtse el a régi szerszámok nyűgét: mindössze <b>1,2 kg</b> és <b>2 darab 60V-os lítiumion-akkumulátor</b> erejével a fűápolás gyors és könnyű. Tiszta erő, nulla akadály.",
        pl="T77 PRO™: Tnie, przycina i kształtuje z milimetrową precyzją. Zapomnij o utrapieniach starych narzędzi: przy zaledwie <b>1,2 kg</b> i mocy <b>2 baterii litowo-jonowych 60V</b> pielęgnacja trawnika staje się szybka i lekka. Czysta moc, zero przeszkód.",
        pt="T77 PRO™: Corta, apara e perfila com precisão milimétrica. Esquece os aborrecimentos das ferramentas velhas: com apenas <b>1,2 kg</b> e a potência de <b>2 baterias de iões de lítio de 60V</b>, cuidar do relvado torna-se rápido e leve. Pura potência, zero obstáculos.",
        ro="T77 PRO™: Taie, tunde și profilează cu precizie milimetrică. Uită deranjul uneltelor vechi: cu doar <b>1,2 kg</b> și puterea a <b>2 baterii litiu-ion de 60V</b>, îngrijirea gazonului devine rapidă și ușoară. Putere pură, zero obstacole.",
    )),
    ("T77 PRO™: Taglia, rifila e sagoma con precisione millimetrica.", D(
        es="T77 PRO™: Corta, recorta y perfila con precisión milimétrica.",
        hu="T77 PRO™: Vág, szegélyez és formáz milliméteres pontossággal.",
        pl="T77 PRO™: Tnie, przycina i kształtuje z milimetrową precyzją.",
        pt="T77 PRO™: Corta, apara e perfila com precisão milimétrica.",
        ro="T77 PRO™: Taie, tunează și profilează cu precizie milimetrică.",
    )),
    ("300m² di giardino con una sola ricarica.", D(
        es="300 m² de jardín con una sola carga.",
        hu="300 m² kert egyetlen töltéssel.",
        pl="300 m² ogrodu na jednym ładowaniu.",
        pt="300 m² de jardim com uma só carga.",
        ro="300 m² de grădină cu o singură încărcare.",
    )),
    ("Addio per sempre a benzina, miscela e strappi.", D(
        es="Adiós para siempre a la gasolina, la mezcla y los tirones.",
        hu="Örökre vége a benzinnek, a keveréknek és a berántásnak.",
        pl="Żegnaj benzyno, mieszance i szarpaniu sznurka.",
        pt="Adeus para sempre à gasolina, à mistura e aos puxões.",
        ro="Adio pentru totdeauna benzinei, amestecului și smuciturilor.",
    )),
    ("✅ Pagamento alla consegna · Spedizione 24/48h", D(
        es="✅ Pago contra reembolso · Envío 24/48h",
        hu="✅ Utánvét · Szállítás 24/48 óra",
        pl="✅ Płatność przy odbiorze · Dostawa 24/48h",
        pt="✅ Pagamento à cobrança · Envio 24/48h",
        ro="✅ Plata ramburs · Livrare 24/48h",
    )),
    ("🔥 Solo <strong>7 pezzi</strong> rimasti a questo prezzo", D(
        es="🔥 Solo quedan <strong>7 unidades</strong> a este precio",
        hu="🔥 Ezen az áron már csak <strong>7 darab</strong> van",
        pl="🔥 Tylko <strong>7 sztuk</strong> zostało w tej cenie",
        pt="🔥 Restam apenas <strong>7 unidades</strong> a este preço",
        ro="🔥 Mai sunt doar <strong>7 bucăți</strong> la acest preț",
    )),
    ("<strong>2 batterie in regalo = lavoro continuo senza pause.</strong>\n            Una in uso, l'altra in carica. Non ti fermi mai a metà giardino con la batteria scarica.", D(
        es="<strong>2 baterías de regalo = trabajo continuo sin pausas.</strong>\n            Una en uso, la otra cargando. Nunca te quedas a medias en el jardín con la batería agotada.",
        hu="<strong>2 akkumulátor ajándékba = folyamatos munka szünet nélkül.</strong>\n            Az egyiket használod, a másik töltődik. Soha nem állsz meg a kert közepén lemerült akkuval.",
        pl="<strong>2 baterie w prezencie = praca bez przerw.</strong>\n            Jedna w użyciu, druga się ładuje. Nigdy nie stajesz w pół ogrodu z rozładowaną baterią.",
        pt="<strong>2 baterias de oferta = trabalho contínuo sem pausas.</strong>\n            Uma em uso, a outra a carregar. Nunca paras a meio do jardim com a bateria descarregada.",
        ro="<strong>2 baterii cadou = lucru continuu fără pauze.</strong>\n            Una în uz, cealaltă la încărcat. Nu te oprești niciodată în mijlocul grădinii cu bateria descărcată.",
    )),
    ("<strong>Motore brushless 3500W — dura 3 volte di più.</strong>\n            Nessun pezzo che si consuma, nessuna manutenzione, nessun meccanico. Accende e funziona per anni.", D(
        es="<strong>Motor brushless 3500W — dura 3 veces más.</strong>\n            Ninguna pieza que se gaste, cero mantenimiento, cero mecánico. Enciende y funciona durante años.",
        hu="<strong>3500W-os brushless motor — 3-szor tovább bírja.</strong>\n            Nincs kopó alkatrész, nincs karbantartás, nincs szerelő. Beindítod, és évekig megy.",
        pl="<strong>Silnik brushless 3500W — wytrzymuje 3 razy dłużej.</strong>\n            Żadnej części, która się zużywa, zero konserwacji, zero mechanika. Włącza się i działa przez lata.",
        pt="<strong>Motor brushless 3500W — dura 3 vezes mais.</strong>\n            Nenhuma peça que se gaste, zero manutenção, zero mecânico. Liga e funciona durante anos.",
        ro="<strong>Motor brushless 3500W — rezistă de 3 ori mai mult.</strong>\n            Nicio piesă care se uzează, zero întreținere, zero mecanic. Pornește și funcționează ani de zile.",
    )),
    ("<strong>Cambio lama in 10 secondi, senza attrezzi.</strong>\n            Filo automatico, disco 40 denti, disco 3 denti, lama multifunzione. Un kit per erba, rovi, cespugli e bordi.", D(
        es="<strong>Cambio de cuchilla en 10 segundos, sin herramientas.</strong>\n            Hilo automático, disco de 40 dientes, disco de 3 dientes, cuchilla multifunción. Un kit para hierba, zarzas, arbustos y bordes.",
        hu="<strong>Pengecsere 10 másodperc alatt, szerszám nélkül.</strong>\n            Automata damil, 40 fogas tárcsa, 3 fogas tárcsa, multifunkciós penge. Egy készlet fűhöz, indákhoz, bokrokhoz és szegélyekhez.",
        pl="<strong>Wymiana tarczy w 10 sekund, bez narzędzi.</strong>\n            Automatyczna żyłka, tarcza 40 zębów, tarcza 3 zęby, tarcza wielofunkcyjna. Zestaw do trawy, ostów, krzewów i krawędzi.",
        pt="<strong>Troca de lâmina em 10 segundos, sem ferramentas.</strong>\n            Fio automático, disco de 40 dentes, disco de 3 dentes, lâmina multifunções. Um kit para erva, silvas, arbustos e bordas.",
        ro="<strong>Schimbarea lamei în 10 secunde, fără scule.</strong>\n            Fir automat, disc 40 dinți, disc 3 dinți, lamă multifuncțională. Un kit pentru iarbă, mărăcini, tufișuri și borduri.",
    )),
    ("<strong>Solo 70 dB di rumore.</strong>\n            Il decespugliatore a benzina ne fa 95–105 dB. Lavori alle 8 del sabato senza svegliare i vicini.", D(
        es="<strong>Solo 70 dB de ruido.</strong>\n            La desbrozadora de gasolina hace 95–105 dB. Trabajas a las 8 del sábado sin despertar a los vecinos.",
        hu="<strong>Csak 70 dB zaj.</strong>\n            A benzines fűkasza 95–105 dB-t ad. Szombat 8-kor dolgozhatsz anélkül, hogy felébresztenéd a szomszédokat.",
        pl="<strong>Tylko 70 dB hałasu.</strong>\n            Podkaszarka spalinowa robi 95–105 dB. Pracujesz w sobotę o 8 rano bez budzenia sąsiadów.",
        pt="<strong>Apenas 70 dB de ruído.</strong>\n            A roçadora a gasolina faz 95–105 dB. Trabalhas às 8 de sábado sem acordar os vizinhos.",
        ro="<strong>Doar 70 dB de zgomot.</strong>\n            Motocoasa pe benzină face 95–105 dB. Lucrezi sâmbătă la 8 fără să trezești vecinii.",
    )),
    ("<strong>Una ricarica costa meno di €0,15</strong>\n            Addio alle taniche di benzina miscelata con olio. Il risparmio del primo mese copre già parte del kit.", D(
        es="<strong>Una recarga cuesta menos de 0,15 €</strong>\n            Adiós a los bidones de gasolina mezclada con aceite. El ahorro del primer mes ya cubre parte del kit.",
        hu="<strong>Egy töltés kevesebb mint 0,15 €</strong>\n            Nincs többé kannányi olajjal kevert benzin. Az első hónap megtakarítása már fedezi a készlet egy részét.",
        pl="<strong>Jedno ładowanie kosztuje mniej niż 0,15 €</strong>\n            Żegnajcie kanistry benzyny zmieszanej z olejem. Oszczędność z pierwszego miesiąca już pokrywa część zestawu.",
        pt="<strong>Uma carga custa menos de 0,15 €</strong>\n            Adeus aos bidões de gasolina misturada com óleo. A poupança do primeiro mês já cobre parte do kit.",
        ro="<strong>O încărcare costă mai puțin de 0,15 €</strong>\n            Adio canistrelor de benzină amestecată cu ulei. Economia din prima lună acoperă deja o parte din kit.",
    )),
    ("Ordina Ora il Kit Completo", D(
        es="Pide ahora el kit completo",
        hu="Rendelje meg most a teljes készletet",
        pl="Zamów teraz kompletny zestaw",
        pt="Encomenda agora o kit completo",
        ro="Comandă acum kitul complet",
    )),
    ("💵 Paghi alla consegna", D(
        es="💵 Pagas al recibir",
        hu="💵 Fizetés átvételkor",
        pl="💵 Płacisz przy odbiorze",
        pt="💵 Pagas na entrega",
        ro="💵 Plătești la livrare",
    )),
    ("↩️ 30 giorni di prova", D(
        es="↩️ 30 días de prueba",
        hu="↩️ 30 napos próba",
        pl="↩️ 30 dni na wypróbowanie",
        pt="↩️ 30 dias de teste",
        ro="↩️ 30 de zile de probă",
    )),
    ("🚚 Consegna rapida", D(
        es="🚚 Entrega rápida",
        hu="🚚 Gyors szállítás",
        pl="🚚 Szybka dostawa",
        pt="🚚 Entrega rápida",
        ro="🚚 Livrare rapidă",
    )),
    ("ACQUISTO SICURO • SPEDIZIONE ESPRESSA • GARANZIA COMPLETA", D(
        es="COMPRA SEGURA • ENVÍO EXPRESS • GARANTÍA COMPLETA",
        hu="BIZTONSÁGOS VÁSÁRLÁS • EXPRESSZ SZÁLLÍTÁS • TELJES GARANCIA",
        pl="BEZPIECZNY ZAKUP • DOSTAWA EKSPRESOWA • PEŁNA GWARANCJA",
        pt="COMPRA SEGURA • ENVIO EXPRESSO • GARANTIA COMPLETA",
        ro="CUMPĂRARE SIGURĂ • LIVRARE EXPRESS • GARANȚIE COMPLETĂ",
    )),
    ("<strong>Spedizione veloce</strong><br>\n        Il pacco arriva direttamente a casa tua in 24–48 ore.", D(
        es="<strong>Envío rápido</strong><br>\n        El paquete llega a tu casa en 24–48 horas.",
        hu="<strong>Gyors szállítás</strong><br>\n        A csomag 24–48 órán belül megérkezik hozzád.",
        pl="<strong>Szybka wysyłka</strong><br>\n        Paczka trafia prosto do Ciebie w 24–48 godzin.",
        pt="<strong>Envio rápido</strong><br>\n        A encomenda chega a tua casa em 24–48 horas.",
        ro="<strong>Livrare rapidă</strong><br>\n        Coletul ajunge direct acasă în 24–48 de ore.",
    )),
    ("<strong>Paghi alla consegna</strong><br>\n        Nessun addebito anticipato: saldi solo a pacco ricevuto", D(
        es="<strong>Pagas al recibir</strong><br>\n        Sin cargo previo: pagas solo cuando llega el paquete",
        hu="<strong>Fizetés átvételkor</strong><br>\n        Nincs előzetes terhelés: csak a csomag átvételekor fizetsz",
        pl="<strong>Płacisz przy odbiorze</strong><br>\n        Bez opłaty z góry: płacisz dopiero po otrzymaniu paczki",
        pt="<strong>Pagas na entrega</strong><br>\n        Sem débito antecipado: pagas só quando a encomenda chegar",
        ro="<strong>Plătești la livrare</strong><br>\n        Fără debit anticipat: plătești doar când primești coletul",
    )),
    ("<strong>Acquisto blindato</strong><br>\n        I tuoi dati personali sono protetti al 100%", D(
        es="<strong>Compra protegida</strong><br>\n        Tus datos personales están protegidos al 100%",
        hu="<strong>Védett vásárlás</strong><br>\n        Személyes adataid 100%-ban védettek",
        pl="<strong>Zakup chroniony</strong><br>\n        Twoje dane osobowe są chronione w 100%",
        pt="<strong>Compra protegida</strong><br>\n        Os teus dados pessoais estão protegidos a 100%",
        ro="<strong>Cumpărare protejată</strong><br>\n        Datele tale personale sunt protejate 100%",
    )),
    ("<strong>Garanzia 2 anni</strong><br>\n        Puoi restituirlo senza pensieri entro 30 giorni", D(
        es="<strong>Garantía 2 años</strong><br>\n        Puedes devolverlo sin preocupaciones en 30 días",
        hu="<strong>2 év garancia</strong><br>\n        Gond nélkül visszaküldheted 30 napon belül",
        pl="<strong>Gwarancja 2 lata</strong><br>\n        Możesz go zwrócić bez stresu w ciągu 30 dni",
        pt="<strong>Garantia 2 anos</strong><br>\n        Podes devolvê-lo sem preocupações em 30 dias",
        ro="<strong>Garanție 2 ani</strong><br>\n        Îl poți returna fără griji în 30 de zile",
    )),
    ("Pezzi ancora disponibili", D(
        es="Unidades aún disponibles",
        hu="Még elérhető darabok",
        pl="Sztuki jeszcze dostępne",
        pt="Unidades ainda disponíveis",
        ro="Bucăți încă disponibile",
    )),
    ("SOLO <span>7</span> PEZZI RIMASTI", D(
        es="SOLO QUEDAN <span>7</span> UNIDADES",
        hu="MÁR CSAK <span>7</span> DARAB VAN",
        pl="ZOSTAŁO TYLKO <span>7</span> SZTUK",
        pt="RESTAM APENAS <span>7</span> UNIDADES",
        ro="MAI SUNT DOAR <span>7</span> BUCĂȚI",
    )),
    ("Il magazzino si sta svuotando in fretta!", D(
        es="¡El almacén se está vaciando rápido!",
        hu="A raktár gyorsan ürül!",
        pl="Magazyn opróżnia się w szybkim tempie!",
        pt="O armazém está a esvaziar-se depressa!",
        ro="Depozitul se golește rapid!",
    )),
    ("Proprio adesso tanti altri clienti hanno gli occhi puntati su questo prodotto: ecco perché le unità disponibili calano così in fretta.", D(
        es="Ahora mismo muchos otros clientes tienen los ojos puestos en este producto: por eso las unidades disponibles bajan tan rápido.",
        hu="Éppen most sok más vásárló figyeli ezt a terméket: ezért fogynak ilyen gyorsan a darabok.",
        pl="Właśnie teraz wielu innych klientów ma ten produkt na oku: dlatego sztuki znikają tak szybko.",
        pt="Neste momento muitos outros clientes estão de olho neste produto: é por isso que as unidades descem tão depressa.",
        ro="Chiar acum mulți alți clienți au ochii pe acest produs: de aceea unitățile disponibile scad atât de repede.",
    )),
    ("Acquista subito e mettiti al sicuro uno degli ultimi pezzi rimasti al prezzo scontato di oggi.", D(
        es="Compra ahora y asegúrate una de las últimas unidades al precio rebajado de hoy.",
        hu="Vásárolj most, és biztosítsd be magadnak az egyik utolsó darabot a mai akciós áron.",
        pl="Kup teraz i zabezpiecz jedną z ostatnich sztuk w dzisiejszej cenie promocyjnej.",
        pt="Compra já e garante uma das últimas unidades ao preço com desconto de hoje.",
        ro="Cumpără acum și asigură-ți una dintre ultimele bucăți la prețul redus de azi.",
    )),
    ("Importante!", D(
        es="¡Importante!",
        hu="Fontos!",
        pl="Ważne!",
        pt="Importante!",
        ro="Important!",
    )),
    ("Compila il modulo d’ordine", D(
        es="Rellena el formulario de pedido",
        hu="Töltse ki a rendelési űrlapot",
        pl="Wypełnij formularz zamówienia",
        pt="Preenche o formulário de encomenda",
        ro="Completează formularul de comandă",
    )),
    ("Ti contatteremo per confermare i dettagli della consegna. Paghi solo alla consegna.", D(
        es="Te contactaremos para confirmar los datos de entrega. Pagas solo al recibir.",
        hu="Felvesszük veled a kapcsolatot a szállítási adatok megerősítéséhez. Csak átvételkor fizetsz.",
        pl="Skontaktujemy się, aby potwierdzić dane dostawy. Płacisz dopiero przy odbiorze.",
        pt="Vamos contactar-te para confirmar os dados de entrega. Pagas só na entrega.",
        ro="Te contactăm pentru a confirma detaliile livrării. Plătești doar la livrare.",
    )),
    ("🔒 Nessun anticipo · Paghi solo alla consegna · Spedizione 24/48h", D(
        es="🔒 Sin anticipo · Pagas solo al recibir · Envío 24/48h",
        hu="🔒 Nincs előleg · Fizetés csak átvételkor · Szállítás 24/48 óra",
        pl="🔒 Bez zaliczki · Płacisz dopiero przy odbiorze · Dostawa 24/48h",
        pt="🔒 Sem adiantamento · Pagas só na entrega · Envio 24/48h",
        ro="🔒 Fără avans · Plătești doar la livrare · Livrare 24/48h",
    )),
    ("Utensili da giardinaggio low cost che non mantengono le promesse", D(
        es="Herramientas de jardín baratas que no cumplen lo que prometen",
        hu="Olcsó kerti szerszámok, amelyek nem tartják a szavukat",
        pl="Tanie narzędzia ogrodowe, które nie dotrzymują obietnic",
        pt="Ferramentas de jardim baratas que não cumprem o que prometem",
        ro="Unelte de grădină ieftine care nu își țin promisiunile",
    )),
    ("Quanti Soldi Hai Già Buttato in Attrezzi da Giardino Inutili?", D(
        es="¿Cuánto dinero has tirado ya en herramientas de jardín inútiles?",
        hu="Mennyi pénzt dobtál már ki haszontalan kerti szerszámokra?",
        pl="Ile pieniędzy wyrzuciłeś już na bezużyteczne narzędzia ogrodowe?",
        pt="Quanto dinheiro já deitaste fora em ferramentas de jardim inúteis?",
        ro="Câți bani ai aruncat deja pe unelte de grădină inutile?",
    )),
    ("La storia la conosci a memoria. Ordini in rete un decespugliatore a basso prezzo.\n        L'estate iniziale fila liscia. Già l'anno dopo l'accumulatore si scarica prima dei 20 minuti.\n        Al terzo giro lo trovi guasto, oppure con lame che ormai non incidono più nulla.", D(
        es="Conoces la historia de memoria. Pides online una desbrozadora barata.\n        El primer verano va bien. Al año siguiente la batería se agota antes de 20 minutos.\n        A la tercera ya está rota, o con cuchillas que ya no cortan nada.",
        hu="A történetet fejből tudod. Rendelkezel olcsó fűkaszát a neten.\n        Az első nyár simán megy. Már a következő évben az akku 20 perc előtt lemerül.\n        Harmadszorra elromlik, vagy a pengék már semmit sem vágnak.",
        pl="Znasz tę historię na pamięć. Zamawiasz w sieci tanią podkaszarkę.\n        Pierwsze lato mija gładko. Już rok później akumulator pada przed 20 minutami.\n        Za trzecim razem jest zepsuta albo tarcze nic już nie tną.",
        pt="Conheces a história de cor. Encomendas online uma roçadora barata.\n        O primeiro verão corre bem. Já no ano seguinte a bateria acaba antes dos 20 minutos.\n        À terceira está avariada, ou com lâminas que já não cortam nada.",
        ro="Știi povestea pe de rost. Comanzi online o motocoasă ieftină.\n        Prima vară merge bine. Deja anul următor acumulatorul se descarcă înainte de 20 de minute.\n        A treia oară e stricat, sau cu lame care nu mai taie nimic.",
    )),
    ("Così ne ordini un altro. E il giro riparte da capo.", D(
        es="Así que pides otra. Y el ciclo empieza otra vez.",
        hu="Szóval rendelsz egy másikat. És a kör kezdődik elölről.",
        pl="Więc zamawiasz kolejną. I koło zaczyna się od nowa.",
        pt="Então encomendas outra. E o ciclo recomeça do zero.",
        ro="Așa că o comanzi pe alta. Și cercul reîncepe de la capăt.",
    )),
    ("Nemmeno la versione a scoppio ti salva: fa un fracasso assurdo, manda odore di carburante,\n        ti pianta a terra proprio quando serve, e ogni accensione diventa una lotta\n        con la cordicella di strappo.", D(
        es="Ni la versión de gasolina te salva: hace un ruido absurdo, huele a combustible,\n        te deja tirado justo cuando la necesitas, y cada arranque es una pelea\n        con la cuerda.",
        hu="A benzines verzió sem ment meg: őrült hangos, üzemanyagszagú,\n        pont akkor hagy cserben, amikor kellene, és minden indítás harc\n        a berántózsinórral.",
        pl="Nawet spalinowa Cię nie ratuje: hałasuje jak szalona, śmierdzi paliwem,\n        staje akurat gdy jej potrzebujesz, a każde odpalenie to walka\n        ze sznurkiem rozrusznika.",
        pt="Nem a versão a gasolina te salva: faz um barulho absurdo, cheira a combustível,\n        deixa-te a pé mesmo quando precisas, e cada arranque vira uma luta\n        com o cordel.",
        ro="Nici varianta pe benzină nu te salvează: face un zgomot absurd, miroase a carburant,\n        te lasă în drum tocmai când ai nevoie, și fiecare pornire e o luptă\n        cu șnurul de smucire.",
    )),
    ("Qui non c'entra nulla la sfortuna.<br>\n          <strong>La verità è che gli utensili da pochi euro nascono per essere ricomprati — non per resistere negli anni.</strong>", D(
        es="Aquí no tiene nada que ver la mala suerte.<br>\n          <strong>La verdad es que las herramientas de pocos euros nacen para volver a comprarse — no para durar años.</strong>",
        hu="Itt nincs köze a balszerencséhez.<br>\n          <strong>Az igazság az, hogy a filléres szerszámok arra születnek, hogy újra megvedd őket — nem arra, hogy évekig bírják.</strong>",
        pl="Tu nie ma nic wspólnego ze pech.<br>\n          <strong>Prawda jest taka, że tanie narzędzia powstają po to, by kupować je od nowa — nie po to, by służyć latami.</strong>",
        pt="Aqui não tem nada a ver com azar.<br>\n          <strong>A verdade é que as ferramentas de poucos euros nascem para serem compradas outra vez — não para aguentar anos.</strong>",
        ro="Aici nu e vorba de ghinion.<br>\n          <strong>Adevărul e că uneltele de câțiva euro se nasc ca să le cumperi din nou — nu ca să reziste ani de zile.</strong>",
    )),
    ("T77 PRO e il suo motore senza spazzole", D(
        es="T77 PRO y su motor sin escobillas",
        hu="T77 PRO és a kefenélküli motorja",
        pl="T77 PRO i jego silnik bezszczotkowy",
        pt="T77 PRO e o seu motor sem escovas",
        ro="T77 PRO și motorul său fără perii",
    )),
    ("Brushless, la tecnologia che fa la differenza", D(
        es="Brushless, la tecnología que marca la diferencia",
        hu="Brushless, a technológia, ami számít",
        pl="Brushless, technologia, która robi różnicę",
        pt="Brushless, a tecnologia que faz a diferença",
        ro="Brushless, tehnologia care face diferența",
    )),
    ("Il Motore Brushless Ribalta Tutte le Regole", D(
        es="El motor brushless cambia todas las reglas",
        hu="A brushless motor felforgatja a szabályokat",
        pl="Silnik brushless odwraca wszystkie zasady",
        pt="O motor brushless vira as regras do avesso",
        ro="Motorul brushless schimbă toate regulile",
    )),
    ("Dentro un propulsore tradizionale trovi spazzole di carbonio, ed è materiale destinato a logorarsi. Passati 18-24 mesi di lavoro, la spinta cala. La temperatura sale. E prima o poi tutto si ferma.", D(
        es="Dentro de un motor tradicional hay escobillas de carbono, y ese material está hecho para desgastarse. Tras 18-24 meses de uso, la potencia baja. Sube la temperatura. Y tarde o temprano todo se para.",
        hu="Egy hagyományos motorban szénkefék vannak, és ez az anyag kopásra született. 18–24 hónap munka után a teljesítmény csökken. A hőmérséklet nő. És előbb-utóbb minden leáll.",
        pl="W tradycyjnym silniku są szczotki węglowe, a to materiał stworzony do zużycia. Po 18–24 miesiącach pracy moc spada. Temperatura rośnie. I prędzej czy później wszystko staje.",
        pt="Dentro de um motor tradicional há escovas de carbono, e esse material nasce para se gastar. Após 18-24 meses de trabalho, a potência cai. A temperatura sobe. E mais cedo ou mais tarde tudo pára.",
        ro="Într-un motor tradițional găsești perii de carbon, iar materialul ăsta e făcut să se uzeze. După 18-24 de luni de lucru, puterea scade. Temperatura crește. Și mai devreme sau mai târziu totul se oprește.",
    )),
    ("<strong>Nel brushless le spazzole non esistono proprio.</strong>\n            Zero spazzole = zero attrito interno che si consuma = zero calo di potenza con il passare delle stagioni.", D(
        es="<strong>En el brushless las escobillas no existen.</strong>\n            Cero escobillas = cero fricción interna que se gasta = cero pérdida de potencia con el paso de las temporadas.",
        hu="<strong>A brushless motorban kefék egyáltalán nincsenek.</strong>\n            Nulla kefe = nulla belső súrlódás, ami kopik = nulla teljesítménycsökkenés az évszakokkal.",
        pl="<strong>W silniku brushless szczotek po prostu nie ma.</strong>\n            Zero szczotek = zero tarcia wewnętrznego, które się zużywa = zero spadku mocy z sezonu na sezon.",
        pt="<strong>No brushless as escovas simplesmente não existem.</strong>\n            Zero escovas = zero atrito interno que se gasta = zero perda de potência com as estações.",
        ro="<strong>La brushless periile nu există deloc.</strong>\n            Zero perii = zero frecare internă care se uzează = zero scădere de putere odată cu sezoanele.",
    )),
    ("<strong>È esattamente il motore montato su T77 PRO.</strong>\n            Ecco perché la sua vita utile va ben oltre quella dei soliti tagliaerba a basso costo.", D(
        es="<strong>Es exactamente el motor montado en T77 PRO.</strong>\n            Por eso su vida útil va mucho más allá de la de los cortacéspedes baratos de siempre.",
        hu="<strong>Pontosan ez a motor van a T77 PRO-ban.</strong>\n            Ezért a hasznos élettartama messze túlmutat a szokásos olcsó fűnyírókén.",
        pl="<strong>To dokładnie ten silnik, który jest w T77 PRO.</strong>\n            Dlatego jego żywotność wykracza daleko poza zwykłe tanie kosiarki.",
        pt="<strong>É exatamente o motor montado no T77 PRO.</strong>\n            Por isso a sua vida útil vai muito além da das aparadoras baratas de sempre.",
        ro="<strong>Este exact motorul montat pe T77 PRO.</strong>\n            De aceea durata de viață trece cu mult peste a tunsoriilor ieftine obișnuite.",
    )),
    ("Vale lo stesso ragionamento che separa un propulsore a benzina da un elettrico ad alte prestazioni: meno componenti che si sfregano, resa migliore, durata superiore.", D(
        es="Es el mismo razonamiento que separa un motor de gasolina de uno eléctrico de alto rendimiento: menos piezas que rozan, mejor rendimiento, más duración.",
        hu="Ugyanaz a logika, ami a benzines motort elválasztja a nagy teljesítményű elektromostól: kevesebb dörzsölődő alkatrész, jobb hatásfok, hosszabb élettartam.",
        pl="To ta sama logika, która oddziela silnik spalinowy od elektrycznego wysokiej wydajności: mniej elementów, które się ocierają, lepsza sprawność, dłuższa żywotność.",
        pt="É o mesmo raciocínio que separa um motor a gasolina de um elétrico de alto desempenho: menos peças a esfregar, melhor rendimento, maior duração.",
        ro="E același raționament care desparte un motor pe benzină de unul electric de performanță: mai puține piese care se freacă, randament mai bun, durată mai mare.",
    )),
    ("Qui non si tratta di pubblicità. <b>Parla l'ingegneria.</b>", D(
        es="Aquí no se trata de publicidad. <b>Habla la ingeniería.</b>",
        hu="Itt nincs szó reklámról. <b>A mérnöki tudás beszél.</b>",
        pl="Tu nie chodzi o reklamę. <b>Mówi inżynieria.</b>",
        pt="Aqui não se trata de publicidade. <b>Fala a engenharia.</b>",
        ro="Aici nu e vorba de reclamă. <b>Vorbește ingineria.</b>",
    )),
    ("✅ I vantaggi concreti", D(
        es="✅ Las ventajas concretas",
        hu="✅ A kézzelfogható előnyök",
        pl="✅ Konkretne korzyści",
        pt="✅ As vantagens concretas",
        ro="✅ Avantajele concrete",
    )),
    ("Ecco il Decespugliatore che Ti Alleggerisce il Weekend", D(
        es="Esta es la desbrozadora que te aligera el fin de semana",
        hu="Íme a fűkasza, ami megkönnyíti a hétvégéd",
        pl="Oto podkaszarka, która odciąża Twój weekend",
        pt="Eis a roçadora que te alivia o fim de semana",
        ro="Iată motocoasa care îți ușurează weekendul",
    )),
    ("Ti fermi di meno, ci metti meno mani, fai molto meno baccano. E il verde torna in ordine in molto meno tempo.", D(
        es="Paras menos, pones menos las manos, haces mucho menos ruido. Y el jardín vuelve a estar en orden en mucho menos tiempo.",
        hu="Kevesebbet állsz meg, kevesebbet nyúlsz hozzá, sokkal kevesebb a zaj. És a zöld sokkal hamarabb rendben van.",
        pl="Rzadziej się zatrzymujesz, mniej się męczysz, hałasu jest znacznie mniej. A zieleń wraca do porządku znacznie szybciej.",
        pt="Paras menos, metes menos as mãos, fazes muito menos barulho. E o verde volta a ficar em ordem em muito menos tempo.",
        ro="Te oprești mai puțin, pui mai puține mâini, faci mult mai puțin zgomot. Și verdele revine în ordine în mult mai puțin timp.",
    )),
    ("Prato sistemato in tempi rapidi", D(
        es="Césped listo en poco tiempo",
        hu="Gyep rendben rövid idő alatt",
        pl="Trawnik ogarnięty w krótkim czasie",
        pt="Relvado arranjado em pouco tempo",
        ro="Gazon pus la punct în timp scurt",
    )),
    ("Basta Weekend Sacrificati in Giardino", D(
        es="Se acabaron los fines de semana sacrificados en el jardín",
        hu="Vége a kertben feláldozott hétvégéknek",
        pl="Koniec z weekendami poświęconymi ogrodowi",
        pt="Chega de fins de semana sacrificados no jardim",
        ro="Gata cu weekendurile sacrificate în grădină",
    )),
    ("Se lo strumento corre e non ti obbliga a soste continue, curare il verde smette di pesarti addosso. Hai 2 batterie e 4 lame che si scambiano al volo: passi da un tipo di taglio all'altro senza mai fermarti per ricaricare o per andare a prendere un altro attrezzo.", D(
        es="Si la herramienta corre y no te obliga a parar sin cesar, cuidar el jardín deja de pesarte. Tienes 2 baterías y 4 cuchillas que se cambian al vuelo: pasas de un tipo de corte a otro sin parar a cargar ni a buscar otra herramienta.",
        hu="Ha a szerszám megy, és nem kényszerít folytonos megállásra, a kertápolás nem nehezedik rád. 2 akkud és 4 pengéd van, amik röptében cserélhetők: egyik vágásról a másikra váltasz anélkül, hogy töltenél vagy másik szerszámért mennél.",
        pl="Jeśli narzędzie działa i nie zmusza Cię do ciągłych przerw, pielęgnacja ogrodu przestaje ciążyć. Masz 2 baterie i 4 tarcze wymieniane w lot: przechodzisz z jednego cięcia na drugie bez zatrzymywania się na ładowanie ani po inne narzędzie.",
        pt="Se a ferramenta corre e não te obriga a paragens contínuas, cuidar do verde deixa de pesar. Tens 2 baterias e 4 lâminas que se trocam a voar: passas de um tipo de corte para outro sem parar para carregar nem ir buscar outra ferramenta.",
        ro="Dacă unealta merge și nu te obligă la opriri continue, îngrijirea verdelui nu te mai apasă. Ai 2 baterii și 4 lame care se schimbă din zbor: treci de la un tip de tăiere la altul fără să te oprești să încarci sau să iei altă unealtă.",
    )),
    ("Un terreno da 300m² chiuso in meno di un'ora.", D(
        es="Un terreno de 300 m² listo en menos de una hora.",
        hu="300 m²-es telek kevesebb mint egy óra alatt kész.",
        pl="Działka 300 m² ogarnięta w mniej niż godzinę.",
        pt="Um terreno de 300 m² concluído em menos de uma hora.",
        ro="Un teren de 300 m² gata în mai puțin de o oră.",
    )),
    ("Come impieghi le ore che ti restano, decidi tu.", D(
        es="Cómo usas las horas que te quedan, lo decides tú.",
        hu="A maradék óráidat te döntöd el, mire fordítod.",
        pl="Jak spędzisz pozostałe godziny, decydujesz Ty.",
        pt="Como usas as horas que te restam, decides tu.",
        ro="Cum folosești orele care îți rămân, decizi tu.",
    )),
    ("Decespugliatore che non chiede manutenzione", D(
        es="Desbrozadora que no pide mantenimiento",
        hu="Fűkasza, ami nem kér karbantartást",
        pl="Podkaszarka, która nie wymaga konserwacji",
        pt="Roçadora que não pede manutenção",
        ro="Motocoasă care nu cere întreținere",
    )),
    ("La Tua Ultima Fattura di Riparazione per un Decespugliatore", D(
        es="Tu última factura de reparación de una desbrozadora",
        hu="Az utolsó javítási számlád egy fűkaszára",
        pl="Twój ostatni rachunek za naprawę podkaszarki",
        pt="A tua última fatura de reparação de uma roçadora",
        ro="Ultima ta factură de reparație pentru o motocoasă",
    )),
    ("Dentro il brushless non c'è nulla che si logori. E ciascuna batteria si cambia da sola — nessun obbligo di riacquistare l'intero kit.", D(
        es="Dentro del brushless no hay nada que se desgaste. Y cada batería se cambia sola: no tienes que volver a comprar el kit entero.",
        hu="A brushlessben nincs mit kopnia. És minden akku külön cserélhető — nem kell az egész készletet újra megvenni.",
        pl="W silniku brushless nie ma nic, co by się zużywało. A każdą baterię wymieniasz osobno — bez obowiązku kupowania całego zestawu od nowa.",
        pt="Dentro do brushless não há nada que se gaste. E cada bateria troca-se à parte — sem obrigação de voltar a comprar o kit inteiro.",
        ro="În brushless nu e nimic care să se uzeze. Și fiecare baterie se schimbă separat — fără să cumperi tot kitul din nou.",
    )),
    ("Pezzi facili da trovare. Spese ridotte. Grattacapi in meno.", D(
        es="Piezas fáciles de encontrar. Gastos bajos. Menos quebraderos de cabeza.",
        hu="Könnyen beszerezhető alkatrészek. Alacsony költség. Kevesebb fejfájás.",
        pl="Części łatwe do zdobycia. Niższe wydatki. Mniej zmartwień.",
        pt="Peças fáceis de encontrar. Despesas baixas. Menos dores de cabeça.",
        ro="Piese ușor de găsit. Cheltuieli reduse. Mai puține bătăi de cap.",
    )),
    ("Le lame seguono la misura universale: le reperisci in rete oppure dal ferramenta sotto casa. A tre anni dall'acquisto di questo kit, la manutenzione ti sarà costata zero euro.", D(
        es="Las cuchillas siguen la medida universal: las encuentras online o en la ferretería de debajo de casa. A los tres años de comprar este kit, el mantenimiento te habrá costado cero euros.",
        hu="A pengék univerzális méretűek: megtalálod neten vagy a sarki vasboltban. A készlet megvétele után három évvel a karbantartás nulla euródba került.",
        pl="Tarcze mają uniwersalny rozmiar: kupisz je w sieci albo w sklepie żelaznym za rogiem. Trzy lata po zakupie tego zestawu konserwacja kosztowała Cię zero euro.",
        pt="As lâminas seguem a medida universal: encontras-nas online ou na ferragem aqui ao lado. Três anos após comprar este kit, a manutenção terá custado zero euros.",
        ro="Lamele respectă măsura universală: le găsești online sau la magazinul de scule de lângă casă. La trei ani de la cumpărarea acestui kit, întreținerea te-a costat zero euro.",
    )),
    ("Tagliaerba a basso rumore per il giardino", D(
        es="Cortacésped de bajo ruido para el jardín",
        hu="Alacsony zajú fűnyíró a kertbe",
        pl="Cicha kosa do ogrodu",
        pt="Corta-relva de baixo ruído para o jardim",
        ro="Mașină de tuns iarba silențioasă pentru grădină",
    )),
    ("Tagli All'Ora che Preferisci. Senza Scusarti con i Vicini.", D(
        es="Corta a la hora que quieras. Sin disculparte con los vecinos.",
        hu="Vágj akkor, amikor neked jó. Szomszédok előtt mentegetőzés nélkül.",
        pl="Tnij o dowolnej porze. Bez przeprosin wobec sąsiadów.",
        pt="Corta à hora que preferires. Sem te desculpares com os vizinhos.",
        ro="Taie la ora care îți convine. Fără scuze față de vecini.",
    )),
    ("Siamo su 70 dB, quanto due persone che discutono con foga. Un modello a benzina in funzione viaggia invece tra i 95-105 dB: praticamente un martello pneumatico.", D(
        es="Estamos en 70 dB, como dos personas discutiendo con ganas. Un modelo de gasolina en marcha va entre 95 y 105 dB: prácticamente un martillo neumático.",
        hu="70 dB-en vagyunk, mint két ember, aki hevesen vitatkozik. Egy benzines modell 95–105 dB között megy: gyakorlatilag egy légkalapács.",
        pl="Mamy 70 dB, jak dwie osoby kłócące się z zapałem. Spalinowy model w ruchu to 95–105 dB: praktycznie młot pneumatyczny.",
        pt="Estamos nos 70 dB, como duas pessoas a discutir com força. Um modelo a gasolina em funcionamento anda entre 95-105 dB: praticamente um martelo pneumático.",
        ro="Suntem la 70 dB, cât două persoane care discută cu aprindere. Un model pe benzină în funcțiune merge între 95-105 dB: practic un ciocan pneumatic.",
    )),
    ("Parti alle 8 di sabato lasciando dormire tutto il palazzo.", D(
        es="Empiezas a las 8 del sábado y dejas dormir a todo el edificio.",
        hu="Szombat 8-kor kezdesz, és hagyod aludni az egész házat.",
        pl="Zaczynasz w sobotę o 8 i pozwalasz spać całemu blokowi.",
        pt="Começas às 8 de sábado e deixas dormir o prédio inteiro.",
        ro="Pornești sâmbătă la 8 și lași tot blocul să doarmă.",
    )),
    ("T77 PRO ti lascia rifinire accanto alle aiuole senza cuffie antirumore e senza proteste di nessuno. Prendersi cura del giardino torna a essere un piacere.", D(
        es="T77 PRO te deja perfilar junto a los parterres sin cascos antirruido y sin protestas de nadie. Cuidar el jardín vuelve a ser un placer.",
        hu="A T77 PRO-val a virágágyások mellett is vághatsz füldugó és panasz nélkül. A kertápolás újra élvezet.",
        pl="T77 PRO pozwala wykańczać przy rabatach bez nauszników i bez protestów. Pielęgnacja ogrodu znów sprawia przyjemność.",
        pt="O T77 PRO deixa-te aparar junto aos canteiros sem auscultadores e sem protestos. Cuidar do jardim volta a ser um prazer.",
        ro="T77 PRO te lasă să finișezi lângă straturi fără căști antifonice și fără proteste. Îngrijirea grădinii devine din nou o plăcere.",
    )),
    ("Prendi Adesso il Tuo T77 PRO ↓", D(
        es="Coge ya tu T77 PRO ↓",
        hu="Vedd meg most a T77 PRO-dat ↓",
        pl="Weź teraz swój T77 PRO ↓",
        pt="Leva já o teu T77 PRO ↓",
        ro="Ia-ți acum T77 PRO ↓",
    )),
    ("💵 Paghi quando arriva", D(
        es="💵 Pagas cuando llega",
        hu="💵 Fizetsz, amikor megérkezik",
        pl="💵 Płacisz, gdy dotrze",
        pt="💵 Pagas quando chega",
        ro="💵 Plătești când ajunge",
    )),
    ("🚚 Consegna in 24/48h", D(
        es="🚚 Entrega en 24/48h",
        hu="🚚 Szállítás 24/48 óra",
        pl="🚚 Dostawa w 24/48h",
        pt="🚚 Entrega em 24/48h",
        ro="🚚 Livrare în 24/48h",
    )),
    ("↩️ Provalo per 30 giorni", D(
        es="↩️ Pruébalo 30 días",
        hu="↩️ Próbáld ki 30 napig",
        pl="↩️ Wypróbuj przez 30 dni",
        pt="↩️ Experimenta durante 30 dias",
        ro="↩️ Probați-l 30 de zile",
    )),
    ("⭐ Recensioni vere", D(
        es="⭐ Reseñas reales",
        hu="⭐ Valódi értékelések",
        pl="⭐ Prawdziwe opinie",
        pt="⭐ Avaliações reais",
        ro="⭐ Recenzii reale",
    )),
    ("Chi lo Prova Non Ci Rinuncia Più", D(
        es="Quien lo prueba ya no lo suelta",
        hu="Aki kipróbálja, nem adja oda többé",
        pl="Kto spróbuje, już nie odda",
        pt="Quem experimenta já não larga",
        ro="Cine îl încearcă nu se mai lasă",
    )),
    ("C'è chi abbandona il motore a scoppio e chi ha già sprecato denaro in versioni low cost: ecco cosa porta gli uni e gli altri a scegliere T77 PRO.", D(
        es="Hay quien deja el motor de gasolina y quien ya ha tirado dinero en versiones baratas: esto es lo que lleva a unos y a otros a elegir T77 PRO.",
        hu="Van, aki otthagyja a benzines motort, és van, aki már olcsó verziókra költött: ez viszi mindkettőt a T77 PRO-hoz.",
        pl="Jedni porzucają silnik spalinowy, inni już zmarnowali pieniądze na tanie wersje: oto, co skłania jednych i drugich do wyboru T77 PRO.",
        pt="Há quem deixe o motor a gasolina e quem já tenha deitado dinheiro em versões baratas: eis o que leva uns e outros a escolher o T77 PRO.",
        ro="Unii lasă motorul pe benzină, alții au aruncat deja bani pe versiuni ieftine: iată ce îi aduce pe unii și pe alții la T77 PRO.",
    )),
]


# Continued in pack2 to keep file readable — merged at runtime below.
PACK2: list[tuple[str, dict[str, str]]] = [
    ("Lorenzo B. racconta la sua esperienza con T77 PRO", D(
        es="Carlos B. cuenta su experiencia con T77 PRO",
        hu="Péter B. meséli a T77 PRO-val szerzett tapasztalatát",
        pl="Piotr B. opowiada o swoich wrażeniach z T77 PRO",
        pt="João B. conta a experiência com o T77 PRO",
        ro="Andrei B. povestește experiența cu T77 PRO",
    )),
    ("Valentina R. e la sua opinione su T77 PRO", D(
        es="Laura R. y su opinión sobre T77 PRO",
        hu="Anna R. véleménye a T77 PRO-ról",
        pl="Anna R. i jej opinia o T77 PRO",
        pt="Ana R. e a opinião sobre o T77 PRO",
        ro="Elena R. și părerea ei despre T77 PRO",
    )),
    ("L'esperienza di Maurizio C. con T77 PRO", D(
        es="La experiencia de Miguel C. con T77 PRO",
        hu="Gábor C. tapasztalata a T77 PRO-val",
        pl="Doświadczenie Marka C. z T77 PRO",
        pt="A experiência do Miguel C. com o T77 PRO",
        ro="Experiența lui Mihai C. cu T77 PRO",
    )),
    ("Lorenzo B.", D(es="Carlos B.", hu="Péter B.", pl="Piotr B.", pt="João B.", ro="Andrei B.")),
    ("Valentina R.", D(es="Laura R.", hu="Anna R.", pl="Anna R.", pt="Ana R.", ro="Elena R.")),
    ("Maurizio C.", D(es="Miguel C.", hu="Gábor C.", pl="Marek C.", pt="Miguel C.", ro="Mihai C.")),
    ("“Ho passato oltre dieci anni a tirare la cordicella di un modello a scoppio. Quando ho dovuto far sistemare l'avviamento per l'ennesima volta, ho mollato. Questo kit l'ho ordinato più per stanchezza che per convinzione, aspettandomi la solita delusione. Invece mi sono ricreduto: prato chiuso in un'unica passata, lame che si cambiano in un attimo e la seconda batteria già pronta quando serviva. Della benzina non sento più la mancanza.”", D(
        es="“Llevaba más de diez años tirando de la cuerda de un modelo de gasolina. Cuando tuve que reparar el arranque por enésima vez, lo dejé. Pedí este kit más por cansancio que por convicción, esperando el decepción de siempre. Me equivoqué: césped listo de una pasada, cuchillas que se cambian en un momento y la segunda batería lista cuando hacía falta. La gasolina ya no la echo de menos.”",
        hu="“Több mint tíz évig rángattam egy benzines berántózsinórját. Amikor az ennyiedik alkalommal kellett javíttatni az indítást, feladtam. Ezt a készletet inkább fáradtságból rendeltem, mint meggyőződésből, a szokásos csalódásra számítva. Tévedtem: a gyep egy menetben kész, a pengék pillanatok alatt cserélhetők, a második akku pedig ott volt, amikor kellett. A benzint már nem hiányolom.”",
        pl="“Ponad dziesięć lat szarpałem sznurek spalinowego modelu. Gdy po raz kolejny musiałem naprawiać rozrusznik, odpuściłem. Ten zestaw zamówiłem raczej ze zmęczenia niż z przekonania, spodziewając się zwykłego rozczarowania. Pomyliłem się: trawnik ogarnięty za jednym razem, tarcze zmieniane w okamgnieniu, a druga bateria gotowa, gdy była potrzebna. Benzyny już nie brakuje.”",
        pt="“Passei mais de dez anos a puxar o cordel de um modelo a gasolina. Quando tive de arranjar o arranque pela enésima vez, desisti. Encomendei este kit mais por cansaço do que por convicção, à espera do desapontamento de sempre. Enganei-me: relvado concluído numa só passagem, lâminas trocadas num instante e a segunda bateria pronta quando fazia falta. Da gasolina já não sinto falta.”",
        ro="“Am petrecut peste zece ani trăgând de șnurul unui model pe benzină. Când a trebuit să repar pornirea a nu știu câta oară, am renunțat. Am comandat kitul mai din oboseală decât din convingere, așteptând dezamăgirea obișnuită. M-am înșelat: gazon gata dintr-o singură trecere, lame schimbate instant și a doua baterie gata când trebuia. De benzină nu-mi mai e dor.”",
    )),
    ("“A farmi decidere è stato proprio il motore brushless. Prima ne avevo presi due a poco prezzo e si erano fermati tutti e due dopo la seconda estate. Questo invece sta affrontando la terza stagione e va come il primo giorno fuori dalla confezione. Montando il disco a 40 denti l'autonomia resta ancora sopra i 40 minuti. Mi rimane solo il rammarico di non averlo comprato prima.”", D(
        es="“Lo que me decidió fue el motor brushless. Antes había comprado dos baratos y los dos se pararon tras el segundo verano. Este va por la tercera temporada y funciona como el primer día. Con el disco de 40 dientes la autonomía sigue por encima de 40 minutos. Solo lamento no haberlo comprado antes.”",
        hu="“A brushless motor döntött el. Előtte vettem kettőt olcsón, és mindkettő megállt a második nyár után. Ez a harmadik szezont bírja, és úgy megy, mint az első napon. A 40 fogas tárcsával az üzemidő még mindig 40 perc felett van. Csak azt bánom, hogy nem vettem meg korábban.”",
        pl="“Przekonał mnie właśnie silnik brushless. Wcześniej wzięłam dwie tanie i obie padły po drugiej wiośnie. Ta idzie w trzeci sezon i działa jak pierwszego dnia. Z tarczą 40 zębów autonomia nadal przekracza 40 minut. Żal tylko, że nie kupiłam wcześniej.”",
        pt="“O que me fez decidir foi o motor brushless. Antes tinha comprado duas baratas e as duas pararam depois do segundo verão. Esta está na terceira época e vai como no primeiro dia. Com o disco de 40 dentes a autonomia continua acima dos 40 minutos. Só lamento não a ter comprado antes.”",
        ro="“M-a convins motorul brushless. Înainte luase două ieftine și amândouă s-au oprit după a doua vară. Asta trece prin al treilea sezon și merge ca în prima zi. Cu discul de 40 de dinți autonomia rămâne peste 40 de minute. Îmi pare rău doar că nu l-am cumpărat mai devreme.”",
    )),
    ("“Sono arrivato a 64 anni e mi bastavano trenta minuti di giardino per ritrovarmi la schiena a pezzi. Con l'imbragatura in dotazione sono andato avanti sessanta minuti senza nemmeno accorgermene. Bastano appena 1,2 kg per ribaltare la situazione: o chiudi contento, o chiudi distrutto. Adesso ci lavora perfino mia moglie.”", D(
        es="“Tengo 64 años y con treinta minutos de jardín la espalda me quedaba hecha polvo. Con el arnés de serie seguí sesenta minutos sin ni enterarme. Bastan 1,2 kg para cambiarlo todo: o acabas contento, o acabas destrozado. Ahora incluso trabaja mi mujer.”",
        hu="“64 éves vagyok, és harminc perc kert után a hátam darabokban volt. A mellékelt hevederrel hatvan percig mentem, észre sem vettem. 1,2 kg elég, hogy megfordítsa a helyzetet: vagy elégedetten zársz, vagy szétcsapva. Most már a feleségem is dolgozik vele.”",
        pl="“Mam 64 lata i wystarczyło trzydzieści minut w ogrodzie, żebym miał plecy w strzępach. Z szelkami z zestawu pracowałem sześćdziesiąt minut i nawet nie zauważyłem. Wystarczy 1,2 kg, by odwrócić sytuację: albo kończysz zadowolony, albo rozbity. Teraz pracuje nim nawet żona.”",
        pt="“Cheguei aos 64 anos e bastavam trinta minutos de jardim para ficar com as costas em pedaços. Com o cinto incluído fui sessenta minutos sem sequer dar por isso. Chegam 1,2 kg para virar a situação: ou acabas contente, ou acabas destruído. Agora até a minha mulher trabalha com ele.”",
        ro="“Am ajuns la 64 de ani și îmi ajungeau treizeci de minute de grădină ca să am spatele făcut praf. Cu hamul din pachet am ținut șaizeci de minute fără să-mi dau seama. Ajung 1,2 kg ca să schimbe totul: ori termini mulțumit, ori termini zdrobit. Acum lucrează cu el până și soția.”",
    )),
    ("✅ Benzina archiviata", D(
        es="✅ Gasolina archivada",
        hu="✅ Benzin lezárva",
        pl="✅ Benzyna odłożona",
        pt="✅ Gasolina arquivada",
        ro="✅ Benzina arhivată",
    )),
    ("✅ Resiste negli anni", D(
        es="✅ Aguanta los años",
        hu="✅ Bírja az éveket",
        pl="✅ Wytrzymuje lata",
        pt="✅ Aguenta os anos",
        ro="✅ Rezistă anii",
    )),
    ("✅ Non affatica la schiena", D(
        es="✅ No cansa la espalda",
        hu="✅ Nem fárasztja a hátat",
        pl="✅ Nie męczy pleców",
        pt="✅ Não cansa as costas",
        ro="✅ Nu obosește spatele",
    )),
    ("📦 Il contenuto del kit", D(
        es="📦 Contenido del kit",
        hu="📦 A készlet tartalma",
        pl="📦 Zawartość zestawu",
        pt="📦 Conteúdo do kit",
        ro="📦 Conținutul kitului",
    )),
    ("C'è Già Tutto nella Confezione.<br>\n        Niente Spese Extra. Niente Sorprese.", D(
        es="Ya está todo en la caja.<br>\n        Sin gastos extra. Sin sorpresas.",
        hu="Minden benne van a dobozban.<br>\n        Nincs extra költség. Nincs meglepetés.",
        pl="W paczce jest już wszystko.<br>\n        Bez dodatkowych kosztów. Bez niespodzianek.",
        pt="Já está tudo na embalagem.<br>\n        Sem gastos extra. Sem surpresas.",
        ro="Totul e deja în cutie.<br>\n        Fără cheltuieli extra. Fără surprize.",
    )),
    ("Apri il pacco, assembli in 3 minuti e cominci a tagliare. Non serve altro.", D(
        es="Abres el paquete, montas en 3 minutos y empiezas a cortar. No hace falta nada más.",
        hu="Kinyitod a csomagot, 3 perc alatt összerakod, és vágsz. Semmi más nem kell.",
        pl="Otwierasz paczkę, składasz w 3 minuty i zaczynasz ciąć. Nic więcej nie trzeba.",
        pt="Abres a embalagem, montas em 3 minutos e começas a cortar. Não é preciso mais nada.",
        ro="Deschizi coletul, asamblezi în 3 minute și începi să tai. Nu trebuie nimic altceva.",
    )),
    ("Cosa c'è dentro", D(
        es="Qué hay dentro",
        hu="Mi van benne",
        pl="Co jest w środku",
        pt="O que está dentro",
        ro="Ce e înăuntru",
    )),
    ("Perché Ti Serve Davvero", D(
        es="Por qué te hace falta de verdad",
        hu="Miért van rá tényleg szükséged",
        pl="Dlaczego naprawdę Ci potrzebne",
        pt="Porque é que realmente precisas",
        ro="De ce îți trebuie cu adevărat",
    )),
    ("⚙️ Unità centrale con motore brushless 21V", D(
        es="⚙️ Unidad central con motor brushless 21V",
        hu="⚙️ Központi egység 21V-os brushless motorral",
        pl="⚙️ Jednostka centralna z silnikiem brushless 21V",
        pt="⚙️ Unidade central com motor brushless 21V",
        ro="⚙️ Unitate centrală cu motor brushless 21V",
    )),
    ("Propulsore che non chiede manutenzione e regge negli anni — il cuore di tutto", D(
        es="Motor que no pide mantenimiento y aguanta años — el corazón de todo",
        hu="Motor, ami nem kér karbantartást és bírja az éveket — mindennek a szíve",
        pl="Napęd bez konserwacji, który służy latami — serce całości",
        pt="Motor que não pede manutenção e aguenta anos — o coração de tudo",
        ro="Motor care nu cere întreținere și ține anii — inima tuturor",
    )),
    ("🔋 2 batterie LiPo da 21V in dotazione", D(
        es="🔋 2 baterías LiPo de 21V incluidas",
        hu="🔋 2 darab 21V-os LiPo akku a csomagban",
        pl="🔋 2 baterie LiPo 21V w zestawie",
        pt="🔋 2 baterias LiPo de 21V incluídas",
        ro="🔋 2 baterii LiPo de 21V incluse",
    )),
    ("Mentre una è in uso, l'altra torna carica — non ti fermi mai", D(
        es="Mientras una está en uso, la otra se recarga — no paras nunca",
        hu="Amíg az egyiket használod, a másik töltődik — soha nem állsz meg",
        pl="Gdy jedna pracuje, druga się ładuje — nigdy się nie zatrzymujesz",
        pt="Enquanto uma está em uso, a outra carrega — nunca paras",
        ro="Cât una e în uz, cealaltă se încarcă — nu te oprești niciodată",
    )),
    ("⚡ Caricabatterie veloce da 60–90 min", D(
        es="⚡ Cargador rápido de 60–90 min",
        hu="⚡ Gyors töltő 60–90 perc",
        pl="⚡ Szybka ładowarka 60–90 min",
        pt="⚡ Carregador rápido de 60–90 min",
        ro="⚡ Încărcător rapid de 60–90 min",
    )),
    ("La metti sotto carica a pranzo e nel pomeriggio riparti subito", D(
        es="La pones a cargar a mediodía y por la tarde vuelves a empezar",
        hu="Ebédnél bedugod, délután már újra indulsz",
        pl="Wkładasz do ładowania w porze obiadu i po południu ruszasz dalej",
        pt="Pões a carregar ao almoço e à tarde partes já",
        ro="O pui la încărcat la prânz și după-amiază o iei de la capăt",
    )),
    ("🌿 Testina automatica a filo", D(
        es="🌿 Cabezal automático de hilo",
        hu="🌿 Automata damilfej",
        pl="🌿 Automatyczna głowica żyłkowa",
        pt="🌿 Cabeça automática de fio",
        ro="🌿 Cap automat cu fir",
    )),
    ("Perfetta su erba alta e per bordature nette — filo da 1,6mm di misura universale", D(
        es="Perfecta en hierba alta y para bordes nítidos — hilo de 1,6 mm de medida universal",
        hu="Tökéletes magas fűre és éles szegélyekre — 1,6 mm-es univerzális damil",
        pl="Idealna na wysoką trawę i czyste krawędzie — żyłka 1,6 mm uniwersalna",
        pt="Perfeita em erva alta e para bordas nítidas — fio de 1,6 mm de medida universal",
        ro="Perfectă pe iarbă înaltă și pentru borduri clare — fir de 1,6 mm măsură universală",
    )),
    ("🪚 Lama in metallo a 40 denti", D(
        es="🪚 Cuchilla de metal de 40 dientes",
        hu="🪚 40 fogas fém penge",
        pl="🪚 Metalowa tarcza 40 zębów",
        pt="🪚 Lâmina de metal de 40 dentes",
        ro="🪚 Lamă metalică cu 40 de dinți",
    )),
    ("Affronta arbusti, rovi e sterpaglia coriacea — passa ovunque", D(
        es="Afronta arbustos, zarzas y maleza dura — pasa por todas partes",
        hu="Bírja a bokrokat, indákat és kemény bozótot — mindenhová befér",
        pl="Radzi sobie z krzewami, ostami i twardymi zaroślami — przechodzi wszędzie",
        pt="Enfrenta arbustos, silvas e mato duro — passa em todo o lado",
        ro="Face față tufișurilor, mărăcinilor și vegetației dure — trece oriunde",
    )),
    ("🔩 Lama d'acciaio a 3 denti", D(
        es="🔩 Cuchilla de acero de 3 dientes",
        hu="🔩 3 fogas acél penge",
        pl="🔩 Stalowa tarcza 3 zęby",
        pt="🔩 Lâmina de aço de 3 dentes",
        ro="🔩 Lamă de oțel cu 3 dinți",
    )),
    ("Pensata per ceppi e radici — l'utensile dei lavori pesanti", D(
        es="Pensada para tocones y raíces — la herramienta de los trabajos duros",
        hu="Tuskókra és gyökerekre — a nehéz munkák szerszáma",
        pl="Do pniaków i korzeni — narzędzie do ciężkiej roboty",
        pt="Pensada para cepos e raízes — a ferramenta dos trabalhos pesados",
        ro="Gândită pentru cioate și rădăcini — unealta lucrărilor grele",
    )),
    ("✂️ Lama multiuso", D(
        es="✂️ Cuchilla multiusos",
        hu="✂️ Multifunkciós penge",
        pl="✂️ Tarcza wielofunkcyjna",
        pt="✂️ Lâmina multiusos",
        ro="✂️ Lamă multifuncțională",
    )),
    ("Per rifiniture accurate sui prati più fitti", D(
        es="Para acabados precisos en los céspedes más densos",
        hu="Pontos kidolgozáshoz a legsűrűbb gyepen",
        pl="Do precyzyjnego wykańczania najgęstszych trawników",
        pt="Para acabamentos precisos nos relvados mais densos",
        ro="Pentru finisaje precise pe cele mai dese gazonuri",
    )),
    ("🎽 Bretellaggio regolabile + ruote d'appoggio", D(
        es="🎽 Arnés regulable + ruedas de apoyo",
        hu="🎽 Állítható heveder + támasztókerekek",
        pl="🎽 Regulowane szelki + kółka podporowe",
        pt="🎽 Arnês regulável + rodas de apoio",
        ro="🎽 Ham reglabil + roți de sprijin",
    )),
    ("Ripartisce il carico — vai avanti per ore senza sentire le braccia", D(
        es="Reparte el peso — sigues horas sin notar los brazos",
        hu="Elosztja a terhet — órákig mész anélkül, hogy éreznéd a karod",
        pl="Rozkłada obciążenie — pracujesz godzinami bez zmęczonych ramion",
        pt="Repartilha o peso — segues horas sem sentir os braços",
        ro="Împarte greutatea — ții ore fără să simți brațele",
    )),
    ("🧵 Filo di scorta in 5 colori", D(
        es="🧵 Hilo de recambio en 5 colores",
        hu="🧵 Tartalék damil 5 színben",
        pl="🧵 Zapasowa żyłka w 5 kolorach",
        pt="🧵 Fio de reserva em 5 cores",
        ro="🧵 Fir de rezervă în 5 culori",
    )),
    ("Compatibilità con lo standard universale — non rimani mai a secco", D(
        es="Compatible con el estándar universal — nunca te quedas sin hilo",
        hu="Univerzális szabvány — soha nem maradsz damil nélkül",
        pl="Zgodność z uniwersalnym standardem — nigdy nie zostaniesz bez żyłki",
        pt="Compatível com o padrão universal — nunca ficas sem fio",
        ro="Compatibil cu standardul universal — nu rămâi niciodată fără fir",
    )),
    ("❓ Le domande più comuni", D(
        es="❓ Las preguntas más frecuentes",
        hu="❓ A leggyakoribb kérdések",
        pl="❓ Najczęstsze pytania",
        pt="❓ As perguntas mais comuns",
        ro="❓ Cele mai frecvente întrebări",
    )),
    ("Qualche Perplessità? Ci Sta.<br>\n        Chiariamo Tutto Qui.", D(
        es="¿Alguna duda? Es normal.<br>\n        Lo aclaramos todo aquí.",
        hu="Van kérdésed? Rendben van.<br>\n        Itt mindent tisztázunk.",
        pl="Masz wątpliwości? To normalne.<br>\n        Wyjaśniamy wszystko tutaj.",
        pt="Alguma dúvida? É normal.<br>\n        Esclarecemos tudo aqui.",
        ro="Ai nelămuriri? E firesc.<br>\n        Clarificăm totul aici.",
    )),
    ("Prima che tu faccia l'ordine, trovi qui le risposte sui dubbi ricorrenti: forza di taglio, autonomia, modalità di pagamento e garanzia.", D(
        es="Antes de hacer el pedido, aquí tienes las respuestas a las dudas habituales: fuerza de corte, autonomía, forma de pago y garantía.",
        hu="Mielőtt megrendeled, itt megtalálod a gyakori kérdésekre a választ: vágóerő, üzemidő, fizetés és garancia.",
        pl="Zanim złożysz zamówienie, znajdziesz tu odpowiedzi na powtarzające się wątpliwości: siła cięcia, autonomia, płatność i gwarancja.",
        pt="Antes de fazeres a encomenda, encontras aqui as respostas às dúvidas habituais: força de corte, autonomia, pagamento e garantia.",
        ro="Înainte să comanzi, găsești aici răspunsurile la nelămuririle obișnuite: forță de tăiere, autonomie, plată și garanție.",
    )),
    ("In passato ho preso decespugliatori a batteria che mi hanno lasciato a piedi.", D(
        es="En el pasado compré desbrozadoras a batería que me dejaron tirado.",
        hu="Korábban vettem akkumulátoros fűkaszákat, amik cserbenhagytak.",
        pl="Wcześniej brałem akumulatorowe podkaszarki, które zostawiły mnie na lodzie.",
        pt="No passado comprei roçadoras a bateria que me deixaram a pé.",
        ro="În trecut am luat motocoase cu baterie care m-au lăsat pe jos.",
    )),
    ("Ci crediamo. Quasi tutti montano motori a spazzole, che si logorano già intorno ai 18 mesi.\n          Su T77 PRO c'è invece un brushless privo di spazzole: la durata arriva a essere 3 volte superiore.\n          Il salto è quello fra un oggetto da buttare e un utensile costruito per resistere.", D(
        es="Te creemos. Casi todas montan motores de escobillas, que se desgastan hacia los 18 meses.\n          En T77 PRO hay un brushless sin escobillas: la duración llega a ser 3 veces mayor.\n          Es el salto entre un objeto para tirar y una herramienta hecha para durar.",
        hu="Elhisszük. Szinte mind kefés motort használ, ami 18 hónap körül kopik.\n          A T77 PRO-ban viszont kefenélküli brushless van: az élettartam akár 3-szoros.\n          Ez a különbség egy kidobnivaló tárgy és egy tartós szerszám között.",
        pl="Wierzymy. Prawie wszystkie mają silniki szczotkowe, które zużywają się koło 18 miesięcy.\n          W T77 PRO jest brushless bez szczotek: żywotność bywa 3 razy dłuższa.\n          To skok między rzeczą do wyrzucenia a narzędziem zbudowanym, by wytrzymać.",
        pt="Acreditamos. Quase todas montam motores de escovas, que se gastam por volta dos 18 meses.\n          No T77 PRO há um brushless sem escovas: a duração chega a ser 3 vezes superior.\n          É o salto entre um objeto para deitar fora e uma ferramenta feita para durar.",
        ro="Te credem. Aproape toate au motoare cu perii, care se uzează pe la 18 luni.\n          Pe T77 PRO e un brushless fără perii: durata ajunge de 3 ori mai mare.\n          E saltul între un obiect de aruncat și o unealtă făcută să reziste.",
    )),
    ("Ce la farà davvero con rovi e sterpaglia resistente?", D(
        es="¿De verdad podrá con zarzas y maleza dura?",
        hu="Tényleg bírja az indákat és a kemény bozótot?",
        pl="Czy naprawdę da radę z ostami i twardymi zaroślami?",
        pt="Dá mesmo conta de silvas e mato resistente?",
        ro="Chiar face față mărăcinilor și vegetației dure?",
    )),
    ("La lama d'acciaio a 3 denti nasce proprio per gli interventi gravosi: ceppi, radici e vegetazione coriacea.\n          Con i suoi 21V e il motore brushless, T77 PRO sviluppa una coppia all'altezza dell'uso domestico più intenso.\n          Di giocattoli qui non ce ne sono.", D(
        es="La cuchilla de acero de 3 dientes nace para los trabajos duros: tocones, raíces y vegetación coriácea.\n          Con 21V y el motor brushless, T77 PRO da un par a la altura del uso doméstico más intenso.\n          Aquí no hay juguetes.",
        hu="A 3 fogas acél penge pont a nehéz munkára való: tuskók, gyökerek, kemény növényzet.\n          21V-tal és brushless motorral a T77 PRO nyomatéka a legkeményebb háztartási használatra is elég.\n          Itt nincsenek játékszerek.",
        pl="Stalowa tarcza 3-zębowa jest właśnie do ciężkiej roboty: pniaki, korzenie, twarda roślinność.\n          Przy 21V i silniku brushless T77 PRO daje moment obrotowy na intensywne użycie domowe.\n          Zabawek tu nie ma.",
        pt="A lâmina de aço de 3 dentes nasce para os trabalhos pesados: cepos, raízes e vegetação dura.\n          Com 21V e o motor brushless, o T77 PRO desenvolve binário à altura do uso doméstico mais intenso.\n          Brinquedos aqui não há.",
        ro="Lama de oțel cu 3 dinți e făcută pentru treburile grele: cioate, rădăcini și vegetație dură.\n          Cu 21V și motorul brushless, T77 PRO dezvoltă un cuplu pe măsura uzului casnic intens.\n          Jucării aici nu sunt.",
    )),
    ("Cosa succede se dopo 2 anni la batteria smette di funzionare?", D(
        es="¿Qué pasa si a los 2 años la batería deja de funcionar?",
        hu="Mi történik, ha 2 év után az akku felmondja a szolgálatot?",
        pl="Co, jeśli po 2 latach bateria przestanie działać?",
        pt="O que acontece se ao fim de 2 anos a bateria deixar de funcionar?",
        ro="Ce se întâmplă dacă după 2 ani bateria nu mai merge?",
    )),
    ("Basta rimpiazzare la sola batteria da 21V, senza riacquistare l'intero kit.\n          Il corpo macchina è costruito per reggere anni: sostituisci soltanto il pezzo necessario, quando serve.", D(
        es="Basta sustituir solo la batería de 21V, sin volver a comprar el kit entero.\n          El cuerpo está hecho para aguantar años: cambias solo la pieza necesaria, cuando hace falta.",
        hu="Elég csak a 21V-os akkut cserélni, az egész készletet nem kell újra megvenni.\n          A gép teste évekig bírja: csak a szükséges alkatrészt cseréled, amikor kell.",
        pl="Wystarczy wymienić samą baterię 21V, bez kupowania całego zestawu.\n          Korpus jest zbudowany na lata: wymieniasz tylko potrzebną część, gdy zajdzie taka potrzeba.",
        pt="Basta substituir só a bateria de 21V, sem voltar a comprar o kit inteiro.\n          O corpo da máquina aguenta anos: substitui só a peça necessária, quando for preciso.",
        ro="Ajunge să înlocuiești doar bateria de 21V, fără să cumperi tot kitul.\n          Corpul e construit să țină ani: schimbi doar piesa necesară, când trebuie.",
    )),
    ("Pagare senza aver visto la merce non mi convince.", D(
        es="Pagar sin haber visto el producto no me convence.",
        hu="Nem győz meg, hogy fizetnem kell, mielőtt látnám az árut.",
        pl="Płacenie bez zobaczenia towaru mnie nie przekonuje.",
        pt="Pagar sem ter visto a mercadoria não me convence.",
        ro="Să plătesc fără să fi văzut marfa nu mă convinge.",
    )),
    ("Tranquillo: tiri fuori i soldi soltanto quando il pacco arriva davanti alla tua porta.\n          Il corriere te lo consegna e tu saldi in quel momento. Nessuna carta. Nessun acconto.", D(
        es="Tranquilo: sacas el dinero solo cuando el paquete llega a tu puerta.\n          El repartidor te lo entrega y pagas en ese momento. Sin tarjeta. Sin adelanto.",
        hu="Nyugi: csak akkor fizetsz, amikor a csomag az ajtód előtt van.\n          A futár átadja, te akkor fizetsz. Nincs kártya. Nincs előleg.",
        pl="Spokojnie: wyjmujesz pieniądze dopiero, gdy paczka stanie pod drzwiami.\n          Kurier Ci ją oddaje i wtedy płacisz. Bez karty. Bez zaliczki.",
        pt="Tranquilo: só tiras o dinheiro quando a encomenda chega à tua porta.\n          O estafeta entrega e pagas nesse momento. Sem cartão. Sem adiantamento.",
        ro="Stai liniștit: scoți banii doar când coletul ajunge la ușa ta.\n          Curierul ți-l dă și atunci plătești. Fără card. Fără avans.",
    )),
    ("E se poi non mi trovo bene?", D(
        es="¿Y si luego no me convence?",
        hu="És ha mégsem jön be?",
        pl="A jeśli mi nie podejdzie?",
        pt="E se depois não me der jeito?",
        ro="Și dacă nu mă mulțumește?",
    )),
    ("Puoi metterlo alla prova per 30 giorni. Se per un motivo qualsiasi non ti convince,\n          chiedi il rimborso seguendo le condizioni di reso. Tu non rischi nulla.", D(
        es="Puedes probarlo 30 días. Si por cualquier motivo no te convence,\n          pide el reembolso según las condiciones de devolución. No arriesgas nada.",
        hu="30 napig kipróbálhatod. Ha bármilyen okból nem győz meg,\n          a visszaküldési feltételek szerint kérheted a visszatérítést. Semmit nem kockáztatsz.",
        pl="Możesz go wypróbować przez 30 dni. Jeśli z dowolnego powodu Cię nie przekona,\n          poproś o zwrot według warunków reklamacji. Niczego nie ryzykujesz.",
        pt="Podes experimentá-lo durante 30 dias. Se por qualquer motivo não te convencer,\n          pede o reembolso segundo as condições de devolução. Não arriscas nada.",
        ro="Îl poți proba 30 de zile. Dacă din orice motiv nu te convinge,\n          ceri rambursarea după condițiile de retur. Nu riști nimic.",
    )),
    ("INSERISCI I DATI DI CONSEGNA", D(
        es="INTRODUCE LOS DATOS DE ENTREGA",
        hu="ADD MEG A SZÁLLÍTÁSI ADATOKAT",
        pl="WPISZ DANE DOSTAWY",
        pt="INTRODUZ OS DADOS DE ENTREGA",
        ro="INTRODU DATELE DE LIVRARE",
    )),
    ("L'ordine parte subito. Paghi solo alla consegna, direttamente al corriere.", D(
        es="El pedido sale de inmediato. Pagas solo al recibirlo, directamente al repartidor.",
        hu="A rendelés azonnal elindul. Csak átvételkor fizetsz, közvetlenül a futárnak.",
        pl="Zamówienie wychodzi od razu. Płacisz dopiero przy odbiorze, bezpośrednio kurierowi.",
        pt="A encomenda parte já. Pagas só na entrega, diretamente ao estafeta.",
        ro="Comanda pleacă imediat. Plătești doar la livrare, direct curierului.",
    )),
    ("Nome e Cognome*", D(
        es="Nombre y apellidos*",
        hu="Teljes név*",
        pl="Imię i nazwisko*",
        pt="Nome e apelido*",
        ro="Nume și prenume*",
    )),
    ("Indirizzo di consegna*", D(
        es="Dirección de entrega*",
        hu="Szállítási cím*",
        pl="Adres dostawy*",
        pt="Morada de entrega*",
        ro="Adresa de livrare*",
    )),
    ("Telefono*", D(
        es="Teléfono*",
        hu="Telefon*",
        pl="Numer telefonu*",
        pt="Telefone*",
        ro="Telefon*",
    )),
    ("CONFERMA ORDINE", D(
        es="CONFIRMAR PEDIDO",
        hu="RENDELÉS MEGERŐSÍTÉSE",
        pl="POTWIERDŹ ZAMÓWIENIE",
        pt="CONFIRMAR ENCOMENDA",
        ro="CONFIRMĂ COMANDA",
    )),
    ("Prodotti utili per la vita quotidiana, consegna in 24–48 ore con pagamento alla consegna.", D(
        es="Productos útiles para el día a día, entrega en 24–48 horas con pago contra reembolso.",
        hu="Hasznos termékek a mindennapokra, 24–48 órás szállítás utánvéttel.",
        pl="Przydatne produkty na co dzień, dostawa w 24–48 godzin z płatnością przy odbiorze.",
        pt="Produtos úteis para o dia a dia, entrega em 24–48 horas com pagamento à cobrança.",
        ro="Produse utile pentru fiecare zi, livrare în 24–48 de ore cu plata ramburs.",
    )),
    ("Informazioni", D(es="Información", hu="Információ", pl="Informacje", pt="Informação", ro="Informaţii")),
    ("Chi siamo", D(es="Sobre nosotros", hu="Rólunk", pl="O nas", pt="Sobre nós", ro="Despre noi")),
    ("Contattaci", D(es="Contáctanos", hu="Kapcsolat", pl="Kontakt", pt="Contacte-nos", ro="Contactaţi-ne")),
    ("Termini e Condizioni", D(
        es="Términos y condiciones",
        hu="Általános szerződési feltételek",
        pl="Regulamin",
        pt="Termos e Condições",
        ro="Termeni și condiții",
    )),
    ("Politica di spedizione", D(
        es="Política de envío",
        hu="Szállítási szabályzat",
        pl="Polityka wysyłki",
        pt="Política de envio",
        ro="Politica de livrare",
    )),
    ("Politica di reso", D(
        es="Política de reembolso",
        hu="Visszatérítési szabályzat",
        pl="Polityka zwrotów",
        pt="Política de reembolso",
        ro="Politica de rambursare",
    )),
    ("Politica di Spedizione", D(
        es="Política de envío",
        hu="Szállítási szabályzat",
        pl="Polityka wysyłki",
        pt="Política de Envio",
        ro="Politica de livrare",
    )),
    ("Politica di Rimborso", D(
        es="Política de reembolso",
        hu="Visszatérítési szabályzat",
        pl="Polityka zwrotów",
        pt="Política de reembolso",
        ro="Politica de rambursare",
    )),
    ("Contatti", D(es="Contacto", hu="Kapcsolat", pl="Kontakt", pt="Contacto", ro="Contact")),
    ("Tutti i diritti riservati.", D(
        es="Todos los derechos reservados.",
        hu="Minden jog fenntartva.",
        pl="Wszelkie prawa zastrzeżone.",
        pt="Todos os direitos reservados.",
        ro="Toate drepturile rezervate.",
    )),
    ("Tutti i diritti riservati", D(
        es="Todos los derechos reservados",
        hu="Minden jog fenntartva",
        pl="Wszelkie prawa zastrzeżone",
        pt="Todos os direitos reservados",
        ro="Toate drepturile rezervate",
    )),
    ("Usiamo cookie tecnici e di terze parti per migliorare la tua esperienza e per analisi.", D(
        es="Usamos cookies técnicas y de terceros para mejorar tu experiencia y para análisis.",
        hu="Technikai és harmadik féltől származó cookie-kat használunk a élmény javítására és elemzésre.",
        pl="Używamy plików cookie technicznych i stron trzecich, aby poprawić Twoje doświadczenie i do analityki.",
        pt="Usamos cookies técnicos e de terceiros para melhorar a tua experiência e para análises.",
        ro="Folosim cookie-uri tehnice și de terți pentru a îmbunătăți experiența ta și pentru analiză.",
    )),
    ("Scopri di più", D(es="Más información", hu="Tudjon meg többet", pl="Dowiedz się więcej", pt="Saber mais", ro="Află mai multe")),
    ("Accetta", D(es="Aceptar", hu="Elfogadom", pl="Akceptuję", pt="Aceitar", ro="Acceptă")),
    ("Invio...", D(es="Enviando...", hu="Küldés...", pl="Wysyłanie...", pt="A enviar...", ro="Se trimite...")),
    ("T77 PRO Kit Completo", D(
        es="T77 PRO Kit completo",
        hu="T77 PRO teljes készlet",
        pl="T77 PRO zestaw kompletny",
        pt="T77 PRO Kit completo",
        ro="T77 PRO Kit complet",
    )),
    ("✅ Paghi quando arriva", D(
        es="✅ Pagas cuando llega",
        hu="✅ Fizetsz, amikor megérkezik",
        pl="✅ Płacisz, gdy dotrze",
        pt="✅ Pagas quando chega",
        ro="✅ Plătești când ajunge",
    )),
]

TY_PACK: list[tuple[str, dict[str, str]]] = [
    ("Ordine ricevuto — Attendi la chiamata di conferma | T77 PRO™", D(
        es="Pedido recibido — Espera la llamada de confirmación | T77 PRO™",
        hu="Rendelés rögzítve — Várja a visszaigazoló hívást | T77 PRO™",
        pl="Zamówienie przyjęte — Poczekaj na telefon potwierdzający | T77 PRO™",
        pt="Encomenda recebida — Aguarde a chamada de confirmação | T77 PRO™",
        ro="Comanda a fost primită — Așteptați apelul de confirmare | T77 PRO™",
    )),
    ("Il tuo ordine T77 PRO™ è stato registrato. Manca solo un ultimo passaggio: rispondi alla chiamata di conferma del nostro operatore.", D(
        es="Tu pedido T77 PRO™ ha sido registrado. Solo falta un último paso: responde a la llamada de confirmación de nuestro operador.",
        hu="T77 PRO™ rendelése rögzítve. Már csak egy lépés van hátra: vegye fel a visszaigazoló hívást.",
        pl="Twoje zamówienie T77 PRO™ zostało zapisane. Został ostatni krok: odbierz telefon potwierdzający od naszego operatora.",
        pt="A tua encomenda T77 PRO™ foi registada. Falta só um último passo: atende a chamada de confirmação do nosso operador.",
        ro="Comanda T77 PRO™ a fost înregistrată. Mai rămâne un ultim pas: răspunde la apelul de confirmare al operatorului nostru.",
    )),
    ("Il tuo ordine T77 PRO™ è stato registrato!", D(
        es="¡Tu pedido T77 PRO™ se ha registrado!",
        hu="T77 PRO™ rendelését rögzítettük!",
        pl="Twoje zamówienie T77 PRO™ zostało zapisane!",
        pt="A tua encomenda T77 PRO™ foi registada!",
        ro="Comanda T77 PRO™ a fost înregistrată!",
    )),
    ("Perfetto — il tuo ordine è in elaborazione. Manca solo <strong>un ultimo passaggio</strong> per completarlo e far partire la spedizione.", D(
        es="Perfecto — tu pedido está en proceso. Solo falta <strong>un último paso</strong> para completarlo y enviar.",
        hu="Tökéletes — a rendelés feldolgozás alatt. Már csak <strong>egy utolsó lépés</strong> kell a teljesítéshez és a feladáshoz.",
        pl="Świetnie — zamówienie jest przetwarzane. Został tylko <strong>ostatni krok</strong>, żeby je dokończyć i nadać przesyłkę.",
        pt="Perfeito — a encomenda está a ser processada. Falta só <strong>um último passo</strong> para a concluir e enviar.",
        ro="Perfect — comanda este în procesare. Mai lipsește doar <strong>un ultim pas</strong> ca să o finalizăm și să o expediem.",
    )),
    ("T77 PRO™ — decespugliatore a batteria", D(
        es="T77 PRO™ — desbrozadora a batería",
        hu="T77 PRO™ — akkumulátoros fűkasza",
        pl="T77 PRO™ — podkaszarka akumulatorowa",
        pt="T77 PRO™ — roçadora a bateria",
        ro="T77 PRO™ — motocoasă cu baterie",
    )),
    ("Kit completo · Pagamento alla consegna", D(
        es="Kit completo · Pago contra reembolso",
        hu="Teljes készlet · Utánvét",
        pl="Zestaw kompletny · Płatność przy odbiorze",
        pt="Kit completo · Pagamento à cobrança",
        ro="Kit complet · Plata ramburs",
    )),
    ("👇 Cosa devi fare adesso", D(
        es="👇 Qué debes hacer ahora",
        hu="👇 Mit kell tennie most",
        pl="👇 Co musisz zrobić teraz",
        pt="👇 O que deves fazer agora",
        ro="👇 Ce trebuie să faci acum",
    )),
    ("📞 Rispondi alla chiamata di conferma", D(
        es="📞 Responde a la llamada de confirmación",
        hu="📞 Vegye fel a visszaigazoló hívást",
        pl="📞 Odbierz telefon potwierdzający",
        pt="📞 Atende a chamada de confirmação",
        ro="📞 Răspunde la apelul de confirmare",
    )),
    ("Un nostro operatore ti contatterà <strong>nelle prossime ore</strong> per confermare il tuo ordine T77 PRO™.", D(
        es="Un operador te contactará <strong>en las próximas horas</strong> para confirmar tu pedido T77 PRO™.",
        hu="Operátorunk <strong>a következő órákban</strong> felhívja, hogy megerősítse a T77 PRO™ rendelést.",
        pl="Nasz operator skontaktuje się <strong>w ciągu najbliższych godzin</strong>, aby potwierdzić zamówienie T77 PRO™.",
        pt="Um operador vai contactar-te <strong>nas próximas horas</strong> para confirmar a encomenda T77 PRO™.",
        ro="Un operator te va contacta <strong>în următoarele ore</strong> pentru a confirma comanda T77 PRO™.",
    )),
    ("Se non rispondi alla chiamata, l'ordine verrà automaticamente annullato.", D(
        es="Si no respondes a la llamada, el pedido se cancelará automáticamente.",
        hu="Ha nem veszi fel a hívást, a rendelés automatikusan törlődik.",
        pl="Jeśli nie odbierzesz telefonu, zamówienie zostanie automatycznie anulowane.",
        pt="Se não atenderes a chamada, a encomenda será cancelada automaticamente.",
        ro="Dacă nu răspunzi la apel, comanda va fi anulată automat.",
    )),
    ("🕒 Orari di contatto", D(
        es="🕒 Horario de contacto",
        hu="🕒 Elérhetőség",
        pl="🕒 Godziny kontaktu",
        pt="🕒 Horário de contacto",
        ro="🕒 Program de contact",
    )),
    ("Lunedì – Sabato · 9:00 – 18:00", D(
        es="Lunes – Sábado · 9:00 – 18:00",
        hu="Hétfő – Szombat · 9:00 – 18:00",
        pl="Poniedziałek – Sobota · 9:00 – 18:00",
        pt="Segunda – Sábado · 9:00 – 18:00",
        ro="Luni – Sâmbătă · 9:00 – 18:00",
    )),
    ("📋 Cosa succede dopo", D(
        es="📋 Qué ocurre después",
        hu="📋 Mi történik ezután",
        pl="📋 Co dalej",
        pt="📋 O que acontece a seguir",
        ro="📋 Ce urmează",
    )),
    ("Rispondi alla chiamata e <strong>conferma i tuoi dati</strong>", D(
        es="Responde a la llamada y <strong>confirma tus datos</strong>",
        hu="Vegye fel a hívást és <strong>erősítse meg az adatait</strong>",
        pl="Odbierz telefon i <strong>potwierdź swoje dane</strong>",
        pt="Atende a chamada e <strong>confirma os teus dados</strong>",
        ro="Răspunde la apel și <strong>confirmă datele</strong>",
    )),
    ("Il tuo T77 PRO™ verrà spedito entro <strong>24–48 ore</strong>", D(
        es="Tu T77 PRO™ se enviará en <strong>24–48 horas</strong>",
        hu="T77 PRO™ készülékét <strong>24–48 órán belül</strong> feladjuk",
        pl="Twój T77 PRO™ zostanie wysłany w ciągu <strong>24–48 godzin</strong>",
        pt="O teu T77 PRO™ será enviado em <strong>24–48 horas</strong>",
        ro="T77 PRO™ va fi expediat în <strong>24–48 de ore</strong>",
    )),
    ("Consegna a domicilio e <strong>pagamento alla consegna</strong>", D(
        es="Entrega a domicilio y <strong>pago contra reembolso</strong>",
        hu="Házhozszállítás és <strong>utánvét</strong>",
        pl="Dostawa do domu i <strong>płatność przy odbiorze</strong>",
        pt="Entrega ao domicílio e <strong>pagamento à cobrança</strong>",
        ro="Livrare la domiciliu și <strong>plata ramburs</strong>",
    )),
    ("🔒 Pagamento alla consegna", D(
        es="🔒 Pago contra reembolso",
        hu="🔒 Utánvét",
        pl="🔒 Płatność przy odbiorze",
        pt="🔒 Pagamento à cobrança",
        ro="🔒 Plata ramburs",
    )),
    ("🛡️ Garanzia 2 anni", D(
        es="🛡️ Garantía 2 años",
        hu="🛡️ 2 év garancia",
        pl="🛡️ Gwarancja 2 lata",
        pt="🛡️ Garantia 2 anos",
        ro="🛡️ Garanție 2 ani",
    )),
    ("↩️ 30 giorni di prova", D(
        es="↩️ 30 días de prueba",
        hu="↩️ 30 napos próba",
        pl="↩️ 30 dni na wypróbowanie",
        pt="↩️ 30 dias de teste",
        ro="↩️ 30 de zile de probă",
    )),
]


def apply_pack(html: str, geo: str, pack: list[tuple[str, dict[str, str]]]) -> str:
    items = sorted(pack, key=lambda x: len(x[0]), reverse=True)
    for src, langs in items:
        if geo not in langs:
            raise KeyError(f"missing {geo} for: {src[:60]}")
        if src not in html:
            # curly vs straight apostrophe
            alt = src.replace("'", "’").replace("’", "'")
            if alt in html:
                html = html.replace(alt, langs[geo])
                continue
            print(f"WARN missing string ({geo}): {src[:80]!r}")
            continue
        html = html.replace(src, langs[geo])
    return html


def slug(geo: str) -> str:
    return f"grass-trimmer-t77-pro-{geo}"


def patch_form(html: str, g: dict, geo: str) -> str:
    html = html.replace("018e3961-c73a-7965-8fc1-b1d91c869a42", g["uid"])
    html = html.replace('value="1274"', f'value="{g["offer"]}"')
    html = html.replace('value="1293"', f'value="{g["lp"]}"')
    html = html.replace(
        "https://gadgetspothub.com/grass-trimmer-t77-pro/thank-you.html",
        f"https://gadgetspothub.com/{slug(geo)}/thank-you.html",
    )
    html = html.replace(
        "https://hook.eu2.make.com/i7pmea9fmpnepx94e5z6dxfwvl1bnnlh",
        g["webhook"],
    )
    html = html.replace(
        "bb9bb46add2c9a64d7a6da26437ad8640be0540b",
        g["key"],
    )
    html = html.replace("Mario Rossi", g["ph_name"])
    html = html.replace("+39 392 0745623", g["ph_tel"])
    html = html.replace("Via Torino 1, 12345 Roma Italia", g["ph_addr"])
    return html


def generate_lp(geo: str, g: dict) -> str:
    html = IT_LP.read_text(encoding="utf-8")
    html = apply_pack(html, geo, PACK + PACK2)
    html = html.replace('lang="it"', f'lang="{g["lang"]}"')
    html = html.replace(
        "https://gadgetspothub.com/grass-trimmer-t77-pro/",
        f"https://gadgetspothub.com/{slug(geo)}/",
    )
    html = html.replace("GEO: 'it'", f"GEO: '{geo}'")
    html = html.replace("PRICE: 99", f"PRICE: {g['price']}")
    html = html.replace("CURRENCY: 'EUR'", f"CURRENCY: '{g['currency']}'")
    html = html.replace("OFFER_NAME: 'T77 PRO 1274'", f"OFFER_NAME: 'T77 PRO {g['offer']}'")
    html = html.replace("LP_ID: 'it-1274'", f"LP_ID: '{geo}-{g['lp']}'")
    html = html.replace("€99", g["now"])
    html = html.replace("€200", g["was"])
    html = html.replace('href="/it/', f'href="/{geo}/')
    html = patch_form(html, g, geo)
    return html


def generate_ty(geo: str, g: dict) -> str:
    html = IT_TY.read_text(encoding="utf-8")
    html = apply_pack(html, geo, PACK + PACK2 + TY_PACK)
    html = html.replace('lang="it"', f'lang="{g["lang"]}"')
    html = html.replace("GEO: 'it'", f"GEO: '{geo}'")
    html = html.replace("PRICE: 99", f"PRICE: {g['price']}")
    html = html.replace("CURRENCY: 'EUR'", f"CURRENCY: '{g['currency']}'")
    html = html.replace("99 €", g["now_ty"])
    html = html.replace('href="/it/', f'href="/{geo}/')
    return html


def update_sitemap() -> None:
    text = SITEMAP.read_text(encoding="utf-8")
    marker = "  <url><loc>https://gadgetspothub.com/grass-trimmer-t77-pro/</loc><lastmod>2026-08-29</lastmod><changefreq>weekly</changefreq><priority>0.95</priority></url>\n"
    extras = marker
    for geo in GEOS:
        loc = f"https://gadgetspothub.com/{slug(geo)}/"
        line = f'  <url><loc>{loc}</loc><lastmod>2026-08-29</lastmod><changefreq>weekly</changefreq><priority>0.95</priority></url>\n'
        if loc not in text:
            extras += line
    if extras != marker:
        text = text.replace(marker, extras)
        SITEMAP.write_text(text, encoding="utf-8")
        print("sitemap updated")
    else:
        print("sitemap already had geos")


def main() -> None:
    for geo, g in GEOS.items():
        dest = ROOT / slug(geo)
        dest.mkdir(parents=True, exist_ok=True)
        lp = generate_lp(geo, g)
        ty = generate_ty(geo, g)
        (dest / "index.html").write_text(lp, encoding="utf-8")
        (dest / "thank-you.html").write_text(ty, encoding="utf-8")
        italianish = ("Pagamento alla", "Spedizione", "decespugliatore", "Ordina Ora", "pezzi rimasti", "Compila il")
        leftovers = [w for w in italianish if w in lp]
        print(f"{geo}: lp={len(lp)} ty={len(ty)} leftovers={leftovers}")
    update_sitemap()


if __name__ == "__main__":
    main()
