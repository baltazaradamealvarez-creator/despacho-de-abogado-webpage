# 2. Mapa del sitio y URLs finales

Dominio canónico propuesto: `https://gonzalezarmendariz.com`, HTTPS, sin www, URLs en minúsculas y con barra final. [PENDIENTE] Confirmar preferencia actual con Search Console y conservar señales de la variante dominante.

| Página | Español es-MX | Inglés en-US | Indexación |
|---|---|---|---|
| Inicio | `/` | `/en/` | Sí |
| Servicios | `/servicios/` | `/en/services/` | Sí |
| Contabilidad | `/servicios/contabilidad-monterrey/` | `/en/services/accounting-monterrey/` | Sí |
| Asesoría fiscal | `/servicios/asesoria-fiscal-monterrey/` | `/en/services/tax-advisory-monterrey/` | Sí |
| Auditoría | `/servicios/auditoria-monterrey/` | `/en/services/audit-monterrey/` | Sí |
| Consultoría | `/servicios/consultoria-negocios-monterrey/` | `/en/services/business-consulting-monterrey/` | Sí |
| Servicios administrativos | `/servicios/servicios-administrativos-monterrey/` | `/en/services/administrative-services-monterrey/` | Sí |
| Nosotros | `/nosotros/` | `/en/about/` | Sí |
| Equipo | `/equipo/` | `/en/team/` | Sí |
| Perspectivas | `/perspectivas/` | `/en/insights/` | Sí |
| Artículo | `/perspectivas/{slug}/` | `/en/insights/{slug}/` | Sí, si publicado |
| Contacto | `/contacto/` | `/en/contact/` | Sí |
| LP Contabilidad | `/lp/contabilidad/` | `/en/lp/accounting/` | noindex,follow |
| LP Fiscal | `/lp/asesoria-fiscal/` | `/en/lp/tax-advisory/` | noindex,follow |
| LP Auditoría | `/lp/auditoria/` | `/en/lp/audit/` | noindex,follow |
| Aviso de privacidad | `/aviso-de-privacidad/` | `/en/privacy-notice/` | Sí; texto legal pendiente |
| Cookies | `/politica-de-cookies/` | `/en/cookie-policy/` | Sí; texto legal pendiente |
| Bolsa de trabajo | `/trabajo/` | `/en/careers/` | Sí cuando tenga contenido útil |

Navegación de escritorio: Inicio, Servicios, Nosotros, Equipo, Perspectivas, Contacto, selector ES/EN y CTA. Móvil: menú accesible y CTA claro. Bolsa de trabajo, privacidad y cookies solo en footer. Las LP llevan logo, selector de idioma equivalente y enlaces legales; no menú de navegación. No crear páginas vacías: estado editorial [PENDIENTE] fuera del sitemap y fuera de producción hasta completar contenido.

## Reglas de redirección y enlaces

- `/blog/` → 301 `/perspectivas/` al migrar el archivo, conservando la paginación con correspondencias reales.
- `/trabajo` → 301 `/trabajo/` si se adopta barra final.
- Inicio, Servicios, Nosotros, Equipo y Contacto conservan sus rutas españolas existentes.
- Artículos: mantener slug cuando tenga tráfico/enlaces; si se mueve bajo `/perspectivas/`, redirección individual desde su URL antigua a su equivalente, nunca todas al home.
- No inventar redirecciones EN: inventariar primero los slugs históricos reales.
- Sitemap solo con URLs canónicas, indexables, publicadas y estado 200. Las LP no se bloquean en robots: Google necesita leer `noindex`.
- Hreflang recíproco `es-MX` y `en-US`, autorreferencia en cada idioma; `x-default` opcional hacia la versión española equivalente. No enviar todos los alternates al home.
- Breadcrumb: Inicio → Servicios → Servicio; Inicio → Perspectivas → Artículo. Cards relacionadas: contabilidad↔fiscal, auditoría↔consultoría, administración↔contabilidad. Cada artículo enlaza al servicio pertinente y cada servicio a 1–2 artículos útiles.

## Metas de páginas de apoyo

| Página | Meta title | Meta description |
|---|---|---|
| Servicios ES | Servicios empresariales · González Armendáriz | Contabilidad, asesoría fiscal, auditoría y apoyo administrativo para su empresa. Conozca nuestros servicios y agende una consulta. |
| Services EN | Business Services · González Armendáriz | Accounting, tax advisory, audit and administrative support for your business in Monterrey. Explore our services and book a consultation. |
| Perspectivas ES | Perspectivas para empresas · González Armendáriz | Guías de contabilidad, fiscalidad, auditoría y administración para empresas. Consulte nuestros artículos y agende una consulta. |
| Insights EN | Business Insights · González Armendáriz | Practical insights on Mexican business accounting, tax, audit and administration. Explore our guides and book a consultation. |

Los separadores verticales en los titles se entienden como parte literal del título; el documento de metas consolidado los reproduce escapados cuando sea necesario.

URLs inglesas históricas observadas en enlaces del home: `/en/about-us/` y `/en/blog-2/`. Sus correspondencias propuestas son `/en/about/` y `/en/insights/`. Confirmar200 y contenido, migrar y aplicar301 únicamente al publicar los destinos; ver `deployment-templates/redirecciones-propuestas.csv`.
