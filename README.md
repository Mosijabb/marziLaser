# Marzi Laser — Kelowna

Static HTML. No npm, no framework, no build step needed to deploy.
`build.py` exists only so the nav, footer, schema and CSS stay in sync when you edit content.

Currently live at **lagom.bond** (temporary).

---

## What changed in this rebuild

### Performance — the 3,690 ms problem is gone

Measured in headless Chrome on the built files:

| | Before | Now |
|---|---|---|
| Render-blocking requests | 3 (~3,690 ms) | **0** |
| First Contentful Paint | — | **192 ms** |
| Total requests | ~12 | **4** |
| Third-party connections | 2 (Google Fonts, cdnjs) | **1** (the hero image only) |

What did it:

1. **Font Awesome deleted.** It was ~35 KB and a blocking request for about a dozen icons.
   Replaced with an inline SVG sprite — 17 icons, ~2 KB, zero requests.
2. **Google Fonts deleted.** Fraunces and Inter are now self-hosted variable fonts
   (`assets/fonts/`, 88 KB total for *every* weight), preloaded with `font-display: swap`.
   No DNS lookup, no third-party CSS, no FOIT.
3. **CSS inlined** into every page's `<head>`. Gzips to ~4 KB inside the HTML, so pages land
   at 10–15 KB gzipped total. That removes the last blocking request.
4. **JS rewritten** — 2.4 KB, deferred. The old mouse-parallax loop read `window.innerWidth`
   on every mousemove, which is what caused your *forced reflow* warning. That code is gone.
5. **LCP hinted properly** — hero image has `fetchpriority="high"`, explicit `width`/`height`
   (no layout shift), and a `preconnect` to marskincare.ca.

### The remaining performance item — one thing left for you

The hero image still loads from `marskincare.ca`. It's your LCP element, so a cross-origin
request costs a DNS lookup + TLS handshake before it can even start. **Download it and put it
in `assets/img/`**, then change `HERO_IMG` in `build.py` to `/assets/img/hero.webp`:

```bash
curl -o assets/img/hero.webp "https://marskincare.ca/wp-content/uploads/2026/03/Natural-beauty-with-Monstera-leaf.png.webp"
# then edit HERO_IMG in build.py, and:
python3 build.py
```

That's the last third-party request on the site. After it, PageSpeed has nothing left to flag.

### Design — new direction

You asked for something better suited to a laser clinic. The old dark plum + champagne gold +
glassmorphism read *luxury spa / nightclub*, and dark glassmorphism is also the single most
recognisable "AI-generated site" look right now — bad for a showcase piece.

**New direction: warm clinical.**

- **Light bone base** (`#FBF9F5`) instead of near-black. Medical aesthetics converts better on
  light: it shows skin and rooms rather than hiding them, and it reads as clinic rather than bar.
- **Deep petrol** (`#0D4A50`) as the single brand colour. Teal reads medical; the pink/gold
  family reads nail salon. One colour, used with discipline.
- **Fraunces + Inter**, both variable. Fraunces has warmth and character without being
  Playfair or Cormorant, which every aesthetics site already uses.
- **Signature element: the Fitzpatrick spectrum.** The six-tone gradient rule that runs through
  the site as section dividers *is* the interactive skin-type selector's palette. It's the
  clinic's actual differentiator — treating all six types — rendered as the brand's visual
  system. Nothing generic about it, and it comes from the subject rather than from a trend.

Every text/background pair on the site passes **WCAG AA** (lowest is 4.91:1).

### Content & data corrections

- **Coordinates fixed** to `49.8809093, -119.4501528` everywhere (meta, schema, map embed,
  directions link).
- **Vagaro booking wired in** — `https://www.vagaro.com/marziskincarecorp1` is now the primary
  CTA in the nav, hero, sticky mobile bar, every area page, every CTA band, and the contact page.
  It's also in schema as a `ReserveAction`, so Google can surface a booking action.
- **Hero image** is now the Monstera-leaf shot from marskincare.ca.
- **No lagomium.com references anywhere.** All canonicals, OG tags and schema point at `lagom.bond`.

### SEO / AEO

- 12 pages, **11,283 words**, all unique, none copied from marskincare.ca.
- Unique titles (50–60 chars) and descriptions (145–165) on every page.
- Canonicals, breadcrumbs, OG + Twitter cards, geo meta, `theme-color`.
- **25 schema types** across the site: MedicalBusiness, MedicalProcedure, Person, Service,
  Product, HowTo, FAQPage (×6 pages), BreadcrumbList, ReserveAction, SpeakableSpecification,
  OpeningHoursSpecification, Offer, GeoCoordinates and more.
- Every page opens with a bordered **Quick answer** block — a self-contained 40–70 word factual
  paragraph. That's the exact shape featured snippets and LLMs extract.
- `llms.txt` gives answer engines a clean structured summary of NAP, pricing and key facts.
- `robots.txt` explicitly allows 17 AI crawlers (GPTBot, ClaudeBot, PerplexityBot, etc.).
- FAQ answers stay in the DOM when collapsed, so crawlers read all of them.
- Pricing is real `<table>` markup, not divs — parseable.

**On Deepseek's "single-page website" comment:** it's wrong. The site has 12 pages with a full
internal link graph. Deepseek almost certainly only fetched the homepage. Don't act on that
part of its review — the rest of its list was reasonable and is now handled.

**Deliberately still omitted: AggregateRating schema.** Self-serving review markup on a
LocalBusiness violates Google's guidelines and risks a manual action, and there's no real
review count to use. Link the actual Google reviews once the GBP is sorted instead.

---

## ⚠️ Before this goes to a real domain

**1. Verify every price with Marzi.** Only upper lip ($80 / $210) and full face ($225 / $615)
came from the original site audit. Everything else is a plausible ladder built from those two
anchors and Kelowna market rates. They are placeholders. Prices live in `pages.py` and `llms.txt`.

**2. Change the domain.** One command, then rebuild:

```bash
grep -rl "lagom.bond" . | xargs sed -i 's|lagom\.bond|YOURDOMAIN.ca|g'
python3 build.py
```

**3. Self-host the hero image** (see above) and add `assets/img/og-laser-hair-removal-kelowna.jpg`
at 1200×630 for social previews — it's referenced but not present.

**4. Add real photos.** Marzi at work, the treatment room, the Alpha Pro machine. Real clinic
photography beats stock on both conversion and local ranking, and this design is built to show
photography rather than hide it.

**5. Confirm the contact form.** FormSubmit sends a one-time activation email to
`marzi@marskincare.ca` that must be clicked before the form works.

**6. Add the postal code.** I left it out of the schema rather than guess. Add it to the
`address` block in `build.py` (`CLINIC` dict in `pages.py`).

---

## The strategic thing worth deciding

For "laser hair removal kelowna" the **map pack sits above organic results**, and the Google
Business Profile accepts exactly **one** website URL. Whichever site that points at gets the
local-pack traffic — and that single decision will likely outweigh everything on this site.

My read: point the GBP here *if* laser growth is the priority, since this is the better
converting landing page for that intent, and add marskincare.ca as the URL on the individual
"Facial" and skincare service items inside the profile. But it's a real trade-off and worth a
conversation with Marzi rather than a unilateral switch.

Also worth knowing: Google treats multiple sites for one business as a doorway pattern *when
the content is thin or duplicated*. This site avoids that — 11,283 unique words, all narrowly
about laser, nothing copied. Keep it that way: marskincare.ca targets facials and skincare,
this one targets laser only.

---

## Files

```
index.html                                        Laser Hair Removal Kelowna  (primary target)
pricing.html                                      cost / price queries — highest commercial intent
brazilian-bikini-laser-hair-removal-kelowna.html
full-body-laser-hair-removal-kelowna.html
facial-laser-hair-removal-kelowna.html            includes PCOS / hormonal hair
mens-laser-hair-removal-kelowna.html              includes razor bumps / PFB
how-it-works.html                                 informational, HowTo schema
alpha-pro-laser.html                              tech differentiator, Product schema
faq.html                                          20 Q&As — the main AEO asset
about.html                                        E-E-A-T (this is YMYL content, it matters)
contact.html                                      NAP, hours, map, Vagaro, form
404.html
robots.txt  sitemap.xml  llms.txt  _headers  _redirects
assets/css/style.css      source of the inlined CSS — edit here, then rebuild
assets/js/site.js         2.4 KB, deferred
assets/fonts/*.woff2      self-hosted variable fonts
build.py                  head, nav, footer, schema helpers, sitemap/robots generation
pages.py                  ALL page content — this is the file you edit
```

## Editing

Content is in `pages.py`. Layout, nav, footer and schema helpers are in `build.py`.
CSS is in `assets/css/style.css` and gets inlined at build time — **you must rebuild after
editing CSS**, or the change won't appear.

```bash
python3 build.py
```

Deploy the folder root. `_headers` and `_redirects` are Cloudflare Pages conventions.

## Local testing

```bash
python3 -m http.server 8000
```

Then open `http://localhost:8000`.

## After launch

1. Google Search Console — verify, submit `sitemap.xml`, request indexing on `/` and `/pricing`.
2. Bing Webmaster Tools — same. Bing feeds ChatGPT search, so it matters for AEO now.
3. Rich Results Test on `/`, `/faq` and `/how-it-works`.
4. Add Google Analytics or Plausible — currently there's no tracking at all, which is why
   Deepseek flagged it. One script tag in `build.py`'s `head()` covers all 12 pages.
5. Local citations with the *exact* same NAP string: Yelp, Yellow Pages CA, Apple Business
   Connect, Bing Places, Facebook. Consistency is the ranking factor — copy-paste, don't retype.
6. Ask clients for Google reviews that naturally use "laser hair removal" and "Kelowna".

---

**English note:** you wrote *"i uploaded the whole marzi new website on lagom.bond"* — that
should be *"to lagom.bond"*. Uploading takes *to* (destination), not *on*. Same pattern in
*"put it on cloudflare"*, which is fine, because there *on* means "hosted on a platform"
rather than a transfer. The rule: *upload/send/move* → **to**; *host/run/store* → **on**.
