# 14. Código HTML/CSS: home y landing page

El código está en `site/` y funciona sin compilar: basta con subir la carpeta a cualquier hosting o abrirla con un servidor local.

```
site/
├── index.html                          Home (ES) con JSON-LD, Consent Mode, GTM, formulario y mapa ligero
├── lp/contabilidad-empresas/index.html Landing de Google Ads/Meta/LinkedIn (noindex, sin menú, variantes ?v=)
├── gracias/index.html                  Página de gracias (noindex): respaldo para medir conversiones
├── assets/css/main.css                 Una sola hoja de estilos para todo el sitio (~23 KB; ~6 KB con gzip)
├── assets/js/main.js                   JS mínimo (~9 KB): menú, eventos de medición, formulario, cookies, UTMs
├── assets/fonts/                       Inter y Cormorant Garamond autoalojadas (WOFF2 latino, licencia OFL)
├── assets/img/og-gonzalez-armendariz.jpg  Imagen para WhatsApp/LinkedIn/Facebook (1200×630)
├── assets/img/favicon.svg              Monograma provisional "GA"
├── assets/img/retrato-pendiente.svg    Marcador hasta tener la foto del fundador
├── robots.txt · sitemap.xml            Con hreflang es-MX / en-US / x-default
└── .htaccess                           HTTPS, dominio canónico, 301, compresión, caché y cabeceras
```

## Verlo en local
```bash
cd site && npx http-server -p 8080
# Home:     http://localhost:8080/
# Landing:  http://localhost:8080/lp/contabilidad-empresas/?v=despacho
```

## Qué incluye
- Mobile-first, sin dependencias ni frameworks, sin jQuery ni sliders.
- Accesibilidad AA: contraste verificado, zoom permitido, enlace "saltar al contenido", foco visible, menú operable con teclado (Esc cierra), acordeones nativos `<details>`, errores de formulario anunciados.
- SEO: un H1, jerarquía lógica, canonical, hreflang, Open Graph/Twitter, JSON-LD (`AccountingService`, `WebSite`, `WebPage`, `Person`, `FAQPage`, `Service`) con FAQ idéntica al texto visible.
- Velocidad: H1 como LCP sin animación, fuentes precargadas con `font-display: swap` y fallback métrico, Google Maps solo bajo demanda, JS diferido, imágenes con dimensiones.
- Conversión: un CTA por pantalla, formulario de 4 campos con validación accesible y honeypot, click-to-call, WhatsApp flotante en móvil, aviso simplificado de privacidad junto al formulario.
- Medición: eventos `generate_lead`, `whatsapp_click`, `phone_click`, `email_click`, `scroll_75`, `form_start`, `form_error`, `cta_click`, `map_open` en `dataLayer`; captura de UTMs y click IDs en campos ocultos; Consent Mode v2 con banner Aceptar/Rechazar.

## Resultado de Lighthouse 12 (móvil, servidor local sin compresión)
| Página | Rendimiento | Accesibilidad | Buenas prácticas | SEO | LCP | CLS | TBT |
|---|---|---|---|---|---|---|---|
| Home | 99 | 100 | 100 | 100 | 1.8 s | 0 | 90 ms |
| Landing | 99 | 100 | 100 | 66* | 1.8 s | 0 | 0 ms |

\* La landing lleva `noindex` a propósito; es lo único que baja la puntuación de SEO. Las sugerencias restantes (compresión, caché, minificación) se resuelven en el servidor con `.htaccess` y el plugin de caché.

## Para pasar a producción
1. Reemplazar `GTM-XXXXXXX` (3 archivos).
2. Configurar `data-endpoint` del formulario (URL del servicio que recibe los datos: Fluent Forms REST, HubSpot Forms API, Formspree, etc.).
3. Quitar los marcadores `.pending` al tener los datos (correo, horario, tiempo de respuesta, afiliaciones, testimonios, frase del fundador).
4. Sustituir `retrato-pendiente.svg` por `alejandro-gonzalez-director-fundador.webp` (800×1000).
5. Verificar las coordenadas `geo` del JSON-LD con el pin de Google Business Profile.
6. Construir las landings de Asesoría Fiscal y Auditoría copiando `lp/contabilidad-empresas/` con el copy de `05-landing-pages.md`.
7. En WordPress: convertir las secciones en patrones de bloques (GenerateBlocks) y cargar `main.css` y `main.js` desde el tema hijo.
