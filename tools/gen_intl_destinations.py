# Generates international destination HTML pages + prints index slider snippet.
# Markup lives in tools/intl-*.html (edit HTML directly; Python only fills @@placeholders@@).
import html as html_lib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"


def load_templates():
    """Load HTML fragments from tools/; inject partials/footer-sitemap.html into footer when present."""
    sitemap_path = ROOT / "partials" / "footer-sitemap.html"
    sitemap = sitemap_path.read_text(encoding="utf-8").strip() if sitemap_path.is_file() else ""
    footer_base = (TOOLS / "intl-footer.html").read_text(encoding="utf-8")
    footer_html = footer_base.replace(
        "@@FOOTER_SITEMAP@@", "\n" + sitemap + "\n" if sitemap else ""
    )
    return {
        "layout": (TOOLS / "intl-page-layout.html").read_text(encoding="utf-8"),
        "header": (TOOLS / "intl-header.html").read_text(encoding="utf-8"),
        "footer": footer_html,
        "hotel_card": (TOOLS / "intl-hotel-card.html").read_text(encoding="utf-8"),
        "spot_card": (TOOLS / "intl-spot-card.html").read_text(encoding="utf-8"),
    }


# slug, display name, accommodations count, hero & card image (unsplash), country, region label, tagline, about, bullets[3], hotels[(name,area,price,img)], spots[(title,desc,img)]
DESTINATIONS = [
    ("dubai", "Dubai", 19464,
     "https://images.unsplash.com/photo-1512453979798-5ea266f8880c?auto=format&fit=crop&w=2200&q=86",
     "https://images.unsplash.com/photo-1512453979798-5ea266f8880c?auto=format&fit=crop&w=800&q=80",
     "United Arab Emirates", "UAE · Middle East",
     "Skyscrapers, desert adventures, and world-class dining on the Gulf.",
     "Dubai pairs futuristic architecture with beach resorts and family theme parks. Infinity Routes lists stays from Downtown and Dubai Marina to palm-fringed shores and desert retreats — ideal for shopping weekends or stopovers.",
     [
         "Metro and taxis make most sights easy; book Burj Khalifa tickets ahead.",
         "Winter (Nov–Mar) is the sweet spot for outdoor dining and beach time.",
         "Friday–Saturday is the weekend; brunches and mall hours follow local norms.",
     ],
     [
         ("Address Downtown", "Downtown · Burj views", 18900, "https://images.unsplash.com/photo-1566073771259-6a8506099945?auto=format&fit=crop&w=1000&q=80"),
         ("Atlantis The Palm", "Palm Jumeirah", 22400, "https://images.unsplash.com/photo-1582719508461-905c673771fd?auto=format&fit=crop&w=1000&q=80"),
         ("Rove City Centre", "Deira", 4200, "https://images.unsplash.com/photo-1618773928121-c32242e63f39?auto=format&fit=crop&w=1000&q=80"),
     ],
     [
         ("Burj Khalifa & Downtown", "Observation decks and the Dubai Fountain show after dark.", "https://images.unsplash.com/photo-1582672060674-bc2bd808a8b7?auto=format&fit=crop&w=900&q=80"),
         ("Dubai Mall & Old Dubai", "Luxury retail plus abras and spice souks across the creek.", "https://images.unsplash.com/photo-1518684079-3c830dcef090?auto=format&fit=crop&w=900&q=80"),
         ("Desert safari", "Dune bashing, camel rides, and Bedouin-style dinners under stars.", "https://images.unsplash.com/photo-1509316785289-025f5b846b5e?auto=format&fit=crop&w=900&q=80"),
     ]),
    ("bangkok", "Bangkok", 12048,
     "https://images.unsplash.com/photo-1563499155-4b2849c7c2e6?auto=format&fit=crop&w=2200&q=86",
     "https://images.unsplash.com/photo-1563499155-4b2849c7c2e6?auto=format&fit=crop&w=800&q=80",
     "Thailand", "Thailand · Southeast Asia",
     "Temples, rooftop bars, and legendary street food on the Chao Phraya.",
     "Bangkok is a high-energy capital of golden wats, night markets, and riverfront dining. We highlight hotels near the BTS and river ferries so you can hop between Sukhumvit, Silom, and the Old City without losing time in traffic.",
     [
         "Use the BTS/MRT and river boats to skip rush-hour gridlock.",
         "Dress modestly for Grand Palace and major temples.",
         "Carry cash for street stalls; many vendors are cash-first.",
     ],
     [
         ("Mandarin Oriental Bangkok", "Chao Phraya riverfront", 28500, "https://images.unsplash.com/photo-1566073771259-6a8506099945?auto=format&fit=crop&w=1000&q=80"),
         ("Pathumwan Princess", "Siam · BTS linked", 9800, "https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?auto=format&fit=crop&w=1000&q=80"),
         ("Casa Nithra", "Old Town · Khao San nearby", 3200, "https://images.unsplash.com/photo-1555854877-bab0e564b8d5?auto=format&fit=crop&w=1000&q=80"),
     ],
     [
         ("Grand Palace & Wat Pho", "Iconic architecture and the reclining Buddha — go early.", "https://images.unsplash.com/photo-1528181304800-259b08848561?auto=format&fit=crop&w=900&q=80"),
         ("Chatuchak Weekend Market", "Thousands of stalls — arrive hungry.", "https://images.unsplash.com/photo-1553527929-0ac90cb1b0d9?auto=format&fit=crop&w=900&q=80"),
         ("Chao Phraya dinner cruise", "City lights reflecting on the water.", "https://images.unsplash.com/photo-1540959733332-eab4deabeeaf?auto=format&fit=crop&w=900&q=80"),
     ]),
    ("abu-dhabi", "Abu Dhabi", 721,
     "https://images.unsplash.com/photo-1582672060674-bc2bd808a8b7?auto=format&fit=crop&w=2200&q=86",
     "https://images.unsplash.com/photo-1582672060674-bc2bd808a8b7?auto=format&fit=crop&w=800&q=80",
     "United Arab Emirates", "UAE · Capital",
     "Culture, Corniche walks, and island beaches away from the Dubai buzz.",
     "Abu Dhabi balances Louvre exhibits, pristine mosques, and island resorts. Stays cluster around the Corniche, Saadiyat, and Yas Island — perfect for families and art lovers.",
     [
         "Sheikh Zayed Mosque visits require modest dress and timed entry slots.",
         "Yas Island pairs theme parks with arena concerts — check event nights.",
         "Allow airport time; AUH is a major long-haul hub.",
     ],
     [
         ("Emirates Palace", "Corniche · iconic", 31200, "https://images.unsplash.com/photo-1566073771259-6a8506099945?auto=format&fit=crop&w=1000&q=80"),
         ("Park Hyatt Saadiyat", "Saadiyat Island", 14200, "https://images.unsplash.com/photo-1542314831-068cd1dbfeeb?auto=format&fit=crop&w=1000&q=80"),
         ("Southern Sun", "Al Danah", 5100, "https://images.unsplash.com/photo-1618773928121-c32242e63f39?auto=format&fit=crop&w=1000&q=80"),
     ],
     [
         ("Sheikh Zayed Grand Mosque", "Marble courtyards and reflective pools at sunset.", "https://images.unsplash.com/photo-1512632578888-169bbbc64f33?auto=format&fit=crop&w=900&q=80"),
         ("Louvre Abu Dhabi", "World art under the iconic dome.", "https://images.unsplash.com/photo-1549887534-1541e9326642?auto=format&fit=crop&w=900&q=80"),
         ("Corniche cycle & beach", "Palm-lined waterfront with family beaches.", "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=900&q=80"),
     ]),
    ("pattaya", "Pattaya", 11909,
     "https://images.unsplash.com/photo-1552465011-b4e21bf6e79a?auto=format&fit=crop&w=2200&q=86",
     "https://images.unsplash.com/photo-1552465011-b4e21bf6e79a?auto=format&fit=crop&w=800&q=80",
     "Thailand", "Thailand · Gulf coast",
     "Beach strips, island day trips, and nightlife east of Bangkok.",
     "Pattaya mixes resort hotels, water sports, and offshore escapes to Koh Larn. Infinity Routes surfaces stays along Beach Road and Jomtien for quieter evenings.",
     [
         "Songthaews (shared pickups) are the budget way to move along the coast.",
         "Combine with Bangkok via motorway or bus in a few hours.",
         "Island ferries run frequently in dry season — check last return times.",
     ],
     [
         ("Hilton Pattaya", "Central Festival rooftop", 11200, "https://images.unsplash.com/photo-1566073771259-6a8506099945?auto=format&fit=crop&w=1000&q=80"),
         ("Holiday Inn Pattaya", "Beach Road", 6400, "https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?auto=format&fit=crop&w=1000&q=80"),
         ("Red Planet", "South Pattaya", 2100, "https://images.unsplash.com/photo-1631049307264-da0ec9d70304?auto=format&fit=crop&w=1000&q=80"),
     ],
     [
         ("Sanctuary of Truth", "All-wood temple by the sea — allow a half day.", "https://images.unsplash.com/photo-1528181304800-259b08848561?auto=format&fit=crop&w=900&q=80"),
         ("Koh Larn day trip", "Snorkel-friendly beaches a short ferry away.", "https://images.unsplash.com/photo-1509316785289-025f5b846b5e?auto=format&fit=crop&w=900&q=80"),
         ("Walking Street evening", "Neon, seafood, and live music — pace yourself.", "https://images.unsplash.com/photo-1553527929-0ac90cb1b0d9?auto=format&fit=crop&w=900&q=80"),
     ]),
    ("sharjah", "Sharjah", 323,
     "https://images.unsplash.com/photo-1518684079-3c830dcef090?auto=format&fit=crop&w=2200&q=86",
     "https://images.unsplash.com/photo-1518684079-3c830dcef090?auto=format&fit=crop&w=800&q=80",
     "United Arab Emirates", "UAE · Cultural capital",
     "Museums, souks, and a relaxed Gulf vibe minutes from Dubai.",
     "Sharjah emphasizes heritage sites, art biennials, and waterfront promenades. Hotels offer value and quick access to Dubai Airport when needed.",
     [
         "Friday is quiet morning; museums may open later.",
         "Alcohol rules differ from Dubai — research hotel policies.",
         "Al Qasba and Al Majaz are family-friendly evening strolls.",
     ],
     [
         ("Sheraton Sharjah", "Al Khan lagoon", 7800, "https://images.unsplash.com/photo-1566073771259-6a8506099945?auto=format&fit=crop&w=1000&q=80"),
         ("Novotel Sharjah", "Expo area", 4500, "https://images.unsplash.com/photo-1542314831-068cd1dbfeeb?auto=format&fit=crop&w=1000&q=80"),
         ("Ibis Styles", "University City", 2900, "https://images.unsplash.com/photo-1618773928121-c32242e63f39?auto=format&fit=crop&w=1000&q=80"),
     ],
     [
         ("Sharjah Art Museum", "Regional modern art in a calm setting.", "https://images.unsplash.com/photo-1549887534-1541e9326642?auto=format&fit=crop&w=900&q=80"),
         ("Al Noor Mosque", "Waterfront mosque with guided visits.", "https://images.unsplash.com/photo-1512632578888-169bbbc64f33?auto=format&fit=crop&w=900&q=80"),
         ("Central Souk (Blue Souk)", "Handicrafts and souvenirs in iconic architecture.", "https://images.unsplash.com/photo-1553527929-0ac90cb1b0d9?auto=format&fit=crop&w=900&q=80"),
     ]),
    ("phuket", "Phuket", 12290,
     "https://images.unsplash.com/photo-1589394815804-964ed0be2eb5?auto=format&fit=crop&w=2200&q=86",
     "https://images.unsplash.com/photo-1589394815804-964ed0be2eb5?auto=format&fit=crop&w=800&q=80",
     "Thailand", "Thailand · Andaman",
     "Island-hopping, limestone karsts, and Patong energy.",
     "Phuket is Thailand’s largest island — Patong for nightlife, Kata for surf-friendly beaches, and Old Phuket Town for cafés in Sino-Portuguese shophouses.",
     [
         "Rent a scooter only with license and insurance; hills are steep.",
         "Similan trips need early starts — book dive slots in peak season.",
         "Respect roped swimming flags during monsoon months.",
     ],
     [
         ("The Nai Harn", "Nai Harn beach", 16800, "https://images.unsplash.com/photo-1582719508461-905c673771fd?auto=format&fit=crop&w=1000&q=80"),
         ("Holiday Inn Express Patong", "Walk to beach", 4100, "https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?auto=format&fit=crop&w=1000&q=80"),
         ("Lub d Phuket", "Patong · social", 1800, "https://images.unsplash.com/photo-1555854877-bab0e564b8d5?auto=format&fit=crop&w=1000&q=80"),
     ],
     [
         ("Phi Phi day tour", "Long-tail boats and Maya Bay viewpoints.", "https://images.unsplash.com/photo-1589394815804-964ed0be2eb5?auto=format&fit=crop&w=900&q=80"),
         ("Big Buddha", "Panoramic island views after a scenic drive.", "https://images.unsplash.com/photo-1528181304800-259b08848561?auto=format&fit=crop&w=900&q=80"),
         ("Phuket Old Town", "Colorful streets and Sunday walking market.", "https://images.unsplash.com/photo-1552465011-b4e21bf6e79a?auto=format&fit=crop&w=900&q=80"),
     ]),
    ("bali", "Bali", 32908,
     "https://images.unsplash.com/photo-1537996194471-e657df975ab4?auto=format&fit=crop&w=2200&q=86",
     "https://images.unsplash.com/photo-1537996194471-e657df975ab4?auto=format&fit=crop&w=800&q=80",
     "Indonesia", "Indonesia · Islands",
     "Rice terraces, surf towns, and wellness retreats.",
     "Bali blends Hindu temples with jungle villas and beach clubs. Ubud for culture, Canggu for digital nomads, Uluwatu for cliffs — Infinity Routes maps stays to your pace.",
     [
         "Scooter traffic is dense — wear helmet and avoid rush near Seminyak.",
         "Temple visits need sarongs; often available at entrance.",
         "Dry season (Apr–Oct) is peak; book Nyepi dates early.",
     ],
     [
         ("Ayana Resort", "Jimbaran cliffs", 24500, "https://images.unsplash.com/photo-1566073771259-6a8506099945?auto=format&fit=crop&w=1000&q=80"),
         ("Alila Ubud", "Jungle infinity pool", 18200, "https://images.unsplash.com/photo-1542314831-068cd1dbfeeb?auto=format&fit=crop&w=1000&q=80"),
         ("Grandmas Plus Seminyak", "Seminyak lanes", 2900, "https://images.unsplash.com/photo-1618773928121-c32242e63f39?auto=format&fit=crop&w=1000&q=80"),
     ],
     [
         ("Tegallalang rice terraces", "Sunrise walks and swings above paddies.", "https://images.unsplash.com/photo-1537953773345-d172fca13bb2?auto=format&fit=crop&w=900&q=80"),
         ("Uluwatu Temple", "Clifftop kecak fire dance at dusk.", "https://images.unsplash.com/photo-1518548419970-58e3b4079ab2?auto=format&fit=crop&w=900&q=80"),
         ("Nusa Penida day trip", "Kelingking Beach viewpoints.", "https://images.unsplash.com/photo-1559827260-dc66d52bef19?auto=format&fit=crop&w=900&q=80"),
     ]),
    ("kuala-lumpur", "Kuala Lumpur", 19902,
     "https://images.unsplash.com/photo-1596422846543-75c6fc197f07?auto=format&fit=crop&w=2200&q=86",
     "https://images.unsplash.com/photo-1596422846543-75c6fc197f07?auto=format&fit=crop&w=800&q=80",
     "Malaysia", "Malaysia · Peninsula",
     "Petronas towers, hawker food, and Batu Caves day trips.",
     "KL is a compact hub of malls, rooftop bars, and multicultural neighborhoods. Stay near KLCC or Bukit Bintang for walkable evenings.",
     [
         "Grab rides are affordable; monorail links key districts.",
         "Rain afternoons are common — carry a light umbrella.",
         "Try Jalan Alor after dark for open-air street food.",
     ],
     [
         ("Mandarin Oriental KL", "KLCC park views", 15200, "https://images.unsplash.com/photo-1566073771259-6a8506099945?auto=format&fit=crop&w=1000&q=80"),
         ("Capri by Fraser", "Bukit Bintang", 6200, "https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?auto=format&fit=crop&w=1000&q=80"),
         ("BackHome Hostel", "Chinatown", 1400, "https://images.unsplash.com/photo-1555854877-bab0e564b8d5?auto=format&fit=crop&w=1000&q=80"),
     ],
     [
         ("Petronas Twin Towers", "Skybridge tickets sell out — book online.", "https://images.unsplash.com/photo-1596422846543-75c6fc197f07?auto=format&fit=crop&w=900&q=80"),
         ("Batu Caves", "Rainbow steps and cave temples — mind the monkeys.", "https://images.unsplash.com/photo-1596422846543-75c6fc197f07?auto=format&fit=crop&w=900&q=80"),
         ("Merdeka Square", "Colonial core and museums on foot.", "https://images.unsplash.com/photo-1596422846543-75c6fc197f07?auto=format&fit=crop&w=900&q=80"),
     ]),
    ("ajman", "Ajman", 264,
     "https://images.unsplash.com/photo-1512453979798-5ea266f8880c?auto=format&fit=crop&w=2200&q=86",
     "https://images.unsplash.com/photo-1512453979798-5ea266f8880c?auto=format&fit=crop&w=800&q=80",
     "United Arab Emirates", "UAE · Emirate",
     "Quiet Corniche, mangroves, and value stays near Sharjah & Dubai.",
     "Ajman offers relaxed beaches and heritage museums without the mega-resort scale. Ideal for budget-conscious travelers exploring the northern Emirates.",
     [
         "Ajman Museum in an old fort tells pearl-diving history.",
         "Quick hops to Sharjah museums or Dubai Marina by car.",
         "Weekend evenings on the Corniche are breezy and family-friendly.",
     ],
     [
         ("Ajman Saray", "Luxury Collection beach", 9800, "https://images.unsplash.com/photo-1582719508461-905c673771fd?auto=format&fit=crop&w=1000&q=80"),
         ("Oberoi Beach Resort", "Al Zorah", 12400, "https://images.unsplash.com/photo-1566073771259-6a8506099945?auto=format&fit=crop&w=1000&q=80"),
         ("Ramada Hotel & Suites", "Sheikh Khalifa", 3800, "https://images.unsplash.com/photo-1618773928121-c32242e63f39?auto=format&fit=crop&w=1000&q=80"),
     ],
     [
         ("Ajman Corniche", "Palm-lined walks and cafés at sunset.", "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=900&q=80"),
         ("Al Zorah Nature Reserve", "Kayak mangrove channels.", "https://images.unsplash.com/photo-1509316785289-025f5b846b5e?auto=format&fit=crop&w=900&q=80"),
         ("Heritage district", "Souks and dhow-building yards.", "https://images.unsplash.com/photo-1518684079-3c830dcef090?auto=format&fit=crop&w=900&q=80"),
     ]),
    ("da-nang", "Da Nang", 5534,
     "https://images.unsplash.com/photo-1559592413-7cec4d0cae2b?auto=format&fit=crop&w=2200&q=86",
     "https://images.unsplash.com/photo-1559592413-7cec4d0cae2b?auto=format&fit=crop&w=800&q=80",
     "Vietnam", "Vietnam · Central coast",
     "My Khe beach, Marble Mountains, and Hoi An day trips.",
     "Da Nang is Vietnam’s coastal playground — long beaches, dragon bridges, and easy drives to Hue or Hoi An. Hotels line the seafront and Han River.",
     [
         "Motorbike taxis are common; agree price or use ride apps.",
         "Marble Mountains climb needs sturdy shoes.",
         "Hoi An lanterns are 30–45 min south — leave before dusk traffic.",
     ],
     [
         ("Fusion Maia", "My Khe · spa-inclusive", 14200, "https://images.unsplash.com/photo-1566073771259-6a8506099945?auto=format&fit=crop&w=1000&q=80"),
         ("Novotel Danang", "Premier Han River", 5100, "https://images.unsplash.com/photo-1542314831-068cd1dbfeeb?auto=format&fit=crop&w=1000&q=80"),
         ("Merry Land Hotel", "Han market area", 2400, "https://images.unsplash.com/photo-1631049307264-da0ec9d70304?auto=format&fit=crop&w=1000&q=80"),
     ],
     [
         ("My Khe Beach", "Morning swims and surf-friendly sand.", "https://images.unsplash.com/photo-1559592413-7cec4d0cae2b?auto=format&fit=crop&w=900&q=80"),
         ("Golden Bridge Ba Na Hills", "Hands in the clouds — cable car day.", "https://images.unsplash.com/photo-1559827260-dc66d52bef19?auto=format&fit=crop&w=900&q=80"),
         ("Marble Mountains", "Caves, pagodas, and coastal views.", "https://images.unsplash.com/photo-1528181304800-259b08848561?auto=format&fit=crop&w=900&q=80"),
     ]),
    ("ho-chi-minh-city", "Ho Chi Minh City", 15546,
     "https://images.unsplash.com/photo-1583417319070-4a69db38cd48?auto=format&fit=crop&w=2200&q=86",
     "https://images.unsplash.com/photo-1583417319070-4a69db38cd48?auto=format&fit=crop&w=800&q=80",
     "Vietnam", "Vietnam · South",
     "Saigon energy: coffee, markets, and Mekong side trips.",
     "HCMC layers French colonial façades with rooftop nightlife and alley pho stalls. District 1 stays keep you near Opera House and Nguyen Hue walking street.",
     [
         "Cross streets carefully — traffic flows constant.",
         "Cu Chi tunnels and Mekong tours are full-day excursions.",
         "Carry small dong notes for street vendors.",
     ],
     [
         ("Park Hyatt Saigon", "Lam Son Square", 19800, "https://images.unsplash.com/photo-1566073771259-6a8506099945?auto=format&fit=crop&w=1000&q=80"),
         ("Liberty Central Riverside", "District 1", 5400, "https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?auto=format&fit=crop&w=1000&q=80"),
         ("The Common Room", "Ben Thanh area", 1900, "https://images.unsplash.com/photo-1555854877-bab0e564b8d5?auto=format&fit=crop&w=1000&q=80"),
     ],
     [
         ("War Remnants Museum", "Powerful exhibits — allow reflective time.", "https://images.unsplash.com/photo-1583417319070-4a69db38cd48?auto=format&fit=crop&w=900&q=80"),
         ("Cu Chi tunnels", "Historic network with optional firing range.", "https://images.unsplash.com/photo-1528181304800-259b08848561?auto=format&fit=crop&w=900&q=80"),
         ("Ben Thanh Market", "Night street food outside the hall.", "https://images.unsplash.com/photo-1553527929-0ac90cb1b0d9?auto=format&fit=crop&w=900&q=80"),
     ]),
    ("krabi", "Krabi", 2053,
     "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?auto=format&fit=crop&w=2200&q=86",
     "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?auto=format&fit=crop&w=800&q=80",
     "Thailand", "Thailand · Andaman",
     "Railay cliffs, long-tail boats, and island silence.",
     "Krabi Town is the gateway; Railay and Ao Nang deliver limestone drama. Pick resorts with long-tail pier access for island hopping.",
     [
         "Monsoon waves can limit boats — check pier notices.",
         "Rock climbing schools operate on Railay for beginners.",
         "Phi Phi ferries depart early; hotels often pack breakfast boxes.",
     ],
     [
         ("Rayavadee", "Railay peninsula", 28500, "https://images.unsplash.com/photo-1582719508461-905c673771fd?auto=format&fit=crop&w=1000&q=80"),
         ("Holiday Inn Ao Nang", "Beach strip", 6200, "https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?auto=format&fit=crop&w=1000&q=80"),
         ("Slumber Party Hostel", "Ao Nang", 1100, "https://images.unsplash.com/photo-1555854877-bab0e564b8d5?auto=format&fit=crop&w=1000&q=80"),
     ],
     [
         ("Railay Beach", "No roads — arrive by boat only.", "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?auto=format&fit=crop&w=900&q=80"),
         ("Tiger Cave Temple", "1237 steps to a giant Buddha view.", "https://images.unsplash.com/photo-1528181304800-259b08848561?auto=format&fit=crop&w=900&q=80"),
         ("Four Islands tour", "Tup, Chicken, Poda — classic long-tail day.", "https://images.unsplash.com/photo-1589394815804-964ed0be2eb5?auto=format&fit=crop&w=900&q=80"),
     ]),
    ("singapore", "Singapore", 1326,
     "https://images.unsplash.com/photo-1525625293386-3f8f99389edd?auto=format&fit=crop&w=2200&q=86",
     "https://images.unsplash.com/photo-1525625293386-3f8f99389edd?auto=format&fit=crop&w=800&q=80",
     "Singapore", "Singapore · City-state",
     "Gardens, hawker culture, and Marina Bay after dark.",
     "Singapore packs hawker centers, Sentosa beaches, and cloud forests into a clean, transit-rich island. Stays in Civic District or Orchard keep you connected.",
     [
         "EZ-link or contactless cards simplify MRT and buses.",
         "Hawker stalls often cash or local pay apps — carry SGD.",
         "Rain bursts are short; carry a compact umbrella.",
     ],
     [
         ("Marina Bay Sands", "SkyPark iconic", 38500, "https://images.unsplash.com/photo-1566073771259-6a8506099945?auto=format&fit=crop&w=1000&q=80"),
         ("Hotel Jen Orchardgateway", "Orchard", 11200, "https://images.unsplash.com/photo-1542314831-068cd1dbfeeb?auto=format&fit=crop&w=1000&q=80"),
         ("The Pod", "Bugis capsule", 3200, "https://images.unsplash.com/photo-1631049307264-da0ec9d70304?auto=format&fit=crop&w=1000&q=80"),
     ],
     [
         ("Gardens by the Bay", "Supertree Grove light show nightly.", "https://images.unsplash.com/photo-1525625293386-3f8f99389edd?auto=format&fit=crop&w=900&q=80"),
         ("Lau Pa Sat", "Satay street after 7pm.", "https://images.unsplash.com/photo-1553621042-f6e147245754?auto=format&fit=crop&w=900&q=80"),
         ("Sentosa beaches", "Cable car or boardwalk from Vivocity.", "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=900&q=80"),
     ]),
    ("ras-al-khaimah", "Ras Al Khaimah", 398,
     "https://images.unsplash.com/photo-1509316785289-025f5b846b5e?auto=format&fit=crop&w=2200&q=86",
     "https://images.unsplash.com/photo-1509316785289-025f5b846b5e?auto=format&fit=crop&w=800&q=80",
     "United Arab Emirates", "UAE · Northern emirate",
     "Jebel Jais zipline, desert camps, and quiet beaches.",
     "RAK mixes adventure sports on the UAE’s highest peak with beach resorts on Al Marjan Island — a calmer foil to Dubai.",
     [
         "Mountain roads to Jebel Jais cool sharply — bring a layer.",
         "Beach resorts run free shuttles from DXB depending on brand.",
         "Friday brunches book fast at resort hotels.",
     ],
     [
         ("Waldorf Astoria RAK", "Vienna-style beach", 15200, "https://images.unsplash.com/photo-1566073771259-6a8506099945?auto=format&fit=crop&w=1000&q=80"),
         ("DoubleTree Marjan Island", "Seafront", 6800, "https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?auto=format&fit=crop&w=1000&q=80"),
         ("Citymax", "RAK downtown", 2200, "https://images.unsplash.com/photo-1618773928121-c32242e63f39?auto=format&fit=crop&w=1000&q=80"),
     ],
     [
         ("Jebel Jais Flight", "Longest zipline ride above wadis.", "https://images.unsplash.com/photo-1509316785289-025f5b846b5e?auto=format&fit=crop&w=900&q=80"),
         ("Al Marjan Island", "Waterfront promenade and cafés.", "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=900&q=80"),
         ("National Museum of RAK", "Pearl trade history in a fort setting.", "https://images.unsplash.com/photo-1549887534-1541e9326642?auto=format&fit=crop&w=900&q=80"),
     ]),
    ("hanoi", "Hanoi", 10744,
     "https://images.unsplash.com/photo-1509031438505-ba0ca31d2dd8?auto=format&fit=crop&w=2200&q=86",
     "https://images.unsplash.com/photo-1509031438505-ba0ca31d2dd8?auto=format&fit=crop&w=800&q=80",
     "Vietnam", "Vietnam · North",
     "Old Quarter lanes, egg coffee, and Ha Long gateways.",
     "Hanoi’s thousand-year core hums with scooters, street bun cha, and lakeside walks. Boutique stays hide in the Old Quarter’s narrow streets.",
     [
         "Train Street visits follow timed safety rules — go with guides.",
         "Ha Long overnight cruises often pick up from Hanoi hotels.",
         "Winter can dip cool — pack a light jacket.",
     ],
     [
         ("Sofitel Legend Metropole", "Hoan Kiem", 22400, "https://images.unsplash.com/photo-1566073771259-6a8506099945?auto=format&fit=crop&w=1000&q=80"),
         ("La Siesta Premium", "Old Quarter", 7200, "https://images.unsplash.com/photo-1542314831-068cd1dbfeeb?auto=format&fit=crop&w=1000&q=80"),
         ("Hanoi Rocks Hostel", "Ma May", 1400, "https://images.unsplash.com/photo-1555854877-bab0e564b8d5?auto=format&fit=crop&w=1000&q=80"),
     ],
     [
         ("Hoan Kiem Lake", "Ngoc Son Temple on the red bridge.", "https://images.unsplash.com/photo-1509031438505-ba0ca31d2dd8?auto=format&fit=crop&w=900&q=80"),
         ("Temple of Literature", "Vietnam’s first university courtyards.", "https://images.unsplash.com/photo-1528181304800-259b08848561?auto=format&fit=crop&w=900&q=80"),
         ("Ha Long Bay cruise", "Day or overnight from Hanoi piers.", "https://images.unsplash.com/photo-1559827260-dc66d52bef19?auto=format&fit=crop&w=900&q=80"),
     ]),
    ("mecca", "Mecca", 970,
     "https://images.unsplash.com/photo-1591604129939-fe8b0a994478?auto=format&fit=crop&w=2200&q=86",
     "https://images.unsplash.com/photo-1591604129939-fe8b0a994478?auto=format&fit=crop&w=800&q=80",
     "Saudi Arabia", "Saudi Arabia · Hijaz",
     "The holiest city in Islam — spiritual focus and modern hospitality.",
     "Mecca welcomes millions for Umrah and Hajj. Hotels ring the Haram with varying walking distances; Infinity Routes notes family-friendly towers with wheelchair access.",
     [
         "Visa and permit rules change — confirm eligibility before booking.",
         "Modest dress codes apply in public spaces.",
         "Zamzam and prayer times shape daily rhythms — plan rest windows.",
     ],
     [
         ("Clock Tower Fairmont", "Abraj Al Bait", 28500, "https://images.unsplash.com/photo-1566073771259-6a8506099945?auto=format&fit=crop&w=1000&q=80"),
         ("Pullman ZamZam", "Haram front", 19200, "https://images.unsplash.com/photo-1542314831-068cd1dbfeeb?auto=format&fit=crop&w=1000&q=80"),
         ("Elaf Kinda", "Ibrahim Khalil", 8900, "https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?auto=format&fit=crop&w=1000&q=80"),
     ],
     [
         ("Masjid al-Haram", "Central mosque — follow crowd management guides.", "https://images.unsplash.com/photo-1591604129939-fe8b0a994478?auto=format&fit=crop&w=900&q=80"),
         ("Abraj Al Bait complex", "Malls and viewing decks near the clock tower.", "https://images.unsplash.com/photo-1512632578888-169bbbc64f33?auto=format&fit=crop&w=900&q=80"),
         ("Zamzam well area", "Historic spring within the mosque precincts.", "https://images.unsplash.com/photo-1512632578888-169bbbc64f33?auto=format&fit=crop&w=900&q=80"),
     ]),
    ("fujairah", "Fujairah", 153,
     "https://images.unsplash.com/photo-1544551763-46a013bb70d5?auto=format&fit=crop&w=2200&q=86",
     "https://images.unsplash.com/photo-1544551763-46a013bb70d5?auto=format&fit=crop&w=800&q=80",
     "United Arab Emirates", "UAE · East coast",
     "Indian Ocean beaches, forts, and diving on the east coast.",
     "Fujairah faces the Gulf of Oman with clearer diving than the Arabian Gulf side. Resorts line Dibba and Al Aqah for snorkel weekends.",
     [
         "Mountain roads from Dubai cross dramatic wadis — fuel up.",
         "Friday diving trips need advance booking in season.",
         "Heritage Village shows traditional barasti houses.",
     ],
     [
         ("Le Meridien Al Aqah", "Beach resort", 8900, "https://images.unsplash.com/photo-1582719508461-905c673771fd?auto=format&fit=crop&w=1000&q=80"),
         ("Ibis Fujairah", "City centre", 3600, "https://images.unsplash.com/photo-1618773928121-c32242e63f39?auto=format&fit=crop&w=1000&q=80"),
         ("Virgin beach camp", "Dibba", 4500, "https://images.unsplash.com/photo-1555854877-bab0e564b8d5?auto=format&fit=crop&w=1000&q=80"),
     ],
     [
         ("Al-Bidyah Mosque", "Oldest UAE mosque — compact and scenic.", "https://images.unsplash.com/photo-1544551763-46a013bb70d5?auto=format&fit=crop&w=900&q=80"),
         ("Snoopy Island", "Snorkel spot off Al Aqah beach.", "https://images.unsplash.com/photo-1509316785289-025f5b846b5e?auto=format&fit=crop&w=900&q=80"),
         ("Fujairah Fort", "Hilltop views over the old town.", "https://images.unsplash.com/photo-1528181304800-259b08848561?auto=format&fit=crop&w=900&q=80"),
     ]),
    ("kathmandu", "Kathmandu", 1914,
     "https://images.unsplash.com/photo-1609137144813-7d992893be098?auto=format&fit=crop&w=2200&q=86",
     "https://images.unsplash.com/photo-1609137144813-7d992893be098?auto=format&fit=crop&w=800&q=80",
     "Nepal", "Nepal · Kathmandu Valley",
     "Stupas, thangkas, and trekking gateways to the Himalaya.",
     "Kathmandu is the valley hub for Durbar squares, Boudhanath’s mandala, and Lukla flight connections. Guesthouses suit trek planners and culture seekers alike.",
     [
         "Altitude prep matters before flying to high trails.",
         "Cash still king in Thamel — ATMs exist but carry backup.",
         "Respect photography rules at temples and cremation ghats.",
     ],
     [
         ("Dwarika’s Hotel", "Heritage luxury", 18500, "https://images.unsplash.com/photo-1566073771259-6a8506099945?auto=format&fit=crop&w=1000&q=80"),
         ("Aloft Thamel", "Rooftop views", 5200, "https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?auto=format&fit=crop&w=1000&q=80"),
         ("Zostel Kathmandu", "Thamel social", 900, "https://images.unsplash.com/photo-1555854877-bab0e564b8d5?auto=format&fit=crop&w=1000&q=80"),
     ],
     [
         ("Boudhanath Stupa", "Kora walks at sunrise with prayer flags.", "https://images.unsplash.com/photo-1609137144813-7d992893be098?auto=format&fit=crop&w=900&q=80"),
         ("Patan Durbar Square", "Newari architecture south of the river.", "https://images.unsplash.com/photo-1528181304800-259b08848561?auto=format&fit=crop&w=900&q=80"),
         ("Swayambhunath", "Monkey temple panoramas over the valley.", "https://images.unsplash.com/photo-1609137144813-7d992893be098?auto=format&fit=crop&w=900&q=80"),
     ]),
    ("medina", "Medina", 745,
     "https://images.unsplash.com/photo-1548013146-72479768b4b8?auto=format&fit=crop&w=2200&q=86",
     "https://images.unsplash.com/photo-1548013146-72479768b4b8?auto=format&fit=crop&w=800&q=80",
     "Saudi Arabia", "Saudi Arabia · Hijaz",
     "The Prophet’s Mosque and peaceful courtyard hospitality.",
     "Medina offers a calmer rhythm than Hajj peaks in Mecca, with hotels fanning out from Al Masjid an Nabawi. Courtyard seating and dates are part of local welcome.",
     [
         "Women’s sections and entry gates have specific timings — check notices.",
         "High-speed rail links Medina and Mecca for eligible travelers.",
         "Evenings around the plaza are busiest after prayers.",
     ],
     [
         ("Oberoi Medina", "Pilgrim walk proximity", 21200, "https://images.unsplash.com/photo-1566073771259-6a8506099945?auto=format&fit=crop&w=1000&q=80"),
         ("Taiba Front Hotel", "Central", 12400, "https://images.unsplash.com/photo-1542314831-068cd1dbfeeb?auto=format&fit=crop&w=1000&q=80"),
         ("Ewan Dar Al Hijra", "Budget tower", 4800, "https://images.unsplash.com/photo-1618773928121-c32242e63f39?auto=format&fit=crop&w=1000&q=80"),
     ],
     [
         ("Al Masjid an Nabawi", "Green dome and vast courtyards.", "https://images.unsplash.com/photo-1548013146-72479768b4b8?auto=format&fit=crop&w=900&q=80"),
         ("Quba Mosque", "First mosque — short trip from the centre.", "https://images.unsplash.com/photo-1512632578888-169bbbc64f33?auto=format&fit=crop&w=900&q=80"),
         ("Mount Uhud", "Historic battlefield viewpoints.", "https://images.unsplash.com/photo-1509316785289-025f5b846b5e?auto=format&fit=crop&w=900&q=80"),
     ]),
    ("phu-quoc-island", "Phu Quoc Island", 4127,
     "https://images.unsplash.com/photo-1559827260-dc66d52bef19?auto=format&fit=crop&w=2200&q=86",
     "https://images.unsplash.com/photo-1559827260-dc66d52bef19?auto=format&fit=crop&w=800&q=80",
     "Vietnam", "Vietnam · Gulf of Thailand",
     "Island resorts, night markets, and snorkel-friendly south coast.",
     "Phu Quoc pairs jungle interior roads with white-sand bays and pearl farms. West-coast sunsets at Long Beach are a nightly ritual.",
     [
         "Domestic flights from HCMC and Hanoi land at PQC airport.",
         "Dry season (Nov–Apr) is best for boat tours.",
         "Night market seafood — confirm prices before seating.",
     ],
     [
         ("JW Marriott Phu Quoc", "Emerald Bay", 22400, "https://images.unsplash.com/photo-1566073771259-6a8506099945?auto=format&fit=crop&w=1000&q=80"),
         ("Lahana Resort", "Long Beach", 6800, "https://images.unsplash.com/photo-1582719508461-905c673771fd?auto=format&fit=crop&w=1000&q=80"),
         ("Mango Bay", "Rustic bungalows", 4100, "https://images.unsplash.com/photo-1555854877-bab0e564b8d5?auto=format&fit=crop&w=1000&q=80"),
     ],
     [
         ("Sunset at Long Beach", "West-coast bars and fire shows.", "https://images.unsplash.com/photo-1559827260-dc66d52bef19?auto=format&fit=crop&w=900&q=80"),
         ("Vinpearl Safari", "Family wildlife park in the north.", "https://images.unsplash.com/photo-1509316785289-025f5b846b5e?auto=format&fit=crop&w=900&q=80"),
         ("An Thoi islands", "Snorkel and cable car island hop.", "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=900&q=80"),
     ]),
]


def fmt_rs(n):
    return "Rs. {:,}".format(n)


def build_page(d, t):
    slug, name, acc, hero, card_img, country, region, tagline, about, bullets, hotels, spots = d
    esc = html_lib.escape
    bullets_html = "\n".join(
        f'            <li class="flex gap-2"><span class="mt-1.5 h-1.5 w-1.5 shrink-0 rounded-full bg-sky-500"></span> {esc(b)}</li>'
        for b in bullets
    )
    hotels_html = ""
    for hname, area, price, himg in hotels:
        hotels_html += (
            t["hotel_card"]
            .replace("@@HOTEL_IMG@@", himg)
            .replace("@@HOTEL_NAME@@", esc(hname))
            .replace("@@AREA@@", esc(area))
            .replace("@@PRICE@@", fmt_rs(price))
        )
    spots_html = ""
    for title, desc, simg in spots:
        spots_html += (
            t["spot_card"]
            .replace("@@SPOT_IMG@@", simg)
            .replace("@@SPOT_TITLE@@", esc(title))
            .replace("@@SPOT_DESC@@", esc(desc))
        )

    hero_css = (
        f'      background-image: linear-gradient(105deg, rgba(15, 23, 42, 0.92) 0%, rgba(15, 23, 42, 0.62) 38%, rgba(2, 132, 199, 0.28) 72%, rgba(15, 23, 42, 0.45) 100%),\n        url("{hero}");'
    )

    title = f"{esc(name)} — City guide &amp; hotels | Infinity Routes Travels"
    meta = f"Explore {esc(name)}: hand-picked hotels, top places to visit, and travel tips with Infinity Routes Travels."
    acc_listed = f"{acc:,}"

    html = t["layout"]
    for key, val in (
        ("@@TITLE@@", title),
        ("@@META_DESCRIPTION@@", meta),
        ("@@HERO_CSS@@", hero_css),
        ("@@HEADER@@", t["header"]),
        ("@@REGION@@", esc(region)),
        ("@@NAME@@", esc(name)),
        ("@@TAGLINE@@", esc(tagline)),
        ("@@ACC_LISTED@@", acc_listed),
        ("@@COUNTRY@@", esc(country)),
        ("@@ABOUT@@", esc(about)),
        ("@@BULLETS@@", bullets_html),
        ("@@CARD_IMG@@", card_img),
        ("@@HOTELS@@", hotels_html),
        ("@@SPOTS@@", spots_html),
        ("@@FOOTER@@", t["footer"]),
    ):
        html = html.replace(key, val)
    return html


def main():
    t = load_templates()
    slider_cards = []
    for d in DESTINATIONS:
        slug, name, acc, _h, card_img, _c, _r, _t, _a, _b, _hot, _s = d
        path = ROOT / f"{slug}.html"
        path.write_text(build_page(d, t), encoding="utf-8")
        print("wrote", path.name)
        acc_s = f"{acc:,}"
        slider_cards.append(
            f'        <a href="{slug}.html" class="group card-lift min-w-[210px] snap-start block overflow-hidden rounded-2xl border border-slate-100 bg-white shadow-sm ring-1 ring-slate-100 focus:outline-none focus-visible:ring-2 focus-visible:ring-sky-500"><div class="card-media card-media--intl"><img src="{card_img}" alt="{html_lib.escape(name)}" loading="lazy" decoding="async" /></div><div class="p-4 text-center"><h3 class="font-bold text-slate-900">{html_lib.escape(name)}</h3><p class="text-sm text-slate-500">{acc_s} accommodations</p></div></a>'
        )

    frag = ROOT / "tools" / "_intl_slider_fragment.html"
    frag.write_text(
        "\n".join(slider_cards),
        encoding="utf-8",
    )
    print("wrote fragment", frag)


if __name__ == "__main__":
    main()
