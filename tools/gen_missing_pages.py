# -*- coding: utf-8 -*-
"""Create HTML pages referenced by nav/footer but missing from the repo."""
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


def write_page(path: Path, title: str, desc: str, main: str, header: str, footer: str) -> None:
    html = (
        HEAD.format(title=title, desc=desc)
        + "\n  "
        + header.strip()
        + "\n"
        + main
        + "\n  "
        + footer.strip()
        + "\n</body>\n</html>\n"
    )
    path.write_text(html, encoding="utf-8")
    print("Wrote", path.name)


DESTINATION_MAIN = """
  <main>
    <section class="border-b border-slate-200 bg-gradient-to-br from-indigo-950 via-slate-900 to-sky-950 px-4 py-14 text-white sm:px-6 lg:px-8">
      <div class="mx-auto max-w-4xl text-center">
        <p class="text-xs font-bold uppercase tracking-[0.2em] text-sky-200/90">Explore</p>
        <h1 class="mt-3 text-3xl font-extrabold tracking-tight sm:text-4xl">Destinations</h1>
        <p class="mx-auto mt-4 max-w-2xl text-sm text-white/85 sm:text-base">Browse city guides and hotel picks across India and worldwide. Jump into a place to see stays, things to do, and travel tips.</p>
      </div>
    </section>
    <section class="mx-auto max-w-6xl px-4 py-12 sm:px-6 lg:px-8">
      <h2 class="text-lg font-extrabold text-slate-900">India — top cities</h2>
      <div class="mt-4 grid gap-2 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4">
        <a href="bangalore.html" class="rounded-xl border border-slate-200 bg-white px-4 py-3 text-sm font-semibold text-slate-800 shadow-sm hover:border-sky-300">Bangalore</a>
        <a href="mumbai.html" class="rounded-xl border border-slate-200 bg-white px-4 py-3 text-sm font-semibold text-slate-800 shadow-sm hover:border-sky-300">Mumbai</a>
        <a href="new-delhi.html" class="rounded-xl border border-slate-200 bg-white px-4 py-3 text-sm font-semibold text-slate-800 shadow-sm hover:border-sky-300">New Delhi</a>
        <a href="goa.html" class="rounded-xl border border-slate-200 bg-white px-4 py-3 text-sm font-semibold text-slate-800 shadow-sm hover:border-sky-300">Goa</a>
        <a href="hyderabad.html" class="rounded-xl border border-slate-200 bg-white px-4 py-3 text-sm font-semibold text-slate-800 shadow-sm hover:border-sky-300">Hyderabad</a>
        <a href="chennai.html" class="rounded-xl border border-slate-200 bg-white px-4 py-3 text-sm font-semibold text-slate-800 shadow-sm hover:border-sky-300">Chennai</a>
        <a href="jaipur.html" class="rounded-xl border border-slate-200 bg-white px-4 py-3 text-sm font-semibold text-slate-800 shadow-sm hover:border-sky-300">Jaipur</a>
        <a href="kolkata.html" class="rounded-xl border border-slate-200 bg-white px-4 py-3 text-sm font-semibold text-slate-800 shadow-sm hover:border-sky-300">Kolkata</a>
        <a href="kochi.html" class="rounded-xl border border-slate-200 bg-white px-4 py-3 text-sm font-semibold text-slate-800 shadow-sm hover:border-sky-300">Kochi</a>
        <a href="pune.html" class="rounded-xl border border-slate-200 bg-white px-4 py-3 text-sm font-semibold text-slate-800 shadow-sm hover:border-sky-300">Pune</a>
        <a href="varanasi.html" class="rounded-xl border border-slate-200 bg-white px-4 py-3 text-sm font-semibold text-slate-800 shadow-sm hover:border-sky-300">Varanasi</a>
        <a href="pondicherry.html" class="rounded-xl border border-slate-200 bg-white px-4 py-3 text-sm font-semibold text-slate-800 shadow-sm hover:border-sky-300">Pondicherry</a>
      </div>
      <h2 class="mt-12 text-lg font-extrabold text-slate-900">International hubs</h2>
      <div class="mt-4 grid gap-2 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4">
        <a href="dubai.html" class="rounded-xl border border-slate-200 bg-white px-4 py-3 text-sm font-semibold text-slate-800 shadow-sm hover:border-sky-300">Dubai</a>
        <a href="bangkok.html" class="rounded-xl border border-slate-200 bg-white px-4 py-3 text-sm font-semibold text-slate-800 shadow-sm hover:border-sky-300">Bangkok</a>
        <a href="singapore.html" class="rounded-xl border border-slate-200 bg-white px-4 py-3 text-sm font-semibold text-slate-800 shadow-sm hover:border-sky-300">Singapore</a>
        <a href="bali.html" class="rounded-xl border border-slate-200 bg-white px-4 py-3 text-sm font-semibold text-slate-800 shadow-sm hover:border-sky-300">Bali</a>
        <a href="phuket.html" class="rounded-xl border border-slate-200 bg-white px-4 py-3 text-sm font-semibold text-slate-800 shadow-sm hover:border-sky-300">Phuket</a>
        <a href="kuala-lumpur.html" class="rounded-xl border border-slate-200 bg-white px-4 py-3 text-sm font-semibold text-slate-800 shadow-sm hover:border-sky-300">Kuala Lumpur</a>
        <a href="abu-dhabi.html" class="rounded-xl border border-slate-200 bg-white px-4 py-3 text-sm font-semibold text-slate-800 shadow-sm hover:border-sky-300">Abu Dhabi</a>
        <a href="hanoi.html" class="rounded-xl border border-slate-200 bg-white px-4 py-3 text-sm font-semibold text-slate-800 shadow-sm hover:border-sky-300">Hanoi</a>
      </div>
      <p class="mt-10 text-center text-sm text-slate-600">Sample detail layout: <a href="destination-details.html" class="font-semibold text-sky-700 hover:underline">destination details</a> · <a href="deals.html" class="font-semibold text-sky-700 hover:underline">Deals</a></p>
    </section>
  </main>
"""

TOUR_MAIN = """
  <main>
    <section class="border-b border-slate-200 bg-gradient-to-br from-amber-900 via-slate-900 to-orange-950 px-4 py-14 text-white sm:px-6 lg:px-8">
      <div class="mx-auto max-w-3xl text-center">
        <p class="text-xs font-bold uppercase tracking-[0.2em] text-amber-200/90">Packages</p>
        <h1 class="mt-3 text-3xl font-extrabold tracking-tight sm:text-4xl">Tours</h1>
        <p class="mx-auto mt-4 max-w-2xl text-sm text-white/85 sm:text-base">Guided itineraries with hotels and experiences—pick a package to see day-by-day plans and what is included.</p>
      </div>
    </section>
    <section class="mx-auto max-w-6xl px-4 py-12 sm:px-6 lg:px-8">
      <div class="grid gap-6 md:grid-cols-3">
        <a href="tour-details.html" class="group overflow-hidden rounded-2xl border border-slate-200 bg-white shadow-sm ring-1 ring-slate-100 transition hover:-translate-y-1 hover:shadow-lg">
          <div class="h-40 bg-gradient-to-br from-rose-500 to-orange-600 p-5">
            <p class="text-xs font-bold text-white/90">7 days · India</p>
            <h2 class="mt-2 text-lg font-extrabold text-white">Heritage Golden Triangle</h2>
          </div>
          <div class="p-4">
            <p class="text-sm text-slate-600">Delhi, Agra &amp; Jaipur with private transfers and boutique stays.</p>
            <span class="mt-3 inline-block text-sm font-semibold text-sky-600 group-hover:underline">View itinerary →</span>
          </div>
        </a>
        <a href="tour-details.html" class="group overflow-hidden rounded-2xl border border-slate-200 bg-white shadow-sm ring-1 ring-slate-100 transition hover:-translate-y-1 hover:shadow-lg">
          <div class="h-40 bg-gradient-to-br from-emerald-500 to-teal-700 p-5">
            <p class="text-xs font-bold text-white/90">5 days · India</p>
            <h2 class="mt-2 text-lg font-extrabold text-white">Kerala Backwaters</h2>
          </div>
          <div class="p-4">
            <p class="text-sm text-slate-600">Houseboat night, Cochin heritage walk, and hill-country tea estates.</p>
            <span class="mt-3 inline-block text-sm font-semibold text-sky-600 group-hover:underline">View itinerary →</span>
          </div>
        </a>
        <a href="tour-details.html" class="group overflow-hidden rounded-2xl border border-slate-200 bg-white shadow-sm ring-1 ring-slate-100 transition hover:-translate-y-1 hover:shadow-lg">
          <div class="h-40 bg-gradient-to-br from-sky-500 to-indigo-700 p-5">
            <p class="text-xs font-bold text-white/90">4 days · UAE</p>
            <h2 class="mt-2 text-lg font-extrabold text-white">Dubai long weekend</h2>
          </div>
          <div class="p-4">
            <p class="text-sm text-slate-600">City icons, desert safari, and marina dining experiences.</p>
            <span class="mt-3 inline-block text-sm font-semibold text-sky-600 group-hover:underline">View itinerary →</span>
          </div>
        </a>
      </div>
      <p class="mt-10 text-center text-sm text-slate-500">Custom trips: <a href="contact.html" class="font-semibold text-sky-700 hover:underline">Contact us</a></p>
    </section>
  </main>
"""

BLOG_MAIN = """
  <main>
    <section class="border-b border-slate-200 bg-gradient-to-br from-slate-900 via-sky-950 to-slate-950 px-4 py-14 text-white sm:px-6 lg:px-8">
      <div class="mx-auto max-w-3xl text-center">
        <p class="text-xs font-bold uppercase tracking-[0.2em] text-sky-200/90">Travel inspiration</p>
        <h1 class="mt-3 text-3xl font-extrabold tracking-tight sm:text-4xl">Blog</h1>
        <p class="mx-auto mt-4 max-w-2xl text-sm text-white/85 sm:text-base">Guides, packing ideas, and destination stories from the Infinity Routes editorial team.</p>
      </div>
    </section>
    <section class="mx-auto max-w-6xl px-4 py-12 sm:px-6 lg:px-8">
      <div class="grid gap-8 md:grid-cols-3">
        <article class="overflow-hidden rounded-2xl border border-slate-200 bg-white shadow-sm">
          <a href="blog-details.html" class="block aspect-[16/10] bg-slate-200 bg-cover bg-center" style="background-image:url('https://images.unsplash.com/photo-1488646953014-85cb44e25828?auto=format&fit=crop&w=800&q=80')"></a>
          <div class="p-5">
            <p class="text-xs font-semibold uppercase tracking-wide text-sky-600">Planning</p>
            <h2 class="mt-2 text-lg font-bold text-slate-900"><a href="blog-details.html" class="hover:text-sky-700">How to plan a multi-city trip without the stress</a></h2>
            <p class="mt-2 text-sm text-slate-600">Flights, buffers, and apps that keep your itinerary sane.</p>
            <a href="blog-details.html" class="mt-3 inline-block text-sm font-semibold text-sky-600 hover:underline">Read more</a>
          </div>
        </article>
        <article class="overflow-hidden rounded-2xl border border-slate-200 bg-white shadow-sm">
          <a href="blog-details.html" class="block aspect-[16/10] bg-slate-200 bg-cover bg-center" style="background-image:url('https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=800&q=80')"></a>
          <div class="p-5">
            <p class="text-xs font-semibold uppercase tracking-wide text-sky-600">Beach</p>
            <h2 class="mt-2 text-lg font-bold text-slate-900"><a href="blog-details.html" class="hover:text-sky-700">Best shoulder-season beach escapes in Asia</a></h2>
            <p class="mt-2 text-sm text-slate-600">Fewer crowds, better rates, and still-great weather windows.</p>
            <a href="blog-details.html" class="mt-3 inline-block text-sm font-semibold text-sky-600 hover:underline">Read more</a>
          </div>
        </article>
        <article class="overflow-hidden rounded-2xl border border-slate-200 bg-white shadow-sm">
          <a href="blog-details.html" class="block aspect-[16/10] bg-slate-200 bg-cover bg-center" style="background-image:url('https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?auto=format&fit=crop&w=800&q=80')"></a>
          <div class="p-5">
            <p class="text-xs font-semibold uppercase tracking-wide text-sky-600">City</p>
            <h2 class="mt-2 text-lg font-bold text-slate-900"><a href="blog-details.html" class="hover:text-sky-700">First-timer’s weekend in a new city</a></h2>
            <p class="mt-2 text-sm text-slate-600">Neighbourhoods, transit, and one “must-book” experience.</p>
            <a href="blog-details.html" class="mt-3 inline-block text-sm font-semibold text-sky-600 hover:underline">Read more</a>
          </div>
        </article>
      </div>
    </section>
  </main>
"""

TERMS_MAIN = """
  <main class="mx-auto max-w-3xl px-4 py-12 sm:px-6 lg:px-8">
    <p class="text-xs font-semibold uppercase tracking-wide text-sky-600">Infinity Routes Travels</p>
    <h1 class="mt-2 text-3xl font-extrabold tracking-tight text-slate-900">Terms of use</h1>
    <p class="mt-2 text-sm text-slate-500">Last updated: April 2026</p>
    <div class="prose prose-slate mt-8 max-w-none text-slate-700 prose-p:leading-relaxed">
      <p>By accessing <strong>Infinity Routes Travels</strong> websites and services, you agree to these terms. If you do not agree, please do not use the site.</p>
      <h2 class="text-xl font-bold text-slate-900 mt-8">Use of the site</h2>
      <p>Content is provided for general travel information and inspiration. Listings, prices, and availability on third-party or partner offers may change without notice. You agree to use the site lawfully and not to misuse or attempt to disrupt our systems.</p>
      <h2 class="text-xl font-bold text-slate-900 mt-8">Intellectual property</h2>
      <p>Branding, text, layout, and media on this site are protected by applicable laws. You may not copy or redistribute materials without permission, except as allowed for personal, non-commercial use.</p>
      <h2 class="text-xl font-bold text-slate-900 mt-8">Disclaimer</h2>
      <p>Information is provided “as is” without warranties of any kind. We are not liable for decisions made based on site content or for third-party services linked from our pages.</p>
      <h2 class="text-xl font-bold text-slate-900 mt-8">Changes</h2>
      <p>We may update these terms from time to time. Continued use of the site after changes constitutes acceptance of the revised terms.</p>
      <h2 class="text-xl font-bold text-slate-900 mt-8">Contact</h2>
      <p>Reach us via <a href="contact.html" class="font-semibold text-sky-700 hover:underline">Contact</a>.</p>
    </div>
  </main>
"""

BLOG_DETAILS_MAIN = """
  <main class="mx-auto max-w-3xl px-4 py-12 sm:px-6 lg:px-8">
    <p class="text-xs font-semibold text-sky-600"><a href="blog.html" class="hover:underline">← Back to blog</a></p>
    <p class="mt-4 text-xs font-semibold uppercase tracking-wide text-slate-500">Planning · 8 min read</p>
    <h1 class="mt-2 text-3xl font-extrabold tracking-tight text-slate-900 sm:text-4xl">How to plan a multi-city trip without the stress</h1>
    <p class="mt-4 text-sm leading-relaxed text-slate-600">Flying through several cities is exciting—until connections, time zones, and hotel check-ins pile up. Here is a practical framework we use at Infinity Routes to keep trips smooth.</p>
    <div class="prose prose-slate mt-8 max-w-none text-slate-700">
      <h2 class="text-xl font-bold text-slate-900">1. Build in buffer days</h2>
      <p>Schedule at least half a day between long hops or international arrivals. You will thank yourself when flights shift or bags arrive late.</p>
      <h2 class="text-xl font-bold text-slate-900 mt-6">2. Anchor cities, not every hour</h2>
      <p>Pick two or three bases and take day trips. You see more with less packing and fewer early-morning transfers.</p>
      <h2 class="text-xl font-bold text-slate-900 mt-6">3. One booking hub</h2>
      <p>Keep confirmations, maps, and emergency contacts in one place—notes app or PDF—so you are not hunting inboxes at immigration.</p>
    </div>
    <p class="mt-10 text-sm text-slate-500">More stories on the <a href="blog.html" class="font-semibold text-sky-700 hover:underline">blog home</a>.</p>
  </main>
"""

TOUR_DETAILS_MAIN = """
  <main>
    <section class="border-b border-slate-200 bg-gradient-to-br from-rose-900 via-slate-900 to-amber-950 px-4 py-12 text-white sm:px-6 lg:px-8">
      <div class="mx-auto max-w-4xl">
        <p class="text-xs font-bold uppercase tracking-[0.2em] text-amber-200/90"><a href="tour.html" class="hover:underline">← All tours</a></p>
        <h1 class="mt-4 text-3xl font-extrabold tracking-tight sm:text-4xl">Heritage Golden Triangle</h1>
        <p class="mt-2 text-sm text-white/85">7 days · Delhi · Agra · Jaipur · Private car &amp; guide</p>
        <p class="mt-6 text-2xl font-extrabold">From ₹1,24,999 <span class="text-base font-normal text-white/70">per person (twin share)</span></p>
        <a href="contact.html" class="mt-6 inline-flex rounded-xl bg-white px-6 py-3 text-sm font-bold text-slate-900 shadow hover:bg-slate-100">Enquire now</a>
      </div>
    </section>
    <section class="mx-auto max-w-3xl px-4 py-12 sm:px-6 lg:px-8">
      <h2 class="text-lg font-extrabold text-slate-900">Highlights</h2>
      <ul class="mt-3 list-disc space-y-2 pl-5 text-sm text-slate-700">
        <li>Sunrise visit to the Taj Mahal with skip-the-line assistance where available</li>
        <li>Jaipur forts, bazaars, and a traditional Rajasthani dinner</li>
        <li>Old Delhi food walk and heritage walk in central Delhi</li>
      </ul>
      <h2 class="mt-10 text-lg font-extrabold text-slate-900">Day-by-day (summary)</h2>
      <p class="mt-3 text-sm leading-relaxed text-slate-600">Days 1–2 Delhi, Days 3–4 Agra, Days 5–7 Jaipur with flexible evenings. Exact timings are shared on booking confirmation.</p>
      <p class="mt-8 text-sm text-slate-500">Prices and availability are indicative; <a href="contact.html" class="font-semibold text-sky-700 hover:underline">contact us</a> for a tailored quote.</p>
    </section>
  </main>
"""

DEST_DETAILS_MAIN = """
  <main>
    <section class="border-b border-slate-200 bg-gradient-to-br from-cyan-900 via-slate-900 to-slate-950 px-4 py-12 text-white sm:px-6 lg:px-8">
      <div class="mx-auto max-w-4xl">
        <p class="text-xs font-bold uppercase tracking-[0.2em] text-cyan-200/90"><a href="destination.html" class="hover:underline">← Destinations</a></p>
        <h1 class="mt-4 text-3xl font-extrabold tracking-tight sm:text-4xl">Destination spotlight</h1>
        <p class="mt-3 max-w-2xl text-sm text-white/85">Use this layout for any city or region: swap the title, hero image, and bullets to match your guide. Link visitors to a dedicated city page when you have one.</p>
      </div>
    </section>
    <section class="mx-auto max-w-3xl px-4 py-12 sm:px-6 lg:px-8">
      <h2 class="text-lg font-extrabold text-slate-900">Why visit</h2>
      <p class="mt-3 text-sm leading-relaxed text-slate-600">Describe climate, culture, and the kind of traveller who will love it—families, foodies, adventure seekers, or weekend city breaks.</p>
      <h2 class="mt-8 text-lg font-extrabold text-slate-900">Where to stay</h2>
      <p class="mt-3 text-sm leading-relaxed text-slate-600">Summarise neighbourhoods or hotel styles (boutique, resort, airport transit). Point to <a href="deals.html" class="font-semibold text-sky-700 hover:underline">current deals</a> or a city page like <a href="bangalore.html" class="font-semibold text-sky-700 hover:underline">Bangalore</a>.</p>
      <h2 class="mt-8 text-lg font-extrabold text-slate-900">Top experiences</h2>
      <ul class="mt-3 list-disc space-y-2 pl-5 text-sm text-slate-700">
        <li>Iconic landmark or viewpoint</li>
        <li>Local food or market experience</li>
        <li>Day trip or nature option</li>
      </ul>
    </section>
  </main>
"""


def main():
    header, footer = extract_chrome()
    pages = [
        ("destination.html", "Destinations | Infinity Routes Travels", "Explore India and international cities—guides, hotels, and things to do.", DESTINATION_MAIN),
        ("tour.html", "Tours | Infinity Routes Travels", "Guided tour packages across India and abroad.", TOUR_MAIN),
        ("blog.html", "Blog | Infinity Routes Travels", "Travel guides and inspiration from Infinity Routes.", BLOG_MAIN),
        ("terms.html", "Terms of Use | Infinity Routes Travels", "Terms and conditions for using the Infinity Routes Travels website.", TERMS_MAIN),
        ("blog-details.html", "How to plan a multi-city trip | Infinity Routes Travels", "Practical tips for stress-free multi-city travel.", BLOG_DETAILS_MAIN),
        ("tour-details.html", "Heritage Golden Triangle | Infinity Routes Travels", "7-day Golden Triangle tour — Delhi, Agra, Jaipur.", TOUR_DETAILS_MAIN),
        ("destination-details.html", "Destination spotlight | Infinity Routes Travels", "Sample destination detail page for guides.", DEST_DETAILS_MAIN),
    ]
    for fname, title, desc, main in pages:
        write_page(ROOT / fname, title, desc, main, header, footer)


if __name__ == "__main__":
    main()
