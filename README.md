# Unlocking AI for Sustainability (UAIFS) — Website v5 draft

Static site for the Unlocking AI for Sustainability Summit (20 November 2026, Singapore), organised by Eco-Business in partnership with UNDP. Dark theme per stakeholder direction; colours from the Eco-Business Corporate Identity Guidelines (2014); structure mirrors unlockingcapitalforsustainability.com.

See **SITEMAP-and-CHANGELOG-v5.md** for the sitemap, what changed from v2, and open items.

## Folders
- `site/` — the publishable website (13 pages). Upload the contents to GitHub Pages.
- `src/` — generator. `content.py` holds all copy and data; `build.py` holds templates.
- `uaifs-walkthrough.html` — single-file version of the whole site for approvers (open in any browser).

## Editing
1. Change copy in `src/content.py` (speakers, sessions, themes, resources, tiers, benefits).
2. Run `python3 src/build.py` (Python 3.12+, no packages needed).
3. `site/` and `uaifs-walkthrough.html` (in `dist/`) are regenerated.
CSS and JS live in `site/assets/` and are edited directly.

## SEO and analytics
- Set `SITE_URL` in `src/content.py` to the final domain, then rebuild. This updates canonical URLs, social cards, structured data and `sitemap.xml`.
- Paste the Google Tag Manager snippet where marked in `<head>` (edit `GTM` in `src/build.py`). Events are listed in the change log's analytics plan.
- Submit `sitemap.xml` in Google Search Console after launch.

## Deploy to GitHub Pages
Copy the contents of `site/` to the repo root, commit and push. Settings → Pages → Deploy from branch → main / (root).

## Before launch
- Remove the review-notes button and notes (see changelog).
- Replace `assets/img/kv-draft.jpg` with the final KV.
- Wire forms (registration, newsletter, speaker nomination, partner enquiry) to CRM / email platform.
- Speaker photos are hot-linked from the UCFS image library; copy them into `assets/img/` for production.
