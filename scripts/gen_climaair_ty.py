#!/usr/bin/env python3
"""Generate ClimaAir-branded thank-you pages for IT + CZ ES PT SK HU LV."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

GEOS = {
    "it": {"lang": "it", "price_num": 99, "currency": "EUR", "now": "99 €", "offer": "1274"},
    "cz": {"lang": "cs", "price_num": 1799, "currency": "CZK", "now": "1 799 Kč", "offer": "3296"},
    "es": {"lang": "es", "price_num": 79, "currency": "EUR", "now": "79,00€", "offer": "3345"},
    "pt": {"lang": "pt", "price_num": 89, "currency": "EUR", "now": "89,00€", "offer": "3344"},
    "sk": {"lang": "sk", "price_num": 69, "currency": "EUR", "now": "69,00€", "offer": "4242"},
    "hu": {"lang": "hu", "price_num": 39900, "currency": "HUF", "now": "39 900 Ft", "offer": "3295"},
    "lv": {"lang": "lv", "price_num": 89, "currency": "EUR", "now": "89,00€", "offer": "4243"},
}

TY = {
    "it": dict(
        title="Ordine ricevuto — Attendi la chiamata di conferma | ClimaAir™",
        description="Il tuo ordine ClimaAir™ è stato registrato. Manca solo un ultimo passaggio: rispondi alla chiamata di conferma del nostro operatore.",
        cookie_text="Usiamo cookie tecnici e di terze parti per migliorare la tua esperienza e per analisi.",
        cookie_accept="Accetta", cookie_learn="Scopri di più",
        headline="Il tuo ordine ClimaAir™ è stato registrato!",
        subhead="Perfetto — il tuo ordine è in elaborazione. Manca solo <strong>un ultimo passaggio</strong> per completarlo e far partire la spedizione.",
        product="ClimaAir™ 4in1 — climatizzatore a colonna",
        product_meta="18.000 BTU · Pagamento alla consegna",
        action_ey="👇 Cosa devi fare adesso",
        action_h="📞 Rispondi alla chiamata di conferma",
        action_p="Un nostro operatore ti contatterà <strong>nelle prossime ore</strong> per confermare il tuo ordine ClimaAir™.",
        action_w="Se non rispondi alla chiamata, l'ordine verrà automaticamente annullato.",
        hours_h="🕒 Orari di contatto",
        hours="Lunedì – Sabato · 9:00 – 18:00",
        next_h="📋 Cosa succede dopo",
        s1="Rispondi alla chiamata e <strong>conferma i tuoi dati</strong>",
        s2="Il tuo ClimaAir™ verrà spedito entro <strong>24–48 ore</strong>",
        s3="Consegna a domicilio e <strong>pagamento alla consegna</strong>",
        b1="🔒 Pagamento alla consegna", b2="🛡️ Garanzia 2 anni", b3="↩️ Reso 60 giorni",
        img_alt="ClimaAir climatizzatore a colonna 4 in 1",
        foot_info="Informazioni", foot_contact="Contatti",
        about="Chi siamo", contact="Contattaci",
        privacy="Privacy Policy", terms="Termini e Condizioni",
        cookies="Cookie Policy", ship="Politica di Spedizione", refund="Politica di Rimborso",
        rights="Tutti i diritti riservati",
    ),
    "cz": dict(
        title="Objednávka přijata — Počkejte na potvrzovací hovor | ClimaAir™",
        description="Vaše objednávka ClimaAir™ byla zaznamenána. Zbývá poslední krok: přijměte potvrzovací hovor od našeho operátora.",
        cookie_text="Používáme technické a cookies třetích stran ke zlepšení vašeho zážitku a pro analytiku.",
        cookie_accept="Přijmout", cookie_learn="Zjistit více",
        headline="Vaše objednávka ClimaAir™ byla úspěšně zaznamenána!",
        subhead="Skvělé — objednávka se zpracovává. Zbývá už jen <strong>poslední krok</strong> k dokončení a odeslání.",
        product="ClimaAir™ 4in1 — sloupová klimatizace",
        product_meta="18.000 BTU · Platba na dobírku",
        action_ey="👇 Co máte udělat teď",
        action_h="📞 Přijměte potvrzovací hovor",
        action_p="Náš operátor vás bude kontaktovat <strong>v příštích hodinách</strong>, aby potvrdil objednávku ClimaAir™.",
        action_w="Pokud hovor nepřijmete, objednávka bude automaticky zrušena.",
        hours_h="🕒 Kontaktní hodiny",
        hours="Pondělí – Sobota · 9:00 – 18:00",
        next_h="📋 Co se stane dál",
        s1="Přijměte hovor a <strong>potvrďte své údaje</strong>",
        s2="Váš ClimaAir™ odešleme do <strong>24–48 hodin</strong>",
        s3="Doručení domů a <strong>platba na dobírku</strong>",
        b1="🔒 Platba na dobírku", b2="🛡️ Záruka 2 roky", b3="↩️ Vrácení 60 dní",
        img_alt="ClimaAir přenosná sloupová klimatizace 4 v 1",
        foot_info="Informace", foot_contact="Kontakt",
        about="O nás", contact="Kontaktujte nás",
        privacy="Zásady ochrany osobních údajů", terms="Smluvní podmínky",
        cookies="Zásady používání souborů cookie", ship="Zásady dopravy", refund="Zásady vrácení peněz",
        rights="Všechna práva vyhrazena",
    ),
    "es": dict(
        title="Pedido recibido — Espera la llamada de confirmación | ClimaAir™",
        description="Tu pedido ClimaAir™ ha sido registrado. Solo falta un último paso: responde a la llamada de confirmación de nuestro operador.",
        cookie_text="Usamos cookies técnicas y de terceros para mejorar tu experiencia y para análisis.",
        cookie_accept="Aceptar", cookie_learn="Más información",
        headline="¡Tu pedido ClimaAir™ se ha registrado correctamente!",
        subhead="Perfecto — tu pedido está en proceso. Solo falta <strong>un último paso</strong> para completarlo y poner en marcha el envío.",
        product="ClimaAir™ 4in1 — aire acondicionado de columna",
        product_meta="18.000 BTU · Pago contra reembolso",
        action_ey="👇 Qué debes hacer ahora",
        action_h="📞 Responde a la llamada de confirmación",
        action_p="Un operador te contactará <strong>en las próximas horas</strong> para confirmar tu pedido ClimaAir™.",
        action_w="Si no respondes a la llamada, el pedido se cancelará automáticamente.",
        hours_h="🕒 Horario de contacto",
        hours="Lunes – Sábado · 9:00 – 18:00",
        next_h="📋 Qué ocurre después",
        s1="Responde a la llamada y <strong>confirma tus datos</strong>",
        s2="Tu ClimaAir™ se enviará en <strong>24–48 horas</strong>",
        s3="Entrega a domicilio y <strong>pago contra reembolso</strong>",
        b1="🔒 Pago contra reembolso", b2="🛡️ Garantía 2 años", b3="↩️ Devolución 60 días",
        img_alt="ClimaAir climatizador de columna portátil 4 en 1",
        foot_info="Información", foot_contact="Contacto",
        about="Sobre nosotros", contact="Contáctanos",
        privacy="Política de privacidad", terms="Términos y condiciones",
        cookies="Política de cookies", ship="Política de envío", refund="Política de reembolso",
        rights="Todos los derechos reservados",
    ),
    "pt": dict(
        title="Encomenda recebida — Aguarde a chamada de confirmação | ClimaAir™",
        description="A sua encomenda ClimaAir™ foi registada. Falta apenas um último passo: atenda a chamada de confirmação do nosso operador.",
        cookie_text="Usamos cookies técnicos e de terceiros para melhorar a sua experiência e para análises.",
        cookie_accept="Aceitar", cookie_learn="Saber mais",
        headline="A sua encomenda ClimaAir™ foi registada com sucesso!",
        subhead="Perfeito — a encomenda está a ser processada. Falta só <strong>um último passo</strong> para a concluir e enviar.",
        product="ClimaAir™ 4in1 — ar condicionado de coluna",
        product_meta="18.000 BTU · Pagamento à cobrança",
        action_ey="👇 O que deve fazer agora",
        action_h="📞 Atenda a chamada de confirmação",
        action_p="Um operador vai contactá-lo <strong>nas próximas horas</strong> para confirmar a encomenda ClimaAir™.",
        action_w="Se não atender a chamada, a encomenda será cancelada automaticamente.",
        hours_h="🕒 Horário de contacto",
        hours="Segunda – Sábado · 9:00 – 18:00",
        next_h="📋 O que acontece a seguir",
        s1="Atenda a chamada e <strong>confirme os seus dados</strong>",
        s2="O seu ClimaAir™ será enviado em <strong>24–48 horas</strong>",
        s3="Entrega ao domicílio e <strong>pagamento à cobrança</strong>",
        b1="🔒 Pagamento à cobrança", b2="🛡️ Garantia 2 anos", b3="↩️ Devolução 60 dias",
        img_alt="ClimaAir climatizador de coluna portátil 4 em 1",
        foot_info="Informação", foot_contact="Contacto",
        about="Sobre nós", contact="Contacte-nos",
        privacy="Política de Privacidade", terms="Termos e Condições",
        cookies="Política de Cookies", ship="Política de envio", refund="Política de reembolso",
        rights="Todos os direitos reservados",
    ),
    "sk": dict(
        title="Objednávka prijatá — Počkajte na potvrdzovací hovor | ClimaAir™",
        description="Vaša objednávka ClimaAir™ bola zaznamenaná. Zostáva posledný krok: prijmite potvrdzovací hovor od nášho operátora.",
        cookie_text="Používame technické a cookies tretích strán na zlepšenie vášho zážitku a na analytiku.",
        cookie_accept="Prijať", cookie_learn="Zistiť viac",
        headline="Vaša objednávka ClimaAir™ bola úspešne zaznamenaná!",
        subhead="Skvelé — objednávka sa spracúva. Zostáva už len <strong>posledný krok</strong> na dokončenie a odoslanie.",
        product="ClimaAir™ 4in1 — stĺpová klimatizácia",
        product_meta="18.000 BTU · Platba na dobierku",
        action_ey="👇 Čo máte urobiť teraz",
        action_h="📞 Prijmite potvrdzovací hovor",
        action_p="Náš operátor vás bude kontaktovať <strong>v najbližších hodinách</strong>, aby potvrdil objednávku ClimaAir™.",
        action_w="Ak hovor neprijmete, objednávka bude automaticky zrušená.",
        hours_h="🕒 Kontaktné hodiny",
        hours="Pondelok – Sobota · 9:00 – 18:00",
        next_h="📋 Čo sa stane ďalej",
        s1="Prijmite hovor a <strong>potvrďte svoje údaje</strong>",
        s2="Váš ClimaAir™ odošleme do <strong>24–48 hodín</strong>",
        s3="Doručenie domov a <strong>platba na dobierku</strong>",
        b1="🔒 Platba na dobierku", b2="🛡️ Záruka 2 roky", b3="↩️ Vrátenie 60 dní",
        img_alt="ClimaAir prenosná stĺpová klimatizácia 4 v 1",
        foot_info="Informácie", foot_contact="Kontaktovať",
        about="O nás", contact="Kontaktujte nás",
        privacy="Zásady ochrany osobných údajov", terms="Zmluvné podmienky",
        cookies="Zásady používania súborov cookie", ship="Pravidlá prepravy", refund="Pravidlá vrátenia peňazí",
        rights="Všetky práva vyhradené",
    ),
    "hu": dict(
        title="Rendelés rögzítve — Várja a visszaigazoló hívást | ClimaAir™",
        description="ClimaAir™ rendelése rögzítve. Már csak egy lépés van hátra: vegye fel a visszaigazoló hívást.",
        cookie_text="Technikai és harmadik féltől származó cookie-kat használunk a élmény javítására és elemzésre.",
        cookie_accept="Elfogadom", cookie_learn="Tudjon meg többet",
        headline="ClimaAir™ rendelését sikeresen rögzítettük!",
        subhead="Tökéletes — a rendelés feldolgozás alatt. Már csak <strong>egy utolsó lépés</strong> kell a teljesítéshez és a szállítás indításához.",
        product="ClimaAir™ 4in1 — oszlopklíma",
        product_meta="18.000 BTU · Utánvét",
        action_ey="👇 Mit kell tennie most",
        action_h="📞 Vegye fel a visszaigazoló hívást",
        action_p="Operátorunk <strong>a következő órákban</strong> felhívja, hogy megerősítse a ClimaAir™ rendelést.",
        action_w="Ha nem veszi fel a hívást, a rendelés automatikusan törlődik.",
        hours_h="🕒 Elérhetőség",
        hours="Hétfő – Szombat · 9:00 – 18:00",
        next_h="📋 Mi történik ezután",
        s1="Vegye fel a hívást és <strong>erősítse meg az adatait</strong>",
        s2="ClimaAir™ készülékét <strong>24–48 órán belül</strong> feladjuk",
        s3="Házhozszállítás és <strong>utánvét</strong>",
        b1="🔒 Utánvét", b2="🛡️ 2 év garancia", b3="↩️ 60 napos visszaküldés",
        img_alt="ClimaAir hordozható oszlopklíma 4 az 1-ben",
        foot_info="Információ", foot_contact="Elérhetőségek",
        about="Rólunk", contact="Kapcsolat",
        privacy="Adatvédelmi irányelvek", terms="Általános szerződési feltételek",
        cookies="Cookie szabályzat", ship="Szállítási feltételek", refund="Visszatérítési szabályzat",
        rights="Minden jog fenntartva",
    ),
    "lv": dict(
        title="Pasūtījums saņemts — Gaidiet apstiprinājuma zvanu | ClimaAir™",
        description="Jūsu ClimaAir™ pasūtījums ir reģistrēts. Atlicis pēdējais solis: atbildiet uz mūsu operatora apstiprinājuma zvanu.",
        cookie_text="Mēs izmantojam tehniskās un trešo pušu sīkdatnes, lai uzlabotu jūsu pieredzi un analītikai.",
        cookie_accept="Pieņemt", cookie_learn="Uzzināt vairāk",
        headline="Jūsu ClimaAir™ pasūtījums ir veiksmīgi reģistrēts!",
        subhead="Lieliski — pasūtījums tiek apstrādāts. Atlicis tikai <strong>pēdējais solis</strong>, lai to pabeigtu un nosūtītu.",
        product="ClimaAir™ 4in1 — kolonnas gaisa kondicionieris",
        product_meta="18.000 BTU · Maksa pēc saņemšanas",
        action_ey="👇 Kas jādara tagad",
        action_h="📞 Atbildiet uz apstiprinājuma zvanu",
        action_p="Mūsu operators sazināsies <strong>nākamo stundu laikā</strong>, lai apstiprinātu jūsu ClimaAir™ pasūtījumu.",
        action_w="Ja nezvanīsiet pretī, pasūtījums tiks automātiski atcelts.",
        hours_h="🕒 Saziņas laiks",
        hours="Pirmdiena – Sestdiena · 9:00 – 18:00",
        next_h="📋 Kas notiek tālāk",
        s1="Atbildiet uz zvanu un <strong>apstipriniet savus datus</strong>",
        s2="Jūsu ClimaAir™ nosūtīsim <strong>24–48 stundu</strong> laikā",
        s3="Piegāde uz mājām un <strong>maksa pēc saņemšanas</strong>",
        b1="🔒 Maksa pēc saņemšanas", b2="🛡️ 2 gadu garantija", b3="↩️ Atgriešana 60 dienas",
        img_alt="ClimaAir pārnēsājams kolonnas klimatizators 4 vienā",
        foot_info="Informācija", foot_contact="Kontakti",
        about="Par mums", contact="Sazinieties ar mums",
        privacy="Privātuma politika", terms="Noteikumi un nosacījumi",
        cookies="Sīkdatņu politika", ship="Piegādes politika", refund="Atmaksas politika",
        rights="Visas tiesības aizsargātas",
    ),
}

TMPL = r"""<!DOCTYPE html>
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
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{description}">
<meta name="contact" content="info@gadgetspothub.com">
<meta name="theme-color" content="#0055ff">
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
  GEO: '{geo}',
  PRODUCT_SLUG: 'climaair',
  CURRENCY: '{currency}',
  PRICE: {price_num},
  META_PIXEL_ID: '',
  GOOGLE_TAG_ID: '',
  GOOGLE_ADS_CONVERSION_ID: '',
  TY_CONVERSION_LABEL: '',
  COOKIE_TEXT: '{cookie_text}',
  COOKIE_ACCEPT: '{cookie_accept}',
  COOKIE_LEARN: '{cookie_learn}'
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
  <h1 class="ty-headline">{headline}</h1>
  <p class="ty-subhead">{subhead}</p>

  <div class="ty-product">
    <img src="/assets/img/products/climaair/hero.webp" alt="{img_alt}" width="88" height="88">
    <div>
      <div class="ty-product__name">{product}</div>
      <div class="ty-product__meta">{product_meta}</div>
      <div class="ty-product__price">{now}</div>
    </div>
  </div>

  <section class="ty-action">
    <div class="ty-action__eyebrow">{action_ey}</div>
    <h2 class="ty-action__title">{action_h}</h2>
    <p class="ty-action__body">{action_p}</p>
    <p class="ty-action__warning">{action_w}</p>
  </section>

  <section class="ty-box">
    <div class="ty-box__header">{hours_h}</div>
    <div class="ty-box__body"><div class="ty-hours-line"><strong>{hours}</strong></div></div>
  </section>

  <section class="ty-box">
    <div class="ty-box__header">{next_h}</div>
    <div class="ty-box__body">
      <ol class="ty-steps-list">
        <li>{s1}</li>
        <li>{s2}</li>
        <li>{s3}</li>
      </ol>
    </div>
  </section>

  <div class="ty-trust">
    <span class="ty-trust__badge">{b1}</span>
    <span class="ty-trust__badge">{b2}</span>
    <span class="ty-trust__badge">{b3}</span>
  </div>
</main>

<footer class="site-footer"><div class="container">
  <div class="site-footer__grid">
    <div>
      <a href="/" class="site-logo">
        <span class="site-logo__text" style="display:inline"><span class="site-logo__text-primary">gadgetspothub</span><span class="site-logo__text-accent">.com</span></span>
      </a>
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
        <li>County of Sussex 16192 Coastal Hwy, Lewes, DE 19958-3608, United States</li>
        <li><a href="mailto:info@gadgetspothub.com">info@gadgetspothub.com</a></li>
      </ul>
    </div>
  </div>
  <div class="site-footer__bottom">© <span data-year>2026</span> <strong>Netmart LLC</strong> — {rights}. <a href="/">gadgetspothub.com</a></div>
</div></footer>

{conversion}

<script>
  document.querySelectorAll('[data-year]').forEach(function (el) {{
    el.textContent = String(new Date().getFullYear());
  }});
</script>
</body>
</html>
"""

CONVERSION_FALLBACK = """<!-- Event snippet for Purchase conversion page -->
<script>
  gtag('event', 'conversion', {
      'send_to': 'AW-18358316754/8U5lCMOvn90cENLd9rFE',
      'transaction_id': ''
      // 'new_customer': true /* calculate dynamically, populate with true/false */,
  });
</script>
"""


def existing_conversion(geo: str) -> str:
    path = ROOT / geo / "climaair" / "thank-you.html"
    if not path.exists():
        return CONVERSION_FALLBACK
    text = path.read_text(encoding="utf-8")
    m = re.search(r"(<!-- Event snippet for Purchase conversion page -->[\s\S]+?</script>)", text)
    return m.group(1) if m else CONVERSION_FALLBACK


def js_str(s: str) -> str:
    return s.replace("\\", "\\\\").replace("'", "\\'")


def main() -> None:
    for geo, g in GEOS.items():
        dest = ROOT / geo / "climaair"
        dest.mkdir(parents=True, exist_ok=True)
        ty = {**TY[geo]}
        ty["cookie_text"] = js_str(ty["cookie_text"])
        ty["cookie_accept"] = js_str(ty["cookie_accept"])
        ty["cookie_learn"] = js_str(ty["cookie_learn"])
        conversion = existing_conversion(geo)
        payload = {**ty, **g, "geo": geo, "conversion": "__CONVERSION__"}
        html = TMPL.format_map(payload).replace("__CONVERSION__", conversion)
        (dest / "thank-you.html").write_text(html, encoding="utf-8")
        print(f"wrote {geo}/climaair/thank-you.html  {g['now']}")


if __name__ == "__main__":
    main()
