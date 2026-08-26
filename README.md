# Feel The Space — Interior Design Studio

25 pages, static, no build step needed to view. Open `index.html`.

Content, pricing and scope are taken from the studio's 2026 client proposal.
All photography is the studio's own project work.

## Structure
```
index.html               Home
studio.html              About the studio
services.html            6 services, anchor-linked (#space-planning etc.)
packages.html            Silver / Gold / Platinum + design fee + BOQ + terms
process.html             Three phases, deliverables, BOQ locking, next steps
gallery.html             Tabbed gallery (Residential / Office / Hospitality) + videos
journal.html + journal/  6 posts
work/*.html              3 verticals: residential, office, hospitality
areas/*.html             6 NCR areas
faq.html contact.html sitemap.html
assets/css/style.css     All styling — design tokens at the top
assets/js/main.js        All behaviour, 16 modules, zero dependencies
assets/img/              41 project photos + 3 video posters
assets/video/            3 compressed walkthrough clips
build/data.py            ALL content: brand, packages, scope, FAQs, areas, alt text
build/build.py           Generator — rebuilds every page from data.py
```

## Editing
- **Phone, email, address, social links** → `BRAND` in `build/data.py`. One edit
  updates the top bar, drawer, rail, footer, contact page and schema.org markup.
- **Package rates and scope** → `PACKAGES`. **Design fee** → `DESIGN_FEE`.
- **Core base scope, materials, terms, FAQs, areas** → their own lists in `data.py`.
- **Colours and type** → `:root` in `assets/css/style.css`.
- After any change: `cd build && python3 build.py`

## Design
The original v1 visual system: deep green-black + brass on bone, Fraunces display
with Manrope body, 4px radii. Tokens live in `:root` at the top of style.css.

## Logo
`assets/img/` holds the brand artwork, background removed and trimmed:
`logo-horizontal.png` (header/drawer), `logo-horizontal-light.png` (dark footer),
`logo.png` (stacked lockup), `logo-mark.png` (arch only), `logo-word.png` (wordmark),
and `favicon-32/180/512.png`. Swap the file to change the logo — no code edits needed.

## Media
41 photos, EXIF-rotated, resized to 1600px, progressive JPEG. Three walkthrough
videos trimmed to 18s, 720p, H.264 with `+faststart`, ~1.2 MB total. Videos are
`preload="none"` with poster frames, so they cost nothing until played.

To add photos: drop the file in `assets/img/`, add an entry to `ALT` in
`data.py` (filename stem → alt text), then reference it in `VERTICALS`,
`SERVICES` or `POSTS`.

## Connecting the forms
`assets/js/main.js`, module 11 — uncomment the `fetch('/api/enquiry')` line and
delete the `setTimeout` stub. Every form posts a hidden `source` field naming the
CTA that opened it, plus carpet area and package interest, so enquiries arrive
pre-qualified.

## SEO
`LocalBusiness`/`InteriorDesigner` JSON-LD on every page with the real NAP,
areas served and social profiles. Canonicals, OG tags, `sitemap.xml`, `robots.txt`.
Update `DOMAIN` in `build.py` if the live domain differs from feelthespace.in.

## Interactions
Sticky header · marquee · hover-intent dropdowns · mobile drawer with accordions ·
hero crossfade carousel (autoplay, arrows, dots, swipe) · draggable content
carousels · package panels with `#hash` deep-linking · gallery tabs with arrow-key
support · focus-trapped modal · client-side validation + honeypot · scroll reveals ·
animated process timeline · floating action rail. All gated behind
`prefers-reduced-motion`.
