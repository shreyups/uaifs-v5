# -*- coding: utf-8 -*-
"""Export site content as JSON seed files, one per CMS collection.
   python3 export_content.py <out_dir>"""
import json, os, sys
from content import *

out = sys.argv[1] if len(sys.argv) > 1 else "data"
os.makedirs(out, exist_ok=True)
def w(name, data):
    with open(os.path.join(out, name + ".json"), "w") as f: json.dump(data, f, indent=2, ensure_ascii=False)

w("editions", [{"slug": "singapore-2026", "name": "Singapore 2026", "market": "Singapore", "year": 2026, "status": "upcoming",
    "date": "2026-11-20", "start": "2026-11-20T09:00:00+08:00", "end": "2026-11-20T14:00:00+08:00", "venue": "TBC",
    "tagline": "Bridging technology and sustainable growth", "is_current": True, "registration_open": True}])

w("themes", [{"slug": t["slug"], "key": t["key"], "short_name": t["short"], "full_name": t["full"], "colour": t["c"], "icon": t["key"],
    "summary": t["one"], "intro": t["intro"], "questions": t["questions"], "who_follows": THEME_EXTRA[t["key"]]["who"],
    "hero_image": THEME_EXTRA[t["key"]]["img"] + ".jpg",
    "key_stats": [{"figure": a, "label": b, "source": c} for a, b, c in THEME_EXTRA[t["key"]]["stats"]],
    "edition_focus": {"singapore-2026": THEME_EXTRA[t["key"]]["sg"]},
    "featured_thought_leadership": t.get("featured"), "sort_order": i + 1} for i, t in enumerate(THEMES)])

res = []
for t in THEMES:
    for r in t["resources"]:
        res.append({"title": r["title"], "type": r["type"], "published": r["date"], "theme": t["slug"], "excerpt": r["ex"],
                    "url": r["url"], "source": "Unlocking Capital for Sustainability" if "unlockingcapital" in r["url"] else "Eco-Business",
                    "flags": [k for k in ("pending", "approx") if r.get(k)]})
w("resources", sorted(res, key=lambda r: r["published"], reverse=True))

w("speakers", [{"slug": k, "name": s["name"], "role": s["role"], "photo_url": s["photo"], "linkedin": s["li"], "bio_short": s["short"],
    "bio_long": s["long"], "speaking_topics": s["topics"], "themes": [THEME[x]["slug"] for x in s["themes"]],
    "editions": ["singapore-2026"], "featured": True} for k, s in SPEAKERS.items()])

sessions = []
for i, s in enumerate(SESSIONS):
    ex = SESSION_EXTRA.get(s["id"], {})
    sessions.append({"slug": s["id"], "edition": "singapore-2026", "start_time": s["time"], "duration": s.get("dur"), "sort_order": i + 1,
        "format": s["fmt"][1], "format_style": s["fmt"][0], "title": s["title"], "is_minor": bool(s.get("minor")),
        "summary": s.get("summary"), "body": s.get("body"), "why_it_matters": ex.get("why"), "best_for": ex.get("best"), "interaction": ex.get("mode"),
        "takeaways": s.get("takeaways", []), "themes": [THEME[k]["slug"] for k in s.get("themes", [])],
        "speakers": [{"speaker": p[0], "proposed": p[1]} if p[0] != "tba" else {"tba_label": p[1]} for p in s.get("people", [])],
        "moderator": {"speaker": s["mod"][0], "proposed": s["mod"][1]} if s.get("mod") else None,
        "focus_tables": [{"theme": THEME[k]["slug"], "title": n, "description": d} for k, n, d in s.get("focus", [])]})
w("sessions", sessions)
w("agenda_blocks", [{"edition": "singapore-2026", "label": a, "start_time": b, "description": c, "sessions": d, "minutes": e, "sort_order": i + 1} for i, (a, b, c, d, e) in enumerate(FLOW)])

tiers = [{"slug": "anchor", "name": "In partnership with", "label": "Anchor partner", "commercial": False, "sort_order": 0,
          "tagline": "Institutional anchor partner (UNDP)", "slots": "1"}]
for i, c in enumerate(TIER_CARDS):
    tiers.append({"slug": c["id"], "name": c["name"], "commercial": True, "sort_order": i + 1, "tagline": c["line"], "ideal_for": c["for"],
                  "headline_benefits": c["gets"], "slots": c["slots"], "accent_colour": c["c"]})
w("partner_tiers", tiers)

partners = []
for tier in TIERS:
    for p in tier["partners"]:
        partners.append({"name": p[0], "tier": tier["id"], "edition": "singapore-2026", "descriptor": p[1] or None,
                         "theme": next((t["slug"] for t in THEMES if len(p) > 3 and t["short"] == p[1]), None),
                         "logo": None, "is_sample": bool(p[2]), "url": None})
w("partners", partners)

cols = [c["id"] for c in TIER_CARDS]
rows, grp = [], None
for b in BENEFITS:
    if b[0] == "grp": grp = b[1]; continue
    rows.append({"group": grp, "benefit": b[0], "values": dict(zip(cols, b[1]))})
w("tier_benefits", {"legend": {"Y": "Included", "P": "Shared or on request", "N": "Not included", "other": "Count or text shown as-is"},
                    "indicative": True, "rows": rows})

w("stakeholder_groups", [{"name": n, "benefit": d, "sort_order": i + 1} for i, (n, d) in enumerate(STAKEHOLDERS)])
w("client_logos", [{"name": n, "logo": None, "sort_order": i + 1} for i, n in enumerate(CLIENT_LOGOS)])
w("faqs", [{"audience": "partners", "question": q, "answer": a} for q, a in PARTNER_FAQ] + [
    {"audience": "delegates", "question": "Is there a fee to attend?", "answer": "To be confirmed. Fee structure pending."},
    {"audience": "delegates", "question": "Can I attend virtually?", "answer": "No. The 2026 summit is in person only."},
    {"audience": "delegates", "question": "Can I register colleagues?", "answer": "To be confirmed. Group registration policy pending."},
    {"audience": "delegates", "question": "What is the cancellation policy?", "answer": "To be confirmed."},
    {"audience": "delegates", "question": "Where is the venue?", "answer": "In Singapore. The venue will be announced shortly and sent to all registered delegates."}])
w("site_settings", {"event": EVENT, "site_url": SITE_URL, "countdown_target": "2026-11-20T09:00:00+08:00",
    "key_numbers": NUMBERS, "why_attend": [{"title": a, "text": b} for a, b in WHY_ATTEND],
    "why_partner": [{"title": a, "text": b} for a, b in WHY_PARTNER_SHORT], "partner_reach": [{"figure": a, "label": b} for a, b in PARTNER_REACH],
    "partner_goal_finder": [{"goal": g, "tier": t} for g, t in FIT], "partner_journey": [{"stage": a, "items": b} for a, b in JOURNEY],
    "page_meta_descriptions": META, "event_video_src": None})
print("exported to", out)
