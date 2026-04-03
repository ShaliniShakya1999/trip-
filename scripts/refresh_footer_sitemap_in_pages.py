# -*- coding: utf-8 -*-
"""Replace embedded footer-sitemap block in *.html with partials/footer-sitemap.html."""
import re
from pathlib import Path
from typing import Tuple

ROOT = Path(__file__).resolve().parents[1]
PARTIAL = ROOT / "partials" / "footer-sitemap.html"
PARTIAL_BOOTSTRAP = ROOT / "partials" / "footer-sitemap-bootstrap.html"

# BoomDevs / theme templates (Bootstrap) — use Bootstrap-styled sitemap block.
BOOTSTRAP_THEME_PAGES = frozenset(
    {
        "about.html",
        "blog-details.html",
        "blog.html",
        "contact.html",
        "destination-details.html",
        "destination.html",
        "tour-details.html",
        "tour.html",
    }
)


def find_outer_div_end(html: str, open_start: int) -> int:
    """open_start = index of '<' of opening <div>. Return index after matching </div>."""
    i = open_start
    depth = 0
    n = len(html)
    while i < n:
        if html.startswith("<div", i) and (i + 4 >= n or html[i + 4] in " \t\n\r/>"):
            depth += 1
            i += 4
            continue
        if html.startswith("</div>", i):
            depth -= 1
            i += 6
            if depth == 0:
                return i
            continue
        i += 1
    return -1


def replace_block(html: str, new_block: str) -> Tuple[str, bool]:
    m = re.search(r"<div[^>]*\bfooter-sitemap\b[^>]*>", html)
    if not m:
        return html, False
    start = m.start()
    end = find_outer_div_end(html, start)
    if end < 0:
        return html, False
    return html[:start] + new_block.rstrip() + "\n" + html[end:], True


def main():
    tw = PARTIAL.read_text(encoding="utf-8").strip()
    bs = PARTIAL_BOOTSTRAP.read_text(encoding="utf-8").strip()
    n = 0
    for p in sorted(ROOT.glob("*.html")):
        raw = p.read_text(encoding="utf-8")
        if "footer-sitemap" not in raw:
            continue
        new_block = bs if p.name in BOOTSTRAP_THEME_PAGES else tw
        updated, ok = replace_block(raw, new_block)
        if ok and updated != raw:
            p.write_text(updated, encoding="utf-8")
            n += 1
            print("updated", p.name)
    print("Done,", n, "files.")


if __name__ == "__main__":
    main()
