/* No advertising or analytics scripts load in this deliverable.
   Only dispatch allowlisted, non-PII events after a CMP grants analytics consent. */
(() => {
  const lang=document.documentElement.lang.startsWith('en')?'en':'es';
  const page=document.body.dataset.page || 'home';
  const track=(event,extra={})=>{
    if(window.gaConsent?.analytics !== true) return;
    window.dataLayer=window.dataLayer||[];
    window.dataLayer.push({event,page_type:page,language:lang,...extra});
  };
  document.querySelectorAll('[data-consultation]').forEach(form=>{
    form.addEventListener('submit',event=>{
      event.preventDefault();
      if(!form.reportValidity())return;
      const data=new FormData(form);
      const phone=String(data.get('phone')||'');
      const input=form.querySelector('[name="phone"]');
      if(phone.replace(/\D/g,'').length<10){
        input.setCustomValidity(lang==='es'?'Escriba al menos 10 dígitos.':'Enter at least 10 digits.');input.reportValidity();return;
      }
      const text=lang==='es'
        ? `Hola, deseo agendar una consulta.\nNombre: ${data.get('name')}\nEmpresa: ${data.get('company')}\nTeléfono: ${phone}\nServicio: ${data.get('service')}`
        : `Hello, I would like to schedule a consultation.\nName: ${data.get('name')}\nCompany: ${data.get('company')}\nPhone: ${phone}\nService: ${data.get('service')}`;
      const destination='https://wa.me/528128845949?text='+encodeURIComponent(text);
      const status=form.querySelector('[role="status"]');
      status.replaceChildren();
      const link=document.createElement('a');link.href=destination;link.target='_blank';link.rel='noopener noreferrer';
      link.textContent=lang==='es'?'Abrir WhatsApp y enviar la solicitud':'Open WhatsApp and send your request';
      status.append(link);
      // This is a handoff, never a successful submission or confirmed appointment.
      track('consultation_handoff',{channel:'whatsapp'});
      window.open(destination,'_blank','noopener,noreferrer');
    });
    form.querySelector('button[type="submit"]').disabled=false;
    form.querySelector('[name="phone"]').addEventListener('input',e=>e.target.setCustomValidity(''));
  });
  document.querySelectorAll('a[href^="tel:"]').forEach(a=>a.addEventListener('click',()=>track('click_phone')));
  document.querySelectorAll('a[href^="mailto:"]').forEach(a=>a.addEventListener('click',()=>track('click_email')));
  document.querySelectorAll('a[href^="https://wa.me/"]').forEach(a=>a.addEventListener('click',()=>track('click_whatsapp')));
  document.querySelectorAll('.mobile-menu a').forEach(a=>a.addEventListener('click',()=>a.closest('details').open=false));
  document.addEventListener('keydown',event=>{
    if(event.key!=='Escape'||document.querySelector('dialog[open]'))return;
    const menu=document.querySelector('.mobile-menu[open]');
    if(menu){menu.open=false;menu.querySelector('summary').focus();}
  });
  let scrolled=false;
  window.addEventListener('scroll',()=>{
    const total=document.documentElement.scrollHeight-innerHeight;
    if(!scrolled&&total>0&&scrollY/total>=.75){scrolled=true;track('scroll_75');}
  },{passive:true});
  document.querySelectorAll('[data-map]').forEach(button=>button.addEventListener('click',()=>{
    const frame=document.createElement('iframe');
    frame.title=lang==='es'?'Ubicación de González Armendáriz':'González Armendáriz office location';
    frame.src='https://maps.google.com/maps?q='+encodeURIComponent('Av. Lázaro Cárdenas 2400 Pte., Edificio Losoles, Residencial San Agustín, San Pedro Garza García, Nuevo León, 66260')+'&output=embed';
    frame.loading='lazy';frame.referrerPolicy='no-referrer-when-downgrade';
    const holder=button.closest('.map');holder.replaceChildren(frame);holder.classList.add('loaded');
  }));
})();
