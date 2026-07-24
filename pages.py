# -*- coding: utf-8 -*-
"""Content for Marzi Laser Kelowna. Imported by build.py."""


def build(B):
    page, crumbs, faq_block, faq_ld, service_ld, ic = (
        B["page"], B["crumbs"], B["faq_block"], B["faq_ld"], B["service_ld"], B["ic"])
    SITE, BOOK, HERO_IMG = B["SITE"], B["BOOK"], B["HERO_IMG"]
    LAT, LNG, PHONE_T, PHONE_H = B["LAT"], B["LNG"], B["PHONE_T"], B["PHONE_H"]

    # ------------------------------------------------------------------ shared
    BAND = f"""
<section class="tight"><div class="container"><div class="band rv">
  <p class="eyebrow">New clients</p>
  <h2>50% off your first laser session.</h2>
  <p>Consultation and patch test are free. Book online any time, or call the clinic — 1856 Ambrosi Rd&nbsp;#120,
  just off Highway&nbsp;97 in central Kelowna.</p>
  <div class="band-cta">
    <a href="{BOOK}" class="btn btn-light" rel="noopener" target="_blank">{ic('cal')} Book online</a>
    <a href="tel:{PHONE_T}" class="btn btn-ghost" style="color:#fff;border-color:rgba(255,255,255,.35)">{ic('phone')} {PHONE_H}</a>
  </div>
</div></div></section>"""

    def phero(crumb_items, eyebrow, h1, lede, answer):
        return f"""<header class="phero"><div class="container">
{crumbs(crumb_items)}
<div class="rv">
  <p class="eyebrow">{eyebrow}</p>
  <h1>{h1}</h1>
  <p class="lede">{lede}</p>
  <div class="answer"><span class="lbl">Quick answer</span><p>{answer}</p></div>
</div></div></header>"""

    CLINIC = {
        "@type": ["MedicalBusiness", "HealthAndBeautyBusiness", "LocalBusiness"],
        "@id": SITE + "/#clinic",
        "name": "Marzi Skincare & Laser Clinic",
        "alternateName": "Marzi Laser Kelowna",
        "description": "Laser hair removal clinic in Kelowna, BC using the Alpha Pro 808 nm diode laser. "
                       "Safe for Fitzpatrick skin types I–VI. Every treatment performed personally by "
                       "Marzi Salehi, a certified medical aesthetician with 22+ years of experience.",
        "url": SITE + "/",
        "telephone": B["PHONE_LD"], "email": B["EMAIL"], "image": HERO_IMG,
        "priceRange": "$$", "currenciesAccepted": "CAD",
        "paymentAccepted": "Cash, Debit, Credit Card",
        "address": {"@type": "PostalAddress", "streetAddress": B["ADDR"], "addressLocality": "Kelowna",
                    "addressRegion": "BC", "addressCountry": "CA"},
        "geo": {"@type": "GeoCoordinates", "latitude": LAT, "longitude": LNG},
        "hasMap": f"https://www.google.com/maps/search/?api=1&query={LAT},{LNG}",
        "areaServed": [{"@type": "City", "name": c} for c in
                       ["Kelowna", "West Kelowna", "Lake Country", "Peachland", "Vernon", "Penticton"]],
        "openingHoursSpecification": [
            {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Thursday"],
             "opens": "09:00", "closes": "17:00"},
            {"@type": "OpeningHoursSpecification", "dayOfWeek": "Wednesday", "opens": "10:30", "closes": "18:30"},
            {"@type": "OpeningHoursSpecification", "dayOfWeek": "Friday", "opens": "11:00", "closes": "19:00"},
            {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Saturday", "Sunday"],
             "opens": "11:00", "closes": "16:00"}],
        "sameAs": [B["IG"], B["MAIN_SITE"]],
        "founder": {"@id": SITE + "/about#marzi"},
        "employee": {"@id": SITE + "/about#marzi"},
        "potentialAction": {"@type": "ReserveAction", "target": {
            "@type": "EntryPoint", "urlTemplate": BOOK,
            "actionPlatform": ["https://schema.org/DesktopWebPlatform", "https://schema.org/MobileWebPlatform"]}},
        "makesOffer": [
            {"@type": "Offer", "priceCurrency": "CAD", "price": "80",
             "itemOffered": {"@type": "Service", "name": "Upper lip laser hair removal"}},
            {"@type": "Offer", "priceCurrency": "CAD", "price": "95",
             "itemOffered": {"@type": "Service", "name": "Underarm laser hair removal"}},
            {"@type": "Offer", "priceCurrency": "CAD", "price": "180",
             "itemOffered": {"@type": "Service", "name": "Brazilian laser hair removal"}},
            {"@type": "Offer", "priceCurrency": "CAD", "price": "290",
             "itemOffered": {"@type": "Service", "name": "Full leg laser hair removal"}}],
    }

    # ================================================================== HOME
    home_faqs = [
        ("How much does laser hair removal cost in Kelowna?",
         ["Single sessions at Marzi Skincare &amp; Laser Clinic start at <strong>$80</strong> for the upper lip and "
          "<strong>$225</strong> for a full face. Underarms are $95, Brazilian $180 and full legs $290. Packages of "
          "three are discounted, and first-time laser clients receive 50% off their first session.",
          "Across Kelowna, expect roughly $70–$120 per session for small areas and $250–$400 for large ones. Judge "
          "cost by the full course rather than the session — a cheap session on an underpowered machine usually "
          "means more sessions overall. <a href='/pricing'>See the full price list</a>."]),
        ("How many sessions will I need?",
         ["Most people need <strong>6 to 10 sessions</strong>, spaced 4 to 8 weeks apart. Hair grows in cycles and a "
          "laser only disables follicles in the active growth phase on the day you are treated, which is why one "
          "session can never do it all.",
          "Coarse dark hair on underarms and the bikini line clears fastest. Fine facial hair and hormone-driven "
          "growth usually need more sessions plus occasional maintenance."]),
        ("Is laser hair removal safe for dark or tanned skin?",
         ["Yes. The Alpha Pro is an <strong>808&nbsp;nm diode laser</strong> with sapphire contact cooling, which makes "
          "it safe across <strong>Fitzpatrick I–VI</strong>, including brown and Black skin. Deeper tones are treated "
          "with lower fluence and longer pulse widths so the follicle heats while surrounding pigment stays protected.",
          "A patch test is performed on every new client before a full session."]),
        ("Does it hurt?",
         ["Most clients describe a warm snap rather than pain. The cooling tip chills the skin before and after each "
          "pulse, and Power Motion Technology moves in continuous passes rather than single high-energy shots, which "
          "spreads the sensation out. Underarms and Brazilian are the most sensitive; arms and legs are usually very "
          "comfortable. Nearly everyone finds it easier than waxing."]),
        ("How do I prepare for my appointment?",
         ["<strong>Shave</strong> the area 12–24 hours before and arrive with clean skin — no lotion, deodorant, "
          "self-tanner or makeup on the treatment area.",
          "<strong>Do not wax, pluck, thread or epilate</strong> for at least two weeks beforehand: the laser needs an "
          "intact root to target. Avoid sun and tanning beds for two weeks, and mention any medication that increases "
          "light sensitivity."]),
        ("Where is the clinic and how do I book?",
         ["Marzi Skincare &amp; Laser Clinic is at 1856 Ambrosi Rd&nbsp;#120, Kelowna, BC — just off Highway&nbsp;97 "
          "near Orchard Park Mall, with free on-site parking. Book online through "
          f"<a href='{BOOK}' rel='noopener' target='_blank'>Vagaro</a> or call "
          f"<a href='tel:{PHONE_T}'>{PHONE_H}</a>. Consultations are free and take about fifteen minutes."]),
    ]

    fp_data = [
        ("I", "var(--fp1)", "Type I — Very fair",
         "Always burns, never tans. Excellent results when hair is dark; very light blonde or red hair will not respond to any laser."),
        ("II", "var(--fp2)", "Type II — Fair",
         "Burns easily, tans minimally. One of the most responsive groups — high contrast between pale skin and dark hair gives fast, clean clearance."),
        ("III", "var(--fp3)", "Type III — Light olive",
         "Sometimes burns, tans gradually. Very responsive. Settings are adjusted seasonally, since Okanagan summers change your baseline tan."),
        ("IV", "var(--fp4)", "Type IV — Olive / mid-brown",
         "Rarely burns, tans easily. Treated with reduced fluence and longer pulse width. A diode wavelength is a far safer choice here than IPL."),
        ("V", "var(--fp5)", "Type V — Brown",
         "Very rarely burns. Treated conservatively across more sessions with strong contact cooling. A patch test 48 hours ahead is required."),
        ("VI", "var(--fp6)", "Type VI — Deeply pigmented",
         "Never burns. Safe on the Alpha Pro with low fluence, long pulses and full cooling. Expect a gentler course — and always a patch test first."),
    ]
    fp_html = "".join(
        f'<button class="fp" role="option" aria-selected="false" data-t="{t}" data-n="{n}">'
        f'<i style="background:{c}"></i>{r}</button>' for r, c, t, n in fp_data)

    home_ld = {"@context": "https://schema.org", "@graph": [
        CLINIC,
        {"@type": "MedicalProcedure", "@id": SITE + "/#procedure", "name": "Laser hair removal",
         "alternateName": "Diode laser permanent hair reduction",
         "procedureType": "https://schema.org/NoninvasiveProcedure",
         "bodyLocation": "Face, underarms, arms, legs, back, chest, bikini area",
         "howPerformed": "A diode laser pulse is delivered to the treatment area. Melanin in the hair shaft absorbs "
                         "the light, converts it to heat and disables the follicle at the root, while a sapphire "
                         "contact cooling head protects the surrounding skin.",
         "preparation": "Shave the area 12 to 24 hours before treatment. Avoid waxing, plucking and sun exposure for "
                        "two weeks beforehand.",
         "followup": "Sessions repeat every 4 to 8 weeks; most people need 6 to 10 sessions for a full result.",
         "performer": {"@id": SITE + "/#clinic"}},
        {"@type": "WebSite", "@id": SITE + "/#website", "url": SITE + "/", "name": "Marzi Laser Kelowna",
         "inLanguage": "en-CA", "publisher": {"@id": SITE + "/#clinic"}},
        {"@type": "WebPage", "@id": SITE + "/#webpage", "url": SITE + "/",
         "name": "Laser Hair Removal Kelowna | Marzi Skincare & Laser Clinic",
         "isPartOf": {"@id": SITE + "/#website"}, "about": {"@id": SITE + "/#procedure"},
         "primaryImageOfPage": HERO_IMG, "datePublished": "2026-07-24", "dateModified": B["TODAY"],
         "speakable": {"@type": "SpeakableSpecification", "cssSelector": [".answer", "h1"]}},
        faq_ld(home_faqs) | {"@id": SITE + "/#faq"},
    ]}

    page("/",
         "Laser Hair Removal Kelowna | Marzi Skincare &amp; Laser Clinic",
         "Laser hair removal in Kelowna with the Alpha Pro diode laser. Safe for all skin tones, 22+ years "
         "experience, 50% off your first session. Book online.",
         f"""
<header class="hero"><div class="container hero-grid">
  <div class="rv">
    <p class="pill">{ic('shield')} Kelowna, BC · 22+ years experience</p>
    <h1>Laser hair removal, done properly.</h1>
    <p class="lede">Permanent hair reduction with the Alpha&nbsp;Pro diode laser — safe for every skin tone,
    three times faster than older systems, and performed start to finish by Marzi herself. Never handed to a technician.</p>
    <div class="hero-cta">
      <a href="{BOOK}" class="btn btn-primary" rel="noopener" target="_blank">{ic('cal')} Book online</a>
      <a href="/pricing" class="btn btn-ghost">See prices {ic('right')}</a>
    </div>
    <div class="hero-tags">
      <span class="tag">{ic('check')} All skin types I–VI</span>
      <span class="tag">{ic('check')} Single-operator clinic</span>
      <span class="tag">{ic('check')} 50% off first session</span>
    </div>
  </div>
  <div class="hero-media rv d1">
    <img src="{HERO_IMG}" width="800" height="1000" fetchpriority="high" decoding="async"
         alt="Marzi Skincare &amp; Laser Clinic, laser hair removal in Kelowna, BC">
    <div class="hero-badge">
      <span><b>Marzi Skincare &amp; Laser Clinic</b><span>1856 Ambrosi Rd #120, Kelowna</span></span>
      <a href="tel:{PHONE_T}" class="btn btn-primary btn-sm">{ic('phone')} Call</a>
    </div>
  </div>
</div></header>

<section class="tight"><div class="container">
  <div class="panel rv">
    <div class="answer" style="margin-top:0">
      <span class="lbl">In short</span>
      <p><strong>Marzi Skincare &amp; Laser Clinic</strong> is a laser hair removal clinic at 1856 Ambrosi Rd&nbsp;#120
      in Kelowna, BC. Treatments use the <strong>Alpha&nbsp;Pro 808&nbsp;nm diode laser</strong>, safe for Fitzpatrick
      skin types&nbsp;I–VI, and are performed personally by <strong>Marzi Salehi</strong>, a certified medical
      aesthetician with more than 22 years of experience. Single sessions start at <strong>$80</strong>, most people
      need 6–10 sessions, and first-time laser clients receive <strong>50% off</strong>. Call
      <strong>{PHONE_H}</strong> or book online.</p>
    </div>
    <div class="spectrum-label"><span>Fitzpatrick I</span><hr class="spectrum"><span>VI</span></div>
    <div class="stats">
      <div class="stat"><b>22+</b><span>Years in practice</span></div>
      <div class="stat"><b>I–VI</b><span>Skin types treated</span></div>
      <div class="stat"><b>3&times;</b><span>Faster per pass</span></div>
      <div class="stat"><b>1</b><span>Aesthetician, always</span></div>
    </div>
  </div>
</div></section>

<section><div class="container grid-2 center">
  <div class="rv">
    <p class="eyebrow">Built for every skin tone</p>
    <h2>Most lasers can't treat dark skin. This one can.</h2>
    <p>Older IPL and alexandrite machines struggle on deeper skin tones, because the light can't distinguish pigment
    in the hair from pigment in the skin. The Alpha&nbsp;Pro solves that with an 808&nbsp;nm diode wavelength, a long
    adjustable pulse and a sapphire contact-cooling tip that chills the surface while the follicle heats underneath.</p>
    <p>The result: Marzi can safely treat <strong>Fitzpatrick I through VI</strong>, including brown and Black skin,
    and tanned Okanagan summer skin that other clinics turn away. Every new client gets a patch test first.</p>
    <p class="mt-1"><a href="/alpha-pro-laser" class="card-go">How the Alpha Pro laser works {ic('right')}</a></p>
  </div>
  <div class="panel rv d1">
    <h3>Select your skin type</h3>
    <p class="muted">The Fitzpatrick scale describes how skin responds to UV. Tap yours.</p>
    <div class="fp-grid" role="listbox" aria-label="Fitzpatrick skin type selector">{fp_html}</div>
    <div class="fp-out" id="fp-out">
      <b>All six are treatable here</b>
      <p>Select a type above to see how treatment is adjusted for it.</p>
    </div>
  </div>
</div></section>

<section><div class="container">
  <div class="sec-head center rv">
    <p class="eyebrow">What we treat</p>
    <h2>Laser hair removal areas</h2>
    <p>From a five-minute upper lip to a full-body course. Each page covers what's involved, how many sessions it
    takes and what it costs.</p>
  </div>
  <div class="grid-3">
    <a href="/brazilian-bikini-laser-hair-removal-kelowna" class="card rv">
      <span class="card-icon">{ic('leaf')}</span>
      <h3>Brazilian &amp; Bikini</h3>
      <p>The most requested treatment at the clinic. Private, unhurried, and no wax strips ever again.</p>
      <div class="card-foot"><span class="card-meta">From $120 · 6–8 sessions</span><span class="card-go">Details {ic('right')}</span></div>
    </a>
    <a href="/full-body-laser-hair-removal-kelowna" class="card rv d1">
      <span class="card-icon">{ic('user')}</span>
      <h3>Full Body</h3>
      <p>Legs, arms, underarms, bikini and face in one 90-minute session at the best rate per area.</p>
      <div class="card-foot"><span class="card-meta">From $650 · 8–10 sessions</span><span class="card-go">Details {ic('right')}</span></div>
    </a>
    <a href="/facial-laser-hair-removal-kelowna" class="card rv d2">
      <span class="card-icon">{ic('spark')}</span>
      <h3>Face, Lip &amp; Chin</h3>
      <p>Upper lip, chin, jawline and full face — including hormonal and PCOS-related growth.</p>
      <div class="card-foot"><span class="card-meta">From $80 · 8–10 sessions</span><span class="card-go">Details {ic('right')}</span></div>
    </a>
  </div>
  <div class="grid-3" style="margin-top:1.25rem">
    <a href="/mens-laser-hair-removal-kelowna" class="card rv">
      <span class="card-icon">{ic('shirt')}</span>
      <h3>Men's Laser Hair Removal</h3>
      <p>Back, chest, shoulders, neckline and beard shaping. Coarse hair responds fastest of all.</p>
      <div class="card-foot"><span class="card-meta">From $120 · 6–8 sessions</span><span class="card-go">Details {ic('right')}</span></div>
    </a>
    <a href="/pricing" class="card rv d1">
      <span class="card-icon">{ic('tag')}</span>
      <h3>Underarms, Arms &amp; Legs</h3>
      <p>Fast, high-yield areas. Underarms take under ten minutes; full legs are the biggest quality-of-life win.</p>
      <div class="card-foot"><span class="card-meta">From $95</span><span class="card-go">See prices {ic('right')}</span></div>
    </a>
    <a href="/contact" class="card rv d2" style="background:var(--sand);border-color:var(--line)">
      <span class="card-icon" style="background:#fff">{ic('chat')}</span>
      <h3>Not sure where to start?</h3>
      <p>Book a free 15-minute consultation. Marzi maps your areas, does a patch test and quotes you exactly.</p>
      <div class="card-foot"><span class="card-meta">Free · 15 min</span><span class="card-go">Book {ic('right')}</span></div>
    </a>
  </div>
</div></section>

<section><div class="container grid-2">
  <div class="rv">
    <p class="eyebrow">The process</p>
    <h2>What actually happens.</h2>
    <p>No sales funnel, no package pressure, no rotating staff. You see Marzi at every appointment, which means your
    settings, your skin's response and your progress live in one person's head instead of a shared clipboard.</p>
    <p class="mt-1"><a href="/how-it-works" class="card-go">Read the full treatment process {ic('right')}</a></p>
  </div>
  <div class="steps rv d1">
    <div class="step"><span class="step-n">01</span><div><h3>Free consultation &amp; patch test</h3>
      <p>Fifteen minutes. Skin type assessment, medical history, a test pulse on a small area, and a written quote.</p></div></div>
    <div class="step"><span class="step-n">02</span><div><h3>Your treatment course</h3>
      <p>Sessions every 4–8 weeks. Shave the day before, arrive with clean skin, and most areas are done in 30 minutes.</p></div></div>
    <div class="step"><span class="step-n">03</span><div><h3>Maintenance</h3>
      <p>After 6–10 sessions most people are down to one or two touch-ups a year, usually for hormonal regrowth.</p></div></div>
  </div>
</div></section>

<section><div class="container grid-2 center">
  <div class="panel panel-sand rv">
    <blockquote style="font-family:var(--serif);font-size:1.45rem;line-height:1.32;color:var(--ink)">
      &ldquo;You won't find a better aesthetic medicine clinic in Kelowna.&rdquo;
    </blockquote>
    <p class="muted" style="margin-top:.75rem">— Client review</p>
    <hr class="spectrum" style="margin:1.5rem 0">
    <ul class="checks">
      <li>{ic('check')} Certified medical aesthetician, 22+ years</li>
      <li>{ic('check')} Every treatment performed personally — no delegated sessions</li>
      <li>{ic('check')} Medical-grade Alpha Pro diode platform</li>
      <li>{ic('check')} Single-use and hygiene protocols on every appointment</li>
    </ul>
  </div>
  <div class="rv d1">
    <p class="eyebrow">Who treats you</p>
    <h2>Marzi Salehi.</h2>
    <p>Certified medical aesthetician, more than <strong>22 years</strong> in practice, specialising in laser hair
    removal, IPL, CryoPen lesion removal and advanced facial work. Marzi runs the clinic solo — she does the
    consultation, the patch test, every pulse and every follow-up.</p>
    <p>That matters more than it sounds. Laser settings are judged by eye against your skin's live response. A
    practitioner who has seen your skin at session one reads session six very differently from someone meeting you
    for the first time.</p>
    <a href="/about" class="btn btn-ghost mt-1">More about Marzi</a>
  </div>
</div></section>

<section><div class="container narrow">
  <div class="sec-head center rv">
    <p class="eyebrow">Transparent pricing</p>
    <h2>What it costs</h2>
    <p>Canadian dollars, per session. Three-session packages save roughly 12–15%.</p>
  </div>
  <div class="panel rv">
    <div class="tw"><table class="t">
      <caption>Popular laser hair removal areas — Kelowna, BC</caption>
      <thead><tr><th scope="col">Area</th><th scope="col">Single session</th><th scope="col">Package of 3</th></tr></thead>
      <tbody>
        <tr><td>Upper lip</td><td class="n">$80</td><td class="n">$210</td></tr>
        <tr><td>Chin</td><td class="n">$85</td><td class="n">$225</td></tr>
        <tr><td>Full face</td><td class="n">$225</td><td class="n">$615</td></tr>
        <tr><td>Underarms</td><td class="n">$95</td><td class="n">$255</td></tr>
        <tr><td>Bikini line</td><td class="n">$120</td><td class="n">$320</td></tr>
        <tr><td>Brazilian</td><td class="n">$180</td><td class="n">$480</td></tr>
        <tr><td>Full legs</td><td class="n">$290</td><td class="n">$780</td></tr>
      </tbody>
    </table></div>
    <p class="muted mt-1">First-time laser clients receive <strong>50% off their first session</strong>.
    Consultations are always free.</p>
    <a href="/pricing" class="btn btn-primary mt-1">Full price list</a>
  </div>
</div></section>

<section><div class="container narrow">
  <div class="sec-head center rv"><p class="eyebrow">Straight answers</p><h2>Common questions</h2></div>
  {faq_block(home_faqs)}
  <p class="text-center mt-2"><a href="/faq" class="card-go">All 20 laser hair removal questions {ic('right')}</a></p>
</div></section>

{BAND}

<section><div class="container">
  <div class="sec-head center rv">
    <p class="eyebrow">Find us</p>
    <h2>Laser hair removal near you in Kelowna</h2>
    <p>Central Kelowna on Ambrosi Rd, minutes from Orchard Park Mall and Highway&nbsp;97, with free on-site parking.
    Clients travel from West Kelowna, Lake Country, Peachland, Vernon and Penticton.</p>
  </div>
  <div class="grid-3 rv">
    <a href="/contact" class="tile">{ic('pin')}<div class="lbl">Address</div><b>1856 Ambrosi Rd #120<br>Kelowna, BC</b></a>
    <a href="tel:{PHONE_T}" class="tile">{ic('phone')}<div class="lbl">Call the clinic</div><b>{PHONE_H}</b></a>
    <a href="/contact" class="tile">{ic('clock')}<div class="lbl">Opening hours</div><b>Mon–Fri from 9:00<br>Weekends 11:00–16:00</b></a>
  </div>
</div></section>""",
         ld=home_ld)

    # ================================================================== PRICING
    pricing_faqs = [
        ("Why do laser hair removal prices vary so much in Kelowna?",
         ["Three things drive it: the machine, the operator and the session count. A medical-grade diode platform "
          "costs several times what a countertop IPL unit does, and it clears hair in fewer sessions — so a $60 IPL "
          "session that needs 15 visits costs more overall than a $95 diode session that needs 7.",
          "The second factor is who holds the handpiece. Here it is always Marzi, a certified medical aesthetician "
          "with 22+ years of experience, not a junior technician working from a settings chart."]),
        ("Do you offer packages?",
         ["Yes. Buying three sessions up front saves roughly 12–15% against paying per session, and it is how most "
          "clients book, because nobody finishes a course in one visit. Larger multi-area packages are quoted "
          "individually at your consultation."]),
        ("Is the consultation really free?",
         ["Yes. It runs about 15 minutes and includes a skin type assessment, a review of your medical history and "
          "medications, a patch test where appropriate, and a written quote for your areas. No obligation to book."]),
        ("What payment methods do you accept?",
         ["Debit, credit and cash. Prices are in Canadian dollars. Call "
          f"<a href='tel:{PHONE_T}'>{PHONE_H}</a> to confirm current pricing before booking."]),
    ]
    page("/pricing",
         "Laser Hair Removal Prices Kelowna | Cost Per Session",
         "Laser hair removal prices in Kelowna: upper lip $80, underarms $95, Brazilian $180, full legs $290. "
         "Package rates and 50% off your first session.",
         phero([("/", "Home"), (None, "Pricing")], "Transparent pricing",
               "Laser Hair Removal Prices in Kelowna",
               "Every price in Canadian dollars, per session, with the three-session package rate beside it. No "
               "consultation fee, no membership, no pressure to prepay a year in advance.",
               "Laser hair removal in Kelowna costs roughly <strong>$80–$120 per session for small areas</strong> "
               "(upper lip, chin, underarms) and <strong>$180–$400 for large areas</strong> (Brazilian, full legs, "
               "back). At Marzi Skincare &amp; Laser Clinic the upper lip is <strong>$80</strong>, underarms "
               "<strong>$95</strong>, Brazilian <strong>$180</strong> and full legs <strong>$290</strong>. Most areas "
               "need 6–10 sessions. First-time clients get <strong>50% off</strong> and the consultation is free.")
         + f"""
<section style="padding-top:1rem"><div class="container">

  <div class="panel rv">
    <h2 style="font-size:1.7rem">Face &amp; neck</h2>
    <div class="tw"><table class="t">
      <caption>Facial laser hair removal — Kelowna, BC. Prices in CAD.</caption>
      <thead><tr><th scope="col">Area</th><th scope="col">Single</th><th scope="col">Package of 3</th><th scope="col">Typical course</th></tr></thead>
      <tbody>
        <tr><td>Upper lip</td><td class="n">$80</td><td class="n">$210</td><td>8–10 sessions</td></tr>
        <tr><td>Chin</td><td class="n">$85</td><td class="n">$225</td><td>8–10 sessions</td></tr>
        <tr><td>Upper lip + chin</td><td class="n">$140</td><td class="n">$375</td><td>8–10 sessions</td></tr>
        <tr><td>Sideburns</td><td class="n">$90</td><td class="n">$240</td><td>6–8 sessions</td></tr>
        <tr><td>Cheeks</td><td class="n">$110</td><td class="n">$295</td><td>8–10 sessions</td></tr>
        <tr><td>Neck (front or back)</td><td class="n">$120</td><td class="n">$320</td><td>6–8 sessions</td></tr>
        <tr><td>Full face</td><td class="n">$225</td><td class="n">$615</td><td>8–10 sessions</td></tr>
      </tbody>
    </table></div>
    <p class="muted mt-1">Facial hair is often hormone-driven, so courses run longer and usually need annual
    maintenance. <a href="/facial-laser-hair-removal-kelowna">More on facial laser hair removal &rarr;</a></p>
  </div>

  <div class="panel rv" style="margin-top:1.5rem">
    <h2 style="font-size:1.7rem">Body</h2>
    <div class="tw"><table class="t">
      <caption>Body laser hair removal — Kelowna, BC. Prices in CAD.</caption>
      <thead><tr><th scope="col">Area</th><th scope="col">Single</th><th scope="col">Package of 3</th><th scope="col">Typical course</th></tr></thead>
      <tbody>
        <tr><td>Underarms</td><td class="n">$95</td><td class="n">$255</td><td>6–8 sessions</td></tr>
        <tr><td>Half arms</td><td class="n">$150</td><td class="n">$400</td><td>6–8 sessions</td></tr>
        <tr><td>Full arms</td><td class="n">$210</td><td class="n">$565</td><td>6–8 sessions</td></tr>
        <tr><td>Half legs</td><td class="n">$190</td><td class="n">$510</td><td>6–8 sessions</td></tr>
        <tr><td>Full legs</td><td class="n">$290</td><td class="n">$780</td><td>6–8 sessions</td></tr>
        <tr><td>Bikini line</td><td class="n">$120</td><td class="n">$320</td><td>6–8 sessions</td></tr>
        <tr><td>Brazilian</td><td class="n">$180</td><td class="n">$480</td><td>6–8 sessions</td></tr>
        <tr><td>Stomach or lower back</td><td class="n">$140</td><td class="n">$375</td><td>6–8 sessions</td></tr>
        <tr><td>Full back</td><td class="n">$260</td><td class="n">$700</td><td>6–8 sessions</td></tr>
        <tr><td>Chest</td><td class="n">$200</td><td class="n">$540</td><td>6–8 sessions</td></tr>
        <tr><td>Shoulders</td><td class="n">$130</td><td class="n">$350</td><td>6–8 sessions</td></tr>
      </tbody>
    </table></div>
  </div>

  <div class="panel rv" style="margin-top:1.5rem">
    <h2 style="font-size:1.7rem">Multi-area packages</h2>
    <div class="tw"><table class="t">
      <caption>Combination packages — best value per area.</caption>
      <thead><tr><th scope="col">Package</th><th scope="col">Includes</th><th scope="col">Per session</th></tr></thead>
      <tbody>
        <tr><td>The Essentials</td><td>Underarms + bikini line</td><td class="n">$185</td></tr>
        <tr><td>Summer Ready</td><td>Full legs + bikini line + underarms</td><td class="n">$425</td></tr>
        <tr><td>Full Body</td><td>Legs, arms, underarms, bikini, stomach, face</td><td class="n">From $650</td></tr>
        <tr><td>Men's Upper Body</td><td>Full back + shoulders + chest</td><td class="n">$490</td></tr>
      </tbody>
    </table></div>
    <p class="muted mt-1">Multi-area packages are confirmed at consultation, since coverage varies by body size.
    <a href="/full-body-laser-hair-removal-kelowna">Full body details &rarr;</a></p>
  </div>

  <div class="grid-2" style="margin-top:2.75rem">
    <div class="rv">
      <h2>What you are actually paying for</h2>
      <p>The number on a price list only means something next to the number of sessions it takes to finish. A clinic
      charging $60 a session on an entry-level IPL device that needs fifteen visits costs more than $95 a session on a
      medical diode that finishes in seven — and takes two years longer to get you there.</p>
      <ul class="checks mt-1">
        <li>{ic('check')} <span><strong>The platform.</strong> An 808&nbsp;nm diode with contact cooling clears coarse
        hair in fewer passes and can run safely on dark skin.</span></li>
        <li>{ic('check')} <span><strong>The operator.</strong> Settings are a judgement call against your live skin
        response, not a chart. Experience shortens courses.</span></li>
        <li>{ic('check')} <span><strong>Honest scheduling.</strong> Being brought back every four weeks when your area
        needs eight just sells sessions that do nothing.</span></li>
      </ul>
    </div>
    <div class="panel rv d1">
      <h3>Cost of a typical course</h3>
      <p class="muted">Example: underarms, a fast-responding area.</p>
      <div class="tw mt-1"><table class="t"><tbody>
        <tr><td>First session (50% off)</td><td class="n">$48</td></tr>
        <tr><td>Sessions 2–3 (package rate)</td><td class="n">$160</td></tr>
        <tr><td>Sessions 4–6 (package rate)</td><td class="n">$255</td></tr>
        <tr><td>Session 7, if needed</td><td class="n">$85</td></tr>
        <tr><td><strong>Full course</strong></td><td class="n">&asymp; $548</td></tr>
      </tbody></table></div>
      <p class="muted mt-1">Against roughly $30 a month on waxing, a course like this pays for itself in about
      18 months — and then stops costing anything.</p>
    </div>
  </div>
</div></section>

<section><div class="container narrow">
  <div class="sec-head center rv"><h2>Pricing questions</h2></div>
  {faq_block(pricing_faqs)}
</div></section>{BAND}""",
         ld={"@context": "https://schema.org", "@graph": [
             service_ld("Laser hair removal", "Laser hair removal pricing in Kelowna, BC", "/pricing", 80),
             faq_ld(pricing_faqs)]})

    # ================================================================== HOW IT WORKS
    hiw_faqs = [
        ("How long does a session take?",
         ["Underarms take about ten minutes. Upper lip is closer to five. Bikini and Brazilian run 15–25 minutes, "
          "full legs 40–50, and a full-body session about 90. Power Motion Technology moves in continuous sweeping "
          "passes rather than single stamped shots, which is where the speed comes from."]),
        ("What should I do after a session?",
         ["Expect mild redness and small raised bumps around each follicle for a few hours — that reaction means the "
          "follicle absorbed the energy. Keep the area cool, use a fragrance-free moisturiser, and skip hot tubs, "
          "saunas, hot yoga and heavy workouts for 24 hours.",
          "Use SPF 30+ on any treated area that sees daylight for the following two weeks. Do not pluck or wax "
          "between sessions — shaving is fine and encouraged."]),
        ("When will I see results?",
         ["Treated hairs shed 7–21 days after each session, which often looks like new growth but is the follicle "
          "pushing the dead shaft out. Most people notice visible thinning after the second or third session. The "
          "clearest gains usually come between sessions three and six."]),
        ("Can I have laser hair removal in summer?",
         ["Yes, with care. The constraint is not the season but the tan: freshly tanned skin has more melanin at the "
          "surface, which changes safe settings. Keep treated areas out of direct sun and under SPF 30+ for two weeks "
          "either side of a session, and avoid self-tanner entirely during a course. Many Okanagan clients start "
          "courses in autumn for this reason."]),
    ]
    page("/how-it-works",
         "How Laser Hair Removal Works | Step by Step, Kelowna",
         "What happens during laser hair removal, how to prepare, what a session feels like and how to care for "
         "your skin after. A step-by-step guide from a Kelowna clinic.",
         phero([("/", "Home"), (None, "How It Works")], "The process", "How Laser Hair Removal Works",
               "The science in plain language, plus exactly what to expect from your first phone call to your final "
               "maintenance session.",
               "Laser hair removal works by <strong>selective photothermolysis</strong>: a laser pulse is tuned to a "
               "wavelength that melanin absorbs strongly. Pigment in the hair shaft converts that light into heat, "
               "which travels down to the follicle and disables the cells that regrow hair, while a cooling tip keeps "
               "surrounding skin at a safe temperature. Because it only works on follicles in the active growth "
               "phase, <strong>6–10 sessions spaced 4–8 weeks apart</strong> are needed for a permanent reduction.")
         + f"""
<section style="padding-top:1rem"><div class="container grid-2">
  <div class="rv prose">
    <h2>The science, briefly</h2>
    <p>Hair and skin both contain melanin, but not in equal concentration. In a hair follicle it is densely packed in
    the shaft; in skin it sits diffusely in the upper layer. A laser exploits that difference.</p>
    <p>The Alpha&nbsp;Pro emits at <strong>808&nbsp;nanometres</strong>, in the near-infrared. That wavelength is
    absorbed well by melanin but passes through water and haemoglobin, so it reaches the follicle 2–5&nbsp;mm below the
    surface without cooking everything on the way. The absorbed light becomes heat. Heat above roughly 70&nbsp;°C
    destroys the follicular stem cells and the dermal papilla — the structures that build a new hair.</p>
    <p>The window for doing that safely is narrow, and it is controlled by three settings: <strong>fluence</strong>
    (energy per square centimetre), <strong>pulse width</strong> (how long the energy is delivered) and
    <strong>cooling</strong>. Longer pulses at lower fluence spread the heat over time, which is exactly what makes
    darker skin safe to treat.</p>

    <h2>Why one session can never be enough</h2>
    <p>Every follicle cycles independently through three phases:</p>
    <ul>
      <li><strong>Anagen</strong> — active growth, shaft attached to the papilla. <em>The only phase a laser can destroy.</em></li>
      <li><strong>Catagen</strong> — transition, the follicle detaches and shrinks.</li>
      <li><strong>Telogen</strong> — rest, then shedding.</li>
    </ul>
    <p>At any moment only around <strong>20–30%</strong> of follicles in an area are in anagen. That is the ceiling on
    what a single session can achieve, no matter how good the machine is. Repeat sessions spaced to the area's cycle
    length catch successive waves — which is why the interval matters as much as the energy.</p>

    <h3>Interval by area</h3>
    <ul>
      <li>Face and neck — every <strong>4 weeks</strong> (fast cycle)</li>
      <li>Underarms and bikini — every <strong>5–6 weeks</strong></li>
      <li>Arms, legs, back and chest — every <strong>6–8 weeks</strong></li>
    </ul>
    <p>Coming in more often than your cycle allows simply wastes a session on follicles that are not there yet.</p>
  </div>

  <div class="rv d1">
    <div class="panel sticky-col">
      <h3>Who is a good candidate?</h3>
      <ul class="checks mt-1">
        <li>{ic('check')} <span><strong>Best results:</strong> dark, coarse hair on any skin tone</span></li>
        <li>{ic('check')} <span><strong>Good results:</strong> medium-brown hair, fine dark hair over more sessions</span></li>
        <li>{ic('spark')} <span><strong>Limited response:</strong> white, grey and true red hair — there is no melanin
        to target, on any machine</span></li>
      </ul>
      <hr class="spectrum" style="margin:1.5rem 0">
      <h3 style="font-size:1.15rem">Tell Marzi about</h3>
      <ul class="checks">
        <li>{ic('check')} Isotretinoin (Accutane) in the last 6 months</li>
        <li>{ic('check')} Photosensitising medication — some antibiotics, retinoids, St John's wort</li>
        <li>{ic('check')} Pregnancy or breastfeeding</li>
        <li>{ic('check')} Active cold sores near the treatment area</li>
        <li>{ic('check')} A history of keloid scarring or hyperpigmentation</li>
        <li>{ic('check')} PCOS or other hormonal conditions</li>
      </ul>
      <p class="muted mt-1">None of these is automatically disqualifying. They change timing and settings, which is
      exactly what the consultation is for.</p>
    </div>
  </div>
</div></section>

<section><div class="container">
  <div class="sec-head center rv"><p class="eyebrow">Step by step</p><h2>Your treatment, start to finish</h2></div>
  <div class="steps rv">
    <div class="step"><span class="step-n">01</span><div><h3>Free consultation (15 min)</h3>
      <p>Skin type assessment on the Fitzpatrick scale, hair colour and density check, medical history and medication
      review, then a patch test. You leave with a written quote and a realistic session count.</p></div></div>
    <div class="step"><span class="step-n">02</span><div><h3>Preparation, 24 hours before</h3>
      <p>Shave the area — do not wax, pluck, thread or epilate for two weeks beforehand, because the laser needs an
      intact root. Arrive with clean skin: no lotion, deodorant, makeup or self-tanner.</p></div></div>
    <div class="step"><span class="step-n">03</span><div><h3>The session</h3>
      <p>Protective eyewear on. Marzi passes the cooled handpiece over the area in overlapping sweeps. You feel warmth
      with a brief snap at each pass. Ten minutes for underarms, up to 50 for full legs.</p></div></div>
    <div class="step"><span class="step-n">04</span><div><h3>The first 24 hours</h3>
      <p>Mild redness and follicular bumps are normal and settle within hours. Skip saunas, hot tubs, hot yoga and
      intense exercise for a day. SPF 30+ on exposed areas for two weeks.</p></div></div>
    <div class="step"><span class="step-n">05</span><div><h3>Days 7–21: the shed</h3>
      <p>Treated hairs push out of the follicle and fall away. It can look like regrowth — it is not. Gentle
      exfoliation helps them clear. Shave freely between sessions.</p></div></div>
    <div class="step"><span class="step-n">06</span><div><h3>Sessions 2 through 10</h3>
      <p>Each visit catches a new wave of follicles entering the growth phase. Density drops, regrowth comes back finer
      and lighter, and intervals stretch out as there is less left to treat.</p></div></div>
    <div class="step"><span class="step-n">07</span><div><h3>Maintenance</h3>
      <p>After the course, most people book one or two touch-ups a year for hormone-driven regrowth. Some never need
      another session at all.</p></div></div>
  </div>
</div></section>

<section><div class="container narrow">
  <div class="sec-head center rv"><h2>Process questions</h2></div>
  {faq_block(hiw_faqs)}
  <p class="text-center mt-2"><a href="/faq" class="card-go">See all questions {ic('right')}</a></p>
</div></section>{BAND}""",
         ld={"@context": "https://schema.org", "@graph": [
             {"@type": "HowTo", "name": "How laser hair removal works, step by step",
              "description": "The full treatment process at a Kelowna laser hair removal clinic.",
              "totalTime": "P10M", "step": [
                  {"@type": "HowToStep", "position": 1, "name": "Free consultation and patch test",
                   "text": "Skin type assessment, medical history review, and a test pulse on a small area."},
                  {"@type": "HowToStep", "position": 2, "name": "Preparation",
                   "text": "Shave 12 to 24 hours before. No waxing, plucking or threading for two weeks prior."},
                  {"@type": "HowToStep", "position": 3, "name": "The session",
                   "text": "A cooled handpiece passes over the area in overlapping sweeps."},
                  {"@type": "HowToStep", "position": 4, "name": "Aftercare",
                   "text": "Avoid heat and intense exercise for 24 hours. Use SPF 30+ for two weeks."},
                  {"@type": "HowToStep", "position": 5, "name": "The shed",
                   "text": "Treated hairs fall out 7 to 21 days later."},
                  {"@type": "HowToStep", "position": 6, "name": "Repeat sessions",
                   "text": "Six to ten sessions spaced four to eight weeks apart."},
                  {"@type": "HowToStep", "position": 7, "name": "Maintenance",
                   "text": "One or two touch-ups a year after the course."}]},
             faq_ld(hiw_faqs)]})

    # ================================================================== ALPHA PRO
    laser_faqs = [
        ("What is the difference between laser hair removal and IPL?",
         ["A laser emits a single wavelength of coherent light; IPL emits a broad spectrum through a filter. A diode "
          "laser puts all its energy at 808&nbsp;nm, which is absorbed by hair melanin and reaches the follicle at "
          "depth. IPL scatters energy across many wavelengths, much of which is absorbed by skin instead.",
          "The consequences: IPL generally needs more sessions, works poorly on coarse or deep hair, and carries a "
          "meaningfully higher risk of burns and pigment change on skin darker than Fitzpatrick III."]),
        ("Is the Alpha Pro laser safe?",
         ["Yes, when operated correctly. It is a professional-grade diode platform with contact cooling and adjustable "
          "fluence, pulse width and repetition rate. Safety comes from matching those parameters to your skin type and "
          "hair, which is why every new client gets a patch test before a full session."]),
        ("What does Power Motion Technology mean?",
         ["Instead of firing single high-energy shots and stepping across an area, the handpiece moves continuously in "
          "overlapping sweeps while delivering rapid lower-energy pulses. The follicle accumulates heat over several "
          "passes rather than absorbing it all at once.",
          "That makes treatments roughly three times faster, noticeably more comfortable, and more forgiving on darker "
          "skin, because peak surface temperature stays lower for the same total energy delivered."]),
    ]
    page("/alpha-pro-laser",
         "Alpha Pro Diode Laser Kelowna | Safe for All Skin Types",
         "The Alpha Pro 808 nm diode laser used at Marzi Skincare & Laser Clinic in Kelowna: how it works, why it is "
         "safe for Fitzpatrick I–VI, and how it compares with IPL.",
         phero([("/", "Home"), (None, "The Alpha Pro Laser")], "The technology", "The Alpha Pro Diode Laser",
               "One machine, one wavelength, and the reason this clinic can treat skin tones that many Kelowna clinics "
               "turn away.",
               "The <strong>Alpha&nbsp;Pro</strong> is a professional <strong>808&nbsp;nm diode laser</strong> for "
               "permanent hair reduction. Its near-infrared wavelength is absorbed by melanin in the hair shaft while "
               "passing through surface skin, and a sapphire contact-cooling tip holds the skin at a safe temperature "
               "during treatment. That combination makes it safe across <strong>Fitzpatrick skin types I–VI</strong>. "
               "Power Motion Technology delivers rapid low-energy pulses in continuous sweeps, making sessions about "
               "<strong>three times faster</strong> and more comfortable than single-shot systems.")
         + f"""
<section style="padding-top:1rem"><div class="container grid-2">
  <div class="rv prose">
    <h2>Why 808 nanometres</h2>
    <p>Wavelength decides two things: how deep light travels into tissue, and what absorbs it. Shorter wavelengths are
    absorbed strongly near the surface. Longer ones penetrate further but are absorbed less efficiently by melanin.</p>
    <p>808&nbsp;nm sits in the useful middle. It reaches the follicular bulb at 2–5&nbsp;mm depth, is absorbed well
    enough by hair melanin to heat it decisively, and is absorbed <em>relatively</em> weakly by the epidermis — which
    is what creates the safety margin on brown and Black skin.</p>
    <p>For comparison: alexandrite lasers at 755&nbsp;nm are absorbed more aggressively by melanin, making them fast on
    pale skin and risky on dark skin. Nd:YAG at 1064&nbsp;nm is the safest option for Fitzpatrick VI but absorbs
    poorly, so it needs high energy and hurts more. The diode is the practical compromise that covers the widest range
    of clients well.</p>

    <h2>Contact cooling</h2>
    <p>The handpiece ends in a chilled sapphire window held against the skin. It does three jobs at once: it cools the
    epidermis before, during and after each pulse; it presses the skin flat so follicles sit closer to the surface; and
    it partially blanches surface capillaries so less energy is wasted on blood.</p>
    <p>Without contact cooling, treating Fitzpatrick V and VI safely is not realistic. With it, it is routine.</p>

    <h2>Diode vs IPL vs home devices</h2>
    <div class="tw"><table class="t">
      <thead><tr><th scope="col"></th><th scope="col">Alpha Pro diode</th><th scope="col">Clinic IPL</th><th scope="col">Home IPL</th></tr></thead>
      <tbody>
        <tr><td>Light source</td><td>Single 808 nm</td><td>Broad spectrum</td><td>Broad spectrum</td></tr>
        <tr><td>Typical fluence</td><td>Up to 40+ J/cm²</td><td>10–30 J/cm²</td><td>Under 10 J/cm²</td></tr>
        <tr><td>Safe skin types</td><td>I–VI</td><td>I–III mainly</td><td>I–IV, low power</td></tr>
        <tr><td>Sessions to result</td><td>6–10</td><td>10–15</td><td>Ongoing use</td></tr>
        <tr><td>Coarse or deep hair</td><td>Strong</td><td>Moderate</td><td>Weak</td></tr>
      </tbody>
    </table></div>
    <p class="muted mt-1">Home devices are not useless — they are maintenance tools. They cannot deliver the fluence
    needed to permanently disable a coarse follicle.</p>
  </div>

  <div class="rv d1">
    <div class="panel sticky-col">
      <h3>Specifications</h3>
      <div class="tw"><table class="t"><tbody>
        <tr><td>Wavelength</td><td class="n">808 nm</td></tr>
        <tr><td>Type</td><td class="n">Diode</td></tr>
        <tr><td>Cooling</td><td class="n">Sapphire contact</td></tr>
        <tr><td>Mode</td><td class="n">Power Motion</td></tr>
        <tr><td>Skin types</td><td class="n">I–VI</td></tr>
      </tbody></table></div>
      <hr class="spectrum" style="margin:1.5rem 0">
      <h3 style="font-size:1.15rem">What this means for you</h3>
      <ul class="checks">
        <li>{ic('check')} Dark and tanned skin can be treated safely</li>
        <li>{ic('check')} Sessions are shorter — underarms in about ten minutes</li>
        <li>{ic('check')} Coarse hair on backs and bikini lines responds strongly</li>
        <li>{ic('check')} Fewer total sessions than IPL, so a lower cost overall</li>
      </ul>
      <a href="{BOOK}" class="btn btn-primary btn-block mt-2" rel="noopener" target="_blank">Book a free patch test</a>
    </div>
  </div>
</div></section>

<section><div class="container narrow">
  <div class="sec-head center rv"><h2>Technology questions</h2></div>
  {faq_block(laser_faqs)}
</div></section>{BAND}""",
         ld={"@context": "https://schema.org", "@graph": [
             {"@type": "Product", "name": "Alpha Pro 808 nm Diode Laser",
              "description": "Professional 808 nm diode laser hair removal platform with sapphire contact cooling and "
                             "Power Motion Technology. Safe for Fitzpatrick skin types I–VI.",
              "category": "Medical aesthetic device",
              "additionalProperty": [
                  {"@type": "PropertyValue", "name": "Wavelength", "value": "808 nm"},
                  {"@type": "PropertyValue", "name": "Laser type", "value": "Diode"},
                  {"@type": "PropertyValue", "name": "Cooling", "value": "Sapphire contact cooling"},
                  {"@type": "PropertyValue", "name": "Safe skin types", "value": "Fitzpatrick I–VI"}]},
             faq_ld(laser_faqs)]})

    # ================================================================== AREA PAGES
    def area(path, title, desc, eyebrow, h1, lede, answer, body, faqs, rows, price):
        tr = "".join(f'<tr><td>{a}</td><td class="n">{b}</td><td class="n">{c}</td></tr>' for a, b, c in rows)
        page(path, title, desc,
             phero([("/", "Home"), ("/pricing", "Treatment Areas"), (None, h1)], eyebrow, h1, lede, answer)
             + f"""
<section style="padding-top:1rem"><div class="container grid-2">
  <div class="rv prose">{body}</div>
  <div class="rv d1"><div class="panel sticky-col">
    <h3>Prices</h3>
    <div class="tw"><table class="t">
      <thead><tr><th scope="col">Area</th><th scope="col">Single</th><th scope="col">3-pack</th></tr></thead>
      <tbody>{tr}</tbody>
    </table></div>
    <p class="muted mt-1">50% off your first session. Free consultation and patch test.</p>
    <a href="{BOOK}" class="btn btn-primary btn-block mt-1" rel="noopener" target="_blank">{ic('cal')} Book online</a>
    <a href="tel:{PHONE_T}" class="btn btn-ghost btn-block" style="margin-top:.6rem">{ic('phone')} {PHONE_H}</a>
    <hr class="spectrum" style="margin:1.5rem 0">
    <p class="muted">Safe for Fitzpatrick I–VI on the Alpha&nbsp;Pro diode laser.
    <a href="/alpha-pro-laser">How it works &rarr;</a></p>
  </div></div>
</div></section>

<section><div class="container narrow">
  <div class="sec-head center rv"><h2>Questions about this treatment</h2></div>
  {faq_block(faqs)}
</div></section>{BAND}""",
             ld={"@context": "https://schema.org", "@graph": [
                 service_ld(h1.replace("&amp;", "&"), desc, path, price), faq_ld(faqs)]},
             cur="/pricing")

    area("/brazilian-bikini-laser-hair-removal-kelowna",
         "Brazilian &amp; Bikini Laser Hair Removal Kelowna | From $120",
         "Brazilian and bikini laser hair removal in Kelowna. Private single-operator clinic, safe for all skin "
         "tones, Brazilian $180. Free consultation, 50% off session one.",
         "Most requested treatment", "Brazilian &amp; Bikini Laser Hair Removal",
         "The treatment most clients come for, done in a private room by one person you will see every time.",
         "Brazilian laser hair removal in Kelowna costs <strong>$180 per session</strong> at Marzi Skincare &amp; "
         "Laser Clinic, or <strong>$480 for three</strong>; a bikini line is <strong>$120</strong>. Most people need "
         "<strong>6–8 sessions</strong> spaced 5–6 weeks apart. Sessions take 15–25 minutes, are performed privately "
         "by Marzi herself, and are safe for all skin tones on the Alpha&nbsp;Pro diode laser. First session is 50% off.",
         """
<h2>Why the bikini area responds so well</h2>
<p>Hair here is typically coarse, dark and densely rooted — which sounds like a disadvantage but is exactly what a
diode laser wants. Thick shafts carry more melanin, absorb more energy and conduct more heat down to the follicle.
Coarse hair clears faster and more completely than fine hair, every time.</p>
<p>The trade-off is sensitivity. Skin in the bikini area is thin, well-supplied with nerve endings, and the follicles
sit close together. That is a comfort question, not a safety one, and it is what contact cooling and continuous motion
passes exist to solve.</p>

<h2>Bikini line, extended, or full Brazilian</h2>
<ul>
  <li><strong>Bikini line</strong> — the visible margin outside underwear. Roughly two finger-widths along each side and across the top.</li>
  <li><strong>Extended bikini</strong> — the line plus a deeper portion of the upper inner thigh.</li>
  <li><strong>Brazilian</strong> — the full front, labia and perianal area, with the option to leave a strip or triangle.</li>
</ul>
<p>You decide the shape at your consultation and can change it between sessions. Nothing is locked in.</p>

<h2>What the session is actually like</h2>
<p>You are in a private treatment room with the door closed. Marzi is the only person in the clinic who will see you,
before and after. You keep everything you want on and move a drape as each section is worked through.</p>
<p>The handpiece is chilled and held flat against the skin. Each pass feels like a warm snap. Density thins visibly by
the third session, and the sessions themselves get easier as it does.</p>

<h2>Waxing versus laser, honestly</h2>
<p>Waxing costs less per visit and works immediately. But it never stops: every four to six weeks, indefinitely, plus
regrowth stubble in between and ingrown hairs to manage. Over ten years the cost comfortably exceeds a laser course.</p>
<p>Laser is more expensive up front and takes months to finish. What you get at the end is an area that mostly stops
needing attention. The switch also means giving up waxing entirely during the course — the laser needs an intact root,
so shaving becomes your only option between sessions.</p>

<h2>Ingrown hairs and folliculitis</h2>
<p>If ingrown hairs and post-wax bumps are your actual problem, this is the treatment that addresses the cause rather
than managing the symptom. Fewer active follicles means fewer hairs curling back under the skin, and remaining regrowth
is finer and softer. Most clients see a clear difference by session three, well before the hair itself is gone.</p>
""",
         [("Does a Brazilian laser session hurt?",
           ["The bikini area is more sensitive than most, and the first session is the sharpest because hair density "
            "is at its highest. Contact cooling and Power Motion passes take most of the edge off, and clients almost "
            "universally describe it as easier than waxing — over in 15–25 minutes with no strips and no ingrowns.",
            "Sessions get progressively more comfortable as density drops. Avoid booking during the two days before "
            "your period, when skin sensitivity peaks."]),
          ("What is the difference between a bikini line and a Brazilian?",
           ["A bikini line treats only what would show outside underwear — roughly a two-finger width along each side "
            "and across the top. A Brazilian treats the full front, the labia and the perianal area, with the option "
            "to leave a strip or triangle if you prefer.",
            "You choose the shape at your consultation, and you can change it between sessions."]),
          ("How should I prepare?",
           ["Shave completely 12–24 hours before — not the same morning, since freshly shaved skin is more reactive. "
            "Do not wax, epilate or use depilatory cream for two weeks beforehand. Arrive freshly showered with no "
            "lotion, oil, powder or deodorant on the area.",
            "Loose clothing afterwards is a good idea; tight denim over freshly treated skin is uncomfortable for the "
            "first evening."]),
          ("Can I have laser hair removal on my period?",
           ["Yes, if you are using a tampon or menstrual cup. Nothing about the treatment is unsafe during your "
            "period. The only real consideration is comfort — skin sensitivity is measurably higher in the days just "
            "before and during menstruation, so if your schedule is flexible, mid-cycle appointments feel easier."]),
          ("Will laser hair removal stop ingrown hairs?",
           ["For most people, yes — and it is one of the main reasons clients switch from waxing. Ingrowns happen when "
            "a hair curls back under the skin instead of breaking through. Fewer follicles producing hair means fewer "
            "chances for that to happen, and regrowth that does appear is finer and less likely to curl. Improvement "
            "is usually obvious by the third session."])],
         [("Bikini line", "$120", "$320"), ("Extended bikini", "$150", "$400"),
          ("Brazilian", "$180", "$480"), ("Brazilian + underarms", "$250", "$670")], 180)

    area("/full-body-laser-hair-removal-kelowna",
         "Full Body Laser Hair Removal Kelowna | Packages From $650",
         "Full body laser hair removal in Kelowna: legs, arms, underarms, bikini, stomach and face in one 90-minute "
         "session. Packages from $650. Free consultation.",
         "Best value per area", "Full Body Laser Hair Removal",
         "Everything in one appointment, at the best rate per area, on a laser fast enough to make it practical.",
         "Full body laser hair removal in Kelowna is quoted <strong>from $650 per session</strong> at Marzi Skincare "
         "&amp; Laser Clinic and typically covers full legs, full arms, underarms, bikini, stomach and face. A session "
         "takes about <strong>90 minutes</strong>, and most people need <strong>8–10 sessions</strong> over 10–14 "
         "months. Booking the same areas individually would cost roughly 40% more.",
         """
<h2>What full body covers</h2>
<p>The standard package includes full legs, full arms, underarms, bikini line, stomach and face. Back, chest and
shoulders can be added — those are usually requested as part of the
<a href="/mens-laser-hair-removal-kelowna">men's upper body package</a>. Exact coverage is confirmed at your
consultation, since surface area varies.</p>

<h2>Why it needs a fast laser</h2>
<p>Full body only makes sense on a system that can cover large surfaces quickly. Older single-shot lasers fire, step
across a few millimetres, and fire again — perfectly good for an upper lip, exhausting across two full legs.</p>
<p>Power Motion Technology delivers rapid lower-energy pulses while the handpiece sweeps continuously. The follicle
accumulates heat across several passes rather than absorbing it all at once. That is roughly three times faster, and it
is what turns a three-hour appointment into a 90-minute one.</p>

<h2>Sequencing your sessions</h2>
<p>Different areas cycle at different rates, which creates a small scheduling puzzle on a full body course. Face wants
four weeks; legs want eight. Two approaches work:</p>
<ul>
  <li><strong>Single appointment, longest interval.</strong> Everything treated together every 6–8 weeks. Simplest, and what most clients choose.</li>
  <li><strong>Split appointments.</strong> Face and underarms on a shorter cycle, larger areas on a longer one. Slightly more efficient, more appointments to manage.</li>
</ul>
<p>Marzi will map this out at the consultation based on which areas matter most to you.</p>

<h2>A realistic timeline</h2>
<p>Eight to ten sessions at 6–8 week intervals means <strong>10 to 14 months</strong> from first appointment to
finished course. Nobody enjoys hearing that, but a clinic promising full body clearance in three months is either
selling sessions that will not work or misdescribing what the laser does.</p>
<p>What actually happens along the way: visible thinning by session three, a real difference in how often you shave by
session five, and by session eight most areas needing nothing at all.</p>

<h2>Cost against the alternative</h2>
<p>Shaving full body properly is 15–20 minutes several times a week, forever, plus razors and product. Waxing full body
in Kelowna runs $150–$250 a visit, every four to six weeks — around $2,000 a year, indefinitely.</p>
<p>A full body laser course is a defined cost that ends. Most clients reach break-even somewhere in the second year and
then stop paying for hair removal altogether.</p>
""",
         [("How long does a full body session take?",
           ["About 90 minutes, sometimes a little more on a first session while settings are established for each "
            "area. Power Motion Technology is what makes that feasible — single-shot systems would take two and a "
            "half to three hours to cover the same ground."]),
          ("Can I split a full body package across visits?",
           ["Yes. Some clients prefer two shorter appointments in the same week — upper body in one, lower body in the "
            "other. It costs the same and is easier to fit around work. Just keep each area on its own interval "
            "afterwards so the cycles stay aligned."]),
          ("Is full body cheaper than booking areas separately?",
           ["Considerably. Booking legs, arms, underarms, bikini, stomach and face individually adds up to well over "
            "$1,000 a session at single-area rates. The full body package is quoted from $650. The saving comes from "
            "one appointment slot and one set-up rather than six."])],
         [("Full body", "From $650", "Quoted"), ("Summer Ready bundle", "$425", "Quoted"),
          ("Full legs", "$290", "$780"), ("Full arms", "$210", "$565")], 650)

    area("/facial-laser-hair-removal-kelowna",
         "Facial Laser Hair Removal Kelowna | Upper Lip From $80",
         "Facial laser hair removal in Kelowna: upper lip $80, chin $85, full face $225. Safe for all skin tones, "
         "including hormonal and PCOS-related hair.",
         "Precision work", "Facial Laser Hair Removal",
         "Upper lip, chin, jawline, sideburns and full face — the areas where settings and a steady hand matter most.",
         "Facial laser hair removal in Kelowna starts at <strong>$80 per session</strong> for the upper lip and "
         "<strong>$225</strong> for a full face at Marzi Skincare &amp; Laser Clinic. Facial hair cycles faster than "
         "body hair, so sessions are spaced <strong>every 4 weeks</strong> and courses usually run <strong>8–10 "
         "sessions</strong>. Hormone-driven growth (PCOS, perimenopause) needs more sessions plus ongoing maintenance. "
         "Safe on all skin tones with the Alpha&nbsp;Pro diode laser.",
         """
<h2>Why the face is treated differently</h2>
<p>Three things separate facial work from body work, and all three change how a course is planned.</p>
<p><strong>Faster hair cycles.</strong> Facial follicles move through growth phases in about four weeks, against six to
eight elsewhere. Sessions are booked closer together, and stretching the interval means missing the window entirely.</p>
<p><strong>Finer hair.</strong> Vellus and fine terminal hair on the face carries less melanin than coarse body hair,
so it absorbs less energy per pulse. That means more sessions and more careful parameter selection — not more power.</p>
<p><strong>Hormonal influence.</strong> Facial hair growth in women is androgen-driven in a way that leg hair simply is
not. Hormones can activate follicles that were dormant, which is why facial courses include maintenance where body
courses often do not.</p>

<h2>Areas treated</h2>
<ul>
  <li><strong>Upper lip</strong> — the most requested facial area. Five-minute session, 8–10 sessions typical.</li>
  <li><strong>Chin and jawline</strong> — usually the coarsest facial hair, and often the most responsive.</li>
  <li><strong>Sideburns</strong> — reshaping rather than clearing, for most clients.</li>
  <li><strong>Cheeks</strong> — finer hair, gradual results, patience required.</li>
  <li><strong>Neck</strong> — front or back, frequently paired with the jawline.</li>
  <li><strong>Full face</strong> — everything above the jaw excluding the orbital area.</li>
</ul>
<p>Nothing inside the orbital rim is ever treated. Protective eyewear stays on throughout.</p>

<h2>PCOS, perimenopause and hormonal hair</h2>
<p>If your facial hair is hormone-driven, you deserve a straight answer rather than a package quote. Laser reduces what
is there now, and it works well — density drops, hairs come back finer, and daily management gets much easier. What it
cannot do is stop your endocrine system from recruiting new follicles.</p>
<p>Practically, that means a longer initial course (often 10–12 sessions) and maintenance every three to four months
rather than once a year. Many clients find that entirely worth it: going from daily tweezing to a session every few
months is a significant change in quality of life. But it is a different promise from the one made for underarms, and
it should be described as one.</p>

<h2>Threading, waxing and why you must stop</h2>
<p>Threading and waxing pull the hair out at the root. A laser needs that root present and attached to work. Stop both
for at least <strong>two weeks</strong> before your first session and for the entire course.</p>
<p>Shaving, trimming and dermaplaning are all fine — they cut at the surface and leave the follicle intact. Shaving
facial hair does not make it grow back thicker; that is a persistent myth about the blunt-cut edge of a shaved shaft,
not a change in the follicle.</p>
""",
         [("Will laser hair removal work on hormonal facial hair?",
           ["It works, but it behaves differently. Conditions like PCOS, perimenopause and thyroid disorders keep "
            "activating new follicles, so the laser is treating a moving target rather than a fixed set of hairs.",
            "Expect a longer course — often 10–12 sessions instead of 6–8 — and ongoing maintenance every few months "
            "rather than annually. The result is still a substantial reduction in density and coarseness; it just is "
            "not a one-and-done."]),
          ("Is laser hair removal safe on the face?",
           ["Yes, with two caveats. Nothing is treated inside the orbital rim — protective eyewear stays on and the "
            "area around the eyes is off limits on any laser, anywhere. And facial skin is thinner and more reactive "
            "than body skin, so settings are more conservative and redness may last a little longer afterwards.",
            "Tell Marzi if you use retinoids, are on acne medication, or have had isotretinoin in the last six months."]),
          ("Can laser hair removal cause more facial hair to grow?",
           ["Paradoxical hypertrichosis is a genuine, rare effect — most often reported on the face and neck in women "
            "with Fitzpatrick III–VI skin and fine dark hair, and generally associated with underpowered treatment: "
            "energy high enough to stimulate a follicle but too low to destroy it.",
            "It is one of the practical reasons to avoid home devices and bargain IPL for facial hair. If you notice "
            "it, say so immediately — the response is to change parameters, not to continue."]),
          ("How often do I need facial sessions?",
           ["Every four weeks. Facial follicles cycle faster than anywhere else on the body, so the interval is "
            "shorter than for legs or back. Stretching it to six or eight weeks means missing the growth-phase window "
            "and wasting sessions."])],
         [("Upper lip", "$80", "$210"), ("Chin", "$85", "$225"), ("Upper lip + chin", "$140", "$375"),
          ("Sideburns", "$90", "$240"), ("Neck", "$120", "$320"), ("Full face", "$225", "$615")], 80)

    area("/mens-laser-hair-removal-kelowna",
         "Men's Laser Hair Removal Kelowna | Back, Chest &amp; Neck",
         "Men's laser hair removal in Kelowna: back $260, chest $200, shoulders $130, plus beard-line shaping. "
         "Coarse hair responds fastest. Free consultation.",
         "For men", "Men's Laser Hair Removal",
         "Back, shoulders, chest, neckline and beard shaping. Coarse hair is what this laser is best at.",
         "Men's laser hair removal in Kelowna at Marzi Skincare &amp; Laser Clinic covers back "
         "(<strong>$260</strong>), chest (<strong>$200</strong>), shoulders (<strong>$130</strong>), neck "
         "(<strong>$120</strong>) and beard-line shaping. Coarse dark male body hair responds faster than most: expect "
         "<strong>6–8 sessions</strong> at 6–8 week intervals for 80–90% reduction. The upper body package (back + "
         "shoulders + chest) is $490 per session.",
         """
<h2>Coarse hair is an advantage</h2>
<p>A diode laser targets melanin in the hair shaft. Thick, dark, deeply rooted hair holds more of it, absorbs more
energy per pulse and conducts more heat down to the follicle. Male back and chest hair is often the most responsive
tissue this laser treats — it is not unusual to see obvious clearing after two sessions.</p>
<p>The corollary is that fine, light or grey hair responds poorly. If your chest hair has already gone grey, no laser on
the market will target it, and any clinic that tells you otherwise is selling you sessions.</p>

<h2>Areas men book most</h2>
<ul>
  <li><strong>Full back</strong> — the most requested. Six to eight sessions, 40 minutes each.</li>
  <li><strong>Shoulders</strong> — usually booked with the back; the boundary is set at your consultation.</li>
  <li><strong>Chest and stomach</strong> — full clearance or density reduction, your choice.</li>
  <li><strong>Neck</strong> — front for razor bumps, back for the hairline.</li>
  <li><strong>Beard line</strong> — shaping the neckline and cheek line rather than removing the beard.</li>
  <li><strong>Ears and nose bridge</strong> — quick, and unexpectedly popular.</li>
</ul>

<h2>Razor bumps and ingrown hairs</h2>
<p>Pseudofolliculitis barbae — chronic razor bumps on the neck and jaw — happens when a curved hair exits the follicle
and re-enters the skin nearby, triggering an inflammatory response. It affects men with coarse curly hair
disproportionately, and men with deeper skin tones most of all.</p>
<p>Reducing the number of active follicles reduces the number of hairs that can do this, which is why laser is one of
the few interventions that addresses the mechanism rather than the aftermath. Because the men most affected tend to
have Fitzpatrick IV–VI skin, the machine matters: an 808&nbsp;nm diode with contact cooling is appropriate here in a
way that broad-spectrum IPL is not.</p>

<h2>Density reduction versus clearance</h2>
<p>Not everyone wants a bare chest. Density reduction is a legitimate goal, and a common one — stopping the course after
three or four sessions leaves a noticeably thinner, softer, more manageable result while keeping hair present.</p>
<p>Say so at your consultation. It changes the plan, the session count and the cost, and it is much easier to stop early
than to put hair back.</p>

<h2>What to expect the first time</h2>
<p>Shave the area the day before. Sessions are straightforward — protective eyewear, a chilled handpiece passing over
the area, a warm snapping sensation. Backs take about 40 minutes; a neckline is under ten.</p>
<p>Afterwards, redness and small bumps around the follicles for a few hours, then nothing. Skip the gym, sauna and hot
tub for 24 hours. If you work outdoors, SPF 30+ on any treated area for two weeks.</p>
""",
         [("Do men get laser hair removal?",
           ["Routinely, and the proportion has climbed steadily. Back and shoulders are the most common requests, "
            "followed by chest, neckline shaping and beard-line definition. Coarse male body hair is among the most "
            "responsive tissue a diode laser encounters."]),
          ("Can I get rid of my back hair permanently?",
           ["Largely, yes. Back hair is typically dark, coarse and densely rooted — close to the ideal target. Most "
            "men see 80–90% reduction after 6–8 sessions, with remaining regrowth noticeably finer.",
            "The one wrinkle is that male body hair remains androgen-responsive throughout life, so new follicles can "
            "activate in your forties and fifties. An annual touch-up handles it."]),
          ("Can laser hair removal fix razor bumps on my neck?",
           ["It is one of the more effective options for pseudofolliculitis barbae — the razor bumps caused by curved "
            "hairs re-entering the skin after shaving, which disproportionately affects men with coarse curly hair and "
            "deeper skin tones.",
            "Reducing follicle density directly reduces the number of hairs that can curl back in. Because it is "
            "concentrated on darker skin, the diode wavelength and contact cooling matter here more than anywhere."]),
          ("Will you shave my beard line without ruining it?",
           ["Beard work is shaping, not clearing. Marzi maps the line with you before anything is treated, and it is "
            "done conservatively across several sessions rather than in one pass, because the change is permanent.",
            "Common requests are lowering a neckline that creeps toward the collar, cleaning up cheek lines, and "
            "reducing density under the jaw to make shaving easier."])],
         [("Full back", "$260", "$700"), ("Shoulders", "$130", "$350"), ("Chest", "$200", "$540"),
          ("Neck", "$120", "$320"), ("Upper body package", "$490", "Quoted")], 260)

    # ================================================================== FAQ
    all_faqs = [
        ("How much does laser hair removal cost in Kelowna?",
         ["Small areas such as the upper lip, chin or underarms run roughly $70–$120 a session across Kelowna clinics; "
          "large areas such as Brazilian, full legs or a full back run $180–$400. At Marzi Skincare &amp; Laser Clinic "
          "the upper lip is $80, underarms $95, Brazilian $180 and full legs $290, with three-session packages "
          "discounted 12–15%.",
          "Judge cost by the full course, not the session. <a href='/pricing'>See the complete price list</a>."]),
        ("How many sessions do I need?",
         ["Six to ten for most areas, spaced four to eight weeks apart. Coarse dark hair on underarms and bikini "
          "clears fastest; fine facial hair and hormone-driven growth need more."]),
        ("Is laser hair removal permanent?",
         ["The accurate term is permanent hair <em>reduction</em>. Properly treated follicles are destroyed and do not "
          "regrow. But hormones can activate follicles that were dormant during your course, which is why most people "
          "book one or two maintenance sessions a year afterwards. Expect 80–90% density reduction, with remaining "
          "regrowth finer and lighter."]),
        ("Does it hurt?",
         ["Most people describe a warm snap rather than pain. The sapphire cooling tip chills the skin before and "
          "after each pulse, and continuous motion passes spread the sensation out rather than concentrating it. "
          "Underarms and Brazilian are the most sensitive; arms and legs are usually very comfortable. Nearly everyone "
          "finds it easier than waxing."]),
        ("Is it safe for dark skin?",
         ["Yes. The Alpha Pro is an 808&nbsp;nm diode laser with contact cooling, safe across Fitzpatrick I–VI "
          "including brown and Black skin. Deeper tones are treated with lower fluence and longer pulse widths. A "
          "patch test is performed on every new client. <a href='/alpha-pro-laser'>More on the technology</a>."]),
        ("Does laser hair removal work on blonde, red, grey or white hair?",
         ["Not reliably, on any machine. Lasers target melanin, and these hair colours contain little or none — there "
          "is nothing for the energy to be absorbed by. Dark blonde and light brown hair often responds partially over "
          "a longer course. Any clinic promising results on white or grey hair is misrepresenting the physics."]),
        ("How should I prepare?",
         ["Shave 12–24 hours before. No waxing, plucking, threading or epilating for two weeks beforehand. Arrive with "
          "clean skin — no lotion, deodorant, makeup or self-tanner on the area. Avoid sun and tanning beds for two "
          "weeks, and mention any photosensitising medication."]),
        ("What happens straight after a session?",
         ["Mild redness and small raised bumps around each follicle for a few hours — that reaction means the energy "
          "was absorbed. Avoid saunas, hot tubs, hot yoga and intense exercise for 24 hours. Use a fragrance-free "
          "moisturiser and SPF 30+ on exposed areas for two weeks."]),
        ("When do the hairs fall out?",
         ["Seven to twenty-one days after each session. It looks like regrowth but is the follicle shedding the dead "
          "shaft. Gentle exfoliation helps clear them."]),
        ("Can I shave between sessions?",
         ["Yes — shaving is the only hair removal method you should use during a course. It cuts at the surface and "
          "leaves the root intact. Waxing, plucking, threading and epilating all remove the target the laser needs."]),
        ("Can I have treatment while pregnant?",
         ["Most clinics, including this one, decline to treat during pregnancy. There is no evidence of harm, but "
          "there is also no research establishing safety, and pregnancy hormones cause hair changes that will reverse "
          "afterwards anyway — so a course started now would partly be wasted. Breastfeeding is generally fine outside "
          "the chest area; mention it at your consultation."]),
        ("What about PCOS or other hormonal conditions?",
         ["Laser works, but it is managing an ongoing process rather than finishing a fixed job. Expect a longer "
          "initial course, often 10–12 sessions, and maintenance every three to four months. The reduction in density "
          "and coarseness is still substantial. <a href='/facial-laser-hair-removal-kelowna'>More on hormonal facial "
          "hair</a>."]),
        ("Can I go in the sun after laser hair removal?",
         ["Keep treated areas out of direct sun for two weeks either side of a session, and use SPF 30+ on anything "
          "exposed. Recently treated skin is more prone to pigment change, and a fresh tan alters the settings that "
          "are safe for your next session. Self-tanner should be avoided for the whole course."]),
        ("What are the risks and side effects?",
         ["Common and temporary: redness, mild swelling around follicles, a sensation like sunburn for a few hours. "
          "Uncommon: blistering, temporary darkening or lightening of the skin, usually where sun exposure or "
          "incorrect settings were involved. Rare: scarring, or paradoxical hair growth on fine facial hair.",
          "Risk drops sharply with correct wavelength selection, adequate cooling, a patch test and an experienced "
          "operator."]),
        ("How is laser different from IPL?",
         ["A laser emits one coherent wavelength; IPL emits broad-spectrum light through a filter. The diode "
          "concentrates all its energy where it is useful, reaches the follicle at depth, and can be run safely on "
          "dark skin. IPL scatters energy, needs more sessions, and carries higher risk beyond Fitzpatrick III."]),
        ("Are home laser devices worth it?",
         ["As maintenance, sometimes. As a replacement for clinical treatment, no. Home units are capped at fluences "
          "under about 10 J/cm² for safety, against 40+ on a clinical diode. That is not enough energy to permanently "
          "disable a coarse follicle, which is why they require indefinite ongoing use."]),
        ("How far apart should sessions be?",
         ["Face and neck every four weeks; underarms and bikini every five to six; arms, legs, back and chest every "
          "six to eight. Booking sooner than the area's cycle wastes a session on follicles that have not re-entered "
          "the growth phase."]),
        ("Can I wear deodorant or makeup afterwards?",
         ["Wait 24 hours before deodorant on treated underarms — the alcohol and aluminium salts sting on reactive "
          "skin. Mineral makeup is usually fine after a few hours if you need it, though bare skin for the first "
          "evening is better."]),
        ("Do you treat teenagers?",
         ["Yes, with parental consent and a consultation first. Laser is often recommended for teenagers with severe "
          "ingrown hairs or hair growth causing genuine distress. Because hormone levels are still changing, results "
          "may need topping up in the early twenties, and that is explained up front."]),
        ("Where is the clinic and how do I book?",
         ["Marzi Skincare &amp; Laser Clinic is at 1856 Ambrosi Rd&nbsp;#120, Kelowna, BC — central, just off "
          "Highway&nbsp;97 near Orchard Park Mall, with free on-site parking. Book online through "
          f"<a href='{BOOK}' rel='noopener' target='_blank'>Vagaro</a>, call "
          f"<a href='tel:{PHONE_T}'>{PHONE_H}</a> or email "
          "<a href='mailto:marzi@marskincare.ca'>marzi@marskincare.ca</a>. The consultation is free and takes about "
          "fifteen minutes. <a href='/contact'>Hours and directions</a>."]),
    ]
    page("/faq",
         "Laser Hair Removal FAQ | Kelowna Clinic Answers 20 Questions",
         "Straight answers on laser hair removal cost, pain, session counts, dark skin safety, hormonal hair and "
         "aftercare, from a Kelowna clinic with 22+ years experience.",
         phero([("/", "Home"), (None, "FAQ")], "Straight answers", "Laser Hair Removal FAQ",
               "Twenty questions clients actually ask, answered without marketing language — including the ones where "
               "the honest answer is \u201cit depends\u201d or \u201cno\u201d.",
               "Laser hair removal takes <strong>6–10 sessions</strong> spaced <strong>4–8 weeks</strong> apart, costs "
               "<strong>$80–$400 per session</strong> depending on area size, produces <strong>80–90% permanent "
               "reduction</strong>, and is safe on <strong>all skin tones</strong> when performed with an 808&nbsp;nm "
               "diode laser and contact cooling. It does not work on white, grey or true red hair, because there is no "
               "melanin for the laser to target.")
         + f"""
<section style="padding-top:.5rem"><div class="container narrow">
  {faq_block(all_faqs, open_first=True)}
  <div class="panel panel-sand rv text-center" style="margin-top:2rem">
    <h3>Question not answered here?</h3>
    <p>Call the clinic and ask Marzi directly. Consultations are free and there is no obligation to book.</p>
    <a href="tel:{PHONE_T}" class="btn btn-primary mt-1">{ic('phone')} {PHONE_H}</a>
  </div>
</div></section>{BAND}""",
         ld=faq_ld(all_faqs))

    # ================================================================== ABOUT
    page("/about",
         "About Marzi Salehi | Kelowna Laser Hair Removal Specialist",
         "Marzi Salehi is a certified medical aesthetician with 22+ years experience, treating every laser hair "
         "removal client personally at her Kelowna clinic.",
         phero([("/", "Home"), (None, "About Marzi")], "Who treats you", "Marzi Salehi",
               "One aesthetician, one machine, twenty-two years. No rotating technicians, no delegated sessions.",
               "<strong>Marzi Salehi</strong> is a certified medical aesthetician with more than <strong>22 "
               "years</strong> of experience, and the owner and sole practitioner at <strong>Marzi Skincare &amp; "
               "Laser Clinic</strong>, 1856 Ambrosi Rd&nbsp;#120 in Kelowna, BC. She specialises in laser hair removal "
               "with the Alpha&nbsp;Pro diode platform, alongside IPL, CryoPen lesion removal and advanced facial "
               "treatments. Every consultation, patch test and session is performed by her personally.")
         + f"""
<section style="padding-top:1rem"><div class="container grid-2">
  <div class="rv prose">
    <h2>Twenty-two years, one pair of hands</h2>
    <p>Marzi has been practising medical aesthetics for over two decades, and laser hair removal is the service the
    clinic is built around. Everything else offered here — IPL, CryoPen, facial work — grew out of the same underlying
    skill: reading skin accurately and choosing settings that respect what it tells you.</p>
    <p>The clinic is deliberately small. There is no front desk handing you to whoever is free, no rotation of junior
    technicians working from a laminated settings chart. You book, you meet Marzi, and Marzi is the person holding the
    handpiece at every session after that.</p>

    <h2>Why that is not just a nice touch</h2>
    <p>Laser settings are not fixed by skin type alone. Fluence, pulse width and repetition rate are adjusted against
    how your skin actually responded last time — how long the redness lasted, how much shed you got, whether density
    dropped as expected, whether you have caught the sun since.</p>
    <p>That information is judgement, and judgement does not transfer well through notes. A practitioner who watched
    your skin at session one reads session six very differently from someone meeting you for the first time. On a
    course that runs eight to fourteen months, continuity compounds.</p>

    <h2>What you can expect</h2>
    <ul>
      <li><strong>An honest session count.</strong> If your hair is grey, you will be told the laser cannot target it, rather than sold a package.</li>
      <li><strong>A patch test before a full session.</strong> Always, for every new client, and mandatory on Fitzpatrick V–VI.</li>
      <li><strong>Settings adjusted to you.</strong> Including seasonally, because Okanagan summers change your baseline skin tone.</li>
      <li><strong>No package pressure.</strong> Three-session packages exist because most people want them, not because you must commit before you know how your skin responds.</li>
    </ul>

    <h2>Where the clinic fits</h2>
    <p>Marzi Skincare &amp; Laser Clinic offers a full range of advanced facial treatments as well — microneedling,
    chemical peels, dermaplaning, CryoPen spot and skin tag removal. Those live on the main clinic site at
    <a href="{B['MAIN_SITE']}" rel="noopener">marskincare.ca</a>.</p>
    <p>This site is specifically about laser hair removal: the technology, the areas, the pricing, and the questions
    people ask before booking. Same clinic, same practitioner, same phone number.</p>
  </div>

  <div class="rv d1"><div class="panel sticky-col">
    <h3>Credentials &amp; focus</h3>
    <ul class="checks mt-1">
      <li>{ic('check')} Certified medical aesthetician</li>
      <li>{ic('check')} 22+ years in practice</li>
      <li>{ic('check')} Laser hair removal — primary specialisation</li>
      <li>{ic('check')} IPL and photo-rejuvenation</li>
      <li>{ic('check')} CryoPen skin tag &amp; spot removal</li>
      <li>{ic('check')} Advanced facial treatments and skin analysis</li>
      <li>{ic('check')} Fitzpatrick I–VI experience</li>
    </ul>
    <hr class="spectrum" style="margin:1.5rem 0">
    <blockquote style="font-family:var(--serif);font-size:1.2rem;line-height:1.35;color:var(--ink)">
      &ldquo;You won't find a better aesthetic medicine clinic in Kelowna.&rdquo;
    </blockquote>
    <p class="muted" style="margin-top:.5rem">— Client review</p>
    <a href="{BOOK}" class="btn btn-primary btn-block mt-2" rel="noopener" target="_blank">Book a free consultation</a>
  </div></div>
</div></section>{BAND}""",
         ld={"@context": "https://schema.org", "@type": "Person", "@id": SITE + "/about#marzi",
             "name": "Marzi Salehi", "jobTitle": "Certified Medical Aesthetician",
             "description": "Certified medical aesthetician with more than 22 years of experience, specialising in "
                            "laser hair removal, IPL, CryoPen lesion removal and advanced facial treatments. Owner and "
                            "sole practitioner at Marzi Skincare & Laser Clinic in Kelowna, BC.",
             "knowsAbout": ["Laser hair removal", "Diode laser", "IPL", "Fitzpatrick skin typing",
                            "Medical aesthetics", "Skin analysis", "CryoPen"],
             "worksFor": {"@id": SITE + "/#clinic"}, "url": SITE + "/about", "telephone": B["PHONE_LD"],
             "workLocation": {"@type": "Place", "address": {
                 "@type": "PostalAddress", "streetAddress": B["ADDR"], "addressLocality": "Kelowna",
                 "addressRegion": "BC", "addressCountry": "CA"}}})

    # ================================================================== CONTACT
    page("/contact",
         "Contact &amp; Book | Laser Hair Removal Clinic Kelowna",
         "Book laser hair removal in Kelowna. Marzi Skincare & Laser Clinic, 1856 Ambrosi Rd #120. "
         "Call (250) 215-4930. Free consultation, open seven days.",
         phero([("/", "Home"), (None, "Contact")], "Visit the clinic", "Book Your Free Consultation",
               "Central Kelowna, free parking, open seven days a week. Book online, call, or send a message below.",
               "<strong>Marzi Skincare &amp; Laser Clinic</strong>, 1856 Ambrosi Rd&nbsp;#120, Kelowna, BC. Phone "
               "<strong>(250) 215-4930</strong>, email <strong>marzi@marskincare.ca</strong>. Open Monday, Tuesday and "
               "Thursday 9:00–17:00, Wednesday 10:30–18:30, Friday 11:00–19:00, Saturday and Sunday 11:00–16:00. "
               "Consultations are free and take about fifteen minutes.")
         + f"""
<section style="padding-top:.5rem"><div class="container">
  <div class="grid-3 rv">
    <a href="{BOOK}" class="tile" rel="noopener" target="_blank" style="background:var(--petrol);border-color:var(--petrol)">
      <span style="color:#fff;display:block">{ic('cal')}</span>
      <div class="lbl" style="color:rgba(255,255,255,.7)">Fastest</div>
      <b style="color:#fff">Book online<br>via Vagaro</b>
    </a>
    <a href="tel:{PHONE_T}" class="tile">{ic('phone')}<div class="lbl">Call the clinic</div><b>{PHONE_H}</b></a>
    <a href="https://www.google.com/maps/search/?api=1&amp;query={LAT},{LNG}" target="_blank" rel="noopener" class="tile">
      {ic('pin')}<div class="lbl">Directions</div><b>1856 Ambrosi Rd #120<br>Kelowna, BC</b></a>
  </div>

  <div class="grid-2" style="margin-top:2.5rem">
    <div class="panel rv">
      <h2 style="font-size:1.6rem">Ask a question</h2>
      <p>Tell Marzi what you would like treated and she will come back with a session estimate and a price.
      No obligation.</p>
      <!-- FormSubmit: confirm the one-time activation email sent to marzi@marskincare.ca before going live. -->
      <form action="https://formsubmit.co/marzi@marskincare.ca" method="POST" style="margin-top:1.25rem">
        <input type="hidden" name="_subject" value="New laser enquiry from the website">
        <input type="hidden" name="_captcha" value="true">
        <input type="hidden" name="_template" value="table">
        <input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off" aria-hidden="true">
        <div class="fld"><label for="f-name">Your name</label>
          <input id="f-name" name="name" type="text" required autocomplete="name" placeholder="First and last name"></div>
        <div class="fld"><label for="f-email">Email</label>
          <input id="f-email" name="email" type="email" required autocomplete="email" placeholder="you@example.com"></div>
        <div class="fld"><label for="f-phone">Phone (optional)</label>
          <input id="f-phone" name="phone" type="tel" autocomplete="tel" placeholder="(250) 000-0000"></div>
        <div class="fld"><label for="f-area">Area you're interested in</label>
          <select id="f-area" name="area">
            <option>Not sure yet — I'd like advice</option>
            <option>Brazilian or bikini</option>
            <option>Underarms</option>
            <option>Legs</option>
            <option>Face — upper lip, chin or full face</option>
            <option>Back, chest or shoulders</option>
            <option>Full body</option>
          </select></div>
        <div class="fld"><label for="f-msg">Anything else Marzi should know</label>
          <textarea id="f-msg" name="message" placeholder="Skin type, hair colour, previous treatments, preferred days…"></textarea>
          <p class="hint">Please don't send detailed medical information by email — bring it to your consultation.</p></div>
        <button type="submit" class="btn btn-primary btn-block">Send enquiry</button>
      </form>
    </div>

    <div class="rv d1">
      <div class="panel">
        <h2 style="font-size:1.6rem">Opening hours</h2>
        <div class="tw"><table class="t"><tbody>
          <tr><td>Monday</td><td class="n">9:00 – 17:00</td></tr>
          <tr><td>Tuesday</td><td class="n">9:00 – 17:00</td></tr>
          <tr><td>Wednesday</td><td class="n">10:30 – 18:30</td></tr>
          <tr><td>Thursday</td><td class="n">9:00 – 17:00</td></tr>
          <tr><td>Friday</td><td class="n">11:00 – 19:00</td></tr>
          <tr><td>Saturday</td><td class="n">11:00 – 16:00</td></tr>
          <tr><td>Sunday</td><td class="n">11:00 – 16:00</td></tr>
        </tbody></table></div>
      </div>
      <div class="panel" style="margin-top:1.25rem">
        <h3>Getting here</h3>
        <p>Ambrosi Rd runs between Harvey Ave (Highway&nbsp;97) and Springfield Rd in central Kelowna, a couple of
        minutes from Orchard Park Mall. Unit&nbsp;#120 is on the ground floor with free on-site parking directly
        outside.</p>
        <p>Clients travel regularly from West Kelowna, Lake Country, Peachland, Winfield, Vernon and Penticton.</p>
      </div>
    </div>
  </div>

  <div class="rv" style="margin-top:2.5rem">
    <iframe class="map" loading="lazy" referrerpolicy="no-referrer-when-downgrade"
      title="Map showing Marzi Skincare &amp; Laser Clinic at 1856 Ambrosi Rd #120, Kelowna BC"
      src="https://www.google.com/maps?q={LAT},{LNG}&amp;z=16&amp;output=embed"></iframe>
  </div>
</div></section>""",
         ld={"@context": "https://schema.org", "@type": "ContactPage", "url": SITE + "/contact",
             "mainEntity": CLINIC})
