# Silent Zone Library — local SEO audit

Audit date: 31 October 2026 (Asia/Kolkata). Website: https://silentzone.nirajpaul.com/.

## Scope and verified identity

Audited the live site, all public source files, HTTP responses, local mobile/desktop rendering, and the signed-in Google Search Console property. The site is a single static HTML page with CSS, local images, and a small optional contact-event script; there is no SPA, hydration dependency, application server, package build, authentication route, student database, or private API in this repository. Public content is delivered in the initial HTML.

- Business: Silent Zone Self Study Library.
- Address supplied by the owner: Ward No. 4, Sonbersa Chowk, **Musa Pur**, Samastipur, Bihar 848103. Natural prose also uses the familiar spelling **Musapur**.
- Telephone/WhatsApp: +91 99424 19837.
- Hours: daily 06:00–22:00, confirmed by the owner; no weekly closure.
- Landmark: Shamb Siva Vivah Bhawan, Musapur.
- Maps identity: [existing business listing](https://www.google.com/maps/place/Silent+Zone+Self+Study+Library/@25.8595435,85.7629547,17z/data=!4m6!3m5!1s0x39ed9b3596592c0f:0xd26c0da7412aeed1!8m2!3d25.859534!4d85.7654646!16s%2Fg%2F11z5w49w8v); coordinates 25.859534, 85.7654646. These are the business pin coordinates, not the map viewport center.
- Regular monthly fees retained: 4 hours ₹350; 8 hours ₹550; 12 hours ₹750; 16 hours ₹950.
- Batches retained: 6–10 AM, 10 AM–2 PM, 2–6 PM, 6–10 PM.
- No October promotional prices were supplied or approved; no promotion or expiry claim was introduced.
- Existing facilities, original photographs, supplied logo, navigation and phone/WhatsApp/Maps destinations were preserved. No unverified social profiles, reviews, ratings, awards, coaching, Wi-Fi, laptop provision or guaranteed seats were added.

## Baseline and prioritized plan

Before editing, the working tree was clean and backup branch `backup/pre-advanced-seo-2026-10-31` was created at `4cf92f1`. Machine-readable baseline: `docs/seo-baseline-2026-10-31/baseline.json`. The action plan was presented before changes.

| Area | Verified starting state | Priority / action |
|---|---|---|
| Title | Self Study Library in Samastipur \| Silent Zone, Musapur | P1: front-load recognizable brand and city, retain service relevance |
| H1 | Local service heading without brand | P1: include Silent Zone; preserve original creative tagline as supporting copy |
| Local content | Address/AC facilities already present; limited reading-room and exam-routine explanation | P1: helpful student guidance and contextual links |
| Canonical, robots, sitemap | Already present and valid | Preserve and regression-test; do not describe them as newly added |
| JSON-LD | Existing LocalBusiness with identity, hours, coordinates and photographs | Preserve one entity, align exact address spelling and natural description |
| Rendering | Meaningful static HTML before JavaScript | Preserve; no prerendering framework necessary |
| HTTP | HTTP homepage returned 200 instead of redirecting | P1 hosting follow-up: scoped HTTP→HTTPS redirect |
| Status codes | HTTPS homepage/robots/sitemap 200; /index.html 301; unknown path 404 | Preserve |
| Images | Existing responsive WebP variants, dimensions, lazy gallery/map, eager high-priority hero | Refine image sizing hints, retain quality and original full-size photo links |
| Fonts | External Google Fonts CSS blocked rendering | P1 after measured PSI evidence: self-host same font files |
| Enquiries | Phone, plan-specific WhatsApp and Maps already worked; no tracking integration | P2: first-screen WhatsApp and optional consent-gated event hook |
| Social preview | Text metadata present, no complete large-image sharing card | P2: add actual library photo and Twitter/OG image metadata |

No accidental `noindex`, `nofollow`, robots blocking rule, missing local asset, broken fragment, or skipped heading level was found by the source checks. Crawlability is not a guarantee of indexing or ranking.

## Search Console evidence

### User-supplied ten-query extract

This is the provided screenshot transcription, not a full six-month export. Its totals are **3 clicks / 47 impressions = 6.38% CTR** for these rows only.

| Query | Clicks | Impressions | CTR |
|---|---:|---:|---:|
| library in samastipur | 2 | 9 | 22.22% |
| library samastipur | 1 | 7 | 14.29% |
| self study | 0 | 10 | 0% |
| library near me | 0 | 9 | 0% |
| silent zone library | 0 | 5 | 0% |
| bilis library | 0 | 3 | 0% |
| cabin library near me | 0 | 1 | 0% |
| labrary | 0 | 1 | 0% |
| laptop library near me | 0 | 1 | 0% |
| self study library | 0 | 1 | 0% |

All ten already have impressions; eight have zero clicks. Samastipur terms produce the visible clicks. There is no Musapur/Musa Pur, Sonbersa, AC, reading-room or competitive-exam query in this extract. This is a coverage opportunity, not proof those searches never occur or that the site has never ranked for them. Do not target another library's possible brand ("bilis library"), misspellings, or unverified laptop facilities.

### Direct Search Console inspection

URL Inspection confirms **URL is on Google / Page is indexed**. Last crawl: 18 October 2026, 06:38:09 AM, Googlebot smartphone. Crawl allowed: Yes; fetch: Successful; indexing allowed: Yes. User-declared canonical is the HTTPS homepage and Google-selected canonical is the inspected URL. Sitemap discovery showed a temporary processing error; the submitted sitemap list was empty. These are the stored index observations, not proof that the new release has already been recrawled.

The authenticated `nirajpaul.com` Domain property was available. Applied **Web search**, **Last 6 months**, and **Page contains `silentzone.nirajpaul.com/`** to exclude the owner's other websites. The chart's available date range was **8–28 October 2026**, not six months of history. Last update at inspection: five hours ago.

| Report | Clicks | Impressions | CTR | Average position |
|---|---:|---:|---:|---:|
| Filtered chart total | 4 | 115 | 3.5% | 5.0 |
| Homepage (only page row) | 4 | 115 | 3.5% | 5.0 |
| India (reported country row) | 3 | 56 | 5.4% | 5.8 |
| Mobile (reported device row) | 1 | 46 | 2.2% | 6.3 |
| Desktop (reported device row) | 2 | 8 | 25% | 1.9 |
| Tablet (reported device row) | 0 | 2 | 0% | 8.5 |

The UI explicitly warns that filtered charts/tables can be partial. Country/device rows total 3/56 and do not reconcile to the 4/115 chart total; preserve that discrepancy rather than filling in missing data. These are separate UI breakdowns, not a joined country-by-device export. No full CSV was exported. The observed typo in the live query table was **"labariy"**, different from **"labrary"** in the supplied transcription.

The live query report exposed 19 rows. Key positions: `library in samastipur` 7.9; `library samastipur` 15.3; `self study` 4.4; `library near me` 4.2; `silent zone library` 1.4. The latter's zero clicks from only five impressions cannot establish a persistent snippet problem. Nine additional rows each had one impression and zero clicks: library (2.0), library for self study (2.0), liebery (2.0), slef study (3.0), library photo self study (5.0), study zone (5.0), just dial (6.0), open library (7.0), silent zones (12.0). The 19 disclosed query rows total 3/56, not the chart total.

Daily data was also inspected: for example October 24 had 13 impressions/0 clicks; October 28 had 3 impressions/1 click. Those tiny daily samples cannot support a trend claim. The homepage is the only reported library page, so there is no supported list of multiple poor-CTR pages. Its 3.5% CTR and mobile's 2.2% are baselines to compare after enough impressions accrue, not universal performance grades. Average position is an aggregate, not a guaranteed position for every student.

Priorities validated by these data: retain Samastipur service relevance, improve recognizable branding and snippet clarity, prioritize mobile enquiries, and explain real study-room use. Avoid creating duplicate location pages. "Best" is used only as student-centered selection advice, never a claim to be Samastipur's best business. "Near me" relevance depends on the real location and searcher; repeating that phrase is not a strategy.

## Implemented changes

1. Title: **Silent Zone Library Samastipur | AC Self Study Library**.
2. Description: **Find a quiet, air-conditioned self-study library in Samastipur. Silent Zone offers individual desks, flexible study batches and affordable monthly plans. Enquire today.** Google can choose a different snippet; length alone does not guarantee display.
3. Single H1: **Silent Zone — Self Study Library in Samastipur**. Original attractive headline retained as supporting copy. H2/H3 structure remains logical.
4. Natural reading-room/exam-preparation copy, guidance on comparing facilities, visit instructions, and an honest seat-enquiry explanation. Contextual links lead to facilities, membership and contact. No new location pages.
5. First-screen WhatsApp CTA; existing four plan-specific messages, telephone links, directions link and contact section remain. An enquiry explicitly does not reserve a seat.
6. Retained accurate LocalBusiness JSON-LD; aligned Musa Pur spelling, alternate recognizable name, and reading-room description. No redundant Organization object (LocalBusiness already represents the business), no BreadcrumbList for a one-page site without a breadcrumb trail, and no unverified social profiles.
7. Large-image OG/Twitter sharing cards use an existing real library photograph with dimensions and alt text. Existing descriptive image alts and responsive variants remain; logo/gallery sizing hints refined.
8. Same DM Sans and Libre Caslon Display fonts hosted locally as WOFF2, with existing `font-display: swap`, local preload for the two Latin faces, and seven-day cache headers. Original SIL Open Font License texts and source URLs retained. Removes the Google Fonts stylesheet dependency; does not change font design. The site still embeds Google Maps.
9. Tiny deferred contact-intent hook; **no analytics provider, tracking requests, cookies or storage are enabled**. It only dispatches `silentzone:contact-intent` after `window.silentZoneAnalyticsConsent === true`, and respects GPC/DNT. Allowed payload contains only action (`whatsapp`, `phone`, `directions`) and plan (`none`, `single`, `double`, `triple`, `full`). Do not call a click a completed enquiry or membership.
10. Extended regression checks for social metadata, local schema/assets, contact annotations and heading hierarchy; added event consent/privacy tests.

## Performance and accessibility evidence

Baseline [mobile PageSpeed report](https://pagespeed.web.dev/analysis/https-silentzone-nirajpaul-com/dpzenzosyr?form_factor=mobile), before this deployment: Lighthouse 13.6.0, emulated Moto G Power, Slow 4G, initial page load.

| Lab measurement | Baseline |
|---|---:|
| Performance | 95 |
| FCP | 1.5 s |
| LCP | 2.6 s |
| TBT | 0 ms |
| CLS | 0 |
| Speed Index | 3.9 s |
| Automated accessibility / best practices / SEO checks | 100 / 100 / 100 |

These are observed Lighthouse results, **not an invented SEO score, ranking forecast, or full accessibility certification**. PSI showed **No Data** for real-user experience. INP was not measured; TBT is not INP. Field Core Web Vitals cannot be declared passed. Google's field targets are LCP ≤2.5 s, INP ≤200 ms and CLS ≤0.1 at the 75th percentile.

Measured opportunities: render-blocking estimate 720 ms (external fonts CSS 750 ms, local CSS 160 ms); hero image recompression estimate 16 KiB; short-lived third-party caching/legacy JS also flagged. Font dependency was addressed. Existing WebP quality was retained rather than degrade real photographs for a small estimate. The small main stylesheet remains blocking to avoid unstyled content. Cloudflare/Maps-owned scripts need separate provider decisions, not unreviewed disabling.

Local checks at 320px, 390px and 1440px found no horizontal overflow. Mobile membership cards showed all unchanged monthly prices clearly; desktop typography and photographic layout preserved. All six image elements loaded in the inspected desktop page. Link names, alt text, iframe title, heading order, skip link and focus styles inspected. A complete screen-reader audit and field responsiveness assessment remain manual.

The DevTools MCP trace workflow could not run because that connector is unavailable. Performance measurement used Google's browser-based PageSpeed report after the keyless API returned quota error 429. No trace timings or field metrics were invented.

## Technical verification and deployment

- PASS: `python3 scripts/check-seo.py` — one H1, hierarchy, canonical, crawl rules, sitemap, real schema identity/address/hours/coordinates/maps, no invented ratings, unchanged prices, social metadata, local assets and variants, fragments, phone/WhatsApp/directions annotations.
- PASS: `node scripts/check-contact-events.mjs` — consent absent/false, GPC/DNT, allowed/invalid payloads and actions.
- PASS: `node --check dist/contact-events.js`; `git diff --check`.
- Build/lint: no package build or lint configuration exists; deploy artifact is the `dist/` directory.
- Production, Rich Results Test, Schema.org Validator and post-deployment PageSpeed results are recorded in the completion section below after release verification.

Changed files: `dist/index.html`, `dist/style.css`, `dist/_headers`, new `dist/contact-events.js`, new `dist/fonts/*` (four WOFF2 files and two licenses), `scripts/check-seo.py`, new `scripts/check-contact-events.mjs`, new `docs/font-sources.json`, new `docs/seo-baseline-2026-10-31/baseline.json`, and this audit. Existing `robots.txt`, `sitemap.xml`, `_redirects`, photographs and prices were inspected and retained.

## Remaining tasks and deployment checklist

- [ ] Confirm successful GitHub-triggered Cloudflare build and compare deployed title, H1, schema and assets to this release. The observed integration is **Workers Builds: libraywebsite**, although it was described as Pages earlier; use the actual connected project.
- [ ] **Fix HTTP→HTTPS** at Cloudflare for host `silentzone.nirajpaul.com`, preserving path/query, using a permanent redirect. Do not use an unconditional static redirect that loops HTTPS traffic. Zone-wide Always Use HTTPS also affects other subdomains; use a scoped rule unless all hosts are intended to change. Re-test HTTP `/`, an asset and a query URL.
- [ ] Check the former `silent-zone-library.nirajpaul2.chatgpt.site` host if still maintained. Its current availability was not established by this audit. Redirect it to the custom domain if controlled; avoid publishing diverging copies. Main site has the correct canonical already.
- [ ] Keep only intended public pages in the sitemap. No admin/student routes currently exist. Any future private routes require authentication; robots.txt is not access control.
- [ ] Check phone/WhatsApp opening on real Android/iPhone devices, all membership-prefilled messages, Maps pin and directions, and the embedded map after scrolling. Do not send test messages to students.
- [ ] Run keyboard-only navigation, zoom at 200%, screen-reader checks and a real-device mobile visit. Verify no overlaps or layout shifts on slow networks.
- [ ] Re-run mobile/desktop PageSpeed and inspect field CWV when sufficient traffic exists. Lab scores vary between runs.
- [ ] If analytics is desired, select an approved provider and consent manager, document retention/privacy, and connect the event hook only after consent. Verify opt-out produces zero events and no provider requests; distinguish click intent, actual enquiries and confirmed memberships. No collection is operational yet.

## Google Business Profile checklist

- [ ] Manage the **existing** listing; verify ownership if needed. Do not create a duplicate.
- [ ] Use the real name **Silent Zone Self Study Library**, without added ranking keywords, awards or city strings not part of the actual name.
- [ ] Inspect categories offered in the current Indian GBP editor. Prefer the most specific category that actually describes this self-study/reading-room business; **Library** is a candidate if appropriate and available. Do not label it a public lending library, coaching centre or coworking business without verifying that service.
- [ ] Match the website's address, postal code and +91 99424 19837; verify the pin at the actual entrance. Confirm Musa Pur/Musapur spelling consistently in the address fields.
- [ ] Daily 6 AM–10 PM, plus accurate exceptional holiday hours when needed.
- [ ] Website field: `https://silentzone.nirajpaul.com/`; ensure directions reach the verified entrance near Shamb Siva Vivah Bhawan.
- [ ] Upload current genuine exterior/signage, entrance, interior and desk photos with permission. No stock photographs presented as the premises; avoid exposing students' personal materials.
- [ ] Describe only confirmed AC hall, individual desks, RO water, power backup, lockers, parking and reading materials; confirm current availability before changing profile claims.
- [ ] List the four regular monthly memberships accurately. Any future promotion needs separately confirmed dates/eligibility/prices and must remain distinct from regular plans.
- [ ] Invite genuine students to share honest reviews without incentives, filtering only happy students or fabricated reviews. Respond helpfully without disclosing personal student information.
- [ ] Keep contact details, photos and factual updates current; monitor profile calls/directions/website interactions where available.

## Search Console checklist

- [x] Existing `nirajpaul.com` Domain property accessible; no extra verification tag needed for this subdomain in that property.
- [ ] If a separate URL-prefix property is preferred, add `https://silentzone.nirajpaul.com/` and complete Google's offered verification method. Never publish secret credentials; do not remove a verification record while ownership relies on it.
- [ ] Submit **https://silentzone.nirajpaul.com/sitemap.xml** in Sitemaps. The inspected Domain property's Submitted sitemaps table was empty. Confirm status Success and one discovered canonical URL after processing.
- [ ] Inspect the exact HTTPS homepage; check Google's selected canonical and last crawl. After deployment run Test live URL, then Request indexing once if appropriate. Submission does not guarantee indexing or ranking.
- [ ] Watch Page indexing, HTTPS and Core Web Vitals reports; investigate real library URLs rather than unrelated domain pages. Do not repeatedly submit unchanged URLs.
- [ ] Save periodic filtered exports with date, page, query, country, device, CTR and position. Preserve filters and date windows for comparisons; annotate this release date. Keep underlying account exports out of a public repository.

## 30/60/90-day roadmap

| Period | Work | Evidence to review |
|---|---|---|
| Days 1–30 | Deploy and validate; fix HTTPS redirect; submit sitemap; confirm GBP facts/category/pin/hours; add permitted real photos; make enquiry handling reliable | URL inspection/canonical, sitemap status, failed links, mobile lab results, baseline filtered Search Console and genuine enquiries |
| Days 31–60 | Compare matched 28-day periods; examine Samastipur and branded query/device performance; answer recurring real student questions on this page; collect honest reviews; integrate consent-based analytics only if chosen | Impressions, clicks, CTR and position together; separate mobile and desktop; record click intents separately from enquiries |
| Days 61–90 | Reassess after enough data; refine only demonstrably unclear snippets/content; update accurate photos/facilities/hours; pursue legitimate local mentions from relevant organizations | Trends with sample sizes and seasonality, actual membership enquiries, Maps actions, field CWV if available |

Avoid ranking guarantees, fake review campaigns, bought spam links, keyword stuffing and duplicate neighborhood pages. The goal is useful local relevance and student enquiries, not a fabricated score.

## Official guidance

- [Google title-link guidance](https://developers.google.com/search/docs/appearance/title-link)
- [Google LocalBusiness structured data](https://developers.google.com/search/docs/appearance/structured-data/local-business)
- [Getting started with Search Console](https://developers.google.com/search/docs/monitor-debug/search-console-start)
- [How local Google ranking works](https://support.google.com/business/answer/7091?hl=en)
- [Core Web Vitals definitions](https://web.dev/articles/vitals)
- [Cloudflare HTTPS redirects](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/always-use-https/)

## Release completion evidence

Pending release verification; update with observed results rather than assumed success.
