/* ============================================================
   i18n · Motor de traducción ES ⇄ EN
   Rodrigo Mendoza Cortés — portafolio
   ------------------------------------------------------------
   Uso en cada página:
     1. <script src="assets/i18n.js"></script>   (o ../assets/i18n.js)
     2. <script>I18N.register({ "texto en español": "english text", ... })</script>
     3. I18N.init();
   El motor recorre los nodos de texto del DOM y los intercambia.
   Guarda la preferencia en memoria de sesión y respeta el idioma
   del navegador en la primera visita.
   ============================================================ */
(function (global) {
  var DICT = {};          // es -> en
  var REV = {};           // en -> es
  var lang = 'es';
  var nodes = [];         // {node, es, en}
  var attrNodes = [];     // {el, attr, es, en}
  var ready = false;

  function register(map) {
    for (var k in map) {
      DICT[k] = map[k];
      REV[map[k]] = k;
    }
  }

  /* recolecta nodos de texto traducibles */
  function collect() {
    nodes = [];
    var walker = document.createTreeWalker(
      document.body, NodeFilter.SHOW_TEXT,
      {
        acceptNode: function (n) {
          var p = n.parentNode;
          if (!p) return NodeFilter.FILTER_REJECT;
          var tag = p.nodeName;
          if (tag === 'SCRIPT' || tag === 'STYLE') return NodeFilter.FILTER_REJECT;
          if (p.closest && p.closest('[data-no-i18n]')) return NodeFilter.FILTER_REJECT;
          var t = n.nodeValue.trim();
          if (!t) return NodeFilter.FILTER_REJECT;
          return DICT[t] ? NodeFilter.FILTER_ACCEPT : NodeFilter.FILTER_REJECT;
        }
      }
    );
    var n;
    while ((n = walker.nextNode())) {
      var raw = n.nodeValue, t = raw.trim();
      var i = raw.indexOf(t);
      nodes.push({
        node: n,
        pre: raw.slice(0, i),
        post: raw.slice(i + t.length),
        es: t,
        en: DICT[t]
      });
    }
    /* atributos traducibles: title, aria-label, alt, placeholder */
    attrNodes = [];
    ['title', 'aria-label', 'alt', 'placeholder'].forEach(function (attr) {
      document.querySelectorAll('[' + attr + ']').forEach(function (el) {
        var v = el.getAttribute(attr).trim();
        if (DICT[v]) attrNodes.push({ el: el, attr: attr, es: v, en: DICT[v] });
      });
    });
  }

  function apply(to, silent) {
    nodes.forEach(function (r) {
      r.node.nodeValue = r.pre + (to === 'en' ? r.en : r.es) + r.post;
    });
    attrNodes.forEach(function (r) {
      r.el.setAttribute(r.attr, to === 'en' ? r.en : r.es);
    });
    document.documentElement.lang = to;
    lang = to;
    syncButtons();
    /* aviso para que los gráficos u otros módulos se redibujen */
    if (!silent) document.dispatchEvent(new CustomEvent('languagechange', { detail: { lang: to } }));
  }

  function syncButtons() {
    document.querySelectorAll('.lang-toggle').forEach(function (btn) {
      btn.setAttribute('aria-label',
        lang === 'es' ? 'Switch to English' : 'Cambiar a español');
      btn.querySelectorAll('[data-lang]').forEach(function (s) {
        s.classList.toggle('on', s.dataset.lang === lang);
      });
    });
  }

  function set(to) {
    if (to === lang) return;
    if (!ready) return;
    apply(to);
    try { sessionStorage.setItem('rmc-lang', to); } catch (e) {}
  }

  function toggle() { set(lang === 'es' ? 'en' : 'es'); }

  /* re-escanea después de que el JS de la página inyecte contenido nuevo */
  function refresh() {
    var current = lang;
    if (current === 'en') apply('es', true);   // vuelve a base antes de recolectar
    collect();
    if (current === 'en') apply('en', true);   // silencioso: evita recursión
  }

  function buildToggle() {
    var host = document.querySelector('[data-lang-toggle-here]');
    var btn = document.createElement('button');
    btn.className = 'lang-toggle';
    btn.type = 'button';
    btn.innerHTML = '<span data-lang="es" class="on">ES</span>' +
                    '<span class="lang-sep">·</span>' +
                    '<span data-lang="en">EN</span>';
    btn.addEventListener('click', toggle);
    if (host) host.appendChild(btn); else document.body.appendChild(btn);
    return btn;
  }

  function init(opts) {
    opts = opts || {};
    buildToggle();
    collect();
    ready = true;
    var saved = null;
    try { saved = sessionStorage.getItem('rmc-lang'); } catch (e) {}
    var start = saved ||
      ((navigator.language || 'es').toLowerCase().indexOf('es') === 0 ? 'es' : 'en');
    if (start === 'en') apply('en'); else syncButtons();
  }

  global.I18N = {
    register: register,
    init: init,
    set: set,
    toggle: toggle,
    refresh: refresh,
    get lang() { return lang; },
    /* helper para textos generados por JS (gráficas, tarjetas) */
    t: function (es) { return lang === 'en' ? (DICT[es] || es) : es; }
  };
})(window);
