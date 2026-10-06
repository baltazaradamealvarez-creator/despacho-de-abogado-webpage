# González Armendáriz · paquete de rediseño

## Render

Este repositorio contiene `render.yaml` para publicar `site/` como **Static Site**. En Render: **New → Blueprint**, conectar este repositorio y seleccionar **`claude/rediseno-gonzalez-armendariz`**. No se necesita servidor de aplicaciones ni variables de entorno. Instrucciones completas en [RENDER.md](RENDER.md).

La entrega vigente está en `entregables/` y en `INFORME.html` / `INFORME.pdf`. El borrador anterior se conserva en `archive/initial-draft/`; los archivos anteriores de `docs/` y `ads/` son referencia histórica y están sustituidos por los entregables vigentes.

Revisión: 6 de octubre de 2026. Fuente primaria: briefing del cliente y sitio público gonzalezarmendariz.com, auditado en español e inglés. Los datos del briefing prevalecen cuando el sitio discrepa. Véase fuentes/auditoria.md para evidencia, límites y activos.

## Lectura y contenido

Abrir INFORME.html para el documento completo de los quince entregables en el orden solicitado. INFORME.md es su versión editable. Los documentos individuales están en entregables/, el código listo para servir en site/, datos estructurados en schemas/, plantillas de migración en deployment-templates/ y resultados de revisión en validacion/.

El paquete incluye copy ES/EN de inicio, cinco servicios, Nosotros, Equipo, Contacto, índices de servicios y Perspectivas; tres landings con traducciones; arquitectura y metas; calendario y auditoría de 18 posts; estrategias de SEO local/Google Ads/Meta/LinkedIn y medición. Los RSA están también en CSV/JSON: 36 piezas, 18 por idioma.

## Código y alcance

El sitio completo contiene **76 páginas** en español e inglés y una página 404: inicio, catálogo, cinco servicios, Nosotros, Equipo, Contacto, Perspectivas, seis guías, archivo de publicaciones, tres landings, privacidad, cookies y oportunidades profesionales. Todos los enlaces de navegación permanecen en el sitio desplegado. `site/route-manifest.json` contiene el inventario y las equivalencias de idioma.

```bash
python3 -m http.server 8000 --directory site
```

Para regenerar las páginas: `python3 -m pip install -r requirements-build.txt` y `python3 build_site.py`. Render sirve el HTML ya generado y no necesita instalar dependencias. Los cambios en la rama configurada disparan el despliegue automático.

Las guías nuevas están en `entregables/guias-web.json`. El archivo conserva las publicaciones del WordPress con fecha original y advertencia de posible desactualización. Las doce publicaciones que no tenían versión inglesa cuentan con un resumen inglés identificado como tal y enlace al original. Las tres traducciones originales se conservan completas. El archivo usa `noindex,follow` y queda fuera del sitemap.

El formulario entrega los datos a una conversación de WhatsApp que el usuario debe enviar, sin afirmar una cita confirmada. No hay receptor de formularios/CRM configurado. Las etiquetas están apagadas y el banner se puede probar mediante la configuración documentada en 14. La validación técnica no envió mensajes reales.

## Pendientes de lanzamiento

[PENDIENTE] Horarios, pin/coordenadas, correo, costo de la consulta, alcances definitivos, perfiles/cargos actuales, certificaciones y permisos de imagen; logos/testimonios autorizados; textos de privacidad y responsable; endpoint/CRM y cuentas de medición/Ads. Los marcadores son instrucciones internas y se retiran del contenido público antes de lanzar.

[SUPUESTO] Año editorial 2027; datos/cifras del briefing vigentes; solución provisional de contacto por WhatsApp; dominio HTTPS sin www propuesto sujeto a Search Console. No hay cifras de volumen de keywords, presupuesto ni resultados de campaña inventados. Las estrategias no garantizan posiciones, ahorro fiscal ni ausencia de auditorías SAT.

Los objetivos de rendimiento y los resultados locales se distinguen en validacion/RESUMEN.md. Antes de producción aplicar la checklist 15, validar el aviso integral de privacidad y confirmar los alcances comerciales.

## Verificación del sitio completo

- `python3 validate_static.py`: rutas, enlaces, anchors, H1, metas y equivalencias de idioma.
- Opcional: `npm install`, iniciar el servidor local en el puerto 8775 y ejecutar `npm run validate:browser` / `npm run validate:flows`. Requieren Chromium; `CHROME_PATH` permite indicar otro ejecutable. `GA_TEST_URL` permite cambiar la URL local.
- Evidencia actual: `validacion/paginas-completas-*.json` y `validacion/lighthouse-servicio-completo.json`. Las capturas locales no forman parte del despliegue.
