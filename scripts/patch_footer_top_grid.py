# -*- coding: utf-8 -*-
"""Replace old 5-column footer top (Help…International) with slim 4-column from tools/intl-footer.html."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INTL_FOOTER = ROOT / "tools" / "intl-footer.html"


def find_div_zero_end(html: str, open_pos: int) -> int:
    i = open_pos
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


def main():
    raw_ft = INTL_FOOTER.read_text(encoding="utf-8")
    if "@@FOOTER_SITEMAP@@" not in raw_ft:
        raise SystemExit("intl-footer.html missing @@FOOTER_SITEMAP@@")
    start = raw_ft.index('<div class="mb-6 rounded-xl')
    end = raw_ft.index("@@FOOTER_SITEMAP@@")
    new_grid = raw_ft[start:end].strip()

    n = 0
    for p in sorted(ROOT.glob("*.html")):
        text = p.read_text(encoding="utf-8")
        if "footer-sitemap" not in text and "footer-links" not in text:
            continue
        # already new
        if 'class="mb-6 rounded-xl border border-slate-800/60 bg-slate-900/35' in text and "International</h4>" not in text:
            continue

        old_open = text.find('<div class="mb-8 rounded-2xl bg-slate-900/60 p-6">')
        if old_open == -1:
            continue
        old_end = find_div_zero_end(text, old_open)
        if old_end < 0:
            continue
        text2 = text[:old_open] + new_grid + "\n" + text[old_end:]
        if text2 != text:
            p.write_text(text2, encoding="utf-8")
            n += 1
            print("patched", p.name)
    print("Done,", n, "files.")


if __name__ == "__main__":
    main()
