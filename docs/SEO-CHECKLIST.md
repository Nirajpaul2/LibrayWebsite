# Silent Zone: SEO audit and release checklist

Canonical homepage: https://silentzone.nirajpaul.com/
Audit date: 9 October 2026.

## Findings and implementation

- Public HTTPS homepage returned 200 without a noindex header. Source contained no noindex meta directive.
- robots.txt and sitemap.xml returned 404 before this update. Added crawl-allowing robots.txt and a one-URL sitemap; a missing robots file alone does not block indexing.
- Added one self-referencing HTTPS canonical, descriptive title/description, local H1/H2 content and LocalBusiness JSON-LD. No fabricated ratings, awards, reviews or keyword location pages.
- Confirmed user-supplied address, telephone, map coordinates, landmark and 06:00–22:00 hours are used. The owner confirmed opening every day; schema includes Monday through Sunday.
- Confirmed regular monthly prices remain ₹350/₹550/₹750/₹950 for 4/8/12/16 hours. No October promotion was present in the source or live page, and the owner confirmed no price changes. Do not invent an offer or substitute promotional prices for regular prices. If approved later, add a separate section with exact eligibility and start/end dates, and remove/hide it after expiry; never promote it through permanent title/description or regular priceRange.
- Six inline images now have local responsive WebP variants, intrinsic dimensions and asynchronous decoding. Below-fold images and map remain lazy loaded; the hero retains fetchpriority=high. Original user assets and original gallery full-size destinations are preserved.
- Original hero: 1,201,322 bytes; largest replacement: 77,616 bytes (93.5% smaller). Original logo: 1,252,638 bytes; 2x header replacement: 3,260 bytes (99.7% smaller). Detailed source sizes and variants: image-optimization.json. These are transfer-size improvements, not measured Core Web Vitals gains.
- Added a keyboard skip link, larger navigation targets, darker secondary text and a mobile gallery aspect-ratio fix. Existing branding, section navigation, facilities and enquiry actions remain.
- Added _headers and _redirects for compatible static hosting (including Cloudflare Pages). Verify the actual hosting platform honors them; they are not enforced by Python's preview server. Asset cache is one week, not immutable, because filenames may be reused.
- HTTP currently returns 200 rather than redirecting to HTTPS. Enable an HTTPS redirect in the domain's hosting/CDN settings. Do not change bot protections blindly: the live HTML includes Cloudflare JavaScript detection. Use Search Console's live test to confirm Googlebot access.

## Automated check

Run `python3 scripts/check-seo.py`. This validates the local crawl directives, canonical, XML, JSON-LD shape and business facts, regular prices, anchors, local assets and WhatsApp URLs. It does not replace Google's rich results validator or prove indexing.

## Google Business Profile (owner)

- [ ] Claim/verify the existing Silent Zone listing; do not create a duplicate.
- [ ] Use the real business name, accurate available category, telephone +91 99424 19837, and website https://silentzone.nirajpaul.com/.
- [ ] Set address to Ward No. 4, Sonbersa Chowk, Musapur, Samastipur, Bihar 848103; check the pin at 25.859534, 85.7654646 and mention Shamb Siva Vivah Bhawan as the landmark where appropriate.
- [ ] Correct the old 24-hour listing to 6 AM–10 PM on confirmed open days; enter holiday exceptions.
- [ ] Add authentic photos and accurate facilities. Invite honest student reviews without incentives or review gating.

## Search Console verification and submission

- [ ] Add the URL-prefix property https://silentzone.nirajpaul.com/ (or use an already verified parent Domain property).
- [ ] Complete a verification method offered by Google. For HTML-tag verification, provide the actual tag for insertion; never invent a token. For DNS verification, add Google's exact TXT record at the DNS provider and wait for verification.
- [ ] Inspect the homepage and run Test Live URL. Confirm Google can fetch it, indexing is allowed, and rendered content/photos are visible.
- [ ] Submit https://silentzone.nirajpaul.com/sitemap.xml and confirm Success.
- [ ] Request indexing after the release. Monitor Page indexing, Performance and Core Web Vitals; a request does not guarantee indexing or a ranking position.

## Manual post-deployment tests

- [ ] Confirm the new title/content and local WebP images appear on the custom domain (not only localhost).
- [ ] Confirm /robots.txt returns plain text 200 and /sitemap.xml returns valid XML 200, not an HTML fallback or challenge.
- [ ] Confirm page source contains exactly one HTTPS canonical and valid LocalBusiness JSON-LD; no noindex meta or X-Robots-Tag noindex header.
- [ ] Run https://search.google.com/test/rich-results and https://validator.schema.org/ against the homepage. Address critical errors; assess optional fields without inventing facts.
- [ ] Verify HTTP redirects permanently to HTTPS and /index.html redirects to / on the production host.
- [ ] Test 320px, 390px and desktop widths; check navigation, prices, images, map and 200% browser zoom for overflow or obscured content.
- [ ] Tab through the skip link, navigation and enquiry buttons. Confirm clear focus and readable contrast.
- [ ] Open Maps and directions, verify the pin, test tap-to-call and WhatsApp prefilled messages without sending a test enquiry.
- [ ] Run PageSpeed Insights on mobile and desktop. Record lab results separately from real-user data. Assess LCP, INP and CLS at the 75th percentile when enough field data exists; local screenshots are not a Core Web Vitals measurement.
- [ ] Recheck prices, opening days and any approved promotion dates after each update.

## Performance measurement limitation

The Chrome DevTools MCP required by the web-perf skill was unavailable, so no DevTools trace or measured INP/CLS/LCP score is claimed. Browser rendering and asset validation are separate checks. Use PageSpeed Insights/Search Console for production measurement.

Sources: https://developers.google.com/search/docs/appearance/structured-data/local-business ; https://developers.google.com/search/docs/crawling-indexing/robots/intro ; https://web.dev/articles/vitals ; https://support.google.com/business/answer/7091

## Deployment verification — 9 October 2026

Commit f6444dc deployed successfully via the GitHub check named `Workers Builds: libraywebsite` (the integration reports Workers Builds, although described as Pages). The public custom domain now serves the SEO update.

Confirmed live using curl: homepage, robots.txt and sitemap.xml return 200; no noindex header; homepage contains the canonical and LocalBusiness JSON-LD with all seven opening days; regular fees are unchanged. The hero WebP returns 200 with `Cache-Control: public, max-age=604800`; /index.html returns 301 to /.

Confirmed in browser: desktop and 320px/354px CSS viewports show no horizontal page overflow; all six inline images load after scrolling; membership navigation works and prices remain legible. Solid-background text checks: secondary text 5.25:1 on cream and 4.83:1 on facilities background; button text 8.70:1; visit labels 4.83:1. This is not a comprehensive WCAG audit.

Still outstanding: HTTP-to-HTTPS redirect at the hosting/CDN layer, Search Console ownership/Googlebot live testing, Google's Rich Results Test, and production Core Web Vitals measurement. One Python automated-client request received HTTP 403; curl checks succeeded. Do not assume this means Googlebot is blocked or that it is allowed—verify through Search Console and inspect Cloudflare security events if its live test fails.
