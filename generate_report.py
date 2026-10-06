from pathlib import Path
import markdown,json,base64,re
from bs4 import BeautifulSoup
ROOT=Path(__file__).parent
FILES=sorted(ROOT.joinpath('entregables').glob('[0-9][0-9]-*.md'))
assert len(FILES)==15
intro='''# González Armendáriz · Rediseño, SEO y captación

**Entrega integral · 6 de octubre de 2026 · Español e inglés**

Fuente primaria: [sitio público de la firma](https://gonzalezarmendariz.com/) y datos reales del briefing. El documento reúne los quince entregables en el orden solicitado. La auditoría incluye el contenido actual de18artículos, sin acceso a Search Console, Analytics ni cuentas publicitarias. Volúmenes de búsqueda, honorarios, horarios, certificaciones y datos legales no se inventan.

**[SUPUESTO]** Se conserva el dominio actual; WordPress puede migrarse a bloques nativos con tema ligero. El formulario de demostración prepara una solicitud por WhatsApp. Año editorial propuesto:2027. **[PENDIENTE]** Validar alcances comerciales, materiales de confianza, textos legales, recepción de formularios y configuración de medición antes de lanzar.

'''
combined=intro+'\n\n---\n\n'.join(p.read_text() for p in FILES)+'\n\n---\n\n# Anexo · Auditoría y trazabilidad\n\n'+ROOT.joinpath('fuentes/auditoria.md').read_text()+'\n\n---\n\n'+ROOT.joinpath('validacion/RESUMEN.md').read_text()
ROOT.joinpath('INFORME.md').write_text(combined)
parts=[];nav=[]
for i,p in enumerate(FILES,1):
 text=p.read_text();title=text.splitlines()[0].lstrip('# ')
 rendered=markdown.markdown(text,extensions=['tables','fenced_code','sane_lists'])
 soup=BeautifulSoup(rendered,'html.parser')
 for j,h in enumerate(soup.find_all(re.compile('^h[1-6]$'))):
  if j==0:h.name='h2'
  else:h.name='h'+str(min(6,int(h.name[1])+1))
 for table in soup.select('table'):
  wrap=soup.new_tag('div',attrs={'class':'table-wrap'});table.wrap(wrap)
 extra=''
 if i==14:
  for filename,alt in [('home-desktop.png','Diseño del inicio en escritorio'),('landing-mobile.png','Landing de contabilidad en móvil')]:
   raw=base64.b64encode(ROOT.joinpath('validacion',filename).read_bytes()).decode()
   extra+=f'<figure><img src="data:image/png;base64,{raw}" alt="{alt}" loading="lazy"><figcaption>{alt}</figcaption></figure>'
  extra='<div class="previews">'+extra+'</div>'
  extra+='<p><a href="site/index.html">Abrir home ES en el paquete</a> · <a href="site/en/index.html">Home EN</a> · <a href="site/lp/contabilidad/index.html">Landing ES</a> · <a href="site/en/lp/accounting/index.html">Landing EN</a></p>'
 parts.append(f'<section id="entregable-{i:02d}">{str(soup)}{extra}</section>')
 nav.append(f'<a href="#entregable-{i:02d}">{title}</a>')
parts.append('<section id="auditoria">'+markdown.markdown(ROOT.joinpath('fuentes/auditoria.md').read_text(),extensions=['tables','fenced_code'])+'</section>')
parts.append('<section id="validacion">'+markdown.markdown(ROOT.joinpath('validacion/RESUMEN.md').read_text(),extensions=['tables','fenced_code'])+'</section>')
css='''*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;font:15px/1.7 Arial,sans-serif;color:#102A35;background:#F5F2EB}a{color:#174D66;text-underline-offset:3px}aside{width:285px;position:fixed;top:0;bottom:0;overflow:auto;padding:32px 24px;background:#102A35;color:#F5F2EB}aside strong{font-family:Georgia,serif;font-size:25px;line-height:1.2;display:block;margin-bottom:10px}aside small{display:block;color:#D0D7D6;margin-bottom:24px}aside a{color:#F5F2EB;display:block;text-decoration:none;font-size:13px;padding:8px 0;border-top:1px solid #3E5660}main{margin-left:285px;padding:50px 55px;max-width:1510px}h1{font:44px/1.1 Georgia,serif;max-width:900px;margin:0 0 25px}h2{font:30px/1.2 Georgia,serif;margin:0 0 26px}h3{font:23px/1.3 Georgia,serif;margin:34px 0 18px}h4{font-size:19px;margin-top:30px}h5,h6{font-size:16px}section{border-top:1px solid #C6C8BE;padding:46px 0;scroll-margin-top:22px}p{max-width:90ch}li{padding-bottom:5px}.intro{padding-bottom:24px}.table-wrap{overflow:auto;margin:25px 0}table{width:100%;border-collapse:collapse;background:#fff;font-size:13px;line-height:1.5;margin:25px 0}th,td{text-align:left;vertical-align:top;padding:13px;border:1px solid #CCD1CF;overflow-wrap:anywhere}th{background:#E7E9E1}code{font:13px/1.5 monospace;overflow-wrap:anywhere}pre{background:#102A35;color:#F5F2EB;padding:22px;overflow:auto}pre code{color:inherit}blockquote{border-left:3px solid #896B43;margin-left:0;padding-left:23px;color:#465D67}.previews{display:grid;grid-template-columns:2fr 1fr;gap:20px;margin-top:35px;align-items:start}.previews figure{margin:0}.previews img{display:block;width:100%;border:1px solid #CCC}.previews figcaption{font-size:12px;margin-top:10px}.stamp{display:inline-block;font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:#52656B;border-bottom:1px solid #896B43;padding-bottom:10px;margin-bottom:28px}:focus-visible{outline:3px solid #896B43;outline-offset:4px}@media(max-width:950px){aside{position:static;width:100%;padding:25px}aside nav{display:grid;grid-template-columns:1fr 1fr;gap:0 18px}main{margin:0;padding:35px 23px}h1{font-size:34px}.previews{grid-template-columns:1fr}}@media print{body{background:#fff;font:11px/1.5 Arial,sans-serif}aside{display:none}main{margin:0;padding:0;max-width:none}h1{font-size:32px}h2{font-size:25px}h3{font-size:18px}section{break-before:page;border:0;padding-top:20px}table{font-size:9px;line-height:1.35;margin:15px 0}th,td{padding:7px;overflow-wrap:anywhere}tr{break-inside:avoid}pre{white-space:pre-wrap;overflow-wrap:anywhere}a{color:#102A35}.previews{display:none}h2,h3,h4{break-after:avoid}}'''
body=f'''<!doctype html><html lang="es-MX"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><title>González Armendáriz · 15 entregables de rediseño</title><style>{css}</style></head><body><aside><strong>González<br>Armendáriz</strong><small>Rediseño · SEO · Captación<br>ES / EN · 06.10.2026</small><nav aria-label="Índice de entregables">{''.join(nav)}<a href="#auditoria">Anexo: auditoría del sitio</a><a href="#validacion">Resultados de validación</a></nav></aside><main><div class="intro"><span class="stamp">Documento de trabajo y código fuente</span>{markdown.markdown(intro)}</div>{''.join(parts)}</main></body></html>'''
ROOT.joinpath('INFORME.html').write_text(body)
print('Report assembled:',len(FILES),'ordered deliverables;',len(combined.split()),'words.')
