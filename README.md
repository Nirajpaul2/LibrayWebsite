# LibrayWebsite — Silent Zone Self Study Library

A responsive, static website for students, built with HTML and CSS. No database, accounts or administration interface.

## Preview

Run `python3 -m http.server 4173 --bind 127.0.0.1 --directory dist`, then open http://127.0.0.1:4173.

## Content

Edit `dist/index.html` for photos, facilities, contact information and map location. Edit `dist/style.css` for colors and layout.

The phone number, map coordinates, address, opening-hours label and photos were verified against the supplied Google Maps listing on 9 October 2026. Facility descriptions come from the library owner's reception banner. Photos are linked to the owner's Google-hosted images and are attributed on the page; they have no verified open license. The map and fonts use external Google services. No fees, reviews, capacity or membership availability are invented.

Enquiry links open WhatsApp with a prepared message or initiate a phone call; they do not send a message automatically, submit an application, or reserve a seat. Navigation links jump to page sections. Gallery links open full-size photos.

## Hosting

Sites identity and static asset directory are in `.openai/hosting.json`. The site starts private; make it public through Sites sharing when ready for visitors.

The additional wide study-space photo is supplied by the user and hosted at `dist/images/library.jpg`.

The user-supplied logo is preserved at `dist/images/logo.png` and used in the header and favicon.

Opening hours are corrected by the owner to 6 AM–10 PM. Four study batches run 6–10 AM, 10 AM–2 PM, 2–6 PM, and 6–10 PM. These supersede the earlier Maps hours.

The owner confirmed all four membership fees are monthly: ₹350, ₹550, ₹750 and ₹950.
