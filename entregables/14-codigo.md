# 14. HTML/CSS completo y responsive

Se entrega código fuente real en `site/`, sin WordPress, WPBakery, dependencias de front ni proceso de compilación. Puede servirse en un servidor estático y también usarse como base para plantillas de un tema WordPress ligero. El archivo generador `build_site.py` conserva el vínculo con el copy JSON; no se necesita Python para servir las páginas ya generadas.

## Archivos incluidos

| Página | HTML |
|---|---|
| Home ES | `site/index.html` |
| Home EN | `site/en/index.html` |
| LP Contabilidad ES | `site/lp/contabilidad/index.html` |
| LP Fiscal ES | `site/lp/asesoria-fiscal/index.html` |
| LP Auditoría ES | `site/lp/auditoria/index.html` |
| LP Accounting EN | `site/en/lp/accounting/index.html` |
| LP Tax Advisory EN | `site/en/lp/tax-advisory/index.html` |
| LP Audit EN | `site/en/lp/audit/index.html` |
| CSS completo compartido | `site/assets/site.css` |
| Formulario, mapa y eventos | `site/assets/site.js` |
| Banner configurable de consentimiento | `site/assets/consent.js` |
| Fuentes locales y licencias | `site/assets/*.woff2`, `OFL-*.txt` |
| Retrato real, logo e icono existentes | `fundador.webp`, `logo.png`, `favicon.png` |
| Imágenes sociales de marca ES/EN | `social-es.png`, `social-en.png` |

La ampliación implementa el sitio completo: catálogo y cinco servicios, Nosotros, Equipo, Contacto, Perspectivas, seis guías, archivo histórico, tres landings y páginas de soporte, en ambos idiomas. Son 76 rutas más una página 404. El inventario está en `site/route-manifest.json`. La navegación es local y funciona en Render. Las doce entradas históricas sin traducción original tienen resúmenes ingleses identificados como tales; las tres traducciones originales se preservan completas.

El archivo histórico incluye fechas originales y advertencias de desactualización. Las páginas de privacidad y cookies explican el funcionamiento actual y conservan explícita la necesidad de un aviso integral aprobado. No se inventaron vacantes ni perfiles. `sitemap.xml` contiene únicamente las 36 rutas indexables actuales; landings, archivo y páginas legales provisionales quedan excluidos.

## Funcionamiento y límites concretos

El home contiene exactamente siete secciones; las cinco tarjetas no repiten el catálogo en otra sección. La landing no tiene menú ni enlaces de servicios; conserva selector de idioma, contacto y enlaces legales. Hay un único H1 por HTML, metas ES/EN, JSON-LD embebido, FAQ accesibles con details/summary, logo real y retrato del fundador descargados del sitio existente. El mapa no afirma coordenadas ni pin comprobados: busca la dirección provista, se carga solo tras una acción del usuario y dispone de enlace alternativo.

[SUPUESTO] Mientras no exista un endpoint autorizado de captación, los cuatro campos preparan una solicitud en WhatsApp. El usuario debe enviar el mensaje; después la firma confirma la cita. El formulario no guarda datos en servidor ni confirma una reserva. Si falla la apertura de una ventana, aparece un enlace alternativo. Sin JavaScript, el botón de envío permanece desactivado y se ofrecen enlaces de teléfono y WhatsApp. No se envían formularios de prueba a terceros durante las validaciones.

Para captación propia: reemplazar el manejador por POST a un endpoint real, validar en servidor, registrar el mínimo necesario, notificar al responsable y devolver éxito/error. Emitir `generate_lead` solo tras confirmación real. Identificadores GA4, Google Ads, Meta, LinkedIn, CRM y correo receptor permanecen [PENDIENTE]. El handoff de WhatsApp es `consultation_handoff`, secundario; las señales de clic no se cuentan como citas.

El código no instala etiquetas de publicidad. La función de eventos usa una lista acotada de parámetros y no envía los cuatro campos. No se coloca información del formulario en la URL de la página: solo en el enlace a WhatsApp que el usuario decide abrir. Bloquear la captura automática de URLs de salida y redactar la query de wa.me en cualquier herramienta futura; allí sí hay datos que se envían a WhatsApp para solicitar contacto.

## Banner y privacidad

El banner opcional está incluido, pero permanece inactivo mientras no existan herramientas opcionales que consentir. Para probarlo, declarar antes de los scripts:

```html
<script>
window.GA_SITE_SETTINGS = {
  optionalTagsEnabled: true,
  policyVersion: "[PENDIENTE: versión del aviso aprobado]"
};
</script>
```

Reemplazar la versión pendiente por la versión legal aprobada. El banner ofrece aceptar, rechazar y configurar analítica/publicidad separadamente, más reapertura desde el footer. Sus preferencias quedan en almacenamiento local; no es un registro central de consentimiento ni un CMP certificado. El evento `ga:consent-change` sirve para integrar el CMP/GTM real; por sí solo no carga GA4 ni píxeles. Una versión distinta vuelve a pedir preferencias. Configurar bloqueo previo, revocación de etiquetas y validación legal antes de activarlo. La aceptación no debe activar publicidad si el usuario solo aceptó analítica.

[PENDIENTE] Publicar aviso integral/simplificado, política de cookies, identidad del responsable, canal ARCO y reglas de tratamiento para WhatsApp. Los enlaces legales del HTML son destinos finales, no documentos jurídicos aprobados. No lanzar publicidad ni captación productiva hasta resolverlos. El archivo15 contiene la verificación de lanzamiento.

## Uso local

Desde la carpeta del paquete:

```bash
python -m http.server 8000 --directory site
```

Abrir `http://localhost:8000/` o `http://localhost:8000/lp/contabilidad/`. El sitio servido solo necesita HTML, CSS, JS y los activos locales. Copiar la carpeta assets junto con las rutas; no subir solo el HTML. Los scripts de validación requieren Playwright/axe/Lighthouse y son herramientas de revisión, no dependencias del sitio.

Ver resultados y capturas en `validacion/`. Las pruebas locales no acreditan PageSpeed ni Core Web Vitals del WordPress publicado: medir el hosting final con los plugins, etiquetas y consentimiento reales.
