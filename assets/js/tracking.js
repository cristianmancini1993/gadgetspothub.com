// ============================================================
// TRACKING PIXELS — Centralizes Meta Pixel + Google Tag events
// ============================================================
// Configure IDs in window.SITE_CONFIG (set in <head> of every page).

(function () {
  const C = window.SITE_CONFIG || {};
  const CLICK_ID_KEYS = ['gclid', 'gbraid', 'wbraid'];
  const DEFAULT_GOOGLE_ADS_SEND_TO = 'AW-18358316754/8U5lCMOvn90cENLd9rFE';
  const CASHBOLT_SUBMIT_SESSION_KEY = 'df_cashbolt_submit';

  function getURLParam(name) {
    const params = new URLSearchParams(window.location.search);
    return params.get(name) || '';
  }

  function getStoredParam(name) {
    try {
      return window.localStorage.getItem('df_' + name) || '';
    } catch (e) {
      return '';
    }
  }

  function setStoredParam(name, value) {
    if (!value) return;
    try {
      window.localStorage.setItem('df_' + name, value);
    } catch (e) {
      // Storage may be blocked; URL parameters still cover the active session.
    }
  }

  function captureClickIds() {
    CLICK_ID_KEYS.forEach(function (key) {
      const value = getURLParam(key);
      if (value) setStoredParam(key, value);
    });
  }

  function getTrackingContext() {
    captureClickIds();

    const utmCampaign = getURLParam('utm_campaign') || getURLParam('campaignid') || getURLParam('campaign_id');
    const urlSubid = getURLParam('subid');
    const context = {
      campaign_id: utmCampaign || urlSubid || getStoredParam('campaign_id'),
      subid: urlSubid || getStoredParam('subid'),
      gclid: getURLParam('gclid') || getStoredParam('gclid'),
      gbraid: getURLParam('gbraid') || getStoredParam('gbraid'),
      wbraid: getURLParam('wbraid') || getStoredParam('wbraid'),
      utm_source: getURLParam('utm_source') || getStoredParam('utm_source'),
      utm_medium: getURLParam('utm_medium') || getStoredParam('utm_medium'),
      utm_campaign: utmCampaign || getStoredParam('utm_campaign'),
      utm_term: getURLParam('utm_term') || getStoredParam('utm_term'),
      utm_content: getURLParam('utm_content') || getStoredParam('utm_content'),
    };

    Object.keys(context).forEach(function (key) {
      if (context[key]) setStoredParam(key, context[key]);
    });

    return context;
  }

  function hasCashboltSubmitCookie() {
    return document.cookie.split(';').some(function (part) {
      return part.trim() === 'df_cashbolt_submit=1';
    });
  }

  function setCashboltSubmitCookie() {
    document.cookie = 'df_cashbolt_submit=1;path=/;max-age=7200;SameSite=Lax';
  }

  function clearCashboltSubmitCookie() {
    document.cookie = 'df_cashbolt_submit=;path=/;max-age=0;SameSite=Lax';
  }

  function markCashboltFormSubmitted() {
    try {
      sessionStorage.setItem(CASHBOLT_SUBMIT_SESSION_KEY, '1');
    } catch (e) {
      // ignore
    }
    setStoredParam('cashbolt_submit', '1');
    setCashboltSubmitCookie();
  }

  function shouldFireThankYouConversion() {
    try {
      if (sessionStorage.getItem(CASHBOLT_SUBMIT_SESSION_KEY) === '1') return true;
    } catch (e) {
      // ignore
    }
    if (getStoredParam('cashbolt_submit') === '1') return true;
    if (hasCashboltSubmitCookie()) return true;

    const p = new URLSearchParams(window.location.search);
    if (p.get('order_id') || p.get('transaction_id') || p.get('tid')) return true;

    return false;
  }

  function clearCashboltSubmitMarkers() {
    try {
      sessionStorage.removeItem(CASHBOLT_SUBMIT_SESSION_KEY);
    } catch (e) {
      // ignore
    }
    try {
      localStorage.removeItem('df_cashbolt_submit');
    } catch (e) {
      // ignore
    }
    clearCashboltSubmitCookie();
  }

  function isCashboltOrderForm(form) {
    const action = form.action || '';
    return form.classList.contains('tm-order-form')
      || action.indexOf('supertrendaffiliateprogram.com') !== -1
      || action.indexOf('unbreakable-offers.com') !== -1;
  }

  function bindCashboltSubmitTracking(form) {
    if (form.dataset.dfCashboltSubmitBound === '1') return;
    form.dataset.dfCashboltSubmitBound = '1';

    form.addEventListener('submit', function () {
      markCashboltFormSubmitted();
    }, true);

    form.addEventListener('click', function (event) {
      const target = event.target;
      if (!target || target.type !== 'submit') return;
      if (!form.checkValidity()) return;
      markCashboltFormSubmitted();
    }, true);
  }

  function setHiddenField(form, name, value) {
    if (!value) return;
    let input = form.querySelector('input[name="' + name + '"]');
    if (!input) {
      input = document.createElement('input');
      input.type = 'hidden';
      input.name = name;
      form.appendChild(input);
    }
    input.value = value;
  }

  function appendTrackingParams(url, context) {
    if (!url) return url;
    try {
      const out = new URL(url, window.location.origin);
      if (context.campaign_id) out.searchParams.set('campaign_id', context.campaign_id);
      if (context.subid) out.searchParams.set('subid', context.subid);
      if (context.gclid) out.searchParams.set('gclid', context.gclid);
      if (context.gbraid) out.searchParams.set('gbraid', context.gbraid);
      if (context.wbraid) out.searchParams.set('wbraid', context.wbraid);
      if (context.utm_campaign) out.searchParams.set('utm_campaign', context.utm_campaign);
      if (context.utm_source) out.searchParams.set('utm_source', context.utm_source);
      if (context.utm_medium) out.searchParams.set('utm_medium', context.utm_medium);
      if (context.utm_term) out.searchParams.set('utm_term', context.utm_term);
      if (context.utm_content) out.searchParams.set('utm_content', context.utm_content);
      return out.toString();
    } catch (e) {
      return url;
    }
  }

  function wireCashboltForms(context) {
    document.querySelectorAll('form').forEach(function (form) {
      setHiddenField(form, 'subid', context.subid || context.campaign_id);
      setHiddenField(form, 'sub_id', context.subid || context.campaign_id);
      setHiddenField(form, 'campaign_id', context.campaign_id);
      setHiddenField(form, 'gclid', context.gclid);
      setHiddenField(form, 'gbraid', context.gbraid);
      setHiddenField(form, 'wbraid', context.wbraid);
      setHiddenField(form, 'utm_campaign', context.utm_campaign || context.campaign_id);
      setHiddenField(form, 'utm_source', context.utm_source);
      setHiddenField(form, 'utm_medium', context.utm_medium);
      setHiddenField(form, 'utm_term', context.utm_term);
      setHiddenField(form, 'utm_content', context.utm_content);

      const thankYouInput = form.querySelector('input[name="thankyoupage"]');
      if (thankYouInput) {
        thankYouInput.value = appendTrackingParams(thankYouInput.value, context);
      }

      if (isCashboltOrderForm(form)) {
        bindCashboltSubmitTracking(form);
      }
    });
  }

  window.getLifepickshopTrackingContext = getTrackingContext;
  window.appendLifepickshopTrackingParams = appendTrackingParams;
  window.markLifepickshopCashboltSubmit = markCashboltFormSubmitted;
  // Legacy aliases
  window.getDevicegroveTrackingContext = getTrackingContext;
  window.appendDevicegroveTrackingParams = appendTrackingParams;
  window.markDevicegroveCashboltSubmit = markCashboltFormSubmitted;

  window.fireLifepickshopThankYouConversion = function (options) {
    options = options || {};
    const cfg = window.SITE_CONFIG || {};

    if (!shouldFireThankYouConversion()) {
      if (cfg.DEBUG_TRACKING) {
        console.log('[tracking] Thank-you conversion skipped (no Cashbolt submit proof).');
      }
      return false;
    }

    if (!window.gtag) return false;

    const T = getTrackingContext();
    const p = new URLSearchParams(window.location.search);
    const transactionId = p.get('order_id') || p.get('transaction_id') || p.get('tid')
      || T.subid || T.campaign_id || ('df_' + Date.now());
    const dedupeKey = 'df_gads_conv_' + transactionId;

    try {
      if (localStorage.getItem(dedupeKey) === '1') return false;
      localStorage.setItem(dedupeKey, '1');
    } catch (e) {
      // ignore
    }

    const sendTo = options.send_to || cfg.GOOGLE_ADS_CONVERSION_SEND_TO || DEFAULT_GOOGLE_ADS_SEND_TO;
    const payload = {
      send_to: sendTo,
      value: options.value != null ? options.value : (cfg.CONVERSION_VALUE != null ? cfg.CONVERSION_VALUE : 1.0),
      currency: options.currency || cfg.CONVERSION_CURRENCY || cfg.CURRENCY || 'EUR',
      transaction_id: transactionId,
      campaign_id: T.campaign_id || '',
      subid: T.subid || T.campaign_id || '',
      utm_campaign: p.get('utm_campaign') || T.utm_campaign || T.campaign_id || '',
      utm_source: p.get('utm_source') || T.utm_source || '',
      utm_medium: p.get('utm_medium') || T.utm_medium || '',
      utm_term: p.get('utm_term') || T.utm_term || '',
      utm_content: p.get('utm_content') || T.utm_content || '',
    };

    if (T.gclid) payload.gclid = T.gclid;
    if (T.gbraid) payload.gbraid = T.gbraid;
    if (T.wbraid) payload.wbraid = T.wbraid;

    window.gtag('event', 'conversion', payload);
    clearCashboltSubmitMarkers();
    return true;
  };
  window.fireDevicegroveThankYouConversion = window.fireLifepickshopThankYouConversion;

  captureClickIds();

  // ---- META PIXEL bootstrap ----
  if (C.META_PIXEL_ID) {
    !(function (f, b, e, v, n, t, s) {
      if (f.fbq) return;
      n = f.fbq = function () {
        n.callMethod ? n.callMethod.apply(n, arguments) : n.queue.push(arguments);
      };
      if (!f._fbq) f._fbq = n;
      n.push = n; n.loaded = !0; n.version = '2.0'; n.queue = [];
      t = b.createElement(e); t.async = !0; t.src = v;
      s = b.getElementsByTagName(e)[0]; s.parentNode.insertBefore(t, s);
    })(window, document, 'script', 'https://connect.facebook.net/en_US/fbevents.js');
    window.fbq('init', C.META_PIXEL_ID);
    window.fbq('track', 'PageView');
  }

  // ---- GOOGLE TAG bootstrap ----
  if (C.GOOGLE_TAG_ID) {
    const s = document.createElement('script');
    s.async = true;
    s.src = 'https://www.googletagmanager.com/gtag/js?id=' + C.GOOGLE_TAG_ID;
    document.head.appendChild(s);
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { window.dataLayer.push(arguments); };
    window.gtag('js', new Date());
    window.gtag('config', C.GOOGLE_TAG_ID);
  }

  // ---- NETWORK PIXEL (Adrice / ClickFlare / Voluum) ----
  if (C.NETWORK_PIXEL_URL) {
    const pixelContext = getTrackingContext();
    const img = new Image();
    img.src = appendTrackingParams(C.NETWORK_PIXEL_URL, {
      subid: pixelContext.subid || pixelContext.campaign_id,
      gclid: pixelContext.gclid,
    });
  }

  function privacyCopy(geo) {
    const g = geo || 'en';
    const privacy = '/' + g + '/privacy-policy.html';
    const terms = '/' + g + '/terms-conditions.html';
    const map = {
      it: 'Ho letto e accetto la <a href="' + privacy + '" target="_blank" rel="noopener">Privacy Policy</a> e i <a href="' + terms + '" target="_blank" rel="noopener">Termini</a>.',
      es: 'He leído y acepto la <a href="' + privacy + '" target="_blank" rel="noopener">Política de privacidad</a> y los <a href="' + terms + '" target="_blank" rel="noopener">Términos</a>.',
      pt: 'Li e aceito a <a href="' + privacy + '" target="_blank" rel="noopener">Política de Privacidade</a> e os <a href="' + terms + '" target="_blank" rel="noopener">Termos</a>.',
      fr: 'J’ai lu et j’accepte la <a href="' + privacy + '" target="_blank" rel="noopener">politique de confidentialité</a> et les <a href="' + terms + '" target="_blank" rel="noopener">conditions</a>.',
      de: 'Ich habe die <a href="' + privacy + '" target="_blank" rel="noopener">Datenschutzerklärung</a> und die <a href="' + terms + '" target="_blank" rel="noopener">AGB</a> gelesen und akzeptiere sie.',
      pl: 'Przeczytałem/am i akceptuję <a href="' + privacy + '" target="_blank" rel="noopener">Politykę prywatności</a> oraz <a href="' + terms + '" target="_blank" rel="noopener">Regulamin</a>.',
      cs: 'Přečetl/a jsem si a souhlasím se <a href="' + privacy + '" target="_blank" rel="noopener">zásadami ochrany osobních údajů</a> a <a href="' + terms + '" target="_blank" rel="noopener">podmínkami</a>.',
      sk: 'Prečítal/a som si a súhlasím so <a href="' + privacy + '" target="_blank" rel="noopener">zásadami ochrany osobných údajov</a> a <a href="' + terms + '" target="_blank" rel="noopener">podmienkami</a>.',
      hu: 'Elolvastam és elfogadom az <a href="' + privacy + '" target="_blank" rel="noopener">Adatvédelmi tájékoztatót</a> és a <a href="' + terms + '" target="_blank" rel="noopener">Feltételeket</a>.',
      ro: 'Am citit și accept <a href="' + privacy + '" target="_blank" rel="noopener">Politica de confidențialitate</a> și <a href="' + terms + '" target="_blank" rel="noopener">Termenii</a>.',
      sl: 'Prebral/a sem in sprejemam <a href="' + privacy + '" target="_blank" rel="noopener">politiko zasebnosti</a> in <a href="' + terms + '" target="_blank" rel="noopener">pogoje</a>.',
      hr: 'Pročitao/la sam i prihvaćam <a href="' + privacy + '" target="_blank" rel="noopener">Politiku privatnosti</a> i <a href="' + terms + '" target="_blank" rel="noopener">Uvjete</a>.',
      lt: 'Perskaičiau ir sutinku su <a href="' + privacy + '" target="_blank" rel="noopener">privatumo politika</a> ir <a href="' + terms + '" target="_blank" rel="noopener">sąlygomis</a>.',
      lv: 'Esmu izlasījis/-usi un piekrītu <a href="' + privacy + '" target="_blank" rel="noopener">privātuma politikai</a> un <a href="' + terms + '" target="_blank" rel="noopener">noteikumiem</a>.',
      et: 'Olen lugenud ja nõustun <a href="' + privacy + '" target="_blank" rel="noopener">privaatsuspoliitika</a> ja <a href="' + terms + '" target="_blank" rel="noopener">tingimustega</a>.',
      el: 'Έχω διαβάσει και αποδέχομαι την <a href="' + privacy + '" target="_blank" rel="noopener">Πολιτική απορρήτου</a> και τους <a href="' + terms + '" target="_blank" rel="noopener">Όρους</a>.',
      bg: 'Прочетох и приемам <a href="' + privacy + '" target="_blank" rel="noopener">Политиката за поверителност</a> и <a href="' + terms + '" target="_blank" rel="noopener">Условията</a>.'
    };
    const byGeo = {
      it: map.it, es: map.es, pt: map.pt, fr: map.fr, de: map.de, pl: map.pl,
      cz: map.cs, sk: map.sk, hu: map.hu, ro: map.ro, si: map.sl, hr: map.hr,
      lt: map.lt, lv: map.lv, ee: map.et, gr: map.el, bg: map.bg, en: null
    };
    if (byGeo[g]) return byGeo[g];
    return 'I have read and accept the <a href="' + privacy + '" target="_blank" rel="noopener">Privacy Policy</a> and <a href="' + terms + '" target="_blank" rel="noopener">Terms</a>.';
  }

  function siteGeo() {
    if (C.GEO) return C.GEO;
    const lang = (document.documentElement.lang || 'en').slice(0, 2).toLowerCase();
    return { cs: 'cz', el: 'gr', sl: 'si' }[lang] || lang;
  }

  function isOrderForm(form) {
    if (!form || form.tagName !== 'FORM') return false;
    if (form.classList.contains('tm-order-form') || form.classList.contains('cod-form') || form.classList.contains('order-form')) return true;
    return !!(form.querySelector('input[name="tel"], input[name="phone"]') && form.querySelector('input[name="name"]'));
  }

  function injectPrivacyConsent(form) {
    if (!isOrderForm(form) || form.querySelector('[name="privacy_consent"]')) return;
    const wrap = document.createElement('div');
    wrap.className = 'cod-form__field df-consent-field';
    wrap.innerHTML = '<label class="df-consent-label">'
      + '<input type="checkbox" name="privacy_consent" value="1" required>'
      + '<span>' + privacyCopy(siteGeo()) + '</span>'
      + '</label>';
    const submitBtn = form.querySelector('button[type="submit"], button[name="submit"]');
    if (submitBtn) submitBtn.parentNode.insertBefore(wrap, submitBtn);
    else form.appendChild(wrap);

    form.addEventListener('submit', function (e) {
      const box = form.querySelector('[name="privacy_consent"]');
      if (box && !box.checked) {
        e.preventDefault();
        e.stopPropagation();
        wrap.classList.add('has-error');
        box.focus();
      }
    }, true);
  }

  function initCookieBanner() {
    if (window.__dfCookieBannerInit) return;
    window.__dfCookieBannerInit = true;
    const KEY = 'df_cookie_consent';
    try {
      if (localStorage.getItem(KEY)) return;
    } catch (e) {
      return;
    }
    const banner = document.createElement('div');
    banner.setAttribute('role', 'dialog');
    banner.setAttribute('aria-label', 'Cookie consent');
    banner.style.cssText = 'position:fixed;bottom:0;left:0;right:0;background:#0f172a;color:#fff;padding:1rem;z-index:1000;display:flex;flex-wrap:wrap;align-items:center;justify-content:center;gap:1rem;font-size:0.875rem;box-shadow:0 -4px 12px rgba(0,0,0,0.2)';
    const cookieText = C.COOKIE_TEXT || 'We use cookies to improve your experience and for analytics.';
    const cookieAccept = C.COOKIE_ACCEPT || 'Accept';
    const cookieLearn = C.COOKIE_LEARN || 'Learn more';
    banner.innerHTML = '<span>' + cookieText + '</span>'
      + '<a href="/' + siteGeo() + '/cookie-policy.html" style="color:#86efac;text-decoration:underline">' + cookieLearn + '</a>'
      + '<button type="button" id="df-cookie-ok" style="background:#16a34a;color:#fff;border:none;padding:0.5rem 1.25rem;border-radius:0.375rem;cursor:pointer;font-weight:700">' + cookieAccept + '</button>';
    document.body.appendChild(banner);
    document.getElementById('df-cookie-ok').addEventListener('click', function () {
      try { localStorage.setItem(KEY, '1'); } catch (err) {}
      banner.remove();
    });
  }

  function injectConsentStyles() {
    if (document.getElementById('df-consent-style')) return;
    const style = document.createElement('style');
    style.id = 'df-consent-style';
    style.textContent = '.df-consent-field{margin:12px 0;text-align:left}.df-consent-label{display:flex;align-items:flex-start;gap:8px;font-size:13px;line-height:1.4;cursor:pointer}.df-consent-label input{margin-top:3px;flex-shrink:0}.df-consent-label a{color:inherit;text-decoration:underline}.df-consent-field.has-error{outline:2px solid #dc2626;outline-offset:4px;border-radius:6px}';
    document.head.appendChild(style);
  }

  document.addEventListener('DOMContentLoaded', function () {
    injectConsentStyles();
    initCookieBanner();
    wireCashboltForms(getTrackingContext());
    document.querySelectorAll('form').forEach(injectPrivacyConsent);
  });
})();

// ---- PUBLIC API ----
window.trackInitiateCheckout = function () {
  const C = window.SITE_CONFIG || {};
  const T = window.getLifepickshopTrackingContext ? window.getLifepickshopTrackingContext() : {};
  if (window.fbq) window.fbq('track', 'InitiateCheckout');
  if (window.gtag && C.GOOGLE_ADS_CONVERSION_ID) {
    window.gtag('event', 'begin_checkout', {
      campaign_id: T.campaign_id || '',
      subid: T.subid || '',
      utm_campaign: T.utm_campaign || '',
      utm_content: T.utm_content || '',
      utm_term: T.utm_term || '',
    });
  }
};

window.trackLead = function () {
  const C = window.SITE_CONFIG || {};
  const T = window.getLifepickshopTrackingContext ? window.getLifepickshopTrackingContext() : {};
  if (window.fbq) window.fbq('track', 'Lead');
  if (window.gtag && C.GOOGLE_ADS_CONVERSION_ID && C.GOOGLE_ADS_CONVERSION_LABEL) {
    window.gtag('event', 'conversion', {
      send_to: C.GOOGLE_ADS_CONVERSION_ID + '/' + C.GOOGLE_ADS_CONVERSION_LABEL,
      campaign_id: T.campaign_id || '',
      subid: T.subid || '',
      gclid: T.gclid || '',
      utm_campaign: T.utm_campaign || '',
      utm_content: T.utm_content || '',
      utm_term: T.utm_term || '',
    });
  }
};

window.trackPurchase = function (value, currency) {
  if (window.fireLifepickshopThankYouConversion) {
    return window.fireLifepickshopThankYouConversion({ value: value, currency: currency });
  }

  const C = window.SITE_CONFIG || {};
  const T = window.getLifepickshopTrackingContext ? window.getLifepickshopTrackingContext() : {};
  if (window.fbq) {
    window.fbq('track', 'Purchase', {
      value: value || C.PRICE || 0,
      currency: currency || C.CURRENCY || 'EUR',
      campaign_id: T.campaign_id || '',
      subid: T.subid || '',
    });
  }
  if (window.gtag && C.GOOGLE_ADS_CONVERSION_ID && C.TY_CONVERSION_LABEL) {
    window.gtag('event', 'conversion', {
      send_to: C.GOOGLE_ADS_CONVERSION_ID + '/' + C.TY_CONVERSION_LABEL,
      value: value || C.PRICE || 0,
      currency: currency || C.CURRENCY || 'EUR',
      campaign_id: T.campaign_id || '',
      subid: T.subid || '',
      gclid: T.gclid || '',
      utm_campaign: T.utm_campaign || '',
      utm_content: T.utm_content || '',
      utm_term: T.utm_term || '',
    });
  }
};
