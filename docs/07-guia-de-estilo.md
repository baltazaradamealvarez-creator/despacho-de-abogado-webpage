# 7. Guía de estilo

Concepto: **"Despacho de consejo"**. Lo que transmite una sala de juntas bien iluminada: poco color, buena tipografía, espacio amplio y detalles en bronce. La sobriedad es lo que hace que la firma se vea cara.

Implementación: tokens en `site/assets/css/main.css` (sección 1).

## 7.1 Color

| Token | HEX | Uso | Contraste verificado (WCAG) |
|---|---|---|---|
| `--navy` | `#0E1B2C` | Fondo institucional: encabezado, hero, liderazgo, footer. Botón primario sobre claro | Texto hueso sobre navy: **15.5:1** |
| `--navy-2` | `#172A44` | Hover y superficies sobre navy | Blanco sobre navy-2: 14.5:1 |
| `--ink` | `#1B1F26` | Texto principal | Sobre blanco 16.5:1 · sobre hueso 14.8:1 |
| `--muted` | `#545B66` | Texto secundario sobre claro | Sobre blanco 6.9:1 · sobre hueso 6.1:1 (AA) |
| `--muted-on-navy` | `#B9C1CC` | Texto secundario sobre navy | 9.5:1 |
| `--bone` | `#F6F2EA` | Fondo cálido alterno ("blanco hueso") | — |
| `--stone` | `#ECE6DA` | Superficie de mapa y bloques neutros | `--muted` sobre stone 5.5:1 |
| `--white` | `#FFFFFF` | Fondo principal y tarjetas | — |
| `--line` | `#DCD4C5` | Bordes y divisores sobre claro | Decorativo |
| `--bronze` | `#9C7A4B` | **Solo** líneas, foco y detalles (no texto pequeño) | 3.5:1 sobre hueso (válido para elementos gráficos) |
| `--bronze-dark` | `#7A5C32` | Texto de acento sobre claro (antetítulos, enlaces "Ver servicio") | 5.5:1 sobre hueso · 6.2:1 sobre blanco (AA) |
| `--gold` | `#C9AE7F` | Acento sobre navy: antetítulos, botón principal sobre navy | Navy sobre gold 8.1:1 · gold sobre navy 8.1:1 |
| `--error` | `#9B2C2C` | Mensajes de error de formulario | 7.5:1 sobre blanco |

Proporción aproximada en cualquier pantalla: **60 % claro (blanco/hueso) · 30 % navy · 10 % bronce/dorado**. El dorado nunca se usa como fondo grande, solo en botones y detalles.

## 7.2 Tipografía (2 familias)

| Rol | Familia | Pesos | Notas |
|---|---|---|---|
| Titulares (H1–H3, cifras, citas) | **Cormorant Garamond** | 500, 600, 500 itálica | Serif clásica, elegante en tamaños grandes. No usar por debajo de 20 px |
| Texto, botones, formularios, navegación | **Inter** | 400, 500, 600 | Legible en móvil, buena para cifras |

Respaldo: `Georgia` para la serif e `Inter-fallback` (Arial ajustada con `size-adjust`) para la sans; reduce el salto visual mientras cargan las fuentes.
Producción: **autoalojar** ambas en `.woff2` con subconjunto latino (≈ 70 KB en total) y `preload` solo de Inter 400 y Cormorant 500.

### Escala (fluida con `clamp`, móvil → escritorio)

| Elemento | Tamaño | Interlineado | Peso |
|---|---|---|---|
| H1 | 38 → 68 px | 1.12 | Cormorant 500 |
| H2 | 30 → 48 px | 1.12 | Cormorant 500 |
| H3 | 22 → 26 px | 1.12 | Cormorant 600 |
| Cita destacada | 26 → 40 px | 1.25 | Cormorant 500 itálica |
| Cifras | 48 → 72 px | 1 | Cormorant 500 |
| Lead / subtítulo | 18 → 21 px | 1.65 | Inter 400 |
| Texto | 17 → 18 px | 1.65 | Inter 400 |
| Pequeño | 15 px | 1.6 | Inter 400 |
| Antetítulo (eyebrow) | 13 px, MAYÚSCULAS, espaciado 0.14 em | — | Inter 600 |

Ancho de línea máximo: 65–75 caracteres (`max-width: 40–46rem`).

## 7.3 Espacio y retícula
- Unidad base 8 px. Secciones: 64 px (móvil) → 120 px (escritorio) de alto de padding.
- Contenedor máximo 1200 px; margen lateral 16 px (móvil) y 32 px (≥768 px).
- Retícula de 12 columnas en escritorio; proporciones usadas: 7/5, 6/5, 5/7 y 3 columnas iguales.
- Puntos de quiebre: 640 · 768 · 896 · 1024 px.

## 7.4 Botones

| Tipo | Fondo | Texto | Borde | Hover | Uso |
|---|---|---|---|---|---|
| Primario sobre claro | `#0E1B2C` | `#F6F2EA` | — | `#172A44` | Enviar formulario |
| Primario sobre navy | `#C9AE7F` | `#0E1B2C` | — | `#D8C29C` | "Agendar una consulta" en hero, encabezado y CTA final |
| Secundario | transparente | hereda | 1 px currentColor | velo dorado 12 % | WhatsApp, "Mostrar mapa" |
| Enlace con flecha | — | `#7A5C32` / `#C9AE7F` | — | flecha se desplaza 4 px | "Ver servicio →" |

- Altura mínima **52 px** (área táctil ≥ 44 px), padding horizontal 28 px, radio **2 px** (esquinas casi rectas = sobriedad).
- Inter 600, 15 px, espaciado 0.02 em. Sin mayúsculas sostenidas en botones.
- Foco visible: contorno de 3 px bronce (dorado sobre navy) con separación de 3 px. Nunca `outline: none` sin reemplazo.
- Estado deshabilitado: opacidad 0.5 y `cursor: not-allowed`.

## 7.5 Formularios
- Etiqueta siempre visible encima del campo (no usar solo placeholder).
- Campo: 52 px de alto, borde 1 px `#8F8573` (contraste 3.6:1 con el fondo blanco), foco con borde navy + halo bronce.
- Error: borde y texto `#9B2C2C`, mensaje bajo el campo y anunciado con `aria-live`.
- `autocomplete` correcto (`name`, `organization`, `tel`) para llenar con un toque en móvil.

## 7.6 Iconografía
Línea fina (1.6 px), estilo Feather/Lucide, 20–24 px, en bronce o heredando color. Solo funcionales (teléfono, ubicación, WhatsApp, correo, horario). No usar íconos decorativos en tarjetas de servicio: el número (01–05) cumple esa función con más elegancia.

## 7.7 Fotografía
- **Reales**: equipo, socios, oficina, edificio Losoles, detalles de trabajo (manos, documentos, pantalla con cifras borrosas). Nada de stock genérico de apretones de manos.
- Tratamiento: blanco y negro o tonos fríos con baja saturación; contraste medio; luz natural lateral.
- Retratos: fondo neutro o la oficina desenfocada; formato 4:5; misma luz para todo el equipo.
- Arquitectura: líneas verticales, cristal, concreto; encuadres con mucho aire para poner texto encima.
- Exportación: WebP (calidad 75–80), AVIF opcional; ancho máximo 1600 px; retratos 800×1000 (~80 KB). Siempre `width`/`height` declarados para evitar CLS, `loading="lazy"` salvo en la primera imagen visible.
- Alt: describe a la persona o el lugar y su contexto ("Equipo de auditoría de González Armendáriz revisando estados financieros en la sala de juntas").

## 7.8 Movimiento
- Solo transiciones de 250–300 ms en hover y una entrada suave (subtítulo y CTA del hero, 900 ms).
- El H1 no se anima (es el elemento LCP).
- Se desactiva todo con `prefers-reduced-motion: reduce`.
- Sin sliders, carruseles, contadores animados ni parallax.

## 7.9 Accesibilidad (AA)
- Contraste verificado en la tabla 7.1.
- Zoom permitido (viewport sin `maximum-scale` ni `user-scalable=no`).
- Enlace "Saltar al contenido", navegación completa con teclado, `Esc` cierra el menú.
- Un H1 por página y jerarquía H2/H3 sin saltos.
- Acordeones con `<details>/<summary>` nativos.
- Textos de enlace descriptivos (no "clic aquí").

## 7.10 Logotipo
[PENDIENTE] Recibir el logotipo vectorial (SVG). Mientras tanto, el sitio usa un logotipo tipográfico: "González Armendáriz" en Cormorant Garamond 600 + descriptor "CONTABILIDAD · IMPUESTOS · AUDITORÍA" en Inter 600 dorado. Si el logo actual no encaja con esta dirección, se recomienda un rediseño ligero (mismo nombre, tipografía serif, monograma "GA" para favicon y redes).
