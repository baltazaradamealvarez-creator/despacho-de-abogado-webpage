# 6. Wireframes en texto

Convenciones: `[BOTÓN]`, `(enlace)`, `▢ imagen`, `≡ menú`. Ancho máximo del contenido: 1200 px. Margen lateral: 16 px en móvil, 32 px en escritorio. Mobile-first: lo que se ve en móvil define el orden; el escritorio solo reacomoda en columnas.

## 6.1 Encabezado (todas las páginas excepto landings)

```
MÓVIL (≤1023 px)                         ESCRITORIO (≥1024 px)
┌──────────────────────────────┐        ┌──────────────────────────────────────────────────────────────┐
│ González Armendáriz   ☎  ≡  │        │ González Armendáriz      81 8363 4412 │ Servicios Nosotros    │
└──────────────────────────────┘        │ CONTABILIDAD·IMPUESTOS…              Equipo Perspectivas      │
  Fondo navy, sticky, 68 px              │                                       Contacto EN [AGENDAR]  │
  ☎ = click-to-call                      └──────────────────────────────────────────────────────────────┘
  ≡ abre panel a pantalla completa         Fondo navy, sticky, 80 px. El botón dorado es el único color fuerte.
```

## 6.2 Home

```
┌─ 1. HERO (navy, ~85 vh en escritorio, sin imagen pesada) ─────────────────────────────┐
│ ── SAN PEDRO GARZA GARCÍA · MÁS DE 28 AÑOS          (antetítulo dorado)               │
│ Despacho contable y fiscal                         ║║║║  líneas verticales            │
│ para empresas en Monterrey            (H1 serif)   ║║║║  arquitectónicas (CSS)       │
│ Cifras confiables e impuestos en orden…  (lead)                                       │
│ [AGENDAR UNA CONSULTA]   (dorado)                                                     │
│ La primera reunión es con un socio de la firma.  (microcopy)                          │
└───────────────────────────────────────────────────────────────────────────────────────┘
┌─ 2. CIFRAS (blanco) ──────────────────────────────────────────────────────────────────┐
│  28+             │  400+                │  30                                         │
│  años de …       │  empresas respald…   │  especialistas en …                         │
└───────────────────────────────────────────────────────────────────────────────────────┘
   Móvil: una debajo de otra, número a la izquierda y texto a la derecha.
┌─ 3. SERVICIOS (hueso) ────────────────────────────────────────────────────────────────┐
│ ── SERVICIOS                                                                          │
│ Todo lo financiero de su empresa, en una sola firma  (H2)                              │
│ ┌──────────────┬──────────────┬──────────────┐                                        │
│ │01            │02            │03            │  Tarjetas blancas, borde 1 px,          │
│ │Contabilidad… │Asesoría Fisc.│Auditoría     │  toda la tarjeta es clicable.            │
│ │una línea     │una línea     │una línea     │  Hover: fondo hueso.                     │
│ │Ver servicio →│Ver servicio →│Ver servicio →│                                         │
│ ├──────────────┼──────────────┼──────────────┤  Móvil: 1 columna. Tablet: 2.            │
│ │04 Consultoría│05 Serv. Adm. │ NAVY: ¿No    │                                         │
│ │              │              │ sabe por dón-│  6.ª tarjeta = CTA (cierra la grilla)    │
│ │              │              │ de empezar? →│                                         │
│ └──────────────┴──────────────┴──────────────┘                                        │
└───────────────────────────────────────────────────────────────────────────────────────┘
┌─ 4. POR QUÉ NOSOTROS (blanco) ────────────────────────────────────────────────────────┐
│ H2: Una firma que conoce su empresa y responde por su trabajo                         │
│ ───────────── (línea bronce) ×3                                                       │
│ Trayectoria         Visión integral        Prevención                                 │
│ una frase           una frase              una frase                                  │
└───────────────────────────────────────────────────────────────────────────────────────┘
┌─ 5. LIDERAZGO (navy) ─────────────────────────────────────────────────────────────────┐
│ ▢ Retrato B/N 4:5 con marco          ── LIDERAZGO                                     │
│   dorado desplazado                   "Un director toma mejores decisiones…" (serif   │
│                                        itálica 40 px)                                 │
│                                       Alejandro González · Director Fundador          │
│                                       (Conocer la firma →)                            │
└───────────────────────────────────────────────────────────────────────────────────────┘
┌─ 6. PREGUNTAS FRECUENTES (hueso) ─────────────────────────────────────────────────────┐
│ H2: Lo que nos preguntan los directores                                               │
│ ¿Qué tipo de empresas atienden?                                                  +    │
│ ─────────────────────────────────────────────────────────────────────────────────     │
│ ¿Cuánto cuestan sus servicios?                                                   +    │
│ … (5 en total, acordeón nativo <details>, funciona sin JavaScript)                    │
└───────────────────────────────────────────────────────────────────────────────────────┘
┌─ 7. CONTACTO (blanco) ────────────────────────────────────────────────────────────────┐
│ H2: Hablemos de su empresa                   ┌──────────────────────────┐             │
│ Agende una reunión con un socio…             │ Agendar una consulta     │             │
│ — 28+ años — 400+ empresas — 30 esp.         │ Nombre        [_______]  │             │
│ ⌖ Dirección                                  │ Empresa       [_______]  │             │
│ ☎ 3 teléfonos (click-to-call)                │ Teléfono      [_______]  │             │
│ ✆ WhatsApp                                   │ Servicio      [▼______]  │             │
│ ✉ Correo  ◷ Horario                          │ [AGENDAR UNA CONSULTA]   │             │
│ ┌ Mapa (fachada ligera) ───────────┐          │ aviso de privacidad      │             │
│ │ [Cómo llegar] [Mostrar mapa]     │          └──────────────────────────┘             │
│ └──────────────────────────────────┘                                                   │
│ Móvil: texto → datos → formulario → mapa                                               │
└───────────────────────────────────────────────────────────────────────────────────────┘
┌─ FOOTER (navy) ───────────────────────────────────────────────────────────────────────┐
│ Marca + NAP + teléfonos │ Servicios (5) │ La firma (… Bolsa de trabajo) │ Legal │ EN    │
│ © 2026 González Armendáriz, S.C.                                                      │
└───────────────────────────────────────────────────────────────────────────────────────┘
  Flotante (solo móvil): ◉ WhatsApp abajo a la derecha, 56 px, navy con borde dorado.
```

## 6.3 Plantilla de página de servicio (igual para las 5)

```
Encabezado
Migas: Inicio › Servicios › Contabilidad                 (BreadcrumbList)
┌─ HERO corto (navy, ~50 vh) ─────────────────────────────────────────────┐
│ H1: Contabilidad para empresas en Monterrey                             │
│ Subtítulo (1 línea)                                                     │
│ [AGENDAR UNA CONSULTA]   (Escribir por WhatsApp)                        │
└─────────────────────────────────────────────────────────────────────────┘
┌─ 2 columnas en escritorio ──────────────────────────────────────────────┐
│ H2 ¿Para quién es?        │  H2 Qué problema resuelve                   │
│ 2–3 líneas                │  • bullet  • bullet  • bullet               │
└─────────────────────────────────────────────────────────────────────────┘
┌─ Qué incluye (hueso) ───────────────────────────────────────────────────┐
│ Lista en 2 columnas con marcas ✓ (máx. 8 puntos, 1 línea cada uno)      │
└─────────────────────────────────────────────────────────────────────────┘
┌─ Cómo trabajamos ───────────────────────────────────────────────────────┐
│ 01 ──── 02 ──── 03 ──── 04     (horizontal en escritorio,               │
│ título  título  título  título   vertical en móvil)                     │
└─────────────────────────────────────────────────────────────────────────┘
┌─ Banda de confianza (blanco) ───────────────────────────────────────────┐
│ 28+ años · 400+ empresas · 30 especialistas · [testimonio PENDIENTE]    │
└─────────────────────────────────────────────────────────────────────────┘
┌─ Preguntas frecuentes (acordeón, 4–5) ──────────────────────────────────┐
└─────────────────────────────────────────────────────────────────────────┘
┌─ Servicios relacionados: 2 tarjetas (enlazado interno) ─────────────────┐
┌─ Artículos relacionados: 2 enlaces a Perspectivas ──────────────────────┐
┌─ CTA final (navy): H2 + [AGENDAR] + WhatsApp + teléfono ────────────────┐
Footer
```

## 6.4 Landing page de publicidad

```
┌─ Encabezado mínimo (navy): marca sin enlace ............ ☎ 81 8363 4412 ─┐
┌─ HERO (navy) ────────────────────────────────────────────────────────────┐
│ ── MONTERREY · SAN PEDRO                ┌────────────────────────────┐   │
│ H1 = título del anuncio                 │ Agende una consulta        │   │
│ Subtítulo                               │ Nombre / Empresa /         │   │
│ ✓ 28+ años  ✓ 400+ empresas  ✓ 30 esp.  │ Teléfono / Servicio ▼      │   │
│                                         │ [SOLICITAR MI CONSULTA]    │   │
│                                         └────────────────────────────┘   │
│ Móvil: H1 → subtítulo → FORMULARIO → ✓ respaldo                           │
└──────────────────────────────────────────────────────────────────────────┘
┌─ 3 beneficios (línea bronce + H3 + frase) ───────────────────────────────┐
┌─ Confianza: cifras + testimonios/logos [PENDIENTE] ──────────────────────┐
┌─ FAQ corta (3) ──────────────────────────────────────────────────────────┐
┌─ CTA repetido (navy, centrado): [AGENDAR] [WHATSAPP] · teléfono ─────────┐
┌─ Footer mínimo: © · dirección · aviso de privacidad ─────────────────────┐
```

## 6.5 Nosotros / Equipo / Contacto (resumen)
- **Nosotros:** Hero corto (H1) → Historia (texto 2 col. + foto de oficina B/N) → Valores (4 en grilla) → Liderazgo (retrato + semblanza) → Cifras → Afiliaciones [PENDIENTE] → CTA.
- **Equipo:** H1 + intro → Dirección (tarjeta grande) → Socios y gerentes (grilla 2/3/4 col.) → Áreas (lista) → CTA + enlace a Bolsa de trabajo.
- **Contacto:** H1 → 2 columnas: formulario | datos (NAP, teléfonos, WhatsApp, horario, cómo llegar) → mapa ancho completo (bajo demanda) → FAQ de visita.

## 6.6 Jerarquía de CTA en todo el sitio
1. **Primario** (uno por pantalla): Agendar una consulta: botón dorado sobre navy o navy sobre claro.
2. **Secundario**: WhatsApp (flotante en móvil + enlace de texto junto al CTA en servicios).
3. **Terciario**: teléfono click-to-call (encabezado y bloque de contacto).
Nunca dos botones primarios juntos.
