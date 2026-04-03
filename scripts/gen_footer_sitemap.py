# -*- coding: utf-8 -*-
"""Generate partials/footer-sitemap.html (Tailwind) and partials/footer-sitemap-bootstrap.html"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
D = "destination.html"  # generic browse

# (label, href) — use real pages where they exist
def h(label, page=None):
    return (label, page if page else D)

# Destination Cities — Asia (from user list)
ASIA_CITIES = [
    h("Bali Hotels", "bali.html"),
    h("Bandung Hotels"),
    h("Bangkok Hotels", "bangkok.html"),
    h("Boracay Island Hotels"),
    h("Busan Hotels"),
    h("Cebu Hotels"),
    h("Chiang Mai Hotels"),
    h("Da Nang Hotels", "da-nang.html"),
    h("Fukuoka Hotels"),
    h("Hanoi Hotels", "hanoi.html"),
    h("Hat Yai Hotels"),
    h("Ho Chi Minh City Hotels", "ho-chi-minh-city.html"),
    h("Hoi An Hotels"),
    h("Hong Kong Hotels"),
    h("Hua Hin Hotels"),
    h("Hualien Hotels"),
    h("Ipoh Hotels"),
    h("Jakarta Hotels"),
    h("Jeju Island Hotels"),
    h("Johor Bahru Hotels"),
    h("Kaohsiung Hotels"),
    h("Kota Kinabalu Hotels"),
    h("Krabi Hotels", "krabi.html"),
    h("Kuala Lumpur Hotels", "kuala-lumpur.html"),
    h("Kuantan Hotels"),
    h("Kyoto Hotels"),
    h("Malacca Hotels"),
    h("Manila Hotels"),
    h("Nagoya Hotels"),
    h("Nha Trang Hotels"),
    h("Okinawa Hotels"),
    h("Osaka Hotels"),
    h("Pattaya Hotels", "pattaya.html"),
    h("Penang Hotels"),
    h("Phuket Hotels", "phuket.html"),
    h("Sapporo Hotels"),
    h("Seoul Hotels"),
    h("Shanghai Hotels"),
    h("Singapore Hotels", "singapore.html"),
    h("Surabaya Hotels"),
    h("Taichung Hotels"),
    h("Tainan Hotels"),
    h("Taipei Hotels"),
    h("Tokyo Hotels"),
    h("Yilan Hotels"),
    h("Yogyakarta Hotels"),
]

EUROPE_CITIES = [
    h("London Hotels"),
    h("Paris Hotels"),
]

ME_CITIES = [
    h("Dubai Hotels", "dubai.html"),
]

# Countries & Territories
AFRICA_C = [h("Morocco Hotels"), h("South Africa Hotels")]
AMERICAS_C = [
    h("Argentina Hotels"),
    h("Brazil Hotels"),
    h("Canada Hotels"),
    h("Mexico Hotels"),
    h("United States Hotels"),
    h("Venezuela Hotels"),
]
ASIA_COUNTRIES = [
    h("Cambodia Hotels"),
    h("China Hotels"),
    h("India Hotels"),
    h("Indonesia Hotels"),
    h("Japan Hotels"),
    h("Laos Hotels"),
    h("Malaysia Hotels"),
    h("Myanmar Hotels"),
    h("Nepal Hotels"),
    h("Philippines Hotels"),
    h("South Korea Hotels"),
    h("Sri Lanka Hotels"),
    h("Taiwan Hotels"),
    h("Thailand Hotels"),
    h("Vietnam Hotels"),
]
EUROPE_COUNTRIES = [
    h("Austria Hotels"),
    h("Czech Republic Hotels"),
    h("Denmark Hotels"),
    h("Finland Hotels"),
    h("France Hotels"),
    h("Germany Hotels"),
    h("Greece Hotels"),
    h("Hungary Hotels"),
    h("Ireland Hotels"),
    h("Italy Hotels"),
    h("Netherlands Hotels"),
    h("Russia Hotels"),
    h("Spain Hotels"),
    h("Sweden Hotels"),
    h("Switzerland Hotels"),
    h("United Kingdom Hotels"),
]
ME_COUNTRIES = [
    h("Bahrain Hotels"),
    h("Egypt Hotels"),
    h("Israel Hotels"),
    h("United Arab Emirates Hotels"),
]
OCEANIA_C = [h("Australia Hotels"), h("New Zealand Hotels")]

# Destination Guides
GUIDES_HOME = [("Destination Guides Home", "destination.html")]
GUIDES_ASIA = [
    ("Bali Guide", "bali.html"),
    ("Nagasaki Guide", D),
    ("Hong Kong Guide", D),
    ("Jakarta Guide", D),
    ("Jeju Island Guide", D),
    ("Kuala Lumpur Guide", "kuala-lumpur.html"),
    ("Kyoto Guide", D),
    ("Kyushu Guide", D),
    ("Malacca Guide", D),
    ("Philippines Guide", D),
    ("Nara Guide", D),
    ("Osaka Guide", D),
    ("Phuket Guide", "phuket.html"),
    ("Sapporo Guide", D),
    ("Seoul Guide", D),
    ("Singapore Guide", "singapore.html"),
    ("Taichung Guide", D),
    ("Taipei Guide", D),
    ("Tokyo Guide", D),
    ("Goa Guide", "goa.html"),
]
GUIDES_EUROPE = [("Paris Guide", D)]
GUIDES_ME = [("Dubai Guide", "dubai.html"), ("Jeddah Guide", D), ("Saudi Arabia Guide", D)]
GUIDES_OCEANIA = [
    ("Brisbane Guide", D),
    ("Melbourne Guide", D),
    ("Sydney Guide", D),
]

# Holiday homes (Agoda-style)
HOMES_APT = [
    ("Bangkok Apartments", "bangkok.html"),
    ("Kuala Lumpur Apartments", "kuala-lumpur.html"),
    ("Manila Apartments", D),
    ("Osaka Apartments", D),
    ("Pattaya Apartments", "pattaya.html"),
    ("Tokyo Apartments", D),
]
HOMES_BUNG = [
    ("Bali Bungalows", "bali.html"),
    ("Koh Kood Bungalows", D),
    ("Koh Lanta Bungalows", D),
    ("Koh Phangan Bungalows", D),
    ("Koh Samet Bungalows", D),
    ("Phu Quoc Island Bungalows", "phu-quoc-island.html"),
]
HOMES_VILLA = [
    ("Bali Villas", "bali.html"),
    ("Phuket Villas", "phuket.html"),
    ("Pattaya Villas", "pattaya.html"),
    ("Hua Hin / Cha-am Villas", D),
    ("Seoul Villas", D),
    ("Port Dickson Villas", D),
]
HOMES_VR = [
    ("Tokyo Vacation Rentals", D),
    ("Bangkok Vacation Rentals", "bangkok.html"),
]


LINK_CLASS = "text-[11px] text-slate-400 underline-offset-2 hover:text-sky-300 hover:underline"


def link_items_tw(items):
    lines = []
    for label, href in items:
        lines.append(f'                <li class="min-w-0"><a class="{LINK_CLASS}" href="{href}">{label}</a></li>')
    return "\n".join(lines)


def region_block_tw(title, items, grid_ul_class):
    """Region label + links (flat, no inner card chrome)."""
    return f"""                <div class="min-w-0">
                  <p class="mb-2 text-[10px] font-semibold uppercase tracking-wide text-slate-500">{title}</p>
                  <ul class="{grid_ul_class}">
{link_items_tw(items)}
                  </ul>
                </div>"""


# Dense grid for long lists; tighter for short columns
GRID_LONG = "grid grid-cols-2 gap-x-2 gap-y-1 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 xl:grid-cols-6"
GRID_MED = "grid grid-cols-1 gap-1 sm:grid-cols-2"
GRID_SHORT = "grid grid-cols-1 gap-1"


def build_tailwind():
    parts = []
    parts.append("""      <div id="footer-sitemap-root" class="footer-sitemap mt-6 rounded-xl border border-slate-800/50 bg-slate-900/25 px-5 py-6 sm:px-6 sm:py-7">
        <p class="mb-6 border-b border-slate-800/60 pb-3 text-xs text-slate-400">International hotels, country hubs, guides &amp; holiday homes</p>
        <div class="space-y-8">""")

    # Destination Cities
    parts.append("""          <section aria-labelledby="fs-cities">
            <h3 id="fs-cities" class="mb-3 text-sm font-semibold text-white">Destination Cities</h3>
            <div class="grid gap-6 lg:grid-cols-12 lg:gap-6">""")
    parts.append(f'              <div class="lg:col-span-8">\n{region_block_tw("Asia", ASIA_CITIES, GRID_LONG)}\n              </div>')
    parts.append(f'              <div class="grid gap-6 sm:grid-cols-2 lg:col-span-4 lg:grid-cols-1">\n{region_block_tw("Europe", EUROPE_CITIES, GRID_SHORT)}\n{region_block_tw("Middle East", ME_CITIES, GRID_SHORT)}\n              </div>')
    parts.append("""            </div>
          </section>""")

    # Countries
    parts.append("""          <section aria-labelledby="fs-countries" class="border-t border-slate-800/50 pt-8">
            <h3 id="fs-countries" class="mb-3 text-sm font-semibold text-white">Countries &amp; Territories</h3>
            <div class="grid gap-6 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-6">""")
    parts.append(region_block_tw("Africa", AFRICA_C, GRID_MED))
    parts.append(region_block_tw("Americas", AMERICAS_C, GRID_MED))
    parts.append(region_block_tw("Asia", ASIA_COUNTRIES, GRID_MED))
    parts.append(region_block_tw("Europe", EUROPE_COUNTRIES, GRID_MED))
    parts.append(region_block_tw("Middle East", ME_COUNTRIES, GRID_MED))
    parts.append(region_block_tw("Oceania", OCEANIA_C, GRID_SHORT))
    parts.append("""            </div>
          </section>""")

    # Guides
    parts.append("""          <section aria-labelledby="fs-guides" class="border-t border-slate-800/50 pt-8">
            <h3 id="fs-guides" class="mb-3 text-sm font-semibold text-white">Destination Guides</h3>
            <div class="grid gap-6 sm:grid-cols-2 lg:grid-cols-4 xl:grid-cols-5">""")
    parts.append(region_block_tw("Start here", GUIDES_HOME, GRID_SHORT))
    parts.append(region_block_tw("Asia", GUIDES_ASIA, GRID_LONG))
    parts.append(region_block_tw("Europe", GUIDES_EUROPE, GRID_SHORT))
    parts.append(region_block_tw("Middle East", GUIDES_ME, GRID_MED))
    parts.append(region_block_tw("Oceania", GUIDES_OCEANIA, GRID_MED))
    parts.append("""            </div>
          </section>""")

    # Homes
    parts.append("""          <section aria-labelledby="fs-homes" class="border-t border-slate-800/50 pt-8">
            <h3 id="fs-homes" class="mb-1 text-sm font-semibold text-white">Holiday homes &amp; rentals</h3>
            <p class="mb-3 text-xs text-slate-500">Apartments, bungalows &amp; villas</p>
            <div class="grid gap-6 sm:grid-cols-2 lg:grid-cols-4">""")
    parts.append(region_block_tw("Asia apartments", HOMES_APT, GRID_MED))
    parts.append(region_block_tw("Asia bungalows", HOMES_BUNG, GRID_MED))
    parts.append(region_block_tw("Asia villas", HOMES_VILLA, GRID_MED))
    parts.append(region_block_tw("Vacation rentals", HOMES_VR, GRID_SHORT))
    parts.append("""            </div>
          </section>""")

    parts.append("""        </div>
      </div>""")
    return "\n".join(parts)


def build_bootstrap():
    """Bootstrap theme: flat sections, light dividers."""

    def region_card(title, items):
        lis = "\n".join(
            f'                            <li class="mb-1"><a href="{href}" class="link-light text-decoration-none small">{label}</a></li>'
            for label, href in items
        )
        return f"""                        <div class="col-12 col-sm-6 col-lg-4 col-xl-3 mb-3">
                            <div class="h-100">
                                <h3 class="text-secondary text-uppercase small mb-2 pb-1 border-bottom border-secondary border-opacity-25">{title}</h3>
                                <ul class="list-unstyled small mb-0" style="columns:2; column-gap:1rem;">
{lis}
                                </ul>
                            </div>
                        </div>"""

    rows = []
    rows.append("""        <div class="footer-sitemap-bootstrap border-top border-secondary border-opacity-25 mt-4">
            <div class="container py-4 py-lg-5">
                <p class="text-muted small border-bottom border-secondary border-opacity-25 pb-3 mb-4">International hotels, country hubs, guides &amp; holiday homes</p>
                <h2 class="h6 text-white mb-3">Destination Cities</h2>
                <div class="row g-3 mb-4 pb-4 border-bottom border-secondary border-opacity-25">""")
    rows.append(region_card("Asia", ASIA_CITIES))
    rows.append(region_card("Europe", EUROPE_CITIES))
    rows.append(region_card("Middle East", ME_CITIES))
    rows.append("""                </div>
                <h2 class="h6 text-white mb-3">Countries &amp; Territories</h2>
                <div class="row g-3 mb-4 pb-4 border-bottom border-secondary border-opacity-25">""")
    rows.append(region_card("Africa", AFRICA_C))
    rows.append(region_card("Americas", AMERICAS_C))
    rows.append(region_card("Asia", ASIA_COUNTRIES))
    rows.append(region_card("Europe", EUROPE_COUNTRIES))
    rows.append(region_card("Middle East", ME_COUNTRIES))
    rows.append(region_card("Oceania", OCEANIA_C))
    rows.append("""                </div>
                <h2 class="h6 text-white mb-3">Destination Guides</h2>
                <div class="row g-3 mb-4 pb-4 border-bottom border-secondary border-opacity-25">""")
    rows.append(region_card("Start here", GUIDES_HOME))
    rows.append(region_card("Asia", GUIDES_ASIA))
    rows.append(region_card("Europe", GUIDES_EUROPE))
    rows.append(region_card("Middle East", GUIDES_ME))
    rows.append(region_card("Oceania", GUIDES_OCEANIA))
    rows.append("""                </div>
                <h2 class="h6 text-white mb-2">Holiday homes &amp; rentals</h2>
                <p class="text-muted small mb-3">Apartments, bungalows &amp; villas</p>
                <div class="row g-3">""")
    rows.append(region_card("Asia apartments", HOMES_APT))
    rows.append(region_card("Asia bungalows", HOMES_BUNG))
    rows.append(region_card("Asia villas", HOMES_VILLA))
    rows.append(region_card("Vacation rentals", HOMES_VR))
    rows.append("""                </div>
            </div>
        </div>""")
    return "\n".join(rows)


def main():
    (ROOT / "partials").mkdir(exist_ok=True)
    (ROOT / "partials" / "footer-sitemap.html").write_text(build_tailwind() + "\n", encoding="utf-8")
    (ROOT / "partials" / "footer-sitemap-bootstrap.html").write_text(build_bootstrap() + "\n", encoding="utf-8")
    print("Wrote partials/footer-sitemap.html and partials/footer-sitemap-bootstrap.html")


if __name__ == "__main__":
    main()
