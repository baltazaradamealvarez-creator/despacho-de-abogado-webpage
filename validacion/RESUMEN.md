# Validación de la entrega

Fecha: 6 de octubre de 2026. Las cifras siguientes proceden de herramientas ejecutadas sobre el código entregado, servido localmente. No son mediciones del WordPress actual ni del futuro hosting público.

## Comprobaciones

- Copy: 56 campos de metadatos de 28 páginas revisados, dentro de 60/155 caracteres. Las 10 versiones ES/EN de páginas de servicio tienen 300–600 palabras de cuerpo; evidencia en entregables/validacion-copy.json.
- Google Ads: 36 RSA completos, 18 ES/18 EN, tres por grupo. Cada pieza tiene 15 títulos y 4 descripciones; máximos observados 28 y 88 caracteres. CSV y JSON equivalentes; sin campañas publicadas.
- Código: 8 rutas (2 homes y 6 landings) revisadas a 320, 390, 768 y 1440 px: 32 vistas sin desbordamiento horizontal, errores JS ni solicitudes a terceros al cargar. Un H1, cuatro campos, metadatos válidos, zoom habilitado y FAQ HTML/JSON-LD coincidentes en cada ruta.
- Contacto: apertura de WhatsApp con datos de prueba mediante un stub local; no se envió ningún mensaje. Enlace alternativo disponible. Handoff secundario; ningún generate_lead ni PII en dataLayer. Sin Google / Meta / LinkedIn activos.
- Navegación: menú móvil, acordeones de FAQ y región de estado funcionan. Escape cierra el menú y devuelve foco; diálogo de cookies usa foco/modal nativos. El mapa no crea iframe antes del clic; la prueba bloqueó la petición externa al abrirlo.
- Accesibilidad automática: axe-core sobre 7 configuraciones representativas (home/LP, ES/EN, móvil/escritorio y banner activo) no detectó infracciones WCAG 2.0 y 2.1, niveles A y AA ni best-practice dentro de su alcance. No equivale a certificación AA ni sustituye lector de pantalla, zoom/manual y revisión de todos los estados.
- Consentimiento: analítica puede aceptarse sin publicidad; guardar cierra el diálogo/oculta banner. Rechazo mantiene guardas apagadas. No hay carga de etiquetas por este código. También se comprobó rechazo, persistencia al recargar y revocación de analítica. Versión del aviso e integración CMP/GTM pendientes.
- Datos estructurados: 28 grafos ES/EN y 2 plantillas de artículo con sintaxis válida. FAQ sincronizadas. Horario y geo desconocidos omitidos. La sintaxis no demuestra elegibilidad para rich results ni posiciones.

## Lighthouse móvil local

| Página | Rendimiento | Accesibilidad automática | Buenas prácticas | LCP laboratorio | CLS laboratorio | TBT |
|---|---:|---:|---:|---:|---:|---:|
| Home ES | 98 | 100 | 100 | 1.88 s | 0 | 19 ms |
| LP Contabilidad ES | 100 | 100 | 100 | 1.66 s | 0.0065 | 0 ms |

Home obtiene 100 en la categoría SEO de Lighthouse; esto comprueba reglas técnicas limitadas y no rankings. La LP noindex se excluyó intencionalmente de esa categoría. Configuración móvil/simulated throttling predeterminada de Lighthouse, servidor HTTP local, sin plugins WordPress ni publicidad. Los resultados completos, versión y entorno están en lighthouse-*.json. Variarán en servidor público, conexiones reales y con etiquetas.

INP de campo no se midió; TBT no lo reemplaza. Core Web Vitals finales requieren datos de usuarios al percentil 75 y muestra suficiente en hosting real. No se afirma que la firma tenga actualmente PageSpeed 90+.

## Pendientes que impiden un lanzamiento productivo completo

Publicar las páginas interiores y los documentos legales con destinos 200; confirmar pin, horarios/correo y permisos de fotos; aprobar alcances y valores; validar perfiles/certificaciones si se usan; definir recepción/CRM y agenda con un socio; instalar cuentas/tags/CMP sin PII y comprobar entrega real; aplicar redirecciones solo cuando existan equivalentes. Sitemap y robots incluidos son plantillas, no se aplicaron al dominio.

No se modificó el WordPress público, no se activaron campañas, no se publicaron cambios en GitHub ni se enviaron mensajes.
