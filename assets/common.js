// Shared behaviour for the homepage concepts: mobile menu, scroll reveals, concept switcher.
(function () {
  document.documentElement.classList.add('js');
  var toggle = document.querySelector('[data-menu-toggle]');
  var nav = document.querySelector('[data-nav]');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    nav.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () { nav.classList.remove('open'); });
    });
  }

  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var items = document.querySelectorAll('[data-reveal]');
  if (!reduce && 'IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
      });
    }, { threshold: 0.15 });
    items.forEach(function (el) { io.observe(el); });
  } else {
    items.forEach(function (el) { el.classList.add('in'); });
  }

  // Review-only switcher between concepts.
  var concepts = [
    ['/', 'All'],
    ['/concept-1/', '1 · Split'],
    ['/concept-2/', '2 · Spotlight'],
    ['/concept-3/', '3 · Editorial'],
    ['/concept-4/', '4 · Unlock']
  ];
  var bar = document.createElement('nav');
  bar.className = 'concept-switcher';
  bar.setAttribute('aria-label', 'Homepage concepts');
  var path = location.pathname.replace(/index\.html$/, '');
  bar.innerHTML = '<span>Concepts</span>' + concepts.map(function (c) {
    return '<a href="' + c[0] + '"' + (path === c[0] ? ' class="on"' : '') + '>' + c[1] + '</a>';
  }).join('');
  document.body.appendChild(bar);
  var css = document.createElement('style');
  css.textContent = '.concept-switcher{position:fixed;left:50%;bottom:14px;transform:translateX(-50%);z-index:999;display:flex;gap:4px;align-items:center;background:rgba(10,10,10,.92);color:#fff;padding:6px 6px 6px 14px;border-radius:999px;font:500 13px/1 system-ui,sans-serif;box-shadow:0 10px 30px rgba(0,0,0,.35);max-width:calc(100% - 20px);overflow-x:auto;white-space:nowrap}' +
    '.concept-switcher span{opacity:.6;margin-right:6px}.concept-switcher a{color:#fff;text-decoration:none;padding:8px 12px;border-radius:999px}.concept-switcher a.on{background:#fff;color:#000;font-weight:700}' +
    'body>footer{padding-bottom:110px!important}';
  document.head.appendChild(css);
})();
