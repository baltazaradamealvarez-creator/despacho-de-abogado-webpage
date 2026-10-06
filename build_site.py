from pathlib import Path
import json,html,urllib.parse
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
def button(text,href,light=False):return f'<a class="button {"light" if light else ""}" href="{E(href)}">{E(text)}<span class="arrow" aria-hidden="true">↗</span></a></footer></div>'
def brand(path,lang,landing=False):
 # No link to another page on the ad landing: the brand remains a visual signpost.
 content=f'<img class="brand-logo" src="{relative(path,"/assets/logo.png")}" width="613" height="199" alt="González Armendáriz · {'Consultoría contable y fiscal' if lang=='es' else 'Accounting and tax advisory'}">'
 return '<div class="brand">'+content+'</div>' if landing else f'<a class="brand" href="{relative(path,"/en/" if lang=="en" else "/")}">{content}</a>'
def header(path,lang,alternate,landing=False):
 t=L[lang]
 language=f'<a class="language" href="{relative(path,alternate)}" lang="{"en" if lang=="es" else "es"}" aria-label="{"EN: View in English" if lang=="es" else "ES: Ver en español"}">{"EN" if lang=="es" else "ES"} <span aria-hidden="true">↗</span></a></footer></div>'
 if landing: nav='<div class="header-nav">'+language+'</div>'
 else:
  links=f'<a href="#servicios">{t["services"]}</a><a href="#firma">{t["about"]}</a><a href="{DOMAIN+t["equipo"]}">{t["team"]}</a><a href="{DOMAIN+t["blog"]}">{t["insights"]}</a><a href="#consulta">{t["contact"]}</a>'
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
 <p class="form-note">{t['note']} <a href="{DOMAIN+t['legal']}">{t['privacy']}</a>.</p>
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
  links=f'<a href="{DOMAIN+t["legal"]}">{t["privacy"]}</a><a href="{DOMAIN+t["cookie_url"]}">{t["cookies"]}</a>'
  contact=f'<div class="footer-contact"><a href="tel:+528183634412">+52 818 363 4412</a><span>San Pedro Garza García · Nuevo León</span></div>'
 else:
  links=''.join(f'<a href="{DOMAIN+t[key]}">{t[label]}</a>' for key,label in [('servicios','services'),('nosotros','about'),('equipo','team'),('blog','insights'),('contacto','contact'),('trabajo','careers'),('legal','privacy'),('cookie_url','cookies')]);contact=''
 return f'<div class="wrap"><footer class="site-footer"><div>{contact}<p>© 2026 González Armendáriz. {t["rights"]}</p></div><div class="footer-links">{links}</div><a class="wa-float" href="https://wa.me/528128845949" aria-label="{t["wa"]}">WhatsApp <span aria-hidden="true">↗</span></a></footer></div>'
def graph(path,lang,data,landing=False,serviceid=None):
 org={'@type':'Organization','@id':DOMAIN+'/#organization','name':'González Armendáriz','url':DOMAIN+'/','logo':DOMAIN+'/assets/logo.png','founder':{'@id':DOMAIN+'/#alejandro-gonzalez'}}
 office={'@type':'AccountingService','@id':DOMAIN+'/#office','name':'González Armendáriz','url':DOMAIN+'/','parentOrganization':{'@id':org['@id']},'telephone':'+528183634412','address':{'@type':'PostalAddress','streetAddress':'Av. Lázaro Cárdenas #2400 Pte., Edificio Losoles Int. PB 18, Col. Residencial San Agustín','addressLocality':'San Pedro Garza García','addressRegion':'Nuevo León','postalCode':'66260','addressCountry':'MX'},'areaServed':[{'@type':'City','name':'Monterrey'},{'@type':'City','name':'San Pedro Garza García'}],'contactPoint':[{'@type':'ContactPoint','telephone':n,'contactType':'customer service'} for n in ['+528183634412','+528183630502','+528183634260']]}
 person={'@type':'Person','@id':DOMAIN+'/#alejandro-gonzalez','name':'Alejandro González','jobTitle':L[lang]['founder'],'worksFor':{'@id':org['@id']}}
 web={'@type':'WebPage','@id':DOMAIN+path+'#webpage','url':DOMAIN+path,'name':data['title'],'description':data['description'],'inLanguage':L[lang]['locale'],'about':{'@id':org['@id']},'isPartOf':{'@id':DOMAIN+'/#website'}}
 website={'@type':'WebSite','@id':DOMAIN+'/#website','url':DOMAIN+'/','name':'González Armendáriz','publisher':{'@id':org['@id']},'inLanguage':['es-MX','en-US']}
 faqpage={'@type':'FAQPage','@id':DOMAIN+path+'#faq','url':DOMAIN+path,'inLanguage':L[lang]['locale'],'isPartOf':{'@id':web['@id']},'mainEntity':[{'@type':'Question','name':x['q'],'acceptedAnswer':{'@type':'Answer','text':x['a']}} for x in data['faqs']]}
 nodes=[org,office,person,website,web,faqpage]
 if landing:
  idx=SERVICE_IDS.index(serviceid)
  service={'@type':'Service','@id':DOMAIN+D['home'][lang]['services'][idx]['url']+'#service','name':D['home'][lang]['services'][idx]['name'],'serviceType':D['home'][lang]['services'][idx]['name'],'provider':{'@id':office['@id']},'areaServed':[{'@type':'City','name':'Monterrey'},{'@type':'City','name':'San Pedro Garza García'}],'url':DOMAIN+D['home'][lang]['services'][idx]['url']}
  nodes.append(service);web['about']={'@id':service['@id']}
 return {'@context':'https://schema.org','@graph':nodes}
def head(path,lang,alt,data,landing=False,serviceid=None):
 espath=path if lang=='es' else alt;enpath=path if lang=='en' else alt
 logoico='data:image/svg+xml,'+urllib.parse.quote('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" fill="#102A35"/><text x="32" y="44" text-anchor="middle" font-family="Georgia" font-size="37" fill="#F5F2EB">G</text></svg>')
 schema=json.dumps(graph(path,lang,data,landing,serviceid),ensure_ascii=False).replace('</','<\\/')
 return f'''<!doctype html><html lang="{L[lang]['locale']}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{E(data['title'])}</title><meta name="description" content="{E(data['description'])}"><meta name="robots" content="{'noindex,follow' if landing else 'index,follow'}"><link rel="canonical" href="{DOMAIN+path}"><link rel="alternate" hreflang="es-MX" href="{DOMAIN+espath}"><link rel="alternate" hreflang="en-US" href="{DOMAIN+enpath}"><link rel="alternate" hreflang="x-default" href="{DOMAIN+espath}"><meta property="og:type" content="website"><meta property="og:site_name" content="González Armendáriz"><meta property="og:title" content="{E(data['title'])}"><meta property="og:description" content="{E(data['description'])}"><meta property="og:url" content="{DOMAIN+path}"><meta property="og:locale" content="{'es_MX' if lang=='es' else 'en_US'}"><meta property="og:image" content="{DOMAIN}/assets/social-{lang}.png"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="González Armendáriz · {'Contabilidad, auditoría y asesoría fiscal' if lang=='es' else 'Accounting, audit and tax advisory'}"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{E(data['title'])}"><meta name="twitter:description" content="{E(data['description'])}"><meta name="twitter:image" content="{DOMAIN}/assets/social-{lang}.png"><meta name="twitter:image:alt" content="González Armendáriz · {'Contabilidad, auditoría y asesoría fiscal' if lang=='es' else 'Accounting, audit and tax advisory'}"><meta property="og:locale:alternate" content="{'en_US' if lang=='es' else 'es_MX'}"><link rel="icon" type="image/png" href="{relative(path,'/assets/favicon.png')}"><link rel="preload" href="{relative(path,'/assets/cormorant-latin.woff2')}" as="font" type="font/woff2" crossorigin><link rel="stylesheet" href="{relative(path,'/assets/site.css')}"><script type="application/ld+json">{schema}</script><script src="{relative(path,'/assets/consent.js')}" defer></script><script src="{relative(path,'/assets/site.js')}" defer></script></head>'''
def save(path,text):
 file=SITE/local(path);file.parent.mkdir(parents=True,exist_ok=True);file.write_text(text.replace('↗','<svg class="arrow-svg" viewBox="0 0 24 24" width="20" height="20" aria-hidden="true"><path d="M5 19 19 5M5 5h14v14" fill="none" stroke="currentColor" stroke-width="1.5"/></svg>'),encoding='utf-8')
def home(lang):
 t=L[lang];d=D['home'][lang];path='/' if lang=='es' else '/en/';alt='/en/' if lang=='es' else '/'
 out=head(path,lang,alt,d)+f'<body data-page="home"><a class="skip" href="#main">{t["skip"]}</a>'+header(path,lang,alt)+'<main id="main">'
 out+=f'<section class="hero wrap" aria-labelledby="hero-title"><div class="hero-top"><p class="eyebrow">San Pedro Garza García · Nuevo León</p><p class="eyebrow">González Armendáriz</p></div><div class="hero-rule" aria-hidden="true"></div><h1 id="hero-title">{d["h1"]}</h1><div class="hero-bottom"><p>{d["subtitle"]}</p>{button(t["cta"],"#consulta")}</div></section>'
 out+='<section class="wrap" aria-label="'+('La firma en cifras' if lang=='es' else 'The firm in figures')+'"><div class="stats">'+''.join(f'<div class="stat"><strong>{v}</strong><span>{t[k]}</span></div>' for v,k in [('28+','years'),('400+','businesses'),('30','members')])+'</div></section>'
 cards=''.join(f'<article class="service"><span class="number" aria-hidden="true">0{i+1}</span><h3><a href="{DOMAIN+s["url"]}">{E(s["name"])}</a></h3><p>{E(s["line"])}</p></article>' for i,s in enumerate(d['services']))
 out+=f'<section id="servicios" class="section wrap" aria-labelledby="services-title"><div class="section-head"><p class="eyebrow">01 / {t["services"]}</p><h2 id="services-title">{t["service_heading"]}</h2></div><div class="services">{cards}</div></section>'
 pillars=''.join(f'<div class="pillar"><h3>{E(p["title"])}</h3><p>{E(p["text"])}</p></div>' for p in d['pillars'])
 out+=f'<section class="section dark" aria-labelledby="why-title"><div class="wrap"><div class="section-head"><p class="eyebrow">02 / {t["why"]}</p><h2 id="why-title">{t["pillars_heading"]}</h2></div><div class="pillars">{pillars}</div></div></section>'
 out+=f'<section id="firma" class="section wrap leadership" aria-labelledby="leadership-title"><img class="founder-image" src="{relative(path,"/assets/fundador.webp")}" width="465" height="500" loading="lazy" decoding="async" alt="{t["alt"]}"><div class="founder-text"><p class="eyebrow">03 / {t["leadership"]}</p><h2 id="leadership-title">{d["leadership"]["headline"]}</h2><p>{d["leadership"]["text"]}</p><div class="signature"><div>Alejandro González<span>{t["founder"]}</span></div><a href="{DOMAIN+t["nosotros"]}">{t["firm"]} ↗</a></div></div></section>'
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
for lang in ['es','en']:
 home(lang)
 for service in D['landings']:landing(service,lang)
print('Generated 2 home versions and 6 ad landing pages.')
