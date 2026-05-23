# Barto Appliance — Site Rebuild

**Client:** Barto Appliance · 3833 Airline Drive, Metairie, LA 70001  
**Agency:** St. Expedite Press  
**Stack:** Next.js · Drizzle ORM · Postgres · Tailwind CSS  
**Hosting:** Replit Reserved VM → bartoappliances.com  

---

## Project Overview

Barto Appliance has operated in Greater New Orleans since 1947. Their current site runs on Tailbase/ColdFusion — a legacy SaaS platform with no custom development path. This rebuild replaces it with a full custom Next.js application designed to convert local search traffic into phone calls and showroom visits.

**Key business context:**
- 2,000+ appliances in stock across all major categories
- 15 major brands including Speed Queen, Whirlpool, KitchenAid, Maytag
- Serves Metairie, New Orleans, Kenner, Jefferson Parish, and Greater New Orleans
- Primary CTA is always a phone call: **(504) 831-2734**
- Competitive differentiator: local expertise, older home installation experience, same-week delivery

---

## Phase 1 — Audit (Complete)

Full audit of the live site before any design work began.

**What we audited:**

| Page | Findings |
|------|----------|
| Homepage | No address, no hours, hero is generic, no local identity signal |
| Refrigerators (204 models) | Strong product data; no stock status, no delivery info on cards |
| Clearance | Good inventory concept; "Contact Us For Price" is a dead end |
| Contact | Address buried, no map embed, no hours table |
| Brands | Logo dump — no positioning copy, no differentiation |
| About | Thin, no local voice, no review integration |

**11 conversion gaps documented** → [`audit/conversion-gaps.md`](audit/conversion-gaps.md)

### Current Live Site

![Barto Appliance — current live site](audit/screens/home/live-site-current.png)

**Critical gaps on the current site:**
- No address or hours visible in header or footer
- "Contact Us For Price" clicks open a contact form — no phone number shown inline
- No stock status on product cards
- No local identity ("Since 1947", service area, installer story)
- No schema markup (LocalBusiness, Product, BreadcrumbList)
- No Google review integration
- Mobile: no sticky phone CTA

---

## Phase 2 — Design System (Complete)

**Brand palette (locked):**

| Token | Value | Role |
|-------|-------|------|
| `--teal` | `#004A6E` | Header, nav, structural dark |
| `--orange` | `#E8871A` | Primary CTAs |
| `--amber` | `#FFC20E` | Phone number, accent highlights |
| `--red` | `#C8321E` | Clearance, sale pricing |
| `--cream` | `#FAF7F2` | Body background |

**Typography:**
- UI + body: **DM Sans** (all weights)
- Heritage callouts only: **Playfair Display** italic ("Since 1947", pull quotes)

**Real logo integrated** from bartoappliances.com across all designs.

---

### Five Design Variants

All variants share the same brand palette, conversion logic, and content structure. They differ in layout composition and how the palette is applied.

---

#### Variant A — Teal Split Hero *(Recommended)*
`audit/designs/barto-homepage.html`

Split composition: dark teal left panel with headline, phone, and CTAs — kitchen photo fills the right. Strong local authority feel, fast visual hierarchy.

![Variant A — Teal Split Hero](audit/designs/screenshots/variant-a-split-hero.png)

---

#### Variant B — Teal Full-Width Hero
`audit/designs/variant-b-navy-brass.html`

Immersive full-width kitchen photo with teal overlay. Amber stat highlights (2,000+ / since 1947 / 15 brands). Horizontal category strip below hero. Most expansive and commercial feel.

![Variant B — Teal Full-Width](audit/designs/screenshots/variant-b-fullwidth.png)

---

#### Variant C — Teal Inverted Split
`audit/designs/variant-c-slate-rust.html`

Flipped composition: cream/light left panel with headline + proof points, teal right panel with kitchen photo. Bold, high-contrast application of the brand palette.

![Variant C — Teal Inverted Split](audit/designs/screenshots/variant-c-inverted-split.png)

---

#### Variant D — Editorial White + Teal
`audit/designs/variant-d-editorial-white.html`

Newspaper-editorial layout: 80px headline on the left, phone call block + Louis David review quote on the right. White-first design with teal as a structural accent. Most minimal and modern.

![Variant D — Editorial White](audit/designs/screenshots/variant-d-editorial.png)

---

#### Variant E — Brand True *(Most Expressive)*
`audit/designs/variant-e-brand-true.html`

The brand palette applied at full intensity: teal split hero with diagonal chevron cut, amber stat strip, orange delivery band. Closest to Barto's existing identity, fully modernized.

![Variant E — Brand True](audit/designs/screenshots/variant-e-brand-true.png)

---

### Supporting Pages

Both supporting pages use the shared brand palette and component system established in the homepage variants.

#### Category / Listing Page
`audit/designs/barto-category.html`

Filter drawer with 12 dimensions (type, brand, width, color, features, price, etc.). Product cards with stock chip, delivery note, rebate badge. "Request Availability" CTA on every card.

![Category Page](audit/designs/screenshots/page-category.png)

---

#### Product Detail Page
`audit/designs/barto-product-detail.html`

Full spec table, stock status, delivery options, "Price By Phone" call block, inquiry form trigger. Schema markup ready for LocalBusiness + Product structured data.

![Product Detail Page](audit/designs/screenshots/page-product-detail.png)

---

### Design System Documentation

`audit/designs/design-system-docs.html`

Full documentation package: all 5 variant swatches, shared token set, typography specimens, component library, conversion gap status, and implementation guidance for Phase 3.

---

## Phase 3 — Next.js Build (Pending)

The production site. Modular monolith. Replit-deployable from day one.

### Technology Stack

| Layer | Choice | Reason |
|-------|--------|--------|
| Framework | Next.js 14 (App Router) | SSR for SEO, file-based routing, image optimization |
| Database | Postgres + Drizzle ORM | Type-safe schema, easy migrations |
| Styling | Tailwind CSS | Design tokens map directly from Phase 2 |
| Email | Resend or SendGrid | Transactional lead alerts |
| Storage | Cloudflare R2 | Clearance item photos |
| Hosting | Replit Reserved VM | Fast deployment, no DevOps overhead |

### Page Routes

| Route | Priority | Description |
|-------|----------|-------------|
| `/` | P1 | Homepage (Variant A or E layout) |
| `/categories/[slug]` | P1 | Category listing with 12-dimension filter |
| `/products/[id]` | P1 | Product detail with inquiry modal |
| `/clearance` | P1 | Clearance center with admin toggle |
| `/contact` | P1 | Address, hours, map embed, contact form |
| `/about` | P1 | Rewritten with local voice and 1947 story |
| `/brands/[slug]` | P2 | Brand pages with positioning copy |
| `/rebates` | P2 | Active rebates with brand filter |
| `/financing` | P2 | Wells Fargo + Acima explained |
| `/reviews` | P2 | Curated reviews + links to write |
| `/admin` | P2 | Inventory editor, clearance manager, leads inbox |
| `/older-homes` | P3 | SEO: older New Orleans homes |
| `/room-air-conditioners` | P3 | SEO: room AC Metairie |
| `/rental-property` | P3 | SEO: landlord replacement appliances |
| `/clearance-scratch-dent` | P3 | SEO: clearance Metairie |
| `/same-week-delivery` | P3 | SEO: fast delivery New Orleans |

### Conversion Fixes Built In

Every gap from the Phase 1 audit is addressed in the design and will be implemented in Phase 3:

| Gap (current site) | Fix (new site) |
|---------------------|----------------|
| No local identity on entry | Hero with address, phone, "since 1947" above the fold |
| "Contact Us For Price" dead end | `InquiryModal` pre-fills model/brand, `tel:` link on every product |
| No address/hours anywhere | `LocalTrustBar` component in header and footer |
| Mobile: no phone CTA | Sticky mobile header: [Call] [Directions] [Clearance] [Search] |
| No stock status on cards | Stock chip + delivery note on every `ProductCard` |
| Reviews siloed to one page | `ReviewPullQuote` on homepage, washer/dryer page, older-homes page |
| Brand pages are logo dumps | Brand tiles with positioning copy and top models |
| No schema markup | `LocalBusiness` + `Product` + `BreadcrumbList` on every page |
| Empty meta descriptions | SEO helper generates per-product and per-category meta |

### Key Components

```
components/
  LocalTrustBar.tsx     — address, phone, hours, service area
  ProductCard.tsx       — stock chip, delivery note, rebate badge, 3 CTAs
  FilterDrawer.tsx      — sticky mobile drawer, 12 filter dimensions
  InquiryModal.tsx      — pre-fills model/brand, captures ZIP + phone
  ClearanceCard.tsx     — condition grade, "only 1 available", call CTA
  ReviewPullQuote.tsx   — Louis David quote, site-wide placement
  PhoneCTA.tsx          — tel: link, sticky mobile header
  SpecTable.tsx         — full manufacturer spec table
```

### Database Schema

```
products          — manufacturer catalog data (refreshable via import)
local_inventory   — Barto-specific flags (in_stock, clearance, call_for_price)
brands            — brand name, logo, positioning copy
categories        — kitchen, laundry, AC, clearance
rebates           — title, brand, dates, PDF link
leads             — inquiry form submissions
reviews           — curated review excerpts
admin_users       — staff logins
```

**Schema rule:** Manufacturer data (`products`) is refreshable via CSV import and never overwrites local judgment (`local_inventory`). Stock status, clearance flags, and pricing notes are always Barto-controlled.

---

## Phase 4 — Enhanced Features (Post-Launch)

| Feature | Description |
|---------|-------------|
| SMS lead alerts | Twilio — staff gets a text the moment a lead comes in |
| Google review ingestion | Pull new reviews automatically |
| Advanced search | Meilisearch or Algolia for instant filtering |
| Simple CRM | Pipeline view: new → contacted → quoted → won/lost |
| Online deposits | For clearance items (prevent no-shows) |
| Google Merchant Center | Product feed for Shopping ads |
| Financing prequalification | Wells Fargo iframe integration |
| Inventory sync | POS → database sync |

---

## Business Data Reference

```
Name:     Barto Appliance
Address:  3833 Airline Drive, Metairie, LA 70001
Phone:    (504) 831-2734
Hours:    Mon–Fri 9:30 AM–6:00 PM (Fri closes 5:30 PM)
          Sat 10:00 AM–3:00 PM · Sun Closed
Geo:      29.9756398, -90.1685747
Since:    1947
Stock:    2,000+ appliances and air conditioners
Areas:    Metairie · New Orleans · Kenner · Jefferson Parish · Greater New Orleans
```

**Brands:** Amana · Avanti · Comfort-Aire · Electrolux · Frigidaire · Frigidaire Gallery · Frigidaire Professional · KitchenAid · Maytag · Maytag Commercial Laundry · Sharp · Speed Queen · Thor Kitchen · Vitara · Whirlpool

**Hero review (used site-wide):**
> "After a terrible experience with getting an unnamed big box store to install a washer/dryer upstairs in an older home, I called Barto and Terri took care of it all! I bought the washer dryer over the phone, and she connected me with a specialty installer."
> — Louis David, March 2024 · Google Review

---

*Built by [St. Expedite Press](https://github.com/St-Expedite-Press)*
