# 13. Plan de medición, atribución y privacidad

Objetivo de negocio: consultas calificadas que llegan a cita con un socio. Un clic en teléfono o WhatsApp expresa intención; no demuestra contacto, consulta ni cita. [PENDIENTE: confirmar socios disponibles, CRM, correo receptor, agenda, IDs de cuenta y responsables]. Este documento no instala etiquetas activas.

## Estado del código entregado: handoff a WhatsApp

El prototipo HTML actual prepara una solicitud en WhatsApp y abre la aplicación; no tiene servidor de recepción ni agenda conectada. Su evento es `consultation_handoff` con `channel: whatsapp`: **microconversión secundaria**, nunca `generate_lead`, cita ni confirmación de envío. Abrir WhatsApp no acredita que el usuario haya enviado el mensaje. No usar este evento como objetivo primario de puja.

En el código actual, los eventos están bloqueados salvo que `window.gaConsent.analytics === true`; no existe una CMP instalada ni etiquetas reales. El valor de `language` emitido es `es`/`en`; mapearlo en GTM a `es-MX`/`en-US` si se adopta el contrato definitivo de abajo. `service` y `placement` todavía deben añadirse a los eventos por una integración validada; no inferir que ya están implementados. `generate_lead` se reserva para el backend futuro o una confirmación comercial verificable.

El formulario incluye los cuatro campos en un borrador de mensaje que se dirige a WhatsApp. Debe informarse antes de continuar y el usuario revisa/envía el mensaje en ese canal. Esa transferencia operativa es distinta de la analítica: **desactivar medición automática de clics salientes de GA4** o excluir estos enlaces de modo comprobable, porque el parámetro `text` de `wa.me` contiene datos personales. Ninguna etiqueta debe capturar `link_url`, el texto prellenado, `FormData`, etiquetas de campos o querystrings de ese enlace. Usar exclusivamente los eventos permitidos, sin valores de los campos. El aviso debe identificar este uso de WhatsApp y los terceros involucrados. [PENDIENTE: revisión jurídica y aviso definitivo].

## Diccionario de eventos

| Evento GA4 / dataLayer | Disparador y control | Parámetros permitidos | Uso |
|---|---|---|---|
| `consultation_handoff` | Formulario válido prepara el borrador y abre WhatsApp; no confirma envío. | `channel: whatsapp`, idioma, tipo de página | Secundaria; implementado en prototipo sin tags activos |
| `generate_lead` | El servidor acepta y almacena el formulario; devuelve éxito e ID aleatorio. Emitir una sola vez por ID, no al pulsar Enviar ni al mostrar un error. | `service`, `language`, `form_id`, `lead_id` opaco, `page_type` | Macroconversión provisional; confirmar calidad |
| `click_whatsapp` | Clic real en enlace wa.me; un evento por clic, sin duplicar por listeners | `service`, `language`, `placement` | Microconversión secundaria |
| `click_phone` | Clic en tel:; no es llamada conectada | `language`, `placement`, `service` | Secundaria |
| `click_email` | Clic en mailto:, solo si existe correo confirmado | `language`, `placement` | Secundaria; correo [PENDIENTE] |
| `scroll_75` | Llega al 75% de profundidad; una vez por page_view | `page_type`, `language`, `service` | Diagnóstico, nunca objetivo de puja |
| `qualify_lead` | CRM confirma empresa, necesidad pertinente y consentimiento/canal correcto | ID opaco y estado, sin texto libre | Conversión offline primaria cuando fiable |
| `appointment_booked` | Agenda registra cita real, no mero clic en Agendar | ID opaco, servicio, fecha del evento | Resultado de negocio; reporte y uso de puja según estrategia |
| `appointment_attended` | CRM confirma asistencia | ID opaco, servicio | Calidad y análisis de embudo |

Valores de `service`: `accounting`, `tax_advisory`, `audit`, `business_consulting`, `administrative`, `unspecified`. `language`: `es-MX` o `en-US`. `page_type`: `home`, `service`, `landing`, `contact`, `article`, `other`. `placement`: `hero`, `sticky`, `body`, `footer`. El ID opaco solo se usa donde la configuración y la privacidad lo permitan; no registrar como dimensión personalizada de GA4 por su alta cardinalidad. Puede omitirse de GA4 y mantenerse en el sistema de deduplicación interno.

`scroll_75` es personalizado; el scroll automático de GA4 tiene otro umbral. Si se conserva el automático, nombrar y reportar ambos por separado. En sitios de una sola página o cambios de ruta, reiniciar control tras cada page_view real. Desactivar captura automática de interacciones de formularios si duplica el evento confirmado o transmite campos.

## GTM y etiquetas

1. Un contenedor web GTM, entorno de prueba separado, permisos mínimos y versiones con descripción. IDs `GTM-…`, `G-…`, Ads, Meta y LinkedIn [PENDIENTE]; no inventarlos.
2. Antes de cualquier etiqueta, la CMP fija estado denegado para medición/publicidad no esencial. Propuesta conservadora: modo básico, sin cargar etiquetas de analítica o marketing antes de elección. Consent Mode no sustituye al aviso ni crea consentimiento por sí mismo.
3. GA4 con page_view único por navegación y eventos anteriores. Validar dominios, enlaces entre idiomas y parámetros permitidos. Evitar que URLs, títulos o querystrings contengan PII.
4. Google Ads: Conversion Linker y etiqueta de conversión nativa al éxito, sujetos a consentimiento. Si se usa conversión nativa, la misma importada desde GA4 será secundaria o no se importará; nunca dos objetivos primarios para el mismo lead. Una conversión por interacción es el punto de partida para captación.
5. Meta Pixel: PageView tras consentimiento de marketing; `Lead` exclusivamente al formulario confirmado. No activar Advanced Matching por defecto. Si luego se añade Conversions API, navegador/servidor deben compartir `event_name` y `event_id` para deduplicación. El envío servidor no elude el consentimiento.
6. LinkedIn Insight Tag tras consentimiento de marketing, conversión por evento confirmado o página de éxito accesible únicamente tras envío válido. Evitar contar recargas o acceso directo. Si hay envío navegador y API, usar la deduplicación admitida y probarla antes de activar ambos.
7. CRM recibe la solicitud, asigna responsable y permite marcar calificado, cita y asistencia. Importar conversiones offline con identificadores de clic y base jurídica/consentimiento aplicable. Ventanas, zonas horarias y retención configuradas de forma coherente.

No colocar nombre, empresa, teléfono, correo, mensajes, datos fiscales, RFC ni contenido del formulario en dataLayer, URLs de medición, analytics, logs de frontend, session replay o parámetros publicitarios. Las URLs operativas de WhatsApp con borrador requieren el control específico descrito arriba y jamás deben copiarse a medición. Incluso los datos con hash requieren base jurídica y configuración adecuada: no activar enhanced conversions de forma automática. El backend comercial almacena solo lo necesario con acceso restringido y plazos documentados.

### Contrato de implementación de ejemplo

```js
// Ejecutar solo después del éxito confirmado por el servidor.
// payload.leadId debe ser un UUID aleatorio: nunca teléfono, correo ni hash de estos.
const event = {
  event: 'generate_lead',
  form_id: 'consultation',
  service: 'accounting',
  language: 'es-MX',
  page_type: 'landing',
  lead_id: payload.leadId
};
// El backend aplica idempotencia para el mismo intento.
// El gestor de eventos de la aplicación evita repetir el mismo lead_id.
window.dataLayer = window.dataLayer || [];
window.dataLayer.push(event);
```

Especificación de integración, no código listo para ejecutar sin backend. El objeto `payload` pertenece a la respuesta de la API real. El formulario nunca simula éxito si no hubo entrega. Sanitizar parámetros y aplicar rate limiting, validación y protección antibots accesible. Servidor y CRM deben permitir conciliación sin trasladar PII a medición.

## Conversiones primarias y pujas

Fase inicial: `generate_lead` puede ser primaria si los envíos son reales y el spam está controlado. Clics y scroll siempre secundarios. Al tener suficiente seguimiento fiable, usar `qualify_lead` como primaria y dejar envío/cita como secundarias de diagnóstico, o usar cita como primaria si su volumen lo sostiene. No sumar etapas del mismo lead como éxitos independientes en la misma estrategia. Decidir con datos, no con un umbral de volumen inventado.

`[PENDIENTE]`: plazo de seguimiento, responsable, definición de lead calificado, ventana de atribución, valores económicos por servicio. No inventar ingresos. Informe por servicio, plataforma, idioma y municipio: inversión, formularios válidos, leads calificados, citas agendadas, citas realizadas y coste por cada etapa. Conciliar semanalmente CRM y plataformas; diferencias por consentimiento y modelos de atribución son esperables, no deben corregirse multiplicando eventos.

## Convención UTM

Minúsculas, ASCII, guiones bajos, sin espacios ni datos personales. No etiquetar enlaces internos porque reinician atribución de campaña.

| Parámetro | Convención | Ejemplo |
|---|---|---|
| `utm_source` | plataforma | `google`, `meta`, `linkedin`, `google_business_profile` |
| `utm_medium` | canal | `cpc`, `paid_social`, `organic` |
| `utm_campaign` | canal_servicio_idioma_geo_objetivo_periodo | `search_accounting_es_mty_consulta_2026q4` |
| `utm_content` | grupo_concepto_variante_formato | `local_autoridad_v1_rsa`, `remarketing_claridad_v1_image` |
| `utm_term` | keyword plantilla Ads; omitir social | `{keyword}` |
| `utm_id` | ID estable de campaña | `{campaignid}` en Google; macro validada en cada plataforma |

Ejemplo Google (adaptar campaña y campos sin concatenar duplicados):
`?utm_source=google&utm_medium=cpc&utm_campaign=search_accounting_es_mty_consulta_2026q4&utm_content=local_autoridad_v1_rsa&utm_term={keyword}&utm_id={campaignid}`

Ejemplo Meta:
`?utm_source=meta&utm_medium=paid_social&utm_campaign=remarketing_tax_es_mty_consulta_2026q4&utm_content=visitors_perspectiva_v1_image`

Ejemplo LinkedIn:
`?utm_source=linkedin&utm_medium=paid_social&utm_campaign=prospecting_audit_en_mty_consulta_2026q4&utm_content=finance_review_v1_image`

Mantener autoetiquetado Google y preservar `gclid`, `gbraid`, `wbraid` cuando corresponda. Guardar primera y última atribución en CRM solo con fundamento y configuración de privacidad adecuados; no reutilizar ID publicitarios como identidad pública. Revisar que redirecciones no eliminen parámetros. No usar UTMs como sistema de deduplicación.

## Privacidad para México

Fuente vigente consultada: LFPDPPP expedida el **20 de marzo de 2025**, texto de Cámara de Diputados con **última reforma DOF 14 de noviembre de 2025**. La ley identifica a la Secretaría Anticorrupción y Buen Gobierno; no copiar una plantilla histórica que remita automáticamente al INAI como autoridad vigente. Revisión final por asesor legal [PENDIENTE].

- Aviso simplificado junto al formulario, enlace al integral. Identificar responsable legal real [PENDIENTE], domicilio, finalidades necesarias, finalidades secundarias opcionales, transferencias aplicables, medios ARCO (acceso, rectificación, cancelación y oposición), revocación, limitación de uso, cambios y medios de contacto confirmados. La marca comercial no confirma por sí sola razón social.
- Propuesta de texto breve: “Usaremos sus datos para atender su solicitud de consulta. Consulte cómo los tratamos y ejerza sus derechos en el Aviso de privacidad.” No afirmar confidencialidad absoluta ni añadir captación comercial oculta.
- El formulario conserva cuatro campos: nombre, empresa, teléfono y servicio. Un mecanismo legal de información/consentimiento no agrega preguntas comerciales. Marketing opcional separado, no premarcado; no condiciona la consulta. Guardar evidencia cuando corresponda.
- Banner con “Aceptar todas”, “Rechazar opcionales” y “Configurar”, con jerarquía equivalente. Necesarias, analítica y publicidad separadas; preferencia modificable desde footer. No presentar una única aceptación forzada ni tratar scroll/silencio como aceptación.
- Describir tecnologías, terceros, finalidades y transferencias; establecer conservación y eliminación en formulario, CRM, analytics y respaldos. [PENDIENTE: proveedores reales y plazos]. Esta propuesta de consentimiento es una decisión de diseño prudente; no afirma que México replique literalmente el régimen europeo de cookies.
- Bloquear embeds de mapas, video y trackers no esenciales según su clasificación hasta elección; preferir enlace al mapa. Evitar que un widget de terceros se cargue silenciosamente desde el botón de WhatsApp.
- Probar rechazo, aceptación parcial, revocación y nueva visita. No enviar retrospectivamente la actividad anterior al consentimiento. Consent Mode v2: documentar `analytics_storage`, `ad_storage`, `ad_user_data`, `ad_personalization`; otorgarlos solo conforme a la preferencia válida.

## QA antes del lanzamiento

Con Tag Assistant, GA4 DebugView y herramientas de prueba de Meta/LinkedIn, validar: envío válido una vez; error cero conversiones; doble clic cero duplicados; recarga sin conversión nueva; rechazo sin requests no esenciales; revocación efectiva; ES/EN correctamente etiquetados; click-to-call y WhatsApp medidos solo como clics; scroll al umbral real; parámetros sin PII; atribución preservada; evento CRM conciliado. Probar móvil y desktop. Descargar un registro de pruebas sin datos personales.

Fuentes oficiales consultadas el 5 de octubre de 2026:

- [LFPDPPP vigente, Cámara de Diputados](https://www.diputados.gob.mx/LeyesBiblio/pdf/LFPDPPP.pdf): PDF descargado y texto verificado, reforma 14-11-2025.
- [Google: configurar Consent Mode](https://developers.google.com/tag-platform/security/guides/consent?hl=es): documentación accesible y vigente en la consulta.
- [LinkedIn: Insight Tag FAQs](https://www.linkedin.com/help/lms/answer/a427660): documentación oficial accesible.
- [Meta Business Help](https://www.facebook.com/business/help/952192354843755): contenido dinámico; verificar configuración y requisitos específicos dentro de la cuenta antes de implantar CAPI o remarketing.
