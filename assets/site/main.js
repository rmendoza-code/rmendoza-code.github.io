(function(){
  const $=(s,c=document)=>c.querySelector(s), $$=(s,c=document)=>[...c.querySelectorAll(s)];
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const body=document.body;

  /* ---------- i18n ---------- */
  const EN={
    loading:"Loading portfolio", nav1:"Profile", nav2:"Services", nav3:"Data &amp; BI", nav6:"Evidence", nav7:"Diploma", nav4:"Experience", nav5:"FAQ", skip:"Skip to content", cv:"Download CV ↓", cvL:"Résumé (PDF)", explore:"Explore dashboard", cta:"Let's talk",
    role:"Agentic AI &amp; Data Engineer", lead:"I build <em>AI agents</em> that work on real business data — with tools, memory and human controls.", heroLab:"See the AI Lab →",
    based:"Mexico City", avail:"Available · 2026", scroll:"Scroll", aboutLabel:"(01) Profile",
    manifesto:"Industrial engineer with 5+ years taking ERP data to decisions. Today I design <span class=\"hl\">AI agents</span> on top of that same data: with RAG, tools, MCP and a human in the loop when the decision calls for it. I understand the process before the model — that’s why my agents don’t break it.",
    f2l:"Education", f2s:"Industrial Eng.", f3l:"Certification", f4l:"Specialization", f4s:"AI Technologies", f4p:"Tec de Monterrey — LLMs, RAG, multi-agent, MCP", f5l:"Languages", f5s:"ES · EN B2", f5p:"Italian · Portuguese",
    st1:"years bridging supply chain and data", st2:"fewer critical incidents through predictive analytics", st3:"of manual reporting eliminated per month", st4:"DAX measures delivered in training",
    svcH:"What I<br>build", svcS:"(02) Three fronts,<br>one source of truth",
    s1t:"AI agents", s1:"Agents that reason, use tools and integrate with business systems: intent routing, tool calling, memory, MCP servers and human approval on sensitive steps.",
    s2t:"RAG &amp; generative AI", s2:"Assistants that answer with the organization’s own information and don’t make things up: chunking, embeddings, vector databases, grounded prompts and answers that cite their source.",
    s3t:"Data &amp; BI", s3:"The foundation that makes an agent trustworthy: Microsoft Fabric lakehouses, semantic models, DAX and Power BI dashboards leadership actually uses.",
    workH:"Data<br>&amp; BI", workS:"(06) Dashboards · Fabric<br>Power Platform", workNote:"Each card opens its case: HTML recreations of dashboards built in Power BI and Fabric, with the same measure logic and anonymized sample data.", caseCta:"See case and demo",
    p1t:"Procurement Analytics — PR to PO", p1d:"Procurement cycle tracking on a Bronze/Silver/Gold architecture sourced from D365 F&amp;O. Cycle time triangulated against stakeholder data.",
    p2c:"Finance · Budget", p2d:"Financial execution report with an embedded comment-capture page via Microsoft Forms → Power Automate → SharePoint, rendered with HTML Viewer.",
    p3t:"RAMS — Railway maintenance", p3d:"MTBF, MTTR and asset availability metrics for railway operations, with Dataverse to SQL Server pipelines and near real-time fleet monitoring.",
    p4xt:"Unified cloud billing", p4xd:"Automation that consolidates the monthly cloud-consumption reports stored in SharePoint, plus an executive dashboard showing trend and cost per service.",
    p5xt:"Training App", p5xd:"Training app (LMS) built on Microsoft Fabric and Power BI to upskill teams on the organization\u2019s data stack.",
    p6xt:"Multi-agent concierge", p6xd:"A multi-agent assistant built in Dify that serves the hotel\u2019s guests and relies on Google Sheets as its operational data source.",
    p7xt:"Finance agent", p7xc:"Personal project", p7xd:"An n8n agent that logs personal expenses into Google Sheets and turns them into a live Looker Studio report.",
    expH:"Journey", expS:"(07) From the plant floor<br>to the AI agent", now:"Current",
    e1:"AI data agents in Microsoft Fabric connected to live semantic models. Migrated an Excel report needing 16–20 h/month of manual prep to Power BI Service with 2-hour refresh and role-based Row-Level Security.", e1w:"2026 — present",
    e2:"Asset maintenance management with D365 F&amp;O, CRM Field Service and Power BI for the Tren Maya railway project.",
    e3:"D365 F&amp;O implementation in manufacturing: Procurement &amp; Sourcing, Warehouse Management and Sales.",
    e4:"Digital transformation success case recognized by Microsoft (BACO): from requirements to go-live, with the SCOR model and end-to-end WMS in D365 F&amp;O.",
    e5:"Power BI dashboards and report automation that reduced critical incidents by 30% through predictive analytics.",
    faqH:"Before<br>you ask", faqS:"(09) Frequently<br>asked questions",
    q5:"Do you have AI agents in production?", a5:"Yes. At CIMMYT I built data agents in Microsoft Fabric that answer business questions over live semantic models. My other agents (hotel, internal assistant with MCP, voice agent) run on Dify, n8n and Make; the code version with LangGraph is under construction and documented in the AI Lab.",
    q6:"Can I see the code?", a6:"Yes. Every agent and flow export, with credentials removed, lives in the <code>lab/</code> folder of this site’s GitHub repository, each with an architecture README.",
    labS:"(03) Agents · RAG · MCP<br>with open code", labIntro:"Each window is a real project. Conversations are recreations with fictitious data; the architecture, prompts and flows are the ones I built — and the exported code is on GitHub.",
    tDemo:"Demo", tArch:"Architecture", tLive:"Live", liveP:"This is the real agent, deployed on Dify. It only loads when you ask for it.", liveB:"Load live agent", liveA:"or open it in a new tab ↗", tGraph:"Graph", tRoad:"Progress", tFlow:"Flow", tMcp:"MCP server", tPipe:"Pipeline", tPrompt:"Prompt", tAsk:"Question", tDax:"DAX", tAll:"Flows", tConv:"Convergence", tRoute:"Best route", tTab:"Results",
    chatOnline:"assistant · online", replay:"↻ Replay", fictNote:"Recreation · fictitious data", sampleNote:"Recreation · sample data",
    h1:"Hi, do you have a double room from November 14 to 16?", h2:"Classifier: availability", h3:"Of course! For those dates the Double Patio Room is available, 2 nights. Shall I share the rate and what’s included?", h4:"Yes. And I need an invoice for my previous stay.", h5:"Classifier: invoicing", h6:"Gladly. For your CFDI invoice I need your RFC tax ID, legal name, tax regime, postal code and CFDI use. Could you share your RFC first?",
    keyL:"Key decision", findL:"Finding", lkCode:"View code", lkDemo:"Try the demo", lkCase:"Case study", lkReport:"PDF report", wip:"In progress", prodTag:"In production", dipTag:"Tec diploma",
    l1t:"Multi-agent hotel concierge", l1d:"Guest assistant for a boutique hotel in Mérida. A classifier routes each message to one of three agents (reservations, CFDI invoicing, availability) with function calling, memory and tools: the hotel’s official source, Google Sheets, Tavily and Wikipedia.", l1k:"One agent per intent instead of one giant prompt: each with its own persona, rules and only the tools it needs.",
    l2t:"From prototype to production, in code", l2d:"Porting the concierge to Python + LangGraph to cover what low-code can’t: RAG over a vector database, input and output guardrails, structured validation of tax data, human approval with interrupt() and reproducible evaluation.", l2k:"Prototype fast in Dify to validate the design with users; move to code when you need controls, tests and deployment.",
    r1:"Design validated in a prototype (Dify)", r2:"LangGraph graph with typed state and memory", r3:"RAG: embeddings + vector DB with hotel policies", r4:"Guardrails: off-topic, personal data, RFC validation", r5:"Human-in-the-loop: approval before issuing an invoice", r6:"Evaluation with test cases and traces", r7:"Deployment with public demo and REST API",
    l3t:"Internal assistant with its own MCP server", l3d:"Internal requests come in through a webhook, get classified and a Switch routes them to Slack, Notion, Gmail or Sheets. When a meeting is needed, an agent (OpenAI or Claude) uses an MCP client connected to my own MCP server with calendar, email and search tools.", l3k:"Deterministic rules where they suffice (Switch) and an LLM only where it adds value; plus a global error workflow that alerts in Slack.",
    m1:"Current date and time to reason about schedules", m2:"Google Calendar: books the meeting with a descriptive title", m3:"Web search via HTTP Request", m4:"Gmail: confirms with the user", m5:"Any MCP client (the n8n agent, Claude or others) discovers and uses these tools.",
    p1:"Federal Civil Code (Justia)", p4:"vector store · similarity · top-4", p5:"context + question",
    l4t:"LexMex: legal chatbot with RAG", l4d:"Diploma case: a law firm loses hours searching scattered regulations. End-to-end RAG pipeline: loading the Federal Civil Code, chunking, embeddings, an AstraDB vector store and an LLM answering only from the retrieved context.", l4k:"Temperature 0.1 and an explicit instruction to answer “I don’t know” when the context falls short: a first guardrail against hallucinations.",
    q_f1:"What was the average PR-to-PO cycle by category this quarter?", q_f2:"certified semantic model · existing measures", c1n:"Services", c2n:"Laboratory", c3n:"IT", c4n:"Field",
    l5t:"Data agents over semantic models", l5d:"At CIMMYT I built AI data agents in Microsoft Fabric connected to live semantic models: users ask in natural language and the agent answers by querying certified measures, not with invented figures.", l5k:"Governed answers: the agent only queries the semantic model and its measures, so the number matches the official dashboard.",
    a1t:"Voice agent", a1s:"books or proposes an alternative", a2t:"Invoices → data", a2s:"structured extraction", a3t:"Automatic meeting minutes", a3s:"summary and title", a4t:"Voice notes", a4s:"replies with audio",
    l6t:"LLMs inside business processes", l6d:"Automations where the LLM is one more step of the process: a voice agent that books appointments, invoice extraction to JSON, meeting minutes and a Telegram assistant that understands voice notes.",
    mxH:"Capabilities<br>→ evidence", mxS:"(04) What an Agentic<br>AI Engineer needs",
    x1:"Design, development and deployment of AI agents", x2:"LLMs, RAG, embeddings and vector databases", x3:"Agentic architectures and tool calling", x4:"Integrations: REST APIs, webhooks, enterprise systems", x5:"Prompts, memory, tools and decision logic", x6:"AI in production environments", x7:"Technical and business stakeholders", x8:"Python", x9:"Guardrails and human-in-the-loop", x10:"Plus: LangChain/LangGraph · MCP · Power Automate · Power Platform",
    stOk:"Proven", stWip:"In progress", lgOk:"with linked evidence", lgWip:"partial evidence, in progress",
    dpH:"Tec de Monterrey<br>diploma", dpS:"(05) Specialization in<br>AI Technologies", done:"Completed", doing:"In progress",
    md1:"Fundamentals of generative AI", md2:"Prompt engineering and LLM agents (low-code)", md2l:"Deliverable: LexMex RAG →", md3:"Automated reasoning", md3l:"Formal logic · Prolog", md4:"Fundamentals of metaheuristics", md4l:"Deliverable: TSP in Python →", md5:"Data preprocessing", md6:"Unsupervised learning",
    thT:"Technique", thB:"Best", thA:"Average", thS:"Std.", thTm:"Time", tr1:"Simulated annealing", tr2:"Genetic algorithm", tbN:"5 runs per technique · instance optimum ≈ 32.22",
    tspT:"Delivery routes with metaheuristics", tspD:"A 15-stop TSP solved with three families: simulated annealing, a genetic algorithm (OX + inversion + elitism) and hill-climbing with 2-opt. All three reach the optimum; the genetic algorithm is the most consistent and hill-climbing the fastest.", tspK:"The brief allowed “gradient”, but there is no differentiable function over permutations: I documented it and justified hill-climbing.",
    q1:"Do the portfolio dashboards use real data?", a1:"No. All data is sample data, generated for illustration. What stays faithful to the real projects is the design, the measure logic and the process — which is what actually demonstrates the work.",
    q2:"Do you take freelance projects or full-time only?", a2:"Both. I take BI and data consulting projects per deliverable, as well as long-term collaborations. The first step is always a short call to understand the need.",
    q3:"What does your work process look like?", a3:"Gather the requirement with the business team, design on paper, build on a solid architecture and validate against the stakeholder\u2019s figures before delivering.",
    q4:"Do you work in English?", a4:"Yes — documentation, meetings and deliverables in English or Spanish. This entire portfolio is available in both languages via the ES · EN toggle.",
    stkS:"(08) Tools I use<br>every day", stk3:"Orchestration", stk4:"ERP &amp; method",
    cK1:"(10) Got a process that deserves an agent?", cK2:"I reply within 24 h", c1:"Let's", c2:"talk ↗",
    cP:"I’m looking to join a team taking AI agents into real processes. If your project needs someone who understands the process, the data and the agent, let’s talk.",
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
      ? ["Agentic AI","LangGraph","RAG","Model Context Protocol","Tool calling","Human-in-the-loop","Microsoft Fabric","Power Platform"]
      : ["IA agéntica","LangGraph","RAG","Model Context Protocol","Tool calling","Human-in-the-loop","Microsoft Fabric","Power Platform"];
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

  /* ---------- AI Lab: window tabs ---------- */
  $$('.win').forEach(win=>{
    const tabs=$$('.win__tabs button',win), panels=$$('.win__panel',win);
    tabs.forEach(t=>t.addEventListener('click',()=>{
      tabs.forEach(b=>b.setAttribute('aria-selected',b===t));
      panels.forEach(p=>p.hidden = p.dataset.panel!==t.dataset.view);
    }));
  });

  /* ---------- AI Lab: scripted chat (recreation) ---------- */
  function playChat(chat){
    const steps=$$('[data-step]',chat), log=$('.chat__log',chat);
    chat._run=(chat._run||0)+1; const run=chat._run;
    if(reduce){ steps.forEach(s=>s.classList.add('on')); return; }
    chat.setAttribute('data-playing',''); steps.forEach(s=>s.classList.remove('on'));
    let i=0;
    (function next(){
      if(run!==chat._run || i>=steps.length) return;
      const st=steps[i], isBot=st.classList.contains('msg--a');
      const show=()=>{ const t=$('.typing',log); if(t) t.remove(); st.classList.add('on'); log.scrollTop=log.scrollHeight; i++; setTimeout(next, isBot?1100:650); };
      if(isBot){ const t=document.createElement('div'); t.className='typing'; t.innerHTML='<i></i><i></i><i></i>'; log.appendChild(t); log.scrollTop=log.scrollHeight; setTimeout(show,900); }
      else show();
    })();
  }
  const ioChat=new IntersectionObserver(es=>es.forEach(e=>{ if(e.isIntersecting){ playChat(e.target); ioChat.unobserve(e.target);} }),{threshold:.45});
  $$('[data-chat]').forEach(c=>{ ioChat.observe(c); const r=$('[data-replay]',c); if(r) r.addEventListener('click',()=>playChat(c)); });

  /* ---------- AI Lab: live demo links (fill in when public) ---------- */
  const DEMOS={ 'lab-hotel':'https://udify.app/chat/reiilNdcCMbuMkX2' };
  $$('[data-live-load]').forEach(btn=>btn.addEventListener('click',()=>{
    const box=btn.closest('[data-live]'); const f=document.createElement('iframe');
    f.src=box.dataset.live; f.title='Agente Hotel Casa Mérida (Dify)'; f.allow='microphone'; f.loading='lazy';
    box.innerHTML=''; box.classList.add('live--on'); box.appendChild(f);
  }));
  Object.entries(DEMOS).forEach(([id,url])=>{ if(!url) return; const a=$('#'+id+' [data-demo]'); if(a){ a.href=url; a.hidden=false; } });

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
