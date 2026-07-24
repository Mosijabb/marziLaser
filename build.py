#!/usr/bin/env python3
"""
Static site generator — Marzi Laser, Kelowna.
No dependencies.  Run:  python3 build.py

Performance strategy:
  * style.css is INLINED into every page   -> zero render-blocking CSS requests
  * both variable fonts are self-hosted    -> zero third-party connections
  * icons are an inline SVG sprite         -> Font Awesome removed entirely
  * site.js is deferred                    -> never blocks parsing
"""
import os, re, json, datetime

# ---------------------------------------------------------------- config
SITE      = "https://lagom.bond"          # TEMPORARY host. One sed + rebuild to move.
BRAND     = "Marzi Skincare & Laser Clinic"
PHONE_H   = "(250) 215-4930"
PHONE_T   = "+12502154930"
PHONE_LD  = "+1-250-215-4930"
EMAIL     = "marzi@marskincare.ca"
ADDR      = "1856 Ambrosi Rd #120"
CITY      = "Kelowna"
LAT, LNG  = 49.8809093, -119.4501528       # verified pin
BOOK      = "https://www.vagaro.com/marziskincarecorp1"
HERO_IMG  = "https://marskincare.ca/wp-content/uploads/2026/03/Natural-beauty-with-Monstera-leaf.png.webp"
MAIN_SITE = "https://marskincare.ca/"
IG        = "https://www.instagram.com/marzi_skincare_laser_clinic/"
HERE      = os.path.dirname(os.path.abspath(__file__))
TODAY     = datetime.date.today().isoformat()

with open(os.path.join(HERE, "assets/css/style.css"), encoding="utf-8") as f:
    CSS = f.read()

NAV = [("/", "Home"), ("/pricing", "Pricing"), ("/how-it-works", "How It Works"),
       ("/alpha-pro-laser", "The Laser"), ("/faq", "FAQ"), ("/about", "About"), ("/contact", "Contact")]
AREAS = [("/brazilian-bikini-laser-hair-removal-kelowna", "Brazilian &amp; Bikini"),
         ("/full-body-laser-hair-removal-kelowna", "Full Body"),
         ("/facial-laser-hair-removal-kelowna", "Face, Lip &amp; Chin"),
         ("/mens-laser-hair-removal-kelowna", "Men's Laser Hair Removal")]

# ---------------------------------------------------------------- icons
_P = {
 "phone":'<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2 4.2 2 2 0 0 1 4 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.1a2 2 0 0 1 2.1-.5c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/>',
 "menu":'<path d="M3 6h18M3 12h18M3 18h18"/>',
 "down":'<path d="m6 9 6 6 6-6"/>',
 "check":'<path d="M20 6 9 17l-5-5"/>',
 "right":'<path d="M5 12h14M12 5l7 7-7 7"/>',
 "ig":'<rect x="2" y="2" width="20" height="20" rx="5"/><path d="M16 11.4A4 4 0 1 1 12.6 8 4 4 0 0 1 16 11.4z"/><path d="M17.5 6.5h.01"/>',
 "mail":'<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/>',
 "pin":'<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/>',
 "clock":'<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
 "cal":'<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/>',
 "shield":'<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/>',
 "spark":'<path d="M12 3v3M12 18v3M5.6 5.6l2.1 2.1M16.3 16.3l2.1 2.1M3 12h3M18 12h3M5.6 18.4l2.1-2.1M16.3 7.7l2.1-2.1"/><circle cx="12" cy="12" r="3"/>',
 "user":'<path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/>',
 "tag":'<path d="M20.6 13.4 12 22l-9-9V3h10l7.6 7.6a2 2 0 0 1 0 2.8z"/><path d="M7 7h.01"/>',
 "chat":'<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>',
 "leaf":'<path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.5 19 2c1 2 2 4.2 2 8 0 5.5-4.8 10-10 10z"/><path d="M2 21c0-3 1.9-5.7 4.5-7"/>',
 "zap":'<path d="M13 2 3 14h9l-1 8 10-12h-9l1-8z"/>',
 "shirt":'<path d="M20.4 6.5 16 4a4 4 0 0 1-8 0L3.6 6.5a1 1 0 0 0-.4 1.3l1.8 3.6a1 1 0 0 0 1.3.4l1.2-.6V20a1 1 0 0 0 1 1h7a1 1 0 0 0 1-1v-8.8l1.2.6a1 1 0 0 0 1.3-.4l1.8-3.6a1 1 0 0 0-.4-1.3z"/>',
 "star":'<path d="m12 2 3.1 6.3 6.9 1-5 4.9 1.2 6.8L12 17.8 5.8 21l1.2-6.8-5-4.9 6.9-1z"/>',
}
SPRITE = '<svg xmlns="http://www.w3.org/2000/svg" style="display:none" aria-hidden="true">' + "".join(
    f'<symbol id="i-{k}" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
    f'stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round">{v}</symbol>'
    for k, v in _P.items()) + "</svg>"


def ic(name, cls=""):
    c = f' class="{cls}"' if cls else ""
    return f'<svg{c} aria-hidden="true"><use href="#i-{name}"/></svg>'


# ---------------------------------------------------------------- head
def head(title, desc, path, ld=None, img=None, page_type="WebPage"):
    url = SITE + path
    img = img or HERO_IMG
    ldjs = ""
    if ld:
        ldjs = '<script type="application/ld+json">%s</script>' % json.dumps(ld, separators=(",", ":"))
    return f"""<!DOCTYPE html>
<html lang="en-CA">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1">
<meta name="theme-color" content="#FBF9F5">
<meta name="geo.region" content="CA-BC">
<meta name="geo.placename" content="Kelowna, British Columbia">
<meta name="geo.position" content="{LAT};{LNG}">
<meta name="ICBM" content="{LAT}, {LNG}">
<meta property="og:type" content="website">
<meta property="og:locale" content="en_CA">
<meta property="og:site_name" content="Marzi Laser Kelowna">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{img}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{img}">
<link rel="preconnect" href="https://marskincare.ca" crossorigin>
<link rel="preload" href="/assets/fonts/inter.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/fraunces.woff2" as="font" type="font/woff2" crossorigin>
<link rel="icon" href="/assets/img/favicon.svg" type="image/svg+xml">
<style>{CSS}</style>
{ldjs}
</head>
<body>
<a href="#main" class="skip">Skip to content</a>
{SPRITE}
"""


# ---------------------------------------------------------------- nav
def nav(cur):
    out = ""
    for href, label in NAV:
        if href == "/pricing":
            sub = "".join(f'<a href="{h}">{l}</a>' for h, l in AREAS)
            out += ('<div class="drop"><button type="button" aria-haspopup="true">Treatment Areas '
                    + ic("down") + f'</button><div class="drop-menu">{sub}</div></div>')
        a = ' aria-current="page"' if href == cur else ""
        out += f'<a href="{href}"{a}>{label}</a>'
    sheet = "".join(f'<a href="{h}">{l}</a>' for h, l in AREAS)
    sheet += "".join(f'<a href="{h}">{l}</a>' for h, l in NAV if h != "/")
    return f"""<nav class="nav" aria-label="Main">
<div class="container nav-in">
<a href="/" class="brand">Marzi Laser<em>Kelowna, BC</em></a>
<div class="nav-links">{out}</div>
<div class="nav-right">
<a href="tel:{PHONE_T}" class="nav-tel">{ic('phone')}{PHONE_H}</a>
<a href="{BOOK}" class="btn btn-primary btn-sm" rel="noopener" target="_blank">Book online</a>
<button class="burger" aria-label="Menu" aria-expanded="false" aria-controls="sheet">{ic('menu')}</button>
</div></div></nav>
<div class="sheet" id="sheet"><div class="container">
<a href="/">Home</a>{sheet}
<a href="{BOOK}" class="btn btn-primary btn-block" rel="noopener" target="_blank">{ic('cal')} Book online</a>
<a href="tel:{PHONE_T}" class="btn btn-ghost btn-block" style="margin-top:.6rem">{ic('phone')} {PHONE_H}</a>
</div></div>
<main id="main">"""


# ---------------------------------------------------------------- footer
FOOT = f"""</main>
<footer class="foot"><div class="container">
<div class="foot-grid">
  <div>
    <a href="/" class="brand">Marzi Laser<em>Kelowna, BC</em></a>
    <p class="muted" style="margin-top:.9rem;max-width:32ch">Laser hair removal in Kelowna with the Alpha&nbsp;Pro
    diode laser. Safe for every skin tone. Every treatment performed personally by Marzi Salehi.</p>
    <div class="foot-social">
      <a href="{IG}" rel="noopener" target="_blank" aria-label="Instagram">{ic('ig')}</a>
      <a href="tel:{PHONE_T}" aria-label="Phone">{ic('phone')}</a>
      <a href="mailto:{EMAIL}" aria-label="Email">{ic('mail')}</a>
    </div>
  </div>
  <div><h3>Treatment areas</h3><ul>
    <li><a href="/brazilian-bikini-laser-hair-removal-kelowna">Brazilian &amp; Bikini</a></li>
    <li><a href="/full-body-laser-hair-removal-kelowna">Full Body</a></li>
    <li><a href="/facial-laser-hair-removal-kelowna">Face, Lip &amp; Chin</a></li>
    <li><a href="/mens-laser-hair-removal-kelowna">Men's Laser</a></li>
  </ul></div>
  <div><h3>Learn</h3><ul>
    <li><a href="/pricing">Pricing</a></li>
    <li><a href="/how-it-works">How it works</a></li>
    <li><a href="/alpha-pro-laser">The Alpha Pro laser</a></li>
    <li><a href="/faq">FAQ</a></li>
    <li><a href="/about">About Marzi</a></li>
  </ul></div>
  <div><h3>Visit</h3><ul>
    <li>{ADDR}<br>{CITY}, BC</li>
    <li><a href="tel:{PHONE_T}">{PHONE_H}</a></li>
    <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
    <li style="margin-top:.4rem">Mon, Tue, Thu 9–17<br>Wed 10:30–18:30<br>Fri 11–19 · Sat–Sun 11–16</li>
  </ul></div>
</div>
<hr class="spectrum" style="margin-bottom:1.25rem">
<div class="foot-bot"><p>&copy; <span data-year>2026</span> Marzi Skincare &amp; Laser Clinic, Kelowna BC ·
Facials, peels and skin treatments at <a href="{MAIN_SITE}" rel="noopener">marskincare.ca</a></p></div>
</div></footer>
<div class="bar">
  <a href="tel:{PHONE_T}" class="btn btn-ghost">{ic('phone')} Call</a>
  <a href="{BOOK}" class="btn btn-primary" rel="noopener" target="_blank">{ic('cal')} Book online</a>
</div>
<script src="/assets/js/site.js" defer></script>
</body></html>"""


# ---------------------------------------------------------------- helpers
def crumbs(items):
    li, ld = "", []
    for i, (href, label) in enumerate(items, 1):
        li += f'<li><a href="{href}">{label}</a></li>' if href else f'<li><span aria-current="page">{label}</span></li>'
        e = {"@type": "ListItem", "position": i, "name": label.replace("&amp;", "&")}
        if href:
            e["item"] = SITE + href
        ld.append(e)
    return (f'<nav class="crumbs" aria-label="Breadcrumb"><ol>{li}</ol></nav>'
            '<script type="application/ld+json">%s</script>'
            % json.dumps({"@context": "https://schema.org", "@type": "BreadcrumbList",
                          "itemListElement": ld}, separators=(",", ":")))


def faq_block(items, open_first=False):
    out = '<div class="faq rv"%s>' % (" data-open-first" if open_first else "")
    for q, paras in items:
        uid = re.sub(r"[^a-z0-9]+", "-", q.lower()).strip("-")[:38]
        body = "".join(f"<p>{p}</p>" for p in paras)
        out += (f'<div class="fq"><button class="fq-q" aria-expanded="false" aria-controls="a-{uid}" '
                f'id="q-{uid}">{q}</button><div class="fq-a" id="a-{uid}" role="region" '
                f'aria-labelledby="q-{uid}"><div>{body}</div></div></div>')
    return out + "</div>"


def faq_ld(items):
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q.replace("&amp;", "&"),
                            "acceptedAnswer": {"@type": "Answer",
                                               "text": re.sub(r"<[^>]+>", "", " ".join(p)).replace("&amp;", "&")}}
                           for q, p in items]}


CLINIC_REF = {"@id": SITE + "/#clinic"}


def service_ld(name, desc, path, price=None):
    d = {"@context": "https://schema.org", "@type": "Service", "@id": SITE + path + "#service",
         "serviceType": name, "name": name, "description": desc, "url": SITE + path,
         "provider": CLINIC_REF, "brand": {"@type": "Brand", "name": "Alpha Pro Diode Laser"},
         "areaServed": [{"@type": "City", "name": c} for c in
                        ["Kelowna", "West Kelowna", "Lake Country", "Peachland", "Vernon", "Penticton"]]}
    if price:
        d["offers"] = {"@type": "Offer", "priceCurrency": "CAD", "price": str(price),
                       "availability": "https://schema.org/InStock", "url": BOOK,
                       "priceValidUntil": f"{datetime.date.today().year + 1}-12-31"}
    return d


def write(path, html):
    fn = "index.html" if path == "/" else path.strip("/") + ".html"
    with open(os.path.join(HERE, fn), "w", encoding="utf-8") as f:
        f.write(html)
    return fn, len(html)


def page(path, title, desc, body, ld=None, cur=None, img=None):
    fn, n = write(path, head(title, desc, path, ld, img) + nav(cur or path) + body + FOOT)
    print(f"  {fn:<50}{n/1024:6.1f} KB")


# ---------------------------------------------------------------- extras
def extras():
    urls = [(p, "1.0" if p == "/" else "0.9" if p in
             ("/pricing", "/brazilian-bikini-laser-hair-removal-kelowna",
              "/full-body-laser-hair-removal-kelowna", "/facial-laser-hair-removal-kelowna",
              "/mens-laser-hair-removal-kelowna") else "0.8" if p in ("/faq", "/how-it-works", "/contact") else "0.7")
            for p, _ in NAV] + [(p, "0.9") for p, _ in AREAS]
    seen, rows = set(), []
    for p, pr in urls:
        if p in seen:
            continue
        seen.add(p)
        rows.append(f"<url><loc>{SITE}{p}</loc><lastmod>{TODAY}</lastmod>"
                    f"<changefreq>monthly</changefreq><priority>{pr}</priority></url>")
    open(os.path.join(HERE, "sitemap.xml"), "w").write(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(rows) + "\n</urlset>\n")

    bots = ["GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-Web", "anthropic-ai",
            "PerplexityBot", "Perplexity-User", "Google-Extended", "Applebot", "Applebot-Extended",
            "Bingbot", "CCBot", "cohere-ai", "Amazonbot", "meta-externalagent", "DuckAssistBot"]
    open(os.path.join(HERE, "robots.txt"), "w").write(
        "User-agent: *\nAllow: /\n\n# Answer engines welcome\n"
        + "".join(f"User-agent: {b}\nAllow: /\n\n" for b in bots)
        + f"Sitemap: {SITE}/sitemap.xml\n")

    open(os.path.join(HERE, "_headers"), "w").write(f"""/*
  X-Content-Type-Options: nosniff
  X-Frame-Options: SAMEORIGIN
  Referrer-Policy: strict-origin-when-cross-origin
  Permissions-Policy: geolocation=(), microphone=(), camera=(), interest-cohort=()
  Strict-Transport-Security: max-age=31536000; includeSubDomains

/assets/fonts/*
  Cache-Control: public, max-age=31536000, immutable
  Access-Control-Allow-Origin: *

/assets/*
  Cache-Control: public, max-age=31536000, immutable

/*.html
  Cache-Control: public, max-age=0, must-revalidate
""")

    open(os.path.join(HERE, "_redirects"), "w").write("""/index.html   /                                              301
/brazilian    /brazilian-bikini-laser-hair-removal-kelowna   301
/bikini       /brazilian-bikini-laser-hair-removal-kelowna   301
/full-body    /full-body-laser-hair-removal-kelowna          301
/mens         /mens-laser-hair-removal-kelowna               301
/men          /mens-laser-hair-removal-kelowna               301
/face         /facial-laser-hair-removal-kelowna             301
/prices       /pricing                                       301
/cost         /pricing                                       301
/book         /contact                                       301
/contacts     /contact                                       301
""")
    print("  sitemap.xml · robots.txt · _headers · _redirects")


if __name__ == "__main__":
    import pages
    print("Building Marzi Laser Kelowna…")
    pages.build(globals())
    extras()
    print("Done.")
