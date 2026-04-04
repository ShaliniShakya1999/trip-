# -*- coding: utf-8 -*-
"""Generate privacy.html, cookies.html, terms.html from index chrome + boilerplate."""
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

MAIN_START = """
  <main class="mx-auto max-w-3xl px-4 py-12 sm:px-6 lg:px-8">
    <p class="text-xs font-semibold uppercase tracking-wide text-sky-600">Infinity Routes Travels</p>
    <h1 class="mt-2 text-3xl font-extrabold tracking-tight text-slate-900">{h1}</h1>
    <p class="mt-2 text-sm text-slate-500">Last updated: April 2026</p>
    <div class="prose prose-slate mt-8 max-w-none text-slate-700 prose-p:leading-relaxed">
"""

MAIN_END = """
    </div>
  </main>
"""


def extract_chrome() -> tuple[str, str]:
    raw = INDEX.read_text(encoding="utf-8")
    h0 = raw.index('<header class="sticky')
    h1 = raw.index("</header>", h0) + len("</header>")
    f0 = raw.index('<footer class="mt-10">')
    f1 = raw.index("</footer>", f0) + len("</footer>")
    return raw[h0:h1], raw[f0:f1]


PAGES = [
    (
        "privacy.html",
        "Privacy Policy | Infinity Routes Travels",
        "How Infinity Routes Travels collects, uses, and protects your information.",
        "Privacy policy",
        """
      <p>This policy describes how <strong>Infinity Routes Travels</strong> (“we”, “us”) handles personal information when you use our website and related services.</p>
      <h2 class="text-xl font-bold text-slate-900 mt-8">Information we collect</h2>
      <p>We may collect information you provide (such as name, email, and travel preferences), technical data (such as browser type and IP address), and usage data to improve our site and respond to enquiries.</p>
      <h2 class="text-xl font-bold text-slate-900 mt-8">How we use information</h2>
      <p>We use this information to operate and improve our services, communicate with you, personalize content, comply with law, and protect our users and business.</p>
      <h2 class="text-xl font-bold text-slate-900 mt-8">Sharing</h2>
      <p>We do not sell your personal information. We may share data with service providers who assist our operations (hosting, analytics), when required by law, or to protect rights and safety.</p>
      <h2 class="text-xl font-bold text-slate-900 mt-8">Your choices</h2>
      <p>Where applicable, you may request access, correction, or deletion of your personal data by contacting us. You can also adjust cookie preferences in your browser.</p>
      <h2 class="text-xl font-bold text-slate-900 mt-8">Contact</h2>
      <p>Questions about this policy: see our <a href="contact.html" class="font-semibold text-sky-700 hover:underline">Contact</a> page.</p>
""",
    ),
    (
        "cookies.html",
        "Cookie Policy | Infinity Routes Travels",
        "How Infinity Routes Travels uses cookies and similar technologies.",
        "Cookie policy",
        """
      <p>This policy explains how <strong>Infinity Routes Travels</strong> uses cookies and similar technologies on this website.</p>
      <h2 class="text-xl font-bold text-slate-900 mt-8">What are cookies?</h2>
      <p>Cookies are small text files stored on your device. They help sites remember preferences, measure traffic, and improve user experience.</p>
      <h2 class="text-xl font-bold text-slate-900 mt-8">How we use cookies</h2>
      <p>We may use essential cookies (required for the site to work), functional cookies (such as language or layout preferences), and analytics cookies to understand how visitors use our pages.</p>
      <h2 class="text-xl font-bold text-slate-900 mt-8">Managing cookies</h2>
      <p>You can control or delete cookies through your browser settings. Blocking some cookies may affect how parts of the site function.</p>
      <h2 class="text-xl font-bold text-slate-900 mt-8">Contact</h2>
      <p>For questions, visit <a href="contact.html" class="font-semibold text-sky-700 hover:underline">Contact</a>.</p>
""",
    ),
    (
        "terms.html",
        "Terms of Use | Infinity Routes Travels",
        "Terms and conditions for using the Infinity Routes Travels website.",
        "Terms of use",
        """
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
""",
    ),
]


def main():
    header, footer = extract_chrome()
    for fname, title, desc, h1, body in PAGES:
        html = (
            HEAD.format(title=title, desc=desc)
            + "\n  "
            + header.strip()
            + "\n"
            + MAIN_START.format(h1=h1)
            + body
            + MAIN_END
            + "\n  "
            + footer.strip()
            + "\n</body>\n</html>\n"
        )
        (ROOT / fname).write_text(html, encoding="utf-8")
        print("Wrote", fname)


if __name__ == "__main__":
    main()
