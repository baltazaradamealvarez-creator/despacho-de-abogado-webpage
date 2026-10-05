# 8. Datos estructurados JSON-LD (listos para pegar)

Cómo usarlos:
- Pegar cada bloque dentro de `<script type="application/ld+json"> … </script>` en el `<head>`.
- El bloque **A (Organización + WebSite)** va en **todas** las páginas. Los demás se agregan según el tipo de página. Todos se conectan por `@id`, así Google entiende que es una sola firma.
- En WordPress: Rank Math o Yoast generan Organization/WebSite/BreadcrumbList. Para no duplicar, desactive su esquema de "Organización" y use el bloque A tal cual, o configure el plugin con estos mismos datos (tipo `AccountingService`).
- Validar cada plantilla en https://search.google.com/test/rich-results y https://validator.schema.org antes de publicar.
- Todos los bloques de este documento se validaron como JSON correcto.

Datos a confirmar antes de publicar:
- `geo`: [VERIFICAR] las coordenadas son aproximadas; copie las exactas del pin de su ficha de Google Business Profile.
- `openingHoursSpecification`: [SUPUESTO] lunes a viernes de 9:00 a 18:00.
- `sameAs`: [PENDIENTE] URLs reales de LinkedIn, Facebook, etc.
- `logo`: [PENDIENTE] PNG cuadrado de al menos 112×112 px.
- `email`: [PENDIENTE] agréguelo al bloque A cuando lo tenga (`"email": "…"`).

> Nota honesta sobre FAQ: desde 2023, Google muestra resultados enriquecidos de FAQ casi solo para sitios gubernamentales y de salud. Aun así, `FAQPage` conviene: ayuda a que buscadores y asistentes de IA (AI Overviews, ChatGPT, Perplexity, Copilot) entiendan y citen sus respuestas. El texto debe ser idéntico al visible en la página.

---

## A. Organización + WebSite: todas las páginas (ES y EN)

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "AccountingService",
      "@id": "https://gonzalezarmendariz.com/#organizacion",
      "name": "González Armendáriz",
      "legalName": "González Armendáriz, S.C.",
      "alternateName": "González Armendáriz Contadores",
      "url": "https://gonzalezarmendariz.com/",
      "logo": "https://gonzalezarmendariz.com/assets/img/logo-gonzalez-armendariz.png",
      "image": "https://gonzalezarmendariz.com/assets/img/og-gonzalez-armendariz.jpg",
      "description": "Firma de contabilidad, asesoría fiscal, auditoría, consultoría de negocios y servicios administrativos para empresas en Monterrey y su área metropolitana.",
      "telephone": "+52-81-8363-4412",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "Av. Lázaro Cárdenas 2400 Pte., Edificio Losoles, Int. PB 18, Col. Residencial San Agustín",
        "addressLocality": "San Pedro Garza García",
        "addressRegion": "N.L.",
        "postalCode": "66260",
        "addressCountry": "MX"
      },
      "geo": { "@type": "GeoCoordinates", "latitude": 25.6517, "longitude": -100.3557 },
      "hasMap": "https://www.google.com/maps/search/?api=1&query=Gonz%C3%A1lez%20Armend%C3%A1riz%20Av.%20L%C3%A1zaro%20C%C3%A1rdenas%202400%20Pte%20San%20Pedro%20Garza%20Garc%C3%ADa",
      "openingHoursSpecification": [
        {
          "@type": "OpeningHoursSpecification",
          "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
          "opens": "09:00",
          "closes": "18:00"
        }
      ],
      "contactPoint": [
        { "@type": "ContactPoint", "telephone": "+52-81-8363-4412", "contactType": "customer service", "areaServed": "MX", "availableLanguage": ["Spanish", "English"] },
        { "@type": "ContactPoint", "telephone": "+52-81-8363-0502", "contactType": "customer service", "areaServed": "MX" },
        { "@type": "ContactPoint", "telephone": "+52-81-8363-4260", "contactType": "customer service", "areaServed": "MX" },
        { "@type": "ContactPoint", "telephone": "+52-81-2884-5949", "contactType": "sales", "contactOption": "https://wa.me/528128845949", "areaServed": "MX" }
      ],
      "areaServed": [
        { "@type": "City", "name": "Monterrey" },
        { "@type": "City", "name": "San Pedro Garza García" },
        { "@type": "City", "name": "San Nicolás de los Garza" },
        { "@type": "City", "name": "Guadalupe" },
        { "@type": "City", "name": "Santa Catarina" },
        { "@type": "City", "name": "Apodaca" },
        { "@type": "State", "name": "Nuevo León" }
      ],
      "numberOfEmployees": { "@type": "QuantitativeValue", "value": 30 },
      "knowsLanguage": ["es", "en"],
      "founder": { "@id": "https://gonzalezarmendariz.com/#alejandro-gonzalez" },
      "sameAs": [
        "https://www.linkedin.com/company/PENDIENTE",
        "https://www.facebook.com/PENDIENTE"
      ],
      "hasOfferCatalog": {
        "@type": "OfferCatalog",
        "name": "Servicios",
        "itemListElement": [
          { "@type": "Offer", "itemOffered": { "@id": "https://gonzalezarmendariz.com/servicios/contabilidad-empresas-monterrey/#servicio" } },
          { "@type": "Offer", "itemOffered": { "@id": "https://gonzalezarmendariz.com/servicios/asesoria-fiscal-monterrey/#servicio" } },
          { "@type": "Offer", "itemOffered": { "@id": "https://gonzalezarmendariz.com/servicios/auditoria-monterrey/#servicio" } },
          { "@type": "Offer", "itemOffered": { "@id": "https://gonzalezarmendariz.com/servicios/consultoria-de-negocios-monterrey/#servicio" } },
          { "@type": "Offer", "itemOffered": { "@id": "https://gonzalezarmendariz.com/servicios/outsourcing-administrativo-monterrey/#servicio" } }
        ]
      }
    },
    {
      "@type": "WebSite",
      "@id": "https://gonzalezarmendariz.com/#website",
      "url": "https://gonzalezarmendariz.com/",
      "name": "González Armendáriz",
      "inLanguage": ["es-MX", "en-US"],
      "publisher": { "@id": "https://gonzalezarmendariz.com/#organizacion" }
    }
  ]
}
```
> Quite `sameAs` si todavía no tiene las URLs: no publique valores `PENDIENTE`.

---

## B. Persona: fundador (en Inicio y Nosotros)

```json
{
  "@context": "https://schema.org",
  "@type": "Person",
  "@id": "https://gonzalezarmendariz.com/#alejandro-gonzalez",
  "name": "Alejandro González",
  "jobTitle": "Director Fundador",
  "worksFor": { "@id": "https://gonzalezarmendariz.com/#organizacion" },
  "url": "https://gonzalezarmendariz.com/nosotros/",
  "image": "https://gonzalezarmendariz.com/assets/img/alejandro-gonzalez-director-fundador.webp",
  "knowsAbout": ["Contabilidad", "Impuestos en México", "Auditoría", "Planeación fiscal"],
  "sameAs": ["https://www.linkedin.com/in/PENDIENTE"]
}
```
[PENDIENTE] Agregar `alumniOf` y `hasCredential` solo con datos reales (universidad, certificación).

---

## C. Página de servicio (plantilla con Contabilidad)

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebPage",
      "@id": "https://gonzalezarmendariz.com/servicios/contabilidad-empresas-monterrey/#webpage",
      "url": "https://gonzalezarmendariz.com/servicios/contabilidad-empresas-monterrey/",
      "name": "Contabilidad para empresas en Monterrey y San Pedro",
      "inLanguage": "es-MX",
      "isPartOf": { "@id": "https://gonzalezarmendariz.com/#website" },
      "about": { "@id": "https://gonzalezarmendariz.com/servicios/contabilidad-empresas-monterrey/#servicio" },
      "breadcrumb": { "@id": "https://gonzalezarmendariz.com/servicios/contabilidad-empresas-monterrey/#breadcrumb" }
    },
    {
      "@type": "Service",
      "@id": "https://gonzalezarmendariz.com/servicios/contabilidad-empresas-monterrey/#servicio",
      "name": "Contabilidad y Cumplimiento Fiscal",
      "serviceType": "Contabilidad para empresas",
      "description": "Registro contable mensual, estados financieros, cálculo y presentación de impuestos, contabilidad electrónica y atención de requerimientos del SAT para empresas en Monterrey.",
      "url": "https://gonzalezarmendariz.com/servicios/contabilidad-empresas-monterrey/",
      "provider": { "@id": "https://gonzalezarmendariz.com/#organizacion" },
      "areaServed": [
        { "@type": "City", "name": "Monterrey" },
        { "@type": "City", "name": "San Pedro Garza García" },
        { "@type": "State", "name": "Nuevo León" }
      ],
      "audience": { "@type": "BusinessAudience", "audienceType": "Pequeñas y medianas empresas" }
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://gonzalezarmendariz.com/servicios/contabilidad-empresas-monterrey/#breadcrumb",
      "itemListElement": [
        { "@type": "ListItem", "position": 1, "name": "Inicio", "item": "https://gonzalezarmendariz.com/" },
        { "@type": "ListItem", "position": 2, "name": "Servicios", "item": "https://gonzalezarmendariz.com/servicios/" },
        { "@type": "ListItem", "position": 3, "name": "Contabilidad", "item": "https://gonzalezarmendariz.com/servicios/contabilidad-empresas-monterrey/" }
      ]
    },
    {
      "@type": "FAQPage",
      "@id": "https://gonzalezarmendariz.com/servicios/contabilidad-empresas-monterrey/#faq",
      "inLanguage": "es-MX",
      "mainEntity": [
        { "@type": "Question", "name": "¿Qué necesito para cambiar de contador?", "acceptedAnswer": { "@type": "Answer", "text": "Acceso a su información del SAT, sus declaraciones y la contabilidad de los últimos ejercicios. Nosotros coordinamos la entrega con su contador anterior." } },
        { "@type": "Question", "name": "¿Cada cuánto recibo información de mi empresa?", "acceptedAnswer": { "@type": "Answer", "text": "Cada mes recibe sus estados financieros y el resumen de impuestos, con una explicación clara de los números." } },
        { "@type": "Question", "name": "¿Qué pasa si me llega una carta o un requerimiento del SAT?", "acceptedAnswer": { "@type": "Answer", "text": "Lo revisamos con usted, preparamos la respuesta y la presentamos dentro del plazo." } },
        { "@type": "Question", "name": "¿Pueden ponerme al corriente con declaraciones atrasadas?", "acceptedAnswer": { "@type": "Answer", "text": "Sí. Revisamos qué falta, calculamos el impacto y presentamos lo pendiente con un plan claro, buscando reducir recargos y multas dentro de lo que permite la ley." } }
      ]
    }
  ]
}
```

**Valores para las otras 4 páginas** (cambie URL, `name`, `serviceType`, `description`, la miga 3 y las preguntas de `04-copy-paginas-es.md`):

| Página | `name` | `serviceType` | Miga 3 |
|---|---|---|---|
| `/servicios/asesoria-fiscal-monterrey/` | Asesoría Fiscal | Asesoría fiscal para empresas | Asesoría Fiscal |
| `/servicios/auditoria-monterrey/` | Auditoría | Auditoría de estados financieros | Auditoría |
| `/servicios/consultoria-de-negocios-monterrey/` | Consultoría de Negocios | Consultoría financiera y de negocios | Consultoría de Negocios |
| `/servicios/outsourcing-administrativo-monterrey/` | Servicios Administrativos | Outsourcing administrativo | Servicios Administrativos |

---

## D. Nosotros

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "AboutPage",
      "@id": "https://gonzalezarmendariz.com/nosotros/#webpage",
      "url": "https://gonzalezarmendariz.com/nosotros/",
      "name": "Nosotros: 28 años de trayectoria",
      "inLanguage": "es-MX",
      "isPartOf": { "@id": "https://gonzalezarmendariz.com/#website" },
      "about": { "@id": "https://gonzalezarmendariz.com/#organizacion" },
      "mainEntity": { "@id": "https://gonzalezarmendariz.com/#organizacion" }
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        { "@type": "ListItem", "position": 1, "name": "Inicio", "item": "https://gonzalezarmendariz.com/" },
        { "@type": "ListItem", "position": 2, "name": "Nosotros", "item": "https://gonzalezarmendariz.com/nosotros/" }
      ]
    }
  ]
}
```
(+ bloque B de la persona)

---

## E. Equipo

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "CollectionPage",
      "@id": "https://gonzalezarmendariz.com/equipo/#webpage",
      "url": "https://gonzalezarmendariz.com/equipo/",
      "name": "Equipo de contadores y auditores",
      "inLanguage": "es-MX",
      "isPartOf": { "@id": "https://gonzalezarmendariz.com/#website" },
      "about": { "@id": "https://gonzalezarmendariz.com/#organizacion" },
      "mainEntity": {
        "@type": "ItemList",
        "itemListElement": [
          { "@type": "ListItem", "position": 1, "item": { "@id": "https://gonzalezarmendariz.com/#alejandro-gonzalez" } }
        ]
      }
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        { "@type": "ListItem", "position": 1, "name": "Inicio", "item": "https://gonzalezarmendariz.com/" },
        { "@type": "ListItem", "position": 2, "name": "Equipo", "item": "https://gonzalezarmendariz.com/equipo/" }
      ]
    }
  ]
}
```
[PENDIENTE] Agregar un `ListItem` con un `Person` por cada socio o gerente publicado.

---

## F. Contacto

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "ContactPage",
      "@id": "https://gonzalezarmendariz.com/contacto/#webpage",
      "url": "https://gonzalezarmendariz.com/contacto/",
      "name": "Contacto: despacho contable en San Pedro Garza García",
      "inLanguage": "es-MX",
      "isPartOf": { "@id": "https://gonzalezarmendariz.com/#website" },
      "about": { "@id": "https://gonzalezarmendariz.com/#organizacion" },
      "mainEntity": { "@id": "https://gonzalezarmendariz.com/#organizacion" }
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        { "@type": "ListItem", "position": 1, "name": "Inicio", "item": "https://gonzalezarmendariz.com/" },
        { "@type": "ListItem", "position": 2, "name": "Contacto", "item": "https://gonzalezarmendariz.com/contacto/" }
      ]
    }
  ]
}
```

---

## G. Artículo del blog (Perspectivas)

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "BlogPosting",
      "@id": "https://gonzalezarmendariz.com/perspectivas/declaracion-anual-personas-morales/#articulo",
      "mainEntityOfPage": "https://gonzalezarmendariz.com/perspectivas/declaracion-anual-personas-morales/",
      "headline": "Declaración anual de personas morales: qué revisar antes del 31 de marzo",
      "description": "Lista de revisión para directores antes de presentar la declaración anual de su empresa.",
      "image": "https://gonzalezarmendariz.com/assets/img/perspectivas/declaracion-anual-1200x630.jpg",
      "datePublished": "2027-02-15",
      "dateModified": "2027-02-15",
      "inLanguage": "es-MX",
      "author": { "@id": "https://gonzalezarmendariz.com/#alejandro-gonzalez" },
      "publisher": { "@id": "https://gonzalezarmendariz.com/#organizacion" },
      "isPartOf": { "@id": "https://gonzalezarmendariz.com/#website" },
      "articleSection": "Obligaciones fiscales"
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        { "@type": "ListItem", "position": 1, "name": "Inicio", "item": "https://gonzalezarmendariz.com/" },
        { "@type": "ListItem", "position": 2, "name": "Perspectivas", "item": "https://gonzalezarmendariz.com/perspectivas/" },
        { "@type": "ListItem", "position": 3, "name": "Declaración anual de personas morales", "item": "https://gonzalezarmendariz.com/perspectivas/declaracion-anual-personas-morales/" }
      ]
    }
  ]
}
```
Agregue un `FAQPage` si el artículo termina con preguntas frecuentes (ver plantilla en `10-blog-perspectivas.md`). El autor debe ser una persona real del equipo con su página o perfil: eso refuerza la autoridad (E-E-A-T) en temas fiscales.

---

## H. Versión en inglés

Mismos bloques con estos cambios:
- `@id` y `url` de la página bajo `/en/` (p. ej. `https://gonzalezarmendariz.com/en/services/accounting-monterrey/#webpage`).
- `"inLanguage": "en-US"`; nombres y descripciones en inglés.
- La organización **no se duplica**: siempre se referencia `https://gonzalezarmendariz.com/#organizacion`.
- `BreadcrumbList`: Home › Services › Accounting.

## I. Landing pages
Son `noindex`: basta con `Service` + `FAQPage` (ya incluidos en `site/lp/contabilidad-empresas/index.html`).
