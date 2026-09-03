# -*- coding: utf-8 -*-
"""Builds the Feel The Space site into the project root."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from data import *

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DOMAIN = "https://www.feelthespace.in/"
D = {"d": 0}


def depth(n):
    D["d"] = n
    return n


def rel():
    return "../" * D["d"]


def tel():
    return "tel:" + BRAND["phone"].replace(" ", "")


def wa():
    return ("https://wa.me/" + BRAND["phone"].replace("+", "").replace(" ", "")
            + "?text=" + WHATSAPP_TEXT.replace(" ", "%20").replace(",", "%2C").replace("'", "%27"))


SVG = {
 "chev": '<svg viewBox="0 0 12 8" fill="none" aria-hidden="true"><path d="M1 1.5 6 6.5l5-5" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>',
 "arrow": '<svg viewBox="0 0 16 12" fill="none" aria-hidden="true"><path d="M1 6h13M9.5 1.5 14 6l-4.5 4.5" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>',
 "phone": '<svg viewBox="0 0 16 16" fill="currentColor" aria-hidden="true"><path d="M3.6 1.5a1 1 0 0 0-.9.3L1.6 2.9C.9 3.6.7 4.6 1.1 5.5c1.7 3.9 4.6 6.8 8.5 8.5.9.4 1.9.2 2.6-.5l1.1-1.1a1 1 0 0 0 0-1.4l-2.1-2.1a1 1 0 0 0-1.4 0l-.9.9a12 12 0 0 1-3.6-3.6l.9-.9a1 1 0 0 0 0-1.4L4.1 1.8a1 1 0 0 0-.5-.3Z"/></svg>',
 "wa": '<svg viewBox="0 0 16 16" fill="currentColor" aria-hidden="true"><path d="M8 0a8 8 0 0 0-6.9 12L0 16l4.1-1.1A8 8 0 1 0 8 0Zm4.3 11.2c-.2.5-1 1-1.5 1-.4 0-.9.2-3-.9-2.5-1.2-4-3.8-4.2-4-.1-.2-1-1.3-1-2.5s.6-1.7.8-2c.2-.2.5-.3.6-.3h.5c.2 0 .4 0 .5.4l.7 1.7c.1.2 0 .4-.1.5l-.3.4c-.1.1-.2.3 0 .5.2.4.8 1.2 1.6 1.9 1 .9 1.8 1.1 2 1.2.2.1.4 0 .5-.1l.6-.7c.2-.2.3-.2.5-.1l1.6.8c.2.1.4.2.4.3.1.2.1.6 0 1Z"/></svg>',
 "mail": '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.4" aria-hidden="true"><rect x="1.5" y="3" width="13" height="10" rx="1.5"/><path d="m2 4 6 4.5L14 4"/></svg>',
 "calc": '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.4" aria-hidden="true"><rect x="2.5" y="1.5" width="11" height="13" rx="1.5"/><path d="M5 5h6M5.5 8.5h.01M8 8.5h.01M10.5 8.5h.01M5.5 11.5h.01M8 11.5h.01M10.5 11.5h.01"/></svg>',
 "pin": '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.4" aria-hidden="true"><path d="M8 14.5s5-4.4 5-8a5 5 0 0 0-10 0c0 3.6 5 8 5 8Z"/><circle cx="8" cy="6.4" r="1.9"/></svg>',
 "left": '<svg width="16" height="12" viewBox="0 0 16 12" fill="none" aria-hidden="true"><path d="M15 6H2M6.5 1.5 2 6l4.5 4.5" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>',
 "right": '<svg width="16" height="12" viewBox="0 0 16 12" fill="none" aria-hidden="true"><path d="M1 6h13M9.5 1.5 14 6l-4.5 4.5" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>',
 "star": '<svg viewBox="0 0 16 16" fill="currentColor" aria-hidden="true"><path d="m8 .9 2.2 4.5 5 .7-3.6 3.5.9 4.9L8 12.2l-4.5 2.3.9-4.9L.8 6.1l5-.7Z"/></svg>',
 "play": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M8 5.5v13l11-6.5z"/></svg>',
}
SOCIAL_SVG = {
 "Instagram": '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.3"><rect x="1.8" y="1.8" width="12.4" height="12.4" rx="3.6"/><circle cx="8" cy="8" r="3"/><circle cx="11.8" cy="4.2" r=".8" fill="currentColor" stroke="none"/></svg>',
 "Facebook": '<svg viewBox="0 0 16 16" fill="currentColor"><path d="M9.5 16V9h2.3l.4-2.7H9.5V4.6c0-.8.2-1.3 1.3-1.3h1.4V.9C11.9.9 11 .8 10.1.8 8 .8 6.6 2.1 6.6 4.4v1.9H4.3V9h2.3v7h2.9Z"/></svg>',
 "YouTube": '<svg viewBox="0 0 16 16" fill="currentColor"><path d="M15.5 4.8a2 2 0 0 0-1.4-1.4C12.9 3 8 3 8 3s-4.9 0-6.1.4A2 2 0 0 0 .5 4.8 21 21 0 0 0 .2 8a21 21 0 0 0 .3 3.2 2 2 0 0 0 1.4 1.4C3.1 13 8 13 8 13s4.9 0 6.1-.4a2 2 0 0 0 1.4-1.4A21 21 0 0 0 15.8 8a21 21 0 0 0-.3-3.2ZM6.5 10.3V5.7L10.4 8Z"/></svg>',
 "WhatsApp": '<svg viewBox="0 0 16 16" fill="currentColor"><path d="M8 0a8 8 0 0 0-6.9 12L0 16l4.1-1.1A8 8 0 1 0 8 0Zm4.3 11.2c-.2.5-1 1-1.5 1-.4 0-.9.2-3-.9-2.5-1.2-4-3.8-4.2-4-.1-.2-1-1.3-1-2.5s.6-1.7.8-2c.2-.2.5-.3.6-.3h.5c.2 0 .4 0 .5.4l.7 1.7c.1.2 0 .4-.1.5l-.3.4c-.1.1-.2.3 0 .5.2.4.8 1.2 1.6 1.9 1 .9 1.8 1.1 2 1.2.2.1.4 0 .5-.1l.6-.7c.2-.2.3-.2.5-.1l1.6.8c.2.1.4.2.4.3.1.2.1.6 0 1Z"/></svg>',
}


# ---------------------------------------------------------------- media
def img(name, mod="ph--4x3", eager=False):
    alt = ALT.get(name, "Feel The Space interior project")
    load = ' fetchpriority="high"' if eager else ' loading="lazy" decoding="async"'
    return (f'<figure class="ph {mod}">'
            f'<img src="{rel()}assets/img/{name}.jpg" alt="{alt}"{load}></figure>')


def video(name, mod="ph--16x9"):
    return (f'<figure class="ph {mod} vid">'
            f'<video src="{rel()}assets/video/{name}.mp4" '
            f'poster="{rel()}assets/img/{name}-poster.jpg" '
            f'controls playsinline preload="none" '
            f'aria-label="{ALT.get(name + "-poster", "Project walkthrough")}"></video></figure>')


def logo(light=False):
    f = "logo-horizontal-light" if light else "logo-horizontal"
    return (f'<a class="logo" href="{rel()}index.html">'
            f'<img src="{rel()}assets/img/{f}.png" '
            f'alt="Feel The Space — Interior Design Studio" width="639" height="199"></a>')


# ---------------------------------------------------------------- chrome
def head(title, desc, canon, og="og-share"):
    ld = f'''{{"@context":"https://schema.org","@type":"InteriorDesigner",
"name":"Feel The Space","logo":"{DOMAIN}assets/img/logo.png","image":"{DOMAIN}assets/img/{og}.jpg","@id":"{DOMAIN}",
"url":"{DOMAIN}","telephone":"{BRAND['phone']}","email":"{BRAND['email']}",
"address":{{"@type":"PostalAddress","streetAddress":"10128, Gaur City Mall",
"addressLocality":"Greater Noida West","addressRegion":"Uttar Pradesh",
"postalCode":"201306","addressCountry":"IN"}},
"sameAs":["{BRAND['instagram']}","{BRAND['facebook']}"],
"areaServed":["Noida","Greater Noida","Ghaziabad","Delhi","Gurugram"]}}'''
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{DOMAIN}{canon}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{DOMAIN}assets/img/{og}.jpg">
<meta property="og:site_name" content="Feel The Space">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#13221D">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300..600;1,9..144,300..500&family=Manrope:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="icon" href="{rel()}assets/img/favicon-32.png" sizes="32x32">
<link rel="icon" href="{rel()}assets/img/favicon-512.png" sizes="512x512">
<link rel="apple-touch-icon" href="{rel()}assets/img/favicon-180.png">
<link rel="stylesheet" href="{rel()}assets/css/style.css">
<script type="application/ld+json">{ld}</script>
</head>
<body>"""


def utility():
    return f"""
<div class="utility"><div class="container utility__inner">
  <div class="marquee" aria-hidden="true"><div class="marquee__track">
    <span>RESIDENTIAL &middot; OFFICE &middot; HOSPITALITY &middot; TURNKEY EXECUTION &middot; GREATER NOIDA WEST &middot; NOIDA &middot; GHAZIABAD &middot; DELHI NCR &middot; GURUGRAM &middot; </span>
    <span>RESIDENTIAL &middot; OFFICE &middot; HOSPITALITY &middot; TURNKEY EXECUTION &middot; GREATER NOIDA WEST &middot; NOIDA &middot; GHAZIABAD &middot; DELHI NCR &middot; GURUGRAM &middot; </span>
  </div></div>
  <a class="utility__call" href="{tel()}">{SVG['phone']}<span>{BRAND['phone']}</span></a>
</div></div>"""


def header(active=""):
    A = lambda k: ' class="is-active"' if active == k else ""
    verts = "".join(f'<li><a href="{rel()}work/{v["slug"]}.html">{v["name"]} &mdash; {v["title"]}</a></li>' for v in VERTICALS)
    servs = "".join(f'<li><a href="{rel()}services.html#{s}">{n}</a></li>' for s, n, _, _ in SERVICES)
    areas = "".join(f'<li><a href="{rel()}areas/{s}.html">{n}</a></li>' for s, n, _ in SERVICE_AREAS)
    return f"""
<header class="header"><div class="container header__inner">
  {logo()}
  <ul class="nav">
    <li{A('home')}><a href="{rel()}index.html">Home</a></li>
    <li{A('studio')}><a href="{rel()}studio.html">Studio</a></li>
    <li class="has-menu"><button class="nav__trigger" aria-expanded="false">Work {SVG['chev']}</button>
      <ul class="dropdown">{verts}<li><a href="{rel()}gallery.html">Full gallery</a></li><li><a href="{rel()}before-after.html">Before &amp; after</a></li></ul></li>
    <li class="has-menu"><button class="nav__trigger" aria-expanded="false">Services {SVG['chev']}</button>
      <ul class="dropdown">{servs}</ul></li>
    <li{A('packages')}><a href="{rel()}packages.html">Packages</a></li>
    <li{A('process')}><a href="{rel()}process.html">Process</a></li>
    <li class="has-menu"><button class="nav__trigger" aria-expanded="false">Areas {SVG['chev']}</button>
      <ul class="dropdown">{areas}</ul></li>
    <li{A('journal')}><a href="{rel()}journal.html">Journal</a></li>
    <li{A('contact')}><a href="{rel()}contact.html">Contact</a></li>
  </ul>
  <div class="header__mobile">
    <a class="header__tel" href="{tel()}" aria-label="Call {BRAND['phone']}">{SVG['phone']}</a>
    <button class="burger" type="button" data-drawer-open aria-label="Open menu" aria-controls="drawer">
      <span></span><span></span><span></span>
    </button>
  </div>
</div></header>"""


def drawer():
    verts = "".join(f'<a href="{rel()}work/{v["slug"]}.html">{v["name"]}</a>' for v in VERTICALS)
    servs = "".join(f'<a href="{rel()}services.html#{s}">{n}</a>' for s, n, _, _ in SERVICES)
    areas = "".join(f'<a href="{rel()}areas/{s}.html">{n}</a>' for s, n, _ in SERVICE_AREAS)
    return f"""
<div class="drawer-backdrop" data-drawer-close></div>
<aside class="drawer" id="drawer" aria-hidden="true" aria-label="Menu">
  <div class="drawer__head">{logo()}
    <button class="drawer__close" type="button" data-drawer-close aria-label="Close menu">&times;</button>
  </div>
  <div class="drawer__body"><nav><ul>
    <li><a href="{rel()}index.html">Home</a></li>
    <li><a href="{rel()}studio.html">Studio</a></li>
    <li><button class="acc__btn" type="button">Work {SVG['chev']}</button>
      <div class="acc__panel">{verts}<a href="{rel()}gallery.html">Full gallery</a><a href="{rel()}before-after.html">Before &amp; after</a></div></li>
    <li><button class="acc__btn" type="button">Services {SVG['chev']}</button>
      <div class="acc__panel">{servs}</div></li>
    <li><a href="{rel()}packages.html">Packages</a></li>
    <li><a href="{rel()}process.html">Process</a></li>
    <li><button class="acc__btn" type="button">Areas we serve {SVG['chev']}</button>
      <div class="acc__panel">{areas}</div></li>
    <li><a href="{rel()}journal.html">Journal</a></li>
    <li><a href="{rel()}faq.html">FAQ</a></li>
    <li><a href="{rel()}contact.html">Contact</a></li>
  </ul></nav>
  <div class="drawer__foot">
    <a class="btn btn--primary" href="{tel()}">{SVG['phone']} Call the studio</a>
    <a class="btn btn--ghost" href="{wa()}" target="_blank" rel="noopener">{SVG['wa']} Chat with our designer</a>
  </div>
  </div>
</aside>"""


def rail():
    return f"""
<div class="rail">
  <a class="rail__item rail__item--wa" href="{wa()}" target="_blank" rel="noopener"><span>Chat with our designer</span>{SVG['wa']}</a>
  <a class="rail__item" href="{tel()}"><span>{BRAND['phone']}</span>{SVG['phone']}</a>
  <a class="rail__item" href="mailto:{BRAND['email']}"><span>Email</span>{SVG['mail']}</a>
  <button class="rail__item rail__item--cta" type="button" data-modal="rail" data-modal-title="Get a free estimate"><span>Free estimate</span>{SVG['calc']}</button>
</div>"""


def form(idp, submit="Send enquiry", compact=False):
    areas = "".join(f'<option value="{n}">{n}</option>' for _, n, _ in SERVICE_AREAS)
    verts = "".join(f'<option value="{v["name"]}">{v["name"]}</option>' for v in VERTICALS)
    pkgs = "".join(f'<option value="{p["name"]}">{p["name"]} — {p["rate"]}/sq. ft.</option>' for p in PACKAGES)
    if compact:
        # calculator gate: name + WhatsApp only, everything else already captured by the steps
        return f"""
<div data-form-wrap>
  <form class="form" data-enquiry novalidate>
    <input type="hidden" name="source" value="{idp}">
    <div class="hp"><label>Company website<input type="text" name="company_website" tabindex="-1" autocomplete="off"></label></div>
    <div class="form__row">
      <div class="field"><label for="{idp}-name">Name</label><input id="{idp}-name" name="name" type="text" autocomplete="name" required><span class="err"></span></div>
      <div class="field"><label for="{idp}-phone">WhatsApp number</label><input id="{idp}-phone" name="phone" type="tel" inputmode="numeric" autocomplete="tel" required><span class="err"></span></div>
    </div>
    <button class="btn btn--primary" type="submit">{submit}</button>
    <p class="form__note">Opens WhatsApp with your estimate attached. No spam.</p>
  </form>
  <div class="form__status" role="status">
    <h4>Sent to WhatsApp.</h4>
    <p>Press send in WhatsApp and we will come back with a detailed breakdown.</p>
  </div>
</div>"""
    return f"""
<div data-form-wrap>
  <form class="form" data-enquiry novalidate>
    <input type="hidden" name="source" value="{idp}">
    <div class="hp"><label>Company website<input type="text" name="company_website" tabindex="-1" autocomplete="off"></label></div>
    <div class="field"><label for="{idp}-name">Name</label><input id="{idp}-name" name="name" type="text" autocomplete="name" required><span class="err"></span></div>
    <div class="form__row">
      <div class="field"><label for="{idp}-phone">Mobile</label><input id="{idp}-phone" name="phone" type="tel" inputmode="numeric" autocomplete="tel" required><span class="err"></span></div>
      <div class="field"><label for="{idp}-email">Email</label><input id="{idp}-email" name="email" type="email" autocomplete="email" required><span class="err"></span></div>
    </div>
    <div class="form__row">
      <div class="field"><label for="{idp}-area">Location</label><select id="{idp}-area" name="city" required><option value="">Select your area</option>{areas}<option value="Other">Elsewhere in NCR</option></select><span class="err"></span></div>
      <div class="field"><label for="{idp}-type">Project type</label><select id="{idp}-type" name="projecttype">{verts}</select></div>
    </div>
    <div class="form__row">
      <div class="field"><label for="{idp}-sqft">Carpet area (sq. ft.)</label><input id="{idp}-sqft" name="sqft" type="text" inputmode="numeric" placeholder="e.g. 1275"></div>
      <div class="field"><label for="{idp}-pkg">Package of interest</label><select id="{idp}-pkg" name="package"><option value="">Not decided yet</option>{pkgs}<option value="Design only">Design only</option></select></div>
    </div>
    <div class="field"><label for="{idp}-msg">Anything we should know?</label><textarea id="{idp}-msg" name="message" placeholder="Possession date, rooms to be covered, budget range."></textarea></div>
    <button class="btn btn--primary" type="submit">{submit}</button>
    <p class="form__note">We reply within one working day. Your number stays with the studio.</p>
  </form>
  <div class="form__status" role="status">
    <h4>Thank you &mdash; that reached the studio.</h4>
    <p>We will call you within one working day. For anything urgent, WhatsApp us on {BRAND['phone']}.</p>
  </div>
</div>"""


def modal():
    return f"""
<div class="modal" id="enquiry" aria-hidden="true" role="dialog" aria-modal="true" aria-labelledby="enquiry-title">
  <div class="modal__backdrop"></div>
  <div class="modal__panel">
    <button class="modal__close" type="button" data-modal-close aria-label="Close">&times;</button>
    <h2 class="modal__title" id="enquiry-title">Get a free estimate</h2>
    <p class="modal__sub">Tell us about the space. We come back with a written estimate, not a phone quote.</p>
    {form("modal")}
  </div>
</div>"""


def cta(title, sub, source, label="Book a consultation"):
    return f"""
<section class="section section--ink"><div class="container section-head section-head--center" style="margin-bottom:0">
  <h2>{title}</h2>
  <p style="margin-top:14px">{sub}</p>
  <p class="cta__row">
    <button class="btn btn--gold" type="button" data-modal="{source}" data-modal-title="{label}">{label}</button>
    <a class="btn btn--outline" href="{wa()}" target="_blank" rel="noopener">{SVG['wa']} Chat with our designer</a>
  </p>
</div></section>"""


def consult():
    return f"""
<section class="consult section"><div class="container consult__grid">
  <div>
    <span class="eyebrow">Talk to the studio</span>
    <h2 class="section-title">Book a free consultation</h2><div class="rule"></div>
    <p style="margin-top:22px">Bring your floor plan, or just your possession letter. We will walk you through what your carpet area can take, what it costs at each finish level, and what the design fee covers.</p>
    <ul class="contact-list">
      <li>{SVG['phone']}<a href="{tel()}">{BRAND['phone']}</a></li>
      <li>{SVG['mail']}<a href="mailto:{BRAND['email']}">{BRAND['email']}</a></li>
      <li>{SVG['pin']}<a href="{BRAND['maps']}" target="_blank" rel="noopener">{BRAND['address_l1']}<br>{BRAND['address_l2']}</a></li>
    </ul>
  </div>
  <div>{form("consult", "Book my consultation")}</div>
</div>
<div class="container">{badges_block()}</div>
</section>"""


def footer():
    quick = [("Studio", "studio.html"), ("Packages", "packages.html"), ("Process", "process.html"),
             ("Services", "services.html"), ("Gallery", "gallery.html"), ("Journal", "journal.html"),
             ("FAQ", "faq.html"), ("Contact", "contact.html"), ("Sitemap", "sitemap.html")]
    q = "".join(f'<li><a href="{rel()}{u}">{t}</a></li>' for t, u in quick)
    w = "".join(f'<li><a href="{rel()}work/{v["slug"]}.html">{v["name"]}</a></li>' for v in VERTICALS)
    w += f'<li><a href="{rel()}before-after.html">Before &amp; after</a></li>'
    a = "".join(f'<li><a href="{rel()}areas/{s}.html">{n}</a></li>' for s, n, _ in SERVICE_AREAS)
    soc = (f'<a href="{BRAND["instagram"]}" target="_blank" rel="noopener" aria-label="Instagram">{SOCIAL_SVG["Instagram"]}</a>'
           f'<a href="{BRAND["facebook"]}" target="_blank" rel="noopener" aria-label="Facebook">{SOCIAL_SVG["Facebook"]}</a>'
           f'<a href="{BRAND["youtube"]}" target="_blank" rel="noopener" aria-label="YouTube">{SOCIAL_SVG["YouTube"]}</a>'
           f'<a href="{wa()}" target="_blank" rel="noopener" aria-label="WhatsApp">{SOCIAL_SVG["WhatsApp"]}</a>')
    return f"""
<footer class="footer"><div class="container">
  <div class="footer__cols">
    <div class="footer__brand">
      {logo(light=True)}
      <p class="footer__tag">{BRAND['tagline']}</p>
      <ul class="contact-list contact-list--sm">
        <li>{SVG['phone']}<a href="{tel()}">{BRAND['phone']}</a></li>
        <li>{SVG['mail']}<a href="mailto:{BRAND['email']}">{BRAND['email']}</a></li>
        <li>{SVG['pin']}<span>{BRAND['address_l1']}<br>{BRAND['address_l2']}</span></li>
      </ul>
      <div class="social">{soc}</div>
      <a class="reviewlink" href="{BRAND['review']}" target="_blank" rel="noopener">
        <span class="reviewlink__stars" aria-hidden="true">{SVG['star']}{SVG['star']}{SVG['star']}{SVG['star']}{SVG['star']}</span>
        <span>Review us on Google</span></a>
    </div>
    <div><h4>Work</h4><ul class="footer__list">{w}</ul></div>
    <div><h4>Studio</h4><ul class="footer__list">{q}</ul></div>
    <div><h4>Areas we serve</h4><ul class="footer__list">{a}</ul></div>
  </div>
  <div class="footer__bottom">
    <p>&copy; <span data-year>2026</span> Feel The Space &middot; Interior Design Studio. All rights reserved.</p>
    <p>{BRAND['site']}</p>
  </div>
</div></footer>
{drawer()}{rail()}{sticky_bar()}{modal()}
<script src="{rel()}assets/js/main.js" defer></script>
</body></html>"""


def promise_block():
    return f"""
<section class="section section--ink"><div class="container promise">
  <div class="promise__main reveal">
    <span class="eyebrow">Our absolute promise</span>
    <h2 class="section-title">{PROMISE['title']}</h2><div class="rule"></div>
    <p style="margin-top:22px">{PROMISE['body']}</p>
    <ul class="promise__pills">
      <li>100% A-grade material</li><li>Best quality</li><li>Best labour work</li>
    </ul>
  </div>
  <figure class="promise__quote reveal" data-d="1">
    <blockquote>{PROMISE['quote']}</blockquote>
    <figcaption>{PROMISE['attrib']}</figcaption>
  </figure>
</div></section>"""


def badges_block():
    items = "".join(
        f'<div class="badge reveal" data-d="{i}"><strong>{a}</strong><span>{b}</span></div>'
        for i, (a, b) in enumerate(TRUST_BADGES))
    return f'<div class="badges">{items}</div>'


def societies_block():
    cols = "".join(
        f'<div class="soc reveal" data-d="{i}"><h3>{city}</h3><ul>'
        + "".join(f"<li>{n}</li>" for n in names) + "</ul></div>"
        for i, (city, names) in enumerate(SOCIETIES))
    return f"""
<section class="section section--paper"><div class="container">
  <div class="section-head section-head--center">
    <span class="eyebrow">Delivered in Delhi NCR</span>
    <h2 class="section-title">Societies we have already worked in</h2><div class="rule"></div>
    <p style="margin-top:18px">If you live in one of these, we have almost certainly done a flat in your layout — ask us to show you.</p>
  </div>
  <div class="socs">{cols}</div>
</div></section>"""


def ba_slider(pair):
    return f"""<div class="ba" data-ba>
    <div class="ba__img ba__img--after">{img(pair['after'], '')}<span class="ba__tag">After</span></div>
    <div class="ba__img ba__img--before">{img(pair['before'], '')}<span class="ba__tag">Before</span></div>
    <div class="ba__handle" role="slider" tabindex="0" aria-label="Reveal before or after"
         aria-valuemin="0" aria-valuemax="100" aria-valuenow="50"><span></span></div>
  </div>"""


def beforeafter_block():
    pair = BEFORE_AFTER[0]
    return f"""
<section class="section"><div class="container container--narrow">
  <div class="section-head section-head--center">
    <span class="eyebrow">Before &amp; after</span>
    <h2 class="section-title">Drag to see the transformation</h2><div class="rule"></div>
  </div>
  {ba_slider(pair)}
  <p class="fineprint">Bare-shell handover on the left, finished interior on the right &mdash; {pair['title']}, {pair['where']}.</p>
  <p class="cta__row" style="justify-content:center"><a class="btn btn--ghost" href="{rel()}before-after.html">See more before &amp; after {SVG['arrow']}</a></p>
</div></section>"""


def calculator_block():
    types = "".join(f'<button type="button" class="calc__opt" data-val="{n}" data-sqft="{a}">{n}<em>~{a} sq. ft.</em></button>'
                    for n, a in CALC_TYPES)
    styles = "".join(f'<button type="button" class="calc__opt" data-val="{n}">{n}</button>' for n in CALC_STYLES)
    pkgs = "".join(
        f'<button type="button" class="calc__opt" data-val="{p["name"]}" data-rate="{p["slug"]}">'
        f'{p["name"]}<em>{p["rate"]} / sq. ft.</em></button>' for p in PACKAGES)
    return f"""
<section class="section section--paper" id="calculator"><div class="container container--narrow">
  <div class="section-head section-head--center">
    <span class="eyebrow">Interior cost calculator</span>
    <h2 class="section-title">Get an indicative budget in three steps</h2><div class="rule"></div>
  </div>
  <div class="calc" data-calc>
    <ol class="calc__bar"><li class="is-on">Property</li><li>Style</li><li>Package</li><li>Result</li></ol>

    <div class="calc__step is-on" data-step="1">
      <h3>1 &middot; What are you doing up?</h3>
      <div class="calc__opts">{types}</div>
      <div class="field calc__area"><label for="calc-sqft">Or enter your carpet area (sq. ft.)</label>
        <input id="calc-sqft" type="text" inputmode="numeric" placeholder="e.g. 1275"></div>
    </div>

    <div class="calc__step" data-step="2">
      <h3>2 &middot; Which direction appeals?</h3>
      <div class="calc__opts">{styles}</div>
    </div>

    <div class="calc__step" data-step="3">
      <h3>3 &middot; Which package?</h3>
      <div class="calc__opts">{pkgs}</div>
    </div>

    <div class="calc__step" data-step="4">
      <h3>Your indicative range</h3>
      <div class="calc__result" data-calc-result>
        <span class="calc__figure">&mdash;</span>
        <span class="calc__meta"></span>
      </div>
      <p class="calc__note">Indicative only, without GST. The exact figure is locked after 3D approval through a signed BOQ. The {DESIGN_FEE['rate']}/sq. ft. design fee is billed separately from execution, also without GST.</p>
      <div class="calc__gate">
        <p>Send this estimate to yourself and we will follow up with a detailed breakdown.</p>
        {form("calculator", "Send me this estimate", compact=True)}
      </div>
    </div>

    <div class="calc__nav">
      <button type="button" class="btn btn--ghost" data-calc-back>Back</button>
      <button type="button" class="btn btn--primary" data-calc-next>Continue</button>
    </div>
  </div>
</div></section>"""


def sticky_bar():
    return f"""
<div class="stickybar">
  <a class="stickybar__btn" href="{tel()}">{SVG['phone']}<span>Call studio</span></a>
  <a class="stickybar__btn stickybar__btn--wa" href="{wa()}" target="_blank" rel="noopener">{SVG['wa']}<span>Free estimate</span></a>
</div>"""


def video_testimonials_block():
    cards = ""
    for i, v in enumerate(VIDEO_TESTIMONIALS):
        if v["video"]:
            media = (f'<video src="{rel()}assets/video/{v["video"]}.mp4" '
                     f'poster="{rel()}assets/img/{v["poster"]}.jpg" '
                     f'controls playsinline preload="none"></video>')
        else:
            media = (f'{img(v["poster"], "")}'
                     f'<span class="vt__play" aria-hidden="true">{SVG["play"]}</span>'
                     f'<span class="vt__soon">Video coming soon</span>')
        cards += f"""<figure class="vt reveal" data-d="{i}">
      <div class="vt__media">{media}</div>
      <figcaption><strong>{v['name']}</strong><span>{v['where']}</span><em>{v['line']}</em></figcaption>
    </figure>"""
    return f"""
<section class="section"><div class="container">
  <div class="section-head section-head--center">
    <span class="eyebrow">In their own words</span>
    <h2 class="section-title">Video testimonials</h2><div class="rule"></div>
    <p style="margin-top:18px">Short clips filmed at handover. More going up as we collect them.</p>
  </div>
  <div class="vts">{cards}</div>
  <p class="cta__row" style="justify-content:center">
    <a class="btn btn--ghost" href="{BRAND['review']}" target="_blank" rel="noopener">{SVG['star']} Read our Google reviews</a>
  </p>
</div></section>"""


def banner(title, crumb, image, lede=""):
    lede_html = f'<p class="banner__lede">{lede}</p>' if lede else ""
    return f"""
<section class="banner">{img(image, "", eager=True)}
  <div class="banner__content"><div class="container">
    <p class="crumbs"><a href="{rel()}index.html">Home</a> <span>/</span> {crumb}</p>
    <h1>{title}</h1>{lede_html}
  </div></div>
</section>"""


def write(path, html):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w", encoding="utf-8").write(html)


def page(path, title, desc, body, active="", og="og-share"):
    write(path, head(title, desc, path, og) + utility() + header(active) + body + footer())


# ---------------------------------------------------------------- blocks
def stats_block():
    items = "".join(f'<div class="stats__item"><span class="stats__label">{a}</span>'
                    f'<span class="stats__value">{b}</span></div>' for a, b in STATS)
    return f'<section class="stats"><div class="container"><div class="stats__grid">{items}</div></div></section>'


def phases_block(paper=False):
    cards = "".join(f"""<div class="phase reveal" data-d="{i}">
      <span class="phase__num">{n}</span>
      <h3>{t}</h3><p>{d}</p></div>""" for i, (n, t, d) in enumerate(PHASES))
    return f"""
<section class="section {'section--paper' if paper else ''}"><div class="container">
  <div class="section-head section-head--center">
    <span class="eyebrow">How we work</span>
    <h2 class="section-title">Three phases. One seamless journey.</h2><div class="rule"></div>
  </div>
  <div class="phases">{cards}</div>
</div></section>"""


def packages_block(heading=True):
    cards = ""
    for i, p in enumerate(PACKAGES):
        feat = ' pkg--feature' if p["slug"] == "gold" else ''
        tag = '<span class="pkg__tag">Most chosen</span>' if p["slug"] == "gold" else ''
        cards += f"""<a class="pkg{feat} reveal" data-d="{i}" href="{rel()}packages.html#{p['slug']}">
  <div class="pkg__media">{img(p['image'], 'ph--4x3')}{tag}</div>
  <div class="pkg__body">
    <span class="eyebrow">{p['kicker']}</span>
    <div class="pkg__name">{p['name']}</div>
    <div class="pkg__price"><span class="pkg__rate">{p['rate']}</span><span class="pkg__unit">/ sq. ft.</span></div>
    <p class="pkg__desc">{p['signature']}</p>
    <span class="pkg__link">What's included {SVG['arrow']}</span>
  </div></a>"""
    head_ = """<div class="section-head section-head--center">
    <span class="eyebrow">Turnkey execution</span>
    <h2 class="section-title">Three packages. Three distinct experiences.</h2><div class="rule"></div>
    <p style="margin-top:18px">The base scope is identical in all three. What changes is the level of finish.</p>
    </div>""" if heading else ""
    return f"""<section class="section"><div class="container">{head_}
  <div class="packages">{cards}</div>
  <p class="fineprint">Rates are per square foot of carpet area, without GST. Final figures are locked after 3D approval through a signed BOQ.</p>
</div></section>"""


def design_fee_block():
    f = DESIGN_FEE
    return f"""
<section class="section section--paper"><div class="container">
  <div class="section-head section-head--center">
    <span class="eyebrow">Phase 1</span>
    <h2 class="section-title">Comprehensive design &amp; consultation</h2><div class="rule"></div>
    <p style="margin-top:18px">{f['note']}</p>
  </div>
  <div class="fee">
    <div class="fee__main">
      <span class="fee__rate">{f['rate']}</span>
      <span class="fee__unit">per sq. ft.</span>
      <p class="fee__note">Design fee, without GST</p>
    </div>
    <div class="fee__example">
      <h4>Worked example &mdash; {f['example_area']}</h4>
      <dl>
        <div class="fee__total"><dt>Total design fee</dt><dd>{f['example_total']}</dd></div>
      </dl>
      <p class="fineprint" style="text-align:left;margin-top:14px">Billed separately from execution, so you always know what design costs on its own.</p>
    </div>
  </div>
</div></section>"""


def deliverables_block():
    cards = "".join(f"""<div class="deliv reveal" data-d="{i}">
      <span class="deliv__num">{n}</span><h3>{t}</h3><p>{d}</p></div>"""
      for i, (n, t, d) in enumerate(DELIVERABLES))
    return f"""
<section class="section section--ink"><div class="container">
  <div class="section-head section-head--center">
    <span class="eyebrow">Design deliverables</span>
    <h2 class="section-title">Everything is planned before execution begins.</h2><div class="rule"></div>
  </div>
  <div class="delivs">{cards}</div>
</div></section>"""


def core_scope_block():
    cards = "".join(f"""<div class="scope reveal" data-d="{i}"><h3>{t}</h3><p>{d}</p></div>"""
      for i, (t, d) in enumerate(CORE_SCOPE))
    return f"""
<section class="section"><div class="container">
  <div class="section-head section-head--center">
    <span class="eyebrow">Phase 2</span>
    <h2 class="section-title">Core base scope</h2><div class="rule"></div>
    <p style="margin-top:18px">The foundation included across every project, whichever package you choose.</p>
  </div>
  <div class="scopes">{cards}</div>
</div></section>"""


def materials_block():
    rows = "".join(f'<div class="mat reveal" data-d="{i%3}"><span>{k}</span><strong>{v}</strong></div>'
                   for i, (k, v) in enumerate(MATERIALS))
    return f"""
<section class="section section--paper"><div class="container">
  <div class="section-head section-head--center">
    <span class="eyebrow">Material highlights</span>
    <h2 class="section-title">A clear material language for every level of finish.</h2><div class="rule"></div>
  </div>
  <div class="mats">{rows}</div>
</div></section>"""


def steps_block(steps, eyebrow, title, note="", ink=False):
    cards = "".join(f'<div class="step reveal" data-d="{i}"><span class="step__num">{n}</span><p>{t}</p></div>'
                    for i, (n, t) in enumerate(steps))
    note_html = f'<p class="steps__note">{note}</p>' if note else ""
    return f"""
<section class="section {'section--ink' if ink else ''} process-sec"><div class="container">
  <div class="section-head section-head--center">
    <span class="eyebrow">{eyebrow}</span>
    <h2 class="section-title">{title}</h2><div class="rule"></div>
  </div>
  <div class="steps">{cards}</div>{note_html}
</div></section>"""


def verticals_block():
    tiles = "".join(f"""<a class="tile reveal" data-d="{i}" href="{rel()}work/{v['slug']}.html">
      {img(v['hero'], 'ph--3x4')}
      <span class="tile__body"><span class="tile__label">{v['name']}</span>
      <span class="tile__sub">{v['lede']}</span></span></a>"""
      for i, v in enumerate(VERTICALS))
    return f"""
<section class="section"><div class="container">
  <div class="section-head section-head--center">
    <span class="eyebrow">What we do</span>
    <h2 class="section-title">Homes, workspaces and hotels</h2><div class="rule"></div>
  </div>
  <div class="tiles tiles--3">{tiles}</div>
</div></section>"""


def testimonials_block():
    slides = "".join(f"""<div class="carousel__slide"><div class="quote">
      <div class="quote__mark">&ldquo;</div><p>{q}</p>
      <div class="quote__who">{n}</div><div class="quote__where">{c}</div></div></div>"""
      for n, c, q in TESTIMONIALS)
    return f"""
<section class="section section--paper"><div class="container">
  <div class="section-head section-head--center">
    <span class="eyebrow">Client feedback</span>
    <h2 class="section-title">What clients say afterwards</h2><div class="rule"></div>
  </div>
  <div class="carousel" data-autoplay="true">
    <div class="carousel__viewport"><div class="carousel__track">{slides}</div></div>
    <div class="carousel__nav"></div>
  </div>
</div></section>"""


def journal_block():
    slides = "".join(f"""<div class="carousel__slide"><a class="post" href="{rel()}journal/{s}.html">
      <div class="post__media">{img(im)}</div>
      <div class="post__body"><span class="post__date">{dt} &middot; {cat}</span><h3>{t}</h3></div></a></div>"""
      for s, t, dt, cat, im, _ in POSTS)
    return f"""
<section class="section"><div class="container">
  <div class="section-head section-head--center"><span class="eyebrow">Journal</span>
  <h2 class="section-title">Notes from the studio</h2><div class="rule"></div></div>
  <div class="carousel">
    <div class="carousel__viewport"><div class="carousel__track">{slides}</div></div>
    <div class="carousel__nav"></div>
  </div>
  <p style="text-align:center;margin-top:28px"><a class="btn btn--ghost" href="{rel()}journal.html">All posts</a></p>
</div></section>"""


def faq_block(limit=None, ink=False):
    items = FAQS[:limit] if limit else FAQS
    li = "".join(f"""<li><button class="acc__btn" type="button">{q} {SVG['chev']}</button>
      <div class="acc__panel"><p>{a}</p></div></li>""" for q, a in items)
    more = f'<p style="text-align:center;margin-top:32px"><a class="btn btn--ghost" href="{rel()}faq.html">All questions</a></p>' if limit else ""
    return f"""
<section class="section {'section--ink' if ink else ''}"><div class="container container--narrow">
  <div class="section-head section-head--center">
    <span class="eyebrow">Questions</span>
    <h2 class="section-title">Answered plainly</h2><div class="rule"></div>
  </div>
  <ul class="accordion">{li}</ul>{more}
</div></section>"""


# ---------------------------------------------------------------- pages
def build_home():
    depth(0)
    # Hero: one slide per package, each a 3-image grid
    sl = ""
    for i, pk in enumerate(PACKAGES):
        cells = "".join(
            f'<div class="hgrid__cell hgrid__cell--{k+1}">{img(n, "", eager=(i == 0 and k == 0))}</div>'
            for k, n in enumerate(pk["images"]))
        sl += (f'<div class="hero__slide{" is-active" if i == 0 else ""}" '
               f'aria-hidden="{"false" if i == 0 else "true"}">'
               f'<div class="hgrid">{cells}</div></div>')
    dots = "".join(f'<button type="button" aria-label="{p["name"]} package">'
                   f'<span>{p["name"]}</span></button>' for p in PACKAGES)
    servs = "".join(f"""<a class="serv reveal" data-d="{i%3}" href="{rel()}services.html#{s_}">
      {img(im, 'ph--4x3')}<h3>{n}</h3><p>{d}</p></a>"""
      for i, (s_, n, im, d) in enumerate(SERVICES))

    body = f"""
<section class="hero hero--grid">
  <div class="hero__slides">{sl}</div>
  <div class="container hero__content">
    <p class="hero__eyebrow">Interior Design Studio &middot; Greater Noida West</p>
    <h1>Let's create your <em>dream space</em>.</h1>
    <p class="hero__lede">Design, drawings and turnkey execution for homes, offices and hotels across Delhi NCR — priced transparently from the first meeting.</p>
    <div class="hero__actions">
      <button class="btn btn--gold" type="button" data-modal="hero" data-modal-title="Get a free estimate">Get a free estimate</button>
      <a class="btn btn--outline" href="{rel()}packages.html">See package rates</a>
    </div>
  </div>
  <div class="hero__arrows">
    <button type="button" data-hero="prev" aria-label="Previous package">{SVG['left']}</button>
    <button type="button" data-hero="next" aria-label="Next package">{SVG['right']}</button>
  </div>
  <div class="hero__dots hero__dots--labelled">{dots}</div>
</section>
{stats_block()}
{verticals_block()}
{phases_block(paper=True)}
{design_fee_block()}
{packages_block()}
<section class="section section--paper"><div class="container">
  <div class="section-head section-head--center"><span class="eyebrow">Services</span>
  <h2 class="section-title">What we take on</h2><div class="rule"></div></div>
  <div class="servs">{servs}</div>
</div></section>
{core_scope_block()}
{promise_block()}
{materials_block()}
{beforeafter_block()}
<section class="section"><div class="container split">
  <div class="split__media reveal">{video("res-walkthrough")}</div>
  <div class="reveal" data-d="1">
    <span class="eyebrow">Walkthrough</span>
    <h2 class="section-title">See a finished home</h2><div class="rule"></div>
    <p style="margin-top:22px">A short walkthrough of a completed residential project — layered ceilings, cove lighting, panelled living-dining and a fully fitted modular kitchen.</p>
    <p>Every project we photograph is our own work, executed by our own team. Nothing on this site is a stock render.</p>
    <p class="cta__row"><a class="btn btn--ghost" href="{rel()}gallery.html">Browse the gallery</a></p>
  </div>
</div></section>
{societies_block()}
{video_testimonials_block()}
{testimonials_block()}
{steps_block(NEXT_STEPS, "Next steps", "From proposal approval to your finished space.", "A well-planned space starts with one clear decision.")}
{journal_block()}
{faq_block(limit=4, ink=True)}
{consult()}"""
    page("index.html", "Feel The Space | Interior Design Studio in Greater Noida West",
         "Interior design and turnkey execution for homes, offices and hotels across Noida, Greater Noida, Ghaziabad and Delhi NCR. Design at ₹150/sq. ft.; Silver, Gold and Platinum packages.",
         body, "home")


def build_packages():
    depth(0)
    panels = ""
    for p in PACKAGES:
        scope = "".join(f"<li>{s}</li>" for s in p["scope"])
        hl = ""
        if p.get("highlights"):
            hl = '<div class="panel__hl">' + "".join(
                f"<div><h4>{t}</h4><p>{d}</p></div>" for t, d in p["highlights"]) + "</div>"
        panels += f"""
<article class="panel" id="{p['slug']}">
  <div class="panel__head">
    <div class="panel__media">{img(p['image'], '')}</div>
    <div class="panel__info">
      <span class="eyebrow">{p['kicker']}</span>
      <h2 class="panel__name">{p['name']}</h2>
      <p class="panel__desc">{p['headline']}</p>
      <div class="panel__price"><span class="pkg__rate">{p['rate']}</span><span class="pkg__unit">/ sq. ft.</span></div>
      <p class="panel__sig">{p['signature']}</p>
      <button class="panel__toggle" type="button" aria-controls="d-{p['slug']}"><span>View details</span>{SVG['chev']}</button>
    </div>
  </div>
  <div class="panel__details" id="d-{p['slug']}">
    <div class="panel__inner">
      <h3>Key upgrades &amp; scope</h3>
      <ul class="ticks">{scope}</ul>{hl}
      <div class="panel__links">
        <button class="btn btn--primary" type="button" data-modal="pkg-{p['slug']}" data-modal-title="Price the {p['name']} package">Price this for my space</button>
        <a class="btn btn--ghost" href="{rel()}faq.html">Questions about packages</a>
      </div>
    </div>
  </div>
</article>"""

    terms = "".join(f'<div class="term reveal" data-d="{i%2}"><h4>{t}</h4><p>{d}</p></div>'
                    for i, (t, d) in enumerate(TERMS))
    body = f"""
{banner("Packages &amp; pricing", "Packages", "res-living-panelled",
        "Choose the level of finish you love. Silver, Gold or Platinum — the base scope stays the same.")}
{design_fee_block()}
{packages_block(heading=True)}
<section class="section section--paper"><div class="container">{panels}</div></section>
{promise_block()}
{core_scope_block()}
{materials_block()}
{steps_block(BOQ_STEPS, "BOQ &amp; commercial clarity", "Final numbers are locked after design approval.",
             "After 3D approval, the detailed Bill of Quantities becomes the commercial reference for payment milestones and execution planning.", ink=True)}
<section class="section"><div class="container">
  <div class="section-head section-head--center"><span class="eyebrow">Commercial terms</span>
  <h2 class="section-title">The key points, clearly summarised.</h2><div class="rule"></div></div>
  <div class="terms">{terms}</div>
</div></section>
{cta("Want this priced for your carpet area?",
     "Send your floor plan and possession date. You will get an itemised estimate, not a range.",
     "packages-cta", "Get my estimate")}
{consult()}"""
    page("packages.html", "Interior packages & pricing | Feel The Space",
         "Silver ₹2,050, Gold ₹2,650 and Platinum ₹3,450 per sq. ft. turnkey interior packages, plus a ₹150/sq. ft. design fee. Full scope and commercial terms.",
         body, "packages", "res-living-panelled")


def build_process():
    depth(0)
    body = f"""
{banner("How we work", "Process", "res-foyer-marble",
        "Design first, priced separately. Execution only once you have approved the drawings and the BOQ.")}
{phases_block()}
{design_fee_block()}
{deliverables_block()}
{core_scope_block()}
{steps_block(BOQ_STEPS, "BOQ &amp; commercial clarity", "Final numbers are locked after design approval.",
             "After 3D approval, the detailed Bill of Quantities becomes the commercial reference for payment milestones and execution planning.")}
{steps_block(NEXT_STEPS, "Next steps", "From proposal approval to your finished space.",
             "A well-planned space starts with one clear decision.", ink=True)}
{materials_block()}
{faq_block(limit=5)}
{consult()}"""
    page("process.html", "Our process | Feel The Space",
         "Three phases: design and consultation, core base scope, then turnkey execution. Deliverables, BOQ locking and commercial terms explained.",
         body, "process", "res-foyer-marble")


def build_services():
    depth(0)
    rows = ""
    for i, (s, n, im, d) in enumerate(SERVICES):
        rev = " split--rev" if i % 2 else ""
        rows += f"""<div class="split{rev} serv-row" id="{s}">
  <div class="split__media reveal">{img(im)}</div>
  <div class="reveal" data-d="1">
    <span class="eyebrow">Service {i+1:02d}</span>
    <h2 class="section-title">{n}</h2><div class="rule"></div>
    <p style="margin-top:22px">{d}</p>
    <p class="cta__row"><button class="btn btn--ghost" type="button" data-modal="serv-{s}" data-modal-title="Enquire about {n}">Enquire about this</button></p>
  </div></div>"""
    body = f"""
{banner("Services", "Services", "res-kitchen-island",
        "From the first layout to the final coat of paint, under one contract.")}
<section class="section"><div class="container">{rows}</div></section>
{materials_block()}
{cta("Not sure which of these you need?",
     "Send us the plan. We will tell you what the space actually requires before quoting anything.",
     "services-cta", "Ask the studio")}
{consult()}"""
    page("services.html", "Interior design services | Feel The Space",
         "Space planning, 3D visualisation, modular kitchens, wardrobes and carpentry, false ceiling and lighting, and full turnkey execution.",
         body, og="res-kitchen-island")


def build_work():
    for v in VERTICALS:
        depth(1)
        grid = "".join(f'<div class="reveal" data-d="{k%4}">{img(n)}</div>' for k, n in enumerate(v["gallery"]))
        vid = ""
        if v["video"]:
            vid = f"""<section class="section section--paper"><div class="container container--narrow">
  <div class="section-head section-head--center"><span class="eyebrow">Walkthrough</span>
  <h2 class="section-title">Video from site</h2><div class="rule"></div></div>
  {video(v['video'])}
</div></section>"""
        others = "".join(
            f'<a class="tile" href="{o["slug"]}.html">{img(o["hero"], "ph--3x4")}'
            f'<span class="tile__body"><span class="tile__label">{o["name"]}</span></span></a>'
            for o in VERTICALS if o["slug"] != v["slug"])
        paras = "".join(f"<p>{b}</p>" for b in v["body"])
        body = f"""
{banner(v['title'], f'Work / {v["name"]}', v['hero'], v['lede'])}
<section class="section"><div class="container split">
  <div class="split__media reveal">{img(v['gallery'][0])}</div>
  <div class="reveal" data-d="1">
    <span class="eyebrow">{v['name']} interiors</span>
    <h2 class="section-title">{v['lede']}</h2><div class="rule"></div>
    <div style="margin-top:22px">{paras}</div>
    <p class="cta__row"><button class="btn btn--primary" type="button" data-modal="work-{v['slug']}" data-modal-title="Start a {v['name'].lower()} project">Start a {v['name'].lower()} project</button></p>
  </div>
</div></section>
<section class="section section--paper"><div class="container">
  <div class="section-head section-head--center"><span class="eyebrow">Portfolio</span>
  <h2 class="section-title">{v['name']} projects</h2><div class="rule"></div></div>
  <div class="grid-gal">{grid}</div>
</div></section>
{vid}
{core_scope_block() if v['slug'] == 'residential' else ''}
{packages_block(heading=True) if v['slug'] == 'residential' else ''}
<section class="section"><div class="container">
  <div class="section-head section-head--center"><h2 class="section-title">Other sectors</h2><div class="rule"></div></div>
  <div class="tiles tiles--2">{others}</div>
</div></section>
{cta("Planning a " + v['name'].lower() + " project?",
     "Send the floor plan and your timeline. We will come back with a scope and a written estimate.",
     "work-cta-" + v['slug'])}
{consult()}"""
        page(f"work/{v['slug']}.html", f"{v['title']} — {v['name']} interior design | Feel The Space",
             v["lede"], body, og=v["hero"])


def build_areas():
    for slug, name, blurb in SERVICE_AREAS:
        depth(1)
        others = "".join(f'<li><a href="{s2}.html">{n2}</a></li>'
                         for s2, n2, _ in SERVICE_AREAS if s2 != slug)
        gal = ["res-living-dining-wide", "res-kitchen-island", "res-wardrobe-dresser",
               "off-workstations-row", "htl-suite-bed", "res-foyer-marble"]
        grid = "".join(f'<div class="reveal" data-d="{k%3}">{img(n)}</div>' for k, n in enumerate(gal))
        body = f"""
{banner(f"Interior designers in {name}", f"Areas / {name}", "res-living-dining-wide", blurb)}
<section class="section"><div class="container split">
  <div class="reveal">
    <span class="eyebrow">Delhi NCR</span>
    <h2 class="section-title">Interior design &amp; turnkey execution in {name}</h2><div class="rule"></div>
    <p style="margin-top:22px">{blurb}</p>
    <p>Our studio at Gaur City Mall covers {name} for residential, office and hospitality work. The engagement is the same wherever you are: a measured design phase at {DESIGN_FEE['rate']} per square foot, then Silver, Gold or Platinum execution once you have approved the 3D and signed the BOQ.</p>
    <p>Site visits, measurement and the first consultation are free. We will tell you honestly if your budget and your brief do not meet.</p>
    <ul class="contact-list">
      <li>{SVG['phone']}<a href="{tel()}">{BRAND['phone']}</a></li>
      <li>{SVG['pin']}<a href="{BRAND['maps']}" target="_blank" rel="noopener">{BRAND['address_l1']}</a></li>
    </ul>
    <p class="cta__row"><button class="btn btn--primary" type="button" data-modal="area-{slug}" data-modal-title="Book a consultation in {name}">Book a consultation in {name}</button></p>
  </div>
  <div class="split__media reveal" data-d="1">{img("res-living-panelled")}</div>
</div></section>
<section class="section section--paper"><div class="container">
  <div class="section-head section-head--center"><span class="eyebrow">Recent work</span>
  <h2 class="section-title">Projects across NCR</h2><div class="rule"></div></div>
  <div class="grid-gal">{grid}</div>
</div></section>
{packages_block(heading=True)}
<section class="section"><div class="container">
  <div class="section-head section-head--center"><h3>Other areas we serve</h3>
  <ul class="chiplist">{others}</ul></div>
</div></section>
{consult()}"""
        page(f"areas/{slug}.html", f"Interior designers in {name} | Feel The Space",
             f"Interior design and turnkey execution in {name}. Design at ₹150/sq. ft.; Silver, Gold and Platinum execution packages from our Greater Noida West studio.",
             body)


def build_gallery():
    depth(0)
    tabs, panes = "", ""
    for i, v in enumerate(VERTICALS):
        act = " is-active" if i == 0 else ""
        tabs += (f'<button class="tab{act}" type="button" role="tab" '
                 f'aria-selected="{"true" if i == 0 else "false"}" aria-controls="pane-{v["slug"]}" '
                 f'id="tab-{v["slug"]}">{v["name"]}</button>')
        items = "".join(f'<div class="reveal" data-d="{k%4}">{img(n)}</div>'
                        for k, n in enumerate([v["hero"]] + v["gallery"]))
        panes += (f'<div class="pane{act}" id="pane-{v["slug"]}" role="tabpanel" '
                  f'aria-labelledby="tab-{v["slug"]}"{"" if i == 0 else " hidden"}>'
                  f'<div class="grid-gal">{items}</div></div>')
    body = f"""
{banner("Gallery", "Gallery", "htl-lobby-chandelier",
        "Completed work, photographed on site. Nothing here is a stock image.")}
<section class="section"><div class="container">
  <div class="tabs" role="tablist" aria-label="Project categories">{tabs}</div>
  {panes}
</div></section>
<section class="section section--paper"><div class="container container--narrow">
  <div class="section-head section-head--center"><span class="eyebrow">Walkthroughs</span>
  <h2 class="section-title">Video from site</h2><div class="rule"></div></div>
  <div class="vidgrid">{video("res-walkthrough")}{video("res-kitchen-tour")}{video("htl-walkthrough")}</div>
</div></section>
{cta("Seen something you want in your space?",
     "Tell us which of these you liked and why. It is the fastest brief you can give a designer.",
     "gallery-cta")}
{consult()}"""
    page("gallery.html", "Project gallery | Feel The Space",
         "Completed residential, office and hospitality interiors by Feel The Space, photographed on site in Delhi NCR.",
         body, og="htl-lobby-chandelier")


def build_before_after():
    depth(0)
    cards = ""
    for i, pair in enumerate(BEFORE_AFTER):
        cards += f"""<div class="reveal" data-d="{i % 3}" style="margin-bottom:56px">
      {ba_slider(pair)}
      <p class="fineprint" style="margin-top:14px"><strong>{pair['title']}</strong> &mdash; {pair['where']}. {pair['note']}</p>
    </div>"""
    body = f"""
{banner("Before &amp; After", "Before &amp; After", "ba04-office-after",
        "Drag each slider to see the same space before we started and after handover. Every pair on this page is one of our own projects — no stock photography.")}
<section class="section"><div class="container container--narrow">
  {cards}
</div></section>
{cta("Want your own before &amp; after story?",
     "Send us your floor plan or site photos and we will walk you through what a full turnkey transformation would look like.",
     "before-after-cta")}
{consult()}"""
    page("before-after.html", "Before &amp; after gallery | Feel The Space",
         "Real before-and-after transformations from Feel The Space — kitchens, bedrooms, offices, corridors and living rooms across Delhi NCR.",
         body, "work", og="ba04-office-after")


def build_studio():
    depth(0)
    body = f"""
{banner("The studio", "Studio", "off-reception",
        "An interior design studio at Gaur City Mall, Greater Noida West.")}
{stats_block()}
<section class="section"><div class="container split">
  <div class="split__media reveal">{img("res-living-dining-wide")}</div>
  <div class="reveal" data-d="1">
    <span class="eyebrow">Who we are</span>
    <h2 class="section-title">Design and execution, under one roof</h2><div class="rule"></div>
    <p style="margin-top:22px">Feel The Space is an interior design studio based at Gaur City Mall in Greater Noida West. We design and execute interiors for homes, offices and hotels across Delhi NCR — and we do both halves ourselves, so there is no gap between the drawing and what gets built.</p>
    <p>Our pricing model is deliberately unusual for this industry. Design is quoted separately at {DESIGN_FEE['rate']} per square foot, so you can see exactly what the thinking costs. Execution is then quoted per square foot at one of three finish levels, and the exact figure is locked through a signed BOQ once you approve the 3D.</p>
    <p>That means no surprise numbers halfway through, and no pressure to commit to execution before you have seen what your space will look like.</p>
    <p class="cta__row"><a class="btn btn--ghost" href="{rel()}process.html">How we work</a></p>
  </div>
</div></section>
{phases_block(paper=True)}
{deliverables_block()}
<section class="section"><div class="container split split--rev">
  <div class="split__media reveal">{img("off-conference")}</div>
  <div class="reveal" data-d="1">
    <span class="eyebrow">Where we work</span>
    <h2 class="section-title">Across Delhi NCR</h2><div class="rule"></div>
    <p style="margin-top:22px">Greater Noida West is our home ground — Gaur City, Ek Murti and the surrounding societies are minutes from the studio. We also work throughout Noida, Greater Noida, Ghaziabad, Delhi and Gurugram.</p>
    <ul class="chiplist chiplist--left">{''.join(f'<li><a href="{rel()}areas/{s}.html">{n}</a></li>' for s, n, _ in SERVICE_AREAS)}</ul>
  </div>
</div></section>
{testimonials_block()}
{cta("Come and talk it through", "The first consultation, site visit and measurement are free.", "studio-cta")}
{consult()}"""
    page("studio.html", "About the studio | Feel The Space",
         "Feel The Space is an interior design studio at Gaur City Mall, Greater Noida West, delivering design and turnkey execution across Delhi NCR.",
         body, "studio", "off-reception")


def build_journal():
    depth(0)
    cards = "".join(f"""<a class="post reveal" data-d="{i%3}" href="journal/{s}.html">
      <div class="post__media">{img(im)}</div>
      <div class="post__body"><span class="post__date">{dt} &middot; {cat}</span>
      <h3>{t}</h3><p>{ex}</p></div></a>"""
      for i, (s, t, dt, cat, im, ex) in enumerate(POSTS))
    body = f"""
{banner("Journal", "Journal", "res-entrance-ceiling",
        "Notes on process, materials and pricing — written for people about to spend real money.")}
<section class="section"><div class="container"><div class="posts">{cards}</div></div></section>
{consult()}"""
    page("journal.html", "Journal | Feel The Space",
         "Notes on interior design process, materials, pricing and completed projects from the Feel The Space studio.",
         body, "journal", "res-entrance-ceiling")

    for i, (s, t, dt, cat, im, ex) in enumerate(POSTS):
        depth(1)
        more = "".join(
            f'<a class="post" href="{s2}.html"><div class="post__media">{img(im2)}</div>'
            f'<div class="post__body"><span class="post__date">{d2}</span><h3>{t2}</h3></div></a>'
            for s2, t2, d2, _, im2, _ in POSTS if s2 != s)
        body = f"""
{banner(t, f'<a href="../journal.html">Journal</a> / {cat}', im, ex)}
<section class="section"><div class="container container--narrow prose">
  <p class="post__date">{dt} &middot; {cat}</p>
  <p class="lede">{ex}</p>
  <p>This is a placeholder body for the article. Replace it with the real post — the template already handles headings, lists, images, pull quotes and the call to action below.</p>
  <h2>The short version</h2>
  <p>Open with the answer. Readers arriving from search want the conclusion first and the reasoning second, especially on pricing questions.</p>
  {img("res-living-panelled", "ph--16x9")}
  <h2>What it means in practice</h2>
  <p>Ground it in a real project. Specific numbers and named materials read as credible; adjectives do not. Reference the carpet area, the package level and the line items that actually moved the cost.</p>
  <ul>
    <li>Sainik 710 BWP for kitchen bases, Century MR for overheads</li>
    <li>Hettich soft-close hardware and InnoTech drawers throughout</li>
    <li>Cove and profile lighting planned on the RCP, not retrofitted</li>
  </ul>
  <blockquote>The exact figure is locked after 3D approval, through a signed BOQ. That document then governs the payment milestones.</blockquote>
  <h2>What we would tell a client</h2>
  <p>Close with the practical recommendation, then the call to action.</p>
  <p class="cta__row"><button class="btn btn--primary" type="button" data-modal="post-{s}" data-modal-title="Talk to the studio">Talk to the studio</button></p>
</div></section>
<section class="section section--paper"><div class="container">
  <div class="section-head section-head--center"><h2 class="section-title">More from the journal</h2><div class="rule"></div></div>
  <div class="posts">{more}</div>
</div></section>
{consult()}"""
        page(f"journal/{s}.html", f"{t} | Feel The Space", ex, body, og=im)


def build_faq_contact_sitemap():
    depth(0)
    body = f"""
{banner("Frequently asked questions", "FAQ", "res-crockery-niche",
        "Pricing, packages, materials and what happens when.")}
{faq_block()}
{cta("Still unsure about something?", "Ask the studio directly. No call centre, no obligation.",
     "faq-cta", "Ask a designer")}
{consult()}"""
    page("faq.html", "FAQ | Feel The Space",
         "Answers on the design fee, Silver/Gold/Platinum packages, GST, materials, BOQ locking and areas served.",
         body, og="res-crockery-niche")

    depth(0)
    body = f"""
{banner("Contact", "Contact", "res-foyer-marble", BRAND['tagline'])}
<section class="section"><div class="container consult__grid">
  <div>
    <span class="eyebrow">Get in touch</span>
    <h2 class="section-title">Tell us about the space</h2><div class="rule"></div>
    <p style="margin-top:22px">The fastest route is the form or WhatsApp — both reach the studio directly. Site visits, measurement and the first consultation are free.</p>
    <ul class="contact-list">
      <li>{SVG['phone']}<a href="{tel()}">{BRAND['phone']}</a></li>
      <li>{SVG['wa']}<a href="{wa()}" target="_blank" rel="noopener">WhatsApp the studio</a></li>
      <li>{SVG['mail']}<a href="mailto:{BRAND['email']}">{BRAND['email']}</a></li>
      <li>{SVG['pin']}<a href="{BRAND['maps']}" target="_blank" rel="noopener">{BRAND['address_l1']}<br>{BRAND['address_l2']}</a></li>
    </ul>
    <h3 style="margin-top:32px">Follow the work</h3>
    <p class="cta__row">
      <a class="btn btn--ghost" href="{BRAND['instagram']}" target="_blank" rel="noopener">Instagram</a>
      <a class="btn btn--ghost" href="{BRAND['facebook']}" target="_blank" rel="noopener">Facebook</a>
    </p>
  </div>
  <div>{form("contact", "Send enquiry")}</div>
</div>
<div class="container">{badges_block()}</div>
</section>
{calculator_block()}
{video_testimonials_block()}
{societies_block()}
<section class="section"><div class="container">
  <div class="section-head section-head--center"><span class="eyebrow">Visit</span>
  <h2 class="section-title">The studio</h2><div class="rule"></div></div>
  <div class="mapwrap">
    <iframe title="Feel The Space studio location" loading="lazy" referrerpolicy="no-referrer-when-downgrade"
      src="https://maps.google.com/maps?q=Gaur%20City%20Mall%20Greater%20Noida%20West&output=embed"></iframe>
  </div>
</div></section>"""
    page("contact.html", "Contact | Feel The Space",
         f"Call {BRAND['phone']}, WhatsApp or email the Feel The Space studio at Gaur City Mall, Greater Noida West.",
         body, "contact", "res-foyer-marble")

    depth(0)
    links = ['<li><a href="index.html">Home</a></li>']
    for t, u in [("Studio", "studio.html"), ("Services", "services.html"), ("Packages", "packages.html"),
                 ("Process", "process.html"), ("Gallery", "gallery.html"), ("Journal", "journal.html"),
                 ("FAQ", "faq.html"), ("Contact", "contact.html")]:
        links.append(f'<li><a href="{u}">{t}</a></li>')
    for v in VERTICALS:
        links.append(f'<li><a href="work/{v["slug"]}.html">{v["title"]} — {v["name"]}</a></li>')
    links.append('<li><a href="before-after.html">Before &amp; after</a></li>')
    for s, n, _ in SERVICE_AREAS:
        links.append(f'<li><a href="areas/{s}.html">Interior designers in {n}</a></li>')
    for s, t, _, _, _, _ in POSTS:
        links.append(f'<li><a href="journal/{s}.html">{t}</a></li>')
    body = f"""
{banner("Sitemap", "Sitemap", "res-corridor-mirror")}
<section class="section"><div class="container"><ul class="sitemap">{''.join(links)}</ul></div></section>"""
    page("sitemap.html", "Sitemap | Feel The Space", "Every page on the Feel The Space website.", body)


def build_extras():
    urls = ["index.html", "studio.html", "services.html", "packages.html", "process.html",
            "gallery.html", "before-after.html", "journal.html", "faq.html", "contact.html", "sitemap.html"]
    urls += [f"work/{v['slug']}.html" for v in VERTICALS]
    urls += [f"areas/{s}.html" for s, _, _ in SERVICE_AREAS]
    urls += [f"journal/{s}.html" for s, _, _, _, _, _ in POSTS]
    xml = "".join(f"<url><loc>{DOMAIN}{u}</loc></url>" for u in urls)
    write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>'
          f'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{xml}</urlset>')
    write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}sitemap.xml\n")
    return len(urls)


if __name__ == "__main__":
    build_home()
    build_packages()
    build_process()
    build_services()
    build_work()
    build_areas()
    build_gallery()
    build_before_after()
    build_studio()
    build_journal()
    build_faq_contact_sitemap()
    print("pages built:", build_extras())