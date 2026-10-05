# 11. Google Ads: estructura, palabras clave, negativas y anuncios

> Documento generado por `ads/generar_google_ads.py`. Para cambiar anuncios o keywords, edite el script y vuelva a ejecutarlo; también regenera los CSV para Google Ads Editor (`ads/google-ads-editor-anuncios.csv` y `ads/google-ads-editor-keywords.csv`). Todos los títulos tienen ≤ 30 caracteres y todas las descripciones ≤ 90 (validado por el script).

## 11.1 Estructura de la cuenta

| Campaña | Presupuesto sugerido | Landing | Grupos de anuncios (por intención) |
|---|---|---|---|
| **GS \| Contabilidad \| MTY** | 45 % del total | `/lp/contabilidad-empresas/` | Despacho contable · Contabilidad para empresas · Contador San Pedro |
| **GS \| Asesoría Fiscal \| MTY** | 30 % del total | `/lp/asesoria-fiscal/` | Asesoría fiscal empresas · Cartas y requerimientos SAT · Planeación fiscal |
| **GS \| Auditoría \| MTY** | 25 % del total | `/lp/auditoria/` | Auditoría estados financieros · Auditoría externa · Estados financieros auditados |
| **GS \| Marca** (recomendada) | 3–5 % | `/` | González Armendáriz (exacta y frase). Protege la marca a bajo costo |
| **Fase 2**: GS \| Outsourcing administrativo \| MTY | según resultados | `/lp/servicios-administrativos/` (por crear) | Outsourcing administrativo · Nómina · Cobranza |
| **Fase 2**: GS \| Accounting EN \| MX | según resultados | `/en/` o landing EN (por crear) | accounting firm Monterrey Mexico · tax advisor Monterrey |

**Presupuesto total:** [PENDIENTE]. Referencia: para tener datos útiles en 60 días, cada campaña necesita suficiente presupuesto para ~10 clics diarios en horario laboral. Revise el CPC estimado en el Planificador de palabras clave antes de definirlo.

**Configuración por campaña**
- Red: solo Búsqueda (desactivar Red de Display y socios de búsqueda al inicio).
- **Ubicación:** Monterrey, San Pedro Garza García, San Nicolás de los Garza, Guadalupe, Santa Catarina, Apodaca y General Escobedo. Opción de ubicación: **"Presencia: personas que están o suelen estar en sus ubicaciones"** (no "interés"), para no pagar clics de otras ciudades.
- **Ajuste San Pedro Garza García:** +20 % mientras la puja sea manual o *Maximizar clics*. Cuando pase a *CPA objetivo* los ajustes de puja dejan de aplicar; si San Pedro convierte claramente mejor, sepárelo en una campaña propia con su presupuesto.
- **Idioma:** español (y inglés, porque muchos directivos usan Google en inglés).
- **Puja:** inicio con *Maximizar conversiones* (con la conversión "Formulario enviado" + "Clic en WhatsApp" + "Llamada ≥ 60 s" como principales). Al llegar a ~30 conversiones en 30 días, pasar a *CPA objetivo*. Más adelante, importar citas realizadas desde el CRM (conversiones offline con `gclid`) y optimizar a esa conversión.
- **Concordancias:** exacta y de frase al inicio. Concordancia amplia solo cuando la campaña tenga historial de conversiones y Smart Bidding activo.
- **Horario:** lunes a viernes 7:00–20:00 y sábado 8:00–14:00 [SUPUESTO: ajustar al horario real de atención telefónica].
- **Rotación:** 3 anuncios por grupo (A, B y C). Fijar (pin) solo el título 1 del anuncio A en la posición 1 para asegurar el message match; los anuncios B y C sin fijaciones.
- **URL final:** la landing + `?v=` del grupo (ver tabla de variantes en `05-landing-pages.md`). Etiquetado automático (`gclid`) activado y sufijo de URL final con UTMs (ver `13-plan-de-medicion.md`).

## 11.2 Palabras clave por grupo

Notación: `[exacta]`, `"frase"`.

### GS | Contabilidad | MTY

| Grupo | Palabras clave | URL final |
|---|---|---|
| Despacho contable | `[despacho contable monterrey]` · `"despacho contable monterrey"` · `"despacho de contadores monterrey"` · `"despacho contable para empresas"` · `[firma de contadores monterrey]` · `"despacho contable nuevo leon"` · `"despacho contable y fiscal"` | `/lp/contabilidad-empresas/?v=despacho` |
| Contabilidad para empresas | `[contabilidad para empresas monterrey]` · `"contabilidad para empresas"` · `"servicios contables para empresas"` · `"servicios de contabilidad monterrey"` · `"contabilidad para pymes"` · `"contador externo para empresa"` · `"outsourcing contable monterrey"` | `/lp/contabilidad-empresas/` |
| Contador San Pedro | `[contador san pedro garza garcia]` · `"contador en san pedro garza garcia"` · `"contadores en san pedro"` · `"contador para empresas san pedro"` · `"despacho contable san pedro garza garcia"` | `/lp/contabilidad-empresas/?v=san-pedro` |

### GS | Asesoría Fiscal | MTY

| Grupo | Palabras clave | URL final |
|---|---|---|
| Asesoría fiscal empresas | `[asesoria fiscal monterrey]` · `"asesoría fiscal para empresas"` · `"asesor fiscal monterrey"` · `"consultoria fiscal monterrey"` · `"asesor fiscal san pedro garza garcia"` · `"despacho fiscal monterrey"` · `"asesoria fiscal empresas nuevo leon"` | `/lp/asesoria-fiscal/` |
| Cartas y requerimientos SAT | `"requerimiento del sat empresa"` · `"carta invitacion sat"` · `"asesoria requerimiento sat"` · `"revision del sat a empresa"` · `"asesor para auditoria del sat"` · `"multa del sat empresa"` | `/lp/asesoria-fiscal/?v=sat` |
| Planeación fiscal | `"planeacion fiscal empresas"` · `[planeacion fiscal monterrey]` · `"planeación fiscal para empresas"` · `"estrategia fiscal empresa"` · `"asesoria fiscal reestructura empresa"` | `/lp/asesoria-fiscal/?v=planeacion` |

### GS | Auditoría | MTY

| Grupo | Palabras clave | URL final |
|---|---|---|
| Auditoría estados financieros | `[auditoria de estados financieros monterrey]` · `"auditoría de estados financieros"` · `"auditoria financiera empresas"` · `"auditoria financiera monterrey"` · `"auditores monterrey"` | `/lp/auditoria/` |
| Auditoría externa | `[auditoria externa monterrey]` · `"auditoría externa empresas"` · `"despacho de auditoria monterrey"` · `"auditor externo monterrey"` · `"firma de auditoria monterrey"` · `"auditores san pedro garza garcia"` | `/lp/auditoria/?v=externa` |
| Estados financieros auditados | `"estados financieros auditados"` · `"estados financieros auditados para banco"` · `"estados financieros dictaminados"` · `"auditoria para credito bancario"` | `/lp/auditoria/?v=banco` |

## 11.3 Palabras clave negativas

**Lista compartida "Negativas generales"** (concordancia de frase, aplicar a todas las campañas):

`gratis` · `gratuito` · `gratuita` · `barato` · `económico` · `curso` · `cursos` · `diplomado` · `maestría` · `licenciatura` · `carrera` · `universidad` · `uanl` · `tesis` · `ensayo` · `tarea` · `pdf` · `libro` · `ejemplo` · `ejemplos` · `formato` · `plantilla` · `excel` · `qué es` · `que es` · `definición` · `concepto` · `significado` · `tipos de` · `wikipedia` · `empleo` · `empleos` · `vacante` · `vacantes` · `trabajo` · `bolsa de trabajo` · `sueldo` · `salario` · `prácticas` · `practicas` · `becario` · `occ` · `indeed` · `computrabajo` · `cita sat` · `citas sat` · `portal sat` · `sat.gob.mx` · `contraseña sat` · `e.firma` · `efirma` · `constancia de situación fiscal` · `rfc` · `buzón tributario` · `imss semanas` · `infonavit` · `software` · `programa` · `app` · `contpaqi` · `aspel` · `descargar` · `resico` · `uber` · `didi` · `airbnb` · `mercado libre` · `cdmx` · `ciudad de méxico` · `guadalajara` · `querétaro` · `puebla` · `tijuana` · `saltillo` · `chihuahua`

**Solo campaña Auditoría:** `auditoría interna curso` · `auditoría de sistemas` · `auditoría informática` · `auditoría médica` · `auditoría de calidad` · `iso 9001` · `auditor iso` · `auditoría ambiental` · `auditoría superior` · `asf` · `auditoría gubernamental` · `auditor lider`

**Solo campaña Asesoría Fiscal:** `declaración anual personas físicas` · `devolución de impuestos personas físicas` · `declaración anual asalariados` (búsquedas de personas físicas de bajo valor)

**Negativas cruzadas (evitan que las campañas compitan entre sí):** en Contabilidad, negar `auditoría` y `auditor`; en Auditoría, negar `contador` y `contabilidad`; en Contabilidad, negar `asesoría fiscal` y `planeación fiscal`.

Revisión semanal del informe de términos de búsqueda durante los primeros 2 meses; después, quincenal.

## 11.4 Anuncios responsivos (3 por grupo)

Cada grupo tiene tres anuncios con enfoques distintos: **A** Autoridad y trayectoria · **B** Beneficio para el director · **C** Local y acción. Los 5 primeros títulos de cada anuncio contienen la keyword del grupo; los 10 restantes refuerzan el enfoque.

Lenguaje revisado contra políticas: sin "garantizado", "ahorre impuestos", "evite auditorías", sin signos de exclamación ni mayúsculas sostenidas.

### GS | Contabilidad | MTY

Ruta visible: `gonzalezarmendariz.com/contabilidad/monterrey`

#### Grupo: Despacho contable → `/lp/contabilidad-empresas/?v=despacho`

**Anuncio A: Autoridad y trayectoria** (título 1 fijado en posición 1)

| # | Título | Car. |
|---|---|---|
| 1 | Despacho contable en Monterrey | 30 |
| 2 | Despacho contable empresarial | 29 |
| 3 | Firma de contadores Monterrey | 29 |
| 4 | Despacho contable y fiscal | 26 |
| 5 | Contadores para su empresa | 26 |
| 6 | Más de 28 años de trayectoria | 29 |
| 7 | 400+ empresas respaldadas | 25 |
| 8 | 30 especialistas en una firma | 29 |
| 9 | González Armendáriz | 19 |
| 10 | Firma contable en Nuevo León | 28 |
| 11 | Respaldo de una firma sólida | 28 |
| 12 | Contabilidad, impuestos y más | 29 |
| 13 | Primera reunión con un socio | 28 |
| 14 | Agende una consulta | 19 |
| 15 | Propuesta por escrito | 21 |

| # | Descripción | Car. |
|---|---|---|
| 1 | Más de 28 años y 400 empresas respaldadas en Nuevo León. Agende una consulta con un socio. | 90 |
| 2 | Contabilidad, impuestos y estados financieros en una sola firma. Oficina en San Pedro. | 86 |
| 3 | Le entregamos una propuesta por escrito con alcance, calendario y honorarios. | 77 |
| 4 | Un equipo de 30 especialistas en contabilidad, impuestos y auditoría. Hablemos. | 79 |

**Anuncio B: Beneficio para el director**

| # | Título | Car. |
|---|---|---|
| 1 | Despacho contable en Monterrey | 30 |
| 2 | Despacho contable empresarial | 29 |
| 3 | Firma de contadores Monterrey | 29 |
| 4 | Contadores para su empresa | 26 |
| 5 | Despacho contable en San Pedro | 30 |
| 6 | Impuestos presentados a tiempo | 30 |
| 7 | Menos riesgo de multas | 22 |
| 8 | Cifras claras cada mes | 22 |
| 9 | Estados financieros mensuales | 29 |
| 10 | Respaldo ante el SAT | 20 |
| 11 | Ponemos al día su contabilidad | 30 |
| 12 | Contabilidad electrónica | 24 |
| 13 | Revisión de sus facturas CFDI | 29 |
| 14 | Enfóquese en dirigir | 20 |
| 15 | Un responsable para su cuenta | 29 |

| # | Descripción | Car. |
|---|---|---|
| 1 | Sus impuestos presentados a tiempo y sus cifras claras cada mes. Agende una consulta. | 85 |
| 2 | Revisamos sus facturas y su contabilidad para reducir riesgos ante el SAT. | 74 |
| 3 | ¿Contabilidad atrasada? La ponemos al día con un plan claro y fechas por escrito. | 81 |
| 4 | Estados financieros explicados en lenguaje sencillo, para decidir con certeza. | 78 |

**Anuncio C: Local y acción**

| # | Título | Car. |
|---|---|---|
| 1 | Despacho contable en Monterrey | 30 |
| 2 | Firma de contadores Monterrey | 29 |
| 3 | Despacho contable y fiscal | 26 |
| 4 | Contadores para su empresa | 26 |
| 5 | Despacho contable en San Pedro | 30 |
| 6 | Oficina en San Pedro | 20 |
| 7 | Atendemos todo Monterrey | 24 |
| 8 | Agende con un socio hoy | 23 |
| 9 | Reunión presencial o en línea | 29 |
| 10 | Hable con un especialista | 25 |
| 11 | Llámenos o escríbanos | 21 |
| 12 | Empresas de Nuevo León | 22 |
| 13 | Respuesta a la brevedad | 23 |
| 14 | Cambie de contador sin estrés | 29 |
| 15 | Propuesta clara de honorarios | 29 |

| # | Descripción | Car. |
|---|---|---|
| 1 | Visítenos en Av. Lázaro Cárdenas, San Pedro, o agende una reunión en línea. | 75 |
| 2 | Atendemos empresas en Monterrey y su área metropolitana. Agende con un socio hoy. | 81 |
| 3 | Cambiar de contador es sencillo: coordinamos la entrega con su contador anterior. | 81 |
| 4 | Déjenos sus datos y le llamamos para acordar fecha y hora de su consulta. | 73 |

#### Grupo: Contabilidad para empresas → `/lp/contabilidad-empresas/`

**Anuncio A: Autoridad y trayectoria** (título 1 fijado en posición 1)

| # | Título | Car. |
|---|---|---|
| 1 | Contabilidad para empresas | 26 |
| 2 | Contabilidad para pymes | 23 |
| 3 | Servicios contables Monterrey | 29 |
| 4 | Contabilidad empresarial | 24 |
| 5 | Su contabilidad al día | 22 |
| 6 | Más de 28 años de trayectoria | 29 |
| 7 | 400+ empresas respaldadas | 25 |
| 8 | 30 especialistas en una firma | 29 |
| 9 | González Armendáriz | 19 |
| 10 | Firma contable en Nuevo León | 28 |
| 11 | Respaldo de una firma sólida | 28 |
| 12 | Contabilidad, impuestos y más | 29 |
| 13 | Primera reunión con un socio | 28 |
| 14 | Agende una consulta | 19 |
| 15 | Propuesta por escrito | 21 |

| # | Descripción | Car. |
|---|---|---|
| 1 | Más de 28 años y 400 empresas respaldadas en Nuevo León. Agende una consulta con un socio. | 90 |
| 2 | Contabilidad, impuestos y estados financieros en una sola firma. Oficina en San Pedro. | 86 |
| 3 | Le entregamos una propuesta por escrito con alcance, calendario y honorarios. | 77 |
| 4 | Un equipo de 30 especialistas en contabilidad, impuestos y auditoría. Hablemos. | 79 |

**Anuncio B: Beneficio para el director**

| # | Título | Car. |
|---|---|---|
| 1 | Contabilidad para empresas | 26 |
| 2 | Contabilidad para pymes | 23 |
| 3 | Servicios contables Monterrey | 29 |
| 4 | Su contabilidad al día | 22 |
| 5 | Contador externo para empresas | 30 |
| 6 | Impuestos presentados a tiempo | 30 |
| 7 | Menos riesgo de multas | 22 |
| 8 | Cifras claras cada mes | 22 |
| 9 | Estados financieros mensuales | 29 |
| 10 | Respaldo ante el SAT | 20 |
| 11 | Ponemos al día su contabilidad | 30 |
| 12 | Contabilidad electrónica | 24 |
| 13 | Revisión de sus facturas CFDI | 29 |
| 14 | Enfóquese en dirigir | 20 |
| 15 | Un responsable para su cuenta | 29 |

| # | Descripción | Car. |
|---|---|---|
| 1 | Sus impuestos presentados a tiempo y sus cifras claras cada mes. Agende una consulta. | 85 |
| 2 | Revisamos sus facturas y su contabilidad para reducir riesgos ante el SAT. | 74 |
| 3 | ¿Contabilidad atrasada? La ponemos al día con un plan claro y fechas por escrito. | 81 |
| 4 | Estados financieros explicados en lenguaje sencillo, para decidir con certeza. | 78 |

**Anuncio C: Local y acción**

| # | Título | Car. |
|---|---|---|
| 1 | Contabilidad para empresas | 26 |
| 2 | Servicios contables Monterrey | 29 |
| 3 | Contabilidad empresarial | 24 |
| 4 | Su contabilidad al día | 22 |
| 5 | Contador externo para empresas | 30 |
| 6 | Oficina en San Pedro | 20 |
| 7 | Atendemos todo Monterrey | 24 |
| 8 | Agende con un socio hoy | 23 |
| 9 | Reunión presencial o en línea | 29 |
| 10 | Hable con un especialista | 25 |
| 11 | Llámenos o escríbanos | 21 |
| 12 | Empresas de Nuevo León | 22 |
| 13 | Respuesta a la brevedad | 23 |
| 14 | Cambie de contador sin estrés | 29 |
| 15 | Propuesta clara de honorarios | 29 |

| # | Descripción | Car. |
|---|---|---|
| 1 | Visítenos en Av. Lázaro Cárdenas, San Pedro, o agende una reunión en línea. | 75 |
| 2 | Atendemos empresas en Monterrey y su área metropolitana. Agende con un socio hoy. | 81 |
| 3 | Cambiar de contador es sencillo: coordinamos la entrega con su contador anterior. | 81 |
| 4 | Déjenos sus datos y le llamamos para acordar fecha y hora de su consulta. | 73 |

#### Grupo: Contador San Pedro → `/lp/contabilidad-empresas/?v=san-pedro`

**Anuncio A: Autoridad y trayectoria** (título 1 fijado en posición 1)

| # | Título | Car. |
|---|---|---|
| 1 | Contador en San Pedro | 21 |
| 2 | Contadores en San Pedro | 23 |
| 3 | Contador para empresas | 22 |
| 4 | Despacho contable San Pedro | 27 |
| 5 | Contadores en Lázaro Cárdenas | 29 |
| 6 | Más de 28 años de trayectoria | 29 |
| 7 | 400+ empresas respaldadas | 25 |
| 8 | 30 especialistas en una firma | 29 |
| 9 | González Armendáriz | 19 |
| 10 | Firma contable en Nuevo León | 28 |
| 11 | Respaldo de una firma sólida | 28 |
| 12 | Contabilidad, impuestos y más | 29 |
| 13 | Primera reunión con un socio | 28 |
| 14 | Agende una consulta | 19 |
| 15 | Propuesta por escrito | 21 |

| # | Descripción | Car. |
|---|---|---|
| 1 | Más de 28 años y 400 empresas respaldadas en Nuevo León. Agende una consulta con un socio. | 90 |
| 2 | Contabilidad, impuestos y estados financieros en una sola firma. Oficina en San Pedro. | 86 |
| 3 | Le entregamos una propuesta por escrito con alcance, calendario y honorarios. | 77 |
| 4 | Un equipo de 30 especialistas en contabilidad, impuestos y auditoría. Hablemos. | 79 |

**Anuncio B: Beneficio para el director**

| # | Título | Car. |
|---|---|---|
| 1 | Contador en San Pedro | 21 |
| 2 | Contadores en San Pedro | 23 |
| 3 | Contador para empresas | 22 |
| 4 | Contadores en Lázaro Cárdenas | 29 |
| 5 | Oficina en Av. Lázaro Cárdenas | 30 |
| 6 | Impuestos presentados a tiempo | 30 |
| 7 | Menos riesgo de multas | 22 |
| 8 | Cifras claras cada mes | 22 |
| 9 | Estados financieros mensuales | 29 |
| 10 | Respaldo ante el SAT | 20 |
| 11 | Ponemos al día su contabilidad | 30 |
| 12 | Contabilidad electrónica | 24 |
| 13 | Revisión de sus facturas CFDI | 29 |
| 14 | Enfóquese en dirigir | 20 |
| 15 | Un responsable para su cuenta | 29 |

| # | Descripción | Car. |
|---|---|---|
| 1 | Sus impuestos presentados a tiempo y sus cifras claras cada mes. Agende una consulta. | 85 |
| 2 | Revisamos sus facturas y su contabilidad para reducir riesgos ante el SAT. | 74 |
| 3 | ¿Contabilidad atrasada? La ponemos al día con un plan claro y fechas por escrito. | 81 |
| 4 | Estados financieros explicados en lenguaje sencillo, para decidir con certeza. | 78 |

**Anuncio C: Local y acción**

| # | Título | Car. |
|---|---|---|
| 1 | Contador en San Pedro | 21 |
| 2 | Contador para empresas | 22 |
| 3 | Despacho contable San Pedro | 27 |
| 4 | Contadores en Lázaro Cárdenas | 29 |
| 5 | Oficina en Av. Lázaro Cárdenas | 30 |
| 6 | Oficina en San Pedro | 20 |
| 7 | Atendemos todo Monterrey | 24 |
| 8 | Agende con un socio hoy | 23 |
| 9 | Reunión presencial o en línea | 29 |
| 10 | Hable con un especialista | 25 |
| 11 | Llámenos o escríbanos | 21 |
| 12 | Empresas de Nuevo León | 22 |
| 13 | Respuesta a la brevedad | 23 |
| 14 | Cambie de contador sin estrés | 29 |
| 15 | Propuesta clara de honorarios | 29 |

| # | Descripción | Car. |
|---|---|---|
| 1 | Visítenos en Av. Lázaro Cárdenas, San Pedro, o agende una reunión en línea. | 75 |
| 2 | Atendemos empresas en Monterrey y su área metropolitana. Agende con un socio hoy. | 81 |
| 3 | Cambiar de contador es sencillo: coordinamos la entrega con su contador anterior. | 81 |
| 4 | Déjenos sus datos y le llamamos para acordar fecha y hora de su consulta. | 73 |

### GS | Asesoría Fiscal | MTY

Ruta visible: `gonzalezarmendariz.com/asesoria-fiscal/monterrey`

#### Grupo: Asesoría fiscal empresas → `/lp/asesoria-fiscal/`

**Anuncio A: Autoridad y trayectoria** (título 1 fijado en posición 1)

| # | Título | Car. |
|---|---|---|
| 1 | Asesoría fiscal en Monterrey | 28 |
| 2 | Asesoría fiscal para empresas | 29 |
| 3 | Asesor fiscal para su empresa | 29 |
| 4 | Consultoría fiscal empresarial | 30 |
| 5 | Asesor fiscal en San Pedro | 26 |
| 6 | Más de 28 años de trayectoria | 29 |
| 7 | 400+ empresas respaldadas | 25 |
| 8 | González Armendáriz | 19 |
| 9 | Especialistas en impuestos | 26 |
| 10 | Primera reunión con un socio | 28 |
| 11 | Firma fiscal en Nuevo León | 26 |
| 12 | Recomendación por escrito | 25 |
| 13 | Agende una consulta | 19 |
| 14 | 30 especialistas en una firma | 29 |
| 15 | Respaldo de una firma sólida | 28 |

| # | Descripción | Car. |
|---|---|---|
| 1 | Más de 28 años asesorando empresas de Nuevo León. Agende una consulta con un socio. | 83 |
| 2 | Planeación fiscal dentro del marco legal, con sustento y razón de negocio. | 74 |
| 3 | Le entregamos una recomendación clara y por escrito, con sus riesgos y alternativas. | 84 |
| 4 | Especialistas en impuestos empresariales. Oficina en San Pedro Garza García. | 76 |

**Anuncio B: Beneficio para el director**

| # | Título | Car. |
|---|---|---|
| 1 | Asesoría fiscal en Monterrey | 28 |
| 2 | Asesoría fiscal para empresas | 29 |
| 3 | Asesor fiscal para su empresa | 29 |
| 4 | Asesor fiscal en San Pedro | 26 |
| 5 | Despacho fiscal en Monterrey | 28 |
| 6 | Decisiones con menos riesgo | 27 |
| 7 | Conozca el impacto fiscal | 25 |
| 8 | Dentro del marco legal | 22 |
| 9 | Reduzca riesgos fiscales | 24 |
| 10 | Sin esquemas agresivos | 22 |
| 11 | Devoluciones de IVA | 19 |
| 12 | Análisis con números claros | 27 |
| 13 | Al día con cambios fiscales | 27 |
| 14 | Segunda opinión fiscal | 22 |
| 15 | Acompañamiento ante el SAT | 26 |

| # | Descripción | Car. |
|---|---|---|
| 1 | Conozca el efecto fiscal de sus decisiones antes de tomarlas. Hable con un socio. | 81 |
| 2 | ¿Recibió una carta o requerimiento del SAT? Revisamos su caso y respondemos en plazo. | 85 |
| 3 | Planeación fiscal anual, devoluciones de IVA y acompañamiento en revisiones del SAT. | 84 |
| 4 | Trabajamos en coordinación con su contador actual. Agende una consulta. | 71 |

**Anuncio C: Local y acción**

| # | Título | Car. |
|---|---|---|
| 1 | Asesoría fiscal en Monterrey | 28 |
| 2 | Asesor fiscal para su empresa | 29 |
| 3 | Consultoría fiscal empresarial | 30 |
| 4 | Asesor fiscal en San Pedro | 26 |
| 5 | Despacho fiscal en Monterrey | 28 |
| 6 | Oficina en San Pedro | 20 |
| 7 | Atendemos todo Monterrey | 24 |
| 8 | Agende con un socio hoy | 23 |
| 9 | Reunión presencial o en línea | 29 |
| 10 | Hable con un especialista | 25 |
| 11 | Llámenos o escríbanos | 21 |
| 12 | Empresas de Nuevo León | 22 |
| 13 | Respuesta a la brevedad | 23 |
| 14 | Revise su caso con nosotros | 27 |
| 15 | Trabajamos con su contador | 26 |

| # | Descripción | Car. |
|---|---|---|
| 1 | Visítenos en Av. Lázaro Cárdenas, San Pedro, o agende una reunión en línea. | 75 |
| 2 | Atendemos empresas en Monterrey y su área metropolitana. Agende con un socio hoy. | 81 |
| 3 | Déjenos sus datos y le llamamos para acordar fecha y hora de su consulta. | 73 |
| 4 | Antes de firmar una operación importante, revise su efecto fiscal con nosotros. | 79 |

#### Grupo: Cartas y requerimientos SAT → `/lp/asesoria-fiscal/?v=sat`

**Anuncio A: Autoridad y trayectoria** (título 1 fijado en posición 1)

| # | Título | Car. |
|---|---|---|
| 1 | ¿Le llegó una carta del SAT? | 28 |
| 2 | Respuesta a requerimientos SAT | 30 |
| 3 | Asesoría ante el SAT | 20 |
| 4 | Carta invitación del SAT | 24 |
| 5 | Revisión del SAT a su empresa | 29 |
| 6 | Más de 28 años de trayectoria | 29 |
| 7 | 400+ empresas respaldadas | 25 |
| 8 | González Armendáriz | 19 |
| 9 | Especialistas en impuestos | 26 |
| 10 | Primera reunión con un socio | 28 |
| 11 | Firma fiscal en Nuevo León | 26 |
| 12 | Recomendación por escrito | 25 |
| 13 | Agende una consulta | 19 |
| 14 | 30 especialistas en una firma | 29 |
| 15 | Respaldo de una firma sólida | 28 |

| # | Descripción | Car. |
|---|---|---|
| 1 | Más de 28 años asesorando empresas de Nuevo León. Agende una consulta con un socio. | 83 |
| 2 | Planeación fiscal dentro del marco legal, con sustento y razón de negocio. | 74 |
| 3 | Le entregamos una recomendación clara y por escrito, con sus riesgos y alternativas. | 84 |
| 4 | Especialistas en impuestos empresariales. Oficina en San Pedro Garza García. | 76 |

**Anuncio B: Beneficio para el director**

| # | Título | Car. |
|---|---|---|
| 1 | ¿Le llegó una carta del SAT? | 28 |
| 2 | Respuesta a requerimientos SAT | 30 |
| 3 | Asesoría ante el SAT | 20 |
| 4 | Revisión del SAT a su empresa | 29 |
| 5 | Respondemos dentro del plazo | 28 |
| 6 | Decisiones con menos riesgo | 27 |
| 7 | Conozca el impacto fiscal | 25 |
| 8 | Dentro del marco legal | 22 |
| 9 | Reduzca riesgos fiscales | 24 |
| 10 | Sin esquemas agresivos | 22 |
| 11 | Devoluciones de IVA | 19 |
| 12 | Análisis con números claros | 27 |
| 13 | Al día con cambios fiscales | 27 |
| 14 | Segunda opinión fiscal | 22 |
| 15 | Acompañamiento ante el SAT | 26 |

| # | Descripción | Car. |
|---|---|---|
| 1 | Conozca el efecto fiscal de sus decisiones antes de tomarlas. Hable con un socio. | 81 |
| 2 | ¿Recibió una carta o requerimiento del SAT? Revisamos su caso y respondemos en plazo. | 85 |
| 3 | Planeación fiscal anual, devoluciones de IVA y acompañamiento en revisiones del SAT. | 84 |
| 4 | Trabajamos en coordinación con su contador actual. Agende una consulta. | 71 |

**Anuncio C: Local y acción**

| # | Título | Car. |
|---|---|---|
| 1 | ¿Le llegó una carta del SAT? | 28 |
| 2 | Asesoría ante el SAT | 20 |
| 3 | Carta invitación del SAT | 24 |
| 4 | Revisión del SAT a su empresa | 29 |
| 5 | Respondemos dentro del plazo | 28 |
| 6 | Oficina en San Pedro | 20 |
| 7 | Atendemos todo Monterrey | 24 |
| 8 | Agende con un socio hoy | 23 |
| 9 | Reunión presencial o en línea | 29 |
| 10 | Hable con un especialista | 25 |
| 11 | Llámenos o escríbanos | 21 |
| 12 | Empresas de Nuevo León | 22 |
| 13 | Respuesta a la brevedad | 23 |
| 14 | Revise su caso con nosotros | 27 |
| 15 | Trabajamos con su contador | 26 |

| # | Descripción | Car. |
|---|---|---|
| 1 | Visítenos en Av. Lázaro Cárdenas, San Pedro, o agende una reunión en línea. | 75 |
| 2 | Atendemos empresas en Monterrey y su área metropolitana. Agende con un socio hoy. | 81 |
| 3 | Déjenos sus datos y le llamamos para acordar fecha y hora de su consulta. | 73 |
| 4 | Antes de firmar una operación importante, revise su efecto fiscal con nosotros. | 79 |

#### Grupo: Planeación fiscal → `/lp/asesoria-fiscal/?v=planeacion`

**Anuncio A: Autoridad y trayectoria** (título 1 fijado en posición 1)

| # | Título | Car. |
|---|---|---|
| 1 | Planeación fiscal empresarial | 29 |
| 2 | Planeación fiscal en Monterrey | 30 |
| 3 | Planeación dentro de la ley | 27 |
| 4 | Estrategia fiscal con sustento | 30 |
| 5 | Planeación fiscal anual | 23 |
| 6 | Más de 28 años de trayectoria | 29 |
| 7 | 400+ empresas respaldadas | 25 |
| 8 | González Armendáriz | 19 |
| 9 | Especialistas en impuestos | 26 |
| 10 | Primera reunión con un socio | 28 |
| 11 | Firma fiscal en Nuevo León | 26 |
| 12 | Recomendación por escrito | 25 |
| 13 | Agende una consulta | 19 |
| 14 | 30 especialistas en una firma | 29 |
| 15 | Respaldo de una firma sólida | 28 |

| # | Descripción | Car. |
|---|---|---|
| 1 | Más de 28 años asesorando empresas de Nuevo León. Agende una consulta con un socio. | 83 |
| 2 | Planeación fiscal dentro del marco legal, con sustento y razón de negocio. | 74 |
| 3 | Le entregamos una recomendación clara y por escrito, con sus riesgos y alternativas. | 84 |
| 4 | Especialistas en impuestos empresariales. Oficina en San Pedro Garza García. | 76 |

**Anuncio B: Beneficio para el director**

| # | Título | Car. |
|---|---|---|
| 1 | Planeación fiscal empresarial | 29 |
| 2 | Planeación fiscal en Monterrey | 30 |
| 3 | Planeación dentro de la ley | 27 |
| 4 | Planeación fiscal anual | 23 |
| 5 | Antes de decidir, consúltenos | 29 |
| 6 | Decisiones con menos riesgo | 27 |
| 7 | Conozca el impacto fiscal | 25 |
| 8 | Dentro del marco legal | 22 |
| 9 | Reduzca riesgos fiscales | 24 |
| 10 | Sin esquemas agresivos | 22 |
| 11 | Devoluciones de IVA | 19 |
| 12 | Análisis con números claros | 27 |
| 13 | Al día con cambios fiscales | 27 |
| 14 | Segunda opinión fiscal | 22 |
| 15 | Acompañamiento ante el SAT | 26 |

| # | Descripción | Car. |
|---|---|---|
| 1 | Conozca el efecto fiscal de sus decisiones antes de tomarlas. Hable con un socio. | 81 |
| 2 | ¿Recibió una carta o requerimiento del SAT? Revisamos su caso y respondemos en plazo. | 85 |
| 3 | Planeación fiscal anual, devoluciones de IVA y acompañamiento en revisiones del SAT. | 84 |
| 4 | Trabajamos en coordinación con su contador actual. Agende una consulta. | 71 |

**Anuncio C: Local y acción**

| # | Título | Car. |
|---|---|---|
| 1 | Planeación fiscal empresarial | 29 |
| 2 | Planeación dentro de la ley | 27 |
| 3 | Estrategia fiscal con sustento | 30 |
| 4 | Planeación fiscal anual | 23 |
| 5 | Antes de decidir, consúltenos | 29 |
| 6 | Oficina en San Pedro | 20 |
| 7 | Atendemos todo Monterrey | 24 |
| 8 | Agende con un socio hoy | 23 |
| 9 | Reunión presencial o en línea | 29 |
| 10 | Hable con un especialista | 25 |
| 11 | Llámenos o escríbanos | 21 |
| 12 | Empresas de Nuevo León | 22 |
| 13 | Respuesta a la brevedad | 23 |
| 14 | Revise su caso con nosotros | 27 |
| 15 | Trabajamos con su contador | 26 |

| # | Descripción | Car. |
|---|---|---|
| 1 | Visítenos en Av. Lázaro Cárdenas, San Pedro, o agende una reunión en línea. | 75 |
| 2 | Atendemos empresas en Monterrey y su área metropolitana. Agende con un socio hoy. | 81 |
| 3 | Déjenos sus datos y le llamamos para acordar fecha y hora de su consulta. | 73 |
| 4 | Antes de firmar una operación importante, revise su efecto fiscal con nosotros. | 79 |

### GS | Auditoría | MTY

Ruta visible: `gonzalezarmendariz.com/auditoria/monterrey`

#### Grupo: Auditoría estados financieros → `/lp/auditoria/`

**Anuncio A: Autoridad y trayectoria** (título 1 fijado en posición 1)

| # | Título | Car. |
|---|---|---|
| 1 | Auditoría financiera Monterrey | 30 |
| 2 | Auditoría financiera empresas | 29 |
| 3 | Auditoría de cifras y control | 29 |
| 4 | Auditoría para su empresa | 25 |
| 5 | Auditores en Monterrey | 22 |
| 6 | Más de 28 años de trayectoria | 29 |
| 7 | 400+ empresas respaldadas | 25 |
| 8 | González Armendáriz | 19 |
| 9 | Opinión independiente | 21 |
| 10 | Primera reunión con un socio | 28 |
| 11 | Equipo de auditoría propio | 26 |
| 12 | Agende una consulta | 19 |
| 13 | Propuesta de auditoría | 22 |
| 14 | 30 especialistas en una firma | 29 |
| 15 | Respaldo de una firma sólida | 28 |

| # | Descripción | Car. |
|---|---|---|
| 1 | Auditoría de estados financieros con más de 28 años de trayectoria. Agende una consulta. | 88 |
| 2 | Una opinión independiente sobre sus cifras para socios, bancos, inversionistas y consejo. | 89 |
| 3 | Más de 400 empresas respaldadas en Nuevo León. Oficina en San Pedro Garza García. | 81 |
| 4 | Informe del auditor independiente y carta de recomendaciones de control interno. | 80 |

**Anuncio B: Beneficio para el director**

| # | Título | Car. |
|---|---|---|
| 1 | Auditoría financiera Monterrey | 30 |
| 2 | Auditoría financiera empresas | 29 |
| 3 | Auditoría de cifras y control | 29 |
| 4 | Auditores en Monterrey | 22 |
| 5 | Auditoría con calendario fijo | 29 |
| 6 | Cifras que generan confianza | 28 |
| 7 | Confianza para su banco | 23 |
| 8 | Alcance y fechas por escrito | 28 |
| 9 | Mínima interrupción | 19 |
| 10 | Carta de recomendaciones | 24 |
| 11 | Detecte errores a tiempo | 24 |
| 12 | Mejore sus controles | 20 |
| 13 | Para socios e inversionistas | 28 |
| 14 | Para su consejo | 15 |
| 15 | Hallazgos antes del informe | 27 |

| # | Descripción | Car. |
|---|---|---|
| 1 | ¿Su banco le pide estados financieros auditados? Acordamos alcance y fechas por escrito. | 88 |
| 2 | Revisamos registros y controles con la menor interrupción posible para su equipo. | 81 |
| 3 | Comentamos hallazgos con la dirección antes de emitir el informe final. | 71 |
| 4 | Detecte errores y controles débiles a tiempo. Hable con un socio de la firma. | 77 |

**Anuncio C: Local y acción**

| # | Título | Car. |
|---|---|---|
| 1 | Auditoría financiera Monterrey | 30 |
| 2 | Auditoría de cifras y control | 29 |
| 3 | Auditoría para su empresa | 25 |
| 4 | Auditores en Monterrey | 22 |
| 5 | Auditoría con calendario fijo | 29 |
| 6 | Oficina en San Pedro | 20 |
| 7 | Atendemos todo Monterrey | 24 |
| 8 | Agende con un socio hoy | 23 |
| 9 | Reunión presencial o en línea | 29 |
| 10 | Hable con un especialista | 25 |
| 11 | Llámenos o escríbanos | 21 |
| 12 | Empresas de Nuevo León | 22 |
| 13 | Respuesta a la brevedad | 23 |
| 14 | Solicite su propuesta | 21 |
| 15 | Calendario desde el inicio | 26 |

| # | Descripción | Car. |
|---|---|---|
| 1 | Visítenos en Av. Lázaro Cárdenas, San Pedro, o agende una reunión en línea. | 75 |
| 2 | Atendemos empresas en Monterrey y su área metropolitana. Solicite su propuesta. | 79 |
| 3 | Déjenos sus datos y le llamamos para acordar fecha y hora de su consulta. | 73 |
| 4 | Le entregamos una propuesta de auditoría con alcance, calendario y honorarios. | 78 |

#### Grupo: Auditoría externa → `/lp/auditoria/?v=externa`

**Anuncio A: Autoridad y trayectoria** (título 1 fijado en posición 1)

| # | Título | Car. |
|---|---|---|
| 1 | Auditoría externa Monterrey | 27 |
| 2 | Auditoría externa empresarial | 29 |
| 3 | Despacho de auditoría | 21 |
| 4 | Firma de auditoría Nuevo León | 29 |
| 5 | Auditor externo independiente | 29 |
| 6 | Más de 28 años de trayectoria | 29 |
| 7 | 400+ empresas respaldadas | 25 |
| 8 | González Armendáriz | 19 |
| 9 | Opinión independiente | 21 |
| 10 | Primera reunión con un socio | 28 |
| 11 | Equipo de auditoría propio | 26 |
| 12 | Agende una consulta | 19 |
| 13 | Propuesta de auditoría | 22 |
| 14 | 30 especialistas en una firma | 29 |
| 15 | Respaldo de una firma sólida | 28 |

| # | Descripción | Car. |
|---|---|---|
| 1 | Auditoría de estados financieros con más de 28 años de trayectoria. Agende una consulta. | 88 |
| 2 | Una opinión independiente sobre sus cifras para socios, bancos, inversionistas y consejo. | 89 |
| 3 | Más de 400 empresas respaldadas en Nuevo León. Oficina en San Pedro Garza García. | 81 |
| 4 | Informe del auditor independiente y carta de recomendaciones de control interno. | 80 |

**Anuncio B: Beneficio para el director**

| # | Título | Car. |
|---|---|---|
| 1 | Auditoría externa Monterrey | 27 |
| 2 | Auditoría externa empresarial | 29 |
| 3 | Despacho de auditoría | 21 |
| 4 | Auditor externo independiente | 29 |
| 5 | Auditores en San Pedro | 22 |
| 6 | Cifras que generan confianza | 28 |
| 7 | Confianza para su banco | 23 |
| 8 | Alcance y fechas por escrito | 28 |
| 9 | Mínima interrupción | 19 |
| 10 | Carta de recomendaciones | 24 |
| 11 | Detecte errores a tiempo | 24 |
| 12 | Mejore sus controles | 20 |
| 13 | Para socios e inversionistas | 28 |
| 14 | Para su consejo | 15 |
| 15 | Hallazgos antes del informe | 27 |

| # | Descripción | Car. |
|---|---|---|
| 1 | ¿Su banco le pide estados financieros auditados? Acordamos alcance y fechas por escrito. | 88 |
| 2 | Revisamos registros y controles con la menor interrupción posible para su equipo. | 81 |
| 3 | Comentamos hallazgos con la dirección antes de emitir el informe final. | 71 |
| 4 | Detecte errores y controles débiles a tiempo. Hable con un socio de la firma. | 77 |

**Anuncio C: Local y acción**

| # | Título | Car. |
|---|---|---|
| 1 | Auditoría externa Monterrey | 27 |
| 2 | Despacho de auditoría | 21 |
| 3 | Firma de auditoría Nuevo León | 29 |
| 4 | Auditor externo independiente | 29 |
| 5 | Auditores en San Pedro | 22 |
| 6 | Oficina en San Pedro | 20 |
| 7 | Atendemos todo Monterrey | 24 |
| 8 | Agende con un socio hoy | 23 |
| 9 | Reunión presencial o en línea | 29 |
| 10 | Hable con un especialista | 25 |
| 11 | Llámenos o escríbanos | 21 |
| 12 | Empresas de Nuevo León | 22 |
| 13 | Respuesta a la brevedad | 23 |
| 14 | Solicite su propuesta | 21 |
| 15 | Calendario desde el inicio | 26 |

| # | Descripción | Car. |
|---|---|---|
| 1 | Visítenos en Av. Lázaro Cárdenas, San Pedro, o agende una reunión en línea. | 75 |
| 2 | Atendemos empresas en Monterrey y su área metropolitana. Solicite su propuesta. | 79 |
| 3 | Déjenos sus datos y le llamamos para acordar fecha y hora de su consulta. | 73 |
| 4 | Le entregamos una propuesta de auditoría con alcance, calendario y honorarios. | 78 |

#### Grupo: Estados financieros auditados → `/lp/auditoria/?v=banco`

**Anuncio A: Autoridad y trayectoria** (título 1 fijado en posición 1)

| # | Título | Car. |
|---|---|---|
| 1 | Estados financieros auditados | 29 |
| 2 | Auditoría para su banco | 23 |
| 3 | Cifras auditadas para socios | 28 |
| 4 | Auditoría para inversionistas | 29 |
| 5 | Informe del auditor | 19 |
| 6 | Más de 28 años de trayectoria | 29 |
| 7 | 400+ empresas respaldadas | 25 |
| 8 | González Armendáriz | 19 |
| 9 | Opinión independiente | 21 |
| 10 | Primera reunión con un socio | 28 |
| 11 | Equipo de auditoría propio | 26 |
| 12 | Agende una consulta | 19 |
| 13 | Propuesta de auditoría | 22 |
| 14 | 30 especialistas en una firma | 29 |
| 15 | Respaldo de una firma sólida | 28 |

| # | Descripción | Car. |
|---|---|---|
| 1 | Auditoría de estados financieros con más de 28 años de trayectoria. Agende una consulta. | 88 |
| 2 | Una opinión independiente sobre sus cifras para socios, bancos, inversionistas y consejo. | 89 |
| 3 | Más de 400 empresas respaldadas en Nuevo León. Oficina en San Pedro Garza García. | 81 |
| 4 | Informe del auditor independiente y carta de recomendaciones de control interno. | 80 |

**Anuncio B: Beneficio para el director**

| # | Título | Car. |
|---|---|---|
| 1 | Estados financieros auditados | 29 |
| 2 | Auditoría para su banco | 23 |
| 3 | Cifras auditadas para socios | 28 |
| 4 | Informe del auditor | 19 |
| 5 | Cumpla con su banco a tiempo | 28 |
| 6 | Cifras que generan confianza | 28 |
| 7 | Confianza para su banco | 23 |
| 8 | Alcance y fechas por escrito | 28 |
| 9 | Mínima interrupción | 19 |
| 10 | Carta de recomendaciones | 24 |
| 11 | Detecte errores a tiempo | 24 |
| 12 | Mejore sus controles | 20 |
| 13 | Para socios e inversionistas | 28 |
| 14 | Para su consejo | 15 |
| 15 | Hallazgos antes del informe | 27 |

| # | Descripción | Car. |
|---|---|---|
| 1 | ¿Su banco le pide estados financieros auditados? Acordamos alcance y fechas por escrito. | 88 |
| 2 | Revisamos registros y controles con la menor interrupción posible para su equipo. | 81 |
| 3 | Comentamos hallazgos con la dirección antes de emitir el informe final. | 71 |
| 4 | Detecte errores y controles débiles a tiempo. Hable con un socio de la firma. | 77 |

**Anuncio C: Local y acción**

| # | Título | Car. |
|---|---|---|
| 1 | Estados financieros auditados | 29 |
| 2 | Cifras auditadas para socios | 28 |
| 3 | Auditoría para inversionistas | 29 |
| 4 | Informe del auditor | 19 |
| 5 | Cumpla con su banco a tiempo | 28 |
| 6 | Oficina en San Pedro | 20 |
| 7 | Atendemos todo Monterrey | 24 |
| 8 | Agende con un socio hoy | 23 |
| 9 | Reunión presencial o en línea | 29 |
| 10 | Hable con un especialista | 25 |
| 11 | Llámenos o escríbanos | 21 |
| 12 | Empresas de Nuevo León | 22 |
| 13 | Respuesta a la brevedad | 23 |
| 14 | Solicite su propuesta | 21 |
| 15 | Calendario desde el inicio | 26 |

| # | Descripción | Car. |
|---|---|---|
| 1 | Visítenos en Av. Lázaro Cárdenas, San Pedro, o agende una reunión en línea. | 75 |
| 2 | Atendemos empresas en Monterrey y su área metropolitana. Solicite su propuesta. | 79 |
| 3 | Déjenos sus datos y le llamamos para acordar fecha y hora de su consulta. | 73 |
| 4 | Le entregamos una propuesta de auditoría con alcance, calendario y honorarios. | 78 |

## 11.5 Recursos (extensiones)

**Enlaces de sitio** (texto ≤ 25 · líneas ≤ 35):

| Texto | Línea 1 | Línea 2 | URL |
|---|---|---|---|
| Contabilidad | Impuestos al día cada mes | Estados financieros claros | `/servicios/contabilidad-empresas-monterrey/` |
| Asesoría fiscal | Decisiones con menos riesgo | Planeación dentro de la ley | `/servicios/asesoria-fiscal-monterrey/` |
| Auditoría | Opinión independiente | Para socios y bancos | `/servicios/auditoria-monterrey/` |
| Nosotros | Más de 28 años en Nuevo León | 400+ empresas respaldadas | `/nosotros/` |
| Agendar consulta | Reunión con un socio | Presencial o en línea | `/contacto/` |
| Preguntas frecuentes | Costos, tiempos y proceso | Respuestas claras | `/#faq-title` |

**Textos destacados** (≤ 25): Más de 28 años · 400+ empresas · 30 especialistas · Oficina en San Pedro · Reunión con un socio · Propuesta por escrito · Presencial o en línea · Atención en inglés ([SUPUESTO] "Atención en inglés": confirmar)

**Fragmentos estructurados**: Encabezado *Servicios*: Contabilidad, Asesoría fiscal, Auditoría, Consultoría de negocios, Servicios administrativos.

**Llamada:** 81 8363 4412, con informes de llamadas activados (número de desvío de Google) y conversión "Llamada desde anuncio ≥ 60 s". Programar solo en horario de atención.

**Ubicación:** vincular la ficha de Google Business Profile.

**Imágenes:** 3–5 fotos reales (fachada, sala de juntas, equipo) en 1:1 y 1.91:1. [PENDIENTE: fotografía]

**Logotipo y nombre de empresa:** González Armendáriz + logo cuadrado.

**Formulario de clientes potenciales (opcional, fase 2):** solo si el formulario de la landing convierte por debajo de lo esperado; exige aviso de privacidad enlazado.

## 11.6 Rutina de optimización

| Frecuencia | Tarea |
|---|---|
| Semanal (mes 1–2) | Términos de búsqueda → negativas · revisar conversiones duplicadas · presupuesto limitado |
| Quincenal | Activos con rendimiento "Bajo" → reemplazar · revisar porcentaje de impresiones perdidas por ranking |
| Mensual | Costo por cita real (CRM) por campaña · mover presupuesto a la campaña con menor costo por cita · probar una variante de landing |
| Trimestral | Revisar concordancia amplia + Smart Bidding · evaluar campañas de Fase 2 · actualizar mensajes por temporada fiscal (marzo, abril, mayo, diciembre) |
