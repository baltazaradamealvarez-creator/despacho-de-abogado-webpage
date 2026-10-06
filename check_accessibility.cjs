const {chromium}=require('playwright');const fs=require('fs');const root=__dirname;const axe=fs.readFileSync(require.resolve('axe-core/axe.min.js'),'utf8');
(async()=>{const browser=await chromium.launch({executablePath:'/usr/bin/chromium',args:['--no-sandbox']});const result=[];
for(const [route,width,consent] of [['/',390,false],['/',1440,false],['/en/',390,false],['/lp/contabilidad/',390,false],['/lp/contabilidad/',1440,false],['/en/lp/accounting/',390,false],['/',390,true]]){
 const page=await browser.newPage({viewport:{width,height:900}});if(consent)await page.addInitScript(()=>window.GA_SITE_SETTINGS={optionalTagsEnabled:true,policyVersion:'qa-only'});await page.goto('http://localhost:8765'+route);await page.evaluate(()=>document.fonts.ready);await page.addScriptTag({content:axe});
 const a=await page.evaluate(()=>axe.run(document,{runOnly:{type:'tag',values:['wcag2a','wcag2aa','wcag21a','wcag21aa','best-practice']}}));
 result.push({route,width,consent,violations:a.violations.map(x=>({id:x.id,impact:x.impact,description:x.description,nodes:x.nodes.map(n=>n.target)}))});
 if(consent){await page.getByRole('button',{name:'Configurar preferencias'}).click();await page.getByLabel('Analítica',{exact:true}).check();await page.getByRole('button',{name:'Guardar preferencias'}).click();const state=await page.evaluate(()=>({consent:window.gaConsent,bannerHidden:document.querySelector('.consent-banner').hidden,dialogClosed:!document.querySelector('.consent-dialog').open}));result.push({consentFlow:state});}
 await page.close();}
fs.writeFileSync(root+'/validacion/accesibilidad.json',JSON.stringify(result,null,2));console.log(JSON.stringify(result,null,2));await browser.close();})();
