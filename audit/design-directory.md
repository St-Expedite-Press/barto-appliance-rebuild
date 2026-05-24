# Barto Appliance — Design Directory & Modernization Guide
**Compiled:** 2026-05-23 | Phase 2 Expansion  
**Scope:** All 10 design variants, full web element inventory, logo modernization brief, contemporary design standards

---

## 1. Design Variant Directory

### Phase 2 — Original 5 Variants (Completed 2026-05-22)

| File | Variant | Concept | Best For |
|------|---------|---------|----------|
| `barto-homepage.html` | **A: Teal Split Hero** | Teal left panel / photo right, Barto brand palette baseline | Client presentation — safe & polished |
| `variant-b-navy-brass.html` | **B: Teal Full-Width** | Full-width hero centered layout, amber stat accents | Demonstrates full-bleed photography |
| `variant-c-slate-rust.html` | **C: Teal Inverted Split** | Inverted split — cream left, teal right | Gives the brand more breathing room |
| `variant-d-editorial-white.html` | **D: Editorial White** | Newspaper-inspired, white body, teal editorial accents | Most differentiated from current site |
| `variant-e-brand-true.html` | **E: Brand True** | Most expressive use of brand palette — richest detail | Widest range of design elements shown |

**Supporting pages (all variants):**
- `barto-category.html` — Category listing with filter sidebar
- `barto-product-detail.html` — Full product detail with inquiry modal
- `design-system-docs.html` — Design token documentation

---

### Phase 2 Expansion — 5 New Variants (Completed 2026-05-23)

| File | Variant | Concept | Defining Move |
|------|---------|---------|---------------|
| `variant-f-dark-luxury.html` | **F: Dark Showroom Luxury** | Charcoal body, amber glow, glassmorphism review card | Dark background — premium showroom feel after dark |
| `variant-g-heritage-editorial.html` | **G: New Orleans Heritage Editorial** | Cream body, Playfair Display dominant, newspaper masthead | Large-scale italic headlines, editorial authority |
| `variant-h-bento-modern.html` | **H: Bento Grid Modern** | Pure white, asymmetric CSS bento grid, oversized DM Sans 900 | 2025/2026 layout pattern — varied card sizes |
| `variant-i-bold-signage.html` | **I: Bold American Signage** | Cream/near-black/teal, Inter Black 900 UPPERCASE, no gradients | Storefront sign typography system — bold & structural |
| `variant-j-coastal-premium.html` | **J: Gulf Coast Coastal Premium** | Warm linen, Playfair + DM Sans, trust chip pills, rounded cards | Louisiana warmth — sun-bleached coastal permanence |

---

## 2. Design Concept Profiles

### Variant F — Dark Showroom Luxury
**Personality:** Restoration Hardware meets a premium local institution after dark.  
**Target emotion:** "This is a serious appliance dealer, not a catalog platform."  
**Key techniques:**
- `rgba(20,20,20,0.92)` + `backdrop-filter: blur(16px)` sticky header (glassmorphism nav)
- Radial amber gradient orb (`rgba(200,134,10,0.12)`) behind hero text — ambient glow
- Dark teal panel (`#003A56`) for trust band — differentiates from pure-black body
- Glassmorphism review card: `bg: rgba(35,35,35,0.8)`, `backdrop-filter: blur(16px)`, amber border
- `filter: brightness(0) invert(1)` on logo to render white on dark
- Category cards: photo overlay with `transition: scale(1.04)` hover, amber border glow
- Footer: `border-top: 2px solid var(--amber)` — amber rule at top of very dark footer

**Works best when:** client wants to compete on premium feel, not price. Best for hero product photography.

---

### Variant G — New Orleans Heritage Editorial
**Personality:** The visual authority of a New Orleans institution — iron lacework, editorial confidence, a newspaper that has been publishing since before you were born.  
**Target emotion:** "These people have been at this longer than I've been alive."  
**Key techniques:**
- Playfair Display italic at 68–80px for hero headline — editorial "ink" voice
- Newspaper masthead strip: `font-size: 11px; letter-spacing: 0.07em; text-transform: uppercase`
- Dateline bar (info strip below hero) mimics a newspaper's dateline formatting
- Category cards: `border-top: 3px solid var(--ink)` on body section — editorial ruled separator
- Speed Queen feature block: full-bleed dark teal panel inside the cream page — contrast shift
- Section headers: `font-family: var(--font-editorial); font-style: italic; font-size: 44px`
- Pull-quote: `font-size: 38px; font-weight: 700` Playfair italic — one line carries the whole review
- Rebates as editorial table: amount | brand | description | expires — reads like a deal sheet
- Ornamental `<div class="rule-diamond">◆</div>` used as section divider element

**Works best when:** client wants heritage and authority to lead, product catalog is secondary.

---

### Variant H — Bento Grid Modern
**Personality:** The 2025/2026 dominant layout language — the page that communicates fluency with current web design instantly.  
**Target emotion:** "This company is forward-thinking."  
**Key techniques:**
- Hero headline at `font-size: 72px; font-weight: 900; letter-spacing: -0.04em` — oversized DM Sans Black
- Animated pulse dot in hero tag: `@keyframes pulse { 0%,100%{opacity:1} 50%{opacity:0.3} }`
- Bento grid: `display: grid; grid-template-columns: repeat(4, 1fr)` with `span 2` / `row-span 2` for varied sizes
- 7 bento cells: Large photo (2×2) | Teal stat | Amber stat | Review (2×1) | Orange clearance (1×2) | Laundry photo | Speed Queen card
- Stat cells: `font-size: 56px; font-weight: 900; letter-spacing: -0.04em` — numbers as design elements
- Review cell: `border-left: 4px solid var(--teal)` — structural left rule not a card border
- Clearance cell: `background: var(--orange)` solid fill — orange as a block element
- Watermark text: `content: 'CLEARANCE'; opacity: 0.08; font-size: 120px` background watermark
- Brand strip: `filter: grayscale(1)` on logos, `hover: filter: none` for color reveal

**Works best when:** client wants to signal modernness. Best for younger demographic. Needs strong product photos.

---

### Variant I — Bold American Signage
**Personality:** A masterclass in American commercial graphic design — the sign painter's confidence applied to pixels.  
**Target emotion:** "Barto knows who they are and doesn't apologize for it."  
**Key techniques:**
- Inter Black 900 weight, UPPERCASE, `letter-spacing: -0.04em` for hero stacked "storefront" headline at 104px
- Hero headline stacks three lines: `BARTO` / `APPLIANCE` / `EST. 1947` — like a building sign
- `border-bottom: 4px solid var(--near-black)` throughout — heavy ruled lines define structure
- **No gradients, no rounded corners, no shadows.** Only solid fills and ruled borders.
- Section divider: teal 4px rule + uppercase label + gray rule extending full width
- Trust row: `background: var(--near-black)` with amber stats — dark bar acts as visual anchor
- Phone number in amber block `<a class="header-phone">` — button-styled, not just a link
- Brand table: `border: 2px solid var(--near-black)` wrapping the entire grid — newspaper-column feel
- Review band: full-width teal, Inter Black 900 weight uppercase quote text + amber highlight span
- Footer border: `border-top: 8px solid var(--near-black)` — maximum structural weight

**Works best when:** client wants to own a strong visual identity. Works for older, local-pride demographic.

---

### Variant J — Gulf Coast Coastal Premium
**Personality:** The permanence of quality in a warm climate. Not beachy — the color of a well-kept New Orleans bungalow, warm afternoon light, things built to last.  
**Target emotion:** "This dealer understands the way we live down here."  
**Key techniques:**
- Linen body `#F5EDD8` — warmer and more distinctive than standard cream `#FAF7F2`
- CSS noise grain texture overlay: SVG `feTurbulence` filter at `opacity: 0.04` for subtle warmth
- Trust chips: `border-radius: 100px` pill shape — soft and approachable (vs. sharp in variants A/I)
- Category cards: `border-radius: 8px` + `box-shadow: 0 8px 32px rgba(232,135,26,0.1)` on hover
- Card hover: `transform: translateY(-2px)` — subtle lift (micro-interaction)
- Pull-quote in driftwood section `#8B7D6B` — warm earth tone background for testimonial
- Review text: Playfair italic `font-size: 38px; font-weight: 700` — largest quote presentation of all variants
- Financing pills: `border-radius: 100px` chips — consistent soft geometry throughout
- Footer social: `border-radius: 50%` circular social buttons — only variant to use circles
- `filter: saturate(0.9)` on category photos — slightly desaturated for warm cohesion

**Works best when:** client wants warmth and local identity. Best for demographic over 45. Looks excellent with showroom photography.

---

## 3. Full Web Element Inventory

### 3.1 Navigation System

**Current site problems:**
- `maximum-scale=1.0` viewport blocks pinch-zoom (accessibility violation)
- Phone not a `tel:` link consistently
- No sticky header
- Hamburger on desktop (flagged as outdated by 2026 standards)

**Standard for rebuild:**

| Element | Spec | Notes |
|---------|------|-------|
| Header height | 68–76px desktop / 56px mobile | Taller = more premium |
| Logo | Height 38–44px, `object-fit: contain` | Always link to home |
| Logo on dark bg | `filter: brightness(0) invert(1)` | Avoids maintaining 2 logo files |
| Nav font | 12–13px, `font-weight: 600`, `letter-spacing: 0.04–0.08em` | |
| Nav active state | `border-bottom: 2–3px solid var(--orange)` | Underline preferred over background pills |
| Header phone | `<a href="tel:5048312734">` always | Clickable on ALL viewports |
| Phone color | Amber `#FFC20E` on dark headers | Maximum visibility |
| Clearance button | Isolated, contrasting fill color | Right-aligned in header |
| Sticky | `position: sticky; top: 0; z-index: 100` | Stays in view on scroll |
| Mobile sticky (Phase 3) | [Call] [Directions] [Clearance] [Search] — 4 full-width touch targets | |
| Mega-menu | Products → Kitchen / Laundry / AC columns | On desktop, never hamburger |

---

### 3.2 Hero Sections

| Approach | When to Use | File |
|----------|-------------|------|
| Split hero (copy left, photo right) | Default — works best at 55/45 or 60/40 | Variants A, C, G, J |
| Full-width photo hero | When photography is strongest asset | Variant B |
| Dark hero with glow | Premium/luxury positioning | Variant F |
| Two-thirds copy + one-third teal panel | Signage aesthetic, product image label | Variant I |

**Hero headline scale by variant:**
- Conservative: 52px (Variant A/E)
- Editorial: 60–68px Playfair italic (Variants G, J)
- Modern oversized: 72–80px DM Sans Black (Variant H)
- Signage: 104px Inter Black (Variant I)

**Hero copy formula (all variants):**
```
Eyebrow: [City] · [Since year]        (10–11px, uppercase, letter-spaced)
H1:      [Brand positioning]           (large, confident, 2–3 lines max)
Sub:     [2,000+ in stock] + [delivery note]  (16–17px, muted color)
CTAs:    [Primary] + [Secondary ghost]  (gap: 12–14px)
```

**Stats always shown in hero (3–4 stats):**
- `2,000+` In Stock
- `Same Day` Delivery
- `Since 1947`
- `(504) 831-2734` (on mobile hero)

---

### 3.3 Button System

| Type | CSS Approach | Use Case |
|------|-------------|----------|
| Primary CTA | Solid orange `#E8871A`, white text, `padding: 15–18px 32px` | Main conversion action |
| Primary dark bg | Solid amber `#C8860A`, dark text | On dark backgrounds (Variant F) |
| Secondary ghost | Transparent, colored border, matching text | Second CTA alongside primary |
| Ghost on dark | `border: 1px solid rgba(255,255,255,0.25)` | On teal/dark panels |
| Teal solid | `background: var(--teal)`, cream text | "Visit Showroom" type CTAs |
| Cream/linen | `background: var(--cream)`, dark text | On dark teal panels (Variant J) |
| White solid | `background: #FFFFFF`, orange text | On orange panels (Variant H) |
| Amber solid | `background: var(--amber)`, dark text | Phone CTAs, Clearance (Variant F) |
| Clearance nav btn | Amber or orange fill, uppercase, in header | Isolated from nav links |

**Border radius decisions:**
- Sharp `0px` — Variants A, E, I (signage/commercial)
- Minimal `2–4px` — Variants B, C, F, G (premium/editorial)
- Moderate `6–8px` — Variants D, H (modern/clean)
- Pill `100px` — Variant J trust chips, needs chips (coastal/soft)

---

### 3.4 Card System

**Product Card (for Phase 3 build):**
```
┌─────────────────────────────┐
│ [Product Photo — 16:9]      │ ← aspect-ratio locked
│                             │
├─ [Rebate badge] [Stock chip]─┤
│ Brand name                  │
│ Model number (large)        │
│ Category descriptor         │
│ Key spec (width)            │
├─────────────────────────────┤
│ [Call] [Ask] [Compare]      │ ← 3 CTAs always
└─────────────────────────────┘
```

**Bento Grid Cards (Variant H pattern):**
- `col-span-2 / row-span-2` — Hero photo (largest)
- `col-span-1 / row-span-1` — Stats, small product cards
- `col-span-2 / row-span-1` — Review quotes, horizontal content
- `col-span-1 / row-span-2` — Clearance CTA, tall callouts

**Category Photo Cards:**
- Overlay: `linear-gradient(to top, rgba(0,0,0,0.75) 0%, transparent 55%)`
- Text: positioned at bottom of card, `z-index: 2`
- Hover: `transform: scale(1.04)` on photo, `transition: 0.5s ease`

**Review/Testimonial Cards:**
- Feature review: Max-width 760px, centered, with glassmorphism option
- Pull-quote band: Full-width section, 38–48px Playfair italic
- Grid reviews: 3-column, standard card format

---

### 3.5 Typography System

**Locked decisions (all variants):**

| Role | Font | Weight | Use |
|------|------|--------|-----|
| Body / UI | DM Sans | 400, 500, 600, 700 | Nav, body, labels, CTAs |
| Heritage callouts | Playfair Display Italic | 400, 600, 700 | "Since 1947", pull-quotes, editorial headlines |
| Bold signage (Variant I only) | Inter | 700, 800, 900 | UPPERCASE structural text |

**Scale by use:**
- `10–11px / 0.14–0.22em letter-spacing / uppercase` → Eyebrows, labels, kickers
- `12–13px / 0.06–0.1em` → Nav links, fine print, captions
- `14–16px` → Body text standard
- `17–18px` → Hero sub-headlines
- `22–32px / -0.01 to -0.02em` → Section titles, card headlines
- `38–48px / -0.01em` → Pull-quotes (Playfair), section titles (editorial)
- `52–68px / -0.01 to -0.02em` → Hero headlines (standard)
- `72–104px / -0.03 to -0.04em` → Oversized display type (Variants H, I)

**Rules:**
- Max 2 font families. DM Sans is always present. Playfair is optional.
- Serif (Playfair) used ONLY for: hero headlines, pull-quotes, "Since 1947", section titles in editorial mode
- Never serif for: nav, buttons, labels, stats, product names
- Tight leading on large display: `line-height: 0.88–1.05`
- Relaxed leading on body: `line-height: 1.6–1.7`

---

### 3.6 Color System

**Brand palette (immutable across all variants):**

| Token | Hex | Role |
|-------|-----|------|
| `--teal` | `#004A6E` | Header, nav, structural fills |
| `--teal-dark` | `#003256` | Footer, hover states, dark panels |
| `--teal-mid` | `#005F8C` | Secondary accents, lighter teal elements |
| `--orange` | `#E8871A` | Primary CTA — never swapped out |
| `--orange-dark` | `#C96F10` | Orange hover state |
| `--amber` | `#FFC20E` | Phone number, clearance accents, highlights |
| `--amber-dark` | `#E0A800` | Amber hover |
| `--red` | `#C8321E` | Clearance badges, sale text only |
| `--cream` | `#FAF7F2` | Body background (standard) |

**Variant-specific body colors:**
- Standard cream: `#FAF7F2` (Variants A, B, C, E, G, I)
- Warm linen: `#F5EDD8` (Variant J — more saturated warmth)
- Pure white: `#FFFFFF` (Variant H — maximum contrast)
- Near-black: `#141414` / `#1C1C1C` (Variant F — dark luxury)

**2026 color principles applied:**
- Never use pure black `#000000` — use `#111111` or `#1C1C1C`
- Never use pure white for text on cream — use `#1E1A16` or `#2A2018`
- Gradient use: Only Variant F (radial amber glow). All others: solid fills.
- Amber/gold as accent on dark backgrounds — highest contrast option
- Orange reserved for CTAs — not used for decorative elements

---

### 3.7 Footer System

**Standard 4-column footer structure (all variants):**
```
Column 1 (2fr): Brand + description + social links
Column 2 (1fr): Products link list
Column 3 (1fr): Company link list
Column 4 (1.5fr): Visit Us (full address + hours block)
```

**Required footer content (conversion gap fixes):**
- Physical address: 3833 Airline Drive, Metairie, LA 70001
- Phone as `tel:` link: (504) 831-2734
- Full hours grid (Mon–Fri 9:30–6, Fri 5:30, Sat 10–3, Sun closed)
- Service areas: Metairie · New Orleans · Kenner · Jefferson Parish
- Social: Facebook + Twitter/X
- Copyright, Terms, Privacy links

**Footer color approaches by variant:**
- Teal dark `#003256` — Variants A, B, C, E, G, H, J
- Near-black `#0D0D0D` — Variant F (darkest)
- Cream with near-black text — Variant I (inverted)

**Footer top accent rules:**
- `border-top: 2px solid var(--amber)` — Variant F
- `border-top: 4px solid var(--orange)` — Variant G
- `border-top: 3px solid var(--coral)` — Variant J
- `border-top: 8px solid var(--near-black)` — Variant I (maximum weight)

---

### 3.8 Trust & Social Proof Elements

**Types implemented across variants:**

1. **Numeric stat bar** (inline horizontal)
   - `2,000+` | `Same-Day` | `Since 1947` | `Phone`
   - Used: Variants A–J (all)

2. **Trust band (4-cell grid)**
   - Icon + number + label + description per cell
   - Used: Variants E, F

3. **Trust chip pills**
   - `border-radius: 100px`, teal border, icon + text
   - Used: Variant J

4. **Masthead/dateline strip**
   - `font-size: 11px; letter-spacing: 0.07em; uppercase` horizontal crawl
   - Used: Variant G

5. **Review: glassmorphism card**
   - `backdrop-filter: blur(16px); bg: rgba(35,35,35,0.8); border: amber`
   - Used: Variant F

6. **Review: full-width pull-quote band**
   - 38–48px Playfair italic, muted background section
   - Used: Variants G, J, I

7. **Review: card grid** (for Phase 3)
   - Standard card + stars + name + platform badge

**Louis David review copy (locked, use site-wide):**
> "After a terrible experience with an unnamed big box store to install a washer/dryer upstairs in an older home, I called Barto and Terri took care of it all. I bought the washer dryer over the phone, and she connected me with a specialty installer who was able to take care of getting everything working and the old unit out."
> — Louis David, March 2024, Google Review

---

### 3.9 Micro-interactions & Animation

**Applied across variants:**

| Effect | CSS | Trigger |
|--------|-----|---------|
| Card lift | `transform: translateY(-2px)` + `box-shadow` | Hover on product/category cards |
| Photo scale | `transform: scale(1.04)` on `img` within card | Card hover |
| Arrow nudge | `gap: 6px → 10px` on flex link arrows | Link hover |
| Button lift | `transform: translateY(-1px)` | CTA button hover |
| Border reveal | `border-color: var(--amber); opacity: 0 → 1` | Category card hover |
| Pulse dot | `@keyframes pulse { opacity: 1 → 0.3 }` | Status indicators |
| Photo desaturate | `filter: saturate(0.8) → saturate(1)` | Card hover |

**Timing spec:**
- All hover transitions: `0.15–0.2s` (micro-interactions)
- Photo transform: `0.4–0.5s ease` (slower for smoothness)
- Background color changes: `0.15s`

**Not used (intentionally avoided):**
- Auto-playing carousels (2026 best practice: users ignore them)
- Parallax scroll (performance cost for mobile)
- Page load animations (defer until Phase 4)
- Scroll-triggered reveals (defer until Phase 4 with `prefers-reduced-motion`)

---

### 3.10 Rebate Display System

The rebate system is a major conversion driver. Three display patterns:

**Pattern A: Card Grid (3 columns)**
- Used: Variants F, H
- `amount → brand → desc → expires → link`
- Hover: `border-color: var(--orange)`

**Pattern B: Table Rows (2 columns)**
- Used: Variants I, J (rebate-grid)
- `amount | brand + desc + expires` side by side
- Reads like a deal sheet

**Pattern C: Editorial List (2 columns)**
- Used: Variant G
- `amount` (Playfair 44px orange) | body text right
- Most visually dramatic

**Active rebates to show (as of May 2026):**
1. KitchenAid NMG Exclusive — up to $4,000 (July 8, 2026)
2. Frigidaire Professional NMG — up to $2,500 (July 8, 2026)
3. Electrolux + Frigidaire Memorial Day — up to $750 (June 3, 2026)
4. Whirlpool/Maytag/KitchenAid Memorial Day — up to $750 (June 3, 2026)

---

### 3.11 "Shop by Need" / Local SEO Tags

All variants include a local-need chip/tag section. This serves double duty:
1. **UX:** Guides visitors who don't know the catalog
2. **SEO:** Targets long-tail local searches

**Standard needs list (all variants):**
- Appliances for Older Homes → `/older-homes`
- Room Air Conditioners → `/room-ac`
- Same-Week Delivery → `/same-week-delivery`
- Scratch & Dent / Clearance → `/clearance`
- Rental Property Replacement → `/rental-property`
- Full Kitchen Packages → `/categories/kitchen-packages`
- Flexible Financing → `/financing`
- Speed Queen Commercial Laundry → `/brands/speed-queen`

**Tag shape by variant:**
- Sharp rectangle: Variants A, E, G, I (crisp/editorial)
- Soft rounded `6px`: Variant H (modern)
- Pill `100px`: Variant J (coastal/warm)

---

## 4. Logo Modernization Brief

### Current State
The Barto logo is a dark navy block with "Barto Appliance" in a blocky script/condensed combination. It is serviceable but not distinctive. Primary issues:
- Low contrast on the current teal header (very dark on dark)
- Script portion is hard to read at small sizes
- No clear logomark/symbol — just wordmark
- Not designed for dark/light mode versatility

### Modernization Direction (NOT a redesign — an evolution)

**Guiding principle:** The logo must remain recognizably Barto. The shape, the script element, and the navy/teal color must be retained. This is a refinement, not a replacement.

**Specific recommendations:**

1. **Create a logomark:**
   - Extract the "B" from the existing script
   - Square container, teal fill, amber "B" letterform
   - Used at small sizes (mobile header, favicon, social avatar)
   - Proportions: 44×44px to 52×52px

2. **Wordmark refinement:**
   - Retain current "Barto Appliance" lockup
   - Pair with `font: Playfair Display italic` tagline beneath: *"Metairie, Louisiana · Est. 1947"*
   - This tagline reinforces local identity at zero extra cost

3. **Color variants needed:**
   - **Full color:** Dark navy/teal on cream background (existing)
   - **Reversed white:** `filter: brightness(0) invert(1)` for use on teal/dark headers
   - **Amber accent:** "Barto" in amber on dark backgrounds (Variant F treatment)
   - **Single color teal:** For embossed/print use

4. **Size hierarchy:**
   - Full lockup (logo + wordmark + tagline): Homepage header only
   - Compact (logomark + wordmark): All interior pages
   - Icon only: Favicon, social avatar, mobile hamburger icon

5. **What NOT to change:**
   - The script/handwritten quality of "Barto" — this is the brand equity
   - The navy/teal as primary color
   - The "Appliance" as a second line (not inline)

---

## 5. Contemporary Web Design Standards Applied

### 5.1 Layout Patterns Used

| Pattern | Used In | 2026 Status |
|---------|---------|------------|
| Split Hero (60/40) | Variants A, C, G, I, J | ✅ Strong — best for photography + copy balance |
| Full-Width Hero | Variant B | ✅ Works when photography is hero |
| Bento Grid | Variant H | ✅ Dominant 2025/2026 pattern |
| F-Pattern Category Grid | All variants | ✅ Standard, reliable |
| Editorial Table/List | Variants G, I | ✅ Distinctive for information-heavy sections |
| Card Grid (product) | Phase 3 | ✅ Universal e-commerce standard |
| Horizontal Rule Dividers | Variants G, I | ✅ Editorial — replacing background color changes |

**NOT used (intentionally):**
- Accordion mega-menus on desktop → use full drop-down columns
- Auto-rotating carousels → use static hero
- Infinite scroll → use pagination (Tailbase products use pagination)
- Sidebar filters as static (Phase 3) → use sticky drawer filter

---

### 5.2 Accessibility Checklist

| Issue | Current Site | Rebuild Standard |
|-------|-------------|-----------------|
| Viewport `maximum-scale=1.0` | ❌ Present | ✅ Remove — allow pinch-zoom |
| Phone `tel:` links | ❌ Inconsistent | ✅ Every phone instance |
| Skip to content | ❌ Missing | ✅ Add `<a href="#main" class="skip-link">` |
| Image `alt` attributes | ❌ Inconsistent | ✅ All images descriptive alt text |
| Color contrast | ❌ Amber on orange fails | ✅ WCAG AA minimum 4.5:1 on all text |
| Focus styles | ❌ Stripped | ✅ `:focus-visible` outline on all interactive elements |
| Semantic HTML | ❌ Div soup | ✅ `<header>`, `<main>`, `<nav>`, `<section>`, `<footer>` |
| Form labels | ❌ Some missing | ✅ All inputs labeled, not placeholder-only |
| `prefers-reduced-motion` | ❌ Missing | ✅ Wrap all CSS transitions in `@media (prefers-reduced-motion: no-preference)` |

---

### 5.3 Performance Standards

| Element | Standard |
|---------|----------|
| Fonts | `display=swap` on all Google Fonts `<link>` |
| Images | `loading="lazy"` on all below-fold images |
| Hero image | `loading="eager"` on hero — preload critical |
| Logo | `<img>` not CSS background — cacheable |
| Icons | SVG inline or CSS — no icon fonts |
| Animations | CSS only — no GSAP for simple hover states |
| JavaScript | Zero JS required for static HTML variants |

---

### 5.4 SEO & Schema Structure

**Every page needs (Phase 3):**
```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "Barto Appliance",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "3833 Airline Drive",
    "addressLocality": "Metairie",
    "addressRegion": "LA",
    "postalCode": "70001"
  },
  "telephone": "+15048312734",
  "openingHoursSpecification": [...],
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": 29.9756398,
    "longitude": -90.1685747
  }
}
```

**Product pages additionally need:**
```json
{
  "@type": "Product",
  "name": "[Model Name]",
  "brand": { "@type": "Brand", "name": "[Brand]" },
  "offers": { "@type": "Offer", "seller": { "@type": "LocalBusiness" } }
}
```

---

## 6. Variant Selection Guide

Use this matrix to recommend a variant to the client:

| Client Priority | Recommended Variant |
|-----------------|-------------------|
| "We want to look premium, high-end" | **F: Dark Luxury** |
| "We want to show our history and New Orleans roots" | **G: Heritage Editorial** |
| "We want to look modern and up-to-date" | **H: Bento Modern** |
| "We want something bold and confident — no-nonsense" | **I: Bold Signage** |
| "We want something warm, local, approachable" | **J: Coastal Premium** |
| "Safe, polished, use our brand colors" | **E: Brand True** |
| "Show us the most differentiated option" | **D: Editorial White** or **H: Bento** |
| "We're starting from our current site's look" | **A: Teal Split Hero** |

---

## 7. Phase 3 Build Recommendations

Based on the 10 variants, the following decisions are recommended for the Next.js build:

### Hero
**Recommended:** Split hero pattern (Variant A/G/J approach)
- Left panel: copy + CTAs
- Right panel: photography
- The split is more versatile than full-bleed when photography varies

### Typography
**Locked:** DM Sans + Playfair Display italic
- Playfair at `64px` for hero (not 104px — too large for product context)
- DM Sans `900` weight for stats and section titles

### Color Scheme
**Locked:** Barto brand palette (teal/orange/amber/cream)
- Body: `#FAF7F2` cream (not pure white, not linen)
- Dark teal `#003256` for footer
- Amber `#FFC20E` for phone/highlights only

### Layout Approach
**Recommended:** Variant E as the baseline, bento grid for homepage's mid section
- Traditional header/hero/trust-band structure
- Bento grid (Variant H) for the category/trust showcase below the fold
- Standard card grid for product listings

### Immediate Phase 3 Priorities (from conversion gaps)
1. `LocalTrustBar` — address + phone + hours on EVERY page
2. `tel:` link on every phone instance
3. Product inquiry modal pre-fills model/brand
4. Footer: full address, hours, service areas
5. Schema on every page
6. Meta descriptions — SEO helper generates from product data
7. Mobile sticky: [Call] [Directions] [Clearance] [Search]
8. Remove `maximum-scale=1.0`

---

*Design Directory compiled 2026-05-23 by Claude Code.*  
*10 variants complete. Phase 3 scaffold ready to begin.*
