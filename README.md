# González Armendáriz · paquete de rediseño

## Render

Este repositorio contiene `render.yaml` para publicar `site/` como **Static Site**. En Render: **New → Blueprint**, conectar este repositorio y seleccionar **`claude/rediseno-gonzalez-armendariz`**. No se necesita servidor de aplicaciones ni variables de entorno. Instrucciones completas en [RENDER.md](RENDER.md).

La entrega vigente está en `entregables/` y en `INFORME.html` / `INFORME.pdf`. El borrador anterior se conserva en `archive/initial-draft/`; los archivos anteriores de `docs/` y `ads/` son referencia histórica y están sustituidos por los entregables vigentes.

Revisión: 6 de octubre de 2026. Fuente primaria: briefing del cliente y sitio público gonzalezarmendariz.com, auditado en español e inglés. Los datos del briefing prevalecen cuando el sitio discrepa. Véase fuentes/auditoria.md para evidencia, límites y activos.

## Lectura y contenido

Abrir INFORME.html para el documento completo de los quince entregables en el orden solicitado. INFORME.md es su versión editable. Los documentos individuales están en entregables/, el código listo para servir en site/, datos estructurados en schemas/, plantillas de migración en deployment-templates/ y resultados de revisión en validacion/.

El paquete incluye copy ES/EN de inicio, cinco servicios, Nosotros, Equipo, Contacto, índices de servicios y Perspectivas; tres landings con traducciones; arquitectura y metas; calendario y auditoría de 18 posts; estrategias de SEO local/Google Ads/Meta/LinkedIn y medición. Los RSA están también en CSV/JSON: 36 piezas, 18 por idioma.

## Código y alcance

Hay dos homes y seis landings HTML, CSS y JS sin dependencias de front. Para verlos:

```bash
python -m http.server 8000 --directory site
```

Abrir http://localhost:8000/ y http://localhost:8000/lp/contabilidad/. Los enlaces ES/EN de esas plantillas funcionan dentro del paquete. Los enlaces a páginas interiores apuntan a su futura ruta de producción: sus textos están redactados, pero el encargo de código incluía solo home y landing. La publicación del código en GitHub no reemplaza el WordPress público ni activa campañas o etiquetas.

El formulario entrega los datos a una conversación de WhatsApp que el usuario debe enviar, sin afirmar una cita confirmada. No hay receptor de formularios/CRM configurado. Las etiquetas están apagadas y el banner se puede probar mediante la configuración documentada en 14. La validación técnica no envió mensajes reales.

## Pendientes de lanzamiento

[PENDIENTE] Horarios, pin/coordenadas, correo, costo de la consulta, alcances definitivos, perfiles/cargos actuales, certificaciones y permisos de imagen; logos/testimonios autorizados; textos de privacidad y responsable; endpoint/CRM y cuentas de medición/Ads. Los marcadores son instrucciones internas y se retiran del contenido público antes de lanzar.

[SUPUESTO] Año editorial 2027; datos/cifras del briefing vigentes; solución provisional de contacto por WhatsApp; dominio HTTPS sin www propuesto sujeto a Search Console. No hay cifras de volumen de keywords, presupuesto ni resultados de campaña inventados. Las estrategias no garantizan posiciones, ahorro fiscal ni ausencia de auditorías SAT.

Los objetivos de rendimiento y los resultados locales se distinguen en validacion/RESUMEN.md. Antes de producción aplicar la checklist 15, validar aviso de privacidad y publicar todas las rutas finales.
