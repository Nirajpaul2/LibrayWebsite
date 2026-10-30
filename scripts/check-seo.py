"""Validate homepage SEO invariants, linked assets and unchanged regular prices."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse, parse_qs
from urllib.robotparser import RobotFileParser
import json, re, xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1] / 'dist'
ORIGIN = 'https://silentzone.nirajpaul.com/'
class Page(HTMLParser):
    def __init__(self):
        super().__init__(); self.tags=[]; self.ids=[]; self.schema=[]; self.in_schema=False; self.h1=0
    def handle_starttag(self, tag, attrs):
        a=dict(attrs); self.tags.append((tag,a))
        if 'id' in a: self.ids.append(a['id'])
        if tag=='h1': self.h1+=1
        if tag=='script' and a.get('type')=='application/ld+json': self.in_schema=True
    def handle_endtag(self, tag):
        if tag=='script': self.in_schema=False
    def handle_data(self, data):
        if self.in_schema: self.schema.append(data)
html=(ROOT/'index.html').read_text(); page=Page(); page.feed(html)
assert '<title>Silent Zone Library Samastipur | AC Self Study Library</title>' in html
meta={a.get('name',a.get('property')):a.get('content') for t,a in page.tags if t=='meta'}
assert meta['description']==meta['og:description']==meta['twitter:description']
assert meta['og:title']==meta['twitter:title']=='Silent Zone Library Samastipur | AC Self Study Library'
assert meta['og:image']==meta['twitter:image']==ORIGIN+'images/library-1200.webp'
assert meta['twitter:card']=='summary_large_image'
assert meta['og:image:alt'] and meta['twitter:image:alt']
levels=[int(t[1]) for t,a in page.tags if re.fullmatch('h[1-6]',t)]
assert all(b<=a+1 for a,b in zip(levels,levels[1:])), 'Heading hierarchy skips a level'
assert page.h1==1 and len(page.ids)==len(set(page.ids))
assert [a['href'] for t,a in page.tags if t=='link' and a.get('rel')=='canonical']==[ORIGIN]
for tag,a in page.tags:
    if tag=='meta' and a.get('name','').lower() in ('robots','googlebot'):
        assert not {'noindex','nofollow','none'} & set(re.split(r'[,\s]+',a.get('content','').lower()))
    if tag=='img':
        assert a.get('alt') and int(a['width'])>0 and int(a['height'])>0
        assert a.get('srcset') and a.get('sizes')
        for candidate in a['srcset'].split(','): assert (ROOT/candidate.strip().split()[0].lstrip('/')).is_file()
        if a.get('class')=='hero-image': assert a.get('loading')!='lazy' and a.get('fetchpriority')=='high'
    if tag=='iframe': assert a.get('title') and a.get('loading')=='lazy'
    if tag=='a' and a.get('href','').startswith(('tel:', 'https://wa.me/', 'https://www.google.com/maps/dir/')):
        assert a.get('data-contact-action') in ('phone','whatsapp','directions')
        assert a.get('data-membership-plan') in ('none','single','double','triple','full')
    if tag=='a' and a.get('href','').startswith('#'): assert a['href'][1:] in page.ids
    for key in ('href','src'):
        value=a.get(key,'')
        if value.startswith('/') and not value.startswith('//'): assert (ROOT/value.lstrip('/')).is_file(),value
    if tag=='a' and a.get('href','').startswith('https://wa.me/'):
        url=urlparse(a['href']); assert url.path=='/919942419837'; assert parse_qs(url.query).get('text')
data=json.loads(''.join(page.schema))
assert data['@type']=='LocalBusiness' and data['name']=='Silent Zone Self Study Library'
assert data['url']==ORIGIN and data['telephone']=='+919942419837'
assert data['geo']['latitude']==25.859534 and data['geo']['longitude']==85.7654646
assert data['image'] and all((ROOT/u.removeprefix(ORIGIN)).is_file() for u in data['image'])
assert data['address']=={'@type':'PostalAddress','streetAddress':'Ward No. 4, Sonbersa Chowk, Musa Pur','addressLocality':'Samastipur','addressRegion':'Bihar','postalCode':'848103','addressCountry':'IN'}
assert data['openingHoursSpecification'][0]['opens']=='06:00' and data['openingHoursSpecification'][0]['closes']=='22:00'
assert len(data['openingHoursSpecification'][0]['dayOfWeek'])==7
assert '0xd26c0da7412aeed1' in data['hasMap']
assert not {'review','aggregateRating','award'} & data.keys()
assert [int(x) for x in re.findall(r'class="membership-price">₹(\d+)',html)]==[350,550,750,950]
assert html.count('class="price-period"')==4
assert 'Open 24 hours' not in html
urls=ET.parse(ROOT/'sitemap.xml').findall('{http://www.sitemaps.org/schemas/sitemap/0.9}url/{http://www.sitemaps.org/schemas/sitemap/0.9}loc')
assert [u.text for u in urls]==[ORIGIN]
robot=RobotFileParser();robot.parse((ROOT/'robots.txt').read_text().splitlines())
assert robot.can_fetch('Googlebot',ORIGIN) and robot.can_fetch('Googlebot-Image',ORIGIN+'images/hero-1200.webp')
assert robot.site_maps()==[ORIGIN+'sitemap.xml']
print('PASS: canonical, crawl directives, XML sitemap, JSON-LD identity/hours/maps, regular prices, headings, anchors, WhatsApp links and local image variants.')
