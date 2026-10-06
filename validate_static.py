import json
from pathlib import Path
from bs4 import BeautifulSoup
from urllib.parse import urljoin,urlparse,unquote
root=Path(__file__).parent/'site';routes=json.loads((root/'route-manifest.json').read_text());errors=[]
for r in routes:
 p=r['path'];s=BeautifulSoup((root/(p.strip('/')+'/index.html' if p!='/' else 'index.html')).read_text(),'html.parser')
 for rule,valid in [('one h1',len(s.find_all('h1'))==1),('one main',len(s.find_all('main'))==1),('one footer',len(s.find_all('footer'))==1),('meta title length',len(s.title.text)<=60),('description length',len(s.find('meta',attrs={'name':'description'})['content'])<=155)]:
  if not valid:errors.append((p,rule))
 json.loads(s.find('script',attrs={'type':'application/ld+json'}).string)
 for a in s.select('a[href],img[src],script[src],link[rel=stylesheet]'):
  href=a.get('href',a.get('src'))
  if href.startswith(('https:','http:','tel:','mailto:','data:')):
   if a.name=='a' and href.startswith('https://gonzalezarmendariz.com'):errors.append((p,'old host navigation',href))
   continue
  u=urlparse(urljoin('https://local.test'+p,href));target=unquote(u.path);f=root/target.lstrip('/')
  if target.endswith('/'):f=f/'index.html'
  if not f.exists():errors.append((p,'broken local link',href))
  elif u.fragment:
   dest=s if target==p else BeautifulSoup(f.read_text(),'html.parser')
   if not dest.find(id=u.fragment):errors.append((p,'missing anchor',href))
 alt=next((x for x in routes if x['path']==r['alternate']),None)
 if not alt or alt['alternate']!=p:errors.append((p,'nonreciprocal alternate'))
print(json.dumps({'pages':len(routes),'errors':errors},ensure_ascii=False,indent=2))
(root.parent/'validacion/paginas-completas-estatico.json').write_text(json.dumps({'pages':len(routes),'errors':errors},ensure_ascii=False,indent=2))
raise SystemExit(bool(errors))
