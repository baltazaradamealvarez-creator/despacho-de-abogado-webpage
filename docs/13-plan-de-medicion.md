# 13. Plan de medición: etiquetas, eventos, UTMs y privacidad

Objetivo: saber **cuántas citas genera cada canal y cuánto cuesta cada una**, no solo cuántos clics.

## 13.1 Arquitectura

```
Sitio (dataLayer)  ──►  Google Tag Manager (contenedor web)
                         ├─ Google tag → GA4 (análisis)
                         ├─ Conversión de Google Ads + conversiones mejoradas (puja)
                         ├─ Píxel de Meta (+ API de Conversiones, deduplicada)
                         └─ Insight Tag de LinkedIn
Formulario ──► CRM [PENDIENTE] con UTMs + gclid/fbclid/li_fat_id ──► importación de "cita realizada" a Google Ads
```

El código del sitio ya envía los eventos al `dataLayer` (`site/assets/js/main.js`) y llena los campos ocultos de atribución en el formulario de la landing. Solo falta crear el contenedor y reemplazar `GTM-XXXXXXX`.

## 13.2 Eventos

| Evento en `dataLayer` | Cuándo ocurre | Parámetros | GA4 | Google Ads | Meta | LinkedIn |
|---|---|---|---|---|---|---|
| `generate_lead` | Formulario enviado con éxito (respuesta 200 del servidor) | `form_id`, `service_interest`, `page_type` | `generate_lead` · **evento clave** | **Formulario enviado**: principal, valor 1.0 | `Lead` (+ CAPI) | Conversión "Lead" |
| (vista de página) `/gracias/` | Llegada a la página de gracias | `origen` | `page_view` | Respaldo si falla el evento | — | — |
| `whatsapp_click` | Clic en cualquier enlace `wa.me` | `link_location` (header, hero, contact, float, footer, lp-final) | `whatsapp_click` · **evento clave** | **Clic en WhatsApp**: principal, valor 0.5 | `Contact` | Conversión "Contacto" |
| `phone_click` | Clic en `tel:` | `link_location`, `phone_number` | `phone_click` · **evento clave** | Clic en teléfono: secundaria (observación) | `Contact` | — |
| (Google Ads) llamada desde anuncio | Llamada ≥ 60 s desde la extensión de llamada | — | — | **Llamada desde anuncio ≥ 60 s**: principal, valor 1.0 | — | — |
| `email_click` | Clic en `mailto:` | `link_location` | `email_click` | — | — | — |
| `scroll_75` | El usuario llega al 75 % de la página (una vez) | `percent_scrolled` | `scroll_75` | Audiencia de remarketing | — | — |
| `form_start` | Primera tecla en el formulario | `form_id` | `form_start` | — | — | — |
| `form_error` | El envío falla | `form_id` | `form_error` | — | — | — |
| `cta_click` | Clic en "Agendar una consulta" | `link_location`, `link_text` | `cta_click` | — | — | — |
| `map_open` | El usuario pide cargar el mapa | — | `map_open` | — | — | — |
| `consent_update` | Acepta o rechaza cookies | `consent` | — | — | — | — |

Notas:
- En GA4, **desactive** "Desplazamientos" en la medición mejorada (mide el 90 %) para no duplicar con `scroll_75`.
- Registre `link_location`, `service_interest` y `form_id` como **dimensiones personalizadas** (ámbito evento) en GA4.
- Los valores de conversión (1.0 / 0.5) son relativos [SUPUESTO]. Cuando haya datos del CRM, ajústelos al valor real de un cliente por servicio.
- **Conversiones mejoradas para leads (Google Ads):** activar en GTM con la variable de datos proporcionados por el usuario que lee el teléfono del formulario (se envía cifrado con SHA-256). Mejora la atribución y permite importar citas desde el CRM.

## 13.3 Contenedor de Google Tag Manager

**Convención de nombres:** `Tipo | Plataforma | Detalle` (p. ej. `Tag | GA4 | Evento generate_lead`).

**Variables**
- `DLV - form_id`, `DLV - service_interest`, `DLV - link_location`, `DLV - phone_number`, `DLV - page_type`, `DLV - percent_scrolled`
- `Const - GA4 Measurement ID` = `G-XXXXXXX` · `Const - Ads Conversion ID` = `AW-XXXXXXX`
- `Const - Meta Pixel ID` · `Const - LinkedIn Partner ID`
- `UPD - Teléfono formulario` (datos proporcionados por el usuario, selector CSS `input[name=telefono]`)

**Activadores**
- `CE - generate_lead`, `CE - whatsapp_click`, `CE - phone_click`, `CE - email_click`, `CE - scroll_75`, `CE - form_start`, `CE - cta_click`
- `Page View - Gracias` (Page Path empieza con `/gracias`)
- `Consent Init - All Pages`

**Etiquetas**
| Etiqueta | Activador | Consentimiento requerido |
|---|---|---|
| Google tag (GA4 + Ads) | Initialization – All Pages | `analytics_storage` / `ad_storage` (Consent Mode avanzado) |
| GA4 – Evento (una por evento de la tabla) | CE correspondiente | `analytics_storage` |
| Google Ads – Conversión "Formulario enviado" + conversiones mejoradas | `CE - generate_lead` | `ad_storage`, `ad_user_data` |
| Google Ads – Conversión "Clic en WhatsApp" | `CE - whatsapp_click` | `ad_storage` |
| Google Ads – Conversión "Clic en teléfono (web)" | `CE - phone_click` | `ad_storage` |
| Google Ads – Remarketing | All Pages | `ad_storage`, `ad_personalization` |
| Conversion Linker | All Pages | — |
| Meta Pixel – Base (PageView) | All Pages | `ad_storage` |
| Meta Pixel – Lead (con `eventID` para deduplicar con CAPI) | `CE - generate_lead` | `ad_storage` |
| Meta Pixel – Contact | `CE - whatsapp_click`, `CE - phone_click` | `ad_storage` |
| LinkedIn Insight Tag – Base | All Pages | `ad_storage` |
| LinkedIn – Conversión Lead | `CE - generate_lead` | `ad_storage` |

**API de Conversiones de Meta:** con el plugin oficial de Meta para WordPress, la *Conversions API Gateway* o un contenedor de GTM del lado del servidor. Use el mismo `event_id` en navegador y servidor para no contar doble.

**Publicación:** pruebe en modo vista previa de GTM + DebugView de GA4 + Tag Assistant + Meta Pixel Helper + LinkedIn Insight Tag Helper. Publique con nombre de versión y descripción.

## 13.4 Convención de UTMs

Reglas: todo en minúsculas, sin acentos ni espacios, palabras unidas con guion bajo `_`. Una hoja compartida registra cada URL etiquetada.

| Parámetro | Valores | Ejemplo |
|---|---|---|
| `utm_source` | `google` · `meta` · `linkedin` · `gbp` · `newsletter` · `whatsapp` | `linkedin` |
| `utm_medium` | `cpc` (búsqueda pagada) · `paid_social` · `organic` (GBP) · `email` | `paid_social` |
| `utm_campaign` | `<canal>_<servicio>_<audiencia o geo>` | `gs_contabilidad_mty` · `meta_rmk_contabilidad` · `li_asesoria_fiscal_directores` · `gbp` |
| `utm_content` | anuncio o pieza: `<concepto>_<formato>` | `c1_calendario_1x1` · `rsa_a` |
| `utm_term` | keyword (Google) o conjunto de anuncios (social) | `{keyword}` · `rmk_landing_14d` |

**Google Ads** (sufijo de URL final a nivel cuenta; etiquetado automático `gclid` activado):
```
utm_source=google&utm_medium=cpc&utm_campaign={_camp}&utm_content={creative}&utm_term={keyword}
```
Parámetro personalizado `{_camp}` por campaña: `gs_contabilidad_mty`, `gs_asesoria_fiscal_mty`, `gs_auditoria_mty`, `gs_marca`.

**Meta** (parámetros de URL del anuncio; Meta reemplaza las variables):
```
utm_source=meta&utm_medium=paid_social&utm_campaign={{campaign.name}}&utm_content={{ad.name}}&utm_term={{adset.name}}
```
Nombre las campañas y anuncios en Meta con la misma convención (minúsculas, guion bajo).

**LinkedIn** (por campaña):
```
utm_source=linkedin&utm_medium=paid_social&utm_campaign=li_asesoria_fiscal_directores&utm_content=c1_antes_de_firmar
```

**Google Business Profile:** `?utm_source=gbp&utm_medium=organic&utm_campaign=gbp` (sitio) y `&utm_campaign=gbp_citas` (enlace de citas). Sin esto, GA4 mezcla ese tráfico con el orgánico de Google.

## 13.5 Del formulario a la cita (cierre del ciclo)
1. El formulario envía nombre, empresa, teléfono, servicio + UTMs + `gclid`/`fbclid`/`li_fat_id` al CRM [PENDIENTE: definir CRM; HubSpot gratuito es suficiente al inicio].
2. Etapas del CRM: Solicitud → Contactado → **Cita realizada** → Propuesta enviada → Cliente.
3. Cada semana se importan a Google Ads las "Citas realizadas" con su `gclid` (importación de conversiones offline). Cuando haya volumen (≥ 30 al mes), se usa como conversión principal de puja.
4. Tablero mensual (Looker Studio): costo por solicitud, costo por cita y costo por cliente, por canal y por servicio.

## 13.6 Privacidad y cumplimiento (México)

> Esto es una guía práctica, no asesoría legal. Validar con el abogado de la firma.

**Marco:** Ley Federal de Protección de Datos Personales en Posesión de los Particulares (LFPDPPP). En marzo de 2025 se publicó una nueva ley que sustituyó a la de 2010 y trasladó las funciones del INAI a la Secretaría Anticorrupción y Buen Gobierno [verificar el estado vigente con su asesor].

**Aviso de privacidad integral** (`/aviso-de-privacidad/`), con al menos:
1. Identidad y domicilio del responsable: González Armendáriz, S.C., Av. Lázaro Cárdenas 2400 Pte., Edificio Losoles, Int. PB 18, San Pedro Garza García, N.L., 66260.
2. Datos que se recaban: nombre, empresa, teléfono, servicio de interés y datos de navegación (cookies, IP, identificadores publicitarios).
3. Finalidades **primarias** (contactarle y atender su solicitud) y **secundarias** (envío de Perspectivas, publicidad personalizada), con un mecanismo sencillo para negarse a las secundarias.
4. Transferencias y encargados: proveedores de hospedaje, CRM, Google, Meta y LinkedIn (como encargados de medición y publicidad).
5. Medios para ejercer derechos ARCO (acceso, rectificación, cancelación y oposición) y revocar el consentimiento: correo y plazo de respuesta [PENDIENTE: correo del responsable de datos].
6. **Sección de cookies** (`#cookies`): qué tecnologías se usan (GA4, Google Ads, Píxel de Meta, Insight Tag de LinkedIn), para qué, y cómo desactivarlas (botón "Configurar cookies" + instrucciones del navegador).
7. Procedimiento para comunicar cambios al aviso y fecha de última actualización.
8. Versión en inglés (`/en/privacy-notice/`).

**Aviso simplificado junto a cada formulario** (ya incluido en el código, con enlace al integral). Texto recomendado:
> "González Armendáriz, S.C. usará sus datos para contactarle sobre su solicitud. Consulte nuestro aviso de privacidad."

**Banner de cookies** (incluido en `site/`):
- Informa, enlaza al aviso y ofrece **Aceptar** y **Rechazar** con el mismo peso visual.
- Conectado a **Google Consent Mode v2**. [SUPUESTO] Para visitantes de México: medición activa por defecto con opción de rechazo (modelo de aviso + oposición que permite la ley mexicana). Para visitantes del Espacio Económico Europeo, Reino Unido y Suiza: todo denegado hasta que acepten.
- En WordPress puede sustituirse por Complianz o CookieYes, configurados igual.
- Guardar el registro de la elección (fecha y versión del aviso).

**Otros puntos legales**
- No pedir datos sensibles en formularios ni por WhatsApp (estados de cuenta, contraseñas del SAT).
- Testimonios y logos de clientes: solo con **autorización por escrito** (y cuidado con el secreto profesional).
- Términos de WhatsApp Business: responder solo a quien inicia la conversación; no enviar promociones masivas sin consentimiento.
- Conservar los leads solo el tiempo necesario [PENDIENTE: política de retención, p. ej. 24 meses si no se vuelven clientes].
