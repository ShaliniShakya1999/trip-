# -*- coding: utf-8 -*-
"""Build deals.html, flights.html, activities.html from index header/footer."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDEX = ROOT / "index.html"

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <meta name="description" content="{desc}" />
  <meta name="robots" content="index,follow" />
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Plus+Jakarta+Sans:wght@500;600;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="css/irt-chrome.css" />
</head>
<body class="bg-slate-50 text-slate-800">
"""


def extract_chrome() -> tuple[str, str]:
    raw = INDEX.read_text(encoding="utf-8")
    h0 = raw.index('<header class="sticky')
    h1 = raw.index("</header>", h0) + len("</header>")
    f0 = raw.index('<footer class="mt-10">')
    f1 = raw.index("</footer>", f0) + len("</footer>")
    return raw[h0:h1], raw[f0:f1]


def page_wrap(inner: str) -> str:
    return "\n  " + inner.strip() + "\n"


DEALS_BODY = """
  <main>
    <section class="border-b border-slate-200 bg-gradient-to-br from-sky-900 via-slate-900 to-slate-950 px-4 py-14 text-white sm:px-6 lg:px-8">
      <div class="mx-auto max-w-4xl text-center">
        <p class="text-xs font-bold uppercase tracking-[0.2em] text-sky-200/90">Save more on every trip</p>
        <h1 class="mt-3 text-3xl font-extrabold tracking-tight sm:text-4xl">Deals &amp; offers</h1>
        <p class="mx-auto mt-4 max-w-2xl text-sm text-white/85 sm:text-base">Curated hotel promotions, flight &amp; activity bundles, and featured stays—hand-picked for Infinity Routes travellers.</p>
      </div>
    </section>
    <section class="mx-auto max-w-6xl px-4 py-12 sm:px-6 lg:px-8">
      <div class="grid gap-6 md:grid-cols-3">
        <a href="accommodation-promotions.html" class="group flex flex-col overflow-hidden rounded-2xl border border-slate-200 bg-white shadow-sm ring-1 ring-slate-100 transition hover:-translate-y-1 hover:shadow-lg">
          <div class="h-36 bg-gradient-to-br from-sky-500 to-indigo-600 p-6">
            <p class="text-xs font-bold uppercase tracking-wide text-white/90">Stays</p>
            <h2 class="mt-2 text-xl font-extrabold text-white">Hotel deals</h2>
          </div>
          <div class="flex flex-1 flex-col p-5">
            <p class="text-sm text-slate-600">Limited-time rates on rooms across India and abroad.</p>
            <span class="mt-4 text-sm font-semibold text-sky-600 group-hover:underline">View accommodation deals →</span>
          </div>
        </a>
        <a href="flights-activities-promotions.html" class="group flex flex-col overflow-hidden rounded-2xl border border-slate-200 bg-white shadow-sm ring-1 ring-slate-100 transition hover:-translate-y-1 hover:shadow-lg">
          <div class="h-36 bg-gradient-to-br from-amber-500 to-rose-600 p-6">
            <p class="text-xs font-bold uppercase tracking-wide text-white/90">Bundles</p>
            <h2 class="mt-2 text-xl font-extrabold text-white">Flights &amp; activities</h2>
          </div>
          <div class="flex flex-1 flex-col p-5">
            <p class="text-sm text-slate-600">Promos on flights, tours, and things to do in top cities.</p>
            <span class="mt-4 text-sm font-semibold text-sky-600 group-hover:underline">Explore promos →</span>
          </div>
        </a>
        <a href="properties.html" class="group flex flex-col overflow-hidden rounded-2xl border border-slate-200 bg-white shadow-sm ring-1 ring-slate-100 transition hover:-translate-y-1 hover:shadow-lg">
          <div class="h-36 bg-gradient-to-br from-emerald-500 to-teal-700 p-6">
            <p class="text-xs font-bold uppercase tracking-wide text-white/90">Homes</p>
            <h2 class="mt-2 text-xl font-extrabold text-white">Holiday homes</h2>
          </div>
          <div class="flex flex-1 flex-col p-5">
            <p class="text-sm text-slate-600">Apartments, villas &amp; unique stays for families and groups.</p>
            <span class="mt-4 text-sm font-semibold text-sky-600 group-hover:underline">Browse properties →</span>
          </div>
        </a>
      </div>
      <p class="mt-10 text-center text-sm text-slate-500">Tip: use the <a href="index.html#search-hero" class="font-semibold text-sky-700 hover:underline">homepage search</a> to compare hotels, flights, and packages in one place.</p>
    </section>
  </main>
"""

FLIGHTS_BODY = """
  <main>
    <section class="border-b border-slate-200 bg-gradient-to-br from-slate-900 via-sky-950 to-slate-900 px-4 py-14 text-white sm:px-6 lg:px-8">
      <div class="mx-auto max-w-3xl text-center">
        <p class="text-xs font-bold uppercase tracking-[0.2em] text-sky-200/90">Fly smarter</p>
        <h1 class="mt-3 text-3xl font-extrabold tracking-tight sm:text-4xl">Flights</h1>
        <p class="mx-auto mt-4 max-w-2xl text-sm text-white/85 sm:text-base">Search routes, compare fares, and plan multi-city trips. Start your search below.</p>
        <div class="mt-8 flex flex-wrap items-center justify-center gap-3">
          <a href="index.html?tab=flights#search-hero" class="inline-flex items-center justify-center rounded-xl bg-sky-500 px-6 py-3 text-sm font-bold text-white shadow-lg shadow-sky-900/40 transition hover:bg-sky-400">Open flight search</a>
          <a href="index.html?tab=packages#search-hero" class="inline-flex items-center justify-center rounded-xl border border-white/30 bg-white/10 px-6 py-3 text-sm font-semibold text-white backdrop-blur hover:bg-white/20">Flight + Hotel</a>
        </div>
      </div>
    </section>
    <section class="mx-auto max-w-6xl px-4 py-12 sm:px-6 lg:px-8">
      <h2 class="text-lg font-extrabold text-slate-900">Popular international routes</h2>
      <p class="mt-1 text-sm text-slate-600">Explore destination guides and hotel picks after you book.</p>
      <div class="mt-6 grid gap-3 sm:grid-cols-2 lg:grid-cols-4">
        <a href="dubai.html" class="rounded-xl border border-slate-200 bg-white px-4 py-3 text-sm font-semibold text-slate-800 shadow-sm hover:border-sky-300 hover:text-sky-800">Dubai</a>
        <a href="singapore.html" class="rounded-xl border border-slate-200 bg-white px-4 py-3 text-sm font-semibold text-slate-800 shadow-sm hover:border-sky-300 hover:text-sky-800">Singapore</a>
        <a href="bangkok.html" class="rounded-xl border border-slate-200 bg-white px-4 py-3 text-sm font-semibold text-slate-800 shadow-sm hover:border-sky-300 hover:text-sky-800">Bangkok</a>
        <a href="kuala-lumpur.html" class="rounded-xl border border-slate-200 bg-white px-4 py-3 text-sm font-semibold text-slate-800 shadow-sm hover:border-sky-300 hover:text-sky-800">Kuala Lumpur</a>
      </div>
      <p class="mt-10 text-sm text-slate-500">Need help? <a href="contact.html" class="font-semibold text-sky-700 hover:underline">Contact</a> our team.</p>
    </section>
  </main>
"""

ACTIVITIES_BODY = """
  <main>
    <section class="border-b border-slate-200 bg-gradient-to-br from-emerald-900 via-slate-900 to-slate-950 px-4 py-14 text-white sm:px-6 lg:px-8">
      <div class="mx-auto max-w-3xl text-center">
        <p class="text-xs font-bold uppercase tracking-[0.2em] text-emerald-200/90">Things to do</p>
        <h1 class="mt-3 text-3xl font-extrabold tracking-tight sm:text-4xl">Activities &amp; experiences</h1>
        <p class="mx-auto mt-4 max-w-2xl text-sm text-white/85 sm:text-base">Tours, attractions, day trips, and local experiences—bookable alongside your stay.</p>
        <div class="mt-8 flex flex-wrap items-center justify-center gap-3">
          <a href="index.html?tab=activities#search-hero" class="inline-flex items-center justify-center rounded-xl bg-emerald-500 px-6 py-3 text-sm font-bold text-white shadow-lg shadow-emerald-900/40 transition hover:bg-emerald-400">Search activities</a>
          <a href="tour.html" class="inline-flex items-center justify-center rounded-xl border border-white/30 bg-white/10 px-6 py-3 text-sm font-semibold text-white backdrop-blur hover:bg-white/20">Browse tours</a>
        </div>
      </div>
    </section>
    <section class="mx-auto max-w-6xl px-4 py-12 sm:px-6 lg:px-8">
      <h2 class="text-lg font-extrabold text-slate-900">Ideas to start</h2>
      <div class="mt-6 grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
        <a href="destination.html" class="rounded-2xl border border-slate-200 bg-white p-5 shadow-sm transition hover:border-sky-200 hover:shadow-md">
          <h3 class="font-bold text-slate-900">Destinations</h3>
          <p class="mt-2 text-sm text-slate-600">City guides and hotel picks worldwide.</p>
        </a>
        <a href="flights-activities-promotions.html" class="rounded-2xl border border-slate-200 bg-white p-5 shadow-sm transition hover:border-sky-200 hover:shadow-md">
          <h3 class="font-bold text-slate-900">Activity promos</h3>
          <p class="mt-2 text-sm text-slate-600">Discounted bundles and seasonal offers.</p>
        </a>
        <a href="blog.html" class="rounded-2xl border border-slate-200 bg-white p-5 shadow-sm transition hover:border-sky-200 hover:shadow-md">
          <h3 class="font-bold text-slate-900">Travel blog</h3>
          <p class="mt-2 text-sm text-slate-600">Inspiration and itineraries from our editors.</p>
        </a>
      </div>
    </section>
  </main>
"""

PAGES = [
    ("deals.html", "Deals & offers | Infinity Routes Travels", "Hotel deals, flight bundles, and holiday homes—Infinity Routes promotions.", DEALS_BODY),
    ("flights.html", "Flights | Infinity Routes Travels", "Search flights, compare routes, and plan trips with Infinity Routes.", FLIGHTS_BODY),
    ("activities.html", "Activities & experiences | Infinity Routes Travels", "Tours, attractions, and things to do with Infinity Routes.", ACTIVITIES_BODY),
]


def main():
    header, footer = extract_chrome()
    for fname, title, desc, body in PAGES:
        html = (
            HEAD.format(title=title, desc=desc)
            + "\n  "
            + header.strip()
            + "\n"
            + body
            + "\n  "
            + footer.strip()
            + "\n</body>\n</html>\n"
        )
        (ROOT / fname).write_text(html, encoding="utf-8")
        print("Wrote", fname)


if __name__ == "__main__":
    main()
