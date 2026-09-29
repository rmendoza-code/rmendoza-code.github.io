(function(){
  const $=(s,c=document)=>c.querySelector(s), $$=(s,c=document)=>[...c.querySelectorAll(s)];
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const body=document.body;

  /* ---------- i18n ---------- */
  const EN={
    loading:"Loading portfolio", nav1:"Profile", nav2:"Services", nav3:"Work", nav4:"Experience", nav5:"FAQ", skip:"Skip to content", cv:"Download CV ↓", cvL:"Résumé (PDF)", explore:"Explore dashboard", cta:"Let's talk",
    role:"Data &amp; AI Engineer", lead:"I turn operational data into <em>decisions</em> — and now, into agents that work for you.",
    based:"Mexico City", avail:"Available · 2026", scroll:"Scroll", aboutLabel:"(01) Profile",
    manifesto:"Industrial engineer with 5+ years bridging operations and data. I build the full path of the data —source, transformation, model— and now <span class=\"hl\">AI agents</span> on top of it, because a good dashboard doesn't show data: it answers questions.",
    f2l:"Education", f2s:"Industrial Eng.", f3l:"Certification", f4l:"Specialization", f4s:"AI Technologies", f4p:"Tec de Monterrey — LLMs, RAG, multi-agent, MCP", f5l:"Languages", f5s:"ES · EN B2", f5p:"Italian · Portuguese",
    st1:"years bridging supply chain and data", st2:"fewer critical incidents through predictive analytics", st3:"of manual reporting eliminated per month", st4:"DAX measures delivered in training",
    svcH:"What I<br>build", svcS:"(02) Three fronts,<br>one source of truth",
    s1:"Semantic models, DAX and dashboards in Power BI and Microsoft Fabric designed for leadership to use every Monday — not just to look good in a demo.",
    s2t:"Data engineering", s2:"Lakehouses, pipelines and automations that bring scattered sources —ERP, SharePoint, monthly Excel— into a single version of the truth, ready to analyze.",
    s3t:"GenAI &amp; agents", s3:"RAG, multi-step agents and LLM workflows wired to real business data: assistants that answer, query and act — not just chat.",
    workH:"Selected<br>work", workS:"(03) Dashboards · Data · AI", workNote:"Cards 01–03 open HTML recreations of dashboards built in Power BI: same measure logic and KPIs, with anonymized sample data.",
    p1t:"Procurement Analytics — PR to PO", p1d:"Procurement cycle tracking on a Bronze/Silver/Gold architecture sourced from D365 F&amp;O. Cycle time triangulated against stakeholder data.",
    p2c:"Finance · Budget", p2d:"Financial execution report with an embedded comment-capture page via Microsoft Forms → Power Automate → SharePoint, rendered with HTML Viewer.",
    p3t:"RAMS — Railway maintenance", p3d:"MTBF, MTTR and asset availability metrics for railway operations, with Dataverse to SQL Server pipelines and near real-time fleet monitoring.",
    p4xt:"Unified cloud billing", p4xd:"Automation that consolidates the monthly cloud-consumption reports stored in SharePoint, plus an executive dashboard showing trend and cost per service.",
    p5xt:"Training App", p5xd:"Training app (LMS) built on Microsoft Fabric and Power BI to upskill teams on the organization\u2019s data stack.",
    p6xt:"Multi-agent concierge", p6xd:"A multi-agent assistant built in Dify that serves the hotel\u2019s guests and relies on Google Sheets as its operational data source.",
    p7xt:"Finance agent", p7xc:"Personal project", p7xd:"An n8n agent that logs personal expenses into Google Sheets and turns them into a live Looker Studio report.",
    expH:"Journey", expS:"(04) From the plant floor<br>to the AI model", now:"Current",
    e1:"AI data agents in Microsoft Fabric connected to live semantic models. Migrated an Excel report needing 16–20 h/month of manual prep to Power BI Service with 2-hour refresh and role-based Row-Level Security.", e1w:"2026 — present",
    e2:"Asset maintenance management with D365 F&amp;O, CRM Field Service and Power BI for the Tren Maya railway project.",
    e3:"D365 F&amp;O implementation in manufacturing: Procurement &amp; Sourcing, Warehouse Management and Sales.",
    e4:"Digital transformation success case recognized by Microsoft (BACO): from requirements to go-live, with the SCOR model and end-to-end WMS in D365 F&amp;O.",
    e5:"Power BI dashboards and report automation that reduced critical incidents by 30% through predictive analytics.",
    faqH:"Before<br>you ask", faqS:"(06) Frequently<br>asked questions",
    q1:"Do the portfolio dashboards use real data?", a1:"No. All data is sample data, generated for illustration. What stays faithful to the real projects is the design, the measure logic and the process — which is what actually demonstrates the work.",
    q2:"Do you take freelance projects or full-time only?", a2:"Both. I take BI and data consulting projects per deliverable, as well as long-term collaborations. The first step is always a short call to understand the need.",
    q3:"What does your work process look like?", a3:"Gather the requirement with the business team, design on paper, build on a solid architecture and validate against the stakeholder\u2019s figures before delivering.",
    q4:"Do you work in English?", a4:"Yes — documentation, meetings and deliverables in English or Spanish. This entire portfolio is available in both languages via the ES · EN toggle.",
    stkS:"(05) Tools I use<br>every day", stk3:"Automation", stk4:"ERP &amp; method",
    cK1:"(07) Got data that tells you nothing?", cK2:"I reply within 24 h", c1:"Let's", c2:"talk ↗",
    cP:"Tell me which process you want to measure, which dashboard nobody opens or which task you'd hand to an agent. Let\u2019s start with a call.",
    figcap:"Rod — 3D version, 2026", copy:"Copy", foot:"Made in Mexico City · with data and coffee", top:"Back to top ↑"
  };
  const ES={};
  $$('[data-i18n]').forEach(el=>{ const k=el.dataset.i18n; if(!(k in ES)) ES[k]=el.innerHTML; });
  const LOGS={es:["conectando lakehouse","cargando modelo semántico","despertando agentes","sirviendo café"],en:["connecting lakehouse","loading semantic model","waking up agents","pouring coffee"]};
  let lang='es';
  try{ const s=localStorage.getItem('rm-lang'); if(s==='en'||s==='es') lang=s; else if((navigator.language||'').slice(0,2)==='en') lang='en'; }catch(e){}
  function setLang(l){
    lang=l; const d=l==='en'?EN:ES; document.documentElement.lang=l;
    $$('[data-i18n]').forEach(el=>{ const v=d[el.dataset.i18n]; if(v!=null){ el.innerHTML=v; if(el.dataset.t!=null) el.dataset.t=el.textContent; } });
    $$('.lang button').forEach(b=>b.setAttribute('aria-pressed', b.dataset.lang===l));
    splitManifesto(); buildMarquee(); onScroll();
    try{localStorage.setItem('rm-lang',l)}catch(e){}
  }
  $$('.lang button').forEach(b=>b.addEventListener('click',()=>setLang(b.dataset.lang)));

  /* ---------- manifesto word split ---------- */
  function splitManifesto(){
    const m=$('#manifesto');
    const walk=(node)=>{
      [...node.childNodes].forEach(n=>{
        if(n.nodeType===3){
          const frag=document.createDocumentFragment();
          n.textContent.split(/(\s+)/).forEach(t=>{ if(!t) return; if(/^\s+$/.test(t)) frag.appendChild(document.createTextNode(t)); else { const s=document.createElement('span'); s.className='w'; s.textContent=t; frag.appendChild(s);} });
          n.replaceWith(frag);
        } else if(n.nodeType===1 && !n.classList.contains('w')) walk(n);
      });
    };
    walk(m);
  }

  /* ---------- marquee ---------- */
  function buildMarquee(){
    const words = lang==='en'
      ? ["Business Intelligence","Microsoft Fabric","Generative AI","Agentic systems","Power BI","Data engineering","RAG","Lean Six Sigma"]
      : ["Business Intelligence","Microsoft Fabric","IA generativa","Sistemas agénticos","Power BI","Ingeniería de datos","RAG","Lean Six Sigma"];
    const star='<svg width="26" height="26" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0l2.6 9.4L24 12l-9.4 2.6L12 24l-2.6-9.4L0 12l9.4-2.6z"/></svg>';
    const one=words.map(w=>`<span class="marquee__item">${w}${star}</span>`).join('');
    $('#marq').innerHTML=one+one;
  }

  /* ---------- preloader ---------- */
  function runLoader(){
    const countEl=$('#count'), bar=$('#bar'), log=$('#log');
    let seen=false; try{ seen=sessionStorage.getItem('rm-seen')==='1'; sessionStorage.setItem('rm-seen','1'); }catch(e){}
    const dur = reduce ? 300 : (seen ? 1100 : 3000), t0=performance.now();
    const ease=t=>t<.5?4*t*t*t:1-Math.pow(-2*t+2,3)/2;
    let shown=-1;
    const lines=LOGS[lang];
    function frame(now){
      const p=Math.min(1,(now-t0)/dur), v=Math.round(ease(p)*100);
      if(v!==shown){ countEl.textContent=v; bar.style.transform=`scaleX(${v/100})`; shown=v;
        const idx=Math.min(lines.length-1,Math.floor(v/ (100/lines.length)));
        const html=lines.slice(Math.max(0,idx-1),idx+1).map((l,i,a)=>`<span>${l}… ${i<a.length-1||v===100?'<b>ok</b>':''}</span>`).join('');
        if(log.dataset.i!==String(idx)+(v===100)){ log.innerHTML=html; log.dataset.i=String(idx)+(v===100); }
      }
      if(p<1) requestAnimationFrame(frame); else setTimeout(finish, reduce?0:380);
    }
    requestAnimationFrame(frame);
  }
  function finish(){
    body.classList.add('loaded'); body.classList.remove('is-loading');
    setTimeout(()=>{ const l=$('#loader'); if(l) l.remove(); }, 1600);
  }

  /* ---------- reveal on scroll ---------- */
  const io=new IntersectionObserver(es=>es.forEach(e=>{ if(e.isIntersecting){ e.target.classList.add('in'); io.unobserve(e.target);} }),{threshold:.15,rootMargin:'0px 0px -6% 0px'});
  $$('.reveal').forEach((el,i)=>{ io.observe(el); });
  $$('.projects .proj').forEach((el,i)=>el.style.transitionDelay=(i%2)*0.12+'s');
  $$('.exp__row').forEach((el,i)=>el.style.transitionDelay=i*0.05+'s');
  $$('.facts .fact').forEach((el,i)=>el.style.transitionDelay=i*0.08+'s');
  // horizontal progress bars in LMS svg
  $$('.hbar').forEach(b=>{ b.style.transformOrigin='left'; b.style.transform='scaleX(0)'; });
  const io2=new IntersectionObserver(es=>es.forEach(e=>{ if(e.isIntersecting){ $$('.hbar,.bar[style*="scaleX"]',e.target).forEach(b=>b.style.transform='scaleX(1)'); io2.unobserve(e.target);} }),{threshold:.3});
  $$('.proj').forEach(p=>io2.observe(p));

  /* ---------- stat counters ---------- */
  const io3=new IntersectionObserver(es=>es.forEach(e=>{ if(!e.isIntersecting) return; io3.unobserve(e.target);
    $$('[data-count]',e.target).forEach(el=>{ const to=+el.dataset.count, t0=performance.now(), d=reduce?0:1600;
      (function f(now){ const p=d?Math.min(1,(now-t0)/d):1; el.textContent=Math.round((1-Math.pow(1-p,3))*to); if(p<1) requestAnimationFrame(f); })(t0); });
  }),{threshold:.4});
  const st=$('#stats'); if(st) io3.observe(st);

  /* ---------- services accordion ---------- */
  $$('.svc__btn').forEach(btn=>btn.addEventListener('click',()=>{
    const it=btn.closest('.svc'), open=!it.classList.contains('open');
    $$('.svc').forEach(s=>{ s.classList.remove('open'); $('.svc__btn',s).setAttribute('aria-expanded','false'); });
    if(open){ it.classList.add('open'); btn.setAttribute('aria-expanded','true'); }
  }));

  /* ---------- scroll effects ---------- */
  const nav=$('#nav'), prog=$('#progress'), avatar=$('#avatar'), dark=$('.dark');
  let lastY=0, ticking=false;
  function onScroll(){
    const y=scrollY, h=document.documentElement.scrollHeight-innerHeight;
    prog.style.transform=`scaleX(${h>0?y/h:0})`;
    nav.classList.toggle('scrolled', y>40);
    if(!body.classList.contains('menu-open')) nav.classList.toggle('hidden', y>lastY && y>innerHeight*.8);
    const dr=dark.getBoundingClientRect(); nav.classList.toggle('dark', dr.top<60 && dr.bottom>60);
    lastY=y;
    if(!reduce && y<innerHeight*1.2){ avatar.style.transform=(innerWidth<=760?'translateX(50%) ':'')+`translateY(${y*.12}px) scale(${1-y*.00012})`; }
    // manifesto words
    const m=$('#manifesto'); if(m){ const r=m.getBoundingClientRect(); const ws=m.querySelectorAll('.w');
      const p=Math.min(1,Math.max(0,(innerHeight*.85-r.top)/(r.height+innerHeight*.35)));
      const n=Math.round(p*ws.length*1.05); ws.forEach((w,i)=>w.classList.toggle('on', i<n || reduce)); }
    ticking=false;
  }
  addEventListener('scroll',()=>{ if(!ticking){ requestAnimationFrame(onScroll); ticking=true; } },{passive:true});
  addEventListener('resize',onScroll);

  /* ---------- mobile menu ---------- */
  const burger=$('#burger');
  burger.addEventListener('click',()=>{ const o=body.classList.toggle('menu-open'); burger.setAttribute('aria-expanded',o); burger.setAttribute('aria-label', o?'Cerrar menú':'Abrir menú'); nav.classList.remove('hidden'); });
  $$('#mmenu a').forEach(a=>a.addEventListener('click',()=>{ body.classList.remove('menu-open'); burger.setAttribute('aria-expanded','false'); }));

  /* ---------- clock ---------- */
  function tick(){ try{ $('#clock').textContent=new Intl.DateTimeFormat('es-MX',{hour:'2-digit',minute:'2-digit',hour12:false,timeZone:'America/Mexico_City'}).format(new Date()); }catch(e){} }
  tick(); setInterval(tick,15000);

  /* ---------- copy email ---------- */
  const toast=$('#toast');
  /* mailto assembled at runtime (mitigates harvesting) */
  const MAIL = 'rdgo.mendoza' + '@' + 'gmail.com';
  $$('[data-em]').forEach(a=>a.setAttribute('href','mailto:'+MAIL));
  $$('[data-em-text]').forEach(el=>el.textContent=MAIL);
  $('#copy').addEventListener('click',async()=>{
    const mail=MAIL;
    try{ await navigator.clipboard.writeText(mail); toast.textContent= lang==='en'?'Email copied':'Correo copiado'; }
    catch(e){ location.href='mailto:'+mail; return; }
    toast.classList.add('show'); setTimeout(()=>toast.classList.remove('show'),1800);
  });

  /* ---------- cursor + magnetic ---------- */
  if(matchMedia('(hover:hover)').matches && !reduce){
    const c=$('#cursor'); let x=innerWidth/2,y=innerHeight/2,cx=x,cy=y;
    addEventListener('mousemove',e=>{ x=e.clientX; y=e.clientY; c.classList.add('on'); });
    document.addEventListener('mouseleave',()=>c.classList.remove('on'));
    (function loop(){ cx+=(x-cx)*.2; cy+=(y-cy)*.2; c.style.transform=`translate(${cx}px,${cy}px)`; requestAnimationFrame(loop); })();
    $$('.proj, .contact__big').forEach(el=>{ el.addEventListener('mouseenter',()=>c.classList.add('big')); el.addEventListener('mouseleave',()=>c.classList.remove('big')); });
    $$('.magnetic').forEach(el=>{
      el.addEventListener('mousemove',e=>{ const r=el.getBoundingClientRect(); el.style.transform=`translate(${(e.clientX-r.left-r.width/2)*.25}px,${(e.clientY-r.top-r.height/2)*.35}px)`; });
      el.addEventListener('mouseleave',()=>el.style.transform='');
    });
    // hero avatar parallax on mouse
    const inner=$('.hero__avatar-inner img');
    $('.hero').addEventListener('mousemove',e=>{ const dx=(e.clientX/innerWidth-.5), dy=(e.clientY/innerHeight-.5); inner.style.transform=`translate(${dx*-14}px,${dy*-8}px)`; });
  }

  /* ---------- init ---------- */
  if(lang!=='es') setLang(lang); else { splitManifesto(); buildMarquee(); }
  onScroll();
  scrollTo(0,0);
  runLoader();
})();
