# Unlocking AI for sustainability (UAIFS) website, version A6

Track A, version 6. Builds on A5.

## What's in this folder

| File | Purpose |
|---|---|
| `index.html` | The whole site in one self-contained file (pages, styles, scripts, logos, images). |
| `assets/img/og-share.jpg` | Social share image (1200 x 600), referenced by the `og:image` tag. |
| `assets/img/speakers/` | Cropped speaker photos (also built into `index.html`; supplied for reuse). |
| `assets/img/client-logos/` | White, transparent client logos used in the homepage logo strip (also built into `index.html`). |
| `assets/logos/` | Event logos: trimmed white and black PNGs, plus the original uploads. The site uses the white version. |
| `docs/UAIFS_A6_content_template.xlsx` | Fresh content template exported from A6, for the next round of copy changes. |
| `.nojekyll` | Lets GitHub Pages serve the site as-is. |

## How to upload

Upload the **contents** of this folder to the web root, so `index.html` sits at the top level and `assets/` sits beside it. The social share image is referenced at `https://www.unlockingaiforsustainability.com/assets/img/og-share.jpg`; if the site lives on another domain, update the `og:image` line in `index.html`.

## Changes in A6

**Video removed** from the homepage.

**Figures updated:**
- Senior-level visitors to Eco-Business each year: 1.8M+ (Home, About, Partner with us).
- Annual pageviews: 17M+.
- Annual sessions: 2.9M+.

**Event details:** 20 November 2026, 9.00am to 2.00pm (GMT+8), at Shangri-La Orchard, Singapore.
- Updated on Home, Agenda, Register (including the venue FAQ) and Singapore 2026, and in the event data search engines read.
- Singapore 2026: format is now "Half-day, in person, with networking lunch"; audience "About 150 senior delegates" (per the programme). A fourth synopsis paragraph on Singapore's call at the UN for a global AI governance body has been added from the programme.

**Agenda rebuilt to the final programme:**

| Time | Session |
|---|---|
| 8.00am | Registration |
| 9.00am | Welcome remarks (Jessica Cheam) |
| 9.10am | Opening keynote address (Edward Vrkić) |
| 9.30am | Ministerial address or fireside chat: The next great divergence – or the next great convergence? |
| 10.15am | Opening plenary: The infrastructure paradox |
| 11.00am | Tea break |
| 11.15am | The next frontier – Future scenarios for AI and the world (Jayant Narayan) |
| 12.00pm | In conversation: Built to adapt – What it takes to prepare a nation for the AI economy |
| 12.30pm | The Oxford Debate: This House believes today's AI leaders can be trusted to govern AI responsibly (Yu Ping Chan) |
| 1.10pm | Closing remarks: The ASEAN advantage |
| 1.15pm | Networking lunch |

- Removed: the separate 9.20am Ministerial address (now combined with the fireside chat), the AI dividend plenary, the 2.00pm tech keynote, the 2.30pm supply chain plenary, the 4.00pm closing keynote and the 4.15pm drinks.
- The "day at a glance" bars (Agenda, Home, Singapore 2026), the homepage session cards and the Singapore 2026 session blocks all follow the new times.

**Speakers:** Edward Vrkić's full bio added. New speaker cards on Home, Speakers and Singapore 2026 for Elina Noor (Carnegie), Jayant Narayan (UNDP Global Centre) and Yu Ping Chan (UNDP-Singapore Global Center), with short bio, full bio and agenda links. Lawrence Wong's card stays hidden.

**Later A6 edits:**
- "Followed by networking" removed from all times (the agenda still ends with the 1.15pm networking lunch).
- Homepage numbers section: "Closing this gap is what the summit is for." removed; the "Read about the summit" button is centred.
- Speaker photos added for Jessica Cheam, Edward Vrkić, Elina Noor, Jayant Narayan and Yu Ping Chan, on speaker cards (Home, Speakers, Singapore 2026) and agenda/session avatars. Photos are built into the page once and reused, so they show in the preview too.
- About page expanded with content from the final programme: a fuller summit description (organisers, purpose, expansion from 2027); "Why now" (US$15T, US$1T for ASEAN, ~200-fold income gap, Singapore's UN call); the five themes with descriptions; "Who's in the room" (about 150 senior delegates and their profile); and "The day" (date, time, venue, format and session overview).

**Further A6 edits:**
- All "to be announced" speaker and moderator placeholders removed from the agenda and homepage session cards. Sessions without named speakers now show their description only, in a single column.
- Draft agenda notice removed from the Agenda page.
- "Audience figures are Eco-Business platform data from the UAIFS partnerships deck." removed from Partner with us.
- Partners: only the two confirmed partners are shown, UNDP (In partnership with) and Gurīn Energy (Thematic partner), on Partner with us and Singapore 2026. All sample partners and the "Available" tiles are removed; a line underneath links to the enquiry form.

**Official copy (latest A6 edit):** site copy aligned with the confirmed "About this Event" text.
- Home hero, Home "Why now", About (hero, summit, why now, themes intro, audience) and the Singapore 2026 synopsis now use the official wording: the defining-technology framing, the capital flows and labour-market points, UNDP's US$15 trillion / US$1 trillion estimate (linked to source), the nearly 200-fold income gap, Singapore's UN call and leadership, and the five-theme overview.
- Event name written as in the official copy, "Unlocking AI for sustainability" (and "Unlocking capital for sustainability"), across headings, body copy, page titles and search descriptions. The logo artwork is unchanged.
- Audience wording follows the programme: senior government officials, diplomatic representatives, business leaders and key decision-makers across financial institutions, corporate and technology firms, academia and civil society.
- Two typos in the supplied text were corrected when used: "renewableenergy model" (now "renewable energy, model") and "the decisions and governments make" (now "the decisions businesses and governments make").

**Client logo strip (homepage):** the scrolling names under "You're in good company" are now white logos, in the style of the EB Enterprise page.
- 20 logos: ABB, AWS, BDO, CDL, Danfoss, ENGIE Impact, Envision Digital, Fair Finance Asia, NUS, OCBC, Olam, Planet, Reuters, Siemens, Temasek, TOMRA, UNEP, Unilever, UOB, Wilmar. Backgrounds removed and logos upscaled from the supplied screenshots; ABB and Siemens use clean vector versions.
- Logos are sized to look balanced (stacked logos slightly taller, wide wordmarks slightly shorter), shown at 78% white and full white on hover; the strip pauses on hover.
- No logo file was available for RSPO, S&P Global, Schneider Electric, Sembcorp and Temasek Foundation; these stay as white text in the strip until logo files are supplied.

## Check before launch

1. **Debate motion:** the programme says today's AI leaders **can** be trusted; the speaker brief for Yu Ping Chan said **cannot**. The site uses "can" (programme). Confirm which is right.
2. **End time:** the programme says 9.00am to 3.00pm with networking lunch; the brief said 9.00am to 2.00pm, followed by networking. The site uses the brief.
3. **Elina Noor:** no session given, so her card says "session to be announced". Tell us which session she is in.
4. **"Speaking on" tags** for the new speakers were drafted from their bios; please check.
5. **Unconfirmed slots:** guest-of-honour or fireside speaker, the 12.00pm conversation speaker (IMDA CEO, not named until confirmed), further debaters and the closing remarks speaker. These sessions currently show no speakers; add them as they are confirmed.
7. **Client logos still needed:** RSPO, S&P Global, Schneider Electric, Sembcorp, Temasek Foundation (white or any colour, PNG or SVG). NUS and CDL were upscaled from small screenshots; higher-resolution files would sharpen them.
6. **Partner logos:** UNDP and Gurīn Energy are shown as names. Send logo files (SVG or transparent PNG) to show logos instead.
