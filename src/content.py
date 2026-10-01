# -*- coding: utf-8 -*-
"""All UAIFS site content lives here, so copy edits never touch templates.
Sources: UAIFS partnerships deck (17 Sep 2026), working programme (internal),
UCFS speaker pages, Eco-Business articles (links verified Sep 2026)."""

EVENT = {
    "name": "Unlocking AI for Sustainability",
    "short": "UAIFS",
    "date": "20 November 2026",
    "time": "9.00am to 2.00pm (GMT+8)",
    "venue": "Singapore, venue to be confirmed",
    "edition": "Singapore 2026",
}

ICONS = {
    "infra": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="6" y="6" width="12" height="12" rx="2"/><rect x="9.5" y="9.5" width="5" height="5" rx="1"/><path d="M9 2v4M15 2v4M9 18v4M15 18v4M2 9h4M2 15h4M18 9h4M18 15h4"/></svg>',
    "climate": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M5 19c0-8 5-13 15-14-1 10-6 15-14 15"/><path d="M5 19l7-7"/><path d="M13 3l-2 4h3l-2 4"/></svg>',
    "supply": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="5" cy="6" r="2.2"/><circle cx="19" cy="6" r="2.2"/><circle cx="12" cy="18" r="2.2"/><path d="M7.2 6h9.6M6.2 8l4.6 8M17.8 8l-4.6 8"/></svg>',
    "finance": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 20h18"/><path d="M6 16v-4M11 16V8M16 16v-6"/><path d="M4 9l6-5 4 3 6-4"/></svg>',
    "gov": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l8 3v6c0 4.5-3.4 8-8 9-4.6-1-8-4.5-8-9V6z"/><path d="M8.5 12l2.5 2.5 4.5-5"/></svg>',
}

EB = "Eco-Business"

THEMES = [
    {
        "slug": "infrastructure", "key": "infra", "short": "AI Infrastructure",
        "full": "Sustainable AI infrastructure", "c": "#28A7E0",
        "one": "Cutting the energy, water and compute cost of AI, and what green-by-design data centres mean for net-zero targets.",
        "intro": [
            "Every AI model runs on physical infrastructure: data centres, chips, cooling, power and water. Across Asia Pacific that footprint is growing faster than grids and water systems were planned for, and regulators in Singapore, Malaysia and Thailand are now tying data centre growth to green performance.",
            "This theme follows how operators, hyperscalers, utilities and policymakers make the build-out sustainable, from efficient cooling and clean power sourcing to leaner model design that needs less compute in the first place.",
        ],
        "questions": [
            "How much grid and water capacity can AI infrastructure claim before it crowds out other decarbonisation?",
            "Which efficiency standards, disclosures and siting rules are becoming the regional baseline?",
            "Can smaller, task-specific models cut demand as much as greener hardware does?",
        ],
        "sessions": ["plenary", "roundtable"],
        "partner": "CapitaLand Investment",
        "resources": [
            {"type": "News", "date": "2026-07-07", "title": "Singapore moves to strengthen data centre sustainability and resilience under new Digital Infrastructure Bill",
             "ex": "With data centres projected to draw close to a fifth of Singapore's grid capacity this year, the new bill links further growth to green performance and resilience requirements.",
             "url": "https://www.eco-business.com/news/singapore-moves-to-strengthen-data-centre-sustainability-and-resilience-under-new-digital-infrastructure-bill/"},
            {"type": "News", "date": "2026-04-15", "title": "APAC data centre leaders launch sustainability framework amid energy, water concerns",
             "ex": "The Sustainable Digital Infrastructure Accord is the first region-wide, industry-led baseline for data centres, covering energy efficiency, clean energy, water use and circularity.",
             "url": "https://www.eco-business.com/news/apac-data-centre-leaders-launch-sustainability-framework-amid-energy-water-concerns/"},
            {"type": "Opinion", "date": "2025-09-10", "title": "Beyond green data centres: Leaner, smarter AI for Southeast Asia's sustainable digital future",
             "ex": "Greener hardware alone will not be enough. The piece argues for the software lever: smaller models, better training data and compression that reduce the compute a task needs.",
             "url": "https://www.eco-business.com/opinion/beyond-green-data-centres-leaner-smarter-ai-for-southeast-asias-sustainable-digital-future/"},
        ],
    },
    {
        "slug": "climate-energy", "key": "climate", "short": "Climate & Energy",
        "full": "AI for climate, energy and environment", "c": "#64B948",
        "one": "Smarter grids, biodiversity monitoring and disaster early warning: the AI use cases moving climate action from pilot to scale.",
        "intro": [
            "AI is already forecasting renewable output, balancing grids, monitoring forests and predicting floods. The open question is whether these climate applications can scale as fast as AI's own energy demand, which is currently growing faster.",
            "This theme tracks the applications that are working in Asia's energy systems and natural environment, what it takes to move them from pilot to deployment, and where the climate case for AI is still unproven.",
        ],
        "questions": [
            "Which AI climate applications have moved past the pilot stage in Asia, and what made them scale?",
            "Can data centres become flexible grid assets rather than a new source of fossil demand?",
            "What data, finance and policy do nature and resilience applications need to reach communities at risk?",
        ],
        "sessions": ["plenary", "roundtable"],
        "partner": "City Developments Limited",
        "resources": [
            {"type": "Research", "date": "2026-06-26", "title": "Nuclear energy fuels AI boom in Southeast Asia data centers",
             "ex": "Malaysia's data centre electricity demand could rise roughly eightfold between 2024 and 2030, to as much as 30 per cent of national supply, putting the region's power mix under pressure.",
             "url": "https://www.eco-business.com/research/nuclear-energy-fuels-ai-boom-in-southeast-asia-data-centers/"},
            {"type": "News", "date": "2026-05-22", "title": "How far can AI improve China's power grid?",
             "ex": "AI forecasting and virtual power plants show promise for integrating wind and solar, but experts warn that rigid grid operations may limit the efficiency gains.",
             "url": "https://www.eco-business.com/id/news/how-far-can-ai-improve-chinas-power-grid/"},
            {"type": "News", "date": "2026-05-13", "title": "AI's energy appetite is outpacing deployment of AI-based climate solutions: IEA",
             "ex": "The IEA flags grid and equipment bottlenecks from data centre growth, while noting that on-site battery storage could let data centres act as flexible grid assets.",
             "url": "https://www.eco-business.com/news/ais-energy-appetite-is-outpacing-deployment-of-ai-based-climate-solutions-iea/"},
        ],
    },
    {
        "slug": "supply-chains", "key": "supply", "short": "Supply Chains",
        "full": "Supply chain resilience and operations optimisation", "c": "#00BFAD",
        "one": "Practical playbooks for using AI to cut waste, sharpen procurement and de-risk logistics across emissions-heavy supply chains.",
        "intro": [
            "Most corporate emissions sit in the value chain, and most of the data needed to manage them is incomplete. AI is being used to fill the gaps: forecasting demand to cut waste, tracing materials, optimising logistics and running buildings and factories more efficiently.",
            "The same technology also depends on fragile supply chains of its own, from copper to nickel. This theme covers both sides: AI as an operations tool, and the resource chains that AI itself relies on.",
        ],
        "questions": [
            "Where is AI delivering measurable waste, cost and emissions cuts in Asian operations today?",
            "How good does supplier data need to be before AI-driven Scope 3 tools can be trusted?",
            "How do critical-mineral supply risks for AI hardware change sourcing and ESG due diligence?",
        ],
        "sessions": ["roundtable"],
        "partner": "Stockholm Environment Institute",
        "resources": [
            {"type": "Video", "date": "2026-08-25", "title": "Indonesia: Navigating AI, ESG risks as a global critical minerals player",
             "ex": "From Unlocking Capital for Sustainability Indonesia 2026: how the nickel and copper supply behind AI and climate tech can grow without compromising climate goals or community trust.",
             "url": "https://www.eco-business.com/videos/indonesia-navigating-ai-esg-risks-as-a-global-critical-minerals-player/"},
            {"type": "News", "date": "2025-12-15", "title": "Asia's AI real estate boom reaches Singapore, bringing efficiency and new risks",
             "ex": "AI now runs cooling, lifts and investment models in buildings. Experts warn that the technology's electricity demand could erode the efficiency gains it delivers.",
             "url": "https://www.eco-business.com/news/asias-ai-real-estate-boom-reaches-singapore-bringing-efficiency-and-new-risks/"},
            {"type": "Press release", "date": "2025-05-12", "title": "Copper supply crunch threatens energy and digital transitions",
             "ex": "UNCTAD warns that a copper shortfall could stall both clean energy and AI infrastructure, with around 80 new mines needed by 2030 to meet demand.",
             "url": "https://www.eco-business.com/ms/press-releases/copper-supply-crunch-threatens-energy-and-digital-transitions/"},
        ],
    },
    {
        "slug": "finance", "key": "finance", "short": "Finance & Investment",
        "full": "Finance and investments", "c": "#FFC300",
        "one": "What makes AI-for-sustainability bankable, and exactly what investors need to see before capital moves.",
        "intro": [
            "Capital is flowing into AI at record levels, but only a small share reaches climate and sustainability applications, and much of AI's environmental and social risk remains unpriced. For financiers, that uncertainty creates hesitation on both sides of the ledger.",
            "This theme looks at how investors, banks and funds assess AI-for-sustainability ventures, how they price AI's resource and governance risks in their portfolios, and which structures are getting early-stage solutions to scale.",
        ],
        "questions": [
            "What evidence do investors need before backing AI-enabled climate and sustainability ventures?",
            "How should lenders and asset owners price AI's energy, water and social risks?",
            "Which blended and catalytic structures are helping Asian start-ups cross from pilot to scale?",
        ],
        "sessions": ["fireside", "roundtable"],
        "partner": "UOB",
        "resources": [
            {"type": "Event", "date": "2026-09-10", "title": "Unlocking Capital for Sustainability Singapore 2026: Igniting capital, powering progress",
             "ex": "The sister summit's 2026 Singapore edition, where stronger governance frameworks for AI, climate tech and the digital economy were named as critical to scaling sustainable solutions.",
             "url": "https://www.unlockingcapitalforsustainability.com/singapore/2026"},
            {"type": "News", "date": "2026-06-05", "title": "Funding for climate tech startups in Southeast Asia rose year-on-year in 2025",
             "ex": "Climate tech start-ups in the region raised more in 2025 than the year before, though still well below the 2023 peak, with Singapore accounting for most funding since 2018.",
             "url": "https://www.eco-business.com/ms/news/funding-for-climate-tech-startups-in-southeast-asia-rose-year-on-year-in-2025/"},
            {"type": "News", "date": "2026-06-01", "title": "New US$100 million fund bets on Southeast Asia's climate startup boom",
             "ex": "A Singapore-based fund plans to build and scale 50 climate-focused start-ups across Southeast Asia and India, against a tough fundraising backdrop.",
             "url": "https://www.eco-business.com/ms/news/new-us100-million-fund-bets-on-southeast-asias-climate-startup-boom/", "approx": True},
        ],
    },
    {
        "slug": "responsible-ai", "key": "gov", "short": "Responsible AI",
        "full": "AI safety and governance, responsible AI", "c": "#F15B29",
        "one": "The accountability, safety and just-transition guardrails that turn responsible-AI principles into standards you can deploy.",
        "intro": [
            "Weak AI governance risks deepening digital divides, displacing jobs and embedding bias, and it leaves boards exposed to risks they cannot yet measure. Governance is also what gives regulators, developers and investors the long-term clarity they need to commit.",
            "This is the anchor theme of the summit. It covers data integrity, transparency, accountability and risk management alongside AI's environmental footprint, and asks how responsible deployment standards can work across Asia's different markets and regulatory regimes.",
        ],
        "questions": [
            "What does good AI governance look like at board level, and who owns it?",
            "How can responsible deployment standards align across Asian markets without stalling innovation?",
            "How do companies manage AI's workforce and inequality risks as part of a just transition?",
        ],
        "sessions": ["keynote", "fireside", "debate"],
        "partner": "OCBC",
        "featured": {"title": "Principles of good AI governance", "text": "A UAIFS thought-leadership paper with UNDP, setting out governance principles for deploying AI in line with sustainable development goals. Publication planned around the summit."},
        "resources": [
            {"type": "Press release", "date": "2026-09-11", "title": "UNDP and Eco-Business announce the Unlocking AI for Sustainability partnership",
             "ex": "Announced alongside UNDP's call for early action and regulatory alignment on Asia's energy and adaptation needs: a new partnership advancing AI governance and sustainable deployment.",
             "url": "https://www.eco-business.com/ms/press-releases/?page=1", "pending": True},
            {"type": "News", "date": "2026-06-24", "title": "AI's societal risks make governance a business-wide challenge in Singapore",
             "ex": "As adoption grows, companies face an AI trilemma of environmental footprint, workforce disruption and inequality, and governance can no longer sit with one team.",
             "url": "https://www.eco-business.com/news/ais-societal-risks-make-governance-a-business-wide-challenge-in-singapore/"},
            {"type": "Webinar", "date": "2026-06-03", "title": "AI and sustainability in Asia-Pacific: accelerator, risk multiplier, or both?",
             "ex": "A practitioner-led Eco-Business session on where AI is moving the needle on sustainable development, and where it is creating new fault lines.",
             "url": "https://events.eco-business.com/events/ai-and-sustainability-in-asia-pacific-accelerator-risk-multiplier-or-both"},
        ],
    },
]
THEME = {t["key"]: t for t in THEMES}

LI_SVG = '<svg viewBox="0 0 24 24"><path d="M20.5 2h-17A1.5 1.5 0 002 3.5v17A1.5 1.5 0 003.5 22h17a1.5 1.5 0 001.5-1.5v-17A1.5 1.5 0 0020.5 2zM8 19H5v-9h3zM6.5 8.3a1.7 1.7 0 110-3.5 1.7 1.7 0 010 3.5zM19 19h-3v-4.4c0-1 0-2.4-1.5-2.4S13 13.4 13 14.5V19h-3v-9h2.9v1.2h.1a3.2 3.2 0 012.9-1.6c3.1 0 3.7 2 3.7 4.7z"/></svg>'

SPEAKERS = {
    "jessica": {
        "name": "Jessica Cheam", "mono": "JC", "role": "Founder and CEO, Eco-Business",
        "photo": "https://cdn.prod.website-files.com/649e7c0ec962420345df0a3b/6a7bf2eb061521022ce4d22f_Jessica%20Cheam.png",
        "li": "https://www.linkedin.com/in/jessicacheam/",
        "short": "Jessica founded Eco-Business and has spent two decades at the intersection of media, sustainable development and ESG. She advises boards of governments and multinationals on ESG strategy and governance, with a particular interest in where sustainability meets technology.",
        "long": "She is an independent non-executive director of Wilmar International and ComfortDelGro, where she chairs the Board Sustainability Committee and sits on the Digitalisation Committee. A former political correspondent at The Straits Times, she manages The Liveability Challenge, is the author of Forging a Greener Tomorrow, holds INSEAD's Certificate in Corporate Governance, and regularly speaks at forums including the World Economic Forum's Annual Meeting in Davos.",
        "topics": ["AI governance and board oversight", "Sustainability and technology", "Just transition"],
        "themes": ["gov", "finance"],
        "sessions": ["welcome", "fireside"],
    },
    "meaghan": {
        "name": "Meaghan See", "mono": "MS", "role": "Chief Commercial Officer, Eco-Business",
        "photo": "https://cdn.prod.website-files.com/649e7c0ec962420345df0a3b/6a7bf27f57b7fe34b681003f_Meaghan%20See.png",
        "li": "https://www.linkedin.com/in/meaghan-see-aa5b7b18/",
        "short": "Meaghan leads partnerships, events and engagement at Eco-Business. A lawyer by training, she was previously APAC legal counsel at a London Stock Exchange-listed financial services institution, where she co-led the local ESG and women's network initiatives.",
        "long": "She holds a Bachelor of Laws from Singapore Management University and a Master of Laws from the University of California, Berkeley, specialising in environmental law and clean energy and technology, and has passed the bar in Singapore and California. At Unlocking Capital for Sustainability she has moderated sessions on climate tech, transition finance and ESG ratings.",
        "topics": ["Scaling climate tech", "Cross-sector partnerships", "ESG regulation"],
        "themes": ["supply", "finance"],
        "sessions": ["roundtable"],
    },
    "lawrence": {
        "name": "Lawrence Wong", "mono": "LW", "role": "Senior Advisor, Eco-Business",
        "photo": "https://cdn.prod.website-files.com/649e7c0ec962420345df0a3b/6a7da5600046e8df0a091f42_Lawrence%20Wong.png",
        "li": "https://www.linkedin.com/in/lawrencewongch/",
        "short": "Lawrence is an investor with 25 years of public and private sector experience across strategy, business building, economic policy and sustainability, at organisations including Temasek, ByteDance, Accenture, PwC and Singapore's Ministry of Trade and Industry.",
        "long": "Early in his career he founded a design start-up selling lifestyle products made from upcycled materials to Asia, Europe and the US. He works at the intersection of business, technology and sustainability to create triple-bottom-line impact, and moderated the nature-risk plenary at Unlocking Capital for Sustainability Singapore 2026.",
        "topics": ["Technology and sustainability in Southeast Asia", "Sustainable finance", "Building new ventures"],
        "themes": ["infra", "climate", "finance"],
        "sessions": ["plenary"],
    },
}

# Agenda — Singapore 2026 (working programme, internal notes excluded)
SESSIONS = [
    {"id": "registration", "time": "8.00am", "fmt": ("break", "Arrivals"), "title": "Registration and networking coffee", "minor": True},
    {"id": "welcome", "time": "9.00am", "dur": "10 min", "fmt": ("key", "Welcome"), "title": "Welcome remarks",
     "summary": "Eco-Business opens the inaugural summit: why AI and sustainability can no longer be planned on separate tracks, and what this room should leave having agreed.",
     "people": [("jessica", True)], "themes": ["gov"]},
    {"id": "keynote", "time": "9.10am", "dur": "15 min", "fmt": ("key", "Keynote"), "title": "Opening keynote by the guest-of-honour",
     "summary": "The policy signal for the morning. Our guest-of-honour sets out how government intends to govern AI-driven growth while keeping climate and development commitments on course.",
     "people": [("tba", "Guest-of-honour, to be announced")], "themes": ["gov"]},
    {"id": "fireside", "time": "9.25am", "dur": "30 min", "fmt": ("fire", "Fireside chat"), "title": "Governing growth in an age of technology and risk",
     "summary": "AI is projected to add US$15 trillion to global GDP by 2030, including US$1 trillion across ASEAN. The same growth brings power-hungry infrastructure, workforce disruption and algorithmic bias, and for financiers these unpriced risks are a reason to hesitate.",
     "body": "In this one-to-one conversation, a senior leader shares how they weigh AI's promise against its governance and stewardship risks: who should set the guardrails, how to keep the transition just for workers and communities, and what clarity regulators, developers and investors need to commit for the long term.",
     "takeaways": ["A leader's view of where AI governance should sit: government, boards or markets", "How just-transition thinking applies to AI-driven job change", "The signals investors need before AI and sustainability capital moves together"],
     "people": [("tba", "Guest-of-honour or senior leader, to be announced")], "mod": ("jessica", True), "themes": ["gov", "finance"]},
    {"id": "plenary", "time": "9.55am", "dur": "50 min", "fmt": ("plen", "Opening plenary"), "title": "AI: the missing piece to the energy transition?",
     "summary": "AI can optimise grids, forecast renewable output and cut energy waste across industry. It is also driving a surge in data centre demand that is outpacing clean power in parts of Southeast Asia.",
     "body": "This plenary brings together data centre operators, utilities, climate tech founders and policymakers to test the claim that AI will help rather than hinder the energy transition. Panellists examine energy and water efficiency in data centres, the resource risks of rapid build-out, and the climate tech applications that are ready to scale.",
     "takeaways": ["Where AI is already saving more energy than it uses, and where it is not", "The efficiency and siting standards shaping data centre growth in Asia", "Climate tech use cases ready for deployment, not just pilots"],
     "people": [("tba", "Speakers from operators, utilities and climate tech, to be announced")], "mod": ("lawrence", True), "themes": ["infra", "climate"]},
    {"id": "break", "time": "10.45am", "fmt": ("break", "Break"), "title": "Tea break and networking", "minor": True},
    {"id": "roundtable", "time": "11.00am", "dur": "75 min", "fmt": ("round", "Roundtable"), "title": "Bridging silos: AI adoption in the real economy",
     "summary": "An interactive, cross-sector deep dive. Delegates from different industries sit together to work through the concerns, challenges and pain points of integrating AI into operations, the emerging risks to sustainable adoption, and where collaboration can lower risk and raise returns.",
     "body": "Delegates join one of four facilitated tables and report back to the room. This is the session built for participation: bring your organisation's real questions.",
     "focus": [("supply", "Sustainable supply chains and operations", "How companies use AI to reduce waste, improve procurement and optimise logistics."),
               ("infra", "Sustainable AI infrastructure", "Data centre efficiency, compute optimisation, water and power demand, and responsible model design."),
               ("climate", "AI for nature and resilience", "Biodiversity monitoring, climate risk prediction, adaptation and disaster preparedness."),
               ("finance", "Investment and scaling", "What investors need to see to back climate and sustainability tech built on AI.")],
     "takeaways": ["Peer benchmarks on AI adoption from other sectors", "A shortlist of collaboration opportunities across your table", "Direct conversations with investors, operators and policymakers"],
     "people": [("tba", "Table hosts from partner organisations, to be announced")], "mod": ("meaghan", True), "themes": ["supply", "infra", "climate", "finance"]},
    {"id": "debate", "time": "12.15pm", "dur": "45 min", "fmt": ("debate", "Plenary debate"), "title": "Plenary debate or partner-led special presentation",
     "summary": "The closing plenary puts one of the hardest trade-offs in AI and sustainability to a vote. Two teams argue a motion, the audience votes before and after, and the swing decides the winner.",
     "body": "The motion and format will be announced closer to the summit. If this slot is taken up as a partner-led presentation, it will focus on a deployable AI-for-sustainability solution.",
     "takeaways": ["The strongest case on each side of a live policy question", "A real-time read of where the room stands"],
     "people": [("tba", "Debaters to be announced")], "themes": ["gov", "infra"]},
    {"id": "close", "time": "1.00pm", "fmt": ("break", "Networking"), "title": "Closing remarks and networking lunch", "minor": True},
]
SESSION = {s["id"]: s for s in SESSIONS}

STAKEHOLDERS = [
    ("Big Tech and cloud providers", "Showcase AI-for-sustainability solutions, strengthen enterprise relationships, and lead the responsible AI conversation."),
    ("Corporates using AI in operations", "Demonstrate innovation leadership and connect with solutions that improve efficiency and lower emissions."),
    ("Start-ups in climate, energy and sustainability", "Gain visibility and credibility, and network with potential investors and customers."),
    ("Government and public-sector agencies", "Shape policy, identify deployable solutions, and support digital and sustainable development goals."),
    ("Investors, funds and family offices", "Access curated deal flow, network with founders, and understand emerging market opportunities."),
]

# Partner tiers — sample partners drawn from UCFS for layout only
TIERS = [
    {"id": "anchor", "name": "In partnership with", "desc": "Anchor partner", "kind": "anchor",
     "partners": [("UNDP", "United Nations Development Programme", False)]},
    {"id": "founding", "name": "Founding partner", "desc": "Backs the platform from its inaugural edition", "partners": [("Temasek Foundation", "", True)]},
    {"id": "thematic", "name": "Thematic partners", "desc": "One per theme; co-owns the theme's sessions and resource hub", "kind": "theme",
     "partners": [(t["partner"], t["short"], True, t["c"]) for t in THEMES]},
    {"id": "innovation", "name": "Innovation partner", "desc": "Curates the start-up and solutions showcase", "partners": [("The Liveability Challenge", "", True)]},
    {"id": "networking", "name": "Networking partners", "desc": "Host the networking breaks and lunch", "partners": [("Singapore Sustainable Finance Association", "", True), ("EU-ASEAN Business Council", "", True), ("International Capital Market Association", "", True)]},
    {"id": "venue", "name": "Venue partner", "desc": "", "partners": [("AT ONE Impact Week", "", True)]},
    {"id": "media", "name": "Media partner", "desc": "", "partners": []},
    {"id": "outreach", "name": "Outreach partners", "desc": "Extend the invitation to their networks", "partners": [("Centre for Sustainable Finance Innovation", "", True), ("CDP", "", True)]},
]

# Benefits by tier: Y = included, P = partial/shared, N = not included, or a string
TIER_COLS = [("Founding", "1 slot"), ("Thematic", "5 slots, 1 per theme"), ("Innovation", "1 slot"), ("Networking", "3 slots"), ("Venue", "1 slot"), ("Media", "1 slot"), ("Outreach", "Open")]
BENEFITS = [
    ("grp", "Thought leadership and speaking"),
    ("Keynote or fireside chat speaking slot", ["Y", "N", "N", "N", "N", "N", "N"]),
    ("Panellist in a plenary on your theme", ["Y", "Y", "P", "N", "N", "N", "N"]),
    ("Host a roundtable table", ["Y", "Y", "Y", "P", "N", "N", "N"]),
    ("Co-develop a session format with Eco-Business", ["Y", "Y", "P", "N", "N", "N", "N"]),
    ("grp", "Content and resource hub"),
    ("Branded theme resource hub page (evergreen)", ["All themes", "Own theme", "N", "N", "N", "N", "N"]),
    ("Co-authored report or white paper", ["Y", "P", "N", "N", "N", "N", "N"]),
    ("Sponsored article on Eco-Business", ["2", "1", "1", "N", "N", "N", "N"]),
    ("Feature in the post-event insights report", ["Y", "Y", "Y", "P", "P", "P", "N"]),
    ("grp", "Visibility"),
    ("Logo on website, event collateral and stage", ["Y", "Y", "Y", "Y", "Y", "Y", "Y"]),
    ("Branding on networking areas", ["Y", "N", "N", "Y", "Y", "N", "N"]),
    ("Eco-Business newsletter and social promotion", ["Y", "Y", "Y", "P", "P", "Y", "P"]),
    ("Solution demo or showcase space", ["Y", "P", "Y", "N", "N", "N", "N"]),
    ("grp", "Access"),
    ("Complimentary delegate passes", ["10", "6", "4", "3", "4", "2", "2"]),
    ("Invitations to closed-door roundtables", ["Y", "Y", "P", "N", "N", "N", "N"]),
    ("Aggregate delegate insights after the event", ["Y", "Y", "Y", "P", "N", "N", "N"]),
]

NUMBERS = [
    {"pre": "US$", "to": 15, "suf": "T", "dec": 0, "l": "AI's projected addition to global GDP by 2030", "s": "Including US$1 trillion across ASEAN"},
    {"pre": "", "to": 1.6, "suf": "M+", "dec": 1, "l": "Senior-level visitors to Eco-Business each year", "s": "68% senior management and above"},
    {"pre": "", "to": 115000, "suf": "+", "dec": 0, "l": "Decision-maker contacts across Asia Pacific and beyond", "s": "Eco-Business marketing network"},
    {"pre": "", "to": 17, "suf": "", "dec": 0, "l": "Years as the region's trusted sustainability platform", "s": "UCFS hosted in six Asian markets since 2018"},
]

# Organisations that work with Eco-Business (EB Enterprise page): homepage logo strip
CLIENT_LOGOS = ["ABB", "AWS", "BDO", "CDL", "Danfoss", "ENGIE Impact", "Envision Digital", "Fair Finance Asia",
    "NUS", "OCBC", "Olam", "Planet", "Reuters", "RSPO", "S&P Global", "Schneider Electric", "Sembcorp",
    "Siemens", "Temasek Foundation", "Temasek", "TOMRA", "UNEP", "Unilever", "UOB", "Wilmar"]

# =====================================================================
# v4.1 additions: richer theme, session, partner and SEO content
# =====================================================================

# Canonical domain for SEO tags. TO CONFIRM: final domain for the site.
SITE_URL = "https://www.unlockingaiforsustainability.com/"

THEME_EXTRA = {
    "infra": {
        "img": "theme-infrastructure",
        "stats": [("~1/5", "of Singapore's grid capacity could be drawn by data centres this year", "Eco-Business, Jul 2026"),
                  ("1st", "region-wide, industry-led sustainability baseline for APAC data centres, launched in 2026", "Eco-Business, Apr 2026")],
        "who": "Data centre operators, hyperscalers and cloud providers, utilities, real estate owners and regulators.",
        "sg": "Singapore is tying new data centre capacity to green performance. In Singapore, delegates will examine what that means for operators across the region: efficiency and water standards, clean power sourcing, and whether leaner AI models can reduce demand at source.",
    },
    "climate": {
        "img": "theme-climate-energy",
        "stats": [("8x", "projected rise in Malaysia's data centre electricity demand between 2024 and 2030", "Eco-Business Research, Jun 2026"),
                  ("Up to 30%", "of Malaysia's national power supply could go to data centres by 2030", "Eco-Business Research, Jun 2026")],
        "who": "Energy companies, grid operators, climate tech founders, conservation groups and resilience planners.",
        "sg": "The opening plenary asks whether AI will speed up or slow down the energy transition. The roundtable's nature and resilience table then looks at the applications ready to scale, from renewable forecasting to flood and biodiversity monitoring.",
    },
    "supply": {
        "img": "theme-supply-chains",
        "stats": [("~80", "new copper mines needed by 2030 to meet demand from clean energy and digital infrastructure", "UNCTAD via Eco-Business, May 2025"),
                  ("+40%", "expected growth in copper demand by 2040", "UNCTAD via Eco-Business, May 2025")],
        "who": "Chief operating, procurement and sustainability officers, logistics firms, manufacturers and commodity producers.",
        "sg": "At the roundtable, delegates compare where AI is already cutting waste, cost and emissions in operations and procurement, and how critical-mineral risks behind AI hardware are changing sourcing and due diligence.",
    },
    "finance": {
        "img": "theme-finance",
        "stats": [("US$15T", "AI's projected addition to global GDP by 2030, including US$1 trillion across ASEAN", "UAIFS partnerships deck"),
                  ("US$166M", "raised by Southeast Asian climate tech start-ups in 2025, still far below the 2023 peak", "Eco-Business, Jun 2026")],
        "who": "Banks, asset owners and managers, venture and impact investors, family offices and founders raising capital.",
        "sg": "The fireside chat explores the clarity investors need before AI and sustainability capital move together. The roundtable's investment table sets out, in practical terms, what makes an AI-enabled climate venture bankable.",
    },
    "gov": {
        "img": "theme-responsible-ai",
        "stats": [("3", "risks in the AI trilemma companies now face: environmental footprint, workforce disruption and inequality", "Eco-Business, Jun 2026"),
                  ("US$1T", "of AI-driven GDP at stake in ASEAN, making governance a growth question, not only a compliance one", "UAIFS partnerships deck")],
        "who": "Boards and general counsel, chief technology and risk officers, policymakers, regulators and civil society.",
        "sg": "The anchor theme runs through the morning: the guest-of-honour keynote sets the policy signal, the fireside chat asks who should set AI's guardrails, and the closing debate puts a live governance trade-off to a vote.",
    },
}

SESSION_EXTRA = {
    "welcome": {"best": "Everyone", "mode": "Listen"},
    "keynote": {"best": "Policy, government and corporate leaders", "mode": "Listen"},
    "fireside": {"best": "Boards, investors and policymakers", "mode": "Listen, then audience Q&A",
                 "why": "Most AI governance debates stay abstract. This conversation is about the decisions a senior leader actually faces."},
    "plenary": {"best": "Energy, infrastructure, real estate and climate tech", "mode": "Panel with audience Q&A",
                "why": "Data centre growth is now a grid and water planning issue across Southeast Asia. This is where operators, utilities and innovators meet on it."},
    "roundtable": {"best": "Practitioners from every sector", "mode": "Hands-on, facilitated tables",
                   "why": "The most valuable 75 minutes for delegates who want peer benchmarks and new collaborators rather than more presentations."},
    "debate": {"best": "Everyone; bring your view", "mode": "Live vote before and after",
               "why": "A format that forces clear positions and shows where the room really stands."},
}

# How the morning flows (edition page + agenda timeline)
FLOW = [
    ("Set the context", "9.00am", "Welcome, keynote and fireside chat", ["welcome", "keynote", "fireside"], 55),
    ("Test the big question", "9.55am", "Opening plenary on AI and the energy transition", ["plenary"], 50),
    ("Break", "10.45am", "Tea and networking", ["break"], 15),
    ("Work the problem", "11.00am", "Cross-sector roundtable, four focus tables", ["roundtable"], 75),
    ("Take a position", "12.15pm", "Plenary debate or partner-led presentation", ["debate"], 45),
    ("Connect", "1.00pm", "Closing remarks and networking lunch", ["close"], 60),
]

WHY_ATTEND = [
    ("Leave with practical answers", "Real deployments and clear next steps from people doing the work, not generic AI talk."),
    ("Meet the people who decide", "A curated, senior room of tech providers, investors, regulators and sustainability leads."),
    ("Shape the rules, not just follow them", "Contribute to the governance conversation UNDP and Eco-Business will carry forward."),
]
WHY_PARTNER_SHORT = [
    ("Own the conversation", "Lead a theme year-round, not just on the day, through its evergreen knowledge hub."),
    ("Reach senior decision-makers", "1.6 million senior-level visitors a year and 115,000+ contacts across Eco-Business channels."),
    ("Co-create, don't just sponsor", "Formats developed with you around your objectives, backed by 17 years of convening."),
]

PARTNER_REACH = [
    ("1.6M+", "senior-level visitors to Eco-Business a year"),
    ("68%", "of the audience is senior management and above"),
    ("115,000+", "decision-maker contacts in the marketing network"),
    ("6", "Asian markets where Eco-Business has run UCFS since 2018"),
]

# Commercial tiers as cards. Indicative; rate card TBC.
TIER_CARDS = [
    {"id": "founding", "name": "Founding partner", "slots": "1 available", "line": "Shape the platform from its first edition",
     "for": "Organisations that want to be the defining voice on AI and sustainability in Asia Pacific.",
     "gets": ["Keynote or fireside chat speaking slot", "Recognition across all five theme hubs, all year", "Co-authored flagship report with Eco-Business", "10 delegate passes and first right of renewal"],
     "c": "#FFC300"},
    {"id": "thematic", "name": "Thematic partner", "slots": "5 available, one per theme", "line": "Own a theme, on stage and all year",
     "for": "Companies with deep expertise in infrastructure, climate and energy, supply chains, finance or responsible AI.",
     "gets": ["Plenary seat and a roundtable table on your theme", "Branded theme knowledge hub, live between editions", "Sponsored article on Eco-Business", "6 delegate passes"],
     "c": "#00BFAD"},
    {"id": "innovation", "name": "Innovation partner", "slots": "1 available", "line": "Put working solutions in front of buyers and investors",
     "for": "Technology providers, accelerators and venture builders with deployable AI-for-sustainability solutions.",
     "gets": ["Curate the solutions showcase or demo corner", "Introductions to corporate buyers and investors", "Feature in the post-event insights report", "4 delegate passes"],
     "c": "#64B948"},
    {"id": "networking", "name": "Networking partner", "slots": "3 available", "line": "Host the conversations that happen off stage",
     "for": "Brands that want visibility with every delegate in a relaxed, relationship-building setting.",
     "gets": ["Branding on the tea break or networking lunch", "Logo on website, collateral and stage", "Newsletter and social mentions", "3 delegate passes"],
     "c": "#28A7E0"},
    {"id": "venue", "name": "Venue partner", "slots": "1 available", "line": "Bring the summit to your space",
     "for": "Venues, campuses and property owners with a sustainability story to tell.",
     "gets": ["Summit hosted at your venue, credited throughout", "Branding across networking areas", "Venue feature in pre-event communications", "4 delegate passes"],
     "c": "#9ad885"},
    {"id": "media", "name": "Media partner", "slots": "1 available", "line": "Extend the summit's reach",
     "for": "Publications and platforms serving technology, business or sustainability audiences.",
     "gets": ["Content exchange with Eco-Business", "Logo on website and collateral", "Press access on the day", "2 delegate passes"],
     "c": "#8fd5f6"},
    {"id": "outreach", "name": "Outreach partner", "slots": "Open", "line": "Bring your members into the room",
     "for": "Industry associations, chambers, networks and universities.",
     "gets": ["Priority registration for your members", "Logo on website and partner listings", "Newsletter mention", "2 delegate passes"],
     "c": "#A7B7C9"},
]

FIT = [
    ("Lead the AI and sustainability agenda", "founding"),
    ("Be the go-to expert on one theme", "thematic"),
    ("Showcase a solution to buyers and investors", "innovation"),
    ("Build relationships with every delegate", "networking"),
    ("Host the summit at our venue", "venue"),
    ("Extend reach to our audience or members", "outreach"),
]

JOURNEY = [
    ("Before the summit", ["Co-design session with the Eco-Business programme team", "Pre-event content in your theme's knowledge hub", "Promotion across Eco-Business newsletters, social and events channels"]),
    ("On the day", ["Stage time, roundtable hosting or showcase space, by tier", "Branding across stage, screens and networking areas", "Curated introductions to senior delegates"]),
    ("After the summit", ["Feature in the post-event insights report", "Evergreen content in the theme hub, all year", "Aggregate delegate insights and first right to the next edition"]),
]

PARTNER_FAQ = [
    ("How are packages priced?", "Every package is tailored to your objectives. Tell us your goals using the enquiry form and our partnerships team will send the prospectus and rate card."),
    ("Can we customise a package?", "Yes. Most partners combine elements across tiers, and Eco-Business co-develops session formats with you around your theme."),
    ("Can we partner across several editions or markets?", "Yes. UAIFS is designed to run across markets and years, like Unlocking Capital for Sustainability. Multi-edition packages are available."),
    ("How does the programme stay credible?", "Eco-Business curates the programme with UNDP as anchor partner, so sessions stay practical and non-promotional. That is what keeps senior delegates in the room, and what makes partner visibility valuable."),
    ("What is the deadline to be included?", "To be confirmed. Earlier confirmation secures more speaking and branding opportunities, including printed collateral."),
]

META = {
    "index": "The inaugural Unlocking AI for Sustainability Summit, 20 November 2026 in Singapore. Organised by Eco-Business in partnership with UNDP. Register or become a partner.",
    "about": "Why Unlocking AI for Sustainability exists, who it is for, and what each stakeholder group gains. A business and policy platform on AI, sustainability and governance in Asia Pacific.",
    "themes": "Five evergreen themes and knowledge hubs: AI infrastructure, climate and energy, supply chains, finance and investment, and responsible AI. News, research and analysis from Eco-Business.",
    "agenda": "Agenda for Unlocking AI for Sustainability, Singapore 2026: keynote, fireside chat, energy transition plenary, cross-sector roundtable and closing debate.",
    "speakers": "Speakers at Unlocking AI for Sustainability 2026, including Eco-Business's Jessica Cheam, Meaghan See and Lawrence Wong. Nominate a speaker.",
    "partners": "Partner with Unlocking AI for Sustainability. Compare founding, thematic, innovation, networking, venue, media and outreach tiers, and enquire about packages.",
    "register": "Register for Unlocking AI for Sustainability, 20 November 2026, Singapore. In person, curated for senior decision-makers.",
    "edition-2026": "Unlocking AI for Sustainability Singapore 2026, the inaugural edition on 20 November. Themes, agenda, speakers and partners.",
}
