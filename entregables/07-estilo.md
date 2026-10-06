# 07. Guía de estilo

Dirección: firma corporativa premium, serena y precisa. El prestigio se comunica mediante orden, espacio y hechos verificables; sin insignias inventadas, ilustraciones de monedas ni fotografías genéricas de apretones de manos.

## Color

| Token | HEX | Uso |
|---|---|---|
| Marino | #102A35 | Texto, header, botón principal |
| Marfil | #F5F2EB | Fondo principal |
| Bronce | #896B43 | Acento, reglas y detalles; nunca único indicador |
| Blanco | #FFFFFF | Formularios y superficies puntuales |
| Gris texto | #51636A | Texto secundario sobre blanco/marfil |
| Borde | #CBCBC1 | Separadores; campos usan borde más oscuro |

Contraste AA debe verificarse por combinación y tamaño final, incluido hover, error, disabled y foco. Marino sobre marfil supera el mínimo 4.5:1. Bronce sobre marfil ronda el umbral para texto normal: usarlo principalmente en detalles o texto grande; no asumir cumplimiento del componente por el color aislado. Links de texto subrayados, errores con texto además de color. Campos borde #65727A, foco de 3 px bronce con separación de 5 px; sobre marino, foco blanco.

## Tipografía y escala

Máximo dos familias. Implementación entregada: Cormorant para titulares e Inter para cuerpo, alojadas en el mismo dominio en WOFF2, con `font-display:swap`; Georgia y Arial son únicamente fallbacks del sistema. Cormorant usa peso 500 e Inter es variable: cargar un único archivo por familia, y utilizar solo los pesos necesarios. Solo precargar la fuente verdaderamente crítica.

| Elemento | Móvil | Escritorio | Interlineado |
|---|---:|---:|---:|
| H1 | 38–44 px | 64–72 px | 1.05–1.12 |
| H2 | 30–34 px | 42–48 px | 1.15 |
| H3 | 23–26 px | 26–28 px | 1.2 |
| Cuerpo | 17 px | 18 px | 1.6 |
| Labels/menú | 16 px | 16 px | 1.4 |
| Nota legal | 14 px | 14 px | 1.5 |

Usar `clamp()` y rem; permitir zoom 200% y reflow a 320 CSS px. No convertir párrafos a mayúsculas. Longitud máxima 60–70 caracteres por línea. Negritas en ideas concretas, no bloques completos.

## Componentes

Espaciado en múltiplos de 8 px. Padding de sección 64 px móvil / 104 px escritorio; gaps 24–40 px. Radios discretos 2–6 px. Bordes finos y sombras mínimas. Botones mínimo 48 px alto, padding 14×24 px; etiqueta principal «Agendar una consulta» también en el formulario. Nunca «Consulta gratuita» sin validación. Enlaces y controles con objetivo táctil recomendado de 44×44 px; sin iconos sin nombre accesible. Botón WhatsApp con nombre «Contactar por WhatsApp», marino o verde oscuro validado, sin parpadeos.

Formulario: labels permanentes, no solo placeholders; `autocomplete=name`, `organization`, `tel`; teléfono `type=tel`, sin patrón restrictivo a un solo país; select de cinco servicios y opción de orientación. Mensajes inline y resumen de error; no borrar datos al fallar. Estado de envío anunciado mediante región viva. Protección antispam preferentemente servidor/honeypot con controles de accesibilidad, sin CAPTCHA intrusivo por defecto.

## Fotografía, movimiento y accesibilidad

Solo equipo, fundador y oficina reales con licencia y consentimiento. Tratamiento frío o blanco y negro, luz natural y fondos limpios. Exportar AVIF/WebP con fallback y tamaños `srcset`; ancho/alto explícitos; alt describe la imagen concreta. Una textura o divisor decorativo tiene `alt=""`. La fotografía real del fundador podría llevar «Alejandro González, Director Fundador de González Armendáriz»; no aplicar ese alt a un placeholder. LCP no usa lazy loading; imágenes bajo el pliegue sí. Se entregan imágenes OG de marca ES/EN de 1200×630 px en assets/social-es.png y social-en.png. [PENDIENTE: aprobación de marca y URL pública definitiva].

Transiciones de 180–250 ms en controles, aparición opcional 350 ms, sin paralaje ni carruseles. Respetar `prefers-reduced-motion`. HTML semántico, tabulación natural, estados expandidos correctos, contraste AA y lectores de pantalla. No deshabilitar selección, zoom ni menú contextual. El mapa tiene título accesible y una alternativa textual con dirección.

La escala anterior es la referencia editorial para las páginas interiores. El home entregado utiliza una escala de portada más amplia: H1 `clamp(46px,6.6vw,100px)`, H2 `clamp(37px,4.1vw,62px)`; la landing H1 `clamp(44px,5vw,72px)`. El ancho exterior del prototipo llega a 1512 px, manteniendo párrafos en 65 caracteres. Validar legibilidad final de todos los textos secundarios en móvil y no trasladar tamaños de etiquetas a párrafos largos.

La implementación final usa cuerpo base de 16 px, con textos de tarjetas, FAQ y etiquetas a 16 px y notas de formulario/contacto a 14 px. La marca conserva el logo real, sin redibujarlo ni inventar un monograma. Color de foco final: #896B43, outline de 3 px, sujeto a contraste en cada superficie y pruebas de teclado. Los tamaños de ceja editorial son decorativos y no sustituyen información sustantiva.

El bronce de acento #896B43 sobre marfil mide 4.42:1: se reserva para reglas, foco y elementos gráficos. El número pequeño de las tarjetas usa #765B38, una variante más oscura que cumple contraste de texto. Marino sobre marfil:13.37:1; gris sobre marfil:5.62:1.
