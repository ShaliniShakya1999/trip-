# -*- coding: utf-8 -*-
"""Insert partials/footer-sitemap.html before copyright in Tailwind footers."""
from pathlib import Path
from typing import Optional

ROOT = Path(__file__).resolve().parents[1]
MARKER = '<div class="mt-8 border-t border-slate-800 pt-4 text-xs text-slate-500">© 2005–2026 Infinity Routes Travels. All rights reserved.</div>'

SITEMAP = (ROOT / "partials" / "footer-sitemap.html").read_text(encoding="utf-8")
SITEMAP_BS = (ROOT / "partials" / "footer-sitemap-bootstrap.html").read_text(encoding="utf-8")

# Bootstrap theme pages: insert before footer-bottom-area
BS_ANCHOR = '<div class="footer-bottom-area">'


def insert_tailwind(html: str) -> Optional[str]:
    if "footer-sitemap" in html or "mt-10 bg-slate-950" not in html:
        return None
    idx = html.find(MARKER)
    if idx == -1:
        return None
    prefix = html[:idx].rstrip()
    suffix = html[idx + len(MARKER) :]
    return prefix + "\n" + SITEMAP + "\n      " + MARKER + suffix


def insert_bootstrap(html: str) -> Optional[str]:
    if "footer-sitemap-bootstrap" in html:
        return None
    if BS_ANCHOR not in html or 'class="footer bg-light-black"' not in html:
        return None
    idx = html.find(BS_ANCHOR)
    return html[:idx] + SITEMAP_BS + "\n        " + html[idx:]


def main():
    n_tw = n_bs = 0
    for p in sorted(ROOT.glob("*.html")):
        raw = p.read_text(encoding="utf-8")
        new = insert_tailwind(raw)
        if new is not None:
            p.write_text(new, encoding="utf-8")
            n_tw += 1
            print("tailwind", p.name)
            continue
        new = insert_bootstrap(raw)
        if new is not None:
            p.write_text(new, encoding="utf-8")
            n_bs += 1
            print("bootstrap", p.name)
    print(f"Done: {n_tw} tailwind, {n_bs} bootstrap pages updated.")


if __name__ == "__main__":
    main()
