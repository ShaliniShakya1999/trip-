# -*- coding: utf-8 -*-
"""Apply Infinity Routes branding + unified nav to RouteHaven HTML pages."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent

HEAD_META = (
    '    <meta name="description" content="Infinity Routes Travels — hotels, tours, destinations, and travel inspiration across India and worldwide."/>\n'
    '    <meta name="keywords" content="Infinity Routes, travel booking, hotels, tours, flights, India travel, international destinations"/>\n'
    '    <meta name="author" content="Infinity Routes Travels" />'
)

IRT_CSS = '    <link rel="stylesheet" href="css/irt-unified.css" />\n'

SIDEBAR_CONTACT = """                        <div class="header-contact-info">
                            <span><i class="fa-solid fa-location-dot"></i>Mumbai &amp; New Delhi, India</span>
                            <span><a href="mailto:support@infinityroutes.in"><i class="fa-solid fa-envelope"></i>support@infinityroutes.in</a></span>
                            <span><a href="tel:+911140000000"><i class="fa-solid fa-phone"></i>+91 11 4000 0000</a></span>
                        </div>"""

COPYRIGHT = """                            <div class="copyright-text">
                                <p>© 2005–2026 Infinity Routes Travels. All rights reserved.</p>
                            </div>"""

# (filename, page_key for nav)
PAGES = [
    ("about.html", "about"),
    ("tour.html", "tour"),
    ("tour-details.html", "tour"),
    ("destination.html", "destination"),
    ("destination-details.html", "destination"),
    ("blog.html", "blog"),
    ("blog-details.html", "blog"),
    ("contact.html", "contact"),
]


def build_nav(active: str) -> str:
    def li_home():
        return '                                    <li><a href="index.html">Home</a></li>\n'

    def li_about():
        ac = ' class="active"' if active == "about" else ""
        return f'                                    <li{ac}><a href="about.html">About</a></li>\n'

    def li_tour():
        ac = 'dropdown active' if active == "tour" else "dropdown"
        return (
            f'                                    <li class="{ac}">\n'
            '                                        <a href="tour.html">Tours</a>\n'
            '                                        <ul class="submenu">\n'
            '                                            <li><a href="tour.html">All tours</a></li>\n'
            '                                            <li><a href="tour-details.html">Tour details</a></li>\n'
            "                                        </ul>\n"
            "                                    </li>\n"
        )

    def li_dest():
        ac = "dropdown active" if active == "destination" else "dropdown"
        return (
            f'                                    <li class="{ac}">\n'
            '                                        <a href="destination.html">Destinations</a>\n'
            '                                        <ul class="submenu">\n'
            '                                            <li><a href="destination.html">Explore</a></li>\n'
            '                                            <li><a href="destination-details.html">Destination details</a></li>\n'
            "                                        </ul>\n"
            "                                    </li>\n"
        )

    def li_blog():
        ac = "dropdown active" if active == "blog" else "dropdown"
        return (
            f'                                    <li class="{ac}">\n'
            '                                        <a href="blog.html">Blog</a>\n'
            '                                        <ul class="submenu">\n'
            '                                            <li><a href="blog.html">Articles</a></li>\n'
            '                                            <li><a href="blog-details.html">Article</a></li>\n'
            "                                        </ul>\n"
            "                                    </li>\n"
        )

    def li_contact():
        ac = ' class="active"' if active == "contact" else ""
        return f'                                    <li{ac}><a href="contact.html">Contact</a></li>\n'

    return (
        "                                <ul>\n"
        + li_home()
        + li_about()
        + li_tour()
        + li_dest()
        + li_blog()
        + li_contact()
        + "                                </ul>\n"
    )


TITLE_SUFFIX = {
    "about": "About",
    "tour": "Tours",
    "destination": "Destinations",
    "blog": "Blog",
    "contact": "Contact",
}


def patch_file(path: Path, page_key: str) -> None:
    text = path.read_text(encoding="utf-8")
    orig = text

    # Title + meta
    text = re.sub(
        r"<title>.*?</title>",
        f"<title>Infinity Routes Travels | {TITLE_SUFFIX.get(page_key, 'Travel')}</title>",
        text,
        count=1,
    )
    text = re.sub(
        r'<meta name="description" content="[^"]*"/>',
        HEAD_META.split("\n")[0].strip(),
        text,
        count=1,
    )
    text = re.sub(
        r'<meta name="keywords"\s*\n\s*content="[^"]*"/>',
        HEAD_META.split("\n")[1].strip(),
        text,
        count=1,
    )
    text = re.sub(
        r'<meta name="author" content="[^"]*"/>',
        HEAD_META.split("\n")[2].strip(),
        text,
        count=1,
    )

    # irt-unified.css after style.css
    if "irt-unified.css" not in text:
        text = text.replace(
            '<link rel="stylesheet" href="css/style.css" />',
            '<link rel="stylesheet" href="css/style.css" />\n' + IRT_CSS.strip(),
        )
        # handle variant without space before />
        text = text.replace(
            '<link rel="stylesheet" href="css/style.css"/>',
            '<link rel="stylesheet" href="css/style.css"/>\n' + IRT_CSS.strip(),
        )

    # Nav UL
    nav_new = build_nav(page_key)
    text = re.sub(
        r"<nav id=\"main-menu\" class=\"main-menu\">\s*<ul>.*?</ul>\s*</nav>",
        "<nav id=\"main-menu\" class=\"main-menu\">\n" + nav_new + "                            </nav>",
        text,
        count=1,
        flags=re.DOTALL,
    )

    # Logo alt
    text = text.replace('alt="logo"', 'alt="Infinity Routes Travels"')

    # Sidebar contact
    text = re.sub(
        r'<div class="header-contact-info">.*?</div>',
        SIDEBAR_CONTACT,
        text,
        count=1,
        flags=re.DOTALL,
    )

    # Footer copyright (theme bottom)
    text = re.sub(
        r'<div class="copyright-text">\s*<p>.*?</p>\s*</div>',
        COPYRIGHT,
        text,
        count=1,
        flags=re.DOTALL,
    )

    # Footer bottom links → real contact
    text = text.replace(
        '<li><a href="#">Contact</a></li>',
        '<li><a href="contact.html">Contact</a></li>',
    )

    if text != orig:
        path.write_text(text, encoding="utf-8")
        print("OK", path.name)
    else:
        print("SKIP (no change)", path.name)


def main():
    for name, key in PAGES:
        p = ROOT / name
        if not p.exists():
            print("MISSING", name)
            continue
        patch_file(p, key)


if __name__ == "__main__":
    main()
