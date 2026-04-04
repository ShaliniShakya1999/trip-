# -*- coding: utf-8 -*-
"""Generate help-center.html and faqs.html from index chrome."""
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


HELP_MAIN = """
  <main>
    <section class="border-b border-slate-200 bg-gradient-to-br from-sky-900 via-slate-900 to-slate-950 px-4 py-14 text-white sm:px-6 lg:px-8">
      <div class="mx-auto max-w-3xl text-center">
        <p class="text-xs font-bold uppercase tracking-[0.2em] text-sky-200/90">Support</p>
        <h1 class="mt-3 text-3xl font-extrabold tracking-tight sm:text-4xl">Help center</h1>
        <p class="mx-auto mt-4 max-w-2xl text-sm text-white/85 sm:text-base">Find answers about bookings, payments, and your Infinity Routes account. Still need help? We are one message away.</p>
        <div class="mt-8 flex flex-wrap items-center justify-center gap-3">
          <a href="contact.html" class="inline-flex rounded-xl bg-white px-6 py-3 text-sm font-bold text-slate-900 shadow-lg hover:bg-slate-100">Contact us</a>
          <a href="faqs.html" class="inline-flex rounded-xl border border-white/30 bg-white/10 px-6 py-3 text-sm font-bold text-white backdrop-blur hover:bg-white/20">Browse FAQs</a>
        </div>
      </div>
    </section>
    <section class="border-b border-slate-200 bg-white px-4 py-10 sm:px-6 lg:px-8">
      <div class="mx-auto grid max-w-5xl gap-4 sm:grid-cols-3">
        <a href="faqs.html" class="rounded-2xl border border-slate-200 bg-slate-50 p-5 transition hover:border-sky-200 hover:bg-sky-50/50">
          <p class="text-xs font-bold uppercase tracking-wide text-sky-700">Quick</p>
          <p class="mt-2 font-bold text-slate-900">FAQs</p>
          <p class="mt-1 text-sm text-slate-600">Short answers to the most common questions.</p>
        </a>
        <a href="tour.html" class="rounded-2xl border border-slate-200 bg-slate-50 p-5 transition hover:border-sky-200 hover:bg-sky-50/50">
          <p class="text-xs font-bold uppercase tracking-wide text-sky-700">Explore</p>
          <p class="mt-2 font-bold text-slate-900">Tours</p>
          <p class="mt-1 text-sm text-slate-600">Packages and guided experiences.</p>
        </a>
        <a href="destination.html" class="rounded-2xl border border-slate-200 bg-slate-50 p-5 transition hover:border-sky-200 hover:bg-sky-50/50">
          <p class="text-xs font-bold uppercase tracking-wide text-sky-700">Places</p>
          <p class="mt-2 font-bold text-slate-900">Destinations</p>
          <p class="mt-1 text-sm text-slate-600">Hotels and guides by city and region.</p>
        </a>
      </div>
    </section>
    <section class="mx-auto max-w-3xl px-4 py-12 sm:px-6 lg:px-8">
      <h2 class="text-lg font-extrabold text-slate-900">Getting started</h2>
      <p class="mt-3 text-sm leading-relaxed text-slate-600">Use the <a href="index.html#search-hero" class="font-semibold text-sky-700 hover:underline">homepage search</a> to explore hotels, flights, and activities. City pages list hand-picked stays and local tips. <a href="deals.html" class="font-semibold text-sky-700 hover:underline">Deals</a> highlights current offers.</p>
      <h2 class="mt-10 text-lg font-extrabold text-slate-900">Before you travel</h2>
      <p class="mt-3 text-sm leading-relaxed text-slate-600">Check passport and visa rules for your nationality, airline baggage limits, and hotel check-in times. For flights, arrive at the airport as your carrier recommends. Save your booking confirmation and a government ID on your phone.</p>
      <h2 class="mt-10 text-lg font-extrabold text-slate-900">Bookings &amp; changes</h2>
      <p class="mt-3 text-sm leading-relaxed text-slate-600">For modifications or cancellations, have your booking reference ready. Policies depend on the airline, hotel, or partner—our team can explain the next steps when you <a href="contact.html" class="font-semibold text-sky-700 hover:underline">contact us</a>. Name changes and date moves are often restricted on promotional fares.</p>
      <h2 class="mt-10 text-lg font-extrabold text-slate-900">Payments &amp; receipts</h2>
      <p class="mt-3 text-sm leading-relaxed text-slate-600">We work with trusted payment partners. Never share OTPs, card CVV, or net-banking passwords by email or chat. Need an invoice or GST details? Mention it in your message to support with your booking ID.</p>
      <h2 class="mt-10 text-lg font-extrabold text-slate-900">Refunds &amp; timelines</h2>
      <p class="mt-3 text-sm leading-relaxed text-slate-600">When a refund is approved, timing depends on your bank or card issuer—often 5–14 business days after the supplier processes it. We will confirm status by email when you <a href="contact.html" class="font-semibold text-sky-700 hover:underline">reach out</a> with your reference.</p>
      <h2 class="mt-10 text-lg font-extrabold text-slate-900">Safety &amp; fraud</h2>
      <p class="mt-3 text-sm leading-relaxed text-slate-600">We only request payments through our official site and listed channels. If someone asks for payment to a personal account or pressures you to share OTPs, stop and <a href="contact.html" class="font-semibold text-sky-700 hover:underline">report it</a> immediately.</p>
      <h2 class="mt-10 text-lg font-extrabold text-slate-900">Privacy &amp; account</h2>
      <p class="mt-3 text-sm leading-relaxed text-slate-600">Read our <a href="privacy.html" class="font-semibold text-sky-700 hover:underline">Privacy policy</a> and <a href="cookies.html" class="font-semibold text-sky-700 hover:underline">Cookie policy</a>. For terms of use, see <a href="terms.html" class="font-semibold text-sky-700 hover:underline">Terms of use</a>.</p>
      <h2 class="mt-10 text-lg font-extrabold text-slate-900">Common questions</h2>
      <p class="mt-3 text-sm leading-relaxed text-slate-600">See the <a href="faqs.html" class="font-semibold text-sky-700 hover:underline">FAQs</a> page for quick answers.</p>
    </section>
  </main>
"""

FAQ_MAIN = """
  <main>
    <section class="border-b border-slate-200 bg-gradient-to-br from-emerald-900 via-slate-900 to-slate-950 px-4 py-14 text-white sm:px-6 lg:px-8">
      <div class="mx-auto max-w-3xl text-center">
        <p class="text-xs font-bold uppercase tracking-[0.2em] text-emerald-200/90">Answers</p>
        <h1 class="mt-3 text-3xl font-extrabold tracking-tight sm:text-4xl">Frequently asked questions</h1>
        <p class="mx-auto mt-4 max-w-2xl text-sm text-white/85 sm:text-base">Quick answers about Infinity Routes. For anything else, visit the <a href="help-center.html" class="font-semibold text-white underline decoration-white/40 underline-offset-2 hover:text-white">Help center</a> or <a href="contact.html" class="font-semibold text-white underline decoration-white/40 underline-offset-2 hover:text-white">contact us</a>.</p>
      </div>
    </section>
    <section class="mx-auto max-w-3xl px-4 py-12 sm:px-6 lg:px-8">
      <dl class="space-y-8">
        <div>
          <dt class="text-base font-bold text-slate-900">How do I search for hotels or flights?</dt>
          <dd class="mt-2 text-sm leading-relaxed text-slate-600">Open the <a href="index.html#search-hero" class="font-semibold text-sky-700 hover:underline">homepage</a>, choose the tab you need (Hotels, Flights, etc.), enter your destination and dates, then explore results.</dd>
        </div>
        <div>
          <dt class="text-base font-bold text-slate-900">Can I change or cancel a booking?</dt>
          <dd class="mt-2 text-sm leading-relaxed text-slate-600">It depends on the fare or room rules set by the airline or hotel. Send us your booking reference via <a href="contact.html" class="font-semibold text-sky-700 hover:underline">Contact</a> and we will outline your options.</dd>
        </div>
        <div>
          <dt class="text-base font-bold text-slate-900">Is my payment secure?</dt>
          <dd class="mt-2 text-sm leading-relaxed text-slate-600">We use industry-standard encryption with payment partners. We will never ask for your full card number or OTP by email.</dd>
        </div>
        <div>
          <dt class="text-base font-bold text-slate-900">Where can I read legal &amp; privacy information?</dt>
          <dd class="mt-2 text-sm leading-relaxed text-slate-600">See <a href="privacy.html" class="font-semibold text-sky-700 hover:underline">Privacy policy</a>, <a href="cookies.html" class="font-semibold text-sky-700 hover:underline">Cookie policy</a>, and <a href="terms.html" class="font-semibold text-sky-700 hover:underline">Terms of use</a>.</dd>
        </div>
        <div>
          <dt class="text-base font-bold text-slate-900">How do I reach customer support?</dt>
          <dd class="mt-2 text-sm leading-relaxed text-slate-600">Use the <a href="contact.html" class="font-semibold text-sky-700 hover:underline">Contact</a> page—form, phone, or email as listed there. We aim to reply within one business day.</dd>
        </div>
        <div>
          <dt class="text-base font-bold text-slate-900">Why did the price change before I paid?</dt>
          <dd class="mt-2 text-sm leading-relaxed text-slate-600">Fares and room rates come from airlines and hotels and can change with availability, currency, or taxes. The price shown at checkout is what applies once you complete payment.</dd>
        </div>
        <div>
          <dt class="text-base font-bold text-slate-900">Can I book for someone else?</dt>
          <dd class="mt-2 text-sm leading-relaxed text-slate-600">Yes—enter the traveller’s name exactly as on their ID for flights, and the guest name the property expects for hotels. You can pay with your card; keep the booking confirmation handy for them.</dd>
        </div>
        <div>
          <dt class="text-base font-bold text-slate-900">How do I get an invoice or GST bill?</dt>
          <dd class="mt-2 text-sm leading-relaxed text-slate-600">Email <a href="mailto:support@infinityroutes.in" class="font-semibold text-sky-700 hover:underline">support@infinityroutes.in</a> with your booking reference and billing details (company name, GSTIN if applicable). What we can issue depends on the supplier’s rules.</dd>
        </div>
        <div>
          <dt class="text-base font-bold text-slate-900">What if my airline delays or cancels the flight?</dt>
          <dd class="mt-2 text-sm leading-relaxed text-slate-600">The operating carrier’s conditions apply. Check your email and the airline’s app for rebooking or refund options, then <a href="contact.html" class="font-semibold text-sky-700 hover:underline">contact us</a> if you need help interpreting your ticket rules.</dd>
        </div>
        <div>
          <dt class="text-base font-bold text-slate-900">How do I manage cookies or marketing emails?</dt>
          <dd class="mt-2 text-sm leading-relaxed text-slate-600">See <a href="cookies.html" class="font-semibold text-sky-700 hover:underline">Cookie policy</a> for browser choices. For newsletters, use the unsubscribe link in any email or ask support to remove you.</dd>
        </div>
        <div>
          <dt class="text-base font-bold text-slate-900">Do you add a separate booking fee?</dt>
          <dd class="mt-2 text-sm leading-relaxed text-slate-600">Any service or convenience fees, if applicable, are shown before you pay—not hidden after checkout. Taxes and supplier charges are itemised where the channel allows.</dd>
        </div>
      </dl>
    </section>
  </main>
"""


def main():
    header, footer = extract_chrome()
    pages = [
        (
            "help-center.html",
            "Help center | Infinity Routes Travels",
            "Get help with bookings, payments, and your Infinity Routes account.",
            HELP_MAIN,
        ),
        (
            "faqs.html",
            "FAQs | Infinity Routes Travels",
            "Frequently asked questions about Infinity Routes Travels.",
            FAQ_MAIN,
        ),
    ]
    for fname, title, desc, main in pages:
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
        (ROOT / fname).write_text(html, encoding="utf-8")
        print("Wrote", fname)


if __name__ == "__main__":
    main()
