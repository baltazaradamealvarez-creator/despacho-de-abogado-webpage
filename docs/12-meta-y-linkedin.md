# 12. Meta Ads y LinkedIn Ads

Rol de cada plataforma:
- **LinkedIn**: prospección. Llega a directores generales, dueños y directores de finanzas de empresas de Monterrey, aunque nunca hayan buscado un despacho.
- **Meta (Facebook e Instagram)**: **remarketing**. Recuerda la firma a quien ya visitó el sitio y lo lleva de vuelta a agendar.
- Google Search: captura la demanda que ya existe (ver `11-google-ads.md`).

## 12.1 Reglas de políticas (servicios financieros)
- Sin promesas: nada de "ahorre impuestos", "pague menos", "garantizado", "evite al SAT", "cero multas".
- **Meta: atributos personales.** No afirmar ni insinuar la situación financiera de quien lee ("¿Tiene problemas con el SAT?", "¿Su empresa debe impuestos?"). Hablar en general: "Si una carta del SAT llega a una empresa…".
- **Meta: categoría especial.** [SUPUESTO] Los servicios contables y fiscales no son "productos financieros" (crédito, inversión, seguros), por lo que no deberían requerir la categoría especial. Si Meta la exige al revisar el anuncio, se declara: se pierde la segmentación por edad y género y el radio mínimo es de 15 km, lo cual no afecta a esta estrategia.
- Imágenes sin texto excesivo, sin capturas falsas de notificaciones y sin logos del SAT ni del gobierno.
- Cada anuncio lleva a la landing del servicio, con UTMs (ver `13-plan-de-medicion.md`).

---

## 12.2 Meta Ads: remarketing

**Audiencias** (requieren el Píxel de Meta y la API de Conversiones activos):
| Audiencia | Ventana | Uso |
|---|---|---|
| Visitó una landing y **no** envió formulario | 14 días | Concepto 2 o 3, frecuencia más alta |
| Visitó una página de servicio | 30 días | Concepto del servicio visitado |
| Todos los visitantes del sitio | 180 días | Concepto 1 (calendario fiscal) en temporadas clave |
| Interactuó con Instagram o Facebook de la firma | 90 días | Concepto 3 |
| **Exclusiones** | — | Personas que enviaron formulario (180 días) + lista de clientes actuales [PENDIENTE] |

Objetivo: *Clientes potenciales* (conversión "Lead" en el sitio). Presupuesto sugerido: 10–15 % del presupuesto total de pauta [PENDIENTE]. Ubicaciones: Feed e Historias de Instagram y Facebook; sin Audience Network.

### Concepto Meta 1: "Calendario fiscal" (temporada: febrero–marzo; repetir en abril, mayo y noviembre con la fecha que corresponda)
- **Texto principal:** La declaración anual de las personas morales vence el 31 de marzo. Prepararla con tiempo reduce riesgos y evita decisiones de último minuto. En González Armendáriz acompañamos a empresas de Nuevo León desde hace más de 28 años.
- **Titular:** Prepare su declaración anual con tiempo
- **Descripción:** Agende una reunión con un socio
- **Botón:** Más información → `/lp/contabilidad-empresas/`
- **Imagen:** fondo navy, una hoja de calendario de marzo en papel hueso con el 31 marcado por un trazo bronce; tipografía serif "31 de marzo". Formatos 1:1 y 4:5; versión 9:16 para Historias con el texto arriba y la marca abajo.

### Concepto Meta 2: "Hable con un socio"
- **Texto principal:** Un director decide mejor cuando confía en sus números. Agende una reunión con un socio de González Armendáriz y revise con calma la situación contable y fiscal de su empresa.
- **Titular:** Su contabilidad, revisada por un socio
- **Descripción:** Oficina en San Pedro Garza García
- **Botón:** Reservar → landing del servicio visitado
- **Imagen:** retrato real en blanco y negro de Alejandro González en la oficina, luz lateral, mirada a cámara; franja inferior navy con nombre y cargo. [PENDIENTE: sesión de fotos]

### Concepto Meta 3: "Respaldo en cifras"
- **Texto principal:** Más de 400 empresas de Nuevo León confían a González Armendáriz su contabilidad, sus impuestos y su auditoría. Si quiere saber qué necesita la suya, la primera reunión es con un socio de la firma.
- **Titular:** 28 años respaldando empresas
- **Descripción:** Contabilidad · Impuestos · Auditoría
- **Botón:** Más información → `/lp/contabilidad-empresas/?v=pymes`
- **Imagen / carrusel:** 3 tarjetas tipográficas sobre fotografía arquitectónica fría del edificio Losoles: "28+ años" · "400+ empresas" · "30 especialistas". Cifras en serif hueso con acento bronce.

---

## 12.3 LinkedIn Ads: directores y dueños

**Segmentación base**
- Ubicación: Área metropolitana de Monterrey (y San Pedro Garza García).
- Cargos: Director General, CEO, Presidente, Dueño/Propietario, Socio, Director de Finanzas, CFO, Director de Administración y Finanzas, Contralor, Gerente de Administración.
- Antigüedad (seniority): Propietario, Socio, CXO, Director, VP.
- Tamaño de empresa: 11–500 empleados.
- Excluir sectores: Contabilidad, Servicios legales (competidores y pares), y empleados de la propia firma.
- Audiencias propias: visitantes del sitio (Insight Tag) y [PENDIENTE] lista de empresas objetivo (ABM) cargada como lista de empresas.
- Tamaño de audiencia: mínimo 300 miembros; idealmente 20,000–80,000. Si queda muy chica, quitar "antigüedad" y dejar cargos.
- Formato: Single Image Sponsored Content + Lead Gen Form (formulario nativo de LinkedIn con los mismos 4 campos + aviso de privacidad). Objetivo: *Generación de oportunidades*.

### Concepto LinkedIn 1: "Antes de firmar" (Asesoría Fiscal)
- **Texto de introducción:** Invertir, reestructurar o repartir utilidades: cada decisión importante tiene un efecto fiscal. Conózcalo antes de firmar. En González Armendáriz revisamos sus opciones con números y dentro del marco legal.
- **Titular:** Asesoría fiscal para directores en Monterrey
- **Descripción:** Agende una consulta con un socio
- **CTA:** "Solicitar presupuesto" con Lead Gen Form, o "Más información" → `/lp/asesoria-fiscal/?v=planeacion` (LinkedIn no ofrece un botón "Agendar")
- **Imagen:** sala de juntas en blanco y negro, mesa con documentos y una pluma; titular superpuesto en serif: "Antes de firmar, revise el efecto fiscal."

### Concepto LinkedIn 2: "Cifras que generan confianza" (Auditoría)
- **Texto de introducción:** Cuando un banco, sus socios o un inversionista piden estados financieros auditados, la confianza depende de quién los revisa. Acordamos alcance y calendario por escrito desde el inicio, con la menor interrupción para su equipo.
- **Titular:** Auditoría de estados financieros en Monterrey
- **Descripción:** Más de 28 años y 400 empresas respaldadas
- **CTA:** Solicitar presupuesto → `/lp/auditoria/?v=banco`
- **Imagen:** detalle arquitectónico (líneas verticales de cristal y concreto) en tonos fríos; franja navy con "Cifras que generan confianza." y el logotipo.

### Concepto LinkedIn 3: "Calendario fiscal 2027 para directores" (atracción con documento)
- **Texto de introducción:** Las fechas fiscales que todo director de empresa en México debería tener a la vista en 2027, en una sola página. Descárguelo sin costo. Lo preparó el equipo de González Armendáriz.
- **Titular:** Calendario fiscal 2027 para directores
- **Descripción:** Descarga en PDF, una página
- **CTA:** Descargar (Document Ad con formulario nativo para descargar)
- **Imagen:** maqueta del PDF sobre un escritorio, papel hueso con tipografía navy y acentos bronce.
- **Pendiente:** [PENDIENTE] diseñar el PDF (12 fechas, explicación de una línea cada una, contacto de la firma). Los leads se nutren con el correo mensual de Perspectivas y se pasan a un socio cuando piden reunión.

**Contenido orgánico de apoyo:** el socio autor de cada artículo lo comparte desde su perfil personal la semana de publicación. En servicios profesionales, el perfil de una persona alcanza más que la página de la empresa.
