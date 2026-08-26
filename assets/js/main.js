/* =========================================================
   NAVA INTERIORS — behaviour layer
   No dependencies. Every module guards for missing markup.
   ========================================================= */
(function () {
  'use strict';

  const $  = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => Array.from(r.querySelectorAll(s));
  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

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
      slides.forEach((s, k) => s.classList.toggle('is-active', k === i));
      dots.forEach((d, k) => d.setAttribute('aria-current', String(k === i)));
    };
    const play = () => { if (!reduced) timer = setInterval(() => go(i + 1), 5000); };
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

      form.addEventListener('submit', async (e) => {
        e.preventDefault();
        if ($('[name="company_website"]', form).value) return; // honeypot
        const inputs = $$('input,select', form).filter((i) => rules[i.name]);
        const ok = inputs.map(validateField).every(Boolean);
        if (!ok) { const bad = $('.field.is-invalid input,.field.is-invalid select', form); bad && bad.focus(); return; }

        const btn = $('button[type="submit"]', form);
        btn.classList.add('is-loading');
        const original = btn.textContent;
        btn.textContent = 'Sending';

        try {
          // Replace with your real endpoint:
          // await fetch('/api/enquiry', { method:'POST', body:new FormData(form) });
          await new Promise((r) => setTimeout(r, 900));
          wrap.classList.add('is-sent');
          form.reset();
        } catch (err) {
          alert('That did not send. Please call us instead, or try again in a moment.');
        } finally {
          btn.classList.remove('is-loading');
          btn.textContent = original;
        }
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

  /* ---------- 15. Year stamp ---------- */
  $$('[data-year]').forEach((el) => (el.textContent = new Date().getFullYear()));
})();
