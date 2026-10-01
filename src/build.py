# -*- coding: utf-8 -*-
"""Build the UAIFS site (v4.1).
   python3 build.py  ->  ../site/*.html + sitemap.xml + robots.txt   (multi-page, GitHub Pages)
                         ../dist/uaifs-walkthrough.html               (single file for approvers)
   Requires Python 3.12+ (uses nested f-strings)."""
import os, re, json, base64, datetime, html
from content import *

ROOT = os.path.dirname(os.path.abspath(__file__))
CLEAN = os.environ.get("UAIFS_CLEAN") == "1"   # 1 = production files: no review notes or notes toggle
SITE = os.environ.get("UAIFS_OUT") or os.path.join(ROOT, "..", "site")
DIST = os.path.join(ROOT, "..", "dist")
MODE = "multi"
E = html.escape

def L(page, anchor=None):
    if MODE == "multi":
        return f"{page}.html" + (f"#{anchor}" if anchor else "")
    return f"#{page}" + (f"--{anchor}" if anchor else "")

IMG = {}
def img(name):
    return IMG.get(name) if MODE == "bundle" else f"assets/img/{name}"

ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
EXT = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14 4h6v6M20 4l-9 9M18 14v5a1 1 0 01-1 1H5a1 1 0 01-1-1V7a1 1 0 011-1h5"/></svg>'
CHEV = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>'
INFO = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="9"/><path d="M12 11v5M12 8h.01"/></svg>'
CHECK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7"/></svg>'
CAL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/></svg>'
PIN = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s7-6.2 7-12a7 7 0 10-14 0c0 5.8 7 12 7 12z"/><circle cx="12" cy="10" r="2.5"/></svg>'
CLK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>'

def note(txt):
    if CLEAN: return ""
    return f'<div class="rnote"><strong>Review note:</strong> {txt}</div>'

def month(d):
    return datetime.date.fromisoformat(d).strftime("%b %Y")

def cap(s):
    return s[0].upper() + s[1:]

def tx(k):
    return THEME_EXTRA[k]

def hidden_utm():
    return "".join(f'<input type="hidden" name="{u}" data-utm="{u}">' for u in ["utm_source", "utm_medium", "utm_campaign", "utm_content"])

# ------------------------------------------------------------------ chrome
def header():
    tlinks = "".join(
        f'<a href="{L("theme-"+t["slug"])}"><span class="ico" style="color:{t["c"]};background:color-mix(in srgb,{t["c"]} 16%,transparent)">{ICONS[t["key"]]}</span><span><strong>{E(t["short"])}</strong><span>{E(cap(t["full"]))}</span></span></a>'
        for t in THEMES)
    def item(h, a, b):
        return f'<a href="{h}" style="grid-template-columns:1fr"><span><strong>{a}</strong><span>{b}</span></span></a>'
    return f'''<header class="site-header">
  <div class="wrap">
    <a class="brand" href="{L("index")}" aria-label="Unlocking AI for Sustainability home"><img src="{img("uaifs-logo-white.svg")}" alt="Unlocking AI for Sustainability" width="91" height="44"></a>
    <button class="nav-toggle" aria-label="Menu" aria-expanded="false" aria-controls="site-nav"><span></span><span></span><span></span></button>
    <nav class="nav" id="site-nav" aria-label="Main">
      <a href="{L("about")}" data-nav="about">About</a>
      <div class="dd" data-nav="themes"><button type="button" aria-expanded="false">Themes {CHEV}</button>
        <div class="dd-menu">{tlinks}<hr><a class="dd-all" href="{L("themes")}">All themes and the knowledge hub</a></div></div>
      <a href="{L("agenda")}" data-nav="agenda">Agenda</a>
      <a href="{L("speakers")}" data-nav="speakers">Speakers</a>
      <div class="dd" data-nav="partners"><button type="button" aria-expanded="false">Partner with us {CHEV}</button>
        <div class="dd-menu" style="min-width:270px">
          {item(L("partners","why"), "Why partner", "Audience, reach and results")}
          {item(L("partners","fit"), "Find your tier", "Match your goals to a package")}
          {item(L("partners","tiers"), "Tiers and benefits", "Compare what each tier includes")}
          {item(L("partners","current"), "Current partners", "By edition and tier")}
          <hr><a class="dd-all" href="{L("partners","become")}">Enquire about partnering</a>
        </div></div>
      <div class="dd" data-nav="editions"><button type="button" aria-expanded="false">Editions {CHEV}</button>
        <div class="dd-menu" style="min-width:240px">
          {item(L("edition-2026"), "Singapore 2026", "Inaugural edition, 20 November")}
          {item(L("register","newsletter"), "Future editions", "Get notified when announced")}
        </div></div>
      <a class="btn btn--primary btn--sm" href="{L("register")}" data-track="nav_register">Register now</a>
    </nav>
  </div>
</header>'''

SOCIAL = [
    ("https://www.instagram.com/ecobusinesscom", "Instagram", '<path d="M12 2.2c3.2 0 3.6 0 4.9.1 1.2.1 1.8.3 2.2.4.6.2 1 .5 1.4.9.4.4.7.8.9 1.4.2.4.4 1 .4 2.2.1 1.3.1 1.7.1 4.9s0 3.6-.1 4.9c-.1 1.2-.3 1.8-.4 2.2-.2.6-.5 1-.9 1.4-.4.4-.8.7-1.4.9-.4.2-1 .4-2.2.4-1.3.1-1.7.1-4.9.1s-3.6 0-4.9-.1c-1.2-.1-1.8-.3-2.2-.4-.6-.2-1-.5-1.4-.9-.4-.4-.7-.8-.9-1.4-.2-.4-.4-1-.4-2.2C2.2 15.6 2.2 15.2 2.2 12s0-3.6.1-4.9c.1-1.2.3-1.8.4-2.2.2-.6.5-1 .9-1.4.4-.4.8-.7 1.4-.9.4-.2 1-.4 2.2-.4C8.4 2.2 8.8 2.2 12 2.2zm0 3.1a6.7 6.7 0 100 13.4 6.7 6.7 0 000-13.4zm0 11a4.3 4.3 0 110-8.6 4.3 4.3 0 010 8.6zm6.5-11.3a1.6 1.6 0 11-3.2 0 1.6 1.6 0 013.2 0z"/>'),
    ("https://www.facebook.com/EcoBusinessMedia/", "Facebook", '<path d="M22 12a10 10 0 10-11.6 9.9v-7H7.9V12h2.5V9.8c0-2.5 1.5-3.9 3.8-3.9 1.1 0 2.2.2 2.2.2v2.5h-1.2c-1.2 0-1.6.8-1.6 1.6V12h2.7l-.4 2.9h-2.3v7A10 10 0 0022 12z"/>'),
    ("https://twitter.com/ecobusinesscom", "X", '<path d="M18.9 2H22l-7 8 8.2 12h-6.4l-5-6.6L6 22H2.9l7.5-8.6L2.5 2h6.6l4.5 6zM17.8 20.1h1.7L7.3 3.8H5.5z"/>'),
    ("https://www.linkedin.com/company/eco-business", "LinkedIn", LI_SVG[LI_SVG.index('<path'):LI_SVG.index('</svg>')]),
    ("https://www.youtube.com/channel/UCagZ0j4TiZ8l-eQ-i2KZlqA", "YouTube", '<path d="M23 7.5a3 3 0 00-2.1-2.1C19 4.9 12 4.9 12 4.9s-7 0-8.9.5A3 3 0 001 7.5 31 31 0 00.5 12 31 31 0 001 16.5a3 3 0 002.1 2.1c1.9.5 8.9.5 8.9.5s7 0 8.9-.5a3 3 0 002.1-2.1A31 31 0 0023.5 12 31 31 0 0023 7.5zM9.8 15.3V8.7l5.7 3.3z"/>'),
    ("https://www.eco-business.com/", "Eco-Business website", '<path d="M12 2a10 10 0 100 20 10 10 0 000-20zm6.9 6h-2.5a15.6 15.6 0 00-1.2-3.1A8 8 0 0118.9 8zM12 4c.7 1 1.3 2.3 1.6 4h-3.2C10.7 6.3 11.3 5 12 4zM4.3 14a7.9 7.9 0 010-4h2.9a17.6 17.6 0 000 4zm.8 2h2.5a15.6 15.6 0 001.2 3.1A8 8 0 015.1 16zm2.5-8H5.1a8 8 0 013.7-3.1A15.6 15.6 0 007.6 8zM12 20c-.7-1-1.3-2.3-1.6-4h3.2c-.3 1.7-.9 3-1.6 4zm2-6h-4a15.3 15.3 0 010-4h4a15.3 15.3 0 010 4zm.9 5.1a15.6 15.6 0 001.2-3.1h2.5a8 8 0 01-3.7 3.1zM16.8 14a17.6 17.6 0 000-4h2.9a7.9 7.9 0 010 4z"/>'),
]

def footer():
    soc = "".join(f'<a href="{u}" aria-label="{n}" target="_blank" rel="noopener"><svg viewBox="0 0 24 24">{p}</svg></a>' for u, n, p in SOCIAL)
    return f'''<footer class="site-footer">
  <div class="wrap">
    <div class="f-cols">
      <div><h4>Country</h4><a href="{L("about")}">About UAIFS</a><a href="{L("edition-2026")}">Singapore</a></div>
      <div><h4>Editions</h4><a href="{L("edition-2026")}">2026</a></div>
      <div><h4>Programme</h4><a href="{L("speakers")}">Speakers</a><a href="{L("themes")}">Themes</a><a href="{L("agenda")}">Agenda</a></div>
      <div><h4>Partners</h4><a href="{L("partners")}">Partners</a><a href="{L("partners","become")}">Become a Partner</a></div>
      <div><h4>Registration</h4><a href="{L("register","newsletter")}">Newsletter Signup</a><a href="{L("register")}">Register Now</a><a href="{L("register","feedback")}">Feedback</a></div>
    </div>
    <div class="f-bottom">
      <div class="logos"><a href="{L("index")}"><img src="{img("uaifs-logo-white.svg")}" alt="Unlocking AI for Sustainability" width="83" height="40"></a><a href="https://www.eco-business.com/" target="_blank" rel="noopener"><img src="{img("eb-logo-white.svg")}" alt="Eco-Business" height="40"></a></div>
      <p class="copyright">&copy; 2026 Eco-Business</p>
      <div class="f-social">{soc}</div>
    </div>
  </div>
</footer>'''

def cta_band(h, p, primary=("Register now", "register", None), secondary=None, bg="kvbg"):
    sec = f'<a class="btn btn--ghost" href="{L(secondary[1], secondary[2])}">{secondary[0]}</a>' if secondary else ""
    return f'''<section class="cta" aria-label="Call to action"><div class="cta__kv {bg}" aria-hidden="true"></div><div class="wrap">
  <h2>{h}</h2><p>{p}</p>
  <div class="sec-cta"><a class="btn btn--primary" href="{L(primary[1], primary[2])}">{primary[0]}</a>{sec}</div>
</div></section>'''

def phero(crumb, h1, lead, extra="", bg="kvbg", pre=""):
    cr = '<span aria-hidden="true">/</span>'.join([f'<a href="{L(p)}">{E(n)}</a>' if p else f'<span aria-current="page">{E(n)}</span>' for n, p in crumb])
    return f'''<section class="phero"><div class="phero__kv {bg}" aria-hidden="true"></div><div class="wrap">
  {pre}<nav class="crumbs" aria-label="Breadcrumb">{cr}</nav><h1>{h1}</h1><p class="lead">{lead}</p>{extra}
</div></section>'''

# ------------------------------------------------------------------ components
def av(pid):
    s = SPEAKERS[pid]
    return f'<span class="av" title="{E(s["name"])}"><span>{s["mono"]}</span><img data-photo src="{s["photo"]}" alt="" loading="lazy"></span>'

def person(pid, prop):
    s = SPEAKERS[pid]; tag = '<span class="tag-prop">Proposed</span>' if prop else ""
    return f'<div class="person">{av(pid)}<div><strong><a href="{L("speakers", "spk-"+pid)}" style="color:#fff">{s["name"]}</a>{tag}</strong><span>{E(s["role"])}</span></div></div>'

def people_block(sess):
    out = []
    for p in sess.get("people", []):
        if p[0] == "tba":
            out.append(f'<div class="person"><span class="av av--tba">?</span><div><strong>To be announced</strong><span>{E(p[1])}</span></div></div>')
        else:
            out.append(person(p[0], p[1]))
    mod = f'<h4>Moderator</h4><div class="people">{person(sess["mod"][0], sess["mod"][1])}</div>' if sess.get("mod") else ""
    return f'<h4>Speakers</h4><div class="people">{"".join(out)}</div>{mod}'

def theme_chips(keys):
    return '<div class="chips">' + "".join(f'<a class="chip" style="--c:{THEME[k]["c"]}" href="{L("theme-"+THEME[k]["slug"])}"><i></i>{E(THEME[k]["short"])}</a>' for k in keys) + '</div>'

def avatars_row(sess):
    items = []; names = []
    for p in sess.get("people", []):
        if p[0] == "tba": items.append('<span class="av av--tba">?</span>'); names.append("Speakers to be announced")
        else: items.append(av(p[0])); names.append(SPEAKERS[p[0]]["name"])
    if sess.get("mod"):
        items.append(av(sess["mod"][0])); names.append("moderated by " + SPEAKERS[sess["mod"][0]]["name"])
    return f'<div class="avs">{"".join(items)}<span class="avs__txt">{E(", ".join(names))}</span></div>'

def speaker_card(pid, full=True):
    s = SPEAKERS[pid]
    sess = " and ".join(f'<a href="{L("agenda", "s-"+x)}">{E(SESSION[x]["title"])}</a>' for x in s["sessions"])
    topics = "".join(f'<span class="chip">{E(t)}</span>' for t in s["topics"])
    bio = f'<details><summary>Full bio</summary><p>{E(s["long"])}</p></details>' if full else ""
    sid = f' id="spk-{pid}"' if full else ""
    return f'''<article class="spk"{sid}>
  <div class="spk__ph"><span class="spk__mono">{s["mono"]}</span><img data-photo src="{s["photo"]}" alt="Portrait of {E(s["name"])}" loading="lazy"></div>
  <div class="spk__b">
    <h3>{E(s["name"])}</h3><div class="spk__role">{E(s["role"])}</div>
    <p>{E(s["short"])}</p>
    <h4>Speaking on</h4><div class="chips">{topics}</div>
    {bio}
    <div class="spk__foot"><span class="spk-sessions">At the summit: {sess}</span><a class="li" href="{s["li"]}" target="_blank" rel="noopener" aria-label="{E(s["name"])} on LinkedIn">{LI_SVG}</a></div>
  </div>
</article>'''

def ed_tabs(group):
    return f'''<div class="ed-tabs" role="tablist" data-group="{group}" aria-label="Edition">
  <button role="tab" aria-selected="true" data-ed="sg2026">Singapore 2026<small>20 Nov</small></button>
  <button role="tab" aria-selected="false" data-ed="next">Next edition<small>To be announced</small></button>
</div>'''

def ed_empty(group, what):
    return f'''<div class="ed-panel" data-ed-panel="next" data-group="{group}" hidden><div class="ed-empty">
  <h3>The next edition's {what} will appear here</h3>
  <p class="muted">UAIFS is built to run across markets and years, like its sister summit Unlocking Capital for Sustainability. When the next edition is confirmed, its {what} will be published under its own tab.</p>
  <div class="sec-cta"><a class="btn btn--primary" href="{L("register","newsletter")}">Get notified</a><a class="btn btn--ghost" href="{L("partners","become")}">Host an edition in your market</a></div>
</div></div>'''

def flow_bar(compact=False):
    total = sum(f[4] for f in FLOW)
    segs = ""
    for i, (phase, t, desc, ids, mins) in enumerate(FLOW):
        tgt = ids[0]
        segs += f'<a class="flow__seg flow__seg--{i}" style="flex:{mins}" href="{L("agenda","s-"+tgt)}"><span class="flow__t">{t}</span><strong>{E(phase)}</strong>{"" if compact else f"<span>{E(desc)}</span>"}</a>'
    return f'<div class="flow" aria-label="The morning at a glance">{segs}</div>'

def rcard(r, t, i=0, show_theme=False):
    pos = ["30% 40%", "70% 60%", "50% 20%", "15% 80%", "85% 30%"][i % 5]
    th = f'<a class="chip" style="--c:{t["c"]}" href="{L("theme-"+t["slug"])}"><i></i>{E(t["short"])}</a>' if show_theme else ""
    src = "Unlocking Capital for Sustainability" if "unlockingcapital" in r["url"] else "Eco-Business"
    return f'''<article class="rcard" data-theme="{t["key"]}" data-type="{E(r["type"])}">
  <a class="rcard__img img-{tx(t["key"])["img"]}" style="background-position:{pos}" href="{r["url"]}" target="_blank" rel="noopener" tabindex="-1" aria-hidden="true"><span class="rcard__type">{E(r["type"])}</span></a>
  <div class="rcard__b">
    <time datetime="{r["date"]}">{month(r["date"])}</time>
    <h3><a href="{r["url"]}" target="_blank" rel="noopener" data-track="resource_click">{E(r["title"])}</a></h3>
    <p>{E(r["ex"])}</p>
    <div class="rcard__meta"><span class="ptype">{src}</span>{th}<a class="rcard__go" href="{r["url"]}" target="_blank" rel="noopener" aria-label="Read: {E(r["title"])}">Read {EXT}</a></div>
  </div>
</article>'''

def partner_groups():
    groups = ""; small = ""
    for tier in TIERS:
        cells = ""
        for p in tier["partners"]:
            if tier.get("kind") == "anchor":
                cells += f'<div class="plogo plogo--anchor"><em>Anchor partner</em><strong>{E(p[0])}</strong><span>{E(p[1])}</span></div>'
            elif tier.get("kind") == "theme":
                cells += f'<div class="plogo plogo--theme" style="--c:{p[3]}"><em>Sample</em><strong>{E(p[0])}</strong><span>{E(p[1])}</span></div>'
            else:
                cells += f'<div class="plogo"><em>Sample</em><strong>{E(p[0])}</strong></div>'
        if tier["id"] in ("media", "outreach", "networking") or not tier["partners"]:
            cells += f'<a class="plogo plogo--open" href="{L("partners","become")}" data-tier="{tier["id"]}"><strong>Available</strong><span>Enquire about this tier</span></a>'
        desc = f'<span>{E(tier["desc"])}</span>' if tier["desc"] else ""
        g = f'<div class="pgroup"><div class="pgroup__h"><h3>{E(tier["name"])}</h3>{desc}</div><div class="plogos">{cells}</div></div>'
        if tier["id"] in ("anchor", "founding", "thematic"): groups += g
        else: small += g
    return groups + f'<div class="ptiers-sm">{small}</div>'

def theme_tiles(big=False):
    out = ""
    for t in THEMES:
        st = tx(t["key"])["stats"][0]
        out += f'''<a class="ttile" style="--c:{t["c"]}" href="{L("theme-"+t["slug"])}">
  <span class="ttile__img img-{tx(t["key"])["img"]}" aria-hidden="true"></span>
  <span class="ttile__b"><span class="ttile__ico">{ICONS[t["key"]]}</span><h3>{E(t["short"])}</h3><span class="ttile__full">{E(cap(t["full"]))}</span>
  <p>{E(t["one"])}</p>
  {f'<span class="ttile__stat"><b>{E(st[0])}</b> {E(st[1])}</span>' if big else ""}
  <span class="tcol__go">Explore the hub {ARROW}</span></span>
</a>'''
    return f'<div class="ttiles{" ttiles--big" if big else ""}">{out}</div>'


# ---- HubSpot forms (v5). IDs supplied by Eco-Business.
HS_PORTAL = "20783472"
HS_REGION = "na1"
HS_FORMS = {
    "registration": {"id": "684f4eef-fca1-4823-a24e-bab30e2a5ce8", "target": "hs-registration", "label": "registration form", "action": "request your seat"},
    "partner_enquiry": {"id": "a7cc19a5-8795-48a2-81e3-6f3acd54c246", "target": "hs-partner-enquiry", "label": "enquiry form", "action": "enquire about partnering"},
    "newsletter": {"id": "0550a53f-d0eb-428a-8254-efa0afd02b2a", "target": "hs-newsletter", "label": "sign-up form", "action": "sign up for updates"},
}
HS_LOADER = "https://js.hsforms.net/forms/embed/v2.js"
CONTACT_EMAIL = "events@eco-business.com"   # placeholder, TBC

def hubspot_form(name):
    """Embed a HubSpot form (HubSpot v2 embed: portalId, formId, region), with:
       a target container, one shared loader, analytics on submit, a fallback only if the
       loader genuinely fails, and a non-destructive 'still loading' note after 10s."""
    f = HS_FORMS[name]
    tgt = f["target"]
    fail_msg = f'The {f["label"]} did not load. A browser extension may be blocking it. Please refresh the page, or email <a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a> to {f["action"]}.'
    slow_msg = f'Still loading. If the form does not appear, please refresh the page or email <a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a>.'
    return f"""<div class="panel hs-panel hs-panel--{name.replace('_', '-')}">
    <div id="{tgt}" class="hs-embed" data-hs-form="{name}" aria-live="polite"><p class="hs-status">Loading the {f["label"]}…</p></div>
    <noscript><p class="hs-status">Please enable JavaScript to use this form, or email <a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a>.</p></noscript>
    <script>
    (function () {{
      var box = document.getElementById("{tgt}");
      function say(html) {{ var p = box.querySelector(".hs-status"); if (!p) {{ p = document.createElement("p"); p.className = "hs-status"; box.appendChild(p); }} p.innerHTML = html; }}
      function hasForm() {{ return !!box.querySelector("form, iframe"); }}
      function fail() {{ if (!hasForm()) say({json.dumps(fail_msg)}); }}
      function create() {{
        if (!window.hbspt || !window.hbspt.forms) {{ fail(); return; }}
        window.hbspt.forms.create({{
          portalId: "{HS_PORTAL}",
          formId: "{f["id"]}",
          region: "{HS_REGION}",
          target: "#{tgt}",
          onFormReady: function () {{
            var p = box.querySelector(".hs-status"); if (p) p.remove();
            if (window.uaifsHsReady) window.uaifsHsReady("{name}", box);
          }},
          onFormSubmitted: function () {{
            window.dataLayer = window.dataLayer || [];
            window.dataLayer.push({{ event: "uaifs_form_submit", form: "{name}", form_platform: "hubspot", page_id: document.body.getAttribute("data-page-id") || "" }});
          }}
        }});
        setTimeout(function () {{ if (!hasForm()) say({json.dumps(slow_msg)}); }}, 10000);
      }}
      if (window.hbspt && window.hbspt.forms) {{ create(); return; }}
      var s = document.querySelector('script[src="{HS_LOADER}"]');
      if (s && s.getAttribute("data-failed")) {{ fail(); return; }}
      if (!s) {{
        s = document.createElement("script"); s.src = "{HS_LOADER}"; s.charset = "utf-8"; s.async = true;
        s.addEventListener("error", function () {{ s.setAttribute("data-failed", "1"); }});
        document.head.appendChild(s);
      }}
      s.addEventListener("load", create);
      s.addEventListener("error", fail);
    }})();
    </script>
  </div>"""

# ------------------------------------------------------------------ pages
def page_home():
    nums = "".join(f'<div class="num"><div class="num__v" data-to="{n["to"]}" data-dec="{n["dec"]}" data-pre="{n["pre"]}" data-suf="{n["suf"]}">{n["pre"]}0{n["suf"]}</div><div class="num__l">{E(n["l"])}<span class="num__s">{E(n["s"])}</span></div></div>' for n in NUMBERS)
    hl = ""
    for sid in ["fireside", "plenary", "roundtable"]:
        s = SESSION[sid]
        hl += f'<a class="scard" href="{L("agenda","s-"+sid)}"><span class="scard__img img-{tx(s["themes"][0])["img"]}" aria-hidden="true"></span><span class="scard__in"><span class="scard__meta"><time>{s["time"]}</time><span class="fmt fmt--{s["fmt"][0]}">{s["fmt"][1]}</span></span><h3>{E(s["title"])}</h3><p>{E(SESSION_EXTRA[sid]["why"])}</p>{avatars_row(s)}</span></a>'
    spk = "".join(speaker_card(p, full=False) for p in ["jessica", "meaghan", "lawrence"])
    aud = "".join(f'<div><h3>{E(n)}</h3><p>{E(d)}</p></div>' for n, d in STAKEHOLDERS) + '<div><h3>Builders and researchers</h3><p>Turn ideas into implementation alongside the people who will deploy them.</p></div>'
    logo_items = "".join(f'<li>{E(n)}</li>' for n in CLIENT_LOGOS)
    wa = "".join(f'<li>{CHECK}<span><strong>{E(a)}</strong> {E(b)}</span></li>' for a, b in WHY_ATTEND)
    wp = "".join(f'<li>{CHECK}<span><strong>{E(a)}</strong> {E(b)}</span></li>' for a, b in WHY_PARTNER_SHORT)
    return f'''
<section class="hero" aria-label="Introduction">
  <div class="hero__kv kvbg" aria-hidden="true"></div>
  <div class="wrap">
    <p class="hero__eyebrow">Organised by Eco-Business <strong>in partnership with UNDP</strong></p>
    <h1>Unlocking AI for Sustainability Summit</h1>
    <p class="lead">Asia's AI boom is coming with a bill for energy, water, jobs and trust. On 20 November, the tech providers, investors, regulators and sustainability leaders who will settle that bill meet in Singapore to decide how AI and sustainable development advance together.</p>
    <div class="hero__cta"><a class="btn btn--primary" href="{L("register")}" data-track="hero_register">Request your seat</a><a class="btn btn--ghost" href="{L("partners")}" data-track="hero_partner">Partner with us</a></div>
    <dl class="hero__bar">
      <div><dt>Date</dt><dd>{EVENT["date"]}</dd></div>
      <div><dt>Time</dt><dd>9.00am to 2.00pm, GMT+8</dd></div>
      <div><dt>Venue</dt><dd>Singapore, to be confirmed</dd></div>
      <div><dt>Summit starts in</dt><dd class="countdown" data-countdown></dd></div>
    </dl>
    {note("Hero background is the <strong>draft KV</strong> from the partnerships deck cover, with the deck's text removed. Swap for the final KV file (min. 2400px wide).")}
  </div>
</section>

<section class="vid" aria-label="Event video">
  <div class="vid__frame">
    <video class="vid__video" playsinline muted loop preload="none" data-src="" aria-label="Unlocking AI for Sustainability event video"></video>
    <div class="vid__poster kvbg" aria-hidden="true"></div>
    <button class="vid__play" type="button" aria-label="Play the event video" data-track="video_play"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5.5v13l11-6.5z" fill="currentColor"/></svg></button>
    <div class="vid__cap"><strong>Event video</strong><span>Placeholder. Final video file to be supplied.</span></div>
    <p class="vid__msg" hidden>The event video will play here once the file is added.</p>
  </div>
  <div class="wrap">{note("Video slot. Add the file path (MP4, 1920x1080, under 20 MB, or a hosted stream) to <code>data-src</code> on the video element. The frame widens to full-bleed as you scroll, then flows into the numbers.")}</div>
</section>

<section class="numbers" aria-label="Why now, in numbers">
  <div class="wrap">
    <div class="head numbers__head"><span class="kicker">Why now</span><h2>AI's economic promise is undeniable. Its resource and governance costs are not.</h2><p class="lead">Power-hungry infrastructure strains local resources, and weak governance risks deepening digital divides, job displacement and algorithmic bias. For financiers, these unpriced risks create hesitation. The defining challenge for Asia is making sure AI and sustainability advance together, not on separate tracks.</p></div>
  </div>
  <div class="numbers__body">
  <svg class="numbers__trail" viewBox="0 0 1440 160" preserveAspectRatio="none" aria-hidden="true">
    <defs><linearGradient id="trailG" x1="0" x2="1"><stop offset="0" stop-color="#FFC300" stop-opacity="0"/><stop offset=".25" stop-color="#FFC300" stop-opacity=".75"/><stop offset=".7" stop-color="#00BFAD" stop-opacity=".6"/><stop offset="1" stop-color="#28A7E0" stop-opacity="0"/></linearGradient></defs>
    <path stroke="url(#trailG)" d="M0,120 C220,120 300,40 520,60 S860,140 1060,90 S1320,30 1440,40"/>
    <path stroke="url(#trailG)" stroke-width="1" opacity=".5" d="M0,132 C240,128 320,58 540,74 S880,150 1080,104 S1330,46 1440,56"/>
  </svg>
  <div class="wrap"><div class="numbers__grid">{nums}</div></div>
  </div>
  <div class="wrap">
    <div class="numbers__cost"><span>The cost, still unpriced</span><div class="chips"><span class="chip chip--cost">Energy and water strain</span><span class="chip chip--cost">Grid and data centre load</span><span class="chip chip--cost">Job displacement</span><span class="chip chip--cost">Algorithmic bias and digital divides</span></div></div>
    <div class="numbers__foot"><p class="muted" style="margin:0;max-width:52ch">Closing this gap is what the summit is for.</p><div class="sec-cta" style="margin:0"><a class="btn btn--primary" href="{L("about")}">Read about the summit</a><a class="link" href="{L("themes")}">Explore the five themes {ARROW}</a></div></div>
  </div>
</section>

<section class="sec" aria-labelledby="paths-h">
  <div class="wrap">
    <div class="head"><span class="kicker">Get involved</span><h2 id="paths-h">Two ways to be in the room</h2></div>
    <div class="paths">
      <div class="path"><span class="path__tag">For delegates</span><h3>Attend the summit</h3><p class="muted">One morning, in person, with a curated group of senior leaders. Seats are confirmed individually to keep the room relevant.</p><ul class="ticks">{wa}</ul>
        <div class="sec-cta"><a class="btn btn--primary" href="{L("register")}" data-track="path_register">Request your seat</a><a class="link" href="{L("agenda")}">See the agenda {ARROW}</a></div></div>
      <div class="path path--partner"><span class="path__tag">For organisations</span><h3>Partner with UAIFS</h3><p class="muted">Seven tiers, from founding partner to outreach partner, each co-developed with you around your objectives.</p><ul class="ticks">{wp}</ul>
        <div class="sec-cta"><a class="btn btn--primary" href="{L("partners","fit")}" data-track="path_partner">Find your tier</a><a class="link" href="{L("partners","tiers")}">Compare benefits {ARROW}</a></div></div>
    </div>
  </div>
</section>

<section class="sec sec--deep" aria-labelledby="themes-h">
  <div class="wrap">
    <div class="head-row"><div class="head"><span class="kicker">Themes</span><h2 id="themes-h">Five themes, each with a knowledge hub that stays live all year</h2><p class="lead">Each theme is led by the people doing the work, with real use cases, deployable solutions and clear next steps. Between editions, the hubs keep publishing news, research and analysis.</p></div>
    <a class="btn btn--ghost" href="{L("themes")}">Explore all themes</a></div>
    {theme_tiles()}
  </div>
</section>

<section class="sec" aria-labelledby="agenda-h">
  <div class="wrap">
    <div class="head-row"><div class="head"><span class="kicker">Agenda highlights, Singapore 2026</span><h2 id="agenda-h">One morning, built for engagement, not talking heads</h2><p class="lead">Set the context, test the big question, work the problem together, then take a position. Every session is designed for participation.</p></div>
    <a class="btn btn--ghost" href="{L("agenda")}">See the full agenda</a></div>
    {flow_bar(compact=True)}
    <div class="sessions3" style="margin-top:22px">{hl}</div>
  </div>
</section>

<section class="sec sec--deep" aria-labelledby="spk-h">
  <div class="wrap">
    <div class="head-row"><div class="head"><span class="kicker">Featured speakers</span><h2 id="spk-h">The first names on the stage</h2><p class="lead">More speakers from Big Tech, government, finance and start-ups will be announced on a rolling basis. Sign up for updates to hear first.</p></div>
    <div style="display:flex;gap:12px;flex-wrap:wrap"><a class="btn btn--ghost" href="{L("speakers","nominate")}">Nominate a speaker</a><a class="btn btn--primary" href="{L("speakers")}">Meet all speakers</a></div></div>
    <div class="spk3">{spk}</div>
    {note("Speaker photos load from the UCFS image library. They show on the live site; inside this preview, external images are blocked, so monograms appear instead.")}
  </div>
</section>

<section class="sec" aria-labelledby="room-h">
  <div class="wrap">
    <div class="head"><span class="kicker">Who's in the room</span><h2 id="room-h">The right room for the right conversations</h2><p class="lead">A curated group of stakeholders, selected for relevance and seniority, so every conversation is with someone who can act on it.</p></div>
    <div class="aud6">{aud}</div>
    <div class="sec-cta"><a class="btn btn--primary" href="{L("register")}">Request your seat</a><a class="link" href="{L("about","stakeholders")}">What each group gains {ARROW}</a></div>
  </div>
</section>

<section class="logos-sec" aria-labelledby="logos-h">
  <div class="wrap"><h2 id="logos-h">You're in good company.<br>The world's leading organisations work with us.</h2></div>
  <div class="marquee" aria-label="Organisations that work with Eco-Business">
    <ul class="marquee__track">{logo_items}</ul>
    <ul class="marquee__track" aria-hidden="true">{logo_items}</ul>
  </div>
  <div class="wrap logos-sec__cta"><a class="link" href="{L("partners","current")}">See partners for this summit {ARROW}</a><a class="link" href="{L("partners","become")}">Become a partner {ARROW}</a></div>
  <div class="wrap">{note("Organisations that work with Eco-Business, following the EB Enterprise page. Shown as text wordmarks; replace with white SVG logos (brand permission needed). The strip pauses on hover.")}</div>
</section>

<section class="sec" aria-labelledby="eb-h">
  <div class="wrap split" style="align-items:center">
    <div><span class="kicker">Organised by Eco-Business</span><h2 id="eb-h">Asia Pacific's leading sustainable development platform since 2009</h2>
      <p class="lead">UAIFS builds on Unlocking Capital for Sustainability, Eco-Business's flagship summit hosted across six Asian markets since 2018. B Corp certified since 2023.</p>
      <div class="sec-cta"><a class="btn btn--ghost" href="https://www.eco-business.com/" target="_blank" rel="noopener">Visit Eco-Business {EXT}</a><a class="link" href="https://www.unlockingcapitalforsustainability.com/" target="_blank" rel="noopener">Our sister summit, UCFS {EXT}</a></div></div>
    <div class="stats4" style="grid-template-columns:1fr 1fr"><div><b>14.6M+</b><span>Annual pageviews</span></div><div><b>2.4M+</b><span>Annual sessions</span></div><div><b>19%</b><span>Readers who are C-suite, presidents or board members</span></div><div><b>6</b><span>Asian markets hosting UCFS</span></div></div>
  </div>
</section>
'''

def page_about():
    stake = "".join(f'<tr><td>{E(n)}</td><td>{E(d)}</td></tr>' for n, d in STAKEHOLDERS)
    return phero([("Home", "index"), ("About", None)], "Turning AI's opportunity into governed, lasting progress",
                 "AI brings both opportunities and risks to the Sustainable Development Goals. UAIFS convenes the people who can strengthen its governance and unlock its benefits for everyone.",
                 f'<div class="hero__cta"><a class="btn btn--primary" href="{L("register")}">Request your seat</a><a class="btn btn--ghost" href="{L("edition-2026")}">View the 2026 edition</a></div>') + f'''
<section class="sec"><div class="wrap split">
  <div><span class="kicker">The summit</span><h2>A business and policy platform for AI, sustainability and development</h2></div>
  <div><p class="lead" style="color:#dbe6f1">Building on Eco-Business's track record with Unlocking Capital for Sustainability, hosted across six Asian markets since 2018, UAIFS puts AI governance at the centre of the conversation.</p>
  <p class="muted">It convenes tech providers, business leaders, investors, builders, regulators and policymakers to turn ideas on the AI and sustainable development nexus into implementation, in Asia and beyond. The aim is a high-signal, high-engagement platform that drives action on both the innovation and the governance of AI.</p></div>
</div></section>

<section class="sec sec--deep"><div class="wrap">
  <div class="undp"><div class="undp__mark">UNDP</div><div><span class="kicker">In partnership with</span><h3 style="font-size:1.5rem">United Nations Development Programme</h3><p class="muted" style="margin:0">UNDP and Eco-Business announced the Unlocking AI for Sustainability partnership in September 2026, to advance AI governance and the sustainable deployment of the technology across the region.</p></div></div>
  {note("Use UNDP's official logo lock-up (with their brand approval) in place of the placeholder mark.")}
</div></section>

<section class="sec"><div class="wrap">
  <div class="head"><span class="kicker">Objectives</span><h2>What the summit is here to do</h2></div>
  <div class="aud6" style="grid-template-columns:1fr 1fr">
    <div><h3>Shape the narrative</h3><p>On how AI can accelerate climate action, the energy transition, resilient supply chains and sustainable growth, anchored by sound governance principles.</p></div>
    <div><h3>Advance governance frameworks</h3><p>Covering data integrity, transparency, accountability and risk management, alongside AI's energy use and infrastructure efficiency.</p></div>
    <div><h3>Build consensus</h3><p>On responsible deployment standards that align AI innovation with sustainability outcomes across markets and regulatory environments.</p></div>
    <div><h3>Catalyse partnerships</h3><p>Raise awareness of the synergies between AI and sustainability, and spark the dialogue and partnerships that move ideas to impact.</p></div>
  </div>
  <div class="sec-cta"><a class="btn btn--ghost" href="{L("themes")}">Explore the five themes</a></div>
</div></section>

<section class="sec sec--deep" id="stakeholders"><div class="wrap">
  <div class="split" style="margin-bottom:40px;align-items:end"><div><span class="kicker">Who it's for</span><h2>Benefits of participating, by stakeholder group</h2></div>
  <blockquote class="northstar">Our North Star: to convene the right room for the right conversations.</blockquote></div>
  <table class="stake"><thead><tr><th>Stakeholder group</th><th>Benefits of participating</th></tr></thead><tbody>{stake}</tbody></table>
  <p class="muted" style="margin-top:22px;max-width:70ch">Participants are curated for relevance and seniority to enable deeper, more meaningful connections and to advance aligned decision-making.</p>
  <div class="sec-cta"><a class="btn btn--primary" href="{L("register")}">Request your seat</a><a class="link" href="{L("partners","tiers")}">Looking for partnership benefits? {ARROW}</a></div>
</div></section>

<section class="sec"><div class="wrap">
  <div class="head"><span class="kicker">Format</span><h2>Beyond the usual talking heads</h2><p class="lead">Plenaries, fireside chats, debates, roundtables and demo sessions, designed for interaction. Eco-Business co-develops formats with partners around their theme.</p></div>
  <div class="formats">
    <div class="fmt-card"><h3>Fishbowl</h3><p>At UCFS Malaysia, investors and project developers sat on opposite sides to discuss financing bankable projects.</p></div>
    <div class="fmt-card"><h3>Boardroom roundtable</h3><p>At Singapore Maritime Week, Eco-Business convened diverse stakeholders with EDF on energy transition in shipping.</p></div>
    <div class="fmt-card"><h3>Innovation workshop</h3><p>Eco-Business runs Impact Exchange and The Liveability Challenge, Asia's largest climate tech innovation platforms.</p></div>
  </div>
  <div class="sec-cta"><a class="btn btn--ghost" href="{L("agenda")}">See how the 2026 agenda uses them</a></div>
</div></section>

<section class="sec sec--deep"><div class="wrap">
  <div class="head"><span class="kicker">Track record</span><h2>17 years as the region's trusted authority</h2><p class="lead">Trusted news and advisory for a senior audience of multinationals, SMEs, governments, multilateral institutions and civil society. Headquartered in Singapore, with a presence in Beijing, Hong Kong, Manila, Kuala Lumpur, Jakarta and London.</p></div>
  <div class="stats4"><div><b>1.6M+</b><span>Senior-level visitors a year</span></div><div><b>49%</b><span>Readers in senior management</span></div><div><b>115,000+</b><span>Marketing contacts worldwide</span></div><div><b>2023</b><span>B Corp certified</span></div></div>
  <div class="sec-cta"><a class="btn btn--ghost" href="https://www.eco-business.com/" target="_blank" rel="noopener">About Eco-Business {EXT}</a></div>
</div></section>
''' + cta_band("Join us on 20 November 2026", "Registration is open for the inaugural edition in Singapore. Seats are confirmed individually.", primary=("Request your seat", "register", None), secondary=("Become a partner", "partners", None))

def page_themes():
    allposts = []
    for t in THEMES:
        for r in t["resources"]:
            allposts.append((r["date"], t, r))
    allposts.sort(key=lambda x: x[0], reverse=True)
    feed = "".join(rcard(r, t, i, show_theme=True) for i, (d, t, r) in enumerate(allposts))
    fbtn = '<button aria-pressed="true" data-k="theme" data-v="all">All themes</button>' + "".join(f'<button aria-pressed="false" data-k="theme" data-v="{t["key"]}">{E(t["short"])}</button>' for t in THEMES)
    return phero([("Home", "index"), ("Themes", None)], "Five themes that cut across every market and edition",
                 "The themes are evergreen. Each has a knowledge hub that stays live between summits, with the news, research, analysis and conversations that matter for AI and sustainability in Asia Pacific.",
                 f'<div class="hero__cta"><a class="btn btn--primary" href="{L("themes","latest")}">Browse the latest</a><a class="btn btn--ghost" href="{L("register","newsletter")}">Get hub updates</a></div>') + f'''
<section class="sec"><div class="wrap">
  {theme_tiles(big=True)}
  {note("Themes are a CMS collection, so new themes can be added later without a redesign. Theme images are crops of the draft KV; replace with final photography or the designer's illustrations.")}
</div></section>
<section class="sec sec--deep" id="latest"><div class="wrap">
  <div class="head-row"><div class="head"><span class="kicker">Knowledge hub</span><h2>Latest across all themes</h2><p class="lead">News, research, opinion and video from Eco-Business and our partners, newest first.</p></div>
  <a class="btn btn--ghost" href="https://www.linkedin.com/company/eco-business" target="_blank" rel="noopener">Follow on LinkedIn {EXT}</a></div>
  <div class="filters" data-feed="feed-all" role="group" aria-label="Filter by theme">{fbtn}</div>
  <div class="rcards" id="feed-all">{feed}</div>
  {note("Items link out to Eco-Business in a new tab. <strong>For discussion:</strong> duplicate a short summary on-site with a canonical link to the EB original, so visitors stay on UAIFS and EB keeps the SEO credit.")}
</div></section>
<section class="sec"><div class="wrap">
  <div class="head"><span class="kicker">How the hubs work</span><h2>Curated, evergreen and open to partners</h2></div>
  <div class="aud6">
    <div><h3>Curated by Eco-Business</h3><p>Every item is selected by the Eco-Business editorial team for relevance to AI and sustainability in Asia Pacific.</p></div>
    <div><h3>Live all year</h3><p>Hubs keep publishing between editions, so the conversation doesn't stop when the summit ends.</p></div>
    <div><h3>Built with partners</h3><p>Thematic partners contribute reports, case studies and perspectives to their theme's hub.</p></div>
  </div>
  <div class="sec-cta"><a class="btn btn--primary" href="{L("register","newsletter")}">Get hub updates</a><a class="link" href="{L("partners","fit")}">Become a thematic partner {ARROW}</a></div>
</div></section>
''' + cta_band("Put these themes on your agenda", "Join the conversation in Singapore on 20 November 2026.", primary=("Request your seat", "register", None), secondary=("See the agenda", "agenda", None))

def page_theme(t):
    x = tx(t["key"])
    tnav = "".join(f'<a href="{L("theme-"+o["slug"])}"{" aria-current=\"page\"" if o is t else ""}>{E(o["short"])}</a>' for o in THEMES)
    ico = f'<div class="theme-hero-ico" style="--c:{t["c"]}">{ICONS[t["key"]]}</div>'
    qs = "".join(f"<li>{E(q)}</li>" for q in t["questions"])
    at = "".join(f'<a href="{L("agenda","s-"+sid)}"><time>{SESSION[sid]["time"]}</time><span><strong>{E(SESSION[sid]["title"])}</strong><span>{SESSION[sid]["fmt"][1]}, Singapore 2026</span></span></a>' for sid in t["sessions"])
    types = []
    for r in t["resources"]:
        if r["type"] not in types: types.append(r["type"])
    fbtn = '<button aria-pressed="true" data-k="type" data-v="all">All</button>' + "".join(f'<button aria-pressed="false" data-k="type" data-v="{E(y)}">{E(y)}</button>' for y in types) + '<button aria-pressed="false" data-k="type" data-v="LinkedIn">LinkedIn posts</button>'
    res = sorted(t["resources"], key=lambda r: r["date"], reverse=True)
    feed = "".join(rcard(r, t, i) for i, r in enumerate(res))
    feed += '<div class="feed-empty" hidden>No LinkedIn posts in this hub yet. Posts from Eco-Business and partners tagged to this theme will appear here. <a href="https://www.linkedin.com/company/eco-business" target="_blank" rel="noopener">Follow Eco-Business on LinkedIn</a>.</div>'
    feat = ""
    if t.get("featured"):
        f = t["featured"]
        feat = f'<div class="feat-tl"><div><span class="kicker" style="color:var(--yellow)">Featured thought leadership, coming soon</span><h3>{E(f["title"])}</h3><p>{E(f["text"])}</p></div><a class="btn btn--ghost" href="{L("register","newsletter")}">Notify me</a></div>'
    notes = ""
    if any(r.get("pending") for r in res): notes += note("The UNDP partnership release link points to the Eco-Business press release listing; update it to the release's own page once published.")
    if any(r.get("approx") for r in res): notes += note("Please verify the publication month of the US$100 million fund article before launch.")
    stats = "".join(f'<div class="tstat"><b style="color:{t["c"]}">{E(a)}</b><span>{E(b)}</span><small>Source: {E(c)}</small></div>' for a, b, c in x["stats"])
    others = "".join(f'<a class="omini" style="--c:{o["c"]}" href="{L("theme-"+o["slug"])}"><span class="img-{tx(o["key"])["img"]}" aria-hidden="true"></span><strong>{E(o["short"])}</strong></a>' for o in THEMES if o is not t)
    return phero([("Home", "index"), ("Themes", "themes"), (t["short"], None)], E(cap(t["full"])), E(t["one"]),
                 f'<nav class="tnav" aria-label="Themes">{tnav}</nav>', bg="img-" + x["img"], pre=ico) + f'''
<section class="sec"><div class="wrap split">
  <div><span class="kicker">About this theme</span><h2>What this theme covers</h2>{"".join(f'<p class="{"lead" if i==0 else "muted"}"{" style=" + chr(34) + "color:#dbe6f1" + chr(34) if i==0 else ""}>{E(p)}</p>' for i,p in enumerate(t["intro"]))}
    <p class="who"><strong>Who follows this theme:</strong> {E(x["who"])}</p></div>
  <div><h3 style="margin-bottom:16px">Questions we're asking</h3><ul class="qlist">{qs}</ul></div>
</div></section>
<section class="tstats-band" style="--c:{t["c"]}" aria-label="Key figures"><div class="wrap"><span class="kicker">By the numbers</span><div class="tstats">{stats}</div></div></section>
<section class="sec sec--deep" id="hub"><div class="wrap">
  <div class="head-row"><div class="head"><span class="kicker">Resource and knowledge hub</span><h2>Reports, news and analysis</h2><p class="lead">Curated from Eco-Business and partners, newest first.</p></div>
  <a class="btn btn--ghost" href="https://www.linkedin.com/company/eco-business" target="_blank" rel="noopener">Follow on LinkedIn {EXT}</a></div>
  {feat}
  <div class="filters" data-feed="feed-{t["key"]}" role="group" aria-label="Filter by type">{fbtn}</div>
  <div class="rcards" id="feed-{t["key"]}">{feed}</div>
  {notes}
  <div class="sec-cta"><a class="btn btn--ghost" href="{L("register","newsletter")}">Get new content by email</a></div>
</div></section>
<section class="sec"><div class="wrap split">
  <div><span class="kicker">At Singapore 2026</span><h2>Where this theme shows up on 20 November</h2><p class="muted">{E(x["sg"])}</p><div class="at-summit">{at}</div>
    <div class="sec-cta"><a class="btn btn--primary" href="{L("register")}" data-track="theme_register">Request your seat</a><a class="link" href="{L("agenda")}">Full agenda {ARROW}</a></div></div>
  <div><span class="kicker">Thematic partner</span><h2>Own this theme</h2><div class="tpartner" style="margin-bottom:18px"><span><strong>{E(t["partner"])}</strong> (sample)<br>Thematic partner, {E(t["short"])}</span></div>
    <p class="muted">Thematic partners take a plenary seat and a roundtable table on their theme, and publish into this hub all year round. One partner per theme.</p>
    <div class="sec-cta"><a class="btn btn--ghost" href="{L("partners","become")}" data-tier="thematic">Enquire about this theme</a></div></div>
</div></section>
<section class="sec sec--deep sec--tight"><div class="wrap"><h3 style="margin-bottom:16px">Explore the other themes</h3><div class="omini-row">{others}</div></div></section>
'''

def acard(s):
    sid = f'id="s-{s["id"]}"'
    if s.get("minor"):
        return f'<article class="acard acard--minor" {sid}><div class="acard__time"><time>{s["time"]}</time></div><div class="acard__body"><h3>{E(s["title"])}</h3></div></article>'
    ex = SESSION_EXTRA.get(s["id"], {})
    focus = ""
    if s.get("focus"):
        focus = '<div class="focus4">' + "".join(f'<a href="{L("theme-"+THEME[k]["slug"])}" class="focus4__i"><span class="img-{tx(k)["img"]}" aria-hidden="true"></span><strong>{E(n)}</strong><span>{E(d)}</span></a>' for k, n, d in s["focus"]) + '</div>'
    tk = "".join(f"<li>{E(y)}</li>" for y in s.get("takeaways", []))
    body = f'<p>{E(s["body"])}</p>' if s.get("body") else ""
    why = f'<p class="why"><strong>Why it matters:</strong> {E(ex["why"])}</p>' if ex.get("why") else ""
    meta = f'<div class="smeta"><span><b>Duration</b>{s.get("dur","")}</span><span><b>Format</b>{E(ex.get("mode",""))}</span><span><b>Best for</b>{E(ex.get("best",""))}</span></div>' if ex else ""
    left = f'{meta}<p>{E(s["summary"])}</p>{body}{why}{focus}' + (f'<h4>You will leave with</h4><ul class="takeaways">{tk}</ul>' if tk else "") + f'<h4>Themes</h4>{theme_chips(s["themes"])}'
    band = f'<div class="acard__band img-{tx(s["themes"][0])["img"]}" aria-hidden="true"></div>' if s["id"] in ("fireside", "plenary", "roundtable", "debate") else ""
    return f'''<article class="acard" {sid}>
  <div class="acard__time"><time>{s["time"]}</time><small>{s.get("dur","")}</small></div>
  <div class="acard__body">{band}
    <div class="acard__top"><span class="fmt fmt--{s["fmt"][0]}">{s["fmt"][1]}</span></div>
    <h3>{E(s["title"])}</h3>
    <div class="acard__cols"><div>{left}</div><div>{people_block(s)}</div></div>
  </div>
</article>'''

def page_agenda():
    cards = "".join(acard(s) for s in SESSIONS)
    return phero([("Home", "index"), ("Agenda", None)], "Agenda", "A half-day, in-person programme built for participation: a keynote and fireside chat to set the context, a plenary on the energy transition, a hands-on cross-sector roundtable and a closing debate. Choose an edition to see its programme.",
                 f'<div class="hero__cta"><a class="btn btn--primary" href="{L("register")}" data-track="agenda_register">Request your seat</a><a class="btn btn--ghost" href="{L("speakers")}">Meet the speakers</a></div>') + f'''
<section class="sec"><div class="wrap">
  {ed_tabs("agenda")}
  <div class="ed-panel" data-ed-panel="sg2026" data-group="agenda">
    <div class="notice">{INFO}<span><strong>Draft agenda, subject to change.</strong> {EVENT["date"]}, {EVENT["time"]}, {EVENT["venue"]}. Sessions and speakers are being confirmed and timings may shift.</span></div>
    <h2 style="font-size:1.4rem;margin-bottom:14px">The morning at a glance</h2>
    {flow_bar()}
    <p class="muted" style="margin:14px 0 30px;font-size:.95rem">Select a block to jump to its sessions.</p>
    <div class="agenda">{cards}</div>
    {note("Session copy is written from the working programme. Kept <strong>internal</strong>: the three debate motion options and the three candidate summit themes. Moderators marked Proposed are suggestions for Events to confirm.")}
    {note("Suggestion: add a 10.45am demo corner during the tea break, run by the Innovation partner. The deck lists demo sessions as part of the format.")}
  </div>
  {ed_empty("agenda", "agenda")}
</div></section>
''' + cta_band("Secure your seat for 20 November", "Seats are limited and confirmed individually for relevance and seniority.", primary=("Request your seat", "register", None), secondary=("Get programme updates", "register", "newsletter"))

def page_speakers():
    cards = "".join(speaker_card(p) for p in ["jessica", "meaghan", "lawrence"])
    return phero([("Home", "index"), ("Speakers", None)], "Speakers", "Senior leaders from Big Tech, corporates, government, investors and start-ups across Asia Pacific. Speakers are announced on a rolling basis, by edition.",
                 f'<div class="hero__cta"><a class="btn btn--primary" href="{L("register")}">Request your seat</a><a class="btn btn--ghost" href="{L("speakers","nominate")}">Nominate a speaker</a></div>') + f'''
<section class="sec"><div class="wrap">
  {ed_tabs("spk")}
  <div class="ed-panel" data-ed-panel="sg2026" data-group="spk">
    <div class="head"><span class="kicker">Singapore 2026</span><h2>Featured speakers</h2></div>
    <div class="spk3">{cards}</div>
    {note("Bios are adapted from the speakers' UCFS profiles.")}
    <div class="ed-empty" style="margin-top:28px;max-width:none"><h3>More speakers to be announced</h3><p class="muted" style="margin:0 0 16px">Guest-of-honour, plenary panellists, roundtable hosts and debaters will be added here as they confirm.</p><a class="btn btn--ghost btn--sm" href="{L("register","newsletter")}">Tell me when speakers are announced</a></div>
  </div>
  {ed_empty("spk", "speakers")}
</div></section>
<section class="sec sec--deep" id="nominate"><div class="wrap split">
  <div><span class="kicker">Call for speakers</span><h2>Know someone who should be on this stage?</h2><p class="lead">We are inviting nominations across all five themes, especially practitioners with deployments, data and results to share.</p></div>
  <div class="panel"><form class="form" data-demo data-form="speaker_nomination">
    <div class="row-2"><div class="field"><label for="n-name">Nominee's name</label><input id="n-name" required></div><div class="field"><label for="n-org">Organisation and role</label><input id="n-org"></div></div>
    <div class="field"><label for="n-theme">Theme</label><select id="n-theme"><option value="">Choose a theme</option>{"".join(f"<option>{E(t['short'])}</option>" for t in THEMES)}</select></div>
    <div class="field"><label for="n-why">Why this speaker?</label><textarea id="n-why" rows="3" placeholder="What they would bring to the room"></textarea></div>
    <div class="field"><label for="n-email">Your email</label><input id="n-email" type="email" required></div>
    {hidden_utm()}
    <button class="btn btn--primary" type="submit">Send nomination</button>
    <p class="form-note" hidden>Nomination sent. Our programme team will review it. (Demo form: connect to the CRM before launch.)</p>
  </form></div>
</div></section>
''' + cta_band("Hear them in person", "Join the inaugural summit in Singapore on 20 November 2026.", primary=("Request your seat", "register", None))

def benefits_table():
    head = "".join(f'<th>{E(n)}<small>{E(s)}</small></th>' for n, s in TIER_COLS) + '<th class="add">+ Tier<small>Expandable</small></th>'
    rows = ""
    for b in BENEFITS:
        if b[0] == "grp":
            rows += f'<tr class="grp"><td>{E(b[1])}</td>' + "".join("<td></td>" for _ in range(len(TIER_COLS)+1)) + "</tr>"; continue
        cells = ""
        for v in b[1]:
            if v == "Y": cells += '<td><span class="y" aria-label="Included">&#10003;</span></td>'
            elif v == "P": cells += '<td><span class="p" role="img" aria-label="Shared or on request"></span></td>'
            elif v == "N": cells += '<td><span class="n" aria-label="Not included">&ndash;</span></td>'
            else: cells += f'<td><strong style="color:#fff">{E(v)}</strong></td>'
        rows += f'<tr><td>{E(b[0])}</td>{cells}<td class="add"></td></tr>'
    return f'<div class="ptable-wrap" tabindex="0" role="region" aria-label="Partnership benefits by tier"><table class="ptable"><thead><tr><th>Benefit</th>{head}</tr></thead><tbody>{rows}</tbody></table></div>'

def page_partners():
    reach = "".join(f'<div><b>{E(a)}</b><span>{E(b)}</span></div>' for a, b in PARTNER_REACH)
    whyp = "".join(f'<div><h3>{E(a)}</h3><p>{E(b)}</p></div>' for a, b in WHY_PARTNER_SHORT)
    fit = "".join(f'<button type="button" aria-pressed="false" data-fit="{tid}">{E(goal)}</button>' for goal, tid in FIT)
    cards = ""
    for c in TIER_CARDS:
        gets = "".join(f'<li>{CHECK}<span>{E(g)}</span></li>' for g in c["gets"])
        cards += f'''<article class="tier" id="tier-{c["id"]}" data-tier-card="{c["id"]}" style="--c:{c["c"]}">
  <div class="tier__top"><h3>{E(c["name"])}</h3><span class="tier__slots">{E(c["slots"])}</span></div>
  <p class="tier__line">{E(c["line"])}</p>
  <p class="tier__for"><strong>Ideal for</strong> {E(c["for"])}</p>
  <ul class="ticks">{gets}</ul>
  <a class="btn btn--ghost btn--sm tier__cta" href="{L("partners","become")}" data-tier="{c["id"]}" data-track="tier_enquire">Enquire about this tier</a>
</article>'''
    journey = "".join(f'<div class="jstep"><span class="jstep__n">{i+1}</span><h3>{E(h)}</h3><ul class="takeaways">{"".join(f"<li>{E(x)}</li>" for x in items)}</ul></div>' for i, (h, items) in enumerate(JOURNEY))
    faq = "".join(f'<details><summary>{E(q)}</summary><p>{E(a)}</p></details>' for q, a in PARTNER_FAQ)
    sub = "".join(f'<a href="{L("partners",a)}">{b}</a>' for a, b in [("why","Why partner"),("fit","Find your tier"),("tiers","Tiers"),("compare","Compare"),("how","How it works"),("current","Current partners"),("faq","FAQs")])
    return phero([("Home", "index"), ("Partner with us", None)], "Put your organisation at the centre of Asia's AI and sustainability agenda",
                 "UAIFS is organised by Eco-Business in partnership with UNDP. Partners lead the conversation on stage and all year round, in front of the senior leaders who will decide how AI is built, financed and governed across the region.",
                 f'<div class="hero__cta"><a class="btn btn--primary" href="{L("partners","fit")}" data-track="partners_fit">Find your tier</a><a class="btn btn--ghost" href="{L("partners","become")}" data-track="partners_enquire">Talk to our team</a></div>') + f'''
<nav class="subnav" aria-label="On this page"><div class="wrap">{sub}<a class="btn btn--primary btn--sm" href="{L("partners","become")}">Enquire</a></div></nav>

<section class="sec" id="why"><div class="wrap">
  <div class="head"><span class="kicker">Why partner</span><h2>More than a logo on a backdrop</h2><p class="lead">The summit is small and senior by design. Partners get visibility where it counts, a voice in the programme, and a year-round platform through the theme knowledge hubs.</p></div>
  <div class="aud6">{whyp}</div>
  <div class="stats4" style="margin-top:44px">{reach}</div>
  <p class="muted" style="margin-top:18px;font-size:.92rem">Audience figures are Eco-Business platform data from the UAIFS partnerships deck.</p>
</div></section>

<section class="sec sec--deep" id="fit"><div class="wrap">
  <div class="head"><span class="kicker">Find your tier</span><h2>What do you want to achieve?</h2><p class="lead">Choose your main goal and we'll point you to the tier that fits best. Most partners combine elements, so treat this as a starting point.</p></div>
  <div class="fit" role="group" aria-label="Partnership goals">{fit}</div>
  <p class="fit__out" aria-live="polite"></p>
</div></section>

<section class="sec" id="tiers"><div class="wrap">
  <div class="head"><span class="kicker">Partnership tiers</span><h2>Seven ways to partner</h2><p class="lead">UNDP is the summit's anchor partner, sitting outside the commercial tiers. Every other package is tailored to your objectives.</p></div>
  <div class="tiers">{cards}<article class="tier tier--custom" style="--c:var(--line-2)"><div class="tier__top"><h3>Custom package</h3><span class="tier__slots">Any combination</span></div><p class="tier__line" style="color:#fff">Not sure which fits?</p><p class="tier__for">Most partners combine elements across tiers, or partner across several editions and markets. Tell us your goals and we'll shape a package around them.</p><a class="btn btn--primary btn--sm tier__cta" href="{L("partners","become")}" data-track="tier_custom">Build a custom package</a></article></div>
  {note("Slot counts, pass numbers and benefits are <strong>indicative placeholders</strong> for Partnerships to confirm against the rate card.")}
</div></section>

<section class="sec sec--deep" id="compare"><div class="wrap">
  <div class="head"><span class="kicker">Compare</span><h2>Benefits side by side</h2><p class="lead">How benefits scale across tiers. Scroll sideways on smaller screens.</p></div>
  {benefits_table()}
  <div class="legend"><span><span class="y">&#10003;</span> Included</span><span><span class="p"></span> Shared or on request</span><span><span class="n">&ndash;</span> Not included</span><span>Numbers are pass or article counts</span></div>
  <div class="sec-cta"><a class="btn btn--primary" href="{L("partners","become")}">Discuss a package</a><a class="link" href="{L("partners","become")}" data-track="prospectus_request">Request the prospectus {ARROW}</a></div>
</div></section>

<section class="sec" id="how"><div class="wrap">
  <div class="head"><span class="kicker">How it works</span><h2>Your partnership, before, during and after</h2><p class="lead">Partnership doesn't start and end on 20 November. Here is what working with us looks like.</p></div>
  <div class="journey">{journey}</div>
</div></section>

<section class="sec sec--deep" id="current"><div class="wrap">
  <div class="head"><span class="kicker">Current partners</span><h2>Partners by edition</h2></div>
  {ed_tabs("ptn")}
  <div class="ed-panel" data-ed-panel="sg2026" data-group="ptn">
    {partner_groups()}
    {note("All partners except UNDP are <strong>samples from UCFS</strong>, placed only to show the tier layout. Tiles take logo files at launch (SVG, white or full-colour on dark).")}
  </div>
  {ed_empty("ptn", "partners")}
</div></section>

<section class="sec" id="faq"><div class="wrap split">
  <div><span class="kicker">FAQs</span><h2>Questions partners ask</h2><p class="muted">Looking for delegate benefits instead? <a href="{L("about","stakeholders")}">See benefits by stakeholder group</a>.</p></div>
  <div class="faq">{faq}</div>
</div></section>

<section class="sec sec--deep" id="become"><div class="wrap split">
  <div><span class="kicker">Enquire</span><h2>Let's co-develop a format around your objectives</h2><p class="lead">Tell us what you want to achieve. Our partnerships team will reply with the prospectus, rate card and ideas tailored to your goals.</p>
    <ul class="ticks" style="margin-top:20px"><li>{CHECK}<span>Reply within two working days</span></li><li>{CHECK}<span>No obligation</span></li><li>{CHECK}<span>Packages can combine tiers</span></li></ul>
    {note("Confirm the response-time promise with Partnerships before launch.")}
    {note("The enquiry form is the Eco-Business <strong>HubSpot form</strong> (a7cc19a5…). Fields, consent wording and the thank-you message are managed in HubSpot. In this preview, external scripts are blocked, so the fallback message shows; on the live site the form loads here. If the HubSpot form has a tier dropdown, the site's 'Enquire about this tier' links pre-select it.")}</div>
  {hubspot_form("partner_enquiry")}
</div></section>'''

def page_register():
    return phero([("Home", "index"), ("Register", None)], "Request your seat at Singapore 2026", f"{EVENT['date']}, {EVENT['time']}. {EVENT['venue']}. In person only. Seats are confirmed individually to keep the room relevant and senior.",
                 '<div class="hero__bar" style="max-width:520px;grid-template-columns:1fr"><div style="justify-self:start;border:0"><dt>Summit starts in</dt><dd class="countdown" data-countdown></dd></div></div>') + f'''
<section class="sec"><div class="wrap split">
  <div><span class="kicker">Registration</span><h2>Tell us about you</h2><p class="lead">Our team reviews each request and confirms your place by email.</p>
    <ul class="ticks" style="margin-top:20px">{"".join(f'<li>{CHECK}<span><strong>{E(a)}</strong> {E(b)}</span></li>' for a,b in WHY_ATTEND)}</ul>
    {note("Registration now uses the Eco-Business <strong>HubSpot form</strong> (portal 20783472). Fields, consent wording, confirmation message and notifications are managed in HubSpot, not on the site. In this preview, external scripts are blocked, so the fallback message shows instead of the form; on the live site the form loads here.")}</div>
  {hubspot_form("registration")}
</div></section>
<section class="sec sec--deep"><div class="wrap split">
  <div><span class="kicker">FAQs</span><h2>Good to know</h2></div>
  <div class="faq">
    <details><summary>Is there a fee to attend?</summary><p>To be confirmed. Fee structure pending.</p></details>
    <details><summary>Can I attend virtually?</summary><p>No. The 2026 summit is in person only.</p></details>
    <details><summary>Can I register colleagues?</summary><p>To be confirmed. Group registration policy pending.</p></details>
    <details><summary>What is the cancellation policy?</summary><p>To be confirmed.</p></details>
    <details><summary>Where is the venue?</summary><p>In Singapore. The venue will be announced shortly and sent to all registered delegates.</p></details>
    <details><summary>I'm interested in partnering. Where do I start?</summary><p>See <a href="{L("partners")}">Partner with us</a> to compare tiers, or send an enquiry directly.</p></details>
  </div>
</div></section>
<section class="sec" id="newsletter"><div class="wrap split">
  <div><span class="kicker">Newsletter</span><h2>Stay in the loop</h2><p class="lead">Not ready to register? Get updates as speakers, the venue, new editions and knowledge hub content are announced.</p></div>
  {hubspot_form("newsletter")}
</div></section>
<section class="sec sec--deep" id="feedback"><div class="wrap split">
  <div><span class="kicker">Feedback</span><h2>Questions or feedback</h2><p class="lead">For programme, registration or partnership questions, write to the team.</p></div>
  <div><a class="btn btn--primary" href="mailto:events@eco-business.com" data-track="email_team">Email the events team</a>{note("Confirm the correct contact address. events@eco-business.com is a placeholder carried over from v2.")}</div>
</div></section>'''

def page_edition():
    spk = "".join(speaker_card(p, full=False) for p in ["jessica", "meaghan", "lawrence"])
    trows = ""
    for t in THEMES:
        x = tx(t["key"])
        sess = "".join(f'<a class="chip" href="{L("agenda","s-"+sid)}">{SESSION[sid]["time"]} {E(SESSION[sid]["fmt"][1])}</a>' for sid in t["sessions"])
        trows += f'''<article class="etheme" style="--c:{t["c"]}">
  <a class="etheme__img img-{x["img"]}" href="{L("theme-"+t["slug"])}" aria-hidden="true" tabindex="-1"></a>
  <div class="etheme__b"><span class="etheme__ico">{ICONS[t["key"]]}</span><h3>{E(cap(t["full"]))}</h3><p>{E(x["sg"])}</p>
    <div class="etheme__foot"><div class="chips">{sess}</div><a class="link" href="{L("theme-"+t["slug"])}">Theme hub {ARROW}</a></div></div>
</article>'''
    phases = ""
    for i, (phase, t, desc, ids, mins) in enumerate(FLOW):
        if ids == ["break"]: continue
        items = "".join(f'<li><a href="{L("agenda","s-"+sid)}"><time>{SESSION[sid]["time"]}</time> {E(SESSION[sid]["title"])}</a></li>' for sid in ids if sid in SESSION)
        blurb = {0: "The welcome, guest-of-honour keynote and fireside chat frame the stakes: what AI-driven growth means for policy, boards and investors.",
                 1: "A panel of operators, utilities and innovators tests whether AI will speed up or slow down Asia's energy transition.",
                 2: "Tea and conversation with delegates and partners.",
                 3: "Delegates split into four facilitated tables on supply chains, infrastructure, nature and resilience, and investment, then report back.",
                 4: "Two teams argue a live motion and the room votes before and after, or a partner presents a deployable solution.",
                 5: "Closing remarks, then lunch with the whole room."}[i]
        phases += f'<div class="phase phase--{i}"><span class="phase__t">{t}</span><h3>{E(phase)}</h3><p>{E(blurb)}</p><ul>{items}</ul></div>'
    facts = [("Date", EVENT["date"]), ("Time", "9.00am to 2.00pm, GMT+8"), ("Venue", "Singapore, to be confirmed"), ("Format", "Half-day, in person"), ("Audience", "Curated senior leaders"), ("Organisers", "Eco-Business in partnership with UNDP")]
    fx = "".join(f'<div><dt>{a}</dt><dd>{E(b)}</dd></div>' for a, b in facts)
    return phero([("Home", "index"), ("Editions", None), ("Singapore 2026", None)], "Singapore 2026, the inaugural edition",
                 "Bridging technology and sustainable growth: technology providers, sustainability leaders, investors and policymakers forging credible pathways to harness AI for sustainable development.",
                 f'<div class="ed-hero-meta"><span>{CAL}{EVENT["date"]}</span><span>{CLK}9.00am to 2.00pm, GMT+8</span><span>{PIN}Singapore, venue TBC</span></div><div class="hero__cta"><a class="btn btn--primary" href="{L("register")}" data-track="edition_register">Request your seat</a><a class="btn btn--ghost" href="{L("partners")}">Partner with this edition</a></div>', bg="img-edition-banner") + f'''
<nav class="subnav" aria-label="On this page"><div class="wrap"><a href="{L("edition-2026","e-synopsis")}">Synopsis</a><a href="{L("edition-2026","e-themes")}">Themes</a><a href="{L("edition-2026","e-agenda")}">Agenda</a><a href="{L("edition-2026","e-speakers")}">Speakers</a><a href="{L("edition-2026","e-partners")}">Partners</a><a class="btn btn--primary btn--sm" href="{L("register")}">Register now</a></div></nav>
<section class="sec" id="e-synopsis"><div class="wrap split">
  <div><span class="kicker">Synopsis</span><h2>Making AI and sustainability advance together</h2><dl class="facts">{fx}</dl></div>
  <div><p class="lead" style="color:#dbe6f1">AI's economic potential is undeniable. By optimising trade, energy and business efficiency, it is projected to add US$15 trillion to global GDP by 2030, with US$1 trillion in ASEAN alone. AI-driven technologies are also vital to the region's resilience, from optimising energy grids to improving supply chain traceability.</p>
  <p class="muted">Yet this growth brings steep costs. Power-intensive infrastructure and fast-expanding data centres strain local resources, while poor governance risks deepening digital divides, job displacement and algorithmic bias. The defining challenge for Asia is making sure AI and sustainability advance together, giving regulators, technology developers and investors the long-term clarity they need.</p>
  <p class="muted">Organised by Eco-Business in partnership with UNDP, this regional business summit will provide practical, actionable insights on the AI and sustainable development nexus, to translate ideas into implementation.</p>
  {note("Summit theme line is neutral until management confirms one of the three candidate themes in the working programme.")}</div>
</div></section>
<figure class="ebanner"><div class="ebanner__img img-edition-banner" aria-hidden="true"></div><figcaption class="wrap"><strong>One morning. Five themes. The people who decide.</strong><span>Singapore, 20 November 2026</span></figcaption></figure>
<section class="sec sec--deep" id="e-themes"><div class="wrap">
  <div class="head"><span class="kicker">Themes at this edition</span><h2>What Singapore 2026 will tackle</h2><p class="lead">All five themes run through the programme. Here is how each one shows up on the day, and where to find it in the agenda.</p></div>
  <div class="ethemes">{trows}</div>
</div></section>
<section class="sec" id="e-agenda"><div class="wrap">
  <div class="head-row"><div class="head"><span class="kicker">Agenda</span><h2>How the morning flows</h2><p class="lead">The programme moves from context to action in five steps, so delegates leave with positions and partners, not just notes.</p></div><a class="btn btn--ghost" href="{L("agenda")}">Full session details</a></div>
  {flow_bar()}
  <div class="phases">{phases}</div>
</div></section>
<section class="sec sec--deep" id="e-speakers"><div class="wrap"><div class="head-row"><div class="head"><span class="kicker">Speakers</span><h2>Key speakers</h2><p class="lead">More names will be announced as they confirm.</p></div><a class="btn btn--ghost" href="{L("speakers")}">All speakers</a></div><div class="spk3">{spk}</div></div></section>
<section class="sec" id="e-partners"><div class="wrap">
  <div class="head-row"><div class="head"><span class="kicker">Partners</span><h2>Partners for this edition</h2><p class="lead">Organised by Eco-Business in partnership with UNDP, with partners across seven tiers.</p></div><a class="btn btn--primary" href="{L("partners","fit")}">Partner with this edition</a></div>
  {partner_groups()}
  {note("All partners except UNDP are <strong>samples from UCFS</strong>, to show layout.")}
</div></section>
''' + cta_band("Be part of the inaugural edition", "Registration is open for 20 November 2026 in Singapore.", primary=("Request your seat", "register", None), secondary=("Become a partner", "partners", None), bg="img-edition-banner")

PAGES = [
    ("index", "Unlocking AI for Sustainability Summit 2026, Singapore | Eco-Business x UNDP", None, page_home),
    ("about", "About the summit | Unlocking AI for Sustainability", "about", page_about),
    ("themes", "Themes and knowledge hub: AI and sustainability in Asia | UAIFS", "themes", page_themes),
] + [("theme-" + t["slug"], f'{t["short"]}: {cap(t["full"])} | UAIFS knowledge hub', "themes", (lambda t=t: page_theme(t))) for t in THEMES] + [
    ("agenda", "Agenda, Singapore 2026 | Unlocking AI for Sustainability", "agenda", page_agenda),
    ("speakers", "Speakers | Unlocking AI for Sustainability 2026", "speakers", page_speakers),
    ("partners", "Partner with us: tiers and benefits | Unlocking AI for Sustainability", "partners", page_partners),
    ("register", "Register, 20 November 2026 | Unlocking AI for Sustainability", None, page_register),
    ("edition-2026", "Singapore 2026 edition | Unlocking AI for Sustainability", "editions", page_edition),
]

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500;600;700;800&family=Source+Sans+3:wght@400;600;700&display=swap" rel="stylesheet">'
NOTES_BTN = '<button class="notes-toggle" type="button" aria-pressed="false"><svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2.2"><circle cx="12" cy="12" r="9"/><path d="M12 11v5M12 8h.01"/></svg> Show review notes</button>'
NOTES_BTN = "" if CLEAN else NOTES_BTN
GTM = '<!-- Analytics: paste the Google Tag Manager (GA4) snippet here. The site pushes events to window.dataLayer (see README, Analytics plan). -->'

def meta_desc(pid):
    if pid.startswith("theme-"):
        t = next(t for t in THEMES if "theme-" + t["slug"] == pid)
        return f'{cap(t["full"])}: {t["one"]} News, research and analysis from the UAIFS knowledge hub.'
    return META.get(pid, META["index"])

def jsonld(pid, title):
    org = {"@type": "Organization", "name": "Eco-Business", "url": "https://www.eco-business.com/"}
    data = [{"@context": "https://schema.org", "@type": "WebPage", "name": title, "url": SITE_URL + (pid + ".html" if pid != "index" else ""), "publisher": org}]
    if pid in ("index", "edition-2026", "agenda", "register"):
        data.append({"@context": "https://schema.org", "@type": "Event", "name": "Unlocking AI for Sustainability Summit 2026",
                     "startDate": "2026-11-20T09:00:00+08:00", "endDate": "2026-11-20T14:00:00+08:00",
                     "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode", "eventStatus": "https://schema.org/EventScheduled",
                     "location": {"@type": "Place", "name": "Singapore (venue to be confirmed)", "address": {"@type": "PostalAddress", "addressCountry": "SG"}},
                     "image": [SITE_URL + "assets/img/kv-draft.jpg"], "description": META["index"],
                     "organizer": org, "url": SITE_URL + "edition-2026.html"})
    return '<script type="application/ld+json">' + json.dumps(data) + '</script>'

def head(pid, title, extra=""):
    desc = meta_desc(pid)
    url = SITE_URL + (pid + ".html" if pid != "index" else "")
    return f'''<!DOCTYPE html>
<html lang="en-SG">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<link rel="canonical" href="{url}">
<meta property="og:site_name" content="Unlocking AI for Sustainability"><meta property="og:type" content="website"><meta property="og:url" content="{url}">
<meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}"><meta property="og:image" content="{SITE_URL}assets/img/og-share-draft.jpg"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@ecobusinesscom">
<meta name="theme-color" content="#061020">
{jsonld(pid, title)}
{GTM}
{FONTS}
{extra}
</head>'''

def build_multi():
    global MODE; MODE = "multi"
    os.makedirs(SITE, exist_ok=True)
    for pid, title, navkey, fn in PAGES:
        body = fn()
        hdr = header()
        if navkey in ("about", "agenda", "speakers"):
            hdr = hdr.replace(f'data-nav="{navkey}"', f'data-nav="{navkey}" class="is-active" aria-current="page"', 1)
        elif navkey:
            hdr = hdr.replace(f'<div class="dd" data-nav="{navkey}">', f'<div class="dd is-active" data-nav="{navkey}">')
        doc = head(pid, title, '<link rel="icon" type="image/svg+xml" href="assets/img/favicon.svg">\n<link rel="stylesheet" href="assets/css/style.css">') + f'''
<body data-page-id="{pid}">
<a class="skip" href="#main">Skip to content</a>
{hdr}
<main id="main">{body}</main>
{footer()}
{NOTES_BTN}
<script src="assets/js/main.js"></script>
</body>
</html>'''
        with open(os.path.join(SITE, pid + ".html"), "w") as f: f.write(doc)
    today = datetime.date.today().isoformat()
    urls = "".join(f"<url><loc>{SITE_URL}{'' if p == 'index' else p + '.html'}</loc><lastmod>{today}</lastmod></url>" for p, *_ in PAGES)
    with open(os.path.join(SITE, "sitemap.xml"), "w") as f:
        f.write(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>')
    with open(os.path.join(SITE, "robots.txt"), "w") as f:
        f.write(f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}sitemap.xml\n")

def b64(path, mime):
    with open(path, "rb") as f: return f"data:{mime};base64," + base64.b64encode(f.read()).decode()

def build_bundle():
    global MODE; MODE = "bundle"
    imgdir = os.path.join(SITE, "assets", "img")
    IMG["uaifs-logo-white.svg"] = b64(os.path.join(imgdir, "uaifs-logo-white.svg"), "image/svg+xml")
    IMG["eb-logo-white.svg"] = b64(os.path.join(imgdir, "eb-logo-white.svg"), "image/svg+xml")
    css = open(os.path.join(SITE, "assets", "css", "style.css")).read()
    css = re.sub(r"url\(\.\./img/([\w.-]+\.jpg)\)", lambda m: f"url({b64(os.path.join(imgdir, m.group(1)), 'image/jpeg')})", css)
    js = open(os.path.join(SITE, "assets", "js", "main.js")).read()
    mains = ""
    for pid, title, navkey, fn in PAGES:
        sec = f' data-section="{navkey}"' if navkey else ""
        mains += f'<main data-page="{pid}" data-title="{E(title)}"{sec} hidden>{fn()}</main>\n'
    doc = head("index", "Unlocking AI for Sustainability | Website walkthrough v4", f"<style>{css}</style>") + f'''
<body>
{header()}
{mains}
{footer()}
{NOTES_BTN}
<script>{js}</script>
</body>
</html>'''
    os.makedirs(DIST, exist_ok=True)
    with open(os.path.join(DIST, "uaifs-walkthrough.html"), "w") as f: f.write(doc)
    return len(doc)

if __name__ == "__main__":
    build_multi()
    if CLEAN:
        print("built", len(PAGES), "clean pages ->", SITE); raise SystemExit
    n = build_bundle()
    print("built", len(PAGES), "pages; bundle bytes", n)
