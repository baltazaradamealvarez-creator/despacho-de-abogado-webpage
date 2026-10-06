# González Armendáriz: rediseño web, SEO y publicidad

Propuesta completa para el nuevo sitio de **González Armendáriz** (gonzalezarmendariz.com), firma de contabilidad, auditoría y asesoría fiscal corporativa en San Pedro Garza García, Nuevo León.

Objetivos: (a) verse como una firma sólida, discreta y confiable; (b) posicionar en búsquedas locales de contabilidad, auditoría y asesoría fiscal; (c) convertir el tráfico pagado en citas con un socio.

## Entregables

| # | Entregable | Archivo |
|---|---|---|
| 1 | Tabla de keywords por página (ES/EN) | [docs/01-keywords.md](docs/01-keywords.md) |
| 2 | Mapa del sitio con URLs finales y plan de redirecciones | [docs/02-mapa-del-sitio.md](docs/02-mapa-del-sitio.md) |
| 3 | Copy del home ES + EN con metas | [docs/03-copy-home.md](docs/03-copy-home.md) |
| 4 | Copy de servicios (5), Servicios, Nosotros, Equipo, Contacto, con metas | [docs/04-copy-paginas-es.md](docs/04-copy-paginas-es.md) · [docs/04b-copy-paginas-en.md](docs/04b-copy-paginas-en.md) |
| 5 | Copy de 3 landing pages | [docs/05-landing-pages.md](docs/05-landing-pages.md) |
| 6 | Wireframes en texto | [docs/06-wireframes.md](docs/06-wireframes.md) |
| 7 | Guía de estilo (HEX, tipografías, botones) | [docs/07-guia-de-estilo.md](docs/07-guia-de-estilo.md) |
| 8 | JSON-LD listo para pegar | [docs/08-json-ld.md](docs/08-json-ld.md) |
| 9 | Google Business Profile y directorios | [docs/09-google-business-profile-y-directorios.md](docs/09-google-business-profile-y-directorios.md) |
| 10 | Blog: pilares, calendario de 12 artículos, plantilla y revisión | [docs/10-blog-perspectivas.md](docs/10-blog-perspectivas.md) |
| 11 | Google Ads: estructura, keywords, negativas, 27 anuncios | [docs/11-google-ads.md](docs/11-google-ads.md) · CSV para Google Ads Editor en [ads/](ads/) |
| 12 | Conceptos para Meta y LinkedIn | [docs/12-meta-y-linkedin.md](docs/12-meta-y-linkedin.md) |
| 13 | Plan de medición (eventos, UTMs, etiquetas, privacidad) | [docs/13-plan-de-medicion.md](docs/13-plan-de-medicion.md) |
| 14 | Código HTML/CSS del home y una landing | [docs/14-codigo-html-css.md](docs/14-codigo-html-css.md) · [site/](site/) |
| 15 | Checklist de lanzamiento | [docs/15-checklist-lanzamiento.md](docs/15-checklist-lanzamiento.md) |

Ver el sitio en local: `cd site && npx http-server -p 8080` → http://localhost:8080/

Regenerar anuncios y CSV de Google Ads: `python3 ads/generar_google_ads.py` (valida 30/90 caracteres).

## Fuentes de datos
- Datos de la firma: los proporcionados en el brief (28+ años, 400+ empresas, 30 colaboradores, servicios, fundador, dirección, teléfonos, WhatsApp).
- **El sitio actual no se pudo rastrear**: la red del entorno de trabajo bloquea `gonzalezarmendariz.com` y `web.archive.org`. Se usaron buscadores y directorios públicos, que mostraron:
  - una página de prueba indexada: `/beta/index.php/nota01/` ("Aguinaldo 2015");
  - tres nombres distintos para la firma en directorios (sin acento en Cosmos; "Asesoría Contable y Fiscal González Armendáriz" en ZoomInfo; "González Armendáriz Consultoría Contable y Fiscal" en RocketReach);
  - un directorio que indica "establecida en julio de 2010", lo que contradice los 28+ años.
  Antes de lanzar hay que rastrear el sitio actual para completar las redirecciones 301 y la revisión del blog.

## Supuestos principales [SUPUESTO]
1. Dominio canónico `https://gonzalezarmendariz.com` sin `www`.
2. Razón social "González Armendáriz, S.C." (tomada de directorios).
3. Horario lunes a viernes de 9:00 a 18:00 (solo en JSON-LD y Google Ads; confirmar).
4. La primera reunión es con un socio y puede ser presencial o en línea.
5. Atención en español e inglés (el sitio es bilingüe).
6. Alcance de Consultoría de Negocios y de RH en Servicios Administrativos inferido de los nombres de servicio.
7. Honorarios de contabilidad fijos mensuales; reporte mensual al cliente.
8. Consent Mode: en México, medición activa con opción de rechazo; en Europa, denegada por defecto.
9. Calendario editorial de noviembre de 2026 a octubre de 2027.
10. Reparto de presupuesto de Google Ads 45/30/25 entre Contabilidad, Asesoría Fiscal y Auditoría.

## Pendientes de la firma [PENDIENTE]
Correo de contacto · horario · tiempo de respuesta a solicitudes · si la primera consulta tiene costo · logotipo vectorial · foto del fundador y del equipo · semblanza del fundador · socios y gerentes · año de fundación e hitos · afiliaciones y certificaciones (Colegio de Contadores, IMCP, etc.) · testimonios y logos de clientes con autorización · si hacen dictamen fiscal/IMSS, due diligence o precios de transferencia · sistemas contables que manejan · registro REPSE (si aplica) · URLs de LinkedIn y Facebook · coordenadas exactas de GBP · presupuesto de publicidad · CRM · URLs actuales para redirecciones · exportación del blog actual.
