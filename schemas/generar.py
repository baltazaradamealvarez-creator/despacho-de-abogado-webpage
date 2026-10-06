"""Genera JSON-LD por URL a partir del contenido aprobado de la entrega."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'schemas'
BASE='https://gonzalezarmendariz.com'
ORG=BASE+'/#organization'; OFFICE=BASE+'/#office'; PERSON=BASE+'/#alejandro-gonzalez'
SERVICES=[('contabilidad-monterrey','accounting-monterrey','Contabilidad y Cumplimiento Fiscal','Accounting and Tax Compliance'),('asesoria-fiscal-monterrey','tax-advisory-monterrey','Asesoría Fiscal','Tax Advisory'),('auditoria-monterrey','audit-monterrey','Auditoría','Audit'),('consultoria-negocios-monterrey','business-consulting-monterrey','Consultoría de Negocios','Business Consulting'),('servicios-administrativos-monterrey','administrative-services-monterrey','Servicios Administrativos','Administrative Services')]
PAGES=[('/', '/en/', 'Inicio','Home','WebPage'),('/servicios/','/en/services/','Servicios','Services','CollectionPage'),('/nosotros/','/en/about/','Nosotros','About','AboutPage'),('/equipo/','/en/team/','Equipo','Team','CollectionPage'),('/contacto/','/en/contact/','Contacto','Contact','ContactPage'),('/perspectivas/','/en/insights/','Perspectivas','Insights','CollectionPage')]
for es,en,nes,nen in SERVICES:PAGES.append(('/servicios/'+es+'/', '/en/services/'+en+'/',nes,nen,'service'))
for i,(es,en) in enumerate([('contabilidad','accounting'),('asesoria-fiscal','tax-advisory'),('auditoria','audit')]):PAGES.append(('/lp/'+es+'/', '/en/lp/'+en+'/',SERVICES[i][2],SERVICES[i][3],'landing'))
faq_path=ROOT/'entregables'/'faq-por-url.json'
FAQ=json.loads(faq_path.read_text()) if faq_path.exists() else {}
def shared(english):
 return [
 {'@type':'Organization','@id':ORG,'name':'González Armendáriz','url':BASE+'/','telephone':'+528183634412','founder':{'@id':PERSON},'location':{'@id':OFFICE}},
 {'@type':'AccountingService','@id':OFFICE,'name':'González Armendáriz','url':BASE+'/en/' if english else BASE+'/','telephone':'+528183634412','parentOrganization':{'@id':ORG},'address':{'@type':'PostalAddress','streetAddress':'Av. Lázaro Cárdenas #2400 Pte., Edificio Losoles Int. PB 18, Col. Residencial San Agustín','addressLocality':'San Pedro Garza García','addressRegion':'Nuevo León','postalCode':'66260','addressCountry':'MX'}},
 {'@type':'Person','@id':PERSON,'name':'Alejandro González','jobTitle':'Founding Director' if english else 'Director Fundador','worksFor':{'@id':ORG}},
 {'@type':'WebSite','@id':BASE+'/#website','url':BASE+'/','name':'González Armendáriz','publisher':{'@id':ORG},'inLanguage':['es-MX','en-US']}
 ]
manifest=[]
for es,en,nes,nen,kind in PAGES:
 for english,path,title in [(False,es,nes),(True,en,nen)]:
  url=BASE+path; lang='en-US' if english else 'es-MX'; home='/en/' if english else '/'
  graph=shared(english)
  page={'@type':kind if kind not in ('service','landing') else 'WebPage','@id':url+'#webpage','url':url,'name':title+' | González Armendáriz','inLanguage':lang,'isPartOf':{'@id':BASE+'/#website'},'publisher':{'@id':ORG},'about':{'@id':ORG}}
  if kind in ('service','landing'):
   match=next(x for x in SERVICES if title in x[2:])
   canonical=BASE+('/en/services/'+match[1]+'/' if english else '/servicios/'+match[0]+'/')
   serviceid=canonical+'#service'
   graph.append({'@type':'Service','@id':serviceid,'name':title,'serviceType':title,'url':canonical,'provider':{'@id':OFFICE},'areaServed':[{'@type':'City','name':'Monterrey'},{'@type':'City','name':'San Pedro Garza García'}]})
   page['about']={'@id':serviceid}
  if path not in ('/','/en/') and kind!='landing':
   crumbs=[{'@type':'ListItem','position':1,'name':'Home' if english else 'Inicio','item':BASE+home}]
   if kind=='service':crumbs.append({'@type':'ListItem','position':2,'name':'Services' if english else 'Servicios','item':BASE+('/en/services/' if english else '/servicios/')})
   crumbs.append({'@type':'ListItem','position':len(crumbs)+1,'name':title,'item':url})
   graph.append({'@type':'BreadcrumbList','@id':url+'#breadcrumb','itemListElement':crumbs});page['breadcrumb']={'@id':url+'#breadcrumb'}
  if path in FAQ:
   rows=FAQ[path]
   if isinstance(rows,dict):rows=rows.get('faq',rows.get('faqs',[]))
   qas=[{'@type':'Question','name':r.get('question',r.get('q')),'acceptedAnswer':{'@type':'Answer','text':r.get('answer',r.get('a'))}} for r in rows]
   if qas:
    graph.append({'@type':'FAQPage','@id':url+'#faq','inLanguage':lang,'isPartOf':{'@id':url+'#webpage'},'mainEntity':qas});page['hasPart']={'@id':url+'#faq'}
  graph.append(page)
  filename=('en' if english else 'es')+'-'+('home' if path in ('/','/en/') else path.strip('/').replace('/','-').removeprefix('en-'))+'.json'
  payload={'@context':'https://schema.org','@graph':graph}
  (OUT/filename).write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
  manifest.append({'url':url,'file':filename,'language':lang,'faq_count':len(FAQ.get(path,[])),'robots':'noindex,follow' if kind=='landing' else 'index,follow'})
(OUT/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print(f'{len(manifest)} páginas generadas; {sum(p["faq_count"] for p in manifest)} FAQ.')
