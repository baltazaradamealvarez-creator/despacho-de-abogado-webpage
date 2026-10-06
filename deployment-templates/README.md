# Plantillas de publicación: no aplicar antes de completar la migración

El sitemap propuesto contiene las 22 URLs orgánicas ES/EN de la arquitectura. No es un inventario de páginas HTML implementadas en este paquete: el código pedido corresponde al home y landings. Publicar cada ruta y validar200/indexable antes de incluirla en el sitemap real. No contiene LP noindex, artículos nuevos inexistentes ni documentos legales todavía pendientes. No usa lastmod ficticio.

En WordPress conservar el índice Yoast, ajustando sus URLs; elegir robots-wordpress.txt. Para un front estático completo, usar robots-estatico.txt y generar sitemap.xml con las rutas realmente implementadas. Son alternativas, no dos sitemaps que deban instalarse simultáneamente.

El CSV contiene decisiones propuestas, no reglas ejecutadas. Las rutas inglesas antiguas se observaron en enlaces reales del home; confirmar estado y contenido de cada destino. Los artículos conservan sus slugs salvo justificación de Search Console; las decisiones individuales están en entregable10. No enviar todos los artículos al home ni aplicar301 a equivalentes que todavía no existen.
