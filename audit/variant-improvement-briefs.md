---
title: Barto Appliance — Variant Improvement Briefs
persona: SANDBATCH.md
date: 2026-05-23
source_critique: audit/sandbatch-critique.md
status: canonical
---

# VARIANT IMPROVEMENT BRIEFS
*Concrete, promptable design changes toward 9/10 — C. Sandbatch / St. Expedite Press*

Each brief is structured as: (1) diagnosis, (2) concrete changes, (3) agent prompt ready to feed to `/new-variant` or `claude-design`.

---

## VARIANT A — Teal Split Hero → 9/10

**Diagnosis:** Structural hierarchy is correct; photo is generic; header has duplicate CSS blocks.

**Concrete changes:**
- Hero photo: replace `hero-kitchen-wide.jpg` with a warm, slightly lived-in kitchen scene — tile backsplash, older cabinetry, real Louisiana domestic energy. Not Sub-Zero-grade. Not HGTV.
- Add the Louis David quote as a small white italic line below the CTAs in the teal panel: *"After a terrible experience with a big box store, I called Barto — Terri took care of it all."*
- Add `EST. 1947` as a 10px spaced-caps amber line above the headline in the teal panel
- Add a bottom-right orange badge: `SAME-WEEK DELIVERY AVAILABLE` in Inter 700 caps
- Remove the duplicate `/* ── BRAND-ALIGNED HEADER */` CSS comment blocks (lines 33–50 of `barto-homepage.html`)
- Teal panel: increase left padding from 48px to 64px for breathing room

**Agent prompt:**
```
Improve Variant A (barto-homepage.html) toward a 9/10 homepage for Barto Appliance.

Keep: split teal-left / photo-right composition, brand palette, DM Sans typography, orange CTA buttons, amber phone number.

Change:
1. Hero photo (right panel): swap for a warm domestic kitchen scene with tile backsplash and real Louisiana home energy — not aspirational luxury, not HGTV.
2. In the teal left panel, above the h1 headline, add: `EST. 1947` in 10px letter-spaced amber DM Sans caps.
3. Below the CTA buttons, add one italic quote line in white at 14px: "After a terrible experience at a big box store, I called Barto — Terri took care of it all." — Louis David, Google Review
4. Add a small amber badge fixed bottom-right of the hero: "SAME-WEEK DELIVERY AVAILABLE" in DM Sans 700 caps.
5. Remove any duplicate CSS comment blocks in the header styles.
6. Increase left panel padding-left to 64px.

Brand palette: teal #004A6E, orange #E8871A, amber #FFC20E, cream #FAF7F2.
```

---

## VARIANT B — Teal Full-Width Hero → 9/10

**Diagnosis:** Immersive structure is sound; Playfair italic amber subhead is decorative not load-bearing; stat data has errors; Louis David quote absent above fold.

**Concrete changes:**
- Remove the Playfair Display italic `In business since 1947.` subtitle from the hero; replace with a DM Sans 600 tagline in white: `They don't make 'em like they used to. We do.`
- Fix stat: "8 Brands" → "15 Major Brands"
- The amber hero eyebrow (`METAIRIE, LOUISIANA · GREATER NEW ORLEANS`) is correct — keep it
- Add the Louis David review as a small inline chip/badge on the hero overlay: amber left border, white 13px italic text, right-aligned or centered below the CTAs
- The stat strip numbers should remain amber-on-white; make the labels DM Sans 500 not 400 for legibility
- The bottom `1947 IN BUSINESS SINCE` large number treatment is the strongest element — increase to 80px and keep

**Agent prompt:**
```
Improve Variant B (variant-b-navy-brass.html) toward a 9/10 homepage for Barto Appliance.

Keep: full-width kitchen photo hero with teal overlay, horizontal category strip, stat row at bottom (2,000+ / 75+ brands / 15 major brands / 8 delivery zones), the large "1947" typographic treatment at the bottom.

Change:
1. Hero subtitle: remove the Playfair Display italic amber "In business since 1947." — replace with DM Sans 600 white text: "They don't make 'em like they used to. We do."
2. Fix the stat: "8 Brands" → "15 Major Brands"
3. Add a Louis David review chip below the CTA buttons: amber left-border, 13px white italic text reading: "After a big box store failed her, Louis David called Barto. Terri answered. Problem solved." — attributed in 10px caps.
4. Increase the bottom "1947" typographic treatment to 80px.
5. Hero overlay opacity: reduce from 0.88 to 0.78 so the kitchen photo reads warmer.

Brand palette: teal #004A6E, orange #E8871A, amber #FFC20E, cream #FAF7F2.
```

---

## VARIANT C — Teal Inverted Split → 9/10

**Diagnosis:** The cream left panel is visually weaker than the teal right panel — info on the weak side, decoration on the strong side. Fix the distribution.

**Concrete changes:**
- Increase the headline to 64px and make it the dominant visual element on the left: **"Major appliances. Real people. Since 1947."**
- Add the Louis David quote below the CTAs on the cream left panel (Playfair italic, 15px, muted color)
- On the teal right panel: keep the 72px stat numbers but change the accent color on the `+` from `var(--orange-dark)` to `var(--amber)` for consistency
- Add a thin amber horizontal rule (2px, full width) between the address block and the CTAs on the left panel
- The orange top border on the header is correct — keep it
- Add `3833 Airline Drive, Metairie` as a DM Sans 13px line below "Since 1947" on the left, styled in `var(--muted)`

**Agent prompt:**
```
Improve Variant C (variant-c-slate-rust.html) toward a 9/10 homepage for Barto Appliance.

Keep: cream-left / teal-right split composition, orange top border on header, large stat numbers on right panel, orange and teal CTAs.

Change:
1. Hero headline (left panel): increase to 64px DM Sans 700. Text: "Major appliances. Real people. Since 1947."
2. Add below the headline: address line in 13px DM Sans muted — "3833 Airline Drive, Metairie, LA"
3. Add a 2px amber horizontal rule between the address and the CTA buttons.
4. Add the Louis David quote below the CTA buttons on the left panel: Playfair Display italic 15px in muted color. Full quote: "After a terrible experience with a big box store, I called Barto and Terri took care of it all!" — Louis David, Google Review, March 2024.
5. Right panel stat accent color: change `var(--orange-dark)` to `var(--amber)` (#FFC20E) on the plus signs.
6. Left panel should visually compete with the right — ensure the headline at 64px creates enough weight.

Brand palette: teal #004A6E, orange #E8871A, amber #FFC20E, cream #FAF7F2.
```

---

## VARIANT D — Editorial White + Teal → 9/10

**Diagnosis:** Already the strongest. Minor precision work only — copy upgrade, class-legibility softening, title tag artifact cleanup.

**Concrete changes:**
- Swap the hero deck copy for: `2,000+ appliances in stock at 3833 Airline Drive. *They don't make 'em like they used to. We do.*` — the italic phrase in Playfair Display
- The dateline `METAIRIE, LOUISIANA · GREATER NEW ORLEANS · EST. 1947` is perfect — do not touch it
- Add a 1px amber bottom-border to the `hero-divider` rule for color punctuation
- Soften the pure white body background to `#FDFCFA` — one step warmer, reduces the editorial coldness concern
- Fix the HTML `<title>`: `Barto Appliance — Variant D: Editorial White + Forest` → `Barto Appliance — Home`
- The Louis David quote block is correctly positioned — make the Playfair italic weight `font-weight: 600` (it reads too light at 400 on white)

**Agent prompt:**
```
Improve Variant D (variant-d-editorial-white.html) toward a 9/10 homepage for Barto Appliance. This is the strongest variant — precision edits only.

Keep: 80px DM Sans headline, 2-column hero (copy left / phone+quote right), dateline in small-caps, newspaper-editorial structure, teal phone call block, Louis David quote placement.

Change:
1. Hero deck copy: "2,000+ appliances in stock at 3833 Airline Drive. They don't make 'em like they used to. We do." — render "They don't make 'em like they used to. We do." in Playfair Display italic.
2. Add a 1px amber bottom-border to the hero-divider rule (the horizontal line between dateline and headline).
3. Body background: change from #FFFFFF to #FDFCFA (one step warmer).
4. Louis David quote: increase Playfair Display font-weight from 400 to 600.
5. Fix HTML <title> from "Variant D: Editorial White + Forest" to "Barto Appliance — Home."

Brand palette: teal #004A6E, orange #E8871A, amber #FFC20E, cream #FAF7F2.
```

---

## VARIANT E — Brand True → 9/10

**Diagnosis:** Best subheadline in the original set; above-the-fold destroyed by three competing header bands.

**Concrete changes:**
- Remove the announcement banner entirely (the promotional strip at the very top) — move any promotional content into the hero stat strip
- Merge the `topbar` and `header` into one unified `header` component: teal background, logo left, nav center, phone + clearance button right
- This brings the hero immediately below the single unified header — the diagonal chevron hero now gets proper above-the-fold real estate
- Promote "They don't make 'em like they used to. We do." to h1 position in the hero — currently buried as deck copy
- The chevron diagonal cut between hero panels is the strongest structural element in E — make the angle more pronounced (20deg instead of the current 12deg)
- The amber stat strip below the hero is correct — do not remove it

**Agent prompt:**
```
Improve Variant E (variant-e-brand-true.html) toward a 9/10 homepage for Barto Appliance.

Keep: brand palette at full intensity, diagonal chevron-cut hero, amber stat strip, photo panel with bento stats (2,000+ / 1947 / 15 / 1 call), the copy "They don't make 'em like they used to. We do."

Change:
1. Remove the announcement banner (the promotional topbar at the very top). Move any promotional content into the hero or stat strip.
2. Merge the topbar and teal header into one unified header: teal #004A6E background, logo left, nav center, amber phone number + orange CLEARANCE button right. One band, not two.
3. Promote "They don't make 'em like they used to. We do." to the hero h1. The current h1 ("Major appliances for greater New Orleans.") becomes the eyebrow/subhead.
4. Increase the diagonal chevron cut angle from current to approximately 20 degrees for more visual drama.
5. Add "Same-Week Delivery Available" as an amber inline tag below the hero CTAs.

Brand palette: teal #004A6E, orange #E8871A, amber #FFC20E, cream #FAF7F2.
```

---

## VARIANT F — Dark Showroom Luxury → 9/10

**Diagnosis:** Concept failure, not detail failure. Path to 9/10 requires a philosophy pivot — keep the dark aesthetic but reground it in Barto's actual identity.

**Concrete changes:**
- Headline: kill "The Finest Appliances in New Orleans" — replace with **"The South's Appliance Authority. Since 1947."** (from G — the best headline in the set)
- Body background: lighten from `#141414` to `#181818` and introduce teal `#003256` as structural fills (currently underused) to maintain brand connection
- Replace all glassmorphism card treatments (`backdrop-filter: blur`) with solid teal-bordered cards (`border: 1px solid #004A6E`) with `#1C1C1C` background
- The amber glow logo is correct — protect it
- The dark luxury aesthetic can coexist with Barto's identity IF the claims are grounded: longevity, service, specific expertise — not "finest"
- Add the Louis David quote in a `#1C1C1C` panel with amber left border immediately below the hero

**Agent prompt:**
```
Regrounding Variant F (variant-f-dark-luxury.html) toward a 9/10 homepage for Barto Appliance. This is a philosophy pivot, not a detail fix.

Keep: dark body (#181818), amber/gold logo treatment with glow effect, DM Sans typography throughout, teal as structural accent color.

Change:
1. Hero headline: replace "The Finest Appliances in New Orleans" with "The South's Appliance Authority. Since 1947." — DM Sans 700 in cream #F0EBE3.
2. Remove all glassmorphism / backdrop-filter effects from card components. Replace with solid cards: background #1C1C1C, border 1px solid #004A6E.
3. Introduce teal #003256 as a structural fill for the header band (currently near-black).
4. Add the Louis David review below the hero: dark panel #1C1C1C, amber left border 3px, Playfair Display italic 17px cream text: "After a terrible experience with a big box store, I called Barto and Terri took care of it all!" — small-caps citation.
5. All "finest" / "luxury" copy language: replace with claims of longevity and service expertise. "Same-Day Delivery" not "Premium Experience."

Brand palette: teal #004A6E, orange #E8871A, amber #FFC20E, body #181818, text #F0EBE3.
```

---

## VARIANT G — Heritage Editorial → 9/10

**Diagnosis:** Best headline in the set. Masthead is 30% too formal — borrows from newspaper institution rather than appliance authority.

**Concrete changes:**
- Keep **"The South's Appliance Authority. Since 1947."** as the definitive headline — this is the asset
- Masthead/header: remove the centered ornamental rule between the topbar and the main header; consolidate to one `header` element with teal background and the Barto logo in Playfair + DM Sans
- The cream/paper body is correct — do not touch the color palette
- Add the Louis David quote to the hero right column: Playfair italic 17px in `var(--warm-dark)` with `var(--warm-border)` left border
- Section headlines below the fold: alternate — use Playfair italic for callout phrases only, DM Sans 700 for navigation/functional copy; currently too Playfair-heavy throughout
- Add the physical address `3833 Airline Drive, Metairie, LA` more prominently — below the hero headline in 14px DM Sans muted, with `📍` or a simple `›` prefix

**Agent prompt:**
```
Improve Variant G (variant-g-heritage-editorial.html) toward a 9/10 homepage for Barto Appliance. The headline is already correct — protect it.

Keep: "The South's Appliance Authority. Since 1947." as the hero headline. Cream #FAF7F2 body. Playfair Display for callout phrases. Ink-teal #004A6E structural color. Warm border #D4C4B0 palette.

Change:
1. Masthead: remove the centered ornamental rule between the topbar dateline and the main header. Consolidate to one clean teal header with logo left, nav center, amber phone + orange clearance button right.
2. Below the hero headline, add: "3833 Airline Drive, Metairie, LA · Mon–Fri 9:30–6 · Sat 10–3" in 14px DM Sans muted, with a right-arrow separator.
3. Hero right column: add the Louis David quote block — Playfair italic 17px in warm-dark color (#6B5F52), left border 3px in warm-border (#D4C4B0). Full text: "After a terrible experience with a big box store, I called Barto and Terri took care of it all!" — Louis David, Google Review, March 2024.
4. Below-the-fold section headlines: use Playfair italic ONLY for short callout phrases (under 6 words). All functional/navigation copy switches to DM Sans 700.

Brand palette: ink-teal #004A6E, orange #E8871A, amber #FFC20E, cream #FAF7F2.
```

---

## VARIANT H — Bento Grid Modern → 9/10

**Diagnosis:** Correct structural language; wrong hero image (glass-door refrigerator); wrong headline ("finest"); fix both and H becomes a strong Phase 3 candidate.

**Concrete changes:**
- Hero headline: replace "New Orleans' Finest Appliances." with **"New Orleans' Appliance Authority. Since 1947."** — DM Sans 900 weight
- Hero bento photo cell: replace the glass-door commercial refrigerator with a warm kitchen scene — range or dishwasher or laundry room, something domestic and human-scale
- Add a "Call for Price" bento cell in amber `#FFC20E` with teal text: `(504) 831-2734` in large DM Sans 700 — currently the phone CTA is buried
- The `2,000+` and `1947` bento cells are the strongest typographic elements — increase their font-size from current to `font-size: clamp(64px, 8vw, 100px)`
- Add the Louis David quote as a full-width cream bento cell below the main grid: DM Sans 400 italic 17px, teal left border 3px
- No Playfair anywhere — maintain the commitment

**Agent prompt:**
```
Improve Variant H (variant-h-bento-modern.html) toward a 9/10 homepage for Barto Appliance.

Keep: asymmetric bento grid layout, DM Sans exclusively (no Playfair), white body, teal structural bento cells, orange CTAs, the 2,000+ and 1947 typographic cells.

Change:
1. Hero headline: "New Orleans' Finest Appliances." → "New Orleans' Appliance Authority. Since 1947." — DM Sans 900.
2. Hero bento photo cell: replace the glass-door commercial refrigerator image with a warm domestic kitchen photo (range, laundry, or dishwasher — human-scale, not commercial-grade).
3. Add a new bento cell in amber #FFC20E: phone number (504) 831-2734 in teal DM Sans 700 at 28px, labeled "Call for Price" in 11px spaced caps.
4. Increase the 2,000+ and 1947 bento cell font-size to clamp(64px, 8vw, 100px).
5. Add a full-width bento row below the main grid: cream #FAF7F2 background, teal 3px left border, DM Sans italic 17px: "After a terrible experience with a big box store, I called Barto and Terri took care of it all!" — Louis David, Google Review, March 2024.

Brand palette: teal #004A6E, orange #E8871A, amber #FFC20E, white #FFFFFF.
```

---

## VARIANT I — Bold American Signage → 9/10

**Diagnosis:** Closest to 9/10 without changes. Minor precision additions only.

**Concrete changes:**
- Add the Louis David quote as an amber-bordered block below the stats row: Playfair Display italic 18px in `var(--near-black)` — the single use of Playfair in the entire design reads as a deliberate exception, not a style inconsistency
- Category tiles: add stock count chips to each tile — "204 models" in 11px DM Sans spaced-caps orange — reinforces the inventory depth claim
- Stats row: add "Same-Week Delivery" as a fourth stat with Inter Black 900 `SAME WEEK` and DM Sans label "Delivery available" — this competitive differentiator is currently missing from I
- Rebate badge on the product feature card: ensure the rebate amount matches actual current promotions; `UP TO $4,000 REBATE` is approximately correct for KitchenAid
- The "EST. 1947" teal block in the hero is the strongest visual anchoring of the founding date in the set — do not touch it

**Agent prompt:**
```
Improve Variant I (variant-i-bold-signage.html) toward a 9/10 homepage for Barto Appliance. This is the closest to finished — precision additions only.

Keep: Inter Black 900 for all headlines, UPPERCASE structural labels, teal block "BARTO APPLIANCE EST. 1947", cream #FAF7F2 body, no gradients, no rounded corners (max 2px), solid fills only, orange CTAs, amber phone number.

Add:
1. Louis David quote block below the stats row: Playfair Display italic 18px in #1C1C1C, left border 3px amber #FFC20E. Text: "After a terrible experience with a big box store, I called Barto and Terri took care of it all!" — Louis David, Google Review, March 2024. This is the only Playfair element in the design — intentional contrast.
2. Category tiles: add "204 models" / "138 models" / etc. stock count chips in 11px DM Sans 600 spaced-caps in orange #E8871A.
3. Stats row: add a fourth stat — Inter Black 900 "SAME WEEK" with DM Sans label "Delivery Available" — in the same style as the existing stats.
4. Verify the rebate badge on the product feature card reads: "UP TO $4,000 REBATE — THRU JUNE 30"

Brand palette: teal #004A6E, orange #E8871A, amber #FFC20E, cream #FAF7F2, near-black #1C1C1C.
```

---

## VARIANT J — Gulf Coast Coastal Premium → 9/10

**Diagnosis:** Palette instinct correct; headline is market-consultant boilerplate; rounded pill chips are the wrong register; stock photo couple needs to go.

**Concrete changes:**
- Headline: replace "Louisiana's Most Trusted Appliance Dealer." with **"Since 1947, Greater New Orleans calls us first."** — Playfair Display italic 52px, warmth without boast
- Kill all rounded pill trust chips (`border-radius: 20px+`). Replace with straight-rule separated claims: `—` dash separator, DM Sans 600, no border at all. The linen palette does the warmth work without the pill shapes.
- Hero photo: replace the couple stock photo with a warm, specific image — a kitchen in an older New Orleans home, tile floors visible, natural light. Barto's customer is a homeowner with a house that has character, not a couple browsing a showroom.
- "Since 1947. Metairie, Louisiana." is already in the design — elevate it to eyebrow position above the headline in 11px DM Sans spaced-caps warm-gray
- Add the Louis David quote in a linen-dark `#EBE0C4` panel below the hero: Playfair italic 17px in `var(--drift-dk)`, warm border left

**Agent prompt:**
```
Improve Variant J (variant-j-coastal-premium.html) toward a 9/10 homepage for Barto Appliance.

Keep: linen body #F5EDD8 with grain texture, Playfair Display italic for section callouts, DM Sans for body and navigation, teal #004A6E structural elements, warm border palette #D4C4A8, coral/orange #E8871A CTAs.

Change:
1. Hero headline: replace "Louisiana's Most Trusted Appliance Dealer." with "Since 1947, Greater New Orleans calls us first." — Playfair Display italic 52px in #2A2018.
2. Add eyebrow above headline: "METAIRIE, LOUISIANA · EST. 1947" in 11px DM Sans 600 spaced-caps in var(--drift) color.
3. Kill ALL rounded pill trust chips (border-radius: 20px+). Replace with inline straight-rule claims: amber dash separator, DM Sans 600, no background, no border-radius. Example: "— 2,000+ Appliances in Stock  — Same Day Delivery  — Since 1947  — Real People Answer"
4. Hero photo: replace the couple stock photo with an older New Orleans home kitchen — tile floors, natural light, character. Not HGTV, not a showroom.
5. Add the Louis David quote in a linen-dark panel #EBE0C4 below the hero: Playfair italic 17px in drift-dark color. Text: "After a terrible experience with a big box store, I called Barto and Terri took care of it all!" — Louis David, Google Review, March 2024.

Brand palette: teal #004A6E, coral #E8871A, amber #FFC20E, linen #F5EDD8, text #2A2018.
```
