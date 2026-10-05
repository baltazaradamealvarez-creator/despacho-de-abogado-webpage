# 5. Landing pages para publicidad

Reglas comunes a las tres:
- **Sin menú** de navegación. El logo no enlaza fuera de la página. El único enlace saliente es el aviso de privacidad.
- `noindex, follow`, fuera del sitemap. No compiten con las páginas orgánicas.
- **Formulario arriba**: en escritorio, a la derecha del titular; en móvil, justo después del subtítulo (sin desplazarse más de una pantalla).
- Teléfono click-to-call en el encabezado y WhatsApp flotante en móvil.
- **Message match**: el H1 repite el título 1 del anuncio que lleva a la página. Una sola URL por servicio, con variantes de titular por grupo de anuncios mediante `?v=` (lista blanca en el HTML; nunca se inserta texto libre de la URL).
- Campos ocultos con UTMs y `gclid`/`fbclid`/`li_fat_id` para medir qué campaña generó cada cita (y poder importar conversiones offline cuando la cita se concrete).
- Estructura: titular + subtítulo + formulario → 3 beneficios → confianza → FAQ corta → CTA repetido → footer mínimo.

Código de referencia: `site/lp/contabilidad-empresas/index.html`. Las otras dos se construyen con la misma plantilla y el copy de abajo.

---

## 5.1 Landing: Contabilidad: `/lp/contabilidad-empresas/`

**Meta title:** Contabilidad para empresas en Monterrey | González Armendáriz (noindex)

| Variante `?v=` | Grupo de anuncios | H1 |
|---|---|---|
| (base) | Contabilidad para empresas | Contabilidad para empresas en Monterrey |
| `despacho` | Despacho contable | Despacho contable para empresas en Monterrey |
| `san-pedro` | Contador San Pedro | Contador para empresas en San Pedro Garza García |
| `pymes` | LinkedIn / Meta (pymes) | Contabilidad para pymes en Monterrey |

- **Antetítulo:** MONTERREY · SAN PEDRO GARZA GARCÍA
- **Subtítulo:** Sus impuestos al día y cifras claras cada mes. Agende una reunión con un socio de la firma.
- **Respaldo bajo el titular:** Más de 28 años respaldando empresas en Nuevo León · Más de 400 empresas han confiado en nosotros · Un equipo de 30 especialistas en una sola firma
- **Formulario:** Agende una consulta. Déjenos sus datos y le llamamos para acordar fecha y hora. [PENDIENTE: tiempo de respuesta] · Nombre · Empresa · Teléfono · Servicio (preseleccionado: Contabilidad) · Botón: **Solicitar mi consulta** · Aviso simplificado: González Armendáriz, S.C. usará sus datos para contactarle sobre su solicitud. Consulte nuestro aviso de privacidad.
- **Beneficios** (H2: Menos preocupaciones, mejores decisiones)
  1. **Impuestos a tiempo.** Calculamos y presentamos sus declaraciones en fecha, para evitar multas y recargos por olvidos.
  2. **Cifras claras cada mes.** Estados financieros explicados en lenguaje sencillo, para saber cuánto gana y cuánto debe.
  3. **Respaldo ante el SAT.** Si llega una carta o un requerimiento, lo revisamos y respondemos dentro del plazo.
- **Confianza:** 28+ años · 400+ empresas · 30 especialistas · [PENDIENTE: 2–3 testimonios con nombre, cargo y empresa, con autorización por escrito] · [PENDIENTE: logos o afiliaciones]
- **FAQ** (H2: Antes de agendar)
  - ¿Cuánto cuesta llevar la contabilidad de mi empresa? → Depende del número de operaciones, empleados y obligaciones de su empresa. Después de la primera reunión le enviamos una propuesta por escrito con alcance y honorarios fijos mensuales. [SUPUESTO: honorarios fijos mensuales]
  - ¿Es complicado cambiar de contador? → No. Le pedimos acceso a su información del SAT, sus declaraciones y su contabilidad reciente. Coordinamos la entrega con su contador anterior para que usted no tenga que hacerlo.
  - Mi contabilidad está atrasada. ¿Pueden ayudarme? → Sí. Revisamos qué falta, calculamos el impacto y presentamos lo pendiente con un plan claro, buscando reducir recargos y multas dentro de lo que permite la ley.
- **CTA final:** H2 Ponga su contabilidad en manos expertas · Una reunión con un socio basta para saber qué necesita su empresa. · [Agendar una consulta] [Escribir por WhatsApp] · O llame al 81 8363 4412

---

## 5.2 Landing: Asesoría Fiscal: `/lp/asesoria-fiscal/`

**Meta title:** Asesoría fiscal para empresas en Monterrey | González Armendáriz (noindex)

| Variante `?v=` | Grupo de anuncios | H1 |
|---|---|---|
| (base) | Asesoría fiscal empresas | Asesoría fiscal para empresas en Monterrey |
| `sat` | Requerimientos y cartas del SAT | Respaldo ante cartas y requerimientos del SAT |
| `planeacion` | Planeación fiscal | Planeación fiscal para empresas en Monterrey |

- **Subtítulo (base y planeación):** Conozca el efecto fiscal de sus decisiones antes de tomarlas. Planeación dentro del marco legal, con un socio de la firma.
- **Subtítulo (variante `sat`):** Revisamos la carta o el requerimiento, le explicamos sus opciones y preparamos la respuesta dentro del plazo.
- **Respaldo bajo el titular:** Más de 28 años en Nuevo León · Más de 400 empresas respaldadas · Especialistas en impuestos empresariales
- **Formulario:** igual; servicio preseleccionado: Asesoría fiscal. Botón: **Solicitar mi consulta**
- **Beneficios** (H2: Decisiones con menos riesgo)
  1. **Antes, no después.** Evaluamos el efecto fiscal de una operación antes de que la firme.
  2. **Dentro del marco legal.** Solo estrategias con sustento legal y razón de negocio. Nada de esquemas agresivos.
  3. **Acompañamiento ante el SAT.** Si llega una carta invitación, una revisión o un requerimiento, respondemos con usted y en plazo.
- **Confianza:** cifras + [PENDIENTE: testimonio de un director o caso real anónimo autorizado]
- **FAQ**
  - ¿La planeación fiscal es legal? → Sí, cuando se basa en la ley y en la operación real de su negocio. Solo recomendamos estrategias con sustento legal y razón de negocio.
  - Me llegó una carta del SAT. ¿Qué hago? → No la ignore. Revisamos el origen, le explicamos sus opciones y preparamos la respuesta dentro del plazo.
  - ¿Pueden trabajar con mi contador actual? → Sí. La asesoría fiscal complementa el trabajo de su contador; coordinamos con él.
- **CTA final:** H2 Revise su próxima decisión con un socio · [Agendar una consulta] [WhatsApp] · 81 8363 4412

> Políticas de anuncios: no usar "pague menos impuestos", "ahorro garantizado" ni "evite auditorías". Sí: "reduzca riesgos", "planeación dentro del marco legal", "decisiones con información".

---

## 5.3 Landing: Auditoría: `/lp/auditoria/`

**Meta title:** Auditoría de estados financieros en Monterrey | González Armendáriz (noindex)

| Variante `?v=` | Grupo de anuncios | H1 |
|---|---|---|
| (base) | Auditoría de estados financieros | Auditoría de estados financieros en Monterrey |
| `externa` | Auditoría externa / despacho de auditoría | Auditoría externa para empresas en Monterrey |
| `banco` | Estados financieros auditados | Estados financieros auditados para su banco o sus socios |

- **Subtítulo:** Una opinión independiente sobre sus cifras, con fechas claras desde el inicio. Agende una reunión con un socio.
- **Respaldo bajo el titular:** Más de 28 años en Nuevo León · Más de 400 empresas respaldadas · Equipo de auditoría con [PENDIENTE: número] especialistas
- **Formulario:** servicio preseleccionado: Auditoría. Botón: **Solicitar una propuesta de auditoría**
- **Beneficios** (H2: Cifras que generan confianza)
  1. **Opinión independiente.** Un informe formal que reconocen bancos, inversionistas y consejos.
  2. **Calendario por escrito.** Alcance y fechas acordados antes de empezar, con mínima interrupción para su equipo.
  3. **Recomendaciones prácticas.** Una carta con mejoras concretas a sus controles y procesos.
- **Confianza:** cifras + [PENDIENTE: afiliaciones profesionales; testimonios]
- **FAQ**
  - ¿Cuánto tarda una auditoría? → Depende del tamaño y del orden de la información. Acordamos un calendario por escrito al inicio. [PENDIENTE: rango típico]
  - ¿Qué necesita mi equipo? → Una lista de documentos que le entregamos al inicio, acceso al sistema contable y una persona de contacto.
  - ¿En qué se diferencia de un dictamen fiscal? → La auditoría opina sobre sus estados financieros; el dictamen fiscal es un informe sobre impuestos que se presenta al SAT y solo es obligatorio para algunas empresas.
- **CTA final:** H2 ¿Necesita estados financieros auditados? Hablemos de alcance y fechas · [Solicitar una propuesta] [WhatsApp] · 81 8363 4412

---

## 5.4 Página de gracias (todas las landings)
`/gracias/?origen=lp-<servicio>` (noindex). H1: Gracias. Recibimos su solicitud. · Un miembro de la firma le llamará para acordar fecha y hora. · Botón WhatsApp para urgencias. No lleva otro formulario ni enlaces a blog (evita que la persona se distraiga antes de la llamada).
