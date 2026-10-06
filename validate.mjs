import { createRequire } from 'node:module';
const require=createRequire(import.meta.url);
const {chromium}=require('playwright');
import fs from 'node:fs';
import {fileURLToPath} from 'node:url';
const root=fileURLToPath(new URL('.',import.meta.url)).replace(/\/$/,'');
const browser=await chromium.launch({executablePath:'/usr/bin/chromium',headless:true,args:['--no-sandbox']});
const routes=['/','/en/','/lp/contabilidad/','/lp/asesoria-fiscal/','/lp/auditoria/','/en/lp/accounting/','/en/lp/tax-advisory/','/en/lp/audit/'];
const results=[];
for(const width of [320,390,768,1440]){
 const context=await browser.newContext({viewport:{width,height:960}});
 for(const route of routes){
  const page=await context.newPage();const errors=[];const remote=[];
  page.on('pageerror',e=>errors.push(e.message));page.on('request',r=>{if(!r.url().startsWith('http://localhost:8765'))remote.push(r.url());});
  await page.goto('http://localhost:8765'+route);await page.evaluate(()=>document.fonts.ready);
  const info=await page.evaluate(()=>{
   const schemas=[...document.querySelectorAll('script[type="application/ld+json"]')].map(x=>JSON.parse(x.textContent));
   const faqs=schemas.flatMap(x=>x['@graph']).find(x=>x['@type']==='FAQPage').mainEntity;
   const visible=[...document.querySelectorAll('.faqs details')].map(x=>({q:x.querySelector('summary').textContent,a:x.querySelector('p').textContent}));
   return{width:innerWidth,documentWidth:document.documentElement.scrollWidth,h1:document.querySelectorAll('h1').length,sections:document.querySelectorAll('main>section').length,title:document.title.length,description:document.querySelector('meta[name="description"]').content.length,formFields:[...document.querySelectorAll('form input,form select')].map(x=>x.name),missingAlt:[...document.images].filter(x=>!x.hasAttribute('alt')).length,faqMatch:JSON.stringify(visible)===JSON.stringify(faqs.map(x=>({q:x.name,a:x.acceptedAnswer.text}))),iframes:document.querySelectorAll('iframe').length,tagsLoaded:!!window.dataLayer,assetsLoaded:[...document.images].filter(x=>x.loading!=='lazy').every(x=>x.complete&&x.naturalWidth>0),zoomAllowed:!document.querySelector('meta[name="viewport"]').content.includes('maximum-scale')};
  });
  const passed=info.documentWidth<=width&&info.h1===1&&info.title<=60&&info.description<=155&&info.formFields.join(',')==='name,company,phone,service'&&info.missingAlt===0&&info.faqMatch&&info.iframes===0&&!info.tagsLoaded&&info.assetsLoaded&&info.zoomAllowed&&errors.length===0&&remote.length===0;
  results.push({route,width,passed,...info,errors,remote});
  if(width===1440&&route==='/')await page.screenshot({path:root+'/validacion/home-desktop.png'});
  if(width===390&&route==='/')await page.screenshot({path:root+'/validacion/home-mobile.png'});
  if(width===1440&&route==='/lp/contabilidad/')await page.screenshot({path:root+'/validacion/landing-desktop.png'});
  await page.close();
 }
 await context.close();
}
const page=await browser.newPage({viewport:{width:390,height:844}});
await page.goto('http://localhost:8765/');
await page.evaluate(()=>{window.openedUrl=null;window.open=(url)=>{window.openedUrl=url;return null;};window.gaConsent={analytics:true};});
await page.locator('#name').fill('Prueba técnica');await page.locator('#company').fill('Empresa de prueba');await page.locator('#phone').fill('8180000000');await page.locator('#service').selectOption({label:'Auditoría'});await page.locator('button[type=submit]').click();
const form=await page.evaluate(()=>({whatsappDestination:window.openedUrl?.startsWith('https://wa.me/528128845949?text='),hasCompany:decodeURIComponent(window.openedUrl||'').includes('Empresa de prueba'),hasFallbackLink:!!document.querySelector('[role=status] a'),handoff:window.dataLayer.some(x=>x.event==='consultation_handoff'),noConfirmedLead:window.dataLayer.every(x=>x.event!=='generate_lead'),noPII:!JSON.stringify(window.dataLayer).includes('8180000000')&&!JSON.stringify(window.dataLayer).includes('Prueba técnica')}));
await page.locator('summary').filter({hasText:'Menú'}).click();
const menu=await page.locator('.mobile-links').isVisible();
await page.locator('.faqs details').first().locator('summary').click();const faqOpened=await page.locator('.faqs details').first().getAttribute('open')!==null;
const keyboard=await page.evaluate(()=>[...document.querySelectorAll('a,button,input,select,summary')].every(x=>x.tabIndex>=0));
const report={date:'2026-10-06',responsive:results,form,menu,faqOpened,keyboard,allPassed:results.every(x=>x.passed)&&Object.values(form).every(Boolean)&&menu&&faqOpened&&keyboard};
fs.writeFileSync(root+'/validacion/codigo.json',JSON.stringify(report,null,2));
console.log(JSON.stringify({views:results.length,failedViews:results.filter(x=>!x.passed).map(x=>({route:x.route,width:x.width,documentWidth:x.documentWidth,errors:x.errors,remote:x.remote})),form,menu,faqOpened,keyboard,allPassed:report.allPassed},null,2));
await browser.close();
