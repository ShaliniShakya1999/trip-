# -*- coding: utf-8 -*-
"""Remove wrongly duplicated site footer from blockquote in blog-details.html."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
path = ROOT / "blog-details.html"
t = path.read_text(encoding="utf-8")
marker = '<footer class="mt-10">'
first = t.find(marker)
if first == -1:
    raise SystemExit("No footer found")
second = t.find(marker, first + 1)
if second == -1:
    print("Single footer only; nothing to fix")
    raise SystemExit(0)
end = t.find("</footer>", first)
if end == -1:
    raise SystemExit("Unclosed first footer")
end += len("</footer>")
small = '<footer class="blockquote-footer text-slate-600">— Infinity Routes Editorial</footer>'
path.write_text(t[:first] + small + t[end:], encoding="utf-8")
print("Fixed embedded site footer inside blockquote.")
