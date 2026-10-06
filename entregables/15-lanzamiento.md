# 15. Checklist final de lanzamiento

Esta entrega contiene especificaciones y código fuente; no reemplaza el WordPress actual ni publica campañas. Los objetivos de velocidad requieren medición en el hosting final, con contenido, consentimiento y etiquetas reales.

## Contenido y operación

- [ ] Aprobar copy ES/EN, cifras (28+ años, 400+ empresas, 30 colaboradores), cargos, alcance por servicio y proceso propuesto. No sustituir «colaboradores» por «especialistas» sin confirmación.
- [ ] Obtener logo de calidad, fotos reales, permisos de imagen, perfiles del equipo, testimonios y afiliaciones comprobables. Omitir lo no confirmado.
- [ ] Confirmar correo de contacto, horarios, coordenadas de la oficina, razón social responsable, datos de privacidad y si una consulta tiene costo. No publicar [PENDIENTE] ni valores inventados.
- [ ] Formulario con exactamente cuatro campos comerciales: nombre, empresa, teléfono, servicio. Definir endpoint, receptor, controles de privacidad, antispam, validación servidor, registro mínimo y seguimiento. Prueba end-to-end de entrega, error y reintento antes de activar.
- [ ] Mensaje de éxito solo tras respuesta exitosa del servidor; no afirmar reserva de cita si solo se capturó una solicitud. Confirmar proceso real de agenda.
- [ ] Revisar teléfono, WhatsApp, dirección y enlaces en móvil; confirmar todos los números con la firma. Horarios o plazos de respuesta sin validar se omiten.
- [ ] Copyright 2026 o año actual dinámico. Empleo solo footer. Blog y newsletter fuera del home.

## Migración WordPress y SEO

- [ ] Copia completa y probada de archivos/base de datos; entorno staging protegido por autenticación, plan de reversión y ventana de cambio.
- [ ] Sustituir WPBakery por tema ligero con bloques nativos, si se conserva WordPress. Migrar textos que dependan de shortcodes antes de desactivar el constructor. No instalar otro constructor pesado para replicar el problema.
- [ ] Inventariar URLs reales con rastreo, sitemap, Search Console y analítica. Tabla URL vieja → URL nueva solo cuando exista equivalencia real de intención. Conservar URLs útiles si cambiarlas no aporta valor.
- [ ] Redirección 301 de una sola transición, sin bucles ni envío masivo de todo al home. Recursos sin equivalente: revisar conservar, redirigir al recurso más pertinente o responder 404/410. Probar cada fila del mapa, incluidos medios y variantes históricas.
- [ ] HTTPS en todos los recursos; www/no-www, slash final y protocolo normalizados con una única versión canónica. Certificado y renovación verificados.
- [ ] Meta title ≤60 caracteres y description ≤155 según matriz; cada página con H1 único, headings ordenados, copy propio y enlaces internos pertinentes. Los límites de caracteres son editoriales; Google puede truncar o reescribir snippets.
- [ ] Canonical absoluto autorreferente en las páginas indexables ES/EN. Cada pareja hreflang recíproca incluye es-MX y en-US más autorreferencia; x-default opcional hacia la versión por defecto. No usar canonical ES en traducción EN.
- [ ] `lang=es-MX` / `en-US`, títulos/labels/errores/alt en idioma correspondiente. No redirigir automáticamente por IP; selector de idioma visible.
- [ ] Sitemap XML solo con URLs canónicas indexables que devuelven 200; excluir noindex, landings publicitarias, redirecciones y staging. `lastmod` refleja modificaciones reales.
- [ ] robots.txt accesible con ubicación del sitemap; no bloquear CSS/JS esenciales. No usar robots.txt para impedir indexación de landings con noindex: el robot debe leer la directiva. Retirar noindex de producción orgánica al publicar.
- [ ] JSON-LD sin placeholders; datos iguales al contenido visible. Validar Schema.org y prueba de resultados enriquecidos, entendiendo que schema válido no equivale a elegibilidad ni aparición garantizada.
- [ ] FAQPage únicamente con preguntas/respuestas visibles y exactas. Google restringe los resultados enriquecidos FAQ principalmente a sitios gubernamentales y de salud reconocidos; no prometerlos a este despacho ni prometer presencia en respuestas de IA.
- [ ] OG/Twitter con URL absoluta, imagen de marca real, alt de imagen social y textos ES/EN; comprobar vistas previas en WhatsApp/LinkedIn y HTTPS de la imagen.
- [ ] 404 útil, enlaces de navegación, formularios, mapas, PDFs y cinco servicios comprobados. Configurar Search Console y enviar sitemap tras publicación.

## Rendimiento y accesibilidad

- [ ] Medir PageSpeed móvil y escritorio en home, servicio, contacto, blog y landing; objetivo 90+, nunca presentarlo como resultado medido antes de probar.
- [ ] Core Web Vitals de campo al percentil 75: LCP <2.5 s, INP <200 ms, CLS <0.1. Lighthouse es prueba de laboratorio; INP real se verifica con datos de campo/CrUX cuando haya muestra suficiente, típicamente ventana móvil de 28 días. Un buen TBT de laboratorio no demuestra INP de campo.
- [ ] Imágenes WebP/AVIF, tamaños responsive, dimensiones explícitas, compresión revisada visualmente. Recurso LCP prioritario sin lazy loading; lazy loading bajo el pliegue.
- [ ] Dos familias máximo, WOFF2 local si se eligen fuentes personalizadas, pesos mínimos, swap y preload selectivo. CSS pequeño, JS diferido y dependencias auditadas; sin sliders, videos de fondo ni plugins redundantes.
- [ ] Caché de página/activos, Brotli o gzip, CDN si conviene y pruebas de TTFB en hosting final. Medir con GTM/consentimiento reales, no solo demo sin terceros.
- [ ] `meta name="viewport" content="width=device-width, initial-scale=1"`; eliminar maximum-scale=1 y user-scalable=no. Zoom 200%, reflow 320 px, teclado, foco, lector de pantalla y reducción de movimiento.
- [ ] Contraste AA para todos los estados, labels permanentes, mensajes de error accesibles, orden lógico y botones táctiles. Botón flotante no tapa contenido ni banner.

## Medición, campañas y privacidad

- [ ] GA4/GTM, conversiones Ads, Meta y LinkedIn bajo consentimiento aplicable; comprobar que no se envían nombre, empresa identificable, teléfono ni correo en URLs o parámetros analíticos.
- [ ] Envío de formulario confirmado por backend como conversión primaria; clic WhatsApp/teléfono/correo y scroll 75% como señales secundarias. Evitar duplicar una conversión mediante etiqueta directa e importación GA4.
- [ ] UTMs consistentes por plataforma/campaña/anuncio, preservadas de forma permitida. Pruebas de una sesión por plataforma, deduplicación y exclusión de tráfico interno.
- [ ] Landings sin menú, con message match, FAQ, identidad real y política de privacidad. Probar política de destino Google Ads, parámetros de tracking, móviles y ausencia de errores.
- [ ] Validar con asesor jurídico el aviso integral y simplificado conforme a la LFPDPPP vigente (nueva ley publicada el 20 de marzo de 2025 y reformas aplicables). No reutilizar sin revisión un aviso antiguo con autoridades/procedimientos obsoletos.
- [ ] Aviso: identidad y domicilio del responsable, datos tratados, finalidades necesarias/optativas, transferencias aplicables, medios ARCO, revocación, limitación de uso y cambios. Definir plazos de conservación y contratos con encargados. No solicitar documentación fiscal por un formulario público de cuatro campos.
- [ ] Banner con aceptar, rechazar y configurar opciones no esenciales de forma clara, control por categoría y retirada posterior. Implementar bloqueo previo de publicidad/terceros según base legal y decisión jurídica; consentimiento no equivale por sí solo a cumplimiento legal.
- [ ] Evaluar Consent Mode v2 y política de cookies con asesor/implementador; para la opción conservadora básica, no cargar etiquetas no esenciales antes de aceptar. Probar navegación, rechazo, aceptación y revocación. No asumir que México copia automáticamente todas las reglas europeas.
- [ ] Verificar alertas de formularios, seguridad WordPress, actualizaciones, backups, permisos, monitorización 404/5xx y responsable de mantenimiento. Revisar semanalmente leads y términos de búsqueda al inicio; mensualmente SEO y contenidos.

## Referencias técnicas oficiales

- Schema.org: https://schema.org/AccountingService y https://schema.org/Service
- Google FAQ: https://developers.google.com/search/docs/appearance/structured-data/faqpage
- Google Organization: https://developers.google.com/search/docs/appearance/structured-data/organization
- Google LocalBusiness: https://developers.google.com/search/docs/appearance/structured-data/local-business
- Versiones localizadas/hreflang: https://developers.google.com/search/docs/specialty/international/localized-versions
- Sitemap: https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview
- Core Web Vitals: https://web.dev/articles/vitals
- LFPDPPP vigente: https://www.diputados.gob.mx/LeyesBiblio/pdf/LFPDPPP.pdf

Consultar versiones vigentes al implementar. Estas referencias sustentan criterios técnicos y remiten la validación jurídica a un profesional; no sustituyen pruebas del sitio final.
