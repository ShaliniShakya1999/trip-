# -*- coding: utf-8 -*-
"""Generate about.html from index header/footer."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDEX = ROOT / "index.html"

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>About us | Infinity Routes Travels</title>
  <meta name="description" content="Infinity Routes Travels — who we are, what we do, and how we help you book hotels, tours, and travel experiences." />
  <meta name="robots" content="index,follow" />
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Plus+Jakarta+Sans:wght@500;600;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="css/irt-chrome.css" />
</head>
<body class="bg-slate-50 text-slate-800">
"""

MAIN = """
  <main>
    <section class="border-b border-slate-200 bg-gradient-to-br from-sky-950 via-slate-900 to-slate-950 px-4 py-14 text-white sm:px-6 lg:px-8">
      <div class="mx-auto max-w-3xl text-center">
        <p class="text-xs font-bold uppercase tracking-[0.2em] text-sky-200/90">Our story</p>
        <h1 class="mt-3 text-3xl font-extrabold tracking-tight sm:text-4xl">About Infinity Routes</h1>
        <p class="mx-auto mt-4 max-w-2xl text-sm text-white/85 sm:text-base">We help travellers discover places, compare stays, and plan trips—with clear information and a modern booking experience.</p>
      </div>
    </section>
    <section class="mx-auto max-w-3xl px-4 py-12 sm:px-6 lg:px-8">
      <div class="prose prose-slate max-w-none text-slate-700">
        <h2 class="text-xl font-bold text-slate-900">Who we are</h2>
        <p class="mt-3 text-sm leading-relaxed sm:text-base"><strong>Infinity Routes Travels</strong> is a travel platform focused on hotels, holiday homes, tours, and inspiration for trips across India and worldwide. We bring together destination guides, curated offers, and search tools so you can plan with confidence.</p>
        <h2 class="mt-10 text-xl font-bold text-slate-900">What we offer</h2>
        <ul class="mt-3 list-disc space-y-2 pl-5 text-sm leading-relaxed sm:text-base">
          <li>City and international destination pages with hand-picked stays and things to do</li>
          <li>Deals and promotions on accommodations, flights &amp; activities bundles, and featured properties</li>
          <li>Travel blog and guides to help you choose where to go next</li>
        </ul>
        <h2 class="mt-10 text-xl font-bold text-slate-900">How we work</h2>
        <p class="mt-3 text-sm leading-relaxed sm:text-base">Our website is designed to be fast and easy to use on mobile and desktop. Search widgets help you explore options; many listings link to partner offers where you can complete bookings. We continue to expand routes, cities, and content based on what travellers ask for.</p>
        <h2 class="mt-10 text-xl font-bold text-slate-900">Get in touch</h2>
        <p class="mt-3 text-sm leading-relaxed sm:text-base">Questions, partnerships, or media enquiries? Visit our <a href="contact.html" class="font-semibold text-sky-700 hover:underline">Contact</a> page—we are happy to hear from you.</p>
      </div>
    </section>
    <section class="border-t border-slate-200 bg-white py-10">
      <div class="mx-auto flex max-w-3xl flex-wrap justify-center gap-4 px-4 sm:px-6">
        <a href="destination.html" class="inline-flex rounded-xl border border-slate-200 bg-slate-50 px-5 py-2.5 text-sm font-semibold text-slate-800 hover:border-sky-300 hover:bg-sky-50">Explore destinations</a>
        <a href="deals.html" class="inline-flex rounded-xl border border-slate-200 bg-slate-50 px-5 py-2.5 text-sm font-semibold text-slate-800 hover:border-sky-300 hover:bg-sky-50">View deals</a>
        <a href="contact.html" class="inline-flex rounded-xl bg-sky-600 px-5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-sky-500">Contact us</a>
      </div>
    </section>
  </main>
"""


def extract_chrome() -> tuple[str, str]:
    raw = INDEX.read_text(encoding="utf-8")
    h0 = raw.index('<header class="sticky')
    h1 = raw.index("</header>", h0) + len("</header>")
    f0 = raw.index('<footer class="mt-10">')
    f1 = raw.index("</footer>", f0) + len("</footer>")
    return raw[h0:h1], raw[f0:f1]


def main():
    header, footer = extract_chrome()
    html = (
        HEAD
        + "\n  "
        + header.strip()
        + "\n"
        + MAIN
        + "\n  "
        + footer.strip()
        + "\n</body>\n</html>\n"
    )
    (ROOT / "about.html").write_text(html, encoding="utf-8")
    print("Wrote about.html")


if __name__ == "__main__":
    main()
