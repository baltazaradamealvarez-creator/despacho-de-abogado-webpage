# 06. Wireframes y comportamiento responsive

[SUPUESTO] Sitio corporativo bilingüe con un objetivo: solicitar una consulta. La recepción de una solicitud no confirma una cita. La integración de agenda, los honorarios de consulta, las fotografías autorizadas y el receptor del formulario están [PENDIENTE]. No publicar estos marcadores como mensajes comerciales.

## Sistema común ES/EN

Ancho de referencia interior 1200 px; portada entregada hasta 1512 px, márgenes 24 px móvil / 48 px escritorio. Columna de lectura de 65 caracteres. Cabecera: marca, Servicios, Nosotros, Equipo, Perspectivas, Contacto, selector ES/EN y «Agendar una consulta». La cabecera móvil usa botón de menú con estado anunciado, cierre con Escape y devolución del foco. El selector conserva la página equivalente, no regresa siempre al inicio. Enlace «Saltar al contenido» antes de la cabecera.

H1 único en cada página. Migas visibles excepto inicio y campañas. Botón principal relleno azul; WhatsApp secundario con texto accesible y discreto, fijo en móvil sin cubrir formulario, cookies o footer. CTA principal lleva a /contacto/#consulta (EN /en/contact/#consultation), o al formulario local de las landings. Las cifras cerca de CTA son texto, no imágenes. Footer común: NAP completo, teléfonos enlazados, privacidad, cookies, empleo y copyright 2026. Bolsa de trabajo solo en footer; enlace [PENDIENTE: destino real]. Sin newsletter en home.

## Inicio: exactamente siete secciones

1. **Hero.** Dos columnas 60/40 en escritorio; una columna en móvil. Izquierda: identificación «González Armendáriz», H1 de máximo ocho palabras, subtítulo de una línea visual amplia y un CTA «Agendar una consulta». Derecha: foto real arquitectónica de la oficina; mientras no exista una foto autorizada, fondo tipográfico sobrio sin stock. No inventar imagen del edificio. H1 y CTA visibles en primer viewport habitual sin altura fija forzada. La cabecera y el footer no se cuentan como secciones de contenido.
2. **Cifras.** Banda de tres columnas: 28+ / años de trayectoria; 400+ / empresas respaldadas; 30 / colaboradores. Usar «especialistas» solamente después de confirmar que describe a los 30. En móvil mantener tres columnas si caben sin reducir legibilidad; de lo contrario apilar. Sin contadores animados.
3. **Servicios.** H2 breve, cinco tarjetas en cuadrícula 3+2, dos columnas intermedias y una en móvil. Cada tarjeta: H3 nombre, una frase de resultado, enlace descriptivo a su página. Sin repetir esta lista en otra sección del home.
4. **Por qué nosotros.** Tres pilares, una frase por pilar. Tipografía y divisores discretos; ningún sello o certificación no verificado. Cuadrícula horizontal / vertical móvil.
5. **Liderazgo.** Foto real de Alejandro González y texto de dos líneas con nombre y cargo Director Fundador. Imagen reservada con dimensiones, sin fotografía ficticia. Si falta: bloque de identidad tipográfico en producción, fotografía [PENDIENTE] en documentación. Evitar atribuir una cita que no haya aprobado.
6. **Preguntas frecuentes.** Cinco preguntas empresariales, acordeones nativos `details/summary`; contenido íntegro en HTML. Área de clic amplia, foco visible y apertura múltiple permitida. Solo preguntas y respuestas presentes se marcan FAQPage.
7. **Consulta y ubicación.** H2, CTA, cifras de confianza, dirección y los tres teléfonos click-to-call; WhatsApp secundario. Enlace de mapa a la dirección exacta; iframe opcional únicamente con consentimiento si el proveedor coloca cookies. En escritorio, contacto y mapa 50/50; en móvil primero contacto. No simular una ubicación con coordenadas aproximadas.

## Índice de Servicios

Cabecera y migas → H1 y resumen de dos líneas → cinco tarjetas ampliadas, cada una con destinatario, beneficio y enlace → bloque «¿Qué necesita su empresa?» con CTA único → footer. Evitar listas de todas las tareas técnicas en este índice. En móvil una tarjeta por fila.

## Plantilla individual de servicio, cinco páginas

1. Migas + hero con H1 servicio y Monterrey, intro de 2–3 líneas, CTA y 28+ / 400+ cerca.
2. «Para quién es»: texto breve con contexto de dirección, finanzas o administración.
3. «Qué problema resuelve»: tres bullets en una sola columna de lectura, o tres tarjetas muy breves.
4. «Qué incluye»: lista de alcance; evitar convertirla en promesa contractual. Aclarar que el alcance se acuerda por escrito.
5. «Cómo trabajamos»: tres o cuatro pasos numerados, horizontales en escritorio y verticales en móvil. Proceso planteado para el nuevo sitio [SUPUESTO: validar operación].
6. FAQ: cuatro o cinco acordeones. Texto total útil de 300–600 palabras por servicio; no ocultarlo por CSS ni cargarlo solo tras interacción.
7. CTA «Agendar una consulta» + WhatsApp, datos de confianza y un enlace contextual a un servicio complementario. Sin formulario adicional largo.

La misma jerarquía rige para Contabilidad, Asesoría Fiscal, Auditoría, Consultoría y Servicios Administrativos. Las preguntas, problemas y alcance cambian; no duplicar texto con un nombre distinto.

## Nosotros

Migas → H1 y dos líneas de posicionamiento → trayectoria con 28+ años, sin inventar fecha de fundación → valores propuestos [SUPUESTO: aprobación de la firma], tres bloques → liderazgo con Alejandro González y cargo verificado → cifras → CTA. No construir línea de tiempo con hitos desconocidos. EN conserva hechos y tono institucional, con traducción natural.

## Equipo

Migas → H1 → introducción sobre 30 colaboradores → fundador con nombre/cargo → perfiles reales únicamente tras aprobación de nombre, cargo, fotografía y biografía [PENDIENTE] → CTA. En versión publicable sin perfiles aprobados, mostrar bloque editorial sobre el equipo y la cifra, sin tarjetas ficticias ni iniciales de personas inventadas.

## Contacto

Migas → H1 y frase «Comparta lo que necesita su empresa» → dos columnas. Izquierda: formulario nombre, empresa, teléfono, servicio de interés; enlace al aviso y mecanismo de privacidad validado, botón «Agendar una consulta». Derecha: confianza, dirección, tres teléfonos, WhatsApp. Correo y horarios [PENDIENTE], se omiten hasta confirmación. Debajo, mapa o enlace de indicaciones. Éxito solo tras confirmación del servidor; mensaje aclara que el equipo dará seguimiento y no promete plazo sin validar. Error conserva datos y lleva foco a resumen accesible. Formulario EN completamente traducido.

## Perspectivas y artículo

**Índice:** H1 → introducción breve → filtros por cuatro pilares como enlaces accesibles → tarjetas con título, resumen, fecha real y categoría → paginación rastreable → CTA. Sin archivos vacíos indexables ni buscador sin resultados. **Artículo:** migas → H1 → autor real/fecha de publicación y actualización reales → introducción dos líneas → respuesta directa destacada → desarrollo con H2/H3 y fuentes oficiales → FAQ específica → dos enlaces relacionados + servicio pertinente → CTA. Índice de contenidos solo para piezas largas; fechas legales se revisan cada año. Metadatos de artículo no se rellenan con personas o fechas ficticias.

## Tres landings ES/EN

Una plantilla compartida y copy propio por Contabilidad, Asesoría Fiscal y Auditoría. **Sin menú**, buscador ni blog; selector ES/EN discreto enlaza únicamente a la landing equivalente y cada campaña envía al idioma correspondiente. Marca como identificación estática.

1. Arriba: columna izquierda H1 idéntico en intención al anuncio y subtítulo; derecha formulario visible, cuatro campos, aviso de privacidad y botón «Agendar una consulta». En móvil H1, subtítulo y formulario, sin imagen que lo empuje demasiado abajo. Franja 28+ / 400+ inmediatamente junto al formulario.
2. Tres beneficios con bullets, legibles sin interacción.
3. Confianza: cifras verificadas; identidad del fundador opcional. Testimonios/logos/certificaciones [PENDIENTE]; omitir hasta autorización.
4. FAQ corta: tres preguntas sobre alcance, información necesaria y contratación, según copy de la landing.
5. CTA repetido que devuelve al formulario, WhatsApp secundario y dirección legal con privacidad/cookies. No repetir el formulario ni duplicar IDs.

Landings con `noindex,follow` y fuera del sitemap para separar campañas de páginas orgánicas; deben permitir rastreo para que se lea `noindex`. Es una decisión editorial [SUPUESTO], no requisito de Google Ads. No redirigir tráfico por dispositivo ni esconder texto a revisores.
