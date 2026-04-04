# -*- coding: utf-8 -*-
"""Write sitemap.xml for every *.html in the site root (edit SITE_BASE for production)."""
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
# Production origin — change if your live domain differs.
SITE_BASE = "https://infinityroutes.in"


def main() -> None:
    base = SITE_BASE.rstrip("/")
    urls: list[tuple[str, str]] = []
    for p in sorted(ROOT.glob("*.html")):
        lm = datetime.fromtimestamp(p.stat().st_mtime, tz=timezone.utc).strftime("%Y-%m-%d")
        urls.append((p.name, lm))

    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for name, lastmod in urls:
        pri = "1.0" if name == "index.html" else "0.7"
        lines.extend(
            [
                "  <url>",
                f"    <loc>{base}/{name}</loc>",
                f"    <lastmod>{lastmod}</lastmod>",
                "    <changefreq>weekly</changefreq>",
                f"    <priority>{pri}</priority>",
                "  </url>",
            ]
        )
    lines.append("</urlset>")
    out = ROOT / "sitemap.xml"
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("Wrote", out.name, f"({len(urls)} URLs)")


if __name__ == "__main__":
    main()
