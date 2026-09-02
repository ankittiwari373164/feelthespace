# -*- coding: utf-8 -*-
"""Feel The Space — Interior Design Studio.
Single source of truth. Figures below come from the studio's 2026 client
proposal; change them here and they update across every page."""

BRAND = {
    "name": "Feel The Space",
    "sub": "Interior Design Studio",
    "tagline": "Let's create your dream space",
    "phone": "+91 74289 68717",
    "email": "contact@feelthespace.in",
    "site": "www.feelthespace.in",
    "address_l1": "10128, Gaur City Mall, Greater Noida West",
    "address_l2": "Gautam Buddha Nagar, Uttar Pradesh – 201306",
    "instagram": "https://www.instagram.com/feelthespace2023/",
    "facebook": "https://www.facebook.com/feelthespacenoida2023",
    "youtube": "https://www.youtube.com/@feelthespace2023",
    "maps": "https://maps.app.goo.gl/NhqQYVEnPzNqLJYy6",
    "review": "https://maps.app.goo.gl/NhqQYVEnPzNqLJYy6",
}

WHATSAPP_TEXT = "Hi Feel The Space, I'd like to discuss an interior project."

# Societies and properties actually delivered in
SOCIETIES = [
    ("Greater Noida West", ["Gaur Saundaryam", "NX One", "Saya Zion",
                            "Amrapali Golf Homes", "5th Avenue, Gaur City", "Gaur City Center"]),
    ("Noida", ["Ajnara Ambrosia", "Sector 118"]),
    ("Ghaziabad", ["Unninav Utopia", "Raj Nagar Extension"]),
    ("New Delhi", ["Golf View Apartments, Saket"]),
    ("Vrindavan", ["Krishyen Dham Hotel"]),
]

# 3-step cost calculator
CALC_TYPES = [("2 BHK", 950), ("3 BHK", 1275), ("4 BHK", 1650), ("Villa", 2400), ("Office", 1800)]
CALC_STYLES = ["Modern Minimalist", "Classic Luxury", "Traditional"]
CALC_SCOPES = [("Full 3D design with execution", 1.0), ("Complete turnkey", 1.0)]

SERVICE_AREAS = [
    ("greater-noida-west", "Greater Noida West", "Gaur City, Ek Murti, Sector 1–4 and the surrounding societies — our home ground, minutes from the studio."),
    ("noida", "Noida", "Sectors 62, 74–79, 100–150 and the Expressway corridor, covering builder flats and independent floors."),
    ("greater-noida", "Greater Noida", "Pari Chowk, Alpha, Omega, Knowledge Park and the Yamuna Expressway belt."),
    ("ghaziabad", "Ghaziabad", "Indirapuram, Vaishali, Vasundhara, Raj Nagar Extension and Crossings Republik."),
    ("delhi", "Delhi NCR", "East and South Delhi residences, plus commercial fit-outs across the capital."),
    ("gurugram", "Gurugram", "Sohna Road, Golf Course Extension and New Gurugram, for homes and offices."),
]

PHASES = [
    ("01", "Design & Consultation",
     "Plan, visualise and technically detail your space before a rupee is spent on execution."),
    ("02", "Core Base Scope",
     "The essential setup — carpentry, kitchen, ceiling and lighting — included across every project."),
    ("03", "Turnkey Execution",
     "Choose Silver, Gold or Platinum, and we deliver the whole build under one contract."),
]

DELIVERABLES = [
    ("01", "2D Space Planning", "Furniture layout and circulation, drawn to your carpet area."),
    ("02", "3D Visualisation", "Bedrooms, living-dining, kitchen and foyer, rendered before approval."),
    ("03", "Execution Drawings", "Detailed carpentry and furniture drawings for the site team."),
    ("04", "RCP + Electrical", "Ceiling, lighting and electrical layouts, coordinated with the design."),
    ("05", "Material + BOQ", "Specification chart and detailed quantities, itemised line by line."),
]

DESIGN_FEE = {
    "rate": "₹150",
    "note": "Design and consultation are priced transparently and kept separate from execution, without GST.",
    "example_area": "1,275 sq. ft.",
    "example_base": "₹1,91,250",
    "example_gst": "₹34,425",
    "example_total": "₹1,91,250",
}

CORE_SCOPE = [
    ("All Bedrooms",
     "Designer bed with headboard, bedside tables, full-height wardrobes, TV/media console, "
     "accent wall, study desk and chair, dressing unit, false ceiling and lighting."),
    ("Modular Kitchen",
     "Sainik 710 BWP base cabinets, Century MR overheads, five InnoTech Hettich drawers, "
     "appliance garage, rolling shutter and soft-close hardware throughout."),
    ("Living, Dining & Foyer",
     "Six-seater sofa with centre table, six-seater dining, room divider, entrance accent "
     "panelling and layered false ceiling."),
]

PACKAGES = [
    {
        "slug": "silver",
        "name": "Silver",
        "kicker": "Essential turnkey setup",
        "rate": "₹2,000",
        "headline": "Complete fixed furniture, built exactly as per your approved 3D design.",
        "signature": "Complete Fixed Furniture",
        "image": "silver-living-panelled",
        "images": ["silver-living-minimal", "silver-living-panelled", "silver-living-chandelier"],
        "scope": [
            "Complete fixed furniture, exactly as per the approved 3D design",
            "Wardrobes, beds, media consoles, study and dressing units",
            "Modular kitchen on Sainik 710 BWP with Century MR overheads",
            "Hettich soft-close hardware and five InnoTech drawers",
            "Complete wiring, LED spotlights and cove lighting",
            "Gypsum false ceiling and Asian Paints emulsion",
        ],
    },
    {
        "slug": "gold",
        "name": "Gold",
        "kicker": "Premium living & soft décor",
        "rate": "₹2,600 – ₹2,800",
        "headline": "Complete fixed furniture plus full decorative and door treatments, exactly as per your approved 3D design.",
        "signature": "Fixed Furniture + Decorative & Door Treatments",
        "image": "gold-bedroom-rosegold",
        "images": ["gold-bedroom-rosegold", "gold-bedroom-blue", "gold-bedroom-tufted"],
        "scope": [
            "Everything in Silver, plus full decorative treatment",
            "Complete door treatments — cladding, moulding and architraves",
            "Premium satin / PU-enamel painted doors",
            "Architectural wall panelling and feature treatments",
            "High-gloss acrylic kitchen shutter option",
            "Natural wood veneer on accent units",
            "POP fall ceiling with layered profile lighting",
            "Sheer and blackout curtains with premium upholstery",
        ],
    },
    {
        "slug": "platinum",
        "name": "Platinum",
        "kicker": "Ultra-luxury & architectural overhaul",
        "rate": "₹4,000",
        "headline": "Everything shown in your luxury 3D design — fixed furniture, grand feature walls and premium lounge furniture.",
        "signature": "The Full Luxury 3D, Delivered",
        "image": "plat-living-classical",
        "images": ["plat-living-classical", "plat-bedroom-gold", "plat-corridor-marble"],
        "scope": [
            "Every single element shown in your luxury 3D design",
            "All fixed furniture, fully detailed",
            "Grand feature walls — CNC routed, fluted and panelled",
            "Premium loose and lounge furniture included",
            "Full-height door cladding with Italian PU finish",
            "Full PU finish on selected furniture",
            "Complete transformation of bathrooms",
            "Smart switches, mood lighting and bespoke accents",
        ],
        "highlights": [
            ("Complete Bathrooms",
             "Full dismantling, designer vitrified wall and floor tiles to an agreed allowance, "
             "Jaquar / Kohler fixtures, custom vanities and toughened glass shower partitions."),
            ("Smart Home",
             "Wi-Fi touch switch plates and app-controlled mood lighting throughout."),
            ("Bespoke Accents",
             "Handcrafted metal and wooden art pieces with premium architectural detailing."),
        ],
    },
]

PROMISE = {
    "title": "What you see in the 3D is exactly what you get",
    "body": "Across all three packages we never compromise on the core strength of your home. "
            "Every project is delivered with 100% A-grade material, best-in-class quality and skilled labour work.",
    "quote": "No matter which package fits your budget, the quality stays non-negotiable. You always get the "
             "best materials and the best labour work from Feel The Space. The price changes only with how much "
             "work and how many design elements you choose from your 3D view.",
    "attrib": "Designer's note",
}

TRUST_BADGES = [
    ("10-Year", "Material warranty"),
    ("45–60 Days", "On-time delivery guarantee"),
    ("Zero", "Hidden costs"),
    ("100%", "In-house carpentry & execution"),
]

MATERIALS = [
    ("Kitchen Base", "Sainik 710 • BWP Marine Plywood"),
    ("Overhead Cabinets", "Century MR Grade Plywood"),
    ("Hardware", "Hettich soft-close hinges & channels"),
    ("Drawers", "5 InnoTech soft-close drawers"),
    ("Shutters", "Laminate → Acrylic/Veneer → Italian PU"),
    ("Doors", "Laminate → Moulding/Paint → CNC/PU"),
]

BOQ_STEPS = [
    ("01", "Final 3D Approval"),
    ("02", "Signed BOQ"),
    ("03", "Material & Brand Selection"),
    ("04", "Execution Schedule"),
    ("05", "Payment Milestones"),
]

NEXT_STEPS = [
    ("01", "Confirm Design Engagement"),
    ("02", "Begin Space Planning"),
    ("03", "Review & Approve 3D"),
    ("04", "Lock BOQ & Package"),
    ("05", "Start Turnkey Execution"),
]

TERMS = [
    ("Carpet Area", "All package rates are calculated on the measured carpet area of your property."),
    ("BOQ Locking", "Final payment milestones and the execution schedule are locked after 3D approval, through the signed BOQ."),
    ("Allowances", "Gold and Platinum soft furnishings and bathroom fittings follow agreed brand and rate allowances."),
    ("GST", "18% GST is charged extra on both the design fee and turnkey execution billing. All quoted rates are shown without GST."),
]

VERTICALS = [
    {
        "slug": "residential",
        "name": "Residential",
        "title": "Homes",
        "lede": "Apartments, builder floors and independent houses across Noida and Greater Noida West.",
        "body": [
            "Most of our work is residential, and most of it sits within a few kilometres of the studio — Gaur City, Ek Murti, the Noida Extension societies and the sectors along the Expressway. We know these layouts: where the beam runs in a Gaur City 3BHK, and how much wardrobe depth is left once the duct is accounted for.",
            "Every home starts with measured drawings and a 3D you sign off before anything is cut. Kitchens go in on Sainik 710 BWP with Hettich hardware, ceilings are layered rather than flat, and the lighting is planned at the drawing stage instead of being drilled in at the end.",
        ],
        "hero": "res-living-dining-wide",
        "gallery": ["res-kitchen-island", "res-living-panelled", "res-foyer-marble",
                    "res-wardrobe-dresser", "res-crockery-niche", "res-kitchen-white",
                    "res-entrance-ceiling", "res-corridor-mirror", "res-kitchen-lshape",
                    "res-bedroom-cove", "res-shoe-console", "res-kitchen-utility"],
        "video": "res-walkthrough",
    },
    {
        "slug": "office",
        "name": "Office",
        "title": "Workspaces",
        "lede": "Commercial fit-outs — workstations, cabins, reception, conference rooms and pantry.",
        "body": [
            "Office work runs on a different clock to residential. There is usually a lease date, a headcount to seat and a landlord's fit-out rulebook, so we plan around the handover deadline first and the mood board second.",
            "We deliver linear workstation banks, glass-front cabins, jaali and fluted partitions, reception desks, conference rooms, pantries and biophilic zones — with electrical, data and HVAC coordination drawn in rather than improvised on site.",
        ],
        "hero": "off-workstations-row",
        "gallery": ["off-desks-linear", "off-reception", "off-conference", "off-green-wall",
                    "off-jaali-partition", "off-pantry", "off-cabin-glass", "off-desks-jaali",
                    "off-lounge-planters", "off-fluted-corridor", "off-cafeteria",
                    "off-workstations-glass"],
        "video": None,
    },
    {
        "slug": "hospitality",
        "name": "Hospitality",
        "title": "Hotels",
        "lede": "Guest rooms, lobbies, corridors and lounges built to take heavy daily use.",
        "body": [
            "Hospitality interiors have to survive what homes never face: hundreds of guests, housekeeping trolleys, and a cleaning cycle that runs every single day. Specification matters more than styling, so we build to commercial tolerances and detail the junctions that normally fail first.",
            "We deliver guest rooms and suites, reception and lobby zones, feature chandeliers and ceilings, corridors and lounge seating — phased so occupied floors can keep trading while we work.",
        ],
        "hero": "htl-lobby-chandelier",
        "gallery": ["htl-suite-bed", "htl-lobby-wide", "htl-lounge-seating", "htl-room-mural",
                    "htl-lobby-arch", "htl-corridor", "htl-reception-lounge", "htl-lobby-detail"],
        "video": "htl-walkthrough",
    },
]

SERVICES = [
    ("space-planning", "Space Planning", "res-foyer-marble",
     "2D layouts that solve circulation before aesthetics — where the sofa sits, how the kitchen triangle works, whether that wardrobe door will actually open."),
    ("3d-visualisation", "3D Visualisation", "res-living-panelled",
     "Photorealistic renders of every key room, so you approve the finished look rather than imagining it from a plan."),
    ("modular-kitchen", "Modular Kitchen", "res-kitchen-island",
     "Sainik 710 BWP bases, Century MR overheads, InnoTech drawers, appliance garages and soft-close hardware throughout."),
    ("wardrobes-carpentry", "Wardrobes & Carpentry", "res-wardrobe-dresser",
     "Full-height wardrobes, media consoles, study units, crockery niches and dressing tables, built to measured site dimensions."),
    ("false-ceiling-lighting", "False Ceiling & Lighting", "res-entrance-ceiling",
     "Layered gypsum and POP ceilings with cove lighting, spotlights and profile lights planned at the drawing stage."),
    ("turnkey-execution", "Turnkey Execution", "off-conference",
     "Civil, electrical, plumbing, painting, flooring and furniture delivered under one contract and one point of contact."),
]

STATS = [
    ("Studio", "Greater Noida West"),
    ("Design fee", "₹150 / sq. ft."),
    ("Packages", "Silver · Gold · Platinum"),
    ("Kitchen base", "Sainik 710 BWP"),
    ("Sectors", "Homes · Offices · Hotels"),
    ("Delivery", "Fully turnkey"),
]

FAQS = [
    ("How is the design fee calculated?",
     "At ₹150 per square foot of carpet area, without GST. For a 1,275 sq. ft. home that is ₹1,91,250 in total. It is quoted and billed separately from execution so you can see exactly what design costs."),
    ("Is GST included in the price?",
     "No. Both the design fee and the execution package rates are shown without GST, which is charged extra at the applicable rate as per your invoice."),
    ("What do I get for the design fee?",
     "Five deliverables: 2D space planning, 3D visualisation of the key rooms, detailed execution drawings for carpentry and furniture, an RCP with electrical layouts, and a material specification chart with a detailed BOQ."),
    ("What is the difference between Silver, Gold and Platinum?",
     "The base scope is the same in all three — what changes is the finish level. Silver uses advance decorative laminates. Gold adds architectural moulding, satin and PU-enamel doors, veneer accents and soft furnishings. Platinum adds CNC and fluted panelling, Italian PU, full bathroom transformation and smart lighting."),
    ("Are the package rates final?",
     "The per-square-foot rate gives you a reliable budget from day one, without GST. The exact figure is locked after you approve the 3D, through a signed BOQ — that document then governs payment milestones and the execution schedule."),
    ("Which brands do you use?",
     "Sainik 710 BWP marine plywood for kitchen bases, Century MR grade for overheads, Hettich soft-close hinges and channels, InnoTech drawers, Asian Paints emulsions, and Jaquar or Kohler bathroom fixtures on Platinum."),
    ("Do you work outside Greater Noida West?",
     "Yes. The studio is at Gaur City Mall, and we take projects across Noida, Greater Noida, Ghaziabad, Delhi and Gurugram — residential, commercial and hospitality."),
    ("Can I engage you for design only?",
     "Yes. Phase one is deliberately standalone. You can take the drawings, the 3D and the BOQ and execute through your own contractor. Most clients continue with us, but nothing obliges you to."),
]

TESTIMONIALS = [
    ("Vinita S.", "Gaur City, Greater Noida West",
     "What sold me was the proposal itself. Everything was written down — the rate, the GST, what was in the base scope, what changed if I upgraded. Nobody else gave me numbers that clear before I paid anything."),
    ("Rohit & Anjali", "Noida Sector 137",
     "The 3D was accurate. Our living room actually looks like the render, down to the cove lighting. That sounds like a low bar until you have been through a project where it wasn't."),
    ("Amit K.", "Indirapuram, Ghaziabad",
     "We did the office fit-out against a lease deadline. Workstations, cabins, reception and pantry, and they hit the date. The coordination between electrical and civil was the part I expected to go wrong, and it didn't."),
    ("Priya M.", "Ek Murti, Greater Noida West",
     "The kitchen is what I appreciate most a year in. The Hettich hardware still closes softly and the drawers take the weight of everything I have put in them."),
    ("Hospitality client", "Greater Noida",
     "They worked floor by floor so we could keep the rest of the property running. The lobby ceiling and chandelier detailing came out better than the reference images we gave them."),
    ("Suresh R.", "Crossings Republik",
     "Straightforward people. When I asked for a change mid-project they quoted it before doing it, so the final bill matched what I had agreed to."),
]

# Video testimonials. Set "video" to a filename in assets/video/ (no extension)
# and "poster" to an image in assets/img/ once the clips are ready.
VIDEO_TESTIMONIALS = [
    {"name": "CA Sanjeev Tiwari", "where": "NX One, Greater Noida West",
     "line": "In his own words — handover walkthrough.", "video": "testimonial-sanjeev-tiwari", "poster": "testimonial-sanjeev-tiwari-poster"},
    {"name": "CA Kiran Dubey", "where": "NX One, Greater Noida West",
     "line": "In her own words — handover walkthrough.", "video": "testimonial-kiran-dubey", "poster": "testimonial-kiran-dubey-poster"},
    {"name": "Mr. Anurag Tiwari", "where": "Office project, NX One, Greater Noida West",
     "line": "In his own words — office fit-out walkthrough.", "video": "testimonial-anurag-tiwari", "poster": "testimonial-anurag-tiwari-poster"},
]

# Before / after pairs — reusable block, shown on the home page and on the
# dedicated before-after.html gallery. Add new pairs here as projects land.
BEFORE_AFTER = [
    {"title": "Modular Kitchen", "where": "Greater Noida West",
     "note": "Bare civil shell turned into a full L-shaped modular kitchen on Sainik 710 BWP with soft-close hardware.",
     "before": "ba01-kitchen-before", "after": "ba01-kitchen-after"},
    {"title": "Bedroom & TV Unit", "where": "Greater Noida West",
     "note": "An empty room becomes a finished bedroom with a marble-panelled TV wall and warm cove lighting.",
     "before": "ba02-room-before", "after": "ba02-tvunit-after"},
    {"title": "Foyer & Entrance", "where": "Greater Noida West",
     "note": "Plastered walls and bare doors transformed into a lit entrance with mirror work and storage.",
     "before": "ba03-hallway-before", "after": "ba03-entrance-after"},
    {"title": "Office Fit-out", "where": "NX One, Greater Noida West",
     "note": "A stripped-down shell, wires and all, turned into a finished coworking floor ready for handover.",
     "before": "ba04-shell-before", "after": "ba04-office-after"},
    {"title": "Living Room", "where": "Greater Noida West",
     "note": "Raw flooring and open windows become a furnished living room with a statement chandelier.",
     "before": "ba05-window-before", "after": "ba07-living-after"},
    {"title": "Common Corridor", "where": "NX One, Greater Noida West",
     "note": "An unplastered brick-and-conduit passage finished into a tiled, lit common corridor.",
     "before": "ba06-corridor-before", "after": "ba06-corridor-after"},
]

POSTS = [
    ("design-fee-explained", "Why we charge a design fee separately from execution",
     "August 12, 2026", "Process", "res-foyer-marble",
     "Bundling design into execution hides the cost of thinking. Here is what ₹150 a square foot actually buys, and why we keep it on its own invoice."),
    ("silver-gold-platinum", "Silver, Gold or Platinum: choosing the right finish level",
     "July 30, 2026", "Packages", "res-living-panelled",
     "The base scope is identical across all three. What changes is the finish — and where that money shows up in daily life."),
    ("gaur-city-3bhk", "Inside a 3BHK in Gaur City: 1,275 sq. ft., start to finish",
     "July 14, 2026", "Projects", "res-living-dining-wide",
     "Space planning, the 3D round, the BOQ, and how the finished home compared against the render."),
    ("modular-kitchen-materials", "Sainik 710 vs Century MR: what goes where in a kitchen",
     "June 26, 2026", "Materials", "res-kitchen-island",
     "Why base cabinets and overheads use different plywood grades, and what happens when a contractor uses one for both."),
    ("office-fitout-deadline", "Running an office fit-out against a lease deadline",
     "June 09, 2026", "Projects", "off-workstations-row",
     "Workstations, cabins, reception and a pantry, sequenced so the trades never wait on each other."),
    ("false-ceiling-lighting", "Plan the lighting with the ceiling, not after it",
     "May 21, 2026", "Design notes", "res-entrance-ceiling",
     "Cove lighting, spotlights and profile lights belong on the RCP drawing. Retrofitting them is how ceilings end up looking busy."),
]

# alt text for every image in assets/img
ALT = {
 "res-living-dining-wide": "Living and dining area with panelled walls, layered false ceiling and a chandelier",
 "res-living-panelled": "Living room with wall panelling, framed mirror and recessed cove lighting",
 "res-foyer-marble": "Entrance foyer with marble-effect cladding, shoe console and slatted screen",
 "res-entrance-ceiling": "Layered false ceiling with cove lighting above the entrance lobby",
 "res-crockery-niche": "Backlit crockery display niche with open shelving and drawer storage",
 "res-shoe-console": "Foyer shoe console with bench seating and a fluted timber wall",
 "res-kitchen-island": "Modular kitchen with pendant lighting, breakfast counter and profile-lit shutters",
 "res-kitchen-white": "White modular kitchen with brass handle detail and under-cabinet lighting",
 "res-kitchen-utility": "Kitchen with utility access, tall units and integrated lighting",
 "res-kitchen-lshape": "L-shaped modular kitchen with wall tiling and continuous counter lighting",
 "res-corridor-mirror": "Corridor with mirror panel, cove lighting and marble flooring",
 "res-wardrobe-dresser": "Full-height wardrobe with an integrated dressing unit and pendant lights",
 "res-lobby-slat": "Lobby with slatted timber ceiling and panelled entrance door",
 "res-bedroom-cove": "Bedroom with recessed cove lighting and a wall-mounted media console",
 "res-ceiling-detail": "False ceiling detail with profile lighting and a media unit below",
 "off-workstations-row": "Open-plan office with linear workstation banks and a green feature ceiling",
 "off-workstations-glass": "Workstations beside a full-height glass partition wall",
 "off-desks-linear": "Linear working desks with task chairs and overhead lighting",
 "off-desks-jaali": "Working desks framed by a terracotta jaali screen partition",
 "off-reception": "Office reception area with timber counter and planting",
 "off-reception-desk": "Reception desk with feature wall and accent lighting",
 "off-pantry": "Office pantry with cabinetry, counter and a jaali screen",
 "off-green-wall": "Biophilic wall with hanging planters and stone cladding",
 "off-lounge-planters": "Informal lounge seating beneath hanging planters",
 "off-cabin-glass": "Glass-fronted manager cabin with a linear light fitting",
 "off-jaali-partition": "Terracotta jaali partition dividing the workspace",
 "off-conference": "Conference room with a boardroom table and glass walls",
 "off-fluted-corridor": "Office corridor with fluted timber panelling",
 "off-cafeteria": "Office cafeteria seating with a mural feature wall",
 "htl-suite-bed": "Hotel suite with an upholstered headboard, cove ceiling and bedside lighting",
 "htl-lobby-chandelier": "Hotel lobby with a tiered crystal chandelier and circular ceiling detail",
 "htl-lounge-seating": "Hotel lounge seating with sofas, ottoman and marble flooring",
 "htl-lobby-wide": "Wide view of the hotel lobby with feature ceiling and seating",
 "htl-corridor": "Hotel corridor with panelled walls and patterned marble flooring",
 "htl-room-mural": "Hotel guest room with a hand-painted mural wall",
 "htl-lobby-arch": "Hotel lobby with a carved timber arch and chandelier",
 "htl-reception-lounge": "Hotel reception lounge with sofas and a mirrored feature wall",
 "htl-lobby-detail": "Hotel lobby ceiling and chandelier detail",
 "plat-living-classical": "Platinum package — classical living room with coffered ceiling, chandelier and marble flooring",
 "plat-bedroom-gold": "Platinum package — master bedroom with fluted headboard wall, cove lighting and crystal chandelier",
 "plat-corridor-marble": "Platinum package — colonnaded corridor with layered gold ceiling detail and marble floor",
 "gold-bedroom-rosegold": "Gold package — bedroom with curved cove ceiling, upholstered headboard and metal wall art",
 "gold-bedroom-blue": "Gold package — bedroom in blue and white with arched niche shelving and profile lighting",
 "gold-bedroom-tufted": "Gold package — bedroom with tufted headboard, wall panelling and under-bed lighting",
 "silver-living-minimal": "Silver package — living room with a neutral sofa, floor lamps and framed prints",
 "silver-living-panelled": "Silver package — living room with wall panelling, wall sconces and a marble floor",
 "silver-living-chandelier": "Silver package — living room with panelled walls, chandelier and glass centre table",
 "res-walkthrough-poster": "Still from the residential project walkthrough",
 "htl-walkthrough-poster": "Still from the hospitality project walkthrough",
 "res-kitchen-tour-poster": "Still from the modular kitchen walkthrough",
 "ba01-kitchen-before": "Bare civil-finish kitchen before renovation, tiled dado and unfinished counter",
 "ba01-kitchen-after": "Finished modular kitchen with white cabinetry, gold trim and pendant lighting",
 "ba02-room-before": "Empty plastered room before interior work, bare floor and single door",
 "ba02-tvunit-after": "Finished bedroom TV unit wall in book-matched marble with a wooden feature door",
 "ba03-hallway-before": "Unfinished room with multiple doors before interior work",
 "ba03-entrance-after": "Finished entrance passage with mirror, chandelier and fitted storage",
 "ba04-shell-before": "Bare concrete shell mid-construction with exposed ceiling grid and debris",
 "ba04-office-after": "Finished coworking office floor with workstations and exposed black ceiling",
 "ba05-window-before": "Unfinished living room with bare marble flooring and glazed window openings",
 "ba05-bedroom-after": "Finished hotel-style bedroom with a maroon and white bed runner",
 "ba06-corridor-before": "Under-construction corridor with exposed brickwork and ceiling conduit",
 "ba06-corridor-after": "Finished hotel corridor with wainscoting, patterned flooring and pendant lights",
 "ba07-living-after": "Finished living room with a circular crystal chandelier and beige upholstered sofas",
 "testimonial-sanjeev-tiwari-poster": "Video testimonial still — CA Sanjeev Tiwari, NX One",
 "testimonial-kiran-dubey-poster": "Video testimonial still — CA Kiran Dubey, NX One",
 "testimonial-anurag-tiwari-poster": "Video testimonial still — Mr. Anurag Tiwari, NX One office project",
}