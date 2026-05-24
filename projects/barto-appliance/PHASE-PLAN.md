# Barto Appliance Rebuild — Phase Plan

**Site:** bartoappliances.com  
**Stack:** Next.js · Drizzle · Postgres · Tailwind  
**Hosting target:** Replit Reserved VM → custom domain  
**Last updated:** 2026-05-23

---

## Phase 1 — Audit ✅ COMPLETE

Full audit of the live site (Tailbase/ColdFusion platform).

| Task | Status |
|------|--------|
| Screenshot all live pages | ✅ Done |
| Content inventory | ✅ Done → `audit/content-inventory.md` |
| Conversion gap analysis | ✅ Done → `audit/conversion-gaps.md` |
| Design token extraction | ✅ Done → `audit/design-inventory.md` |
| 11 conversion gaps documented | ✅ Done |

**Key findings:**
- Platform is Tailbase (ColdFusion SaaS) — full custom rebuild required
- 204 refrigerators, full filter taxonomy, strong product data — keep structure
- Fatal gaps: no address/hours in header/footer, no local identity, no schema markup, no stock status on cards, "Contact Us For Price" is a dead end
- Best asset: Louis David Google Review (older home washer/dryer install, phone purchase) — use site-wide
- Typography: Roboto Condensed only, orange+teal palette — scrap both

---

## Phase 2 — Design System ✅ COMPLETE (Expanded 2026-05-23)

10 visual variants + comprehensive design directory + documentation package.

### Phase 2 Original — 5 Variants + Supporting Pages

| Task | Status |
|------|--------|
| Variant A: Teal Split / Cream (split hero, dark teal left panel) | ✅ Done → `audit/designs/barto-homepage.html` |
| Variant B: Teal Full-Width / Amber (centered full-width hero, amber stat accents) | ✅ Done → `audit/designs/variant-b-navy-brass.html` |
| Variant C: Teal Contrast / Orange (inverted split, cream left + teal right) | ✅ Done → `audit/designs/variant-c-slate-rust.html` |
| Variant D: Editorial White / Teal Accents (newspaper layout, white body) | ✅ Done → `audit/designs/variant-d-editorial-white.html` |
| **Variant E: Brand True — their actual teal+orange palette, enhanced** | ✅ Done → `audit/designs/variant-e-brand-true.html` |
| Category page design | ✅ Done → `audit/designs/barto-category.html` |
| Product detail page design | ✅ Done → `audit/designs/barto-product-detail.html` |
| Stock photo integration (Unsplash CDN) | ✅ Done → `audit/designs/images/` |
| Real logo download + integration into all 7 designs | ✅ Done → `audit/designs/images/barto-logo.png` |
| Brand alignment across all 7 designs | ✅ Done → `audit/scripts/brand_align.py` |
| Design system documentation | ✅ Done → `audit/designs/design-system-docs.html` |

### Phase 2 Expansion — 5 New Variants + Design Directory

| Task | Status |
|------|--------|
| **Variant F: Dark Showroom Luxury** — charcoal body, amber glow, glassmorphism | ✅ Done → `audit/designs/variant-f-dark-luxury.html` |
| **Variant G: New Orleans Heritage Editorial** — Playfair dominant, newspaper masthead, ink-teal | ✅ Done → `audit/designs/variant-g-heritage-editorial.html` |
| **Variant H: Bento Grid Modern** — pure white, asymmetric bento grid, oversized DM Sans 900 | ✅ Done → `audit/designs/variant-h-bento-modern.html` |
| **Variant I: Bold American Signage** — Inter Black 900 UPPERCASE, no gradients, sharp storefront feel | ✅ Done → `audit/designs/variant-i-bold-signage.html` |
| **Variant J: Gulf Coast Coastal Premium** — warm linen, pill trust chips, rounded cards, Playfair | ✅ Done → `audit/designs/variant-j-coastal-premium.html` |
| Comprehensive design directory (full element inventory, logo brief, modernization guide) | ✅ Done → `audit/design-directory.md` |
| Industry sector research & competitive analysis | ✅ Done → session context |

**Design decisions locked:**
- Typography: DM Sans (all UI) + Playfair Display italic (heritage callouts only)
- **All 10 variants share the Barto brand palette**: Teal `#004A6E` · Orange `#E8871A` · Amber `#FFC20E` · Red `#C8321E`
- Variants differ by: body color, layout structure, typographic scale, border radius system, section divider style
- Layout: Variant A (safe/polished) · Variant F (premium) · Variant H (modern 2026) · Variant I (boldest) · Variant J (warmest)
- All 10 variants are production-ready HTML mockups with real logo and stock photos

**Variant selection guide:**
- Premium/luxury positioning → **F: Dark Luxury**
- Heritage/New Orleans identity lead → **G: Heritage Editorial**
- Modern/forward-thinking → **H: Bento Modern**
- Bold/authoritative → **I: Bold Signage**
- Warm/local/approachable → **J: Coastal Premium**
- Safe client presentation → **E: Brand True** or **A: Teal Split**

**Images available** (`audit/designs/images/`):
- `hero-kitchen-wide.jpg` — primary dark hero (New Orleans kitchen feel)
- `hero-kitchen-light.jpg` — editorial/bright hero
- `product-french-door.jpg` — vintage teal refrigerator
- `product-washer.jpg` — styled laundry room
- `product-topload-washer.jpg` — commercial dryers (Speed Queen context)
- `lifestyle-kitchen.jpg` — couple cooking (lifestyle use)

---

## Phase 3 — Next.js Scaffold ⏳ PENDING

Build the production site. Modular monolith. Replit-deployable.

### 3A — Project Setup

| Task | Status |
|------|--------|
| `npx create-next-app barto-site` with TypeScript + Tailwind | ⏳ Pending |
| Configure Drizzle ORM + Postgres connection | ⏳ Pending |
| Set up environment variables (.env.local) | ⏳ Pending |
| Configure Tailwind design tokens from design system | ⏳ Pending |
| Set up path aliases and folder structure | ⏳ Pending |

**Target folder structure:**
```
barto-site/
  app/
    page.tsx                  # Homepage
    products/
    categories/[slug]/
    brands/[slug]/
    clearance/
    rebates/
    financing/
    about/
    contact/
    admin/
    api/
  components/
    LocalTrustBar.tsx
    ProductCard.tsx
    CategoryTile.tsx
    BrandTile.tsx
    ClearanceCard.tsx
    ReviewPullQuote.tsx
    PhoneCTA.tsx
    FilterDrawer.tsx
    InquiryModal.tsx
    SpecTable.tsx
  lib/
    db.ts
    auth.ts
    search.ts
    productImport.ts
    email.ts
    seo.ts
  drizzle/
    schema.ts
    migrations/
  scripts/
    import-products.ts
    seed.ts
```

### 3B — Database Schema (Drizzle + Postgres)

| Table | Status |
|-------|--------|
| `products` — manufacturer catalog data | ⏳ Pending |
| `local_inventory` — Barto-specific flags (in_stock, clearance, call_for_price, etc.) | ⏳ Pending |
| `brands` — brand name, logo, positioning copy | ⏳ Pending |
| `categories` — kitchen, laundry, AC, clearance | ⏳ Pending |
| `rebates` — title, brand, dates, PDF link, applicable products | ⏳ Pending |
| `leads` — inquiry form submissions (model, ZIP, phone, delivery need) | ⏳ Pending |
| `reviews` — curated review excerpts with permission flag | ⏳ Pending |
| `content_pages` — editable local landing pages | ⏳ Pending |
| `admin_users` — staff logins | ⏳ Pending |

**Schema design rule:** Manufacturer data (`products`) is refreshable via import. Local judgment (`local_inventory`) is never overwritten by imports. Keep them separate.

### 3C — Core Components

| Component | Status |
|-----------|--------|
| `LocalTrustBar` — address, phone, hours, service area | ⏳ Pending |
| `ProductCard` — stock chip, delivery note, rebate badge, 3 CTAs | ⏳ Pending |
| `FilterDrawer` — sticky mobile drawer, 12 filter dimensions | ⏳ Pending |
| `InquiryModal` — pre-fills model/brand, captures ZIP + phone + delivery | ⏳ Pending |
| `ClearanceCard` — condition grade, "only 1 available", call CTA | ⏳ Pending |
| `ReviewPullQuote` — Louis David quote, site-wide placement | ⏳ Pending |
| `PhoneCTA` — tel: link, sticky mobile header | ⏳ Pending |
| `SpecTable` — full manufacturer spec table | ⏳ Pending |

### 3D — Page Routes

| Route | Priority | Status |
|-------|----------|--------|
| `/` — Homepage (Variant A or D layout) | P1 | ⏳ Pending |
| `/categories/[slug]` — Category listing with filters | P1 | ⏳ Pending |
| `/products/[id]` — Product detail with inquiry modal | P1 | ⏳ Pending |
| `/clearance` — Clearance center with admin toggle | P1 | ⏳ Pending |
| `/contact` — Address, hours, map, form | P1 | ⏳ Pending |
| `/about` — Rewritten with local voice | P1 | ⏳ Pending |
| `/brands/[slug]` — Brand page with positioning copy | P2 | ⏳ Pending |
| `/rebates` — Active rebates with brand filter | P2 | ⏳ Pending |
| `/financing` — Wells Fargo + Acima explained | P2 | ⏳ Pending |
| `/reviews` — Curated reviews + links to write | P2 | ⏳ Pending |
| `/admin` — Inventory editor, clearance manager, leads inbox | P2 | ⏳ Pending |
| `/older-homes` — SEO landing: older New Orleans homes | P3 | ⏳ Pending |
| `/room-air-conditioners` — SEO: room AC Metairie | P3 | ⏳ Pending |
| `/rental-property` — SEO: landlord replacement | P3 | ⏳ Pending |
| `/clearance-scratch-dent` — SEO: clearance Metairie | P3 | ⏳ Pending |
| `/same-week-delivery` — SEO: fast delivery | P3 | ⏳ Pending |

### 3E — Conversion Fixes (from Phase 1 gaps)

| Gap | Fix | Status |
|-----|-----|--------|
| No local identity on entry | Hero with address + phone + "since 1947" | ⏳ Pending |
| "Contact Us For Price" dead end | `InquiryModal` pre-fills model, tel: link on every product | ⏳ Pending |
| No address/hours in footer | `LocalTrustBar` in footer | ⏳ Pending |
| Mobile phone-first header | Sticky: [Call] [Directions] [Clearance] [Search] | ⏳ Pending |
| No stock status on cards | Stock chip + delivery note on every `ProductCard` | ⏳ Pending |
| Reviews siloed | `ReviewPullQuote` on homepage, washer/dryer page, older-homes page | ⏳ Pending |
| Brand page is logo dump | Brand tiles with positioning copy | ⏳ Pending |
| No schema markup | `LocalBusiness` + `Product` + `BreadcrumbList` on every page | ⏳ Pending |
| Empty meta descriptions | SEO helper generates per-product and per-category meta | ⏳ Pending |

### 3F — Infrastructure

| Task | Status |
|------|--------|
| CSV/feed product import script | ⏳ Pending |
| Transactional email for leads (Resend or SendGrid) | ⏳ Pending |
| External object storage for clearance photos (Cloudflare R2 or S3) | ⏳ Pending |
| Replit Reserved VM deployment config | ⏳ Pending |
| Custom domain: www.bartoappliances.com | ⏳ Pending |

---

## Phase 4 — Enhanced Features (Post-Launch)

| Feature | Status |
|---------|--------|
| SMS lead alerts (Twilio) | ⏳ Future |
| Google Business review ingestion | ⏳ Future |
| Better search (Meilisearch or Algolia) | ⏳ Future |
| CSV import UI in admin | ⏳ Future |
| Delivery ZIP rules engine | ⏳ Future |
| Staff picks system | ⏳ Future |
| Product comparison tool | ⏳ Future |
| Simple CRM pipeline (new/contacted/quoted/won/lost) | ⏳ Future |
| Online deposits for clearance items | ⏳ Future |
| Financing prequalification integration | ⏳ Future |
| Google Merchant Center feed | ⏳ Future |
| Inventory sync with POS | ⏳ Future |

---

## Key Business Data (locked from audit)

```
Name:     Barto Appliance
Address:  3833 Airline Drive, Metairie, LA 70001
Phone:    (504) 831-2734
Hours:    Mon–Fri 9:30 AM – 6:00 PM (Fri closes 5:30 PM) · Sat 10:00 AM – 3:00 PM · Sun Closed
Geo:      29.9756398, -90.1685747
Since:    1947
Stock:    2,000+ appliances and air conditioners
Areas:    Metairie · New Orleans · Kenner · Jefferson Parish · Greater New Orleans
Social:   facebook.com/Barto-Appliance-326384047514670 · twitter.com/bartoappliance
```

**Brands carried:** Amana · Avanti · Comfort-Aire · Electrolux · Frigidaire · Frigidaire Gallery · Frigidaire Professional · KitchenAid · Maytag · Maytag Commercial Laundry · Sharp · Speed Queen · Thor Kitchen · Vitara · Whirlpool

**Hero review (use site-wide):**
> "After a terrible experience with getting an unnamed big box store to install a washer/dryer upstairs in an older home, I called Barto and Terri took care of it all! I bought the washer dryer over the phone, and she connected me with a specialty installer."
> — Louis David, March 2024 · Google Review
