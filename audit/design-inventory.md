# Barto Appliance — Design Inventory
Audited: 2026-05-22 | Source: bartoappliances.com (Tailbase platform)

---

## Current Design Tokens

### Colors (extracted via Firecrawl branding scan)

| Token | Hex | Role |
|-------|-----|------|
| Primary | `#FF0000` | Detected as "primary" — likely sale/badge red |
| Secondary / Accent | `#F7941D` | Orange — primary CTA button background, "Subscribe" |
| Background | `#FFFFFF` | Page background (pure white) |
| Text Primary | `#00486E` | Dark teal/navy — body text, links, secondary button bg |
| Nav button text | `#FFC20E` | Yellow — text on dark teal secondary button ("Clearance Center") |
| Input background | `#FFFFFF` | Form inputs |
| Input text | `#555555` | Form input placeholder/text |

**Observed additional colors (from screenshots):**
- Logo background: dark navy/teal (`#003A5E` approx)
- Page background: light gray (`#F5F5F5` approx) behind content panels
- Product card border: light gray
- Discount/sale badge: red-orange

### Typography

| Role | Family | Stack |
|------|--------|-------|
| Heading | Roboto Condensed | `"Roboto Condensed", "Arial Narrow", sans-serif` |
| Body | Roboto Condensed | same — no separate body font |
| No serif typeface in use |

**Font sizes:**
- H1: 24px
- H2: 17.6px
- Body: 18.72px

**Weight:** Condensed sans-serif throughout. No serif for heritage, no geometric grotesque, no editorial voice.

### Spacing + Geometry

- Base unit: 4px
- Border radius (cards): 5px
- Border radius (buttons): 0px — sharp rectangular corners
- No shadows on buttons or inputs

### Component Styles

**Primary CTA button:** orange (`#F7941D`) bg, white text, 0px radius (flat rectangle)
**Secondary button:** dark teal (`#00486E`) bg, yellow (`#FFC20E`) text — used for "Clearance Center" nav button
**Links:** dark teal (`#00486E`)
**Product card:** white bg, gray border, logo at bottom, model + description + "Contact Us For Price" text + "Price Request" orange button

---

## Layout Structure

### Global
- Fixed-width layout (~1000px max)
- Two-column on desktop: left nav/filter sidebar + right content
- Single column on mobile (untested — site uses `width=device-width, initial-scale=1.0, maximum-scale=1.0, minimal-ui`)
- `maximum-scale=1.0` prevents user zoom — accessibility issue

### Header
- Very top bar: phone number left, "About Us | Contact Us" links right (small, easy to miss)
- Logo center-left
- Search bar right of logo
- Primary nav below logo: Products | Brands | Rebates | Financing | Reviews
- "Clearance Center" button isolated far right of primary nav

### Homepage Layout
1. Hero slideshow (full width, left ~70%)
2. Featured Product sidebar (right ~30%) — static, manually chosen
3. Below-fold: Whirlpool banner | Scratch-N-Dent box | Mailing list | Financing widget
4. Footer (logo only, 3 links)

### Category Page Layout
- Left sidebar: all filter dimensions stacked vertically
- Right main: product grid (12 per page default), sort/display controls, pagination
- No sticky filters
- Filters collapse to hamburger "Filters" on mobile

### Product Detail Layout
- Left: image gallery (main + thumbnails)
- Right: model number, description, CTA block, brand logo, document links, "Ask an Expert"
- Below: full spec table
- No related products, no stock status, no delivery info

### Contact Page
- Full-width Google Static Map at top
- Address + hours block
- Contact form below

---

## What the Current Design Is

A vendor-template appliance catalog from Tailbase (ColdFusion). The design looks like approximately 2010–2015 appliance retail UI:
- Condensed fonts everywhere for space efficiency
- Orange+teal+white color palette (generic "deal retail")
- Heavy on product data, thin on brand/place identity
- No photography of the actual store, staff, or New Orleans context
- No editorial hierarchy — the page doesn't guide the eye toward anything
- Logo is dark navy with "Barto Appliance" in a blocky script — serviceable but not distinctive
- "They Don't Make 'Em Like They Used To. We Do." hero copy is actually good — but it's delivered as a photo overlay with no follow-through

---

## What to Keep

| Element | Keep | Reason |
|---------|------|--------|
| Product data structure | Yes | Full spec tables, filter dimensions, PDFs — strong foundation |
| Filter taxonomy | Yes | 12 filter dimensions on refrigerators is actually good |
| Rebate integration | Yes | Active rebates properly attached to products |
| Product image feeds | Yes | Tailbase image CDN works fine |
| Phone number in header | Yes | Right priority placement |
| "Clearance Center" as distinct button | Yes | Good visual separation, right instinct |
| Mailing list widget | Yes | Keep, redesign |
| Speed Queen partnership | Yes | Shows brand relationships worth highlighting |

---

## What to Scrap

| Element | Scrap | Reason |
|---------|-------|--------|
| Condensed font only | Yes | No typographic personality or hierarchy |
| Orange+red primary palette | Yes | Generic deal-retail, no local identity |
| Pure white background | Yes | No warmth, no texture, no Barto character |
| Static featured product sidebar | Yes | Not dynamic, not useful for most visitors |
| Whirlpool banner ads in homepage body | Yes | Vendor ad placement — dilutes Barto's voice |
| Generic hero slideshow | Yes | No local photography, no location context |
| `maximum-scale=1.0` on viewport | Yes | Accessibility violation |
| Empty meta descriptions | Yes | Terrible for SEO |
| og:url pointing to google.com | Yes | Tailbase platform bug, needs fixing |
| Footer with only 3 links | Yes | Address, hours, service area not in footer |
| Reviews isolated to /reviews page | Yes | Best social proof buried, not threaded through site |
| Brand page as logo dump | Yes | No brand positioning copy |
| Financing as QR-code-only page | Yes | Acima not explained, Wells Fargo poorly formatted |

---

## New Design Direction (from brief)

### Palette
| Token | Hex Target | Role |
|-------|-----------|------|
| Background | `#F5F0E8` approx | Warm appliance white / cream |
| Primary | `#1A3028` approx | Deep bottle green / Charleston green |
| Accent | `#7BA3A0` approx | Muted Gulf blue |
| Sale/Clearance | `#C0432A` approx | Restrained red-orange (not neon) |
| Border | `#D4C9B8` approx | Warm gray |
| Text | `#1A1A1A` | Near-black for readability |

### Typography
- **Body/UI:** Sturdy grotesk sans (e.g., Inter, Instrument Sans, DM Sans)
- **Heritage callouts:** Restrained serif (e.g., Playfair Display, Lora, Spectral) — used sparingly for "since 1947" type statements
- No condensed fonts as primary
- No script fonts

### Geometry
- Square-cornered panels (0–2px radius max on cards)
- Thin rule lines between sections
- Signage-like CTA buttons (sharp, uppercase, generous padding)
- Grid-based layout, not floating sidebars

### Photography direction
- Real store photography (Airline Drive showroom)
- Real appliances in real rooms (not stock kitchen photos)
- Staff photography optional but powerful
- No stock-family-in-kitchen photos
