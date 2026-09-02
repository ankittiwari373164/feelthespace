/* =========================================================
   NAVA INTERIORS — behaviour layer
   No dependencies. Every module guards for missing markup.
   ========================================================= */
(function () {
  'use strict';

  const $  = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => Array.from(r.querySelectorAll(s));
  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const WA_BASE = 'https://wa.me/917428968717';

  /* ---------- 1. Sticky header ---------- */
  (function stickyHeader() {
    const header = $('.header');
    if (!header) return;
    const sentinel = document.createElement('div');
    header.parentNode.insertBefore(sentinel, header);
    new IntersectionObserver(
      ([e]) => header.classList.toggle('is-stuck', !e.isIntersecting),
      { rootMargin: '0px' }
    ).observe(sentinel);
  })();

  /* ---------- 2. CALL NOW panel ---------- */
  (function callNow() {
    const wrap = $('.callnow');
    if (!wrap) return;
    const btn = $('.callnow__btn', wrap);
    const toggle = (open) => {
      wrap.classList.toggle('is-open', open);
      btn.setAttribute('aria-expanded', String(open));
    };
    btn.addEventListener('click', (e) => {
      e.stopPropagation();
      toggle(!wrap.classList.contains('is-open'));
    });
    document.addEventListener('click', (e) => {
      if (!wrap.contains(e.target)) toggle(false);
    });
    document.addEventListener('keydown', (e) => e.key === 'Escape' && toggle(false));
  })();

  /* ---------- 3. Desktop nav dropdowns (hover-intent + keyboard) ---------- */
  (function navMenus() {
    const items = $$('.nav > li.has-menu');
    let timer;
    items.forEach((li) => {
      const trigger = $('.nav__trigger', li);
      const open = (state) => {
        if (state) items.forEach((o) => o !== li && o.classList.remove('is-open'));
        li.classList.toggle('is-open', state);
        if (trigger) trigger.setAttribute('aria-expanded', String(state));
      };
      li.addEventListener('mouseenter', () => { clearTimeout(timer); open(true); });
      li.addEventListener('mouseleave', () => { timer = setTimeout(() => open(false), 150); });
      if (trigger) {
        trigger.addEventListener('click', (e) => {
          e.preventDefault();
          open(!li.classList.contains('is-open'));
        });
      }
      li.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') { open(false); trigger && trigger.focus(); }
      });
      li.addEventListener('focusout', (e) => {
        if (!li.contains(e.relatedTarget)) open(false);
      });
    });
  })();

  /* ---------- 4. Mobile drawer ---------- */
  (function drawer() {
    const drawer = $('.drawer');
    const backdrop = $('.drawer-backdrop');
    const openers = $$('[data-drawer-open]');
    if (!drawer || !backdrop) return;
    let lastFocus = null;

    const setOpen = (state) => {
      drawer.classList.toggle('is-open', state);
      backdrop.classList.toggle('is-open', state);
      drawer.setAttribute('aria-hidden', String(!state));
      document.body.classList.toggle('is-locked', state);
      if (state) {
        lastFocus = document.activeElement;
        const first = $('.drawer__close', drawer);
        first && first.focus();
      } else if (lastFocus) {
        lastFocus.focus();
      }
    };

    openers.forEach((b) => b.addEventListener('click', () => setOpen(true)));
    $$('[data-drawer-close]').forEach((b) => b.addEventListener('click', () => setOpen(false)));
    backdrop.addEventListener('click', () => setOpen(false));
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && drawer.classList.contains('is-open')) setOpen(false);
    });
    // close on navigation
    $$('a', drawer).forEach((a) => a.addEventListener('click', () => setOpen(false)));
  })();

  /* ---------- 5. Accordions (drawer submenus, footer, FAQ) ---------- */
  (function accordions() {
    $$('.acc__btn').forEach((btn) => {
      const panel = btn.nextElementSibling;
      if (!panel) return;
      btn.setAttribute('aria-expanded', 'false');
      btn.addEventListener('click', () => {
        const open = btn.getAttribute('aria-expanded') === 'true';
        btn.setAttribute('aria-expanded', String(!open));
        panel.style.height = open ? '0px' : panel.scrollHeight + 'px';
      });
    });
    window.addEventListener('resize', () => {
      $$('.acc__btn[aria-expanded="true"]').forEach((b) => {
        b.nextElementSibling.style.height = b.nextElementSibling.scrollHeight + 'px';
      });
    });
  })();

  /* ---------- 6. Hero carousel (crossfade, autoplay, swipe) ---------- */
  (function hero() {
    const root = $('.hero');
    if (!root) return;
    const slides = $$('.hero__slide', root);
    const dots = $$('.hero__dots button', root);
    if (slides.length < 2) return;
    let i = 0, timer;

    const go = (n) => {
      i = (n + slides.length) % slides.length;
      slides.forEach((s, k) => {
        s.classList.toggle('is-active', k === i);
        s.setAttribute('aria-hidden', String(k !== i));
      });
      dots.forEach((d, k) => d.setAttribute('aria-current', String(k === i)));
    };
    const play = () => { if (!reduced) timer = setInterval(() => go(i + 1), 6000); };
    const stop = () => clearInterval(timer);

    dots.forEach((d, k) => d.addEventListener('click', () => { stop(); go(k); play(); }));
    const prev = $('[data-hero="prev"]', root);
    const next = $('[data-hero="next"]', root);
    prev && prev.addEventListener('click', () => { stop(); go(i - 1); play(); });
    next && next.addEventListener('click', () => { stop(); go(i + 1); play(); });
    root.addEventListener('mouseenter', stop);
    root.addEventListener('mouseleave', play);

    let x0 = null;
    root.addEventListener('touchstart', (e) => { x0 = e.touches[0].clientX; stop(); }, { passive: true });
    root.addEventListener('touchend', (e) => {
      if (x0 === null) return;
      const dx = e.changedTouches[0].clientX - x0;
      if (Math.abs(dx) > 45) go(dx < 0 ? i + 1 : i - 1);
      x0 = null; play();
    });

    go(0); play();
  })();

  /* ---------- 7. Content carousels (testimonials, blog) ---------- */
  (function carousels() {
    $$('.carousel').forEach((root) => {
      const track = $('.carousel__track', root);
      const nav = $('.carousel__nav', root);
      const slides = $$('.carousel__slide', track);
      if (!track || !slides.length) return;
      let page = 0, dots = [], perPage = 1, pages = 1, drag = null;

      const measure = () => {
        const vw = root.querySelector('.carousel__viewport').clientWidth;
        perPage = Math.max(1, Math.round(vw / slides[0].getBoundingClientRect().width));
        pages = Math.ceil(slides.length / perPage);
        page = Math.min(page, pages - 1);
        if (nav) {
          nav.innerHTML = '';
          dots = Array.from({ length: pages }, (_, k) => {
            const b = document.createElement('button');
            b.type = 'button';
            b.setAttribute('aria-label', 'Go to slide group ' + (k + 1));
            b.addEventListener('click', () => go(k));
            nav.appendChild(b);
            return b;
          });
        }
        go(page);
      };
      const go = (n) => {
        page = (n + pages) % pages;
        const step = slides[0].getBoundingClientRect().width + 22;
        track.style.transform = `translateX(-${page * perPage * step}px)`;
        dots.forEach((d, k) => d.setAttribute('aria-current', String(k === page)));
      };

      // pointer drag
      track.addEventListener('pointerdown', (e) => {
        drag = { x: e.clientX, page };
        track.classList.add('is-dragging');
        track.setPointerCapture(e.pointerId);
      });
      track.addEventListener('pointerup', (e) => {
        if (!drag) return;
        const dx = e.clientX - drag.x;
        track.classList.remove('is-dragging');
        if (Math.abs(dx) > 60) go(drag.page + (dx < 0 ? 1 : -1)); else go(drag.page);
        drag = null;
      });
      track.addEventListener('pointercancel', () => { drag = null; track.classList.remove('is-dragging'); });

      let auto;
      if (root.dataset.autoplay === 'true' && !reduced) {
        const start = () => auto = setInterval(() => go(page + 1), 6000);
        root.addEventListener('mouseenter', () => clearInterval(auto));
        root.addEventListener('mouseleave', start);
        start();
      }

      measure();
      window.addEventListener('resize', debounce(measure, 180));
    });
  })();

  /* ---------- 8. Read more ---------- */
  (function readMore() {
    $$('.readmore').forEach((root) => {
      const text = $('.readmore__text', root);
      const btn = $('.readmore__btn', root);
      if (!text || !btn) return;
      const collapsed = parseInt(root.dataset.collapsed || '140', 10);
      const apply = () => {
        if (text.scrollHeight <= collapsed + 10) { btn.style.display = 'none'; text.style.maxHeight = 'none'; return; }
        btn.style.display = '';
        text.style.maxHeight = root.classList.contains('is-open') ? text.scrollHeight + 'px' : collapsed + 'px';
      };
      btn.addEventListener('click', () => {
        root.classList.toggle('is-open');
        btn.textContent = root.classList.contains('is-open') ? 'Read less' : 'Read more';
        apply();
      });
      apply();
      window.addEventListener('resize', debounce(apply, 180));
    });
  })();

  /* ---------- 9. Package detail panels ---------- */
  (function panels() {
    $$('.panel__toggle').forEach((btn) => {
      const panel = document.getElementById(btn.getAttribute('aria-controls'));
      if (!panel) return;
      btn.setAttribute('aria-expanded', 'false');
      btn.addEventListener('click', () => {
        const open = btn.getAttribute('aria-expanded') === 'true';
        btn.setAttribute('aria-expanded', String(!open));
        panel.classList.toggle('is-open', !open);
        panel.style.height = open ? '0px' : panel.scrollHeight + 'px';
        $('span', btn).textContent = open ? 'View details' : 'Hide details';
      });
    });
  })();

  /* ---------- 10. Enquiry modal (shared, source-attributed) ---------- */
  (function modal() {
    const modal = $('#enquiry');
    if (!modal) return;
    const panel = $('.modal__panel', modal);
    const titleEl = $('.modal__title', modal);
    const sourceEl = $('[name="source"]', modal);
    let lastFocus = null;

    const focusables = () =>
      $$('a[href],button:not([disabled]),input,select,textarea', panel)
        .filter((el) => el.offsetParent !== null);

    const open = (title, source) => {
      lastFocus = document.activeElement;
      if (title) titleEl.textContent = title;
      if (sourceEl) sourceEl.value = source || 'unknown';
      modal.classList.add('is-open');
      modal.setAttribute('aria-hidden', 'false');
      document.body.classList.add('is-locked');
      const f = focusables();
      f.length && f[0].focus();
    };
    const close = () => {
      modal.classList.remove('is-open');
      modal.setAttribute('aria-hidden', 'true');
      document.body.classList.remove('is-locked');
      lastFocus && lastFocus.focus();
    };

    $$('[data-modal]').forEach((btn) =>
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        open(btn.dataset.modalTitle, btn.dataset.modal);
      })
    );
    $$('[data-modal-close]', modal).forEach((b) => b.addEventListener('click', close));
    $('.modal__backdrop', modal).addEventListener('click', close);
    document.addEventListener('keydown', (e) => {
      if (!modal.classList.contains('is-open')) return;
      if (e.key === 'Escape') close();
      if (e.key === 'Tab') {
        const f = focusables();
        if (!f.length) return;
        const first = f[0], last = f[f.length - 1];
        if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
        else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
      }
    });
  })();

  /* ---------- 11. Form validation + async submit ---------- */
  (function forms() {
    const rules = {
      name: (v) => v.trim().length >= 2 || 'Enter your full name.',
      email: (v) => /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v) || 'Enter a valid email address.',
      phone: (v) => /^[6-9]\d{9}$/.test(v.replace(/[^\d]/g, '').slice(-10)) || 'Enter a 10-digit mobile number.',
      city: (v) => v !== '' || 'Choose your city.'
    };

    $$('form[data-enquiry]').forEach((form) => {
      const wrap = form.closest('[data-form-wrap]') || form.parentElement;

      const validateField = (input) => {
        const rule = rules[input.name];
        const field = input.closest('.field');
        if (!rule || !field) return true;
        const res = rule(input.value);
        field.classList.toggle('is-invalid', res !== true);
        const err = $('.err', field);
        if (err && res !== true) err.textContent = res;
        return res === true;
      };

      $$('input,select', form).forEach((input) => {
        input.addEventListener('blur', () => validateField(input));
        input.addEventListener('input', () => {
          const f = input.closest('.field');
          f && f.classList.remove('is-invalid');
        });
      });

      form.addEventListener('submit', (e) => {
        e.preventDefault();
        if ($('[name="company_website"]', form).value) return; // honeypot
        const inputs = $$('input,select', form).filter((i) => rules[i.name]);
        const ok = inputs.map(validateField).every(Boolean);
        if (!ok) {
          const bad = $('.field.is-invalid input,.field.is-invalid select', form);
          bad && bad.focus();
          return;
        }

        const btn = $('button[type="submit"]', form);
        btn.classList.add('is-loading');

        // Build a readable WhatsApp message from whatever the form collected
        const val = (n) => {
          const el = $(`[name="${n}"]`, form);
          return el && el.value ? el.value.trim() : '';
        };
        const lines = ['*New enquiry from the website*', ''];
        const push = (label, v) => { if (v) lines.push(`${label}: ${v}`); };
        push('Name', val('name'));
        push('Mobile', val('phone'));
        push('Email', val('email'));
        push('Location', val('city'));
        push('Project type', val('projecttype'));
        push('Carpet area', val('sqft') ? val('sqft') + ' sq. ft.' : '');
        push('Package', val('package'));
        push('Notes', val('message'));

        const src = val('source');
        if (src && src.startsWith('calculator:')) {
          const fig = document.querySelector('[data-calc-result] .calc__figure');
          const meta = document.querySelector('[data-calc-result] .calc__meta');
          lines.push('');
          lines.push('*Calculator estimate*');
          if (fig && fig.textContent.trim() !== '—') push('Indicative range', fig.textContent.trim());
          if (meta && meta.textContent.trim()) push('Based on', meta.textContent.trim());
        } else if (src) {
          push('Enquiry from', src);
        }

        const url = WA_BASE + '?text=' + encodeURIComponent(lines.join('\n'));

        // Open WhatsApp. Popup blockers can bite, so fall back to same-tab navigation.
        const win = window.open(url, '_blank');
        if (!win) window.location.href = url;

        wrap.classList.add('is-sent');
        form.reset();
        btn.classList.remove('is-loading');
      });
    });
  })();

  /* ---------- 12. Scroll reveals + timeline + count-up ---------- */
  (function reveals() {
    const io = new IntersectionObserver(
      (entries) => entries.forEach((e) => {
        if (!e.isIntersecting) return;
        e.target.classList.add('is-in');
        if (e.target.dataset.count) countUp(e.target);
        io.unobserve(e.target);
      }),
      { threshold: 0.18, rootMargin: '0px 0px -8% 0px' }
    );
    $$('.reveal, .process, [data-count]').forEach((el) => io.observe(el));

    function countUp(el) {
      if (reduced) { el.textContent = el.dataset.count; return; }
      const target = parseFloat(el.dataset.count);
      const suffix = el.dataset.suffix || '';
      const t0 = performance.now(), dur = 1400;
      const tick = (t) => {
        const p = Math.min((t - t0) / dur, 1);
        const eased = 1 - Math.pow(1 - p, 3);
        el.textContent = Math.round(target * eased).toLocaleString('en-IN') + suffix;
        if (p < 1) requestAnimationFrame(tick);
      };
      requestAnimationFrame(tick);
    }
  })();

  /* ---------- 13. Floating rail reveal ---------- */
  (function rail() {
    const rail = $('.rail');
    const anchor = $('.hero') || $('.banner');
    if (!rail) return;
    if (!anchor) { rail.classList.add('is-visible'); return; }
    new IntersectionObserver(
      ([e]) => rail.classList.toggle('is-visible', !e.isIntersecting),
      { threshold: 0.1 }
    ).observe(anchor);
  })();

  /* ---------- 14. Open a package panel when arriving via hash ---------- */
  (function hashPanel() {
    if (!location.hash) return;
    const target = document.querySelector(location.hash);
    if (!target || !target.classList.contains('panel')) return;
    const btn = $('.panel__toggle', target);
    btn && btn.getAttribute('aria-expanded') === 'false' && btn.click();
    setTimeout(() => target.scrollIntoView({ behavior: reduced ? 'auto' : 'smooth' }), 120);
  })();

  /* ---------- helpers ---------- */
  function debounce(fn, ms) {
    let t;
    return (...a) => { clearTimeout(t); t = setTimeout(() => fn(...a), ms); };
  }

  /* ---------- 14b. Gallery tabs ---------- */
  (function tabs() {
    const bar = $('.tabs');
    if (!bar) return;
    const btns = $$('.tab', bar);
    btns.forEach((btn) => {
      btn.addEventListener('click', () => {
        btns.forEach((b) => {
          const on = b === btn;
          b.classList.toggle('is-active', on);
          b.setAttribute('aria-selected', String(on));
          const pane = document.getElementById(b.getAttribute('aria-controls'));
          if (pane) {
            pane.classList.toggle('is-active', on);
            pane.hidden = !on;
          }
        });
      });
      btn.addEventListener('keydown', (e) => {
        const i = btns.indexOf(btn);
        if (e.key === 'ArrowRight') btns[(i + 1) % btns.length].focus();
        if (e.key === 'ArrowLeft') btns[(i - 1 + btns.length) % btns.length].focus();
      });
    });
  })();


  /* ---------- 16. Before / after slider ---------- */
  (function beforeAfter() {
    $$('[data-ba]').forEach((root) => {
      const before = $('.ba__img--before', root);
      const handle = $('.ba__handle', root);
      if (!before || !handle) return;
      let dragging = false;

      const set = (pct) => {
        const p = Math.max(0, Math.min(100, pct));
        before.style.clipPath = `inset(0 ${100 - p}% 0 0)`;
        handle.style.left = p + '%';
        handle.setAttribute('aria-valuenow', Math.round(p));
      };
      const fromEvent = (e) => {
        const r = root.getBoundingClientRect();
        const x = (e.touches ? e.touches[0].clientX : e.clientX) - r.left;
        set((x / r.width) * 100);
      };

      root.addEventListener('pointerdown', (e) => {
        dragging = true; root.setPointerCapture(e.pointerId); fromEvent(e);
      });
      root.addEventListener('pointermove', (e) => { if (dragging) fromEvent(e); });
      root.addEventListener('pointerup', () => { dragging = false; });
      root.addEventListener('pointercancel', () => { dragging = false; });

      handle.addEventListener('keydown', (e) => {
        const now = parseFloat(handle.getAttribute('aria-valuenow')) || 50;
        if (e.key === 'ArrowLeft') { e.preventDefault(); set(now - 4); }
        if (e.key === 'ArrowRight') { e.preventDefault(); set(now + 4); }
        if (e.key === 'Home') { e.preventDefault(); set(0); }
        if (e.key === 'End') { e.preventDefault(); set(100); }
      });

      set(50);
    });
  })();

  /* ---------- 17. Cost calculator ---------- */
  (function calculator() {
    const root = $('[data-calc]');
    if (!root) return;
    const steps = $$('.calc__step', root);
    const bar = $$('.calc__bar li', root);
    const next = $('[data-calc-next]', root);
    const back = $('[data-calc-back]', root);
    const areaInput = $('#calc-sqft', root);
    const resultEl = $('[data-calc-result] .calc__figure', root);
    const metaEl = $('[data-calc-result] .calc__meta', root);
    const sourceField = $('[name="source"]', root);

    // low/high rate per package slug, in ₹/sq.ft.
    const RATES = { silver: [2000, 2000], gold: [2600, 2800], platinum: [4000, 4000] };
    const state = { type: null, sqft: null, style: null, pkg: null, slug: null };
    let step = 1;

    const show = (n) => {
      step = Math.max(1, Math.min(steps.length, n));
      steps.forEach((s, i) => s.classList.toggle('is-on', i === step - 1));
      bar.forEach((b, i) => b.classList.toggle('is-on', i <= step - 1));
      root.classList.toggle('is-past-first', step > 1);
      root.classList.toggle('is-last', step === steps.length);
      if (step === steps.length) compute();
    };

    const fmt = (n) => '₹' + Math.round(n).toLocaleString('en-IN');

    const compute = () => {
      if (!state.sqft || !state.slug) {
        resultEl.textContent = '—';
        metaEl.textContent = 'Choose a property type and package';
        return;
      }
      const [lo, hi] = RATES[state.slug];
      const low = state.sqft * lo, high = state.sqft * hi;
      resultEl.textContent = low === high ? fmt(low) : fmt(low) + ' – ' + fmt(high);
      metaEl.textContent =
        `${state.pkg} · ${state.sqft.toLocaleString('en-IN')} sq. ft.` +
        (state.style ? ' · ' + state.style : '') + ' · excl. GST';
      if (sourceField) {
        sourceField.value = `calculator:${state.slug}:${state.sqft}` +
          (state.style ? ':' + state.style.replace(/\s+/g, '-').toLowerCase() : '');
      }
    };

    $$('.calc__opt', root).forEach((btn) => {
      btn.addEventListener('click', () => {
        const group = btn.parentElement;
        $$('.calc__opt', group).forEach((b) => b.classList.remove('is-sel'));
        btn.classList.add('is-sel');
        const stepNo = parseInt(btn.closest('.calc__step').dataset.step, 10);
        if (stepNo === 1) {
          state.type = btn.dataset.val;
          if (!areaInput.value) state.sqft = parseInt(btn.dataset.sqft, 10);
        } else if (stepNo === 2) {
          state.style = btn.dataset.val;
        } else if (stepNo === 3) {
          state.pkg = btn.dataset.val;
          state.slug = btn.dataset.rate;
        }
      });
    });

    if (areaInput) {
      areaInput.addEventListener('input', () => {
        const v = parseInt(areaInput.value.replace(/[^\d]/g, ''), 10);
        if (v > 0) state.sqft = v;
      });
    }

    next && next.addEventListener('click', () => show(step + 1));
    back && back.addEventListener('click', () => show(step - 1));
    show(1);
  })();

  /* ---------- 18. "View project" hover bubble ---------- */
  (function bubble() {
    if (!window.matchMedia('(hover:hover)').matches || reduced) return;
    const el = document.createElement('div');
    el.className = 'bubble';
    el.textContent = 'View';
    el.setAttribute('aria-hidden', 'true');
    document.body.appendChild(el);
    let raf = null, x = 0, y = 0;

    const move = (e) => {
      x = e.clientX; y = e.clientY;
      if (raf) return;
      raf = requestAnimationFrame(() => {
        el.style.transform = `translate(${x}px, ${y}px) translate(-50%,-50%) ` +
          (el.classList.contains('is-on') ? 'scale(1)' : 'scale(0)');
        raf = null;
      });
    };

    $$('.tile, .serv, .post').forEach((card) => {
      card.addEventListener('mouseenter', () => {
        el.textContent = card.classList.contains('post') ? 'Read' : 'View';
        el.classList.add('is-on');
      });
      card.addEventListener('mouseleave', () => el.classList.remove('is-on'));
    });
    document.addEventListener('mousemove', move, { passive: true });
  })();

  /* ---------- 19. Smooth in-page scroll with header offset ---------- */
  (function smoothAnchors() {
    document.addEventListener('click', (e) => {
      const a = e.target.closest('a[href^="#"]');
      if (!a) return;
      const id = a.getAttribute('href');
      if (id === '#' || id.length < 2) return;
      const target = document.querySelector(id);
      if (!target) return;
      e.preventDefault();
      const header = $('.header');
      const offset = (header ? header.getBoundingClientRect().height : 0) + 16;
      const top = target.getBoundingClientRect().top + window.scrollY - offset;
      window.scrollTo({ top, behavior: reduced ? 'auto' : 'smooth' });
      history.replaceState(null, '', id);
    });
  })();

  /* ---------- 15. Year stamp ---------- */
  $$('[data-year]').forEach((el) => (el.textContent = new Date().getFullYear()));
})();