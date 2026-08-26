#!/usr/bin/env python3
"""Clone clima-pro-it HTML and translate it for CZ ES PT SK HU LV."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

UID = "0198c21c-8430-751a-a450-d7f01a76c3ee"
WEBHOOK = "https://hook.eu2.make.com/7nudarijfrsvnhnwfnpqfh2t8vqt109i"
IT_UID = "018e3961-c73a-7965-8fc1-b1d91c869a42"
IT_WEBHOOK = "https://hook.eu2.make.com/i7pmea9fmpnepx94e5z6dxfwvl1bnnlh"
IT_KEY = "bb9bb46add2c9a64d7a6da26437ad8640be0540b"

GEOS = {
    "cz": dict(lang="cs", price_num=1799, currency="CZK", now="1 799 Kč", was="3 598 Kč", offer="3590", lp="3627", key="e5d307d9de4b10efb23d853246a0677d6b8c6f80"),
    "es": dict(lang="es", price_num=79, currency="EUR", now="79,00€", was="158,00€", offer="3587", lp="3624", key="2af2c1ec0bbe33b257d37839f043b8beba23a806"),
    "pt": dict(lang="pt", price_num=89, currency="EUR", now="89,00€", was="178,00€", offer="3588", lp="3625", key="0f4b28c87f1287b7753a5379eabeb8581b83bb40"),
    "sk": dict(lang="sk", price_num=69, currency="EUR", now="69,00€", was="138,00€", offer="3589", lp="3626", key="5ac3efddc05cb9c3f1be79aa221072f4def341f7"),
    "hu": dict(lang="hu", price_num=39900, currency="HUF", now="39 900 Ft", was="79 800 Ft", offer="3431", lp="3467", key="2a933fff3f54a5436980d423bd4fe776adb2d052"),
    "lv": dict(lang="lv", price_num=89, currency="EUR", now="89,00€", was="178,00€", offer="4241", lp="4281", key="cbfe35078931603dbf1d617f67c379ac0d9c3ab7"),
}

# it -> {geo: translation}. Longer strings are applied first.
PACK = [
    # --- meta ---
    ("Clima PRO — Climatizzatore a colonna 4 in 1 senza installazione | -50%", dict(
        cz="Clima PRO — Sloupová klimatizace 4 v 1 bez instalace | -50%",
        es="Clima PRO — Aire acondicionado de columna 4 en 1 sin instalación | -50%",
        pt="Clima PRO — Ar condicionado de coluna 4 em 1 sem instalação | -50%",
        sk="Clima PRO — Stĺpová klimatizácia 4 v 1 bez inštalácie | -50%",
        hu="Clima PRO — Oszlopklíma 4 az 1-ben telepítés nélkül | -50%",
        lv="Clima PRO — Kolonnas kondicionieris 4 vienā bez uzstādīšanas | -50%",
    )),
    ("Clima PRO: climatizzatore a colonna 4 in 1 senza installazione e senza unità esterna. Raffredda, riscalda, deumidifica e purifica fino a 120 m². Pagamento alla consegna.", dict(
        cz="Clima PRO: sloupová klimatizace 4 v 1 bez instalace a bez venkovní jednotky. Chladí, topí, odvlhčuje a čistí až 120 m². Platba na dobírku.",
        es="Clima PRO: aire acondicionado de columna 4 en 1 sin instalación y sin unidad exterior. Enfría, calienta, deshumidifica y purifica hasta 120 m². Pago contra reembolso.",
        pt="Clima PRO: ar condicionado de coluna 4 em 1 sem instalação e sem unidade exterior. Arrefece, aquece, desumidifica e purifica até 120 m². Pagamento à cobrança.",
        sk="Clima PRO: stĺpová klimatizácia 4 v 1 bez inštalácie a bez vonkajšej jednotky. Chladí, kúri, odvlhčuje a čistí až 120 m². Platba na dobierku.",
        hu="Clima PRO: oszlopklíma 4 az 1-ben telepítés és külső egység nélkül. Hűt, fűt, párátlanít és tisztít akár 120 m²-en. Utánvét.",
        lv="Clima PRO: kolonnas gaisa kondicionieris 4 vienā bez uzstādīšanas un bez āra bloka. Dzesē, silda, sausina un attīra līdz 120 m². Maksa pēc saņemšanas.",
    )),
    ("Invio in corso...", dict(cz="Odesílání...", es="Enviando...", pt="A enviar...", sk="Odosielanie...", hu="Küldés...", lv="Nosūta...")),
    ("Usiamo cookie tecnici e di terze parti per migliorare la tua esperienza e per analisi.", dict(
        cz="Používáme technické a cookies třetích stran ke zlepšení vašeho zážitku a pro analytiku.",
        es="Usamos cookies técnicas y de terceros para mejorar tu experiencia y para análisis.",
        pt="Usamos cookies técnicos e de terceiros para melhorar a sua experiência e para análises.",
        sk="Používame technické a cookies tretích strán na zlepšenie vášho zážitku a na analytiku.",
        hu="Technikai és harmadik féltől származó cookie-kat használunk a élmény javítására és elemzésre.",
        lv="Mēs izmantojam tehniskās un trešo pušu sīkdatnes, lai uzlabotu jūsu pieredzi un analītikai.",
    )),
    ("Scopri di più", dict(cz="Zjistit více", es="Más información", pt="Saber mais", sk="Zistiť viac", hu="Tudjon meg többet", lv="Uzzināt vairāk")),
    ("Accetta", dict(cz="Přijmout", es="Aceptar", pt="Aceitar", sk="Prijať", hu="Elfogadom", lv="Piekrist")),
    # --- hero ---
    ("OGGI IN SCONTO AL 50% · ❄️ Pagamento alla consegna · Spedizione 24/48 h", dict(
        cz="DNES SLEVA 50 % · ❄️ Platba na dobírku · Doručení 24/48 h",
        es="HOY 50% DE DESCUENTO · ❄️ Pago contra reembolso · Envío 24/48 h",
        pt="HOJE COM 50% DE DESCONTO · ❄️ Pagamento à cobrança · Envio 24/48 h",
        sk="DNES ZĽAVA 50 % · ❄️ Platba na dobierku · Doručenie 24/48 h",
        hu="MA 50% KEDVEZMÉNY · ❄️ Utánvét · Szállítás 24/48 óra",
        lv="ŠODIEN 50% ATLAIDE · ❄️ Maksa pēc saņemšanas · Piegāde 24/48 h",
    )),
    ("❄️ Pagamento alla consegna · Spedizione 24/48 h", dict(
        cz="❄️ Platba na dobírku · Doručení 24/48 h",
        es="❄️ Pago contra reembolso · Envío 24/48 h",
        pt="❄️ Pagamento à cobrança · Envio 24/48 h",
        sk="❄️ Platba na dobierku · Doručenie 24/48 h",
        hu="❄️ Utánvét · Szállítás 24/48 óra",
        lv="❄️ Maksa pēc saņemšanas · Piegāde 24/48 h",
    )),
    ("Climatizzatore a colonna 4 in 1 senza installazione e senza unità esterna", dict(
        cz="Sloupová klimatizace 4 v 1 bez instalace a bez venkovní jednotky",
        es="Aire acondicionado de columna 4 en 1 sin instalación y sin unidad exterior",
        pt="Ar condicionado de coluna 4 em 1 sem instalação e sem unidade exterior",
        sk="Stĺpová klimatizácia 4 v 1 bez inštalácie a bez vonkajšej jednotky",
        hu="Oszlopklíma 4 az 1-ben telepítés és külső egység nélkül",
        lv="Kolonnas gaisa kondicionieris 4 vienā bez uzstādīšanas un bez āra bloka",
    )),
    ("Raffredda, riscalda, deumidifica e purifica l'aria in ambienti fino a <strong>120 m²</strong>, garantendo comfort in pochi minuti. Riduci i consumi e dimentica le bollette alte! Grazie alla tecnologia a basso consumo e alla <strong>classe energetica A+++</strong>, consuma solo <strong>€0,18 al giorno</strong>.", dict(
        cz="Chladí, topí, odvlhčuje a čistí vzduch v místnostech až do <strong>120 m²</strong> a přinese komfort během několika minut. Snižte spotřebu a zapomeňte na vysoké účty! Díky úsporné technologii a <strong>energetické třídě A+++</strong> spotřebuje jen <strong>4,50 Kč denně</strong>.",
        es="Enfría, calienta, deshumidifica y purifica el aire en espacios de hasta <strong>120 m²</strong>, con confort en pocos minutos. Reduce el consumo y olvídate de las facturas altas. Gracias a la tecnología de bajo consumo y a la <strong>clase energética A+++</strong>, consume solo <strong>0,18€ al día</strong>.",
        pt="Arrefece, aquece, desumidifica e purifica o ar em espaços até <strong>120 m²</strong>, com conforto em poucos minutos. Reduza o consumo e esqueça as faturas altas. Graças à tecnologia de baixo consumo e à <strong>classe energética A+++</strong>, consome apenas <strong>0,18€ por dia</strong>.",
        sk="Chladí, kúri, odvlhčuje a čistí vzduch v miestnostiach až do <strong>120 m²</strong> a prinesie komfort v priebehu niekoľkých minút. Znížte spotrebu a zabudnite na vysoké účty. Vďaka úspornej technológii a <strong>energetickej triede A+++</strong> spotrebuje len <strong>0,18€ denne</strong>.",
        hu="Hűt, fűt, párátlanít és tisztítja a levegőt akár <strong>120 m²</strong>-es terekben, perceken belül kényelmet adva. Csökkentse a fogyasztást, és felejtse el a magas számlákat. Az energiatakarékos technológiának és az <strong>A+++ energiaosztálynak</strong> köszönhetően napi fogyasztása csak <strong>70 Ft</strong>.",
        lv="Dzesē, silda, sausina un attīra gaisu telpās līdz <strong>120 m²</strong>, sniedzot komfortu dažu minūšu laikā. Samaziniet patēriņu un aizmirstiet par augstiem rēķiniem. Pateicoties energoefektīvai tehnoloģijai un <strong>enerģijas klasei A+++</strong>, patērē tikai <strong>0,18€ dienā</strong>.",
    )),
    ("Clima PRO climatizzatore a colonna portatile 4 in 1", dict(
        cz="Clima PRO přenosná sloupová klimatizace 4 v 1",
        es="Clima PRO climatizador de columna portátil 4 en 1",
        pt="Clima PRO climatizador de coluna portátil 4 em 1",
        sk="Clima PRO prenosná stĺpová klimatizácia 4 v 1",
        hu="Clima PRO hordozható oszlopklíma 4 az 1-ben",
        lv="Clima PRO pārnēsājams kolonnas klimatizators 4 vienā",
    )),
    ("Solo <strong>7 pezzi</strong> rimasti a questo prezzo", dict(
        cz="Za tuto cenu zbývá jen <strong>7 kusů</strong>",
        es="Solo quedan <strong>7 unidades</strong> a este precio",
        pt="Restam apenas <strong>7 unidades</strong> a este preço",
        sk="Za túto cenu ostáva len <strong>7 kusov</strong>",
        hu="Ezen az áron már csak <strong>7 darab</strong> van",
        lv="Šajā cenā palikušas tikai <strong>7 vienības</strong>",
    )),
    ("120 m² rinfrescati in 5 minuti.", dict(
        cz="120 m² vychlazeno za 5 minut.",
        es="120 m² refrigerados en 5 minutos.",
        pt="120 m² arrefecidos em 5 minutos.",
        sk="120 m² schladených za 5 minút.",
        hu="120 m² lehűtve 5 perc alatt.",
        lv="120 m² atdzesēti 5 minūtēs.",
    )),
    ("Dalla camera al soggiorno: lo sposti sulle ruote e la stanza cambia temperatura prima ancora che tu finisca di prepararti per la notte.", dict(
        cz="Z ložnice do obýváku: přesunete ho na kolečkách a místnost změní teplotu dřív, než se stihnete připravit na noc.",
        es="Del dormitorio al salón: lo mueves sobre ruedas y la habitación cambia de temperatura antes de que termines de prepararte para la noche.",
        pt="Do quarto à sala: move-o sobre rodas e a divisão muda de temperatura antes de acabares de te preparares para a noite.",
        sk="Zo spálne do obývačky: presuniete ho na kolieskach a miestnosť zmení teplotu skôr, než sa stihnete pripraviť na noc.",
        hu="A hálóból a nappaliba: kerekeken tolja, és a szoba hamarabb vált hőmérsékletet, mint ahogy éjszakára készülne.",
        lv="No guļamistabas uz dzīvojamo: pārvietojat uz riteņiem, un telpa maina temperatūru, pirms pagūstat sagatavoties naktij.",
    )),
    ("Silenzio da 18 dB — meno di un sussurro.", dict(
        cz="Ticho 18 dB — tišší než šepot.",
        es="Silencio de 18 dB — menos que un susurro.",
        pt="Silêncio de 18 dB — menos que um sussurro.",
        sk="Ticho 18 dB — tichšie ako šepot.",
        hu="18 dB csend — halkabb egy suttogásnál.",
        lv="18 dB klusums — klusāks par čukstu.",
    )),
    ("Ti addormenti e non ti accorgi nemmeno che è acceso: pensato apposta per la camera da letto.", dict(
        cz="Usnete a ani nevíte, že běží: navrženo speciálně do ložnice.",
        es="Te duermes y ni te das cuenta de que está encendido: pensado para el dormitorio.",
        pt="Adormeces e nem reparas que está ligado: pensado para o quarto.",
        sk="Zaspite a ani neviete, že beží: navrhnuté špeciálne do spálne.",
        hu="Elalszik, és észre sem veszi, hogy be van kapcsolva: hálószobára tervezték.",
        lv="Aizmiegat un pat nepamanāt, ka tas ir ieslēgts: radīts tieši guļamistabai.",
    )),
    ("Zero fori nel muro, zero unità esterna, nessun tecnico richiesto.", dict(
        cz="Žádné díry ve zdi, žádná venkovní jednotka, žádný technik.",
        es="Cero agujeros en la pared, cero unidad exterior, ningún técnico.",
        pt="Zero furos na parede, zero unidade exterior, nenhum técnico.",
        sk="Žiadne diery v stene, žiadna vonkajšia jednotka, žiadny technik.",
        hu="Sem lyuk a falon, sem külső egység, sem szerelő.",
        lv="Nulle caurumu sienā, nulle āra bloka, neviens tehniķis.",
    )),
    ("Lo tiri fuori dalla scatola, lo appoggi a terra, colleghi la spina ed è pronto in 5 minuti.", dict(
        cz="Vytáhnete ho z krabice, postavíte na zem, zapojíte šňůru a za 5 minut je připravený.",
        es="Lo sacas de la caja, lo apoyas en el suelo, enchufas y está listo en 5 minutos.",
        pt="Tiras da caixa, pousas no chão, ligas a ficha e está pronto em 5 minutos.",
        sk="Vytiahnete ho z krabice, postavíte na zem, zapojíte šnúru a za 5 minút je pripravený.",
        hu="Kiveszi a dobozból, a földre állítja, bedugja, és 5 perc múlva kész.",
        lv="Izņemat no kastes, noliekat uz grīdas, iespraužat, un pēc 5 minūtēm tas ir gatavs.",
    )),
    ("Consuma solo €0,18 al giorno.", dict(
        cz="Spotřeba jen 4,50 Kč denně.",
        es="Consume solo 0,18€ al día.",
        pt="Consome apenas 0,18€ por dia.",
        sk="Spotreba len 0,18€ denne.",
        hu="Napi fogyasztása csak 70 Ft.",
        lv="Patērē tikai 0,18€ dienā.",
    )),
    ("Tecnologia intelligente che riduce i consumi al minimo: zero brutte sorprese in bolletta.", dict(
        cz="Inteligentní technologie snižuje spotřebu na minimum: žádná nepříjemná překvapení na účtu.",
        es="Tecnología inteligente que reduce el consumo al mínimo: cero sorpresas en la factura.",
        pt="Tecnologia inteligente que reduz o consumo ao mínimo: zero surpresas na fatura.",
        sk="Inteligentná technológia znižuje spotrebu na minimum: žiadne nepríjemné prekvapenia na účte.",
        hu="Intelligens technológia, amely a fogyasztást a minimumra csökkenti: semmi meglepetés a számlán.",
        lv="Vieda tehnoloģija samazina patēriņu līdz minimumam: nekādu pārsteigumu rēķinā.",
    )),
    ("4 funzioni in 1, controllo da smartphone.", dict(
        cz="4 funkce v 1, ovládání z telefonu.",
        es="4 funciones en 1, control desde el móvil.",
        pt="4 funções em 1, controlo pelo smartphone.",
        sk="4 funkcie v 1, ovládanie z telefónu.",
        hu="4 funkció 1-ben, vezérlés telefonról.",
        lv="4 funkcijas 1, vadība no viedtālruņa.",
    )),
    ("Raffredda, riscalda, deumidifica e purifica: regoli tutto restando sotto le lenzuola.", dict(
        cz="Chladí, topí, odvlhčuje a čistí: vše nastavíte, aniž byste vstali z postele.",
        es="Enfría, calienta, deshumidifica y purifica: lo regulas sin levantarte de la cama.",
        pt="Arrefece, aquece, desumidifica e purifica: regulas tudo sem sair da cama.",
        sk="Chladí, kúri, odvlhčuje a čistí: všetko nastavíte, aniž by ste vstali z postele.",
        hu="Hűt, fűt, párátlanít és tisztít: mindent az ágyból állít.",
        lv="Dzesē, silda, sausina un attīra: visu regulējat, neizkāpjot no gultas.",
    )),
    ("Sì, voglio dormire fresco: ordino ora", dict(
        cz="Ano, chci spát v chládku: objednávám teď",
        es="Sí, quiero dormir fresco: pido ahora",
        pt="Sim, quero dormir fresco: encomendo agora",
        sk="Áno, chcem spať v chládku: objednávam teraz",
        hu="Igen, hűvösen akarok aludni: most rendelem",
        lv="Jā, gribu gulēt vēsumā: pasūtu tagad",
    )),
    ("Acquisto sicuro • Spedizione espressa • Garanzia completa", dict(
        cz="Bezpečný nákup • Expresní doručení • Kompletní záruka",
        es="Compra segura • Envío exprés • Garantía completa",
        pt="Compra segura • Envio expresso • Garantia completa",
        sk="Bezpečný nákup • Expresné doručenie • Kompletná záruka",
        hu="Biztonságos vásárlás • Expressz szállítás • Teljes garancia",
        lv="Drošs pirkums • Ekspress piegāde • Pilna garantija",
    )),
    ("Il pacco arriva direttamente a casa tua in 24–48 ore.", dict(
        cz="Balíček dorazí k vám domů do 24–48 hodin.",
        es="El paquete llega a tu casa en 24–48 horas.",
        pt="A encomenda chega a casa em 24–48 horas.",
        sk="Balík dorazí k vám domov do 24–48 hodín.",
        hu="A csomag 24–48 órán belül megérkezik otthonába.",
        lv="Paciņa nonāk pie jums mājās 24–48 stundu laikā.",
    )),
    ("Nessun addebito anticipato: saldi solo a pacco ricevuto", dict(
        cz="Žádná platba předem: zaplatíte, až balíček obdržíte",
        es="Sin cargo anticipado: pagas solo cuando llega el paquete",
        pt="Sem cobrança antecipada: paga só quando receber o pacote",
        sk="Žiadna platba vopred: zaplatíte, až balík prevezmete",
        hu="Nincs előleg: csak a csomag átvételekor fizet",
        lv="Bez avansa: maksājat tikai, kad saņemat paciņu",
    )),
    ("I tuoi dati personali sono protetti al 100%", dict(
        cz="Vaše osobní údaje jsou 100% chráněny",
        es="Tus datos personales están protegidos al 100%",
        pt="Os seus dados pessoais estão protegidos a 100%",
        sk="Vaše osobné údaje sú 100% chránené",
        hu="Személyes adatai 100%-ban védettek",
        lv="Jūsu personas dati ir 100% aizsargāti",
    )),
    ("Puoi restituirlo senza pensieri entro 60 giorni", dict(
        cz="Můžete ho vrátit bez starostí do 60 dnů",
        es="Puedes devolverlo sin preocupaciones en 60 días",
        pt="Pode devolver sem preocupações em 60 dias",
        sk="Môžete ho vrátiť bez starostí do 60 dní",
        hu="60 napon belül gond nélkül visszaviheti",
        lv="Varat to atdot bez raizēm 60 dienu laikā",
    )),
    ("Spedizione veloce", dict(cz="Rychlé doručení", es="Envío rápido", pt="Envio rápido", sk="Rýchle doručenie", hu="Gyors szállítás", lv="Ātra piegāde")),
    ("Paghi alla consegna", dict(cz="Platíte při převzetí", es="Pagas al recibir", pt="Paga na entrega", sk="Platíte pri prevzatí", hu="Fizetés átvételkor", lv="Maksājat saņemot")),
    ("Acquisto blindato", dict(cz="Nákup pod ochranou", es="Compra protegida", pt="Compra protegida", sk="Nákup pod ochranou", hu="Védett vásárlás", lv="Aizsargāts pirkums")),
    ("Garanzia 2 anni", dict(cz="Záruka 2 roky", es="Garantía 2 años", pt="Garantia 2 anos", sk="Záruka 2 roky", hu="2 év garancia", lv="2 gadu garantija")),
    ("SOLO 7 PEZZI RIMASTI", dict(
        cz="ZBÝVÁ JEN 7 KUSŮ", es="SOLO QUEDAN 7 UNIDADES", pt="RESTAM APENAS 7 UNIDADES",
        sk="OSTÁVA LEN 7 KUSOV", hu="MÁR CSAK 7 DARAB VAN", lv="PALIKUŠAS TIKAI 7 VIENĪBAS",
    )),
    ("Importante! Il magazzino si sta svuotando in fretta!", dict(
        cz="Důležité! Sklad se rychle vyprazdňuje!",
        es="¡Importante! El almacén se está vaciando rápido!",
        pt="Importante! O armazém está a esvaziar-se depressa!",
        sk="Dôležité! Sklad sa rýchlo vyprázdňuje!",
        hu="Fontos! A raktár gyorsan ürül!",
        lv="Svarīgi! Noliktava tukšojas strauji!",
    )),
    ("Proprio adesso tanti altri clienti hanno gli occhi puntati su questo prodotto: ecco perché le unità disponibili calano così in fretta. Acquista subito e mettiti al sicuro uno degli ultimi pezzi rimasti al prezzo scontato di oggi.", dict(
        cz="Právě teď má na tento produkt spousta dalších zákazníků oči. Proto dostupné kusy mizí tak rychle. Objednejte hned a zajistěte si jeden z posledních kusů za dnešní slevovou cenu.",
        es="Ahora mismo muchos otros clientes tienen los ojos puestos en este producto: por eso las unidades disponibles bajan tan rápido. Compra ya y asegúrate una de las últimas unidades al precio de hoy.",
        pt="Neste momento muitos outros clientes estão de olho neste produto: por isso as unidades disponíveis descem tão rápido. Compre já e garanta uma das últimas unidades ao preço de hoje.",
        sk="Práve teraz má na tento produkt veľa ďalších zákazníkov oči. Preto dostupné kusy miznú tak rýchlo. Objednajte hneď a zabezpečte si jeden z posledných kusov za dnešnú zľavovú cenu.",
        hu="Épp most sok másik vásárló figyeli ezt a terméket: ezért fogy ilyen gyorsan. Rendeljen azonnal, és biztosítson be egyet az utolsó darabok közül a mai áron.",
        lv="Tieši tagad daudzi citi klienti raugās uz šo produktu: tāpēc pieejamās vienības izzūd tik ātri. Pasūtiet tūlīt un nodrošiniet vienu no pēdējām vienībām par šodienas cenu.",
    )),
    ("⏰ Offerta -50% attiva solo oggi", dict(
        cz="⏰ Nabídka -50 % platí jen dnes",
        es="⏰ Oferta -50% activa solo hoy",
        pt="⏰ Oferta -50% ativa só hoje",
        sk="⏰ Ponuka -50 % platí len dnes",
        hu="⏰ A -50% ajánlat csak ma él",
        lv="⏰ -50% piedāvājums spēkā tikai šodien",
    )),
    ('<div class="lbl">Ore</div>', dict(
        cz='<div class="lbl">Hod</div>', es='<div class="lbl">Hrs</div>', pt='<div class="lbl">Hrs</div>',
        sk='<div class="lbl">Hod</div>', hu='<div class="lbl">Óra</div>', lv='<div class="lbl">St</div>',
    )),
    ('<div class="lbl">Min</div>', dict(
        cz='<div class="lbl">Min</div>', es='<div class="lbl">Min</div>', pt='<div class="lbl">Min</div>',
        sk='<div class="lbl">Min</div>', hu='<div class="lbl">Perc</div>', lv='<div class="lbl">Min</div>',
    )),
    ('<div class="lbl">Sec</div>', dict(
        cz='<div class="lbl">Sek</div>', es='<div class="lbl">Seg</div>', pt='<div class="lbl">Seg</div>',
        sk='<div class="lbl">Sek</div>', hu='<div class="lbl">Mp</div>', lv='<div class="lbl">Sek</div>',
    )),
    ("Pezzi ancora disponibili", dict(cz="Ještě dostupné kusy", es="Unidades aún disponibles", pt="Unidades ainda disponíveis", sk="Ešte dostupné kusy", hu="Még elérhető darabok", lv="Vēl pieejamas vienības")),
    ("Pochi pezzi rimasti!", dict(cz="Zbývá jen pár kusů!", es="¡Quedan pocas unidades!", pt="Restam poucas unidades!", sk="Ostáva len pár kusov!", hu="Már csak kevés darab!", lv="Palikušas tikai dažas!")),
    ('<strong>{n} persone</strong> stanno guardando Clima PRO ora', dict(
        cz="<strong>{n} lidí</strong> právě sleduje Clima PRO",
        es="<strong>{n} personas</strong> están viendo Clima PRO ahora",
        pt="<strong>{n} pessoas</strong> estão a ver Clima PRO agora",
        sk="<strong>{n} ľudí</strong> práve sleduje Clima PRO",
        hu="<strong>{n} ember</strong> nézi most a Clima PRO-t",
        lv="<strong>{n} cilvēki</strong> tagad skatās Clima PRO",
    )),
    ("<strong>41 persone</strong> stanno guardando Clima PRO ora", dict(
        cz="<strong>41 lidí</strong> právě sleduje Clima PRO",
        es="<strong>41 personas</strong> están viendo Clima PRO ahora",
        pt="<strong>41 pessoas</strong> estão a ver Clima PRO agora",
        sk="<strong>41 ľudí</strong> práve sleduje Clima PRO",
        hu="<strong>41 ember</strong> nézi most a Clima PRO-t",
        lv="<strong>41 cilvēki</strong> tagad skatās Clima PRO",
    )),
    ("Compila il modulo d’ordine", dict(
        cz="Vyplňte objednávkový formulář",
        es="Completa el formulario de pedido",
        pt="Preencha o formulário de encomenda",
        sk="Vyplňte objednávkový formulár",
        hu="Töltse ki a rendelési űrlapot",
        lv="Aizpildiet pasūtījuma veidlapu",
    )),
    ("Ti contatteremo per confermare i dettagli della consegna.", dict(
        cz="Budeme vás kontaktovat kvůli potvrzení detailů doručení.",
        es="Te contactaremos para confirmar los datos de entrega.",
        pt="Vamos contactá-lo para confirmar os dados de entrega.",
        sk="Budeme vás kontaktovať kvôli potvrdeniu detailov doručenia.",
        hu="Felvesszük a kapcsolatot a szállítási adatok megerősítéséhez.",
        lv="Sazināsimies, lai apstiprinātu piegādes datus.",
    )),
    ("Nome e Cognome*", dict(cz="Jméno a příjmení*", es="Nombre y apellidos*", pt="Nome e apelido*", sk="Meno a priezvisko*", hu="Név*", lv="Vārds un uzvārds*")),
    ("Mario Rossi", dict(cz="Jan Novák", es="Juan García", pt="João Silva", sk="Ján Novák", hu="Kovács János", lv="Jānis Bērziņš")),
    ("Telefono*", dict(cz="Telefon*", es="Teléfono*", pt="Telefone*", sk="Telefón*", hu="Telefon*", lv="Tālrunis*")),
    ("+39 392 0745623", dict(cz="+420 601 123 456", es="+34 612 345 678", pt="+351 912 345 678", sk="+421 901 123 456", hu="+36 30 123 4567", lv="+371 21 234 567")),
    ("Indirizzo di consegna*", dict(cz="Doručovací adresa*", es="Dirección de entrega*", pt="Morada de entrega*", sk="Doručovacia adresa*", hu="Szállítási cím*", lv="Piegādes adrese*")),
    ("Via Torino 1, 12345 Roma Italia", dict(
        cz="Ulice 10, 110 00 Praha",
        es="Calle Mayor 10, 28013 Madrid",
        pt="Rua Augusta 10, 1100-053 Lisboa",
        sk="Ulica 10, 811 01 Bratislava",
        hu="Fő utca 10, 1051 Budapest",
        lv="Brīvības iela 10, LV-1010 Rīga",
    )),
    ("ACQUISTA ORA", dict(cz="KOUPIT NYNÍ", es="COMPRAR AHORA", pt="COMPRAR AGORA", sk="KÚPIŤ TERAZ", hu="MEGVESZEM MOST", lv="PIRKT TAGAD")),
    ("🔒 Nessun anticipo · Paghi solo alla consegna · Spedizione 24/48h", dict(
        cz="🔒 Bez zálohy · Platíte až při doručení · Doprava 24/48 h",
        es="🔒 Sin anticipo · Pagas al recibir · Envío 24/48 h",
        pt="🔒 Sem adiantamento · Paga na entrega · Envio 24/48 h",
        sk="🔒 Bez zálohy · Platíte až pri doručení · Doprava 24/48 h",
        hu="🔒 Nincs előleg · Fizetés átvételkor · Szállítás 24/48 óra",
        lv="🔒 Bez avansa · Maksājat saņemot · Piegāde 24/48 h",
    )),
    ("✅ I benefici reali", dict(cz="✅ Skutečné výhody", es="✅ Los beneficios reales", pt="✅ Os benefícios reais", sk="✅ Skutočné výhody", hu="✅ Valódi előnyök", lv="✅ Īstās priekšrocības")),
    ("Nessuna installazione, nessuna unità esterna, nessun tecnico. Lo appoggi a terra, colleghi la spina e basta.", dict(
        cz="Žádná instalace, žádná venkovní jednotka, žádný technik. Postavíte ho na zem, zapojíte šňůru a hotovo.",
        es="Ninguna instalación, ninguna unidad exterior, ningún técnico. Lo apoyas en el suelo, enchufas y listo.",
        pt="Nenhuma instalação, nenhuma unidade exterior, nenhum técnico. Pousa no chão, liga a ficha e está feito.",
        sk="Žiadna inštalácia, žiadna vonkajšia jednotka, žiadny technik. Postavíte ho na zem, zapojíte šnúru a hotovo.",
        hu="Sem telepítés, sem külső egység, sem szerelő. A földre állítja, bedugja, kész.",
        lv="Nekāda uzstādīšana, nekāds āra bloks, neviens tehniķis. Noliekat uz grīdas, iespraužat, un gatavs.",
    )),
    ("Clima PRO — Tecnologia FlowCore", dict(
        cz="Clima PRO — Technologie FlowCore", es="Clima PRO — Tecnología FlowCore", pt="Clima PRO — Tecnologia FlowCore",
        sk="Clima PRO — Technológia FlowCore", hu="Clima PRO — FlowCore technológia", lv="Clima PRO — FlowCore tehnoloģija",
    )),
    ("01 — Tecnologia FlowCore®", dict(
        cz="01 — Technologie FlowCore®", es="01 — Tecnología FlowCore®", pt="01 — Tecnologia FlowCore®",
        sk="01 — Technológia FlowCore®", hu="01 — FlowCore® technológia", lv="01 — FlowCore® tehnoloģija",
    )),
    ("FlowCore® sostituisce compressore e gas refrigeranti", dict(
        cz="FlowCore® nahrazuje kompresor a chladicí plyny",
        es="FlowCore® sustituye el compresor y los gases refrigerantes",
        pt="FlowCore® substitui o compressor e os gases refrigerantes",
        sk="FlowCore® nahrádza kompresor a chladiace plyny",
        hu="A FlowCore® kiváltja a kompresszort és a hűtőgázokat",
        lv="FlowCore® aizstāj kompresoru un aukstumaģentus",
    )),
    ("⏱️ Pronto in 90 secondi", dict(cz="⏱️ Připraveno za 90 sekund", es="⏱️ Listo en 90 segundos", pt="⏱️ Pronto em 90 segundos", sk="⏱️ Pripravené za 90 sekúnd", hu="⏱️ Kész 90 másodperc alatt", lv="⏱️ Gatavs 90 sekundēs")),
    ("👉 Su ruote", dict(cz="👉 Na kolečkách", es="👉 Con ruedas", pt="👉 Com rodas", sk="👉 Na kolieskach", hu="👉 Kerekeken", lv="👉 Uz riteņiem")),
    ("FlowCore® è il sistema interno ad alta efficienza che sostituisce compressore e gas refrigeranti tradizionali. Funziona semplicemente collegato alla presa di corrente di casa: sta in piedi da solo, appoggiato a terra, senza fissaggi alla parete né unità esterna.", dict(
        cz="FlowCore® je vysoce účinný interní systém, který nahrazuje tradiční kompresor a chladiva. Funguje zapojený do domácí zásuvky: stojí volně na zemi, bez kotvení do zdi a bez venkovní jednotky.",
        es="FlowCore® es el sistema interno de alta eficiencia que sustituye el compresor y los refrigerantes tradicionales. Funciona enchufado a un tomacorriente de casa: se sostiene solo, apoyado en el suelo, sin fijaciones a la pared ni unidad exterior.",
        pt="FlowCore® é o sistema interno de alta eficiência que substitui o compressor e os refrigerantes tradicionais. Funciona ligado à tomada de casa: fica de pé sozinho, pousado no chão, sem fixações na parede nem unidade exterior.",
        sk="FlowCore® je vysoko účinný interný systém, ktorý nahrádza tradičný kompresor a chladivá. Funguje zapojený do domácej zásuvky: stojí voľne na zemi, bez kotvenia do steny a bez vonkajšej jednotky.",
        hu="A FlowCore® nagy hatékonyságú belső rendszer, amely kiváltja a hagyományos kompresszort és hűtőközeget. Otthoni konnektorba dugva működik: magától áll a padlón, falrögzítés és külső egység nélkül.",
        lv="FlowCore® ir iekšēja augstas efektivitātes sistēma, kas aizstāj tradicionālo kompresoru un aukstumaģentus. Darbojas, iesprausta mājas rozetē: stāv pats uz grīdas, bez stiprinājumiem pie sienas un bez āra bloka.",
    )),
    ("Si attiva in meno di 90 secondi e raggiunge la temperatura impostata in circa 5 minuti. Con le ruote lo sposti da una stanza all'altra in dieci secondi: camera, soggiorno, ufficio, sempre lo stesso apparecchio. Senza preventivi, senza operai, senza aspettare settimane.", dict(
        cz="Spustí se do 90 sekund a nastavené teploty dosáhne zhruba za 5 minut. Na kolečkách ho přesunete z místnosti do místnosti za deset sekund: ložnice, obývák, kancelář — stále stejný přístroj. Bez nabídek, bez řemeslníků, bez čekání týdny.",
        es="Se activa en menos de 90 segundos y alcanza la temperatura en unos 5 minutos. Con las ruedas lo mueves de una habitación a otra en diez segundos: dormitorio, salón, oficina, siempre el mismo aparato. Sin presupuestos, sin operarios, sin esperar semanas.",
        pt="Ativa-se em menos de 90 segundos e atinge a temperatura em cerca de 5 minutos. Com as rodas move-o de uma divisão para outra em dez segundos: quarto, sala, escritório, sempre o mesmo aparelho. Sem orçamentos, sem operários, sem esperar semanas.",
        sk="Spustí sa do 90 sekúnd a nastavenú teplotu dosiahne zhruba za 5 minút. Na kolieskach ho presuniete z miestnosti do miestnosti za desať sekúnd: spálňa, obývačka, kancelária — stále ten istý prístroj. Bez ponúk, bez remeselníkov, bez čakania týždne.",
        hu="90 másodpercen belül bekapcsol, a beállított hőmérsékletet kb. 5 perc alatt éri el. Kerekeken tíz másodperc alatt viszi szobáról szobára: háló, nappali, iroda — ugyanaz a készülék. Ajánlat, szerelő és hetek várakozás nélkül.",
        lv="Ieslēdzas mazāk nekā 90 sekundēs un sasniedz temperatūru aptuveni 5 minūtēs. Ar riteņiem pārvietojat no istabas uz istabu desmit sekundēs: guļamistaba, dzīvojamā, birojs — vienmēr tā pati ierīce. Bez tāmes, bez strādniekiem, bez gaidīšanas nedēļām.",
    )),
    ("Clima PRO — 4 funzioni, 1 solo apparecchio", dict(
        cz="Clima PRO — 4 funkce, jeden přístroj", es="Clima PRO — 4 funciones, un solo aparato", pt="Clima PRO — 4 funções, um só aparelho",
        sk="Clima PRO — 4 funkcie, jeden prístroj", hu="Clima PRO — 4 funkció, egy készülék", lv="Clima PRO — 4 funkcijas, viena ierīce",
    )),
    ("02 — 4 funzioni, 1 solo apparecchio", dict(
        cz="02 — 4 funkce, jeden přístroj", es="02 — 4 funciones, un solo aparato", pt="02 — 4 funções, um só aparelho",
        sk="02 — 4 funkcie, jeden prístroj", hu="02 — 4 funkció, egy készülék", lv="02 — 4 funkcijas, viena ierīce",
    )),
    ("Raffredda, riscalda, deumidifica e purifica", dict(
        cz="Chladí, topí, odvlhčuje a čistí", es="Enfría, calienta, deshumidifica y purifica", pt="Arrefece, aquece, desumidifica e purifica",
        sk="Chladí, kúri, odvlhčuje a čistí", hu="Hűt, fűt, párátlanít és tisztít", lv="Dzesē, silda, sausina un attīra",
    )),
    ("99% germi", dict(cz="99 % zárodků", es="99% gérmenes", pt="99% germes", sk="99 % zárodkov", hu="99% kórokozó", lv="99% mikrobu")),
    ("Clima PRO™ raffredda, riscalda, purifica l'aria con filtro a tripla azione e deumidifica l'ambiente in automatico. Raffredda fino a <strong>16°C</strong>, riscalda fino a <strong>40°C</strong>, elimina fino al <strong>99%</strong> di germi e batteri nell'aria.", dict(
        cz="Clima PRO™ chladí, topí, čistí vzduch trojitým filtrem a automaticky odvlhčuje. Chladí až na <strong>16°C</strong>, topí až na <strong>40°C</strong>, odstraní až <strong>99 %</strong> zárodků a bakterií ze vzduchu.",
        es="Clima PRO™ enfría, calienta, purifica el aire con filtro de triple acción y deshumidifica en automático. Enfría hasta <strong>16°C</strong>, calienta hasta <strong>40°C</strong>, elimina hasta el <strong>99%</strong> de gérmenes y bacterias del aire.",
        pt="Clima PRO™ arrefece, aquece, purifica o ar com filtro de tripla ação e desumidifica em automático. Arrefece até <strong>16°C</strong>, aquece até <strong>40°C</strong>, elimina até <strong>99%</strong> de germes e bactérias no ar.",
        sk="Clima PRO™ chladí, kúri, čistí vzduch trojitým filtrom a automaticky odvlhčuje. Chladí až na <strong>16°C</strong>, kúri až na <strong>40°C</strong>, odstráni až <strong>99 %</strong> zárodkov a baktérií zo vzduchu.",
        hu="A Clima PRO™ hűt, fűt, hármas szűrővel tisztítja a levegőt és automatikusan párátlanít. Akár <strong>16°C-ra</strong> hűt, <strong>40°C-ig</strong> fűt, a levegőben lévő kórokozók és baktériumok akár <strong>99%-át</strong> eltávolítja.",
        lv="Clima PRO™ dzesē, silda, attīra gaisu ar trīskāršu filtru un automātiski sausina. Dzesē līdz <strong>16°C</strong>, silda līdz <strong>40°C</strong>, noņem līdz <strong>99%</strong> mikrobu un baktēriju no gaisa.",
    )),
    ("Non dovrai più comprare un deumidificatore, un purificatore e un riscaldatore separati. Risparmi spazio in casa e centinaia di euro in acquisti multipli.", dict(
        cz="Už nemusíte kupovat zvlášť odvlhčovač, čističku a přímotop. Ušetříte místo v bytě i tisíce korun za další nákupy.",
        es="Ya no tendrás que comprar un deshumidificador, un purificador y un calefactor por separado. Ahorras espacio en casa y cientos de euros en compras múltiples.",
        pt="Já não precisa de comprar um desumidificador, um purificador e um aquecedor em separado. Poupa espaço em casa e centenas de euros em compras múltiplas.",
        sk="Už nemusíte kupovať zvlášť odvlhčovač, čističku a ohrievač. Ušetríte miesto v byte aj stovky eur za ďalšie nákupy.",
        hu="Nem kell külön párátlanítót, légtisztítót és fűtőt vennie. Helyet spórol otthon, és több tízezer forintot a plusz vásárlásokon.",
        lv="Vairs nav jāpērk atsevišķi mitruma savācējs, gaisa attīrītājs un sildītājs. Ietaupāt vietu mājās un simtiem eiro papildu pirkumos.",
    )),
    ("Clima PRO — Consumi minimi, risparmio massimo", dict(
        cz="Clima PRO — Minimální spotřeba, maximální úspora", es="Clima PRO — Consumo mínimo, ahorro máximo", pt="Clima PRO — Consumo mínimo, poupança máxima",
        sk="Clima PRO — Minimálna spotreba, maximálna úspora", hu="Clima PRO — Minimális fogyasztás, maximális megtakarítás", lv="Clima PRO — Minimāls patēriņš, maksimāls ietaupījums",
    )),
    ("03 — Consumi minimi, risparmio massimo", dict(
        cz="03 — Minimální spotřeba, maximální úspora", es="03 — Consumo mínimo, ahorro máximo", pt="03 — Consumo mínimo, poupança máxima",
        sk="03 — Minimálna spotreba, maximálna úspora", hu="03 — Minimális fogyasztás, maximális megtakarítás", lv="03 — Minimāls patēriņš, maksimāls ietaupījums",
    )),
    ("Classe energetica A+++ e bollette più leggere", dict(
        cz="Energetická třída A+++ a nižší účty", es="Clase energética A+++ y facturas más bajas", pt="Classe energética A+++ e faturas mais leves",
        sk="Energetická trieda A+++ a nižšie účty", hu="A+++ energiaosztály és könnyebb számlák", lv="Enerģijas klase A+++ un vieglāki rēķini",
    )),
    ("0,12€ / ora", dict(cz="3 Kč / hod", es="0,12€ / hora", pt="0,12€ / hora", sk="0,12€ / hod", hu="50 Ft / óra", lv="0,12€ / stundā")),
    ("Fino a -80%", dict(cz="Až -80 %", es="Hasta -80%", pt="Até -80%", sk="Až -80 %", hu="Akár -80%", lv="Līdz -80%")),
    ("Grazie alla Classe energetica A+++, Clima PRO™ ottimizza automaticamente potenza e flusso d'aria in base alla temperatura della stanza. Consumo da <strong>0,12€ l'ora</strong>, fino all'<strong>80% in meno</strong> rispetto a un climatizzatore tradizionale con unità esterna.", dict(
        cz="Díky třídě A+++ Clima PRO™ automaticky ladí výkon a proudění podle teploty v místnosti. Spotřeba od <strong>3 Kč za hodinu</strong>, až o <strong>80 % méně</strong> než u klasické klimatizace s venkovní jednotkou.",
        es="Gracias a la clase A+++, Clima PRO™ optimiza automáticamente potencia y flujo de aire según la temperatura de la habitación. Consumo desde <strong>0,12€ la hora</strong>, hasta un <strong>80% menos</strong> que un aire acondicionado tradicional con unidad exterior.",
        pt="Graças à classe A+++, o Clima PRO™ otimiza automaticamente potência e fluxo de ar segundo a temperatura da divisão. Consumo desde <strong>0,12€ por hora</strong>, até <strong>80% menos</strong> do que um ar condicionado tradicional com unidade exterior.",
        sk="Vďaka triede A+++ Clima PRO™ automaticky ladí výkon a prúdenie podľa teploty v miestnosti. Spotreba od <strong>0,12€ za hodinu</strong>, až o <strong>80 % menej</strong> ako pri klasickej klimatizácii s vonkajšou jednotkou.",
        hu="Az A+++ osztálynak köszönhetően a Clima PRO™ automatikusan hangolja a teljesítményt és a légáramot a szoba hőmérsékletéhez. Fogyasztás <strong>50 Ft/órától</strong>, akár <strong>80%-kal kevesebb</strong>, mint egy hagyományos, külső egységes klímánál.",
        lv="Pateicoties A+++ klasei, Clima PRO™ automātiski pielāgo jaudu un gaisa plūsmu telpas temperatūrai. Patēriņš no <strong>0,12€ stundā</strong>, līdz <strong>80% mazāk</strong> nekā tradicionālam kondicionierim ar āra bloku.",
    )),
    ("Potrai tenerlo acceso tutta la notte, tutti i giorni, senza guardare con ansia la bolletta a fine mese.", dict(
        cz="Můžete ho nechat běžet celou noc, každý den, aniž byste na konci měsíce s obavami koukali na účet.",
        es="Podrás dejarlo encendido toda la noche, todos los días, sin mirar la factura con ansiedad a fin de mes.",
        pt="Pode deixá-lo ligado a noite toda, todos os dias, sem olhar para a fatura com ansiedade no fim do mês.",
        sk="Môžete ho nechať bežať celú noc, každý deň, bez toho, aby ste na konci mesiaca s obavami pozerali na účet.",
        hu="Egész éjjel, minden nap bekapcsolva hagyhatja, anélkül, hogy a hónap végén izgulna a számla miatt.",
        lv="Varat to atstāt ieslēgtu visu nakti, katru dienu, neskatoties uz rēķinu ar satraukumu mēneša beigās.",
    )),
    ("Ordina Ora il Tuo Clima PRO™ ↓", dict(
        cz="Objednejte Clima PRO™ teď ↓", es="Pide ahora tu Clima PRO™ ↓", pt="Encomende agora o seu Clima PRO™ ↓",
        sk="Objednajte Clima PRO™ teraz ↓", hu="Rendelje meg most a Clima PRO™-t ↓", lv="Pasūtiet savu Clima PRO™ tagad ↓",
    )),
    ("💵 Pagamento alla consegna", dict(cz="💵 Platba na dobírku", es="💵 Pago contra reembolso", pt="💵 Pagamento à cobrança", sk="💵 Platba na dobierku", hu="💵 Utánvét", lv="💵 Maksa pēc saņemšanas")),
    ("🚚 Spedizione 24/48h", dict(cz="🚚 Doručení 24/48 h", es="🚚 Envío 24/48 h", pt="🚚 Envio 24/48 h", sk="🚚 Doručenie 24/48 h", hu="🚚 Szállítás 24/48 óra", lv="🚚 Piegāde 24/48 h")),
    ("↩️ 60 giorni di prova", dict(cz="↩️ 60 dní na vyzkoušení", es="↩️ 60 días de prueba", pt="↩️ 60 dias de prova", sk="↩️ 60 dní na vyskúšanie", hu="↩️ 60 napos próba", lv="↩️ 60 dienu izmēģinājums")),
    ("⚖️ Il confronto", dict(cz="⚖️ Srovnání", es="⚖️ La comparación", pt="⚖️ A comparação", sk="⚖️ Porovnanie", hu="⚖️ Összehasonlítás", lv="⚖️ Salīdzinājums")),
    ("Perché Clima PRO batte il climatizzatore tradizionale", dict(
        cz="Proč Clima PRO poráží klasickou klimatizaci", es="Por qué Clima PRO gana al aire acondicionado tradicional",
        pt="Porque o Clima PRO vence o ar condicionado tradicional", sk="Prečo Clima PRO poráža klasickú klimatizáciu",
        hu="Miért veri a Clima PRO a hagyományos klímát", lv="Kāpēc Clima PRO pārspēj tradicionālo kondicionieri",
    )),
    ("Stessa aria fresca, nessun lavoro necessario.", dict(
        cz="Stejný chladný vzduch, žádná práce navíc.", es="El mismo aire fresco, ningún trabajo necesario.",
        pt="O mesmo ar fresco, nenhum trabalho necessário.", sk="Rovnaký chladný vzduch, žiadna práca naviac.",
        hu="Ugyanaz a hűvös levegő, semmi munka.", lv="Tas pats vēsais gaiss, nekāds darbs.",
    )),
    ("Climatizzatore tradizionale", dict(
        cz="Klasická klimatizace", es="Aire acondicionado tradicional", pt="Ar condicionado tradicional",
        sk="Klasická klimatizácia", hu="Hagyományos klíma", lv="Tradicionālais kondicionieris",
    )),
    ("Tecnico + unità esterna", dict(
        cz="Technik + venkovní jednotka", es="Técnico + unidad exterior", pt="Técnico + unidade exterior",
        sk="Technik + vonkajšia jednotka", hu="Szerelő + külső egység", lv="Tehniķis + āra bloks",
    )),
    ("✅ Nessuna: lo appoggi a terra e colleghi la spina", dict(
        cz="✅ Žádná: postavíte na zem a zapojíte", es="✅ Ninguna: lo apoyas en el suelo y enchufas",
        pt="✅ Nenhuma: pousa no chão e liga a ficha", sk="✅ Žiadna: postavíte na zem a zapojíte",
        hu="✅ Semmi: földre állítja és bedugja", lv="✅ Nekāda: noliekat uz grīdas un iespraužat",
    )),
    ("Giorni o settimane", dict(cz="Dny nebo týdny", es="Días o semanas", pt="Dias ou semanas", sk="Dni alebo týždne", hu="Napok vagy hetek", lv="Dienas vai nedēļas")),
    ("✅ Pronto in 5 minuti", dict(cz="✅ Připraveno za 5 minut", es="✅ Listo en 5 minutos", pt="✅ Pronto em 5 minutos", sk="✅ Pripravené za 5 minút", hu="✅ 5 perc alatt kész", lv="✅ Gatavs 5 minūtēs")),
    ("Costo installazione", dict(cz="Cena instalace", es="Coste de instalación", pt="Custo de instalação", sk="Cena inštalácie", hu="Telepítési költség", lv="Uzstādīšanas izmaksas")),
    ("400-800€", dict(cz="10 000–20 000 Kč", es="400-800€", pt="400-800€", sk="400-800€", hu="160 000–320 000 Ft", lv="400-800€")),
    ("✅ 0€", dict(cz="✅ 0 Kč", es="✅ 0€", pt="✅ 0€", sk="✅ 0€", hu="✅ 0 Ft", lv="✅ 0€")),
    ("Rumore notturno", dict(cz="Noční hluk", es="Ruido nocturno", pt="Ruído noturno", sk="Nočný hluk", hu="Éjszakai zaj", lv="Nakts troksnis")),
    ("35-45 dB, spesso disturba", dict(
        cz="35–45 dB, často ruší", es="35-45 dB, a menudo molesta", pt="35-45 dB, muitas vezes incomoda",
        sk="35–45 dB, často ruší", hu="35–45 dB, gyakran zavar", lv="35-45 dB, bieži traucē",
    )),
    ("✅ 18 dB, quasi impercettibile", dict(
        cz="✅ 18 dB, skoro neslyšitelné", es="✅ 18 dB, casi imperceptible", pt="✅ 18 dB, quase impercetível",
        sk="✅ 18 dB, skoro nepočuteľné", hu="✅ 18 dB, szinte észrevehetetlen", lv="✅ 18 dB, gandrīz nemanāms",
    )),
    ("Solo raffredda", dict(cz="Jen chladí", es="Solo enfría", pt="Só arrefece", sk="Len chladí", hu="Csak hűt", lv="Tikai dzesē")),
    ("✅ Raffredda, riscalda, deumidifica, purifica", dict(
        cz="✅ Chladí, topí, odvlhčuje, čistí", es="✅ Enfría, calienta, deshumidifica, purifica",
        pt="✅ Arrefece, aquece, desumidifica, purifica", sk="✅ Chladí, kúri, odvlhčuje, čistí",
        hu="✅ Hűt, fűt, párátlanít, tisztít", lv="✅ Dzesē, silda, sausina, attīra",
    )),
    ("Puoi spostarlo?", dict(cz="Můžete ho přemístit?", es="¿Puedes moverlo?", pt="Pode movê-lo?", sk="Môžete ho premiestniť?", hu="Átvihető?", lv="Vai var pārvietot?")),
    ("No: resta fisso alla parete dove l'hanno montato", dict(
        cz="Ne: zůstane tam, kde ho namontovali", es="No: queda fijo en la pared donde lo montaron",
        pt="Não: fica fixo na parede onde o montaram", sk="Nie: ostane tam, kde ho namontovali",
        hu="Nem: ott marad, ahová felszerelték", lv="Nē: paliek pie sienas, kur to uzmontēja",
    )),
    ("✅ Sì: è su ruote, lo porti in qualsiasi stanza", dict(
        cz="✅ Ano: je na kolečkách, odvezete ho kamkoli", es="✅ Sí: va sobre ruedas, lo llevas a cualquier habitación",
        pt="✅ Sim: tem rodas, leva-o para qualquer divisão", sk="✅ Áno: je na kolieskach, odveziete ho kamkoľvek",
        hu="✅ Igen: kerekeken bármelyik szobába viszi", lv="✅ Jā: ir uz riteņiem, aizvedat uz jebkuru istabu",
    )),
    ("Sì, voglio Clima PRO a 99€ →", dict(
        cz="Ano, chci Clima PRO za 1 799 Kč →",
        es="Sí, quiero Clima PRO a 79,00€ →",
        pt="Sim, quero Clima PRO a 89,00€ →",
        sk="Áno, chcem Clima PRO za 69,00€ →",
        hu="Igen, kérem a Clima PRO-t 39 900 Ft →",
        lv="Jā, gribu Clima PRO par 89,00€ →",
    )),
    ("⭐ Chi lo usa ogni giorno", dict(cz="⭐ Kdo ho používá každý den", es="⭐ Quién lo usa cada día", pt="⭐ Quem o usa todos os dias", sk="⭐ Kto ho používa každý deň", hu="⭐ Aki minden nap használja", lv="⭐ Kas to lieto katru dienu")),
    ("Cosa dicono le famiglie che l'hanno già provato", dict(
        cz="Co říkají rodiny, které ho už vyzkoušely", es="Qué dicen las familias que ya lo han probado",
        pt="O que dizem as famílias que já o experimentaram", sk="Čo hovoria rodiny, ktoré ho už vyskúšali",
        hu="Mit mondanak a családok, akik már kipróbálták", lv="Ko saka ģimenes, kas jau ir izmēģinājušas",
    )),
    ("★★★★★ 4,8/5 su oltre 1.824 recensioni verificate", dict(
        cz="★★★★★ 4,8/5 z více než 1 824 ověřených recenzí", es="★★★★★ 4,8/5 en más de 1.824 reseñas verificadas",
        pt="★★★★★ 4,8/5 em mais de 1.824 avaliações verificadas", sk="★★★★★ 4,8/5 z viac ako 1 824 overených recenzií",
        hu="★★★★★ 4,8/5 több mint 1 824 ellenőrzött értékelés alapján", lv="★★★★★ 4,8/5 no vairāk nekā 1 824 pārbaudītām atsauksmēm",
    )),
    ("Recensione Clima PRO Giulia T.", dict(
        cz="Recenze Clima PRO Jana T.", es="Reseña Clima PRO Julia T.", pt="Avaliação Clima PRO Júlia T.",
        sk="Recenzia Clima PRO Jana T.", hu="Clima PRO értékelés Júlia T.", lv="Clima PRO atsauksme Jūlija T.",
    )),
    ("«Ero scettica, pensavo fosse l'ennesimo gadget che finisce in cantina dopo un mese. Invece lo uso ogni giorno da giugno: in camera la sera è perfetto, e con il timer si spegne da solo. Unico neo: il telecomando, ogni tanto lo perdo tra le lenzuola ahah»", dict(
        cz="„Byla jsem skeptická, myslela jsem, že je to další gadget, který skončí ve sklepě. Místo toho ho používám každý den od června: v ložnici večer je perfektní a s časovačem se sám vypne. Jediná vada: dálkový ovladač, občas ho ztratím v peřinách ahah“",
        es="«Estaba escéptica, pensaba que era otro gadget que acaba en el trastero. En cambio lo uso cada día desde junio: en el dormitorio por la noche es perfecto, y con el temporizador se apaga solo. El único pero: el mando, a veces lo pierdo entre las sábanas jaja»",
        pt="«Estava cética, pensava que era mais um gadget a acabar na arrecadação. Em vez disso uso-o todos os dias desde junho: no quarto à noite é perfeito, e com o temporizador desliga-se sozinho. O único senão: o comando, às vezes perco-o entre os lençóis ahah»",
        sk="„Bola som skeptická, myslela som, že je to ďalší gadget, ktorý skončí v pivnici. Namiesto toho ho používam každý deň od júna: v spálni večer je perfektný a s časovačom sa sám vypne. Jediná vada: diaľkový ovládač, občas ho stratím v perinách ahah“",
        hu="„Szkeptikus voltam, azt hittem, megint egy kütyü, ami a pincében landol. Ehelyett június óta minden nap használom: a hálóban este tökéletes, és az időzítővel magától kikapcsol. Egyetlen baj: a távirányító, néha elveszítem a paplan között ahah”",
        lv="«Biju skeptiska, domāju, ka tas ir kārtējais sīkrīks, kas nonāks pagrabā. Tā vietā lietoju katru dienu kopš jūnija: guļamistabā vakarā ir ideāli, un ar taimeri pats izslēdzas. Vienīgais mīnuss: pults, reizēm pazaudēju starp palagiem ahah»",
    )),
    ("Giulia T., Bologna ✅ — Acquisto verificato", dict(
        cz="Jana T., Praha ✅ — Ověřený nákup", es="Julia T., Madrid ✅ — Compra verificada", pt="Júlia T., Lisboa ✅ — Compra verificada",
        sk="Jana T., Bratislava ✅ — Overený nákup", hu="Júlia T., Budapest ✅ — Ellenőrzött vásárlás", lv="Jūlija T., Rīga ✅ — Pārbaudīts pirkums",
    )),
    ("Recensione Clima PRO Davide P.", dict(
        cz="Recenze Clima PRO David P.", es="Reseña Clima PRO David P.", pt="Avaliação Clima PRO David P.",
        sk="Recenzia Clima PRO Dávid P.", hu="Clima PRO értékelés Dávid P.", lv="Clima PRO atsauksme Dāvids P.",
    )),
    ("«Lo abbiamo preso per lo studio di mio marito che lavora da casa. D'inverno lo accende al mattino ed è già caldo dopo pochi secondi. La bolletta di gennaio è stata più bassa del previsto, e questo per noi è stato il vero motivo per consigliarlo.»", dict(
        cz="„Pořídili jsme ho do pracovny manžela, který pracuje z domova. V zimě ho ráno zapne a za pár sekund je teplo. Lednový účet byl nižší, než jsme čekali — a to byl ten pravý důvod, proč ho doporučujeme.“",
        es="«Lo compramos para el despacho de mi marido, que trabaja desde casa. En invierno lo enciende por la mañana y ya está caliente en segundos. La factura de enero fue más baja de lo esperado, y ese fue el verdadero motivo para recomendarlo.»",
        pt="«Comprámos para o escritório do meu marido, que trabalha em casa. No inverno liga de manhã e já está quente em segundos. A fatura de janeiro foi mais baixa do que o esperado, e esse foi o verdadeiro motivo para o recomendar.»",
        sk="„Kúpili sme ho do pracovne manžela, ktorý pracuje z domu. V zime ho ráno zapne a za pár sekúnd je teplo. Januárový účet bol nižší, než sme čakali — a to bol ten pravý dôvod, prečo ho odporúčame.“",
        hu="„A férjem home office-ához vettük. Télen reggel bekapcsolja, és másodpercek alatt meleg van. A januári számla alacsonyabb lett a vártnál — ez volt az igazi ok, hogy ajánljuk.”",
        lv="«Nopirkām vīra kabinetam, viņš strādā no mājām. Ziemā no rīta ieslēdz, un pēc dažām sekundēm jau ir silts. Janvāra rēķins bija zemāks, nekā gaidījām — tas bija īstais iemesls to ieteikt.»",
    )),
    ("Davide P., Napoli ✅ — Acquisto verificato", dict(
        cz="David P., Brno ✅ — Ověřený nákup", es="David P., Barcelona ✅ — Compra verificada", pt="David P., Porto ✅ — Compra verificada",
        sk="Dávid P., Košice ✅ — Overený nákup", hu="Dávid P., Debrecen ✅ — Ellenőrzött vásárlás", lv="Dāvids P., Liepāja ✅ — Pārbaudīts pirkums",
    )),
    ("Recensione Clima PRO Sara M.", dict(
        cz="Recenze Clima PRO Sara M.", es="Reseña Clima PRO Sara M.", pt="Avaliação Clima PRO Sara M.",
        sk="Recenzia Clima PRO Sara M.", hu="Clima PRO értékelés Sara M.", lv="Clima PRO atsauksme Sara M.",
    )),
    ("«Vivo in affitto e non potevo installare un climatizzatore vero. Con Clima PRO™ ho risolto in un pomeriggio: nessun foro, nessun permesso da chiedere al proprietario. D'estate lo tengo in camera, d'inverno lo porto in salotto. Di notte in modalità silenziosa non lo sento nemmeno.»", dict(
        cz="„Bydlím v nájmu a nemohla jsem nainstalovat pořádnou klimatizaci. S Clima PRO™ jsem to vyřešila za odpoledne: žádná díra, žádné povolení od majitele. V létě ho mám v ložnici, v zimě v obýváku. V tichém nočním režimu ho skoro neslyším.“",
        es="«Vivo de alquiler y no podía instalar un aire acondicionado de verdad. Con Clima PRO™ lo resolví en una tarde: ningún agujero, ningún permiso al casero. En verano lo tengo en el dormitorio, en invierno en el salón. De noche en modo silencioso ni lo oigo.»",
        pt="«Vivo de arrendamento e não podia instalar um ar condicionado a sério. Com o Clima PRO™ resolvi numa tarde: nenhum furo, nenhuma autorização do senhorio. No verão fica no quarto, no inverno na sala. À noite no modo silencioso nem o oiço.»",
        sk="„Bývam v nájme a nemohla som nainštalovať poriadnu klimatizáciu. S Clima PRO™ som to vyriešila za popoludnie: žiadna diera, žiadne povolenie od majiteľa. V lete ho mám v spálni, v zime v obývačke. V tichom nočnom režime ho skoro nepočujem.“",
        hu="„Albérletben lakom, és nem szerelhettem fel igazi klímát. A Clima PRO™-rel egy délután alatt megoldottam: sem lyuk, sem engedély a tulajtól. Nyáron a hálóban van, télen a nappaliban. Éjjel csendes módban szinte nem hallom.”",
        lv="«Dzīvoju īrētā dzīvoklī un nevarēju uzstādīt īstu kondicionieri. Ar Clima PRO™ atrisināju pēcpusdienā: ne cauruma, ne atļaujas no saimnieka. Vasarā tas ir guļamistabā, ziemā dzīvojamajā. Naktī klusajā režīmā gandrīz nedzirdu.»",
    )),
    ("Sara M., Torino ✅ — Acquisto verificato", dict(
        cz="Sara M., Ostrava ✅ — Ověřený nákup", es="Sara M., Valencia ✅ — Compra verificada", pt="Sara M., Faro ✅ — Compra verificada",
        sk="Sara M., Žilina ✅ — Overený nákup", hu="Sara M., Szeged ✅ — Ellenőrzött vásárlás", lv="Sara M., Daugavpils ✅ — Pārbaudīts pirkums",
    )),
    ("📦 Cosa trovi nel pacco", dict(cz="📦 Co je v balení", es="📦 Qué hay en el paquete", pt="📦 O que encontra na caixa", sk="📦 Čo je v balení", hu="📦 Mi van a csomagban", lv="📦 Kas ir paciņā")),
    ("Tutto nella scatola.<br>Zero acquisti aggiuntivi. Zero sorprese.", dict(
        cz="Všechno v krabici.<br>Žádné další nákupy. Žádná překvapení.",
        es="Todo en la caja.<br>Cero compras extra. Cero sorpresas.",
        pt="Tudo na caixa.<br>Zero compras extra. Zero surpresas.",
        sk="Všetko v krabici.<br>Žiadne ďalšie nákupy. Žiadne prekvapenia.",
        hu="Minden a dobozban.<br>Semmi extra vásárlás. Semmi meglepetés.",
        lv="Viss kastē.<br>Nulle papildu pirkumu. Nulle pārsteigumu.",
    )),
    ("Kit completo Clima PRO climatizzatore a colonna portatile", dict(
        cz="Kompletní sada Clima PRO přenosná sloupová klimatizace",
        es="Kit completo Clima PRO climatizador de columna portátil",
        pt="Kit completo Clima PRO climatizador de coluna portátil",
        sk="Kompletná sada Clima PRO prenosná stĺpová klimatizácia",
        hu="Teljes Clima PRO hordozható oszlopklíma készlet",
        lv="Pilns Clima PRO pārnēsājama kolonnas klimatizatora komplekts",
    )),
    ("Apri la scatola, lo appoggi a terra, colleghi la spina e in 5 minuti la stanza è già fresca. Tutto qui.", dict(
        cz="Otevřete krabici, postavíte ho na zem, zapojíte šňůru a za 5 minut je v místnosti chladno. A to je vše.",
        es="Abres la caja, lo apoyas en el suelo, enchufas y en 5 minutos la habitación ya está fresca. Eso es todo.",
        pt="Abre a caixa, pousa no chão, liga a ficha e em 5 minutos a divisão já está fresca. É só isto.",
        sk="Otvoríte krabicu, postavíte ho na zem, zapojíte šnúru a za 5 minút je v miestnosti chladno. A to je všetko.",
        hu="Kinyitja a dobozt, a földre állítja, bedugja, és 5 perc múlva a szoba már hűvös. Ennyi.",
        lv="Atverat kasti, noliekat uz grīdas, iespraužat, un pēc 5 minūtēm telpa jau ir vēsa. Un tas arī viss.",
    )),
    ("1x Climatizzatore a colonna portatile Clima PRO 18.000 BTU", dict(
        cz="1× přenosná sloupová klimatizace Clima PRO 18.000 BTU",
        es="1× climatizador de columna portátil Clima PRO 18.000 BTU",
        pt="1× climatizador de coluna portátil Clima PRO 18.000 BTU",
        sk="1× prenosná stĺpová klimatizácia Clima PRO 18.000 BTU",
        hu="1× hordozható oszlopklíma Clima PRO 18.000 BTU",
        lv="1× pārnēsājams kolonnas klimatizators Clima PRO 18.000 BTU",
    )),
    ("4x Ruote piroettanti già montate alla base", dict(
        cz="4× otočná kolečka už namontovaná na základně", es="4× ruedas giratorias ya montadas en la base",
        pt="4× rodas giratórias já montadas na base", sk="4× otočné kolieska už namontované na základni",
        hu="4× már a talpra szerelt guruló kerék", lv="4× grozāmi riteņi jau uzstādīti uz pamatnes",
    )),
    ("1x Telecomando incluso", dict(cz="1× dálkový ovladač v balení", es="1× mando a distancia incluido", pt="1× comando incluído", sk="1× diaľkový ovládač v balení", hu="1× távirányító a csomagban", lv="1× tālvadības pults komplektā")),
    ("1x Manuale d'uso in italiano", dict(
        cz="1× návod k použití v češtině", es="1× manual de uso en español", pt="1× manual de utilização em português",
        sk="1× návod na použitie v slovenčine", hu="1× magyar használati útmutató", lv="1× lietošanas instrukcija latviešu valodā",
    )),
    ("Accesso all'app dedicata per il controllo da smartphone", dict(
        cz="Přístup k aplikaci pro ovládání z telefonu", es="Acceso a la app para control desde el smartphone",
        pt="Acesso à app para controlo pelo smartphone", sk="Prístup k aplikácii na ovládanie z telefónu",
        hu="Hozzáférés az apphoz okostelefonos vezérléshez", lv="Piekļuve lietotnei vadībai no viedtālruņa",
    )),
    ("Spedizione gratuita in 24-48h", dict(
        cz="Doprava zdarma do 24–48 h", es="Envío gratuito en 24-48 h", pt="Envio gratuito em 24-48 h",
        sk="Doprava zadarmo do 24–48 h", hu="Ingyenes szállítás 24–48 óra", lv="Bezmaksas piegāde 24–48 h",
    )),
    ("Garanzia estesa 2 anni", dict(cz="Prodloužená záruka 2 roky", es="Garantía ampliada 2 años", pt="Garantia alargada 2 anos", sk="Predĺžená záruka 2 roky", hu="2 év meghosszabbított garancia", lv="Pagarināta 2 gadu garantija")),
    ("❓ Domande frequenti", dict(cz="❓ Časté otázky", es="❓ Preguntas frecuentes", pt="❓ Perguntas frequentes", sk="❓ Časté otázky", hu="❓ Gyakori kérdések", lv="❓ Biežākie jautājumi")),
    ("Hai dei dubbi? È normale.<br>Li chiariamo qui.", dict(
        cz="Máte pochybnosti? To je v pořádku.<br>Vyjasníme je tady.",
        es="¿Tienes dudas? Es normal.<br>Las aclaramos aquí.",
        pt="Tem dúvidas? É normal.<br>Esclarecemos aqui.",
        sk="Máte pochybnosti? To je v poriadku.<br>Vyjasníme ich tu.",
        hu="Kétségei vannak? Ez természetes.<br>Itt tisztázzuk.",
        lv="Ir šaubas? Tas ir normāli.<br>Noskaidrosim šeit.",
    )),
    ("Prima di ordinare, trova le risposte alle domande più comuni su rumore, installazione, pagamento e garanzia.", dict(
        cz="Než objednáte, najděte odpovědi na nejčastější otázky o hluku, instalaci, platbě a záruce.",
        es="Antes de pedir, encuentra respuestas sobre ruido, instalación, pago y garantía.",
        pt="Antes de encomendar, encontre respostas sobre ruído, instalação, pagamento e garantia.",
        sk="Než objednáte, nájdite odpovede na najčastejšie otázky o hluku, inštalácii, platbe a záruke.",
        hu="Rendelés előtt találja meg a zajra, telepítésre, fizetésre és garanciára vonatkozó válaszokat.",
        lv="Pirms pasūtīšanas atrodiet atbildes par troksni, uzstādīšanu, maksājumu un garantiju.",
    )),
    ("È rumoroso di notte?", dict(cz="Je v noci hlučný?", es="¿Hace ruido por la noche?", pt="Faz barulho à noite?", sk="Je v noci hlučný?", hu="Zajos éjszaka?", lv="Vai naktī ir skaļš?")),
    ("No: in modalità notte scende a 18 dB, un livello sonoro più basso di un sussurro. È pensato apposta per la camera da letto.", dict(
        cz="Ne: v nočním režimu klesne na 18 dB, tišší než šepot. Je navržený právě do ložnice.",
        es="No: en modo noche baja a 18 dB, más bajo que un susurro. Está pensado para el dormitorio.",
        pt="Não: no modo noite desce para 18 dB, mais baixo do que um sussurro. Foi pensado para o quarto.",
        sk="Nie: v nočnom režime klesne na 18 dB, tichšie ako šepot. Je navrhnutý práve do spálne.",
        hu="Nem: éjszakai módban 18 dB-re csökken, halkabb egy suttogásnál. Pont hálószobába tervezték.",
        lv="Nē: nakts režīmā nokrītas līdz 18 dB, klusāks par čukstu. Radīts tieši guļamistabai.",
    )),
    ("Devo installarlo o chiamare un tecnico?", dict(
        cz="Musím ho instalovat nebo volat technika?", es="¿Tengo que instalarlo o llamar a un técnico?",
        pt="Tenho de o instalar ou chamar um técnico?", sk="Musím ho inštalovať alebo volať technika?",
        hu="Telepítenem kell, vagy szerelőt hívni?", lv="Vai jāuzstāda vai jāizsauc tehniķis?",
    )),
    ("No. Clima PRO non va fissato al muro e non ha unità esterna: lo appoggi a terra, colleghi la spina e in 5 minuti è già operativo. Quando vuoi cambiarlo di stanza lo spingi sulle ruote.", dict(
        cz="Ne. Clima PRO se nepřipevňuje na zeď a nemá venkovní jednotku: postavíte ho na zem, zapojíte šňůru a za 5 minut funguje. Když chcete změnit místnost, odstrčíte ho na kolečkách.",
        es="No. Clima PRO no se fija a la pared y no tiene unidad exterior: lo apoyas en el suelo, enchufas y en 5 minutos está listo. Si quieres cambiar de habitación, lo empujas sobre las ruedas.",
        pt="Não. O Clima PRO não se fixa à parede e não tem unidade exterior: pousa no chão, liga a ficha e em 5 minutos está a funcionar. Se quiser mudar de divisão, empurra-o sobre as rodas.",
        sk="Nie. Clima PRO sa nepripevňuje na stenu a nemá vonkajšiu jednotku: postavíte ho na zem, zapojíte šnúru a za 5 minút funguje. Keď chcete zmeniť miestnosť, odstrčíte ho na kolieskach.",
        hu="Nem. A Clima PRO nem a falra kerül, és nincs külső egysége: a földre állítja, bedugja, és 5 perc múlva működik. Ha szobát váltana, kerekeken tolja.",
        lv="Nē. Clima PRO nav jāstiprina pie sienas un tam nav āra bloka: noliekat uz grīdas, iespraužat, un pēc 5 minūtēm tas darbojas. Ja gribat mainīt istabu, palīdzat uz riteņiem.",
    )),
    ("Copre davvero 120 m²?", dict(cz="Opravdu pokryje 120 m²?", es="¿Cubre de verdad 120 m²?", pt="Cobre mesmo 120 m²?", sk="Naozaj pokryje 120 m²?", hu="Tényleg 120 m²-t fed?", lv="Vai tiešām nosedz 120 m²?")),
    ("Sì, grazie alla potenza di 18.000 BTU. Per ambienti molto grandi ti consigliamo di tenerlo nella stanza principale e lasciare le porte aperte per distribuire l'aria.", dict(
        cz="Ano, díky výkonu 18.000 BTU. U velmi velkých prostor ho nechte v hlavní místnosti a nechte dveře otevřené, aby se vzduch rozložil.",
        es="Sí, gracias a la potencia de 18.000 BTU. En espacios muy grandes, déjalo en la habitación principal y abre las puertas para distribuir el aire.",
        pt="Sim, graças à potência de 18.000 BTU. Em espaços muito grandes, deixe-o na divisão principal e abra as portas para distribuir o ar.",
        sk="Áno, vďaka výkonu 18.000 BTU. Pri veľmi veľkých priestoroch ho nechajte v hlavnej miestnosti a nechajte dvere otvorené, aby sa vzduch rozložil.",
        hu="Igen, a 18.000 BTU teljesítménynek köszönhetően. Nagyon nagy terekben a fő szobában tartsa, és nyissa ki az ajtókat, hogy a levegő szétoszoljon.",
        lv="Jā, pateicoties 18.000 BTU jaudai. Ļoti lielās telpās atstājiet to galvenajā istabā un turiet durvis vaļā, lai gaiss izplatītos.",
    )),
    ("Fa solo freddo o anche caldo?", dict(cz="Umí jen chladit, nebo i topit?", es="¿Solo enfría o también calienta?", pt="Só arrefece ou também aquece?", sk="Vie len chladiť, alebo aj kúriť?", hu="Csak hűt, vagy fűt is?", lv="Vai tikai dzesē, vai arī silda?")),
    ("Entrambi. Raffredda in estate, riscalda in inverno, e in più deumidifica e purifica l'aria: un solo apparecchio per tutto l'anno.", dict(
        cz="Obojí. V létě chladí, v zimě topí a navíc odvlhčuje a čistí vzduch: jeden přístroj na celý rok.",
        es="Ambos. Enfría en verano, calienta en invierno y además deshumidifica y purifica: un solo aparato para todo el año.",
        pt="Ambos. Arrefece no verão, aquece no inverno e ainda desumidifica e purifica: um só aparelho para o ano todo.",
        sk="Oboje. V lete chladí, v zime kúri a navyše odvlhčuje a čistí vzduch: jeden prístroj na celý rok.",
        hu="Mindkettő. Nyáron hűt, télen fűt, plusz párátlanít és tisztít: egy készülék egész évre.",
        lv="Abi. Vasarā dzesē, ziemā silda un vēl sausina un attīra gaisu: viena ierīce visam gadam.",
    )),
    ("Come funziona il pagamento?", dict(cz="Jak funguje platba?", es="¿Cómo funciona el pago?", pt="Como funciona o pagamento?", sk="Ako funguje platba?", hu="Hogyan működik a fizetés?", lv="Kā darbojas maksājums?")),
    ("Paghi comodamente in contanti al corriere, solo quando ricevi il pacco a casa. Nessun pagamento anticipato, nessuna carta richiesta.", dict(
        cz="Zaplatíte v hotovosti kurýrovi, až balíček dorazí domů. Žádná platba předem, žádná karta.",
        es="Pagas en efectivo al mensajero cuando llega el paquete a casa. Sin pago anticipado, sin tarjeta.",
        pt="Paga em numerário ao estafeta quando a encomenda chega a casa. Sem pagamento antecipado, sem cartão.",
        sk="Zaplatíte v hotovosti kuriérovi, keď balík dorazí domov. Žiadna platba vopred, žiadna karta.",
        hu="Készpénzzel fizet a futárnak, amikor a csomag megérkezik. Nincs előleg, nincs kártya.",
        lv="Maksājat skaidrā naudā kurjeram, kad paciņa nonāk mājās. Bez avansa, bez kartes.",
    )),
    ("E se non mi convince?", dict(cz="A když mě to nepřesvědčí?", es="¿Y si no me convence?", pt="E se não me convencer?", sk="A keď ma to nepresvedčí?", hu="És ha nem győz meg?", lv="Un ja tas nepārliecina?")),
    ("Hai 60 giorni per restituirlo e ricevere il rimborso completo. Nessuna domanda, nessuna complicazione.", dict(
        cz="Máte 60 dní na vrácení a plnou náhradu. Bez otázek, bez komplikací.",
        es="Tienes 60 días para devolverlo y recibir el reembolso completo. Sin preguntas, sin complicaciones.",
        pt="Tem 60 dias para devolver e receber o reembolso completo. Sem perguntas, sem complicações.",
        sk="Máte 60 dní na vrátenie a plnú náhradu. Bez otázok, bez komplikácií.",
        hu="60 napja van a visszaküldésre és a teljes visszatérítésre. Kérdés nélkül, komplikáció nélkül.",
        lv="Jums ir 60 dienas, lai atdotu un saņemtu pilnu atmaksu. Bez jautājumiem, bez sarežģījumiem.",
    )),
    ("💶 Pagamento alla consegna", dict(cz="💶 Platba na dobírku", es="💶 Pago contra reembolso", pt="💶 Pagamento à cobrança", sk="💶 Platba na dobierku", hu="💶 Utánvét", lv="💶 Maksa pēc saņemšanas")),
    ("🚚 Spedizione 24/48 h", dict(cz="🚚 Doručení 24/48 h", es="🚚 Envío 24/48 h", pt="🚚 Envio 24/48 h", sk="🚚 Doručenie 24/48 h", hu="🚚 Szállítás 24/48 óra", lv="🚚 Piegāde 24/48 h")),
    ("↩️ Reso 60 giorni", dict(cz="↩️ Vrácení 60 dní", es="↩️ Devolución 60 días", pt="↩️ Devolução 60 dias", sk="↩️ Vrátenie 60 dní", hu="↩️ 60 napos visszaküldés", lv="↩️ Atgriešana 60 dienas")),
    ("Prodotti utili per la vita quotidiana, consegna in 24-48 ore con pagamento alla consegna.", dict(
        cz="Užitečné produkty pro každodenní život, doručení do 24–48 hodin s platbou na dobírku.",
        es="Productos útiles para el día a día, entrega en 24–48 horas con pago contra reembolso.",
        pt="Produtos úteis para o dia a dia, entrega em 24–48 horas com pagamento à cobrança.",
        sk="Užitočné produkty pre každodenný život, doručenie do 24–48 hodín s platbou na dobierku.",
        hu="Hasznos termékek a mindennapokra, 24–48 órás szállítás utánvéttel.",
        lv="Noderīgi produkti ikdienai, piegāde 24–48 stundās ar samaksu pēc saņemšanas.",
    )),
    ("Informazioni", dict(cz="Informace", es="Información", pt="Informação", sk="Informácie", hu="Információ", lv="Informācija")),
    ("Chi siamo", dict(cz="O nás", es="Sobre nosotros", pt="Sobre nós", sk="O nás", hu="Rólunk", lv="Par mums")),
    ("Contattaci", dict(cz="Kontaktujte nás", es="Contáctanos", pt="Contacte-nos", sk="Kontaktujte nás", hu="Kapcsolat", lv="Sazinieties")),
    ("Termini e Condizioni", dict(cz="Smluvní podmínky", es="Términos y condiciones", pt="Termos e Condições", sk="Zmluvné podmienky", hu="Általános szerződési feltételek", lv="Noteikumi un nosacījumi")),
    ("Cookie Policy", dict(cz="Zásady používání souborů cookie", es="Política de cookies", pt="Política de Cookies", sk="Zásady používania súborov cookie", hu="Cookie szabályzat", lv="Sīkdatņu politika")),
    ("Politica di spedizione", dict(cz="Zásady dopravy", es="Política de envío", pt="Política de envio", sk="Zásady dopravy", hu="Szállítási szabályzat", lv="Piegādes politika")),
    ("Politica di Spedizione", dict(cz="Zásady dopravy", es="Política de envío", pt="Política de envio", sk="Zásady dopravy", hu="Szállítási szabályzat", lv="Piegādes politika")),
    ("Politica di reso", dict(cz="Zásady vrácení peněz", es="Política de reembolso", pt="Política de reembolso", sk="Zásady vrátenia peňazí", hu="Visszatérítési szabályzat", lv="Atmaksas politika")),
    ("Politica di Rimborso", dict(cz="Zásady vrácení peněz", es="Política de reembolso", pt="Política de reembolso", sk="Zásady vrátenia peňazí", hu="Visszatérítési szabályzat", lv="Atmaksas politika")),
    ("Privacy Policy", dict(cz="Zásady ochrany osobních údajů", es="Política de privacidad", pt="Política de Privacidade", sk="Zásady ochrany osobných údajov", hu="Adatvédelmi szabályzat", lv="Privātuma politika")),
    ("Tutti i diritti riservati", dict(cz="Všechna práva vyhrazena", es="Todos los derechos reservados", pt="Todos os direitos reservados", sk="Všetky práva vyhradené", hu="Minden jog fenntartva", lv="Visas tiesības aizsargātas")),
    ("<td>Installazione</td>", dict(cz="<td>Instalace</td>", es="<td>Instalación</td>", pt="<td>Instalação</td>", sk="<td>Inštalácia</td>", hu="<td>Telepítés</td>", lv="<td>Uzstādīšana</td>")),
    ("<td>Tempi</td>", dict(cz="<td>Čas</td>", es="<td>Tiempos</td>", pt="<td>Tempos</td>", sk="<td>Čas</td>", hu="<td>Idő</td>", lv="<td>Laiks</td>")),
    ("<td>Funzioni</td>", dict(cz="<td>Funkce</td>", es="<td>Funciones</td>", pt="<td>Funções</td>", sk="<td>Funkcie</td>", hu="<td>Funkciók</td>", lv="<td>Funkcijas</td>")),
    ("Contatti", dict(cz="Kontakt", es="Contacto", pt="Contacto", sk="Kontaktovať", hu="Kapcsolat", lv="Kontakti")),
    # --- thank-you ---
    ("Ordine ricevuto — Attendi la chiamata di conferma | Clima PRO™", dict(
        cz="Objednávka přijata — Počkejte na potvrzovací hovor | Clima PRO™",
        es="Pedido recibido — Espera la llamada de confirmación | Clima PRO™",
        pt="Encomenda recebida — Aguarde a chamada de confirmação | Clima PRO™",
        sk="Objednávka prijatá — Počkajte na potvrdzovací hovor | Clima PRO™",
        hu="Rendelés rögzítve — Várja a visszaigazoló hívást | Clima PRO™",
        lv="Pasūtījums saņemts — Gaidiet apstiprinājuma zvanu | Clima PRO™",
    )),
    ("Il tuo ordine Clima PRO™ è stato registrato. Manca solo un ultimo passaggio: rispondi alla chiamata di conferma del nostro operatore.", dict(
        cz="Vaše objednávka Clima PRO™ byla zaznamenána. Zbývá poslední krok: přijměte potvrzovací hovor od našeho operátora.",
        es="Tu pedido Clima PRO™ ha sido registrado. Solo falta un último paso: responde a la llamada de confirmación de nuestro operador.",
        pt="A sua encomenda Clima PRO™ foi registada. Falta apenas um último passo: atenda a chamada de confirmação do nosso operador.",
        sk="Vaša objednávka Clima PRO™ bola zaznamenaná. Zostáva posledný krok: prijmite potvrdzovací hovor od nášho operátora.",
        hu="Clima PRO™ rendelése rögzítve. Már csak egy lépés van hátra: vegye fel a visszaigazoló hívást.",
        lv="Jūsu Clima PRO™ pasūtījums ir reģistrēts. Atlicis pēdējais solis: atbildiet uz mūsu operatora apstiprinājuma zvanu.",
    )),
    ("Il tuo ordine Clima PRO™ è stato registrato!", dict(
        cz="Vaše objednávka Clima PRO™ byla úspěšně zaznamenána!",
        es="¡Tu pedido Clima PRO™ se ha registrado correctamente!",
        pt="A sua encomenda Clima PRO™ foi registada com sucesso!",
        sk="Vaša objednávka Clima PRO™ bola úspešne zaznamenaná!",
        hu="Clima PRO™ rendelését sikeresen rögzítettük!",
        lv="Jūsu Clima PRO™ pasūtījums ir veiksmīgi reģistrēts!",
    )),
    ("Perfetto — il tuo ordine è in elaborazione. Manca solo <strong>un ultimo passaggio</strong> per completarlo e far partire la spedizione.", dict(
        cz="Skvělé — objednávka se zpracovává. Zbývá už jen <strong>poslední krok</strong> k dokončení a odeslání.",
        es="Perfecto — tu pedido está en proceso. Solo falta <strong>un último paso</strong> para completarlo y poner en marcha el envío.",
        pt="Perfeito — a encomenda está a ser processada. Falta só <strong>um último passo</strong> para a concluir e enviar.",
        sk="Skvelé — objednávka sa spracúva. Zostáva už len <strong>posledný krok</strong> na dokončenie a odoslanie.",
        hu="Rendben — a rendelés feldolgozás alatt. Már csak <strong>egy utolsó lépés</strong> van hátra a feladáshoz.",
        lv="Lieliski — pasūtījums tiek apstrādāts. Atlicis tikai <strong>pēdējais solis</strong>, lai to pabeigtu un nosūtītu.",
    )),
    ("Clima PRO™ 4in1 — climatizzatore a colonna", dict(
        cz="Clima PRO™ 4in1 — sloupová klimatizace", es="Clima PRO™ 4in1 — aire acondicionado de columna",
        pt="Clima PRO™ 4in1 — ar condicionado de coluna", sk="Clima PRO™ 4in1 — stĺpová klimatizácia",
        hu="Clima PRO™ 4in1 — oszlopklíma", lv="Clima PRO™ 4in1 — kolonnas gaisa kondicionieris",
    )),
    ("18.000 BTU · Pagamento alla consegna", dict(
        cz="18.000 BTU · Platba na dobírku", es="18.000 BTU · Pago contra reembolso", pt="18.000 BTU · Pagamento à cobrança",
        sk="18.000 BTU · Platba na dobierku", hu="18.000 BTU · Utánvét", lv="18.000 BTU · Maksa pēc saņemšanas",
    )),
    ("Clima PRO climatizzatore a colonna 4 in 1", dict(
        cz="Clima PRO sloupová klimatizace 4 v 1", es="Clima PRO aire acondicionado de columna 4 en 1",
        pt="Clima PRO ar condicionado de coluna 4 em 1", sk="Clima PRO stĺpová klimatizácia 4 v 1",
        hu="Clima PRO oszlopklíma 4 az 1-ben", lv="Clima PRO kolonnas gaisa kondicionieris 4 vienā",
    )),
    ("👇 Cosa devi fare adesso", dict(cz="👇 Co máte udělat teď", es="👇 Qué debes hacer ahora", pt="👇 O que deve fazer agora", sk="👇 Čo máte urobiť teraz", hu="👇 Mit kell tennie most", lv="👇 Kas jādara tagad")),
    ("📞 Rispondi alla chiamata di conferma", dict(
        cz="📞 Přijměte potvrzovací hovor", es="📞 Responde a la llamada de confirmación", pt="📞 Atenda a chamada de confirmação",
        sk="📞 Prijmite potvrdzovací hovor", hu="📞 Vegye fel a visszaigazoló hívást", lv="📞 Atbildiet uz apstiprinājuma zvanu",
    )),
    ("Un nostro operatore ti contatterà <strong>nelle prossime ore</strong> per confermare il tuo ordine Clima PRO™.", dict(
        cz="Náš operátor vás bude kontaktovat <strong>v příštích hodinách</strong>, aby potvrdil objednávku Clima PRO™.",
        es="Un operador te contactará <strong>en las próximas horas</strong> para confirmar tu pedido Clima PRO™.",
        pt="Um operador vai contactá-lo <strong>nas próximas horas</strong> para confirmar a encomenda Clima PRO™.",
        sk="Náš operátor vás bude kontaktovať <strong>v najbližších hodinách</strong>, aby potvrdil objednávku Clima PRO™.",
        hu="Operátorunk <strong>a következő órákban</strong> felhívja, hogy megerősítse a Clima PRO™ rendelést.",
        lv="Mūsu operators sazināsies <strong>nākamo stundu laikā</strong>, lai apstiprinātu jūsu Clima PRO™ pasūtījumu.",
    )),
    ("Se non rispondi alla chiamata, l'ordine verrà automaticamente annullato.", dict(
        cz="Pokud hovor nepřijmete, objednávka bude automaticky zrušena.",
        es="Si no respondes a la llamada, el pedido se cancelará automáticamente.",
        pt="Se não atender a chamada, a encomenda será cancelada automaticamente.",
        sk="Ak hovor neprijmete, objednávka bude automaticky zrušená.",
        hu="Ha nem veszi fel, a rendelés automatikusan törlődik.",
        lv="Ja nezvanīsiet, pasūtījums tiks automātiski atcelts.",
    )),
    ("🕒 Orari di contatto", dict(cz="🕒 Kontaktní hodiny", es="🕒 Horario de contacto", pt="🕒 Horário de contacto", sk="🕒 Kontaktné hodiny", hu="🕒 Elérhetőségi idő", lv="🕒 Saziņas laiks")),
    ("Lunedì – Sabato · 9:00 – 18:00", dict(
        cz="Pondělí – Sobota · 9:00 – 18:00", es="Lunes – Sábado · 9:00 – 18:00", pt="Segunda – Sábado · 9:00 – 18:00",
        sk="Pondelok – Sobota · 9:00 – 18:00", hu="Hétfő – Szombat · 9:00 – 18:00", lv="Pirmdiena – Sestdiena · 9:00 – 18:00",
    )),
    ("📋 Cosa succede dopo", dict(cz="📋 Co se stane dál", es="📋 Qué ocurre después", pt="📋 O que acontece a seguir", sk="📋 Čo sa stane ďalej", hu="📋 Mi történik ezután", lv="📋 Kas notiek tālāk")),
    ("Rispondi alla chiamata e <strong>conferma i tuoi dati</strong>", dict(
        cz="Přijměte hovor a <strong>potvrďte své údaje</strong>", es="Responde a la llamada y <strong>confirma tus datos</strong>",
        pt="Atenda a chamada e <strong>confirme os seus dados</strong>", sk="Prijmite hovor a <strong>potvrďte svoje údaje</strong>",
        hu="Vegye fel a hívást és <strong>erősítse meg az adatait</strong>", lv="Atbildiet uz zvanu un <strong>apstipriniet savus datus</strong>",
    )),
    ("Il tuo Clima PRO™ verrà spedito entro <strong>24–48 ore</strong>", dict(
        cz="Váš Clima PRO™ odešleme do <strong>24–48 hodin</strong>", es="Tu Clima PRO™ se enviará en <strong>24–48 horas</strong>",
        pt="O seu Clima PRO™ será enviado em <strong>24–48 horas</strong>", sk="Váš Clima PRO™ odošleme do <strong>24–48 hodín</strong>",
        hu="Clima PRO™ készülékét <strong>24–48 órán belül</strong> feladjuk", lv="Jūsu Clima PRO™ nosūtīsim <strong>24–48 stundu</strong> laikā",
    )),
    ("Consegna a domicilio e <strong>pagamento alla consegna</strong>", dict(
        cz="Doručení domů a <strong>platba na dobírku</strong>", es="Entrega a domicilio y <strong>pago contra reembolso</strong>",
        pt="Entrega ao domicílio e <strong>pagamento à cobrança</strong>", sk="Doručenie domov a <strong>platba na dobierku</strong>",
        hu="Házhozszállítás és <strong>utánvét</strong>", lv="Piegāde uz mājām un <strong>maksa pēc saņemšanas</strong>",
    )),
    ("🔒 Pagamento alla consegna", dict(cz="🔒 Platba na dobírku", es="🔒 Pago contra reembolso", pt="🔒 Pagamento à cobrança", sk="🔒 Platba na dobierku", hu="🔒 Utánvét", lv="🔒 Maksa pēc saņemšanas")),
    ("🛡️ Garanzia 2 anni", dict(cz="🛡️ Záruka 2 roky", es="🛡️ Garantía 2 años", pt="🛡️ Garantia 2 anos", sk="🛡️ Záruka 2 roky", hu="🛡️ 2 év garancia", lv="🛡️ 2 gadu garantija")),
]


def apply_pack(html: str, geo: str) -> str:
    missing = []
    for it, langs in sorted(PACK, key=lambda x: len(x[0]), reverse=True):
        if it not in html:
            missing.append(it[:70])
            continue
        html = html.replace(it, langs[geo])
    return html, missing


def patch_config(html: str, geo: str, g: dict) -> str:
    html = html.replace('lang="it"', f'lang="{g["lang"]}"')
    html = html.replace("https://gadgetspothub.com/clima-pro-it/", f"https://gadgetspothub.com/clima-pro-{geo}/")
    html = html.replace("https://gadgetspothub.com/clima-pro-it/thank-you.html", f"https://gadgetspothub.com/clima-pro-{geo}/thank-you.html")
    html = html.replace("GEO: 'it'", f"GEO: '{geo}'")
    html = html.replace("CURRENCY: 'EUR'", f"CURRENCY: '{g['currency']}'")
    html = html.replace("PRICE: 99", f"PRICE: {g['price_num']}")
    html = html.replace("OFFER_NAME: 'Clima PRO 1274'", f"OFFER_NAME: 'Clima PRO {g['offer']}'")
    html = html.replace("LP_ID: 'it-1274'", f"LP_ID: '{geo}-{g['offer']}'")
    html = html.replace(IT_UID, UID)
    html = html.replace('value="1274"', f'value="{g["offer"]}"')
    html = html.replace('value="1293"', f'value="{g["lp"]}"')
    html = html.replace(IT_WEBHOOK, WEBHOOK)
    html = html.replace(IT_KEY, g["key"])
    html = html.replace('href="/it/', f'href="/{geo}/')
    html = html.replace("200 €", g["was"])
    html = html.replace("99 €", g["now"])
    return html


def main() -> None:
    it_index = (ROOT / "clima-pro-it" / "index.html").read_text(encoding="utf-8")
    it_ty = (ROOT / "clima-pro-it" / "thank-you.html").read_text(encoding="utf-8")
    for geo, g in GEOS.items():
        dest = ROOT / f"clima-pro-{geo}"
        dest.mkdir(parents=True, exist_ok=True)
        landing, miss_l = apply_pack(it_index, geo)
        landing = patch_config(landing, geo, g)
        ty, miss_t = apply_pack(it_ty, geo)
        ty = patch_config(ty, geo, g)
        (dest / "index.html").write_text(landing, encoding="utf-8")
        (dest / "thank-you.html").write_text(ty, encoding="utf-8")
        unused = [m for m in miss_l if m in it_index]
        print(f"wrote clima-pro-{geo}/  {g['now']}  unused_on_landing={len(miss_l)} unused_on_ty={len(miss_t)}")


if __name__ == "__main__":
    main()
