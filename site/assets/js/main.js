/* UAIFS v3 — site behaviour. No dependencies. */
(function () {
  var doc = document;
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- Single-file walkthrough router (bundle only) ---------- */
  var pages = doc.querySelectorAll('[data-page]');
  function route() {
    if (!pages.length) return;
    var h = (location.hash || '#index').slice(1);
    var parts = h.split('--');
    var page = parts[0] || 'index', anchor = parts[1];
    var found = doc.querySelector('[data-page="' + page + '"]');
    if (!found) { page = 'index'; found = doc.querySelector('[data-page="index"]'); anchor = h; }
    pages.forEach(function (p) { p.hidden = p !== found; });
    doc.querySelectorAll('.nav a, .dd').forEach(function (a) { a.classList.remove('is-active'); });
    doc.querySelectorAll('[data-nav="' + (found.getAttribute('data-section') || page) + '"]').forEach(function (a) { a.classList.add('is-active'); });
    var t = found.getAttribute('data-title'); if (t) doc.title = t;
    closeMenus();
    var target = anchor ? doc.getElementById(anchor) : null;
    if (target && !found.contains(target)) target = null;
    requestAnimationFrame(function () {
      if (target) target.scrollIntoView({ behavior: 'instant', block: 'start' });
      else window.scrollTo({ top: 0, left: 0, behavior: 'instant' });
      initInView();
    });
  }
  if (pages.length) { window.addEventListener('hashchange', route); }

  /* ---------- Nav: dropdowns + mobile ---------- */
  var toggle = doc.querySelector('.nav-toggle');
  var nav = doc.querySelector('.nav');
  function closeMenus(except) {
    doc.querySelectorAll('.dd.is-open').forEach(function (d) {
      if (d !== except) { d.classList.remove('is-open'); var b = d.querySelector('button'); if (b) b.setAttribute('aria-expanded', 'false'); }
    });
    if (!except && nav && nav.classList.contains('is-open')) {
      nav.classList.remove('is-open'); if (toggle) toggle.setAttribute('aria-expanded', 'false');
    }
  }
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('is-open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }
  doc.querySelectorAll('.dd').forEach(function (dd) {
    var btn = dd.querySelector('button');
    btn.addEventListener('click', function (e) {
      e.stopPropagation();
      var open = !dd.classList.contains('is-open');
      closeMenus(dd);
      dd.classList.toggle('is-open', open);
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    var fine = window.matchMedia && window.matchMedia('(hover: hover) and (min-width: 1021px)');
    dd.addEventListener('mouseenter', function () { if (fine && fine.matches) { closeMenus(dd); dd.classList.add('is-open'); btn.setAttribute('aria-expanded', 'true'); } });
    dd.addEventListener('mouseleave', function () { if (fine && fine.matches) { dd.classList.remove('is-open'); btn.setAttribute('aria-expanded', 'false'); } });
  });
  doc.addEventListener('click', function (e) { if (!e.target.closest('.dd')) doc.querySelectorAll('.dd.is-open').forEach(function (d) { d.classList.remove('is-open'); }); });
  doc.addEventListener('keydown', function (e) { if (e.key === 'Escape') closeMenus(); });
  if (nav) nav.addEventListener('click', function (e) { if (e.target.closest('a')) closeMenus(); });

  var header = doc.querySelector('.site-header');
  if (header) {
    var onScroll = function () { header.classList.toggle('is-scrolled', window.scrollY > 8); };
    onScroll(); window.addEventListener('scroll', onScroll, { passive: true });
  }

  /* ---------- Countdown to 20 Nov 2026, 9.00am GMT+8 ---------- */
  var target = Date.UTC(2026, 10, 20, 1, 0, 0);
  function tick() {
    var diff = Math.max(0, target - Date.now());
    var d = Math.floor(diff / 864e5), h = Math.floor(diff / 36e5) % 24, m = Math.floor(diff / 6e4) % 60;
    doc.querySelectorAll('[data-countdown]').forEach(function (el) {
      el.innerHTML = '<div><b>' + d + '</b><small>days</small></div><div><b>' + ('0' + h).slice(-2) + '</b><small>hours</small></div><div><b>' + ('0' + m).slice(-2) + '</b><small>mins</small></div>';
    });
  }
  tick(); setInterval(tick, 30000);

  /* ---------- Key numbers: count up once + draw the trail ---------- */
  function fmt(n, dec) { var s = n.toFixed(dec); var p = s.split('.'); p[0] = p[0].replace(/\B(?=(\d{3})+(?!\d))/g, ','); return p.join('.'); }
  function runCount(el) {
    if (el.dataset.done) return; el.dataset.done = '1';
    var to = parseFloat(el.dataset.to), dec = parseInt(el.dataset.dec || '0', 10);
    var pre = el.dataset.pre || '', suf = el.dataset.suf || '';
    if (reduce) { el.textContent = pre + fmt(to, dec) + suf; return; }
    var t0 = null, dur = 1600;
    function step(t) {
      if (!t0) t0 = t; var k = Math.min(1, (t - t0) / dur); var e = 1 - Math.pow(1 - k, 3);
      el.textContent = pre + fmt(to * e, dec) + suf;
      if (k < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }
  function drawTrail(svg) {
    if (svg.dataset.done) return; svg.dataset.done = '1';
    svg.querySelectorAll('path').forEach(function (p) {
      var L = p.getTotalLength(); p.style.strokeDasharray = L; p.style.strokeDashoffset = reduce ? 0 : L;
      if (!reduce) { p.getBoundingClientRect(); p.style.transition = 'stroke-dashoffset 2.2s cubic-bezier(.3,.7,.2,1)'; p.style.strokeDashoffset = 0; }
    });
  }
  var io = ('IntersectionObserver' in window) ? new IntersectionObserver(function (entries) {
    entries.forEach(function (en) {
      if (!en.isIntersecting) return;
      var el = en.target;
      if (el.matches('[data-to]')) runCount(el); else drawTrail(el);
      io.unobserve(el);
    });
  }, { threshold: 0.35 }) : null;
  function initInView() {
    doc.querySelectorAll('[data-to]:not([data-done]), .numbers__trail:not([data-done])').forEach(function (el) {
      if (el.offsetParent === null && !el.closest('svg')) return;
      if (io) io.observe(el); else if (el.matches('[data-to]')) runCount(el); else drawTrail(el);
    });
  }

  /* ---------- Edition tabs (agenda / speakers / partners) ---------- */
  doc.querySelectorAll('.ed-tabs').forEach(function (tabs) {
    var group = tabs.getAttribute('data-group');
    tabs.querySelectorAll('button').forEach(function (b) {
      b.addEventListener('click', function () {
        tabs.querySelectorAll('button').forEach(function (x) { x.setAttribute('aria-selected', x === b ? 'true' : 'false'); });
        doc.querySelectorAll('[data-ed-panel][data-group="' + group + '"]').forEach(function (p) { p.hidden = p.getAttribute('data-ed-panel') !== b.getAttribute('data-ed'); });
      });
    });
  });

  /* ---------- Resource hub filters ---------- */
  doc.querySelectorAll('.filters').forEach(function (f) {
    var feed = doc.getElementById(f.getAttribute('data-feed'));
    if (!feed) return;
    f.querySelectorAll('button').forEach(function (b) {
      b.addEventListener('click', function () {
        f.querySelectorAll('button').forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
        var key = b.getAttribute('data-k'), val = b.getAttribute('data-v');
        feed.querySelectorAll('.post, .rcard').forEach(function (p) { p.hidden = !(val === 'all' || p.getAttribute('data-' + key) === val); });
        var empty = feed.querySelector('.feed-empty');
        if (empty) empty.hidden = !!feed.querySelector('.post:not([hidden]), .rcard:not([hidden])');
        track('filter_use', { filter: key, value: val });
      });
    });
  });


  /* ---------- v4.1: analytics (GA4 via GTM dataLayer) ---------- */
  window.dataLayer = window.dataLayer || [];
  function pageId() { var m = doc.querySelector('[data-page]:not([hidden])'); return m ? m.getAttribute('data-page') : (doc.body.getAttribute('data-page-id') || ''); }
  function track(ev, params) {
    var o = { event: 'uaifs_' + ev, page_id: pageId() };
    for (var k in (params || {})) o[k] = params[k];
    window.dataLayer.push(o);
  }
  window.uaifsTrack = track;
  doc.addEventListener('click', function (e) {
    var a = e.target.closest('a, button');
    if (!a) return;
    var sec = a.closest('section, header, footer, nav');
    var where = sec ? (sec.id || sec.getAttribute('aria-label') || sec.className.split(' ')[0]) : '';
    var label = (a.textContent || a.getAttribute('aria-label') || '').trim().replace(/\s+/g, ' ').slice(0, 80);
    if (a.dataset.track) track('cta_click', { cta_id: a.dataset.track, cta_text: label, section: where });
    else if (a.classList.contains('btn') || a.classList.contains('link')) track('cta_click', { cta_id: 'auto', cta_text: label, section: where });
    if (a.tagName === 'A' && a.hostname && a.hostname !== location.hostname && /^https?:/.test(a.href)) track('outbound_click', { url: a.href, link_text: label, section: where });
    if (a.getAttribute('role') === 'tab') track('edition_tab', { edition: a.dataset.ed });
  });

  /* ---------- UTM capture: kept for the session, copied into every form ---------- */
  (function () {
    var q = new URLSearchParams(location.search), keys = ['utm_source', 'utm_medium', 'utm_campaign', 'utm_content'];
    try { keys.forEach(function (k) { if (q.get(k)) sessionStorage.setItem(k, q.get(k)); }); } catch (e) {}
    doc.querySelectorAll('input[data-utm]').forEach(function (i) { try { i.value = sessionStorage.getItem(i.dataset.utm) || ''; } catch (e) {} });
  })();

  /* ---------- Partners: find your tier ---------- */
  doc.querySelectorAll('.fit').forEach(function (fit) {
    var out = fit.parentNode.querySelector('.fit__out');
    fit.querySelectorAll('button').forEach(function (b) {
      b.addEventListener('click', function () {
        fit.querySelectorAll('button').forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
        var id = b.dataset.fit;
        doc.querySelectorAll('[data-tier-card]').forEach(function (c) { c.classList.toggle('is-rec', c.dataset.tierCard === id); });
        var card = doc.querySelector('[data-page]:not([hidden]) [data-tier-card="' + id + '"]') || doc.querySelector('[data-tier-card="' + id + '"]');
        if (card && out) {
          var name = card.querySelector('h3').textContent;
          out.innerHTML = 'Best fit: <strong>' + name + '</strong>. <a href="#" data-goto="' + card.id + '">See what it includes</a>';
        }
        track('fit_select', { goal: b.textContent.trim(), tier: id });
      });
    });
    if (out) out.addEventListener('click', function (e) {
      var g = e.target.closest('[data-goto]'); if (!g) return; e.preventDefault();
      var t = doc.getElementById(g.dataset.goto); if (t) t.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth', block: 'start' });
    });
  });

  /* ---------- Tier links pre-select the enquiry form ----------
     Works with the site's own <select data-tier-select> and, best effort, with the HubSpot
     enquiry form: if HubSpot renders inline and has a dropdown whose name or options mention
     the tier, it is set. Not possible if HubSpot renders the form in an iframe. */
  function setNative(el, v) {
    var proto = el.tagName === 'SELECT' ? HTMLSelectElement.prototype : HTMLInputElement.prototype;
    var d = Object.getOwnPropertyDescriptor(proto, 'value'); if (d && d.set) d.set.call(el, v); else el.value = v;
    el.dispatchEvent(new Event('input', { bubbles: true })); el.dispatchEvent(new Event('change', { bubbles: true }));
  }
  function applyTier(box) {
    var id = ''; try { id = sessionStorage.getItem('uaifs_tier') || ''; } catch (e) {}
    if (!id) return;
    (box || doc).querySelectorAll('[data-hs-form="partner_enquiry"] select').forEach(function (sel) {
      var named = /tier|partner/i.test(sel.name || '');
      var opt = Array.prototype.find.call(sel.options, function (o) { return (o.text + ' ' + o.value).toLowerCase().indexOf(id) > -1; });
      if (opt && (named || sel.options.length < 15)) setNative(sel, opt.value);
    });
  }
  window.uaifsHsReady = function (name, box) { if (name === 'partner_enquiry') applyTier(box); };
  doc.addEventListener('click', function (e) {
    var a = e.target.closest('[data-tier]'); if (!a) return;
    var id = a.dataset.tier;
    try { sessionStorage.setItem('uaifs_tier', id); } catch (err) {}
    setTimeout(function () {
      doc.querySelectorAll('[data-tier-select]').forEach(function (s) { if (s.querySelector('option[value="' + id + '"]')) s.value = id; });
      applyTier();
    }, 60);
  });

  /* ---------- Demo forms ---------- */
  doc.querySelectorAll('form[data-demo]').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var note = form.querySelector('.form-note');
      track('form_submit', { form: form.dataset.form || 'form' });
      if (note) { note.hidden = false; note.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth', block: 'center' }); }
      form.reset();
    });
  });

  /* ---------- Speaker photos: fall back to monogram if blocked ---------- */
  doc.querySelectorAll('img[data-photo]').forEach(function (img) {
    function fail() { img.remove(); }
    if (img.complete && img.naturalWidth === 0) fail(); else img.addEventListener('error', fail);
  });


  /* ---------- v4: event video — frame widens as it scrolls in; play/placeholder ---------- */
  function vidScroll() {
    doc.querySelectorAll('.vid').forEach(function (v) {
      if (v.offsetParent === null) return;
      var r = v.getBoundingClientRect(), vh = window.innerHeight;
      var p = reduce ? 1 : Math.min(1, Math.max(0, (vh - r.top) / (vh * 0.95) - 0.15) / 0.75);
      v.querySelector('.vid__frame').style.setProperty('--p', p.toFixed(3));
    });
  }
  window.addEventListener('scroll', vidScroll, { passive: true });
  window.addEventListener('resize', vidScroll);
  window.addEventListener('hashchange', function () { setTimeout(vidScroll, 50); });
  vidScroll();
  doc.querySelectorAll('.vid').forEach(function (v) {
    var btn = v.querySelector('.vid__play'), video = v.querySelector('video'), msg = v.querySelector('.vid__msg');
    btn.addEventListener('click', function () {
      var src = video.getAttribute('data-src');
      if (!src) { msg.hidden = false; setTimeout(function () { msg.hidden = true; }, 3200); return; }
      if (!video.src) video.src = src;
      video.muted = false; video.controls = true;
      v.classList.add('is-playing'); video.play(); track('video_play', {});
    });
  });

  /* ---------- Review notes toggle (approval walkthrough) ---------- */
  var nt = doc.querySelector('.notes-toggle');
  if (nt) {
    var on = false;
    try { on = sessionStorage.getItem('uaifs-notes') === '1'; } catch (e) {}
    function setNotes(v) { doc.body.classList.toggle('show-notes', v); nt.setAttribute('aria-pressed', v ? 'true' : 'false'); nt.lastChild.textContent = v ? ' Hide review notes' : ' Show review notes'; try { sessionStorage.setItem('uaifs-notes', v ? '1' : '0'); } catch (e) {} }
    setNotes(on);
    nt.addEventListener('click', function () { setNotes(!doc.body.classList.contains('show-notes')); });
  }

  if (pages.length) route(); else initInView();
})();
