# 08. Datos estructurados y metadatos técnicos

Los archivos de `schemas/` contienen JSON válido listo para insertar dentro de `<script type="application/ld+json">…</script>` en su URL correspondiente. `manifest.json` relaciona cada URL con su archivo; no se inserta el manifest como schema. Hay una versión ES y EN de inicio, índice de servicios, cinco servicios, Nosotros, Equipo, Contacto, Perspectivas y tres landings. El generador `schemas/generar.py` conserva la fuente para actualizar los archivos conjuntamente.

## Entidades y coherencia

- `https://gonzalezarmendariz.com/#organization`: Organization representa a la firma.
- `https://gonzalezarmendariz.com/#office`: AccountingService representa a la oficina local. AccountingService ya es un subtipo de LocalBusiness; no hace falta crear una segunda oficina idéntica.
- `https://gonzalezarmendariz.com/#alejandro-gonzalez`: Person, nombre y cargo de Alejandro González, sin títulos, matrículas ni credenciales no verificados.
- Service usa un ID por página de servicio e idioma, enlazado con `provider` a la oficina. Una landing referencia el servicio orgánico correspondiente, sin inventar una nueva sucursal ni duplicar una ubicación.
- WebPage, CollectionPage, AboutPage y ContactPage identifican el tipo editorial. Las migas estructuradas deben coincidir con las migas visibles; no se incluyen en landings porque estas no tienen navegación.
- FAQPage incluye exclusivamente preguntas/respuestas del copy visible; cambiar HTML y JSON conjuntamente. Las respuestas en acordeón son válidas si el usuario puede acceder a ellas. No reutilizar todo el FAQ de servicios en páginas que no lo muestran.

El teléfono canónico es `+528183634412`; los otros dos teléfonos y WhatsApp permanecen visibles en contacto. La dirección es exactamente la indicada por la firma. No se inventan coordenadas ni horario. [PENDIENTE: latitud/longitud de la oficina confirmadas, openingHoursSpecification real, perfiles sociales oficiales, imagen/logo con URL pública definitiva, correo de contacto y forma jurídica]. Omitir propiedades desconocidas mantiene JSON válido y evita publicar información falsa; completarlas después de verificar los datos. No insertar `[PENDIENTE]` como valor de un dato factual.

Es posible reutilizar estas entidades con IDs estables en todas las páginas. Si WordPress/Yoast/Rank Math ya genera schema, consolidar o desactivar módulos duplicados antes de añadir los archivos. Un único grafo coherente es preferible a dos Organization con nombres o teléfonos distintos.

## Cómo pegar y comprobar

```html
<script type="application/ld+json">
{ "@context": "https://schema.org", "@graph": [] }
</script>
```

Sustituir el objeto del ejemplo por el contenido íntegro del archivo que corresponda, sin anidar otra etiqueta script ni comentar JSON. El código HTML entregado puede incorporar estos datos directamente. Comprobar cada URL con Schema Markup Validator y Rich Results Test, y revisar que el DOM final coincide con el copy. El chequeo de sintaxis JSON de esta entrega no equivale a validación de elegibilidad de Google.

Google limita los resultados enriquecidos FAQ principalmente a sitios gubernamentales y de salud reconocidos. Este despacho no debe esperar dicho resultado por añadir FAQPage. Organization, LocalBusiness, Service y Person ayudan a expresar entidades; no garantizan posiciones ni menciones en respuestas de IA. No crear Review/AggregateRating sin reseñas reales y sin estudiar las restricciones sobre reseñas de la propia organización.

## Plantilla de artículo: completar antes de publicar

`schemas/templates/article-es.json` y `article-en.json` son plantillas de sintaxis válida, expresamente **no publicables sin completar**. Incluyen marcadores solo en campos editoriales, no fechas falsas. Reemplazar slug, título, descripción, autor realmente responsable y fechas ISO reales; añadir imagen autorizada con URL final si existe. Añadir BreadcrumbList y preguntas específicas del artículo únicamente cuando estén visibles. No atribuir todos los artículos al fundador por defecto. La colección Perspectivas publicada no declara artículos todavía inexistentes.

## Hreflang, canonical y social

En cada pareja publicada e indexable, usar URL absoluta y enlaces recíprocos. Ejemplo ES; en EN el canonical cambia a su propia URL y se conserva el mismo conjunto de alternates:

```html
<link rel="canonical" href="https://gonzalezarmendariz.com/servicios/auditoria-monterrey/">
<link rel="alternate" hreflang="es-MX" href="https://gonzalezarmendariz.com/servicios/auditoria-monterrey/">
<link rel="alternate" hreflang="en-US" href="https://gonzalezarmendariz.com/en/services/audit-monterrey/">
<link rel="alternate" hreflang="x-default" href="https://gonzalezarmendariz.com/servicios/auditoria-monterrey/">
<meta name="viewport" content="width=device-width, initial-scale=1">
```

`x-default` es opcional. No usar hreflang hacia traducciones pendientes o redirigidas. Las LP tienen noindex,follow y canonical propio; no necesitan hreflang para posicionarse y no se incluyen en el sitemap orgánico. Puede conservarse selector de idioma para visitantes. No bloquearlas en robots.txt.

Por página: `og:type=website` (article en artículos), `og:title`, `og:description`, `og:url`, `og:locale=es_MX/en_US`, locale alterno, `og:image` absoluto y `og:image:alt`; Twitter `summary_large_image`, title/description/image. Imagen de marca propia 1200×630 [PENDIENTE: URL pública final]. No usar una imagen ficticia como si fuera la oficina. Metas completas de páginas principales en 03–05 y de índices en 02; complemento legal/editorial en `schemas/metadata-apoyo.json`.

## Referencias oficiales

- https://schema.org/Organization
- https://schema.org/AccountingService
- https://schema.org/Service
- https://schema.org/Person
- https://schema.org/FAQPage
- https://schema.org/BreadcrumbList
- https://schema.org/BlogPosting
- https://developers.google.com/search/docs/appearance/structured-data/faqpage
- https://developers.google.com/search/docs/appearance/structured-data/local-business
- https://developers.google.com/search/docs/specialty/international/localized-versions
- https://validator.schema.org/
- https://search.google.com/test/rich-results

Estas referencias orientan la implementación; los objetivos de Core Web Vitals y publicación se comprueban con la checklist 15.
