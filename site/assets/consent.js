/* Conservative optional consent UI. No analytics/advertising tags are installed.
   Enable only after final privacy text, vendor configuration and legal review.
   Before loading this script set GA_SITE_SETTINGS.optionalTagsEnabled=true.
   Integrate the ga:consent-change event with the chosen CMP/tag implementation. */
(() => {
  window.gaConsent={analytics:false,advertising:false};
  if(window.GA_SITE_SETTINGS?.optionalTagsEnabled!==true)return;
  const en=document.documentElement.lang.startsWith('en');
  const text=en?{
    heading:'Cookie preferences',body:'We use optional tools to measure visits and advertising. You can accept, reject or choose your preferences.',accept:'Accept optional cookies',reject:'Reject optional cookies',configure:'Choose preferences',necessary:'Necessary preferences remain enabled.',analytics:'Analytics',ads:'Advertising',save:'Save preferences',close:'Close',policy:'Cookie policy'
  }:{heading:'Preferencias de cookies',body:'Usamos herramientas opcionales para medir visitas y publicidad. Puede aceptar, rechazar o elegir sus preferencias.',accept:'Aceptar cookies opcionales',reject:'Rechazar cookies opcionales',configure:'Configurar preferencias',necessary:'Las preferencias necesarias permanecen activas.',analytics:'Analítica',ads:'Publicidad',save:'Guardar preferencias',close:'Cerrar',policy:'Política de cookies'};
  const key='ga-consent-v1';let saved=null;
  try{saved=JSON.parse(localStorage.getItem(key));}catch{}
  const banner=document.createElement('aside');banner.className='consent-banner';banner.setAttribute('aria-label',text.heading);
  const message=document.createElement('p');message.textContent=text.body;banner.append(message);
  const actions=document.createElement('div');actions.className='consent-actions';banner.append(actions);
  const dialog=document.createElement('dialog');dialog.className='consent-dialog';dialog.setAttribute('aria-label',text.heading);
  const title=document.createElement('h2');title.textContent=text.heading;dialog.append(title);
  const necessary=document.createElement('p');necessary.textContent=text.necessary;dialog.append(necessary);
  const checks={};
  for(const [category,labelText] of [['analytics',text.analytics],['advertising',text.ads]]){
    const label=document.createElement('label');const check=document.createElement('input');check.type='checkbox';checks[category]=check;label.append(check,document.createTextNode(' '+labelText));dialog.append(label);
  }
  const makeButton=(label,fn)=>{const b=document.createElement('button');b.type='button';b.className='button outline';b.textContent=label;b.addEventListener('click',fn);return b;};
  function apply(value,persist){
    window.gaConsent={analytics:value.analytics===true,advertising:value.advertising===true};
    if(persist){try{localStorage.setItem(key,JSON.stringify({...window.gaConsent,updatedAt:new Date().toISOString(),policyVersion:window.GA_SITE_SETTINGS.policyVersion || 'unconfigured'}));}catch{}}
    window.dispatchEvent(new CustomEvent('ga:consent-change',{detail:{...window.gaConsent}}));
    banner.hidden=true;document.body.classList.remove('consent-open');
  }
  const open=()=>{checks.analytics.checked=window.gaConsent.analytics;checks.advertising.checked=window.gaConsent.advertising;dialog.showModal();};
  actions.append(makeButton(text.accept,()=>apply({analytics:true,advertising:true},true)),makeButton(text.reject,()=>apply({analytics:false,advertising:false},true)),makeButton(text.configure,open));
  const policy=document.createElement('a');policy.href='https://gonzalezarmendariz.com'+(en?'/en/cookie-policy/':'/politica-de-cookies/');policy.textContent=text.policy;actions.append(policy);
  dialog.append(makeButton(text.save,()=>{apply({analytics:checks.analytics.checked,advertising:checks.advertising.checked},true);dialog.close();}),makeButton(text.close,()=>dialog.close()));
  document.body.append(banner,dialog);
  const reserveBanner=()=>document.documentElement.style.setProperty('--consent-height',banner.offsetHeight+'px');
  if('ResizeObserver' in window)new ResizeObserver(reserveBanner).observe(banner);
  else window.addEventListener('resize',reserveBanner);
  reserveBanner();
  const preferences=makeButton(text.heading,open);preferences.className='consent-reopen';document.querySelector('.footer-links')?.append(preferences);
  if(saved&&typeof saved.analytics==='boolean'&&typeof saved.advertising==='boolean'&&saved.policyVersion===window.GA_SITE_SETTINGS.policyVersion)apply(saved,false);
  else{banner.hidden=false;document.body.classList.add('consent-open');}
})();
