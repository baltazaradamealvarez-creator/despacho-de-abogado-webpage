from pathlib import Path
import json,html,urllib.parse,re
import markdown
from bs4 import BeautifulSoup
ROOT=Path(__file__).parent
SITE=ROOT/'site'
D=json.loads((ROOT/'entregables/contenido-web.json').read_text())
DOMAIN='https://gonzalezarmendariz.com'
E=lambda x:html.escape(str(x),quote=True)
SERVICE_IDS=['contabilidad','asesoria-fiscal','auditoria','consultoria-negocios','servicios-administrativos']
SLUGS={'es':['contabilidad','asesoria-fiscal','auditoria'],'en':['accounting','tax-advisory','audit']}
L={
'es':{'cta':'Agendar una consulta','locale':'es-MX','alt':'Alejandro González, Director Fundador de González Armendáriz','founder':'Director Fundador','services':'Servicios','about':'Nosotros','team':'Equipo','insights':'Perspectivas','contact':'Contacto','why':'Por qué elegirnos','service_heading':'Respaldo para las decisiones de su empresa','pillars_heading':'Experiencia que acompaña sus decisiones','leadership':'Liderazgo','faq':'Preguntas frecuentes','faq_heading':'Antes de conversar','firm':'Conocer la firma','request':'Solicite una consulta','name':'Nombre','company':'Empresa','phone':'Teléfono','interest':'Servicio de interés','select':'Seleccione un servicio','guidance':'Necesito orientación','years':'años de trayectoria','businesses':'empresas respaldadas','members':'colaboradores','office':'Oficina en San Pedro Garza García','map':'Ver ubicación','load_map':'Cargar mapa','map_note':'El mapa se carga desde Google solo al solicitarlo.','privacy':'Aviso de privacidad','cookies':'Política de cookies','careers':'Bolsa de trabajo','rights':'Todos los derechos reservados.','note':'Al continuar, se abrirá WhatsApp con su solicitud. Deberá enviar el mensaje para contactar a la firma. La cita queda sujeta a confirmación.','wa':'Contactar por WhatsApp','skip':'Ir al contenido','menu':'Menú','benefits':'Claridad para el siguiente paso','trust':'28+ años de trayectoria · 400+ empresas respaldadas','nosotros':'/nosotros/','equipo':'/equipo/','blog':'/perspectivas/','contacto':'/contacto/','servicios':'/servicios/','legal':'/aviso-de-privacidad/','cookie_url':'/politica-de-cookies/','trabajo':'/trabajo/'},
'en':{'cta':'Schedule a consultation','locale':'en-US','alt':'Alejandro González, Founding Director of González Armendáriz','founder':'Founding Director','services':'Services','about':'About','team':'Team','insights':'Insights','contact':'Contact','why':'Why choose us','service_heading':'Support for your business decisions','pillars_heading':'Experience behind your decisions','leadership':'Leadership','faq':'Frequently asked questions','faq_heading':'Before we speak','firm':'Meet the firm','request':'Request a consultation','name':'Name','company':'Company','phone':'Phone','interest':'Service of interest','select':'Select a service','guidance':'I need guidance','years':'years of experience','businesses':'businesses supported','members':'team members','office':'Office in San Pedro Garza García','map':'View location','load_map':'Load map','map_note':'The Google map loads only when you request it.','privacy':'Privacy notice','cookies':'Cookie policy','careers':'Careers','rights':'All rights reserved.','note':'Continuing opens WhatsApp with your request. Send the message to contact the firm. Appointments are subject to confirmation.','wa':'Contact via WhatsApp','skip':'Skip to content','menu':'Menu','benefits':'Clarity for your next step','trust':'28+ years of experience · 400+ businesses supported','nosotros':'/en/about/','equipo':'/en/team/','blog':'/en/insights/','contacto':'/en/contact/','servicios':'/en/services/','legal':'/en/privacy-notice/','cookie_url':'/en/cookie-policy/','trabajo':'/en/careers/'}}

def local(path):return path.lstrip('/')+'index.html' if path!='/' else 'index.html'
def relative(origin,target):
 import posixpath
 return posixpath.relpath(target.lstrip('/') or '.',start=origin.strip('/') or '.')+('/' if target.endswith('/') and target!='/' else '')
def button(text,href,light=False):return f'<a class="button {"light" if light else ""}" href="{E(href)}">{E(text)}<span class="arrow" aria-hidden="true">↗</span></a>'
def brand(path,lang,landing=False):
 # No link to another page on the ad landing: the brand remains a visual signpost.
 content=f'<img class="brand-logo" src="{relative(path,"/assets/logo.png")}" width="613" height="199" alt="González Armendáriz · {'Consultoría contable y fiscal' if lang=='es' else 'Accounting and tax advisory'}">'
 return '<div class="brand">'+content+'</div>' if landing else f'<a class="brand" href="{relative(path,"/en/" if lang=="en" else "/")}">{content}</a>'
def header(path,lang,alternate,landing=False):
 t=L[lang]
 language=f'<a class="language" href="{relative(path,alternate)}" lang="{"en" if lang=="es" else "es"}" aria-label="{"EN: View in English" if lang=="es" else "ES: Ver en español"}">{"EN" if lang=="es" else "ES"} <span aria-hidden="true">↗</span></a>'
 if landing: nav='<div class="header-nav">'+language+'</div>'
 else:
  links="".join(f'<a href="{t[key]}" {chr(32)+"aria-current=page" if path==t[key] else ""}>{t[label]}</a>' for key,label in [("servicios","services"),("nosotros","about"),("equipo","team"),("blog","insights"),("contacto","contact")])
  nav=f'<nav class="header-nav" aria-label="{"Navegación principal" if lang=="es" else "Main navigation"}">{links}<details class="mobile-menu"><summary>{t["menu"]}</summary><div class="mobile-links">{links}</div></details>{language}</nav>'
 return '<div class="wrap"><header class="site-header">'+brand(path,lang,landing)+nav+'</header></div>'
def trust(lang):return f'<p class="trust">{L[lang]["trust"]}</p>'
def form(path,lang,selected=None,landing=False):
 t=L[lang]
 services=D['home'][lang]['services']
 opts=[f'<option value="" {"selected" if selected is None else ""} disabled>{t["select"]}</option>']
 for key,s in zip(SERVICE_IDS,services):opts.append(f'<option value="{E(s["name"])}" {"selected" if key==selected else ""}>{E(s["name"])}</option>')
 opts.append(f'<option value="{t["guidance"]}">{t["guidance"]}</option>')
 fields=''
 for name,label,typ,auto in [('name',t['name'],'text','name'),('company',t['company'],'text','organization'),('phone',t['phone'],'tel','tel')]:
  fields+=f'<div class="field"><label for="{name}">{label}</label><input id="{name}" name="{name}" type="{typ}" autocomplete="{auto}" required maxlength="100" {"inputmode=tel" if typ=="tel" else ""}></div>'
 fields+=f'<div class="field"><label for="service">{t["interest"]}</label><select id="service" name="service" required>{"".join(opts)}</select></div>'
 return f'''<form class="consultation-form" id="consultation-form" data-consultation action="#consulta" method="post">
 <{'h2' if landing else 'h3'} class="form-title">{t['request']}</{'h2' if landing else 'h3'}><div class="fields">{fields}</div>
 <button class="button" type="submit" disabled>{t['cta']}<span class="arrow" aria-hidden="true">↗</span></button>
 <p class="form-note">{t['note']} <a href="{t['legal']}">{t['privacy']}</a>.</p>
 <p class="form-status" role="status" aria-live="polite"></p>
 <noscript><p class="form-note">{'Para solicitar una consulta sin JavaScript, contacte a la firma por' if lang=='es' else 'To request a consultation without JavaScript, contact the firm via'} <a href="https://wa.me/528128845949">WhatsApp</a> {'o teléfono.' if lang=='es' else 'or phone.'}</p></noscript>
 </form>'''
def faq(items):return '<div class="faqs">'+''.join(f'<details><summary>{E(x["q"])}</summary><p>{E(x["a"])}</p></details>' for x in items)+'</div>'
def phones():return '<div class="phones">'+''.join(f'<a href="tel:{num}">{display}</a>' for num,display in [('+528183634412','+52 818 363 4412'),('+528183630502','+52 818 363 0502'),('+528183634260','+52 818 363 4260')])+'</div>'
def office(lang):
 t=L[lang];address='Av. Lázaro Cárdenas #2400 Pte., Edificio Losoles Int. PB 18, Col. Residencial San Agustín, San Pedro Garza García, N.L., C.P. 66260.'
 mapurl='https://www.google.com/maps/search/?api=1&query='+urllib.parse.quote(address)
 return f'''<div class="office"><div><h3>{t['office']}</h3><address>{E(address)}</address>{phones()}<p class="phones"><a href="https://wa.me/528128845949">WhatsApp · +52 812 884 5949</a></p></div><div><div class="map"><span class="eyebrow">San Pedro Garza García</span><p>Av. Lázaro Cárdenas #2400 Pte.<br>Edificio Losoles · PB 18</p><button class="button outline" type="button" data-map>{t['load_map']}<span aria-hidden="true">↗</span></button></div><a class="map-link" href="{mapurl}" target="_blank" rel="noopener noreferrer">{t['map']} ↗</a><p class="map-disclosure">{t['map_note']}</p></div></div>'''
def footer(path,lang,landing=False):
 t=L[lang]
 if landing:
  links=f'<a href="{t["legal"]}">{t["privacy"]}</a><a href="{t["cookie_url"]}">{t["cookies"]}</a>'
  contact=f'<div class="footer-contact"><a href="tel:+528183634412">+52 818 363 4412</a><span>San Pedro Garza García · Nuevo León</span></div>'
 else:
  links=''.join(f'<a href="{t[key]}">{t[label]}</a>' for key,label in [('servicios','services'),('nosotros','about'),('equipo','team'),('blog','insights'),('contacto','contact'),('trabajo','careers'),('legal','privacy'),('cookie_url','cookies')]);contact=''
 return f'<div class="wrap"><footer class="site-footer"><div>{contact}<p>© 2026 González Armendáriz. {t["rights"]}</p></div><div class="footer-links">{links}</div><a class="wa-float" href="https://wa.me/528128845949" aria-label="{t["wa"]}">WhatsApp <span aria-hidden="true">↗</span></a></footer></div>'
def graph(path,lang,data,landing=False,serviceid=None):
 org={'@type':'Organization','@id':DOMAIN+'/#organization','name':'González Armendáriz','url':DOMAIN+'/','logo':DOMAIN+'/assets/logo.png','founder':{'@id':DOMAIN+'/#alejandro-gonzalez'}}
 office={'@type':'AccountingService','@id':DOMAIN+'/#office','name':'González Armendáriz','url':DOMAIN+'/','parentOrganization':{'@id':org['@id']},'telephone':'+528183634412','address':{'@type':'PostalAddress','streetAddress':'Av. Lázaro Cárdenas #2400 Pte., Edificio Losoles Int. PB 18, Col. Residencial San Agustín','addressLocality':'San Pedro Garza García','addressRegion':'Nuevo León','postalCode':'66260','addressCountry':'MX'},'areaServed':[{'@type':'City','name':'Monterrey'},{'@type':'City','name':'San Pedro Garza García'}],'contactPoint':[{'@type':'ContactPoint','telephone':n,'contactType':'customer service'} for n in ['+528183634412','+528183630502','+528183634260']]}
 person={'@type':'Person','@id':DOMAIN+'/#alejandro-gonzalez','name':'Alejandro González','jobTitle':L[lang]['founder'],'worksFor':{'@id':org['@id']}}
 web={'@type':data.get('schema_type','WebPage'),'@id':DOMAIN+path+'#webpage','url':DOMAIN+path,'name':data['title'],'description':data['description'],'inLanguage':L[lang]['locale'],'about':{'@id':org['@id']},'isPartOf':{'@id':DOMAIN+'/#website'}}
 website={'@type':'WebSite','@id':DOMAIN+'/#website','url':DOMAIN+'/','name':'González Armendáriz','publisher':{'@id':org['@id']},'inLanguage':['es-MX','en-US']}
 faqpage={'@type':'FAQPage','@id':DOMAIN+path+'#faq','url':DOMAIN+path,'inLanguage':L[lang]['locale'],'isPartOf':{'@id':web['@id']},'mainEntity':[{'@type':'Question','name':x['q'],'acceptedAnswer':{'@type':'Answer','text':x['a']}} for x in data.get('faqs',[])]}
 nodes=[org,office,person,website,web]
 if data.get("faqs"):nodes.append(faqpage)
 if data.get('schema_type')=='Article':
  article={'@type':'Article','@id':DOMAIN+path+'#article','headline':data['h1'],'inLanguage':L[lang]['locale'],'mainEntityOfPage':{'@id':web['@id']},'publisher':{'@id':org['@id']}}
  web['@type']='WebPage';web['mainEntity']={'@id':article['@id']};nodes.append(article)
 if path not in ["/","/en/"]:
  nodes.append({"@type":"BreadcrumbList","@id":DOMAIN+path+"#breadcrumbs","itemListElement":[{"@type":"ListItem","position":1,"name":"Inicio" if lang=="es" else "Home","item":DOMAIN+("/" if lang=="es" else "/en/")},{"@type":"ListItem","position":2,"name":data.get("h1",data["title"]),"item":DOMAIN+path}]})
 if serviceid:
  idx=SERVICE_IDS.index(serviceid)
  service={'@type':'Service','@id':DOMAIN+D['home'][lang]['services'][idx]['url']+'#service','name':D['home'][lang]['services'][idx]['name'],'serviceType':D['home'][lang]['services'][idx]['name'],'provider':{'@id':office['@id']},'areaServed':[{'@type':'City','name':'Monterrey'},{'@type':'City','name':'San Pedro Garza García'}],'url':DOMAIN+D['home'][lang]['services'][idx]['url']}
  nodes.append(service);web['about']={'@id':service['@id']}
 return {'@context':'https://schema.org','@graph':nodes}
def head(path,lang,alt,data,landing=False,serviceid=None):
 espath=path if lang=='es' else alt;enpath=path if lang=='en' else alt
 logoico='data:image/svg+xml,'+urllib.parse.quote('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" fill="#102A35"/><text x="32" y="44" text-anchor="middle" font-family="Georgia" font-size="37" fill="#F5F2EB">G</text></svg>')
 schema=json.dumps(graph(path,lang,data,landing,serviceid),ensure_ascii=False).replace('</','<\\/')
 return f'''<!doctype html><html lang="{L[lang]['locale']}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{E(data['title'])}</title><meta name="description" content="{E(data['description'])}"><meta name="robots" content="{'noindex,follow' if landing or data.get('noindex') else 'index,follow'}"><link rel="canonical" href="{DOMAIN+path}"><link rel="alternate" hreflang="es-MX" href="{DOMAIN+espath}"><link rel="alternate" hreflang="en-US" href="{DOMAIN+enpath}"><link rel="alternate" hreflang="x-default" href="{DOMAIN+espath}"><meta property="og:type" content="website"><meta property="og:site_name" content="González Armendáriz"><meta property="og:title" content="{E(data['title'])}"><meta property="og:description" content="{E(data['description'])}"><meta property="og:url" content="{DOMAIN+path}"><meta property="og:locale" content="{'es_MX' if lang=='es' else 'en_US'}"><meta property="og:image" content="{DOMAIN}/assets/social-{lang}.png"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="González Armendáriz · {'Contabilidad, auditoría y asesoría fiscal' if lang=='es' else 'Accounting, audit and tax advisory'}"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{E(data['title'])}"><meta name="twitter:description" content="{E(data['description'])}"><meta name="twitter:image" content="{DOMAIN}/assets/social-{lang}.png"><meta name="twitter:image:alt" content="González Armendáriz · {'Contabilidad, auditoría y asesoría fiscal' if lang=='es' else 'Accounting, audit and tax advisory'}"><meta property="og:locale:alternate" content="{'en_US' if lang=='es' else 'es_MX'}"><link rel="icon" type="image/png" href="{relative(path,'/assets/favicon.png')}"><link rel="preload" href="{relative(path,'/assets/cormorant-latin.woff2')}" as="font" type="font/woff2" crossorigin><link rel="stylesheet" href="{relative(path,'/assets/site.css')}"><script type="application/ld+json">{schema}</script><script src="{relative(path,'/assets/consent.js')}" defer></script><script src="{relative(path,'/assets/site.js')}" defer></script></head>'''
def save(path,text):
 file=SITE/local(path);file.parent.mkdir(parents=True,exist_ok=True);file.write_text(text.replace('#consultation','#consulta').replace('↗','<svg class="arrow-svg" viewBox="0 0 24 24" width="20" height="20" aria-hidden="true"><path d="M5 19 19 5M5 5h14v14" fill="none" stroke="currentColor" stroke-width="1.5"/></svg>'),encoding='utf-8')
def home(lang):
 t=L[lang];d=D['home'][lang];path='/' if lang=='es' else '/en/';alt='/en/' if lang=='es' else '/'
 out=head(path,lang,alt,d)+f'<body data-page="home"><a class="skip" href="#main">{t["skip"]}</a>'+header(path,lang,alt)+'<main id="main">'
 out+=f'<section class="hero wrap" aria-labelledby="hero-title"><div class="hero-top"><p class="eyebrow">San Pedro Garza García · Nuevo León</p><p class="eyebrow">González Armendáriz</p></div><div class="hero-rule" aria-hidden="true"></div><h1 id="hero-title">{d["h1"]}</h1><div class="hero-bottom"><p>{d["subtitle"]}</p>{button(t["cta"],"#consulta")}</div></section>'
 out+='<section class="wrap" aria-label="'+('La firma en cifras' if lang=='es' else 'The firm in figures')+'"><div class="stats">'+''.join(f'<div class="stat"><strong>{v}</strong><span>{t[k]}</span></div>' for v,k in [('28+','years'),('400+','businesses'),('30','members')])+'</div></section>'
 cards=''.join(f'<article class="service"><span class="number" aria-hidden="true">0{i+1}</span><h3><a href="{s["url"]}">{E(s["name"])}</a></h3><p>{E(s["line"])}</p></article>' for i,s in enumerate(d['services']))
 out+=f'<section id="servicios" class="section wrap" aria-labelledby="services-title"><div class="section-head"><p class="eyebrow">01 / {t["services"]}</p><h2 id="services-title">{t["service_heading"]}</h2></div><div class="services">{cards}</div></section>'
 pillars=''.join(f'<div class="pillar"><h3>{E(p["title"])}</h3><p>{E(p["text"])}</p></div>' for p in d['pillars'])
 out+=f'<section class="section dark" aria-labelledby="why-title"><div class="wrap"><div class="section-head"><p class="eyebrow">02 / {t["why"]}</p><h2 id="why-title">{t["pillars_heading"]}</h2></div><div class="pillars">{pillars}</div></div></section>'
 out+=f'<section id="firma" class="section wrap leadership" aria-labelledby="leadership-title"><img class="founder-image" src="{relative(path,"/assets/fundador.webp")}" width="465" height="500" loading="lazy" decoding="async" alt="{t["alt"]}"><div class="founder-text"><p class="eyebrow">03 / {t["leadership"]}</p><h2 id="leadership-title">{d["leadership"]["headline"]}</h2><p>{d["leadership"]["text"]}</p><div class="signature"><div>Alejandro González<span>{t["founder"]}</span></div><a href="{t["nosotros"]}">{t["firm"]} ↗</a></div></div></section>'
 out+=f'<section id="preguntas" class="section faq-section" aria-labelledby="faq-title"><div class="wrap faq-layout"><div class="faq-intro"><p class="eyebrow">04 / {t["faq"]}</p><h2 id="faq-title">{t["faq_heading"]}</h2></div>{faq(d["faqs"])}</div></section>'
 out+=f'<section id="consulta" class="section wrap" aria-labelledby="contact-title"><div class="contact-layout"><div class="contact-intro"><p class="eyebrow">05 / {t["contact"]}</p><h2 id="contact-title">{d["final_title"]}</h2><p>{d["final_text"]}</p>{trust(lang)}</div>{form(path,lang)}</div>{office(lang)}</section>'
 out+='</main>'+footer(path,lang)+'</body></html>';save(path,out)
def landing(service,lang):
 t=L[lang];d=D['landings'][service][lang];other='en' if lang=='es' else 'es';path=d['url'];alt=D['landings'][service][other]['url']
 out=head(path,lang,alt,d,True,service)+f'<body class="landing" data-page="landing_{service}"><a class="skip" href="#main">{t["skip"]}</a>'+header(path,lang,alt,True)+'<main id="main">'
 out+=f'<section class="wrap landing-hero" aria-labelledby="hero-title"><div><p class="eyebrow">San Pedro Garza García · Monterrey</p><h1 id="hero-title">{E(d["h1"])}</h1><p class="lead">{E(d["subtitle"])}</p>{trust(lang)}</div><div id="consulta">{form(path,lang,service,True)}</div></section>'
 out+=f'<section class="dark landing-benefits" aria-label="{t["benefits"]}"><div class="wrap"><ul>'+''.join(f'<li>{E(x)}</li>' for x in d['benefits'])+'</ul></div></section>'
 out+=f'<section class="section wrap faq-layout" aria-labelledby="faq-title"><div class="faq-intro"><p class="eyebrow">{t["faq"]}</p><h2 id="faq-title">{t["faq_heading"]}</h2></div>{faq(d["faqs"])}</section>'
 out+=f'<section class="landing-cta dark" aria-labelledby="final-title"><div class="wrap"><h2 id="final-title">{E(d["final_title"])}</h2>{button(t["cta"],"#consulta",True)}<p class="trust" style="color:#D0D7D6">{t["trust"]}</p></div></section>'
 out+='</main>'+footer(path,lang,True)+'</body></html>';save(path,out)

# All first-party navigation stays on the current host (including Render previews).
PAGES={}
copy=(ROOT/'entregables/04-paginas.md').read_text()
for match in re.finditer(r'^## ([^\n]+?) · (ES|EN)\n(.*?)(?=^## [^\n]+? · (?:ES|EN)\n|\Z)',copy,re.M|re.S):
 label,language,block=match.groups();lang=language.lower()
 path=re.search(r'\*\*URL:\*\* (\S+)',block)[1]
 h1=re.search(r'^# (.+)',block,re.M)[1]
 body=block[re.search(r'^# .+\n',block,re.M).end():]
 body=re.sub(r'^\[(?:PENDIENTE|PENDING|SUPUESTO).*?\]\s*$', '',body,flags=re.M)
 body=re.sub(r'\n---\s*$', '',body)
 PAGES[path]={'title':re.search(r'\*\*Meta title:\*\* (.+)',block)[1],'description':re.search(r'\*\*Meta description:\*\* (.+)',block)[1],'h1':h1,'body':body.strip(),'lang':lang,'label':label,'faqs':[]}
FAQS=json.loads((ROOT/'entregables/faq-por-url.json').read_text())
ROUTES=[]
def register(path,lang,alt,kind):
 ROUTES.append({'path':path,'language':lang,'alternate':alt,'type':kind})
def md(text):
 text=re.sub(r'^\*\*[^\n]+\*\* → \S+\s*$', '',text,flags=re.M)
 return markdown.markdown(text,extensions=['sane_lists'])
def sections(body):
 return [(x.group(1),x.group(2).strip()) for x in re.finditer(r'^## ([^\n]+)\n(.*?)(?=^## |\Z)',body,re.M|re.S)]
def page_start(path,lang,alt,d,kind,service=None):
 register(path,lang,alt,kind)
 data_types={'services':'CollectionPage','insights':'CollectionPage','about':'AboutPage','contact':'ContactPage','article':'Article'}
 d['schema_type']=data_types.get(kind,'WebPage')
 return head(path,lang,alt,d,False,service)+f'<body data-page="{kind}"><a class="skip" href="#main">{L[lang]["skip"]}</a>'+header(path,lang,alt)+'<main id="main">'
def page_end(path,lang):return '</main>'+footer(path,lang)+'</body></html>'
def intro(d,lang,label,subtitle='',service=None):
 t=L[lang]
 return f'''<section class="page-hero wrap"><div class="breadcrumbs"><a href="{'/' if lang=='es' else '/en/'}">{'Inicio' if lang=='es' else 'Home'}</a><span aria-hidden="true">/</span>{f'<a href="{t["servicios"]}">{t["services"]}</a><span aria-hidden="true">/</span>' if service else ''}<span>{E(label)}</span></div><p class="eyebrow">{E(label)} · San Pedro Garza García</p><h1>{E(d['h1'])}</h1>{f'<p class="page-lead">{E(subtitle)}</p>' if subtitle else ''}</section>'''
def consultation(path,lang,selected=None):
 t=L[lang]
 title='Conversemos sobre su empresa' if lang=='es' else 'Let’s discuss your business'
 desc='Comparta lo que necesita resolver. Definamos el siguiente paso.' if lang=='es' else 'Tell us what you need to address. Let’s define the next step.'
 return f'<section class="section wrap" id="consulta"><div class="contact-layout"><div class="contact-intro"><p class="eyebrow">{t["contact"]}</p><h2>{title}</h2><p>{desc}</p>{trust(lang)}<a class="text-link" href="https://wa.me/528128845949">{t["wa"]} ↗</a></div>{form(path,lang,selected)}</div></section>'
def service_cards(lang):
 return '<div class="overview-grid">'+''.join(f'<a class="overview-card" href="{s["url"]}"><span class="number">0{i+1}</span><h2>{E(s["name"])}</h2><p>{E(s["line"])}</p><span class="text-link">{"Conocer el servicio" if lang=="es" else "Explore the service"} ↗</span></a>' for i,s in enumerate(D['home'][lang]['services']))+'</div>'
def service_page(index,lang):
 s=D['home'][lang]['services'][index];path=s['url'];alt=D['home']['en' if lang=='es' else 'es']['services'][index]['url'];d=PAGES[path];t=L[lang];d['faqs']=FAQS[path]
 blocks=sections(d['body']);who,problems,includes,steps=blocks[:4]
 out=page_start(path,lang,alt,d,'service',SERVICE_IDS[index])+intro(d,lang,s['name'],s['line'],True)
 out+=f'<section class="wrap service-opening"><div class="service-audience prose"><p class="eyebrow">01 / {E(who[0])}</p>{md(who[1])}{button(t["cta"],"#consulta")}{trust(lang)}</div><aside class="decision-card"><p class="eyebrow">{t["benefits"]}</p><h2>{E(problems[0])}</h2>{md(problems[1])}<span class="decision-foot">González Armendáriz · Monterrey</span></aside></section>'
 out+=f'<section class="section service-scope"><div class="wrap editorial-grid"><div><p class="eyebrow">02 / {t["services"]}</p><h2>{E(includes[0])}</h2></div><div class="prose scope-list">{md(includes[1])}</div></div></section>'
 out+=f'<section class="section wrap"><div class="section-head"><p class="eyebrow">03 / {"Nuestro enfoque" if lang=="es" else "Our approach"}</p><h2>{E(steps[0])}</h2></div><div class="steps prose">{md(steps[1])}</div></section>'
 out+=f'<section class="section faq-section"><div class="wrap faq-layout"><div class="faq-intro"><p class="eyebrow">04 / {t["faq"]}</p><h2>{t["faq_heading"]}</h2></div>{faq(d["faqs"])}</div></section>'
 out+=f'<section class="section wrap related"><div class="section-head"><p class="eyebrow">{t["services"]}</p><h2>{"Una visión integral de su empresa" if lang=="es" else "A broader view of your business"}</h2></div><div class="related-links">'+''.join(f'<a href="{x["url"]}">{E(x["name"])} ↗</a>' for j,x in enumerate(D['home'][lang]['services']) if j!=index)+'</div></section>'
 out+=consultation(path,lang,SERVICE_IDS[index])+page_end(path,lang);save(path,out)
def overview(lang):
 t=L[lang];path=t['servicios'];alt=L['en' if lang=='es' else 'es']['servicios'];d=PAGES[path]
 subtitle='Cinco servicios. Un punto de partida: lo que su empresa necesita.' if lang=='es' else 'Five services. One starting point: what your business needs.'
 out=page_start(path,lang,alt,d,'services')+intro(d,lang,t['services'],subtitle)
 out+='<section class="wrap overview-section">'+service_cards(lang)+'</section>'
 out+=f'<section class="section dark"><div class="wrap editorial-grid"><p class="eyebrow">{t["why"]}</p><div><h2>{t["pillars_heading"]}</h2><p class="page-lead">{"28+ años de trayectoria, 400+ empresas respaldadas y 30 colaboradores." if lang=="es" else "28+ years of experience, 400+ businesses supported and 30 team members."}</p></div></div></section>'
 out+=consultation(path,lang)+page_end(path,lang);save(path,out)
def firm_page(lang,team=False):
 t=L[lang];key='equipo' if team else 'nosotros';path=t[key];alt=L['en' if lang=='es' else 'es'][key];d=PAGES[path];es=lang=='es'
 subtitle=('30 colaboradores. Una firma enfocada en las necesidades de su empresa.' if es else '30 team members. A firm focused on your business needs.') if team else ('Experiencia contable, fiscal y empresarial desde San Pedro Garza García.' if es else 'Accounting, tax and business experience from San Pedro Garza García.')
 out=page_start(path,lang,alt,d,'team' if team else 'about')+intro(d,lang,t['team'] if team else t['about'],subtitle)
 out+=f'<section class="section wrap leadership firm-profile"><div class="portrait-frame"><img class="founder-image" src="/assets/fundador.webp" width="465" height="500" alt="{t["alt"]}" decoding="async"><p class="portrait-caption">Alejandro González · {t["founder"]}</p></div><div class="founder-text"><p class="eyebrow">{t["leadership"]}</p><h2>{"Las decisiones comienzan con una conversación" if es else "Decisions begin with a conversation"}</h2><p>{"González Armendáriz es una firma de contabilidad, auditoría y asesoría fiscal corporativa. Nuestra oferta también incluye consultoría de negocios y servicios administrativos." if es else "González Armendáriz is an accounting, audit and corporate tax advisory firm. Our offering also includes business consulting and administrative services."}</p><div class="signature"><div>Alejandro González<span>{t["founder"]}</span></div><a href="{t["nosotros"] if team else t["equipo"]}">{t["firm"] if team else t["team"]} ↗</a></div></div></section>'
 out+='<section class="dark section"><div class="wrap"><div class="firm-stats">'+''.join(f'<div><strong>{v}</strong><p>{t[k]}</p></div>' for v,k in [('28+','years'),('400+','businesses'),('30','members')])+'</div></div></section>'
 if team:
  out+=f'<section class="section wrap editorial-grid"><div><p class="eyebrow">{t["team"]}</p><h2>{"Experiencia para su operación" if es else "Experience for your operations"}</h2></div><div class="prose"><p>{"30 colaboradores forman parte de González Armendáriz. La oferta de la firma reúne cinco áreas de servicio para atender necesidades contables, fiscales y empresariales." if es else "González Armendáriz has 30 team members. The firm’s offering brings together five service areas to address accounting, tax and business needs."}</p><div class="expertise-list">'+''.join(f'<a href="{s["url"]}">{E(s["name"])} ↗</a>' for s in D['home'][lang]['services'])+'</div></div></section>'
 else:
  first=sections(d['body'])[0]
  out+=f'<section class="section wrap editorial-grid"><div><p class="eyebrow">{t["about"]}</p><h2>{E(first[0])}</h2></div><div class="prose">{md(first[1])}<p>{"La trayectoria de la firma se ha desarrollado alrededor de las necesidades contables, fiscales y empresariales de sus clientes." if es else "The firm’s track record has developed around the accounting, tax and business needs of its clients."}</p></div></section>'
  out+=f'<section class="section faq-section"><div class="wrap"><div class="section-head"><p class="eyebrow">{t["why"]}</p><h2>{t["pillars_heading"]}</h2></div><div class="pillars">'+''.join(f'<div class="pillar"><h3>{E(p["title"])}</h3><p>{E(p["text"])}</p></div>' for p in D['home'][lang]['pillars'])+'</div></div></section>'
 out+=consultation(path,lang)+page_end(path,lang);save(path,out)
def contact_page(lang):
 t=L[lang];path=t['contacto'];alt=L['en' if lang=='es' else 'es']['contacto'];d=PAGES[path];es=lang=='es'
 out=page_start(path,lang,alt,d,'contact')+intro(d,lang,t['contact'],'Comparta sus datos y el servicio de interés para iniciar la conversación.' if es else 'Share your details and the service of interest to start a conversation.')
 out+=f'<section class="wrap contact-page-body" id="consulta"><div class="contact-layout"><div class="contact-intro"><p class="eyebrow">{t["office"]}</p><h2>{"Atención directa a su empresa" if es else "Direct attention to your business"}</h2><p>{"Solicite una consulta por WhatsApp o por teléfono. Los honorarios, el alcance y la fecha se confirman con la firma." if es else "Request a consultation via WhatsApp or phone. Fees, scope and the appointment date are confirmed with the firm."}</p>{trust(lang)}{phones()}<p class="contact-wa"><a class="text-link" href="https://wa.me/528128845949">WhatsApp · +52 812 884 5949 ↗</a></p></div>{form(path,lang)}</div>{office(lang)}</section>'+page_end(path,lang);save(path,out)
GUIDES=json.loads((ROOT/'entregables/guias-web.json').read_text())
ARCHIVE=json.loads((ROOT/'fuentes/wp-json_wp_v2_posts_per_page=100.txt').read_text())
EN_OLD={'there-will-be-no-tax-reform-in-mexico-sat-will-go-after-large-taxpayers','buenrostro-foresees-tax-reform-by-september','how-did-outsourcing-2021-end-up-in-mexico'}
# Pair the original translations by topic, never by unordered set position.
OLD_PAIRS={'se-modifica-la-ley-de-amparos-fiscales':'there-will-be-no-tax-reform-in-mexico-sat-will-go-after-large-taxpayers','el-sistema-fiscal-ayuda-a-tu-empresa':'buenrostro-foresees-tax-reform-by-september','el-nuevo-mundo-de-las-finanzas-contables':'how-did-outsourcing-2021-end-up-in-mexico'}
ARCHIVE_ES=[x for x in ARCHIVE if x['slug'] not in EN_OLD]
EN_TITLES=['Invoice cancellation in 2025','Individual annual tax returns','Corporate annual tax returns','Annual income tax returns','Understanding the RESICO tax regime','Economic perspectives for 2025','The importance of an annual budget','Preparing the accounting and tax close','Tax implications of liquidating a company in Mexico','Personal tax deductions','Artificial intelligence in accounting','Employee profit sharing']
def archive_url(p,lang):
 slug=p['slug'] if lang=='es' else OLD_PAIRS.get(p['slug'],p['slug'])
 return ('/perspectivas/archivo/' if lang=='es' else '/en/insights/archive/')+slug+'/'
def article_card(g,lang,i):
 d=g[lang];url=L[lang]['blog']+d['slug']+'/'
 return f'<a class="insight-card" href="{url}"><div class="article-art art-{i%3}" aria-hidden="true"><span>GA</span><i>{i+1:02d}</i></div><div class="insight-copy"><p class="eyebrow">{E(d["category"])}</p><h2>{E(d["h1"])}</h2><p>{E(d["answer"])}</p><span class="text-link">{"Leer perspectiva" if lang=="es" else "Read insight"} ↗</span></div></a>'
def insights_page(lang):
 t=L[lang];path=t['blog'];alt=L['en' if lang=='es' else 'es']['blog'];d=PAGES[path];es=lang=='es'
 out=page_start(path,lang,alt,d,'insights')+intro(d,lang,t['insights'],'Ideas breves sobre contabilidad, impuestos y decisiones empresariales.' if es else 'Concise ideas on accounting, tax and business decisions.')
 out+='<section class="wrap insights-grid">'+''.join(article_card(g,lang,i) for i,g in enumerate(GUIDES))+'</section>'
 out+=f'<section class="section wrap"><details class="archive-index"><summary>{"Archivo de publicaciones" if es else "Publication archive"}<span>{len(ARCHIVE_ES):02d}</span></summary><p class="archive-note">{"Publicaciones recuperadas del sitio anterior. Su contenido refleja la fecha original y puede requerir actualización; confirme las reglas vigentes antes de utilizarlo." if es else "Publications recovered from the previous website. They reflect their original dates and may require updating; confirm current rules before using them."}</p><div class="archive-links">'+''.join(f'<a href="{archive_url(p,lang)}"><span>{E(BeautifulSoup(p["title"]["rendered"],"html.parser").get_text()) if es else E(EN_TITLES[i] if i<12 else BeautifulSoup(next(x for x in ARCHIVE if x["slug"]==OLD_PAIRS[p["slug"]])["title"]["rendered"],"html.parser").get_text())}</span><time datetime="{p["date"][:10]}">{p["date"][:10]}</time> ↗</a>' for i,p in enumerate(ARCHIVE_ES))+'</div></details></section>'
 out+=consultation(path,lang)+page_end(path,lang);save(path,out)
def guide_page(g,lang):
 t=L[lang];x=g[lang];other='en' if lang=='es' else 'es';path=t['blog']+x['slug']+'/';alt=L[other]['blog']+g[other]['slug']+'/';es=lang=='es'
 faqs=[{'q':'¿Cómo se define el alcance de una consulta?' if es else 'How is the scope of a consultation defined?','a':'Depende de su operación, la información disponible y la decisión que necesita atender. Los entregables y honorarios se acuerdan con la firma.' if es else 'It depends on your operations, available information and the decision you need to address. Deliverables and fees are agreed with the firm.'},{'q':'¿Esta guía sustituye una revisión de mi empresa?' if es else 'Does this guide replace a review of my business?','a':'No. Es información general. Una recomendación para su empresa requiere revisar su situación y las reglas aplicables.' if es else 'No. This is general information. A recommendation for your business requires reviewing your circumstances and the applicable rules.'}]
 d={'title':x['h1'] if len(x['h1'])<=60 else ('Perspectivas | González Armendáriz' if es else 'Insights | González Armendáriz'),'description':'Información útil para su empresa. Revise puntos clave y solicite una consulta con González Armendáriz.' if es else 'Useful information for your business. Review key considerations and request a consultation with González Armendáriz.','h1':x['h1'],'faqs':faqs}
 out=page_start(path,lang,alt,d,'article')+intro(d,lang,x['category'])
 out+=f'<section class="wrap article-layout"><aside class="article-aside"><p class="eyebrow">{"En esta perspectiva" if es else "In this insight"}</p><nav aria-label="{"Contenido del artículo" if es else "Article contents"}">'+''.join(f'<a href="#parte-{i}">{E(h)}</a>' for i,(h,p) in enumerate(x['sections']))+f'</nav><a class="text-link" href="{t["blog"]}">← {t["insights"]}</a></aside><article class="article-body prose"><div class="direct-answer"><p class="eyebrow">{"Respuesta directa" if es else "Direct answer"}</p><p>{E(x["answer"])}</p></div>'+''.join(f'<section id="parte-{i}"><h2>{E(h)}</h2><p>{E(p)}</p></section>' for i,(h,p) in enumerate(x['sections']))+f'<section><h2>{t["faq"]}</h2>{faq(faqs)}</section><p class="article-disclaimer">{"Información general. El alcance del servicio y las reglas aplicables deben revisarse para su empresa." if es else "General information. Service scope and applicable rules should be reviewed for your business."}</p><a class="text-link" href="{D["home"][lang]["services"][g["service"]]["url"]}">{E(D["home"][lang]["services"][g["service"]]["name"])} ↗</a></article></section>'
 out+=consultation(path,lang,SERVICE_IDS[g['service']])+page_end(path,lang);save(path,out)
def clean_original(raw):
 soup=BeautifulSoup(raw,'html.parser')
 for tag in soup(['script','style','iframe','img','figure','form','input','button','h1']):tag.decompose()
 for tag in soup.find_all(['h3','h4']):tag.name='h2'
 for tag in soup.find_all(True):
  attrs={}
  if tag.name=='a':
   href=tag.get('href','')
   if href.startswith('https://') and 'gonzalezarmendariz.com' not in href:attrs={'href':href,'rel':'noopener noreferrer','target':'_blank'}
  tag.attrs=attrs
  if tag.name not in ['p','h2','h3','h4','strong','b','em','i','ul','ol','li','a','br','blockquote','table','thead','tbody','tr','th','td']:tag.unwrap()
 return str(soup)
def archive_page(p,index,lang):
 es=lang=='es';path=archive_url(p,lang);alt=archive_url(p,'en' if es else 'es');t=L[lang]
 original=p if es else next((x for x in ARCHIVE if x['slug']==OLD_PAIRS.get(p['slug'])),None)
 title=BeautifulSoup(original['title']['rendered'],'html.parser').get_text().strip() if original else EN_TITLES[index]
 d={'title':'Archivo | González Armendáriz' if es else 'Archive | González Armendáriz','description':'Publicación del archivo de González Armendáriz. Revise su fecha original y consulte su situación con la firma.' if es else 'Publication from the González Armendáriz archive. Check its original date and discuss your situation with the firm.','h1':title,'faqs':[]}
 d['noindex']=True
 out=page_start(path,lang,alt,d,'archive')+intro(d,lang,'Archivo' if es else 'Archive')
 note='Esta publicación refleja información de su fecha original. Puede contener reglas, cifras o plazos desactualizados. No la utilice como asesoría para una operación actual sin verificar su situación.' if es else 'This publication reflects information at its original date. Rules, figures or deadlines may be outdated. Do not use it as advice for a current transaction without reviewing your circumstances.'
 content=clean_original(original['content']['rendered']) if original else f'<p>This archive entry covers the topic “{E(title)}” in a publication originally released in Spanish on {p["date"][:10]}. The original article is preserved in the Spanish version.</p><h2>What to consider today</h2><p>Before using the information for your business, confirm the current requirements, the relevant period and how the rules apply to your operations. A historic article cannot establish your current obligations or guarantee a tax outcome.</p><h2>Prepare your consultation</h2><p>Explain the decision you need to make, who is involved and what information is available. Agree the documents needed for an assessment and the scope of any written deliverables. Avoid sending confidential files through the initial consultation form.</p><p><a href="{alt}">Read the original Spanish publication ↗</a></p>'
 out+=f'<section class="wrap archive-body prose"><div class="archive-notice"><p class="eyebrow">{"Publicación original" if es else "Original publication"} · <time datetime="{p["date"][:10]}">{p["date"][:10]}</time><p>{note}</p>{"" if original else "<p>English summary. The complete original text is available in Spanish.</p>"}</div>{content}<p class="article-back"><a href="{t["blog"]}">← {t["insights"]}</a></p></section>'
 out+=consultation(path,lang)+page_end(path,lang);save(path,out)
def support_page(lang,key):
 t=L[lang];es=lang=='es';other='en' if es else 'es';path=t[key];alt=L[other][key]
 if key=='trabajo':
  title='Talento para una firma con trayectoria' if es else 'Talent for an experienced firm'
  paragraphs=[('Información sobre oportunidades' if es else 'Information about opportunities','Para consultar oportunidades profesionales en González Armendáriz, comuníquese directamente con la firma. La disponibilidad de vacantes y el canal de recepción de candidaturas deben confirmarse.' if es else 'To ask about professional opportunities at González Armendáriz, contact the firm directly. Vacancy availability and the application channel must be confirmed.'),('Antes de compartir sus datos' if es else 'Before sharing your details','No envíe documentos de identidad ni información sensible por el formulario de consulta empresarial. Solicite primero el canal y las condiciones para presentar su candidatura.' if es else 'Do not send identity documents or sensitive information through the business consultation form. First request the appropriate channel and conditions for applying.')]
 elif key=='cookie_url':
  title=t['cookies'];paragraphs=[('Herramientas de este sitio' if es else 'Tools on this website','Esta versión no carga etiquetas de analítica ni publicidad. La tipografía y las imágenes de la firma se sirven desde el propio sitio.' if es else 'This version does not load analytics or advertising tags. The firm’s fonts and images are served from this website.'),('Servicios externos' if es else 'External services','El mapa de Google se carga solo cuando usted lo solicita. Al abrir WhatsApp o Google Maps, aplican también las condiciones y políticas de esos proveedores.' if es else 'The Google map loads only when you request it. When opening WhatsApp or Google Maps, those providers’ terms and policies also apply.'),('Preferencias opcionales' if es else 'Optional preferences','Si se habilitan herramientas opcionales, el sitio dispone de controles para aceptar, rechazar o elegir categorías. Las etiquetas y la política definitiva requieren configuración y revisión antes de activarse.' if es else 'If optional tools are enabled, the website has controls to accept, reject or choose categories. Tags and the final policy require configuration and review before activation.')]
 else:
  title=t['privacy'];paragraphs=[('Cómo funciona su solicitud' if es else 'How your request works','El formulario prepara un mensaje de WhatsApp con nombre, empresa, teléfono y servicio de interés. Los datos no se envían a un servidor de formularios de este sitio. Usted debe enviar el mensaje en WhatsApp para contactar a la firma.' if es else 'The form prepares a WhatsApp message with your name, company, phone and service of interest. Details are not sent to a form server on this website. You must send the message in WhatsApp to contact the firm.'),('Comparta solo lo necesario' if es else 'Share only what is necessary','Utilice la solicitud inicial para describir su necesidad. No incluya documentos fiscales, bancarios, identificaciones ni otros datos sensibles. Confirme con la firma un canal adecuado para compartir documentación.' if es else 'Use the initial request to describe your needs. Do not include tax or bank documents, identification or other sensitive data. Confirm an appropriate document-sharing channel with the firm.'),('Aviso integral' if es else 'Full privacy notice','El aviso integral aprobado, la identidad jurídica del responsable y el procedimiento para ejercer derechos de acceso, rectificación, cancelación y oposición están pendientes de confirmación por la firma. Esta información operativa no sustituye ese aviso. Puede solicitar información de privacidad por teléfono.' if es else 'The approved full notice, the controller’s legal identity and the procedure for exercising access, rectification, cancellation and objection rights are pending confirmation by the firm. This operational information does not replace that notice. You can request privacy information by phone.')]
 d={'title':t['careers' if key=='trabajo' else 'cookies' if key=='cookie_url' else 'privacy']+' | González Armendáriz','description':'Consulte información del sitio y contacte a González Armendáriz en San Pedro Garza García.' if es else 'Read website information and contact González Armendáriz in San Pedro Garza García.','h1':title,'faqs':[]}
 d['noindex']=key!='trabajo'
 out=page_start(path,lang,alt,d,'careers' if key=='trabajo' else 'legal')+intro(d,lang,t['careers' if key=='trabajo' else 'cookies' if key=='cookie_url' else 'privacy'])
 out+='<section class="section wrap support-layout prose">'+''.join(f'<section><h2>{E(h)}</h2><p>{E(p)}</p></section>' for h,p in paragraphs)+f'<div class="support-contact"><h2>{t["contact"]}</h2>{phones()}<p><a href="{t["contacto"]}">{t["contact"]} ↗</a></p></div></section>'+page_end(path,lang);save(path,out)
for lang in ['es','en']:
 home(lang);register('/' if lang=='es' else '/en/',lang,'/en/' if lang=='es' else '/','home')
 for service in D['landings']:
  landing(service,lang);register(D['landings'][service][lang]['url'],lang,D['landings'][service]['en' if lang=='es' else 'es']['url'],'landing')
 overview(lang)
 for i in range(5):service_page(i,lang)
 firm_page(lang);firm_page(lang,True);contact_page(lang);insights_page(lang)
 for g in GUIDES:guide_page(g,lang)
 for i,p in enumerate(ARCHIVE_ES):archive_page(p,i,lang)
 for key in ['legal','cookie_url','trabajo']:support_page(lang,key)
# Render serves this document for missing routes; a bilingual route back home is included.
d={'title':'Página no encontrada | González Armendáriz','description':'Regrese al sitio de González Armendáriz.','h1':'Esta página no está disponible','faqs':[]}
error=head('/404/','es','/en/',d,True)+'<body data-page="404">'+header('/','es','/en/')+'<main id="main"><section class="section wrap error-page"><p class="eyebrow">404 / Page not found</p><h1>'+d['h1']+'</h1><p>Puede explorar nuestros servicios o volver al inicio.<br>This page is unavailable. Explore our services or return home.</p>'+button('Ir al inicio','/')+' '+button('View English website','/en/')+'</section></main>'+footer('/','es')+'</body></html>'
(SITE/'404.html').write_text(error)
(SITE/'route-manifest.json').write_text(json.dumps(ROUTES,ensure_ascii=False,indent=2))
urls=[r['path'] for r in ROUTES if r['type'] not in ['landing','archive','legal']]
(SITE/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join(f'<url><loc>{DOMAIN+p}</loc></url>\n' for p in urls)+'</urlset>')
(SITE/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: '+DOMAIN+'/sitemap.xml\n')
print(f'Generated {len(ROUTES)} pages plus custom 404; {len(urls)} sitemap URLs.')
