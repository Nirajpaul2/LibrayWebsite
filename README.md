# Silent Zone Self Study Library

A responsive, static website for students, built with HTML and CSS. No database, accounts or administration interface.

## Preview

Run `python3 -m http.server 4173 --bind 127.0.0.1 --directory dist`, then open http://127.0.0.1:4173.

## Content

Edit `dist/index.html` for photos, facilities, contact information and map location. Edit `dist/style.css` for colors and layout.

The phone number, map coordinates, address, opening-hours label and photos were verified against the supplied Google Maps listing on 9 October 2026. Facility descriptions come from the library owner's reception banner. Photos are linked to the owner's Google-hosted images and are attributed on the page; they have no verified open license. The map and fonts use external Google services. No fees, reviews, capacity or membership availability are invented.

Membership links initiate a phone call; they do not submit an application or reserve a seat. Navigation links jump to page sections. Gallery links open full-size photos.

## Hosting

Sites identity and static asset directory are in `.openai/hosting.json`. The site starts private; make it public through Sites sharing when ready for visitors.
