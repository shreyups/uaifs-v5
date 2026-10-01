# UAIFS website — Sitemap and change log (v5)

**Status:** v5 draft, 30 September 2026. Page list unchanged; v5 replaces the registration, partner enquiry and newsletter forms with Eco-Business HubSpot forms.
**Sister site:** follows the structure of unlockingcapitalforsustainability.com (UCFS); footer kept identical in structure.
**Confidence:** about 90% confirmed. Open items are listed at the end.

## 1. Sitemap v3

```
Home  (index.html)
│
├── About  (about.html)
│     ├── The summit
│     ├── In partnership with UNDP
│     ├── Objectives
│     ├── Benefits by stakeholder group   ← moved from Partners  (#stakeholders)
│     ├── Format
│     └── Track record
│
├── Themes ▾  (themes.html — evergreen hub; cuts across all markets and editions)
│     ├── AI Infrastructure      (theme-infrastructure.html)
│     ├── Climate & Energy       (theme-climate-energy.html)
│     ├── Supply Chains          (theme-supply-chains.html)
│     ├── Finance & Investment   (theme-finance.html)
│     └── Responsible AI         (theme-responsible-ai.html)
│           Each theme page contains: write-up · questions · resource and knowledge hub
│           (news, reports, white papers, video, LinkedIn; newest first; filterable) ·
│           where the theme appears in the current agenda · thematic partner slot
│
├── Agenda  (agenda.html — tabbed by edition)
│     └── Singapore 2026: one card per session (#s-welcome, #s-fireside, #s-plenary, #s-roundtable, #s-debate …)
│
├── Speakers  (speakers.html — tabbed by edition)
│     ├── Featured speakers with bio, topics, sessions (#spk-jessica, #spk-meaghan, #spk-lawrence)
│     └── Call for speakers form (#nominate)
│
├── Partner with us ▾  (partners.html — sticky on-page menu)
│     ├── Why partner — value, audience and reach (#why)
│     ├── Find your tier — goal selector that recommends a tier (#fit)
│     ├── Tiers — seven tier cards + custom package (#tiers)
│     ├── Compare — benefits table (#compare)
│     ├── How it works — before, on the day, after (#how)
│     ├── Current partners — by edition and tier (#current)
│     ├── FAQs (#faq)
│     └── Enquire — form, pre-filled with the chosen tier (#become)
│
├── Editions ▾
│     ├── Singapore 2026  (edition-2026.html — synopsis, themes, speakers, agenda, partners)
│     └── Future editions  (→ newsletter signup until announced)
│
└── Register  (register.html)
      ├── Registration form
      ├── FAQs
      ├── Newsletter (#newsletter)
      └── Feedback (#feedback)

Footer (same columns as UCFS)
Country: About UAIFS, Singapore · Editions: 2026 · Programme: Speakers, Themes, Agenda ·
Partners: Partners, Become a Partner · Registration: Newsletter Signup, Register Now, Feedback ·
UAIFS + Eco-Business logos · © 2026 Eco-Business · social icons
```

### How "by edition" works
Agenda, Speakers and Partners each carry an edition switcher. Content is tagged with an edition (market + year) in the CMS, exactly as UCFS tags content by market and year. Themes are **not** tagged by edition: they are evergreen and shared across all editions. Adding "Jakarta 2027", for example, means adding one edition record and tagging sessions, speakers and partners to it — no new templates.

### Partner tiers (order as requested; expandable)
1. In partnership with — UNDP (anchor partner)
2. Founding partner
3. Thematic partners — one per theme (5)
4. Innovation partner
5. Networking partners (3)
6. Venue partner
7. Media partner
8. Outreach partners
9. Additional tier slot — tiers are a CMS collection; the benefits table has a "+ Tier" column to show expansion.

All partner names except UNDP are **samples taken from UCFS**, used only for layout.

## 2-v5. Changes in v5

| Request | What changed |
|---|---|
| Replace every instance of the registration form with the HubSpot embed | The mockup's registration form (Register page, the target of every "Register now" and "Request your seat" button) is replaced with the Eco-Business HubSpot form: portal `20783472`, form `684f4eef-fca1-4823-a24e-bab30e2a5ce8`, region `na1`. The embed is a reusable component (`hubspot_registration()` in `src/build.py`), so any future placement uses the same code |
| Replace every instance of the partnerships form with the HubSpot embed | The "Enquire" form on Partner with us (`#become`) is replaced with the Eco-Business HubSpot form `a7cc19a5-8795-48a2-81e3-6f3acd54c246` (portal `20783472`, region `na1`). This is the target of every "Enquire about this tier", "Available" tile, "Talk to our team", "Become a partner" and "Enquire about this theme" link |
| Replace every instance of the newsletter form with the HubSpot embed | The newsletter form on the Register page (`#newsletter`) is replaced with the Eco-Business HubSpot form `0550a53f-d0eb-428a-8254-efa0afd02b2a` (portal `20783472`, region `na1`). It is the target of every newsletter link: footer "Newsletter Signup", Editions → "Future editions", "Get notified", "Get hub updates", "Get new content by email", "Notify me" and "Tell me when speakers are announced". It uses the shared `hubspot_form()` component (`HS_FORMS["newsletter"]`). The script address was corrected again, because the pasted code had the same Slack-link problem. The Register page shares one HubSpot loader between its two forms. Reserved panel height is now set per form, so the short sign-up form isn't padded |
| Shared HubSpot component (after the registration diagnosis) | Both forms now use one component, `hubspot_form(name)` in `src/build.py`, configured in `HS_FORMS`:<br>• the loader script loads once, even with two forms in the walkthrough bundle;<br>• "did not load" shows **only** if HubSpot's script fails to load;<br>• a slow form gets a "Still loading" note after 10 seconds, which never replaces a form that arrives later. This fixes the risk in the first v5 build, where an 8-second timeout could overwrite a slow form |
| Tier pre-selection with HubSpot | Tier links store the chosen tier. When the HubSpot form is ready, the site selects that tier, provided the form has a dropdown whose name or options mention the tier, for example "Thematic partner". This works within the page and across pages. It is not possible if HubSpot renders the form in an iframe |

**Implementation notes** (both forms):
- **Script address.** The registration embed code was pasted with its script address converted into a Slack link (`[//js.hsforms.net/...](https://eco-business.slack.com//...)`). The partner embed code uses `//js.hsforms.net/...`, which fails when a page is opened from disk. The site uses `https://js.hsforms.net/forms/embed/v2.js` for both.
- **Additions to HubSpot's standard code:**
  - `target` places the form inside the existing panel;
  - `onFormReady` removes the loading text;
  - `onFormSubmitted` pushes the `uaifs_form_submit` analytics event (`form: registration`, `partner_enquiry` or `newsletter`, `form_platform: hubspot`).
- **Fallback.** If the HubSpot script is blocked, a message asks visitors to refresh or email the team. If it's slow, a "Still loading" note appears after 10 seconds without removing anything.
- **Styling.** Dark-theme CSS for HubSpot's form markup (`.hs-embed` rules in `style.css`) matches the site's inputs and gradient button. It applies when HubSpot renders the form inline. If the portal renders forms in an iframe, set matching colours and fonts in HubSpot's form style settings.
- **Fields and messages.** Field list, required fields, consent wording, the thank-you message and notification emails are now managed **in HubSpot**, not in the site code.
- **Preview limitation.** The published walkthrough blocks external scripts, so it shows the fallback message instead of the form. The form loads on the real site (GitHub Pages, or the CMS build).

## 2b. Changes in the v4.1 round

### Whole site: copy, findability, SEO and analytics
| Area | What changed |
|---|---|
| Copy | Sharper, benefit-led headlines and CTAs across the site ("Request your seat", "Find your tier"). Every page ends in a clear next step. |
| Findability | New homepage "Two ways to be in the room" block splits delegates and partners into their own paths. "Partners" in the main menu is now "Partner with us", with a dropdown straight to Why partner, Find your tier, Tiers and Current partners. |
| SEO | Unique page titles and meta descriptions; canonical URLs; Open Graph and X (Twitter) cards; schema.org Event and WebPage data (enables Google event rich results); `sitemap.xml` and `robots.txt`; breadcrumbs; one H1 per page; skip link; `lang="en-SG"`. |
| Analytics | Ready for GA4 via Google Tag Manager (see plan below). UTM parameters are captured and passed into every form, so registrations and enquiries can be traced to campaigns. |

### Themes and knowledge hub
- Each theme now has its own image (crops of the draft KV) on theme tiles, page heroes and resource cards.
- Theme pages now include:
  - a "By the numbers" band with two sourced figures;
  - a "Who follows this theme" line;
  - a Singapore 2026 focus, with links to the relevant sessions;
  - a strip linking to the other themes.
- The resource hub is now a card grid, in the style of UCFS's insights section, with type filters.
- The themes landing page has bigger tiles, each with a key figure, plus a "How the hubs work" section.
- Every figure comes from the Eco-Business articles linked in the hubs or from the partnerships deck.

### Agenda
- "The morning at a glance" timeline groups the programme into six blocks: Set the context, Test the big question, Break, Work the problem, Take a position and Connect. Each block links to its sessions.
- Session cards now show duration, format and who the session is best for, plus a "Why it matters" line.
- Major sessions have an image band.
- The roundtable's four focus tables are shown as picture cards that link to the matching theme hubs.

### Partners (restructured)
- The page is reordered to follow a partner's decisions: why partner, then which tier, then what's included, then how it works, then who's already in, then enquire.
- A sticky on-page menu is added.
- The "Find your tier" goal selector highlights the recommended tier.
- There are seven tier cards covering:
  - who each tier is for;
  - headline benefits;
  - available slots;
  - an enquire button that pre-fills the form with that tier.
  A dashed "custom package" card sits alongside them.
- New sections:
  - "How it works" (before, on the day, after);
  - partner FAQs;
  - audience reach figures;
  - a prospectus request.

### Singapore 2026 edition page
- Visuals: a new hero image, a full-width banner and picture rows for each theme.
- The Synopsis gains an "at a glance" facts panel.
- Themes: each theme has an expanded write-up of what Singapore 2026 will tackle, with links to its sessions and hub.
- Agenda: a "How the morning flows" timeline plus five step cards explaining each block and its sessions.
- Partners: the full tier-by-tier partner list is shown at the bottom of the page.

## 2c. Analytics plan (GA4 via Google Tag Manager)
Paste the GTM container snippet where marked in each page's `<head>`. The site pushes these events to `dataLayer`:

| Event | When | Parameters |
|---|---|---|
| `uaifs_cta_click` | Any button or link CTA | `cta_id` (e.g. hero_register, tier_enquire), `cta_text`, `section`, `page_id` |
| `uaifs_form_submit` | Registration, newsletter, partner enquiry, speaker nomination | `form` |
| `uaifs_fit_select` | Partner tier finder | `goal`, `tier` |
| `uaifs_filter_use` | Knowledge hub filters | `filter`, `value` |
| `uaifs_edition_tab` | Edition tabs | `edition` |
| `uaifs_outbound_click` | Links to Eco-Business and other sites | `url`, `link_text` |
| `uaifs_video_play` | Event video | none |

Suggested key events (conversions) in GA4: `uaifs_form_submit` where form = registration or partner_enquiry.
Suggested reporting: registrations and enquiries by UTM campaign; hub-to-register journeys; tier finder selections vs enquiries.

## 2a. Changes in v4 (homepage)

| Request | What changed |
|---|---|
| Space above the numbers for the event video, scrolling seamlessly | New video section between the hero and the numbers. The frame starts inset with rounded corners and widens to full-bleed as you scroll, then flows into the numbers with no break. Currently a placeholder poster with a play button; add the MP4 path to `data-src` on the video element (1920x1080, under 20 MB) or swap in a hosted stream. |
| Remove "Why now" and put its text in the numbers section | "Why now" headline and paragraph now introduce the numbers band. The "cost, still unpriced" list is a row of chips under the numbers, followed by the CTAs. The separate section and its card are gone. |
| Replace partners with scrolling logos (EB Enterprise style) | "You're in good company. The world's leading organisations work with us." with a continuously scrolling strip of 25 organisations (ABB to Wilmar). Pauses on hover; shows as a static grid for visitors who reduce motion. Names are text wordmarks until white SVG logo files are supplied (brand permission needed). Links below to this summit's partners and Become a partner. |
| Remove "Be in the room that shapes how AI and sustainability advance together" | Removed from the homepage. The page now ends with the Eco-Business section, then the footer. |

## 2. Changes from v2 (per review comments)

| Comment | What changed |
|---|---|
| Homepage: CTAs clear for all sections | Every section ends with a primary or secondary CTA. |
| Homepage: KV draft in background | Hero uses the KV from the partnerships deck cover, with the deck's text digitally removed (`assets/img/kv-draft.jpg`). Replace with final KV file. |
| Homepage: 5 topics as columns, not rows | Five columns, each linking to its theme hub. |
| Featured speakers: write-up, role, background, topics, photo | Jessica Cheam, Meaghan See, Lawrence Wong (Eco-Business). Bios adapted from UCFS profiles. Photos load from the UCFS image library. Lawrence Peters (UNDP) from v2 removed. |
| Partners, agenda, speakers split by edition | Edition tabs on all three pages + new edition hub page. |
| Themes and agenda on separate pages | `themes.html` and `agenda.html`. |
| Themes: own page, 5 subpages in dropdown, shorter names | Done. Short names in menu, full names on pages. |
| Themes: resource hub, 3 pieces each, chronological, blog format | 15 real Eco-Business items, newest first, with type filters and a LinkedIn slot. Links open Eco-Business in a new tab. |
| Thought leadership e.g. principles of good AI governance | Featured placeholder on the Responsible AI hub. |
| Agenda: cards selling each session, speaker pictures, more substance | Cards with description, "you will leave with", themes, speakers and moderator photos. |
| Partnerships: tiers + benefits table + room to expand | Done (see above). |
| Stakeholder benefits → About | Moved to About `#stakeholders`. |
| Dark, clean, sleek, key numbers prominent and dynamic | Dark theme from KV; key-numbers band with count-up animation; live countdown. |
| Brand guide wins on conflict | Palette is the 2014 guide's primary, secondary and accent colours only; dark navy taken from the KV (the guide has no dark colour). |
| EB logo as is; event logo like UCFS | EB logo unchanged. UAIFS logo kept from v2 (UCFS lock-up style). |
| Footer same | Same columns and order as UCFS. The footer screenshot was not received; matched against the live UCFS site. |

### Also added
- **Review notes toggle** (bottom-left): shows yellow notes on decisions, placeholders and TBCs for the approval team. Remove before launch (delete the `NOTES_BTN` line and `.rnote` blocks in `src/build.py`).
- **Generator** (`src/`): all copy lives in `src/content.py`; header and footer are shared. Run `python3 src/build.py` to rebuild every page. This replaces hand-editing the nav on each page.
- **Typography:** Montserrat (matches the logo lettering) and Source Sans 3 (open-source sibling of the guide's Myriad Pro), via Google Fonts.

## 3. Kept internal (not published)
- The three plenary debate motions.
- The three candidate summit themes (A/B/C).

## 4. Open items for management

| # | Item | Owner |
|---|---|---|
| 1 | Resource hub: link out to EB (current) or duplicate summaries on-site with a canonical link to EB? **Recommend duplicate.** | Management / Editorial |
| 2 | Summit theme wording (1 of 3 options) | Management / Events |
| 3 | Venue, fee structure, cancellation and group-registration policy | Events |
| 4 | Guest-of-honour; confirm proposed moderators (Jessica: fireside; Lawrence: plenary; Meaghan: roundtable) | Events |
| 5 | Tier benefits and pass counts in the table are indicative — replace with rate card | Partnerships |
| 6 | Real partner list and logo files (SVG, dark-background versions); UNDP logo with brand approval | Partnerships |
| 7 | Final KV (min. 2400px wide) | Design |
| 8 | Contact email (events@eco-business.com is a placeholder) | Events |
| 9 | UNDP partnership press release URL (currently points to EB press release listing); verify month of the "US$100 million fund" article | Editorial |
| 10 | Connect registration, newsletter, nomination and partner forms to CRM/email platform | Web |
| 13 | Final domain (canonical URLs and sitemap use unlockingaiforsustainability.com as a placeholder in `src/content.py`, SITE_URL); GTM container ID | Web / Marketing |
| 14 | Final theme photography or illustrations to replace KV crops; confirm tier slot counts and partner response time (two working days) | Design / Partnerships |
| 12 | Event video file (MP4 or hosted stream) and logo files for the 25 organisations in the homepage strip | Marketing / Design |
| 11 | Optional: demo corner during the 10.45am tea break, run by the Innovation partner | Events |
