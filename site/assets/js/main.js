/* González Armendáriz — JS mínimo (~3 KB). Sin dependencias. Se carga con `defer`.
   1. Menú móvil  2. Eventos de medición (dataLayer)  3. Formulario
   4. Mapa bajo demanda  5. Aviso de cookies + Consent Mode  6. Año del copyright
   7. Message match en landing pages (titular según anuncio, con lista blanca) */
(function () {
  "use strict";
  var dl = (window.dataLayer = window.dataLayer || []);
  var lang = document.documentElement.lang || "es";
  var es = lang.indexOf("es") === 0;

  function track(event, params) {
    var payload = { event: event, page_type: document.body.getAttribute("data-page-type") || "" };
    for (var k in params) payload[k] = params[k];
    dl.push(payload);
  }

  /* 1. Menú móvil ---------------------------------------------------- */
  var toggle = document.querySelector(".menu-toggle");
  var nav = document.getElementById("site-nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = toggle.getAttribute("aria-expanded") === "true";
      toggle.setAttribute("aria-expanded", String(!open));
      nav.classList.toggle("is-open", !open);
      document.body.style.overflow = open ? "" : "hidden";
    });
    nav.addEventListener("click", function (e) {
      if (e.target.closest("a") && nav.classList.contains("is-open")) toggle.click();
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && nav.classList.contains("is-open")) { toggle.click(); toggle.focus(); }
    });
  }

  /* 2. Clics en WhatsApp, teléfono y correo ---------------------------- */
  document.addEventListener("click", function (e) {
    var a = e.target.closest("a[href]");
    if (!a) return;
    var href = a.getAttribute("href");
    var where = a.getAttribute("data-location") || "";
    if (href.indexOf("https://wa.me/") === 0) track("whatsapp_click", { link_location: where });
    else if (href.indexOf("tel:") === 0) track("phone_click", { link_location: where, phone_number: href.slice(4) });
    else if (href.indexOf("mailto:") === 0) track("email_click", { link_location: where });
    else if (a.hasAttribute("data-cta")) track("cta_click", { link_location: where, link_text: a.textContent.trim() });
  });

  // Scroll al 75 % (una vez por página). También puede hacerse con el disparador nativo de GTM.
  var scrolled = false;
  window.addEventListener("scroll", function () {
    if (scrolled) return;
    var h = document.documentElement;
    if ((h.scrollTop + window.innerHeight) / h.scrollHeight >= 0.75) {
      scrolled = true;
      track("scroll_75", { percent_scrolled: 75 });
    }
  }, { passive: true });

  /* 3. Formulario de consulta ------------------------------------------ */
  var msgs = es
    ? { required: "Este dato es necesario.", tel: "Escriba un teléfono de 10 dígitos.", sending: "Enviando…", error: "No pudimos enviar su solicitud. Llámenos o escríbanos por WhatsApp.", demo: "Formulario en modo demostración: falta configurar el destino (data-endpoint)." }
    : { required: "This field is required.", tel: "Please enter a 10-digit phone number.", sending: "Sending…", error: "We could not send your request. Please call us or message us on WhatsApp.", demo: "Demo mode: the form endpoint (data-endpoint) is not configured yet." };

  function validate(field) {
    var err = document.getElementById(field.id + "-error");
    var msg = "";
    if (!field.value.trim()) msg = msgs.required;
    else if (field.type === "tel" && field.value.replace(/\D/g, "").length < 10) msg = msgs.tel;
    field.setAttribute("aria-invalid", msg ? "true" : "false");
    if (err) err.textContent = msg;
    return !msg;
  }

  Array.prototype.forEach.call(document.querySelectorAll("form.lead-form"), function (form) {
    var started = false;
    form.addEventListener("input", function () {
      if (!started) { started = true; track("form_start", { form_id: form.id }); }
    });
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var fields = form.querySelectorAll("[required]");
      var ok = true, first = null;
      Array.prototype.forEach.call(fields, function (f) { if (!validate(f)) { ok = false; first = first || f; } });
      if (!ok) { first.focus(); return; }
      if (form.website && form.website.value) return; // honeypot: bot

      var status = form.querySelector(".form-status");
      var btn = form.querySelector("[type=submit]");
      var endpoint = form.getAttribute("data-endpoint");
      var service = form.servicio ? form.servicio.value : "";
      var done = function () {
        track("generate_lead", { form_id: form.id, service_interest: service });
        window.location.href = form.getAttribute("data-success") || "/gracias/";
      };
      if (!endpoint) { status.textContent = msgs.demo; console.warn(msgs.demo); return; }

      btn.disabled = true; status.removeAttribute("data-state"); status.textContent = msgs.sending;
      fetch(endpoint, { method: "POST", body: new FormData(form), headers: { Accept: "application/json" } })
        .then(function (r) { if (!r.ok) throw new Error(r.status); done(); })
        .catch(function () {
          btn.disabled = false; status.setAttribute("data-state", "error"); status.textContent = msgs.error;
          track("form_error", { form_id: form.id });
        });
    });
    Array.prototype.forEach.call(form.querySelectorAll("[required]"), function (f) {
      f.addEventListener("blur", function () { if (f.value) validate(f); });
    });
  });

  /* 4. Mapa bajo demanda (no carga Google Maps hasta que el usuario lo pide) */
  Array.prototype.forEach.call(document.querySelectorAll("[data-map-load]"), function (btn) {
    btn.addEventListener("click", function () {
      var box = btn.closest(".map-facade");
      var f = document.createElement("iframe");
      f.src = box.getAttribute("data-map-src");
      f.title = btn.getAttribute("data-map-title") || "Mapa";
      f.loading = "lazy";
      f.referrerPolicy = "no-referrer-when-downgrade";
      box.appendChild(f);
      track("map_open", {});
    });
  });

  /* 5. Aviso de cookies + Google Consent Mode v2 ------------------------ */
  var banner = document.getElementById("cookie-banner");
  var KEY = "ga_consent_v1";
  function store(v) { try { localStorage.setItem(KEY, v); } catch (e) {} }
  function read() { try { return localStorage.getItem(KEY); } catch (e) { return null; } }
  function applyConsent(v) {
    var g = v === "granted" ? "granted" : "denied";
    if (typeof window.gtag === "function") {
      window.gtag("consent", "update", { analytics_storage: g, ad_storage: g, ad_user_data: g, ad_personalization: g });
    }
    track("consent_update", { consent: g });
  }
  if (banner) {
    var saved = read();
    if (saved) applyConsent(saved);
    else banner.hidden = false;
    banner.addEventListener("click", function (e) {
      var b = e.target.closest("[data-consent]");
      if (!b) return;
      var v = b.getAttribute("data-consent");
      store(v); applyConsent(v); banner.hidden = true;
    });
  }

  /* 6. Año del copyright ---------------------------------------------- */
  Array.prototype.forEach.call(document.querySelectorAll("[data-year]"), function (el) {
    el.textContent = new Date().getFullYear();
  });

  /* 6b. Atribución: guarda UTMs y click IDs de la primera página vista y los
         copia a los campos ocultos [data-utm] del formulario. */
  var ATTR = ["utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content", "gclid", "fbclid", "li_fat_id"];
  var qs = new URLSearchParams(window.location.search);
  ATTR.forEach(function (k) {
    var v = qs.get(k);
    try { if (v) sessionStorage.setItem("attr_" + k, v.slice(0, 200)); else v = sessionStorage.getItem("attr_" + k); } catch (e) {}
    if (!v) return;
    Array.prototype.forEach.call(document.querySelectorAll('input[data-utm][name="' + k + '"]'), function (i) { i.value = v; });
  });

  /* 7. Message match: ?v=<variante> cambia el titular por uno de la lista
        blanca definida en la propia página (nunca se inserta texto de la URL). */
  var variants = document.getElementById("lp-variants");
  if (variants) {
    try {
      var map = JSON.parse(variants.textContent);
      var v = new URLSearchParams(window.location.search).get("v");
      if (v && Object.prototype.hasOwnProperty.call(map, v)) {
        var h1 = document.querySelector("[data-lp-headline]");
        var sub = document.querySelector("[data-lp-sub]");
        if (h1 && map[v].h1) h1.textContent = map[v].h1;
        if (sub && map[v].sub) sub.textContent = map[v].sub;
      }
    } catch (e) {}
  }
})();
