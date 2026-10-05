#!/usr/bin/env python3
"""Genera la estructura de Google Ads de González Armendáriz.

Salidas:
  ads/google-ads-editor-anuncios.csv   anuncios responsivos (RSA) para Google Ads Editor
  ads/google-ads-editor-keywords.csv   palabras clave y negativas para Google Ads Editor
  docs/11-google-ads.md                documento con estructura, keywords, negativas y anuncios

Valida que cada título tenga ≤ 30 caracteres, cada descripción ≤ 90, rutas ≤ 15,
que no haya signos de exclamación ni títulos repetidos dentro del mismo anuncio.
Uso:  python3 ads/generar_google_ads.py
"""
import csv
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://gonzalezarmendariz.com"

# ---------------------------------------------------------------------------
# Datos
# ---------------------------------------------------------------------------
LOCAL_C = [  # tema C (local + acción), común a las tres campañas
    "Oficina en San Pedro", "Atendemos todo Monterrey", "Agende con un socio hoy",
    "Reunión presencial o en línea", "Hable con un especialista", "Llámenos o escríbanos",
    "Empresas de Nuevo León", "Respuesta a la brevedad",
]

CAMPAIGNS = [
    {
        "name": "GS | Contabilidad | MTY",
        "camp_param": "gs_contabilidad_mty",
        "lp": "/lp/contabilidad-empresas/",
        "path": ("contabilidad", "monterrey"),
        "budget_share": "45 %",
        "themes": {
            "A": ["Más de 28 años de trayectoria", "400+ empresas respaldadas", "30 especialistas en una firma",
                  "González Armendáriz", "Firma contable en Nuevo León", "Respaldo de una firma sólida",
                  "Contabilidad, impuestos y más", "Primera reunión con un socio", "Agende una consulta",
                  "Propuesta por escrito"],
            "B": ["Impuestos presentados a tiempo", "Menos riesgo de multas", "Cifras claras cada mes",
                  "Estados financieros mensuales", "Respaldo ante el SAT", "Ponemos al día su contabilidad",
                  "Contabilidad electrónica", "Revisión de sus facturas CFDI", "Enfóquese en dirigir",
                  "Un responsable para su cuenta"],
            "C": LOCAL_C + ["Cambie de contador sin estrés", "Propuesta clara de honorarios"],
        },
        "descriptions": {
            "A": ["Más de 28 años y 400 empresas respaldadas en Nuevo León. Agende una consulta con un socio.",
                  "Contabilidad, impuestos y estados financieros en una sola firma. Oficina en San Pedro.",
                  "Le entregamos una propuesta por escrito con alcance, calendario y honorarios.",
                  "Un equipo de 30 especialistas en contabilidad, impuestos y auditoría. Hablemos."],
            "B": ["Sus impuestos presentados a tiempo y sus cifras claras cada mes. Agende una consulta.",
                  "Revisamos sus facturas y su contabilidad para reducir riesgos ante el SAT.",
                  "¿Contabilidad atrasada? La ponemos al día con un plan claro y fechas por escrito.",
                  "Estados financieros explicados en lenguaje sencillo, para decidir con certeza."],
            "C": ["Visítenos en Av. Lázaro Cárdenas, San Pedro, o agende una reunión en línea.",
                  "Atendemos empresas en Monterrey y su área metropolitana. Agende con un socio hoy.",
                  "Cambiar de contador es sencillo: coordinamos la entrega con su contador anterior.",
                  "Déjenos sus datos y le llamamos para acordar fecha y hora de su consulta."],
        },
        "groups": [
            {
                "name": "Despacho contable", "v": "despacho",
                "kw_headlines": ["Despacho contable en Monterrey", "Despacho contable empresarial",
                                 "Firma de contadores Monterrey", "Despacho contable y fiscal",
                                 "Contadores para su empresa", "Despacho contable en San Pedro"],
                "keywords": [("despacho contable monterrey", "Exact"), ("despacho contable monterrey", "Phrase"),
                             ("despacho de contadores monterrey", "Phrase"), ("despacho contable para empresas", "Phrase"),
                             ("firma de contadores monterrey", "Exact"), ("despacho contable nuevo leon", "Phrase"),
                             ("despacho contable y fiscal", "Phrase")],
            },
            {
                "name": "Contabilidad para empresas", "v": "",
                "kw_headlines": ["Contabilidad para empresas", "Contabilidad para pymes",
                                 "Servicios contables Monterrey", "Contabilidad empresarial",
                                 "Su contabilidad al día", "Contador externo para empresas"],
                "keywords": [("contabilidad para empresas monterrey", "Exact"), ("contabilidad para empresas", "Phrase"),
                             ("servicios contables para empresas", "Phrase"), ("servicios de contabilidad monterrey", "Phrase"),
                             ("contabilidad para pymes", "Phrase"), ("contador externo para empresa", "Phrase"),
                             ("outsourcing contable monterrey", "Phrase")],
            },
            {
                "name": "Contador San Pedro", "v": "san-pedro",
                "kw_headlines": ["Contador en San Pedro", "Contadores en San Pedro", "Contador para empresas",
                                 "Despacho contable San Pedro", "Contadores en Lázaro Cárdenas",
                                 "Oficina en Av. Lázaro Cárdenas"],
                "keywords": [("contador san pedro garza garcia", "Exact"), ("contador en san pedro garza garcia", "Phrase"),
                             ("contadores en san pedro", "Phrase"), ("contador para empresas san pedro", "Phrase"),
                             ("despacho contable san pedro garza garcia", "Phrase")],
            },
        ],
    },
    {
        "name": "GS | Asesoría Fiscal | MTY",
        "camp_param": "gs_asesoria_fiscal_mty",
        "lp": "/lp/asesoria-fiscal/",
        "path": ("asesoria-fiscal", "monterrey"),
        "budget_share": "30 %",
        "themes": {
            "A": ["Más de 28 años de trayectoria", "400+ empresas respaldadas", "González Armendáriz",
                  "Especialistas en impuestos", "Primera reunión con un socio", "Firma fiscal en Nuevo León",
                  "Recomendación por escrito", "Agende una consulta", "30 especialistas en una firma",
                  "Respaldo de una firma sólida"],
            "B": ["Decisiones con menos riesgo", "Conozca el impacto fiscal", "Dentro del marco legal",
                  "Reduzca riesgos fiscales", "Sin esquemas agresivos", "Devoluciones de IVA",
                  "Análisis con números claros", "Al día con cambios fiscales", "Segunda opinión fiscal",
                  "Acompañamiento ante el SAT"],
            "C": LOCAL_C + ["Revise su caso con nosotros", "Trabajamos con su contador"],
        },
        "descriptions": {
            "A": ["Más de 28 años asesorando empresas de Nuevo León. Agende una consulta con un socio.",
                  "Planeación fiscal dentro del marco legal, con sustento y razón de negocio.",
                  "Le entregamos una recomendación clara y por escrito, con sus riesgos y alternativas.",
                  "Especialistas en impuestos empresariales. Oficina en San Pedro Garza García."],
            "B": ["Conozca el efecto fiscal de sus decisiones antes de tomarlas. Hable con un socio.",
                  "¿Recibió una carta o requerimiento del SAT? Revisamos su caso y respondemos en plazo.",
                  "Planeación fiscal anual, devoluciones de IVA y acompañamiento en revisiones del SAT.",
                  "Trabajamos en coordinación con su contador actual. Agende una consulta."],
            "C": ["Visítenos en Av. Lázaro Cárdenas, San Pedro, o agende una reunión en línea.",
                  "Atendemos empresas en Monterrey y su área metropolitana. Agende con un socio hoy.",
                  "Déjenos sus datos y le llamamos para acordar fecha y hora de su consulta.",
                  "Antes de firmar una operación importante, revise su efecto fiscal con nosotros."],
        },
        "groups": [
            {
                "name": "Asesoría fiscal empresas", "v": "",
                "kw_headlines": ["Asesoría fiscal en Monterrey", "Asesoría fiscal para empresas",
                                 "Asesor fiscal para su empresa", "Consultoría fiscal empresarial",
                                 "Asesor fiscal en San Pedro", "Despacho fiscal en Monterrey"],
                "keywords": [("asesoria fiscal monterrey", "Exact"), ("asesoría fiscal para empresas", "Phrase"),
                             ("asesor fiscal monterrey", "Phrase"), ("consultoria fiscal monterrey", "Phrase"),
                             ("asesor fiscal san pedro garza garcia", "Phrase"), ("despacho fiscal monterrey", "Phrase"),
                             ("asesoria fiscal empresas nuevo leon", "Phrase")],
            },
            {
                "name": "Cartas y requerimientos SAT", "v": "sat",
                "kw_headlines": ["¿Le llegó una carta del SAT?", "Respuesta a requerimientos SAT",
                                 "Asesoría ante el SAT", "Carta invitación del SAT",
                                 "Revisión del SAT a su empresa", "Respondemos dentro del plazo"],
                "keywords": [("requerimiento del sat empresa", "Phrase"), ("carta invitacion sat", "Phrase"),
                             ("asesoria requerimiento sat", "Phrase"), ("revision del sat a empresa", "Phrase"),
                             ("asesor para auditoria del sat", "Phrase"), ("multa del sat empresa", "Phrase")],
            },
            {
                "name": "Planeación fiscal", "v": "planeacion",
                "kw_headlines": ["Planeación fiscal empresarial", "Planeación fiscal en Monterrey",
                                 "Planeación dentro de la ley", "Estrategia fiscal con sustento",
                                 "Planeación fiscal anual", "Antes de decidir, consúltenos"],
                "keywords": [("planeacion fiscal empresas", "Phrase"), ("planeacion fiscal monterrey", "Exact"),
                             ("planeación fiscal para empresas", "Phrase"), ("estrategia fiscal empresa", "Phrase"),
                             ("asesoria fiscal reestructura empresa", "Phrase")],
            },
        ],
    },
    {
        "name": "GS | Auditoría | MTY",
        "camp_param": "gs_auditoria_mty",
        "lp": "/lp/auditoria/",
        "path": ("auditoria", "monterrey"),
        "budget_share": "25 %",
        "themes": {
            "A": ["Más de 28 años de trayectoria", "400+ empresas respaldadas", "González Armendáriz",
                  "Opinión independiente", "Primera reunión con un socio", "Equipo de auditoría propio",
                  "Agende una consulta", "Propuesta de auditoría", "30 especialistas en una firma",
                  "Respaldo de una firma sólida"],
            "B": ["Cifras que generan confianza", "Confianza para su banco", "Alcance y fechas por escrito",
                  "Mínima interrupción", "Carta de recomendaciones", "Detecte errores a tiempo",
                  "Mejore sus controles", "Para socios e inversionistas", "Para su consejo",
                  "Hallazgos antes del informe"],
            "C": LOCAL_C + ["Solicite su propuesta", "Calendario desde el inicio"],
        },
        "descriptions": {
            "A": ["Auditoría de estados financieros con más de 28 años de trayectoria. Agende una consulta.",
                  "Una opinión independiente sobre sus cifras para socios, bancos, inversionistas y consejo.",
                  "Más de 400 empresas respaldadas en Nuevo León. Oficina en San Pedro Garza García.",
                  "Informe del auditor independiente y carta de recomendaciones de control interno."],
            "B": ["¿Su banco le pide estados financieros auditados? Acordamos alcance y fechas por escrito.",
                  "Revisamos registros y controles con la menor interrupción posible para su equipo.",
                  "Comentamos hallazgos con la dirección antes de emitir el informe final.",
                  "Detecte errores y controles débiles a tiempo. Hable con un socio de la firma."],
            "C": ["Visítenos en Av. Lázaro Cárdenas, San Pedro, o agende una reunión en línea.",
                  "Atendemos empresas en Monterrey y su área metropolitana. Solicite su propuesta.",
                  "Déjenos sus datos y le llamamos para acordar fecha y hora de su consulta.",
                  "Le entregamos una propuesta de auditoría con alcance, calendario y honorarios."],
        },
        "groups": [
            {
                "name": "Auditoría estados financieros", "v": "",
                "kw_headlines": ["Auditoría financiera Monterrey", "Auditoría financiera empresas",
                                 "Auditoría de cifras y control", "Auditoría para su empresa",
                                 "Auditores en Monterrey", "Auditoría con calendario fijo"],
                "keywords": [("auditoria de estados financieros monterrey", "Exact"),
                             ("auditoría de estados financieros", "Phrase"), ("auditoria financiera empresas", "Phrase"),
                             ("auditoria financiera monterrey", "Phrase"), ("auditores monterrey", "Phrase")],
            },
            {
                "name": "Auditoría externa", "v": "externa",
                "kw_headlines": ["Auditoría externa Monterrey", "Auditoría externa empresarial",
                                 "Despacho de auditoría", "Firma de auditoría Nuevo León",
                                 "Auditor externo independiente", "Auditores en San Pedro"],
                "keywords": [("auditoria externa monterrey", "Exact"), ("auditoría externa empresas", "Phrase"),
                             ("despacho de auditoria monterrey", "Phrase"), ("auditor externo monterrey", "Phrase"),
                             ("firma de auditoria monterrey", "Phrase"), ("auditores san pedro garza garcia", "Phrase")],
            },
            {
                "name": "Estados financieros auditados", "v": "banco",
                "kw_headlines": ["Estados financieros auditados", "Auditoría para su banco",
                                 "Cifras auditadas para socios", "Auditoría para inversionistas",
                                 "Informe del auditor", "Cumpla con su banco a tiempo"],
                "keywords": [("estados financieros auditados", "Phrase"), ("estados financieros auditados para banco", "Phrase"),
                             ("estados financieros dictaminados", "Phrase"), ("auditoria para credito bancario", "Phrase")],
            },
        ],
    },
]

NEG_COMMON = [
    # gratis / precio
    "gratis", "gratuito", "gratuita", "barato", "económico",
    # formación
    "curso", "cursos", "diplomado", "maestría", "licenciatura", "carrera", "universidad", "uanl",
    "tesis", "ensayo", "tarea", "pdf", "libro", "ejemplo", "ejemplos", "formato", "plantilla", "excel",
    # informativas
    "qué es", "que es", "definición", "concepto", "significado", "tipos de", "wikipedia",
    # empleo
    "empleo", "empleos", "vacante", "vacantes", "trabajo", "bolsa de trabajo", "sueldo", "salario",
    "prácticas", "practicas", "becario", "occ", "indeed", "computrabajo",
    # trámites que el usuario hace solo
    "cita sat", "citas sat", "portal sat", "sat.gob.mx", "contraseña sat", "e.firma", "efirma",
    "constancia de situación fiscal", "rfc", "buzón tributario", "imss semanas", "infonavit",
    # software
    "software", "programa", "app", "contpaqi", "aspel", "descargar",
    # personas físicas de bajo ticket / plataformas
    "resico", "uber", "didi", "airbnb", "mercado libre",
    # otras ciudades
    "cdmx", "ciudad de méxico", "guadalajara", "querétaro", "puebla", "tijuana", "saltillo", "chihuahua",
]
NEG_AUDITORIA = ["auditoría interna curso", "auditoría de sistemas", "auditoría informática", "auditoría médica",
                 "auditoría de calidad", "iso 9001", "auditor iso", "auditoría ambiental", "auditoría superior",
                 "asf", "auditoría gubernamental", "auditor lider"]
NEG_FISCAL = ["declaración anual personas físicas", "devolución de impuestos personas físicas", "declaración anual asalariados"]

# Rotación de títulos con keyword por anuncio (índices de kw_headlines)
KW_ROTATION = {"A": [0, 1, 2, 3, 4], "B": [0, 1, 2, 4, 5], "C": [0, 2, 3, 4, 5]}
THEME_NAMES = {"A": "Autoridad y trayectoria", "B": "Beneficio para el director", "C": "Local y acción"}

# ---------------------------------------------------------------------------
errors = []


def check(text, limit, where):
    if len(text) > limit:
        errors.append(f"{where}: {len(text)}/{limit} → {text}")
    if "!" in text or "¡" in text:
        errors.append(f"{where}: signo de exclamación → {text}")


def esc(text):
    """Escapa la barra vertical dentro de tablas Markdown."""
    return text.replace("|", "\\|")


def final_url(c, g):
    return BASE + c["lp"] + (f"?v={g['v']}" if g["v"] else "")


ads = []
for c in CAMPAIGNS:
    check(c["path"][0], 15, "path1"); check(c["path"][1], 15, "path2")
    for g in c["groups"]:
        for t in "ABC":
            heads = [g["kw_headlines"][i] for i in KW_ROTATION[t]] + c["themes"][t]
            if len(heads) != 15:
                errors.append(f"{c['name']}/{g['name']}/{t}: {len(heads)} títulos")
            if len(set(h.lower() for h in heads)) != len(heads):
                errors.append(f"{c['name']}/{g['name']}/{t}: títulos repetidos")
            for h in heads:
                check(h, 30, f"{c['name']}/{g['name']}/{t} título")
            descs = c["descriptions"][t]
            for d in descs:
                check(d, 90, f"{c['name']}/{g['name']}/{t} descripción")
            ads.append({"c": c, "g": g, "t": t, "heads": heads, "descs": descs})

if errors:
    print("\n".join(errors))
    sys.exit(1)

# ---------------------------------------------------------------------------
# CSV para Google Ads Editor
# ---------------------------------------------------------------------------
os.makedirs(os.path.join(ROOT, "ads"), exist_ok=True)
with open(os.path.join(ROOT, "ads", "google-ads-editor-anuncios.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["Campaign", "Ad group", "Ad type"] + [f"Headline {i}" for i in range(1, 16)]
               + ["Headline 1 position"] + [f"Description {i}" for i in range(1, 5)]
               + ["Final URL", "Path 1", "Path 2", "Labels"])
    for a in ads:
        w.writerow([a["c"]["name"], a["g"]["name"], "Responsive search ad"] + a["heads"]
                   + ["1" if a["t"] == "A" else ""] + a["descs"]
                   + [final_url(a["c"], a["g"]), a["c"]["path"][0], a["c"]["path"][1], f"RSA-{a['t']}"])

with open(os.path.join(ROOT, "ads", "google-ads-editor-keywords.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["Campaign", "Ad group", "Keyword", "Criterion Type"])
    for c in CAMPAIGNS:
        for g in c["groups"]:
            for kw, mt in g["keywords"]:
                w.writerow([c["name"], g["name"], kw, mt])
        extra = NEG_AUDITORIA if "Auditoría" in c["name"] else NEG_FISCAL if "Fiscal" in c["name"] else []
        for n in NEG_COMMON + extra:
            w.writerow([c["name"], "", n, "Campaign Negative Phrase"])

# ---------------------------------------------------------------------------
# Documento
# ---------------------------------------------------------------------------
L = []
A = L.append
A("# 11. Google Ads: estructura, palabras clave, negativas y anuncios\n")
A("> Documento generado por `ads/generar_google_ads.py`. Para cambiar anuncios o keywords, edite el script y vuelva a ejecutarlo; "
  "también regenera los CSV para Google Ads Editor (`ads/google-ads-editor-anuncios.csv` y `ads/google-ads-editor-keywords.csv`). "
  "Todos los títulos tienen ≤ 30 caracteres y todas las descripciones ≤ 90 (validado por el script).\n")
A("## 11.1 Estructura de la cuenta\n")
A("| Campaña | Presupuesto sugerido | Landing | Grupos de anuncios (por intención) |")
A("|---|---|---|---|")
for c in CAMPAIGNS:
    A(f"| **{esc(c['name'])}** | {c['budget_share']} del total | `{c['lp']}` | " + " · ".join(g["name"] for g in c["groups"]) + " |")
A("| **GS \\| Marca** (recomendada) | 3–5 % | `/` | González Armendáriz (exacta y frase). Protege la marca a bajo costo |")
A("| **Fase 2**: GS \\| Outsourcing administrativo \\| MTY | según resultados | `/lp/servicios-administrativos/` (por crear) | Outsourcing administrativo · Nómina · Cobranza |")
A("| **Fase 2**: GS \\| Accounting EN \\| MX | según resultados | `/en/` o landing EN (por crear) | accounting firm Monterrey Mexico · tax advisor Monterrey |")
A("")
A("**Presupuesto total:** [PENDIENTE]. Referencia: para tener datos útiles en 60 días, cada campaña necesita suficiente presupuesto para ~10 clics diarios en horario laboral. "
  "Revise el CPC estimado en el Planificador de palabras clave antes de definirlo.\n")
A("**Configuración por campaña**")
A("- Red: solo Búsqueda (desactivar Red de Display y socios de búsqueda al inicio).")
A("- **Ubicación:** Monterrey, San Pedro Garza García, San Nicolás de los Garza, Guadalupe, Santa Catarina, Apodaca y General Escobedo. "
  "Opción de ubicación: **\"Presencia: personas que están o suelen estar en sus ubicaciones\"** (no \"interés\"), para no pagar clics de otras ciudades.")
A("- **Ajuste San Pedro Garza García:** +20 % mientras la puja sea manual o *Maximizar clics*. Cuando pase a *CPA objetivo* los ajustes de puja dejan de aplicar; "
  "si San Pedro convierte claramente mejor, sepárelo en una campaña propia con su presupuesto.")
A("- **Idioma:** español (y inglés, porque muchos directivos usan Google en inglés).")
A("- **Puja:** inicio con *Maximizar conversiones* (con la conversión \"Formulario enviado\" + \"Clic en WhatsApp\" + \"Llamada ≥ 60 s\" como principales). "
  "Al llegar a ~30 conversiones en 30 días, pasar a *CPA objetivo*. Más adelante, importar citas realizadas desde el CRM (conversiones offline con `gclid`) y optimizar a esa conversión.")
A("- **Concordancias:** exacta y de frase al inicio. Concordancia amplia solo cuando la campaña tenga historial de conversiones y Smart Bidding activo.")
A("- **Horario:** lunes a viernes 7:00–20:00 y sábado 8:00–14:00 [SUPUESTO: ajustar al horario real de atención telefónica].")
A("- **Rotación:** 3 anuncios por grupo (A, B y C). Fijar (pin) solo el título 1 del anuncio A en la posición 1 para asegurar el message match; los anuncios B y C sin fijaciones.")
A("- **URL final:** la landing + `?v=` del grupo (ver tabla de variantes en `05-landing-pages.md`). Etiquetado automático (`gclid`) activado y sufijo de URL final con UTMs (ver `13-plan-de-medicion.md`).\n")

A("## 11.2 Palabras clave por grupo\n")
A("Notación: `[exacta]`, `\"frase\"`.\n")
for c in CAMPAIGNS:
    A(f"### {c['name']}\n")
    A("| Grupo | Palabras clave | URL final |")
    A("|---|---|---|")
    for g in c["groups"]:
        kws = " · ".join(f"`[{k}]`" if m == "Exact" else f"`\"{k}\"`" for k, m in g["keywords"])
        A(f"| {g['name']} | {kws} | `{final_url(c, g).replace(BASE, '')}` |")
    A("")

A("## 11.3 Palabras clave negativas\n")
A("**Lista compartida \"Negativas generales\"** (concordancia de frase, aplicar a todas las campañas):\n")
A(" · ".join(f"`{n}`" for n in NEG_COMMON) + "\n")
A("**Solo campaña Auditoría:** " + " · ".join(f"`{n}`" for n in NEG_AUDITORIA) + "\n")
A("**Solo campaña Asesoría Fiscal:** " + " · ".join(f"`{n}`" for n in NEG_FISCAL) + " (búsquedas de personas físicas de bajo valor)\n")
A("**Negativas cruzadas (evitan que las campañas compitan entre sí):** en Contabilidad, negar `auditoría` y `auditor`; en Auditoría, negar `contador` y `contabilidad`; "
  "en Contabilidad, negar `asesoría fiscal` y `planeación fiscal`.\n")
A("Revisión semanal del informe de términos de búsqueda durante los primeros 2 meses; después, quincenal.\n")

A("## 11.4 Anuncios responsivos (3 por grupo)\n")
A("Cada grupo tiene tres anuncios con enfoques distintos: **A** " + THEME_NAMES["A"] + " · **B** " + THEME_NAMES["B"] + " · **C** " + THEME_NAMES["C"] + ". "
  "Los 5 primeros títulos de cada anuncio contienen la keyword del grupo; los 10 restantes refuerzan el enfoque.\n")
A("Lenguaje revisado contra políticas: sin \"garantizado\", \"ahorre impuestos\", \"evite auditorías\", sin signos de exclamación ni mayúsculas sostenidas.\n")
for c in CAMPAIGNS:
    A(f"### {c['name']}\n")
    A(f"Ruta visible: `gonzalezarmendariz.com/{c['path'][0]}/{c['path'][1]}`\n")
    for g in c["groups"]:
        A(f"#### Grupo: {g['name']} → `{final_url(c, g).replace(BASE, '')}`\n")
        for a in [x for x in ads if x["c"] is c and x["g"] is g]:
            pin = " (título 1 fijado en posición 1)" if a["t"] == "A" else ""
            A(f"**Anuncio {a['t']}: {THEME_NAMES[a['t']]}**{pin}\n")
            A("| # | Título | Car. |")
            A("|---|---|---|")
            for i, h in enumerate(a["heads"], 1):
                A(f"| {i} | {h} | {len(h)} |")
            A("")
            A("| # | Descripción | Car. |")
            A("|---|---|---|")
            for i, d in enumerate(a["descs"], 1):
                A(f"| {i} | {d} | {len(d)} |")
            A("")

A("## 11.5 Recursos (extensiones)\n")
sitelinks = [
    ("Contabilidad", "Impuestos al día cada mes", "Estados financieros claros", "/servicios/contabilidad-empresas-monterrey/"),
    ("Asesoría fiscal", "Decisiones con menos riesgo", "Planeación dentro de la ley", "/servicios/asesoria-fiscal-monterrey/"),
    ("Auditoría", "Opinión independiente", "Para socios y bancos", "/servicios/auditoria-monterrey/"),
    ("Nosotros", "Más de 28 años en Nuevo León", "400+ empresas respaldadas", "/nosotros/"),
    ("Agendar consulta", "Reunión con un socio", "Presencial o en línea", "/contacto/"),
    ("Preguntas frecuentes", "Costos, tiempos y proceso", "Respuestas claras", "/#faq-title"),
]
for s in sitelinks:
    check(s[0], 25, "sitelink"); check(s[1], 35, "sitelink d1"); check(s[2], 35, "sitelink d2")
callouts = ["Más de 28 años", "400+ empresas", "30 especialistas", "Oficina en San Pedro",
            "Reunión con un socio", "Propuesta por escrito", "Presencial o en línea", "Atención en inglés"]
for co in callouts:
    check(co, 25, "callout")
if errors:
    print("\n".join(errors))
    sys.exit(1)
A("**Enlaces de sitio** (texto ≤ 25 · líneas ≤ 35):\n")
A("| Texto | Línea 1 | Línea 2 | URL |")
A("|---|---|---|---|")
for s in sitelinks:
    A(f"| {s[0]} | {s[1]} | {s[2]} | `{s[3]}` |")
A("")
A("**Textos destacados** (≤ 25): " + " · ".join(callouts) + " ([SUPUESTO] \"Atención en inglés\": confirmar)\n")
A("**Fragmentos estructurados**: Encabezado *Servicios*: Contabilidad, Asesoría fiscal, Auditoría, Consultoría de negocios, Servicios administrativos.\n")
A("**Llamada:** 81 8363 4412, con informes de llamadas activados (número de desvío de Google) y conversión \"Llamada desde anuncio ≥ 60 s\". Programar solo en horario de atención.\n")
A("**Ubicación:** vincular la ficha de Google Business Profile.\n")
A("**Imágenes:** 3–5 fotos reales (fachada, sala de juntas, equipo) en 1:1 y 1.91:1. [PENDIENTE: fotografía]\n")
A("**Logotipo y nombre de empresa:** González Armendáriz + logo cuadrado.\n")
A("**Formulario de clientes potenciales (opcional, fase 2):** solo si el formulario de la landing convierte por debajo de lo esperado; exige aviso de privacidad enlazado.\n")

A("## 11.6 Rutina de optimización\n")
A("| Frecuencia | Tarea |")
A("|---|---|")
A("| Semanal (mes 1–2) | Términos de búsqueda → negativas · revisar conversiones duplicadas · presupuesto limitado |")
A("| Quincenal | Activos con rendimiento \"Bajo\" → reemplazar · revisar porcentaje de impresiones perdidas por ranking |")
A("| Mensual | Costo por cita real (CRM) por campaña · mover presupuesto a la campaña con menor costo por cita · probar una variante de landing |")
A("| Trimestral | Revisar concordancia amplia + Smart Bidding · evaluar campañas de Fase 2 · actualizar mensajes por temporada fiscal (marzo, abril, mayo, diciembre) |")

with open(os.path.join(ROOT, "docs", "11-google-ads.md"), "w", encoding="utf-8") as f:
    f.write("\n".join(L) + "\n")

print(f"OK: {len(ads)} anuncios, "
      f"{sum(len(g['keywords']) for c in CAMPAIGNS for g in c['groups'])} keywords, "
      f"{len(NEG_COMMON)} negativas generales")
