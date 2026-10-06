import urllib.request,concurrent.futures,json,os
from bs4 import BeautifulSoup
base='https://gonzalezarmendariz.com/'
paths=['wp-json/wp/v2/posts?per_page=100','wp-sitemap.xml','robots.txt','blog/','equipo/','nosotros/','contacto/','servicios/','en/']
def f(path):
 try:
  r=urllib.request.urlopen(base+path,timeout=45); body=r.read().decode('utf-8','ignore');name=path.replace('/','_').replace('?','_');open('/workspace/gonzalez-armendariz/fuentes/'+name+'.txt','w').write(body)
  s=BeautifulSoup(body,'html.parser');return path,r.status,s.get_text(' ',strip=True)[-16000:]
 except Exception as e:return path,str(e)
with concurrent.futures.ThreadPoolExecutor(max_workers=9) as ex:
 for result in ex.map(f,paths): print(json.dumps(result,ensure_ascii=False))
