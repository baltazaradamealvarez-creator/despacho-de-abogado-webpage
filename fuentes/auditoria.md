# Auditoría del sitio público y trazabilidad

Consulta realizada durante la sesión del 5–6 de octubre de 2026. Los primeros intentos con timeout corto fallaron; el acceso HTTP posterior con timeout45 s obtuvo respuesta200 y contenido. Un timeout inicial no demuestra caída general del sitio.

## Fuentes efectivamente leídas

| URL | Copia local / alcance |
|---|---|
| https://gonzalezarmendariz.com/ | `home-original.html`, documento HTML completo en español |
| https://gonzalezarmendariz.com/nosotros/ | `nosotros_.txt`, historia, misión, visión y valores |
| https://gonzalezarmendariz.com/equipo/ | `equipo_.txt`, nombres y cargos publicados |
| https://gonzalezarmendariz.com/servicios/ | `servicios_.txt`, catálogo y descripciones visibles |
| https://gonzalezarmendariz.com/contacto/ | `contacto_.txt`, dirección, teléfonos y WhatsApp antiguo |
| https://gonzalezarmendariz.com/blog/ | `blog_.txt`, archivo y enlaces |
| https://gonzalezarmendariz.com/en/ | `en_.txt`, contenido inglés con diferencias respecto a español |
| https://gonzalezarmendariz.com/wp-json/wp/v2/posts?per_page=100 | `wp-json_wp_v2_posts_per_page=100.txt`: JSON válido con 18 entradas, 15 ES y 3 EN, título, URL, fecha y cuerpo. Auditoría individual en entregable10. No se infiere inventario de borradores, privados o tipos de contenido adicionales. |
| https://gonzalezarmendariz.com/wp-sitemap.xml | `wp-sitemap.xml.txt`: índice Yoast de posts, páginas, categorías, tags y autores |
| https://gonzalezarmendariz.com/robots.txt | `robots.txt.txt`: respuesta sin contenido en esta captura; reconfirmar cabeceras/servidor antes de concluir configuración |

## Hallazgos observados y acciones

1. **Home redundante:** muestra una primera selección de servicios y luego otra sección completa con descripciones repetidas. Sustituir por cinco tarjetas únicas; sacar blog y newsletter del home.
2. **Lenguaje arriesgado:** se publican formulaciones sobre prevenir auditorías SAT y eliminar riesgos de auditoría, además de garantías amplias. Sustituir por revisión, claridad y reducción de riesgos; no prometer ausencia de revisión o sanciones.
3. **Zoom bloqueado:** meta viewport exacta `width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no`. Cambiar a `width=device-width, initial-scale=1`.
4. **Meta description del home:** no se encontró etiqueta `meta[name=description]` en el HTML descargado. Crear metas únicas y probar HTML servido, no solo vista del editor.
5. **H1 existente:** uno, con texto largo “FIRMA DE CONSULTORÍA CONTABLE, AUDITORÍA Y ASESORÍA FISCAL CORPORATIVA.”. Reemplazar por titular local corto; no afirmar que hoy hay varios H1.
6. **Peso potencial del front:** HTML referencia 19 scripts externos y 18 hojas de estilo; contiene `js_composer` (WPBakery). Estos conteos no son métricas de rendimiento. Recomendación: WordPress con bloques nativos y tema ligero o front estático; medir laboratorio y datos reales antes/después.
7. **Imágenes sin texto alternativo:** seis imágenes de contenido visibles en la captura tienen `alt=""`, entre ellas fundador, colaboradora y artículos. Añadir alt útil cuando informativas; conservar alt vacío solo para decoración. El logo sí tiene alt.
8. **Datos estructurados:** existe un bloque JSON-LD Yoast; no se debe afirmar ausencia total de schema. Integrar entidades propuestas evitando duplicación/conflictos de IDs con el plugin.
9. **Versiones desalineadas:** ES dice28+ años; Equipo dice 26 y EN26. Home EN conserva hero en español, blog 2021 y copyright 2021. ES copyright 2024. Unificar a los datos actuales del briefing y copyright 2026 en ambas versiones.
10. **Contacto inconsistente:** `/contacto/` publica WhatsApp8118004188; el briefing autoriza8128845949. Adoptar este último, corregir fichas y probar desde móvil. Tres teléfonos y dirección coinciden en sustancia; normalizar espacios y municipio.
11. **Autoría editorial:** entradas publicadas como “Admin” y tres artículos EN son teasers de una frase; reemplazar por autor/revisor identificados y textos completos. No asignar al fundador autoría de artículos sin aprobación.
12. **Sitemap:** ya hay un índice Yoast. Revisar necesidad de categorías/tags/autores indexables; no generar archivos paralelos que contradigan el índice principal. `lastmod` solo cuando cambia el contenido real.

## Datos adicionales encontrados: no aprobados automáticamente para nuevo copy

- Nosotros declara fundación en 1998. [PENDIENTE] Confirmar antes de usar fecha legal/histórica o `foundingDate`; briefing solo confirma28+ años.
- Equipo publica a **Karla Hibargüen, Asesor Sr.**, contador público, UANL y20 años de experiencia. [PENDIENTE] Actualidad del cargo, semblanza y consentimiento. EN también menciona **Xiomara Salazar, Administrative Services**, no presente en home ES actual; no asumir que sigue en el equipo.
- Equipo afirma profesionales certificados/calificados por IMCP; EN afirma certificaciones oficiales. [PENDIENTE] Documentos, titulares, vigencia y alcance. No usar sellos, afiliaciones ni claims de certificación sin verificación.
- No se encontró enlace `mailto:` en home ni correo validado en las páginas examinadas. No deducir `info@` ni `contacto@` del dominio.
- No se verificaron horarios, coordenadas exactas, consulta gratuita, testimonios ni autorizaciones de logos.

## Activos reales localizados

- Logo: https://gonzalezarmendariz.com/wp-content/uploads/2021/09/logo.png
- Foto asociada en el home a Alejandro González: https://gonzalezarmendariz.com/wp-content/uploads/2021/10/fotos-equipo-GA_1.jpg
- Foto asociada a Karla Hibargüen: https://gonzalezarmendariz.com/wp-content/uploads/2021/10/fotos-equipo-GA_4.jpg
- Otra imagen presente: https://gonzalezarmendariz.com/wp-content/uploads/2021/09/5efcaa44df941c49a9a2a6f0_Imagen-9.jpg — su presencia no prueba que represente oficina real de la firma; verificar procedencia antes de presentarla como tal.

Se pueden reutilizar activos identificados de la misma firma para el rediseño, manteniendo [PENDIENTE] confirmación de actualidad y derechos. No generar retratos ficticios ni usar imágenes de terceros como si fueran el equipo.

## Límites de la auditoría

No hay acceso a Analytics, Search Console, Keyword Planner, perfil GBP, Google Ads ni CMS privado. No se midieron Core Web Vitals reales, ranking, tráfico, conversiones, volumen de búsquedas ni enlaces entrantes. Los objetivos 90+ móvil/LCP<2.5s/CLS<0.1/INP<200ms son objetivos, no resultados certificados. El HTML permite hallazgos concretos; no constituye auditoría completa de seguridad, accesibilidad o todas las URLs.

Fuentes normativas de apoyo consultadas mediante herramienta web: Google Business Profile categorías (`https://support.google.com/business/answer/7249669?hl=es`) y reseñas (`https://support.google.com/business/answer/3474122?hl=es`); SAT (`https://www.sat.gob.mx/`, portal sin cuerpo extraíble en esa herramienta) y Ley del ISR (`https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf`, PDF disponible). La guía no afirma que el calendario 2027 esté ya emitido. Los directorios se proponen con condición explícita de verificación de alta/elegibilidad.
