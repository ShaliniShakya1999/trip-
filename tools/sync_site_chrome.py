# -*- coding: utf-8 -*-
"""Unify header + footer across all site HTML (same as index.html)."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDEX = ROOT / "index.html"
SKIP = {"index.html"}


def extract_chrome() -> tuple[str, str]:
    raw = INDEX.read_text(encoding="utf-8")
    h0 = raw.index('<header class="sticky')
    h1 = raw.index("</header>", h0) + len("</header>")
    header = raw[h0:h1]
    f0 = raw.index('<footer class="mt-10">')
    f1 = raw.index("</footer>", f0) + len("</footer>")
    footer = raw[f0:f1]
    return header, footer


HEAD_INJECT = """    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="css/irt-chrome.css" />
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Plus+Jakarta+Sans:wght@500;600;700&display=swap" rel="stylesheet" />
"""


def process_file(path: Path, header: str, footer: str) -> bool:
    name = path.name
    if name in SKIP:
        return False
    t = path.read_text(encoding="utf-8")
    orig = t

    is_theme = 'class="header-area"' in t or (
        "header-area" in t and "main-menu" in t and "cdn.tailwindcss.com" not in t
    )
    is_tailwind_only = ("cdn.tailwindcss.com" in t or "/tailwind" in t) and not is_theme

    if is_theme:
        if "cdn.tailwindcss.com" not in t and "irt-chrome.css" not in t:
            t = t.replace("</head>", HEAD_INJECT + "</head>", 1)
        t = re.sub(
            r"(?s)<!-- Preloader Start !-->.*?<div class=\"body-overlay\"></div>\s*",
            header + "\n",
            t,
            count=1,
        )
        t = re.sub(
            r"(?s)<!--- Start Footer !-->.*?<!--- End Footer !-->",
            footer,
            t,
            count=1,
        )
        if "irt-site" not in t:
            t = re.sub(
                r"<body>",
                '<body class="bg-slate-50 text-slate-800 irt-site">',
                t,
                count=1,
            )
    elif is_tailwind_only:
        t = re.sub(r"<header\b[^>]*>.*?</header>", header, t, count=1, flags=re.DOTALL)
        # Replace only the last site chrome footer (avoids matching <footer> inside blockquotes)
        marker = '<footer class="mt-10">'
        pos = t.rfind(marker)
        if pos != -1:
            end = t.find("</footer>", pos)
            if end != -1:
                end += len("</footer>")
                t = t[:pos] + footer + t[end:]
        if "irt-chrome.css" not in t and "footer-directory" in footer:
            t = t.replace(
                "</head>",
                '    <link rel="stylesheet" href="css/irt-chrome.css" />\n</head>',
                1,
            )
    else:
        return False

    if (
        "irt-mobile-menu-btn" in t
        and "js/irt-nav.js" not in t
        and "</body>" in t
    ):
        t = t.replace(
            "</body>",
            '  <script src="js/irt-nav.js" defer></script>\n</body>',
            1,
        )

    if t != orig:
        path.write_text(t, encoding="utf-8")
        return True
    return False


def main():
    header, footer = extract_chrome()
    done = []
    for path in sorted(ROOT.glob("*.html")):
        if path.name.startswith("_"):
            continue
        try:
            if process_file(path, header, footer):
                done.append(path.name)
        except (ValueError, re.error) as e:
            print("FAIL", path.name, e)
    print("Updated:", len(done), "files")
    for n in done:
        print(" ", n)


if __name__ == "__main__":
    main()
