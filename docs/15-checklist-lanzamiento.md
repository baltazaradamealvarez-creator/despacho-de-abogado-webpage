# 15. Checklist final de lanzamiento

Marque cada punto en staging **y** de nuevo en producción el día del lanzamiento.

## 15.0 Plataforma (recomendación)
- [ ] **Quitar WPBakery.** Genera HTML pesado, shortcodes que se rompen al desinstalarlo y CSS/JS en todas las páginas.
- [ ] Opción recomendada: **WordPress + tema ligero (GeneratePress o Kadence) + GenerateBlocks**, construyendo las plantillas con el HTML/CSS de `site/`.
  Plugins: Rank Math o Yoast (SEO) · Polylang Pro o WPML (bilingüe con hreflang) · Fluent Forms (formulario) · Redirection · WP Rocket o LiteSpeed Cache · Complianz (cookies) · plugin oficial de Meta (CAPI). Nada más.
- [ ] Alternativa: sitio estático (Astro/Eleventy) con el blog en un CMS headless. Más rápido, pero el equipo depende de un desarrollador para cambios.
- [ ] Hosting con PHP 8.2+, HTTP/2 o HTTP/3, Brotli y TTFB < 600 ms desde México (servidor en EE. UU. centro/sur o CDN con nodo en Querétaro/Monterrey).

## 15.1 Contenido y datos
- [ ] Todos los `[PENDIENTE]` resueltos o retirados del sitio (buscar "PENDIENTE" y la clase `.pending` en el código).
- [ ] Todos los `[SUPUESTO]` confirmados por la firma (horario, alcance de servicios, atención en inglés, honorarios fijos, primera consulta).
- [ ] Frase del fundador aprobada; semblanza y foto real.
- [ ] Testimonios y logos solo con autorización por escrito.
- [ ] Copy revisado por un socio (exactitud técnica) y por un editor nativo en inglés.
- [ ] Ninguna promesa de resultado ("garantizado", "ahorre", "evite auditorías").
- [ ] Teléfonos, WhatsApp, dirección y correo idénticos en sitio, GBP, LinkedIn, Facebook y directorios (NAP).
- [ ] Año de copyright dinámico (ya implementado con `data-year`).
- [ ] Newsletter y blog fuera del home; Bolsa de trabajo solo en el footer.

## 15.2 SEO técnico
- [ ] Un H1 por página; jerarquía H2/H3 sin saltos.
- [ ] Meta title ≤ 60 y meta description ≤ 155 en todas las páginas (ver `03`, `04`, `04b`).
- [ ] URLs finales según `02-mapa-del-sitio.md`; minúsculas, sin acentos.
- [ ] `canonical` autorreferente en cada página.
- [ ] `hreflang` es-MX ↔ en-US recíproco + `x-default` en cada par de páginas (Polylang/WPML los generan; verificar con un validador de hreflang).
- [ ] JSON-LD de `08-json-ld.md` instalado y validado en Rich Results Test y validator.schema.org, sin valores "PENDIENTE".
- [ ] `sitemap.xml` sin landings, gracias ni páginas noindex; enviado en Search Console.
- [ ] `robots.txt` publicado; no bloquea CSS, JS ni páginas con noindex.
- [ ] Landings y `/gracias/` con `noindex, follow`.
- [ ] Páginas de etiquetas, autor, fecha y adjuntos de WordPress en `noindex` o desactivadas.
- [ ] Alt descriptivo en todas las imágenes; nombres de archivo descriptivos.
- [ ] Enlazado interno: servicios ↔ servicios relacionados ↔ artículos ↔ contacto.
- [ ] Viewport sin `maximum-scale=1` ni `user-scalable=no` (ya corregido en el código).
- [ ] Open Graph y Twitter Cards con imagen 1200×630 (incluida: `assets/img/og-gonzalez-armendariz.jpg`); probar con el Post Inspector de LinkedIn, el Sharing Debugger de Facebook y un chat de WhatsApp.
- [ ] Favicon SVG + `favicon.ico` + `apple-touch-icon.png`.
- [ ] Página 404 útil (buscador, servicios y contacto) que devuelva estado 404 real.

## 15.3 Redirecciones
- [ ] Rastreo completo del sitio actual (Screaming Frog) + exportación de Search Console y Analytics.
- [ ] Mapa 1 a 1 de URLs viejas → nuevas (incluye `/beta/` y la versión EN actual).
- [ ] 301 implementadas (plugin Redirection o `.htaccess`), sin cadenas ni bucles.
- [ ] HTTP → HTTPS y www → sin www en una sola redirección.
- [ ] Prueba con la lista de URLs viejas: todas responden 301 → 200.
- [ ] Instalación `/beta/` eliminada (archivos y base de datos).
- [ ] Rastreo del sitio nuevo: 0 enlaces rotos internos, 0 redirecciones internas (los enlaces apuntan a la URL final).

## 15.4 Velocidad y Core Web Vitals (objetivo: 90+ en PageSpeed móvil)
Medición de referencia del código entregado (Lighthouse 12, perfil móvil, servidor local): **home 99 · accesibilidad 100 · buenas prácticas 100 · SEO 100; LCP 1.8 s, CLS 0, TBT 90 ms**. La landing obtiene lo mismo (su SEO marca 66 solo porque es `noindex`, a propósito).
- [ ] LCP < 2.5 s, CLS < 0.1, INP < 200 ms en PageSpeed Insights (móvil) para home, un servicio, un artículo y cada landing.
- [ ] Imágenes en WebP/AVIF con `width` y `height`, `loading="lazy"` salvo la primera visible, `srcset` para retratos.
- [ ] Fuentes autoalojadas (incluidas en `assets/fonts/`, 110 KB en total) con `preload` de las dos principales.
- [ ] Sin sliders, sin jQuery innecesario, sin Google Maps cargado de inicio (fachada incluida).
- [ ] CSS y JS minificados en producción; compresión Brotli o Gzip; caché de 1 año para estáticos con nombre versionado (reglas en `site/.htaccess`).
- [ ] GTM con pocas etiquetas; nada de scripts de chat de terceros sin justificar.
- [ ] Revisar Core Web Vitals reales en Search Console 28 días después del lanzamiento.

## 15.5 Conversión
- [ ] Formulario de 4 campos funcionando de punta a punta: envío → correo al responsable y al CRM → página de gracias.
- [ ] Destino del formulario configurado (`data-endpoint`) y protegido contra spam (honeypot incluido + reCAPTCHA v3 o Turnstile si hace falta).
- [ ] Notificación de nuevo lead a [PENDIENTE: correo(s) y WhatsApp del responsable] con tiempo de respuesta objetivo.
- [ ] Enlaces `tel:` y `wa.me` probados en iPhone y Android.
- [ ] Botón flotante de WhatsApp visible en móvil sin tapar el formulario ni el aviso de cookies.
- [ ] Variantes `?v=` de las landings probadas (titular correcto por grupo de anuncios).
- [ ] Prueba de navegación solo con teclado y con lector de pantalla (VoiceOver o NVDA) en home y landing.

## 15.6 Medición
- [ ] Contenedor GTM publicado (reemplazar `GTM-XXXXXXX` en todas las plantillas).
- [ ] GA4: flujo de datos, eventos clave (`generate_lead`, `whatsapp_click`, `phone_click`), dimensiones personalizadas, exclusión de IP interna, vinculación con Google Ads y Search Console.
- [ ] Google Ads: conversiones creadas y marcadas como principales o secundarias (ver `13`), conversiones mejoradas para leads, etiquetado automático activado, sufijo de URL final con UTMs.
- [ ] Píxel de Meta + API de Conversiones con deduplicación; dominio verificado en Business Manager; evento `Lead` priorizado.
- [ ] LinkedIn Insight Tag + conversión "Lead".
- [ ] Prueba real de cada conversión (formulario, WhatsApp, teléfono) vista en GTM Preview, DebugView, Tag Assistant, Pixel Helper e Insight Tag Helper.
- [ ] Consent Mode v2 verificado: con "Rechazar", las etiquetas de publicidad no escriben cookies.
- [ ] Tablero en Looker Studio (leads y costo por lead por canal y servicio).
- [ ] Anotar la fecha de lanzamiento en GA4 y en Search Console.

## 15.7 Legal y privacidad
- [ ] Aviso de privacidad integral ES/EN publicado, con sección de cookies (ver `13-plan-de-medicion.md` §13.6) y revisado por el abogado.
- [ ] Aviso simplificado junto a cada formulario (incluido en el código).
- [ ] Banner de cookies con Aceptar y Rechazar en igualdad de condiciones; registro de consentimiento.
- [ ] Términos de uso del sitio [PENDIENTE: si la firma los requiere].
- [ ] Autorizaciones por escrito de testimonios, logos y fotos del equipo.
- [ ] Certificado SSL vigente con renovación automática.
- [ ] Respaldos automáticos diarios del sitio y la base de datos; usuarios administradores con 2FA.

## 15.8 SEO local y lanzamiento
- [ ] Google Business Profile actualizado (categorías, descripción, servicios, fotos, enlace con UTM) según `09`.
- [ ] Directorios corregidos o registrados (10 + plataformas globales).
- [ ] Primer artículo de Perspectivas publicado y 3 artículos viejos actualizados o redirigidos.
- [ ] Campañas de Google Ads en pausa hasta verificar conversiones; después, encender con presupuesto bajo la primera semana.
- [ ] Revisión a las 2, 4 y 8 semanas: cobertura en Search Console, errores 404, posiciones de keywords principales, costo por lead.
