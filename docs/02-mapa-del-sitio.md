# 2. Mapa del sitio con URLs finales

Dominio canónico: `https://gonzalezarmendariz.com` (sin `www`, con HTTPS y barra final). [SUPUESTO] Confirmar cuál es la versión que hoy indexa Google; la otra se redirige con 301.

## 2.1 Árbol

```
ES (es-MX)                                              EN (en-US)
/                                                       /en/
├── /servicios/                                         ├── /en/services/
│   ├── /servicios/contabilidad-empresas-monterrey/     │   ├── /en/services/accounting-monterrey/
│   ├── /servicios/asesoria-fiscal-monterrey/           │   ├── /en/services/tax-advisory-monterrey/
│   ├── /servicios/auditoria-monterrey/                 │   ├── /en/services/audit-monterrey/
│   ├── /servicios/consultoria-de-negocios-monterrey/   │   ├── /en/services/business-consulting-monterrey/
│   └── /servicios/outsourcing-administrativo-monterrey/│   └── /en/services/administrative-outsourcing-monterrey/
├── /nosotros/                                          ├── /en/about/
├── /equipo/                                            ├── /en/team/
├── /perspectivas/                                      ├── /en/insights/
│   ├── /perspectivas/tema/obligaciones-fiscales/       │   └── /en/insights/<slug>/
│   ├── /perspectivas/tema/auditoria-y-control/
│   ├── /perspectivas/tema/planeacion-financiera/
│   ├── /perspectivas/tema/administracion-y-nomina/
│   └── /perspectivas/<slug-del-articulo>/
├── /contacto/                                          ├── /en/contact/
├── /bolsa-de-trabajo/        (solo enlazada en footer) ├── /en/careers/
├── /aviso-de-privacidad/     (incluye #cookies)        ├── /en/privacy-notice/
└── /gracias/                 (noindex)                 └── /en/thank-you/  (noindex)

Landing pages de publicidad (noindex, fuera del sitemap y del menú)
/lp/contabilidad-empresas/
/lp/asesoria-fiscal/
/lp/auditoria/
```

## 2.2 Reglas de URL
- Minúsculas, sin acentos ni `ñ`, palabras separadas con guiones, sin fechas ni IDs.
- Los artículos del blog usan `/perspectivas/<slug>/` sin categoría en la URL, para poder cambiar de tema sin romper enlaces.
- Los temas del blog se muestran como páginas de archivo (`/perspectivas/tema/...`). Si tienen menos de 4 artículos, llevan `noindex, follow` hasta crecer.
- Las páginas de etiquetas, autor, fecha y adjuntos de WordPress llevan `noindex` o se desactivan.

## 2.3 Menú principal
`Servicios ▾ · Nosotros · Equipo · Perspectivas · Contacto · EN · [Agendar una consulta]`
Teléfono visible en escritorio; ícono de llamada en móvil.

El submenú de Servicios muestra los 5 servicios. En móvil se abre como lista simple, sin mega menú.

## 2.4 Footer
Servicios (5) · La firma (Nosotros, Equipo, Perspectivas, Contacto, **Bolsa de trabajo**) · Legal (Aviso de privacidad, Cookies, English) · NAP completo · © año en curso.

## 2.5 Redirecciones 301 (sitio actual → nuevo)

No pude rastrear el sitio actual: la red de este entorno bloquea `gonzalezarmendariz.com`. **[PENDIENTE]** Exportar todas las URLs actuales con Screaming Frog (o desde Search Console → Páginas, más Google Analytics → páginas con tráfico en los últimos 16 meses) y completar esta tabla. Ninguna URL con tráfico o con enlaces externos puede terminar en 404.

| URL actual (ejemplos a confirmar) | URL nueva | Tipo |
|---|---|---|
| `/beta/index.php/nota01/` (aparece indexada en buscadores: "Aguinaldo 2015") | `/perspectivas/aguinaldo-calculo-y-fecha-limite/` | 301 |
| `/beta/*` (instalación de prueba indexada) | Página equivalente o `/` | 301 + borrar la instalación |
| `/servicios/` o `/nuestros-servicios/` [confirmar] | `/servicios/` | 301 si cambia |
| `/contabilidad/` [confirmar] | `/servicios/contabilidad-empresas-monterrey/` | 301 |
| `/auditoria/` [confirmar] | `/servicios/auditoria-monterrey/` | 301 |
| `/asesoria-fiscal/` [confirmar] | `/servicios/asesoria-fiscal-monterrey/` | 301 |
| `/consultoria/` [confirmar] | `/servicios/consultoria-de-negocios-monterrey/` | 301 |
| `/servicios-administrativos/` [confirmar] | `/servicios/outsourcing-administrativo-monterrey/` | 301 |
| `/quienes-somos/` o `/nosotros/` [confirmar] | `/nosotros/` | 301 si cambia |
| `/blog/<slug>/` o `/noticias/<slug>/` [confirmar] | `/perspectivas/<slug>/` | 301 uno a uno |
| `/newsletter/` [confirmar] | `/perspectivas/` | 301 |
| `/en/...` versión inglés actual [confirmar] | `/en/...` nueva | 301 uno a uno |
| `http://` y `www.` | `https://gonzalezarmendariz.com/...` | 301 a nivel servidor |

Reglas:
- Una sola redirección (sin cadenas A→B→C).
- No redirigir todo al home: cada URL va a su equivalente más cercano.
- Artículos sin valor y sin tráfico ni enlaces: `410 Gone`.
- Revisar en Search Console el informe "Páginas" 2 y 6 semanas después del lanzamiento.

Ejemplo de reglas para Apache en `site/.htaccess`; en WordPress se recomienda el plugin **Redirection** o el gestor de redirecciones de Rank Math.
