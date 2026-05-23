# Barto Appliance — Conversion Gaps
Audited: 2026-05-22 | Compared against rebuild brief in dump.md

This document maps where the current site fails to convert visitors against each specific conversion scenario in the brief.

---

## Gap 1: No Local Identity on Entry

**What the brief says:** The site should immediately answer "why buy here instead of Lowe's/Home Depot/Best Buy?"

**What the site does:** The home page hero says "They Don't Make 'Em Like They Used To. We Do." — which is actually a good line — but then provides no supporting evidence. No address, no phone in the hero, no "since 1947," no "2,000+ in stock," no service area claim.

**Specific failures:**
- Home page has no `<h1>` with local positioning
- "Since 1947" and "2,000+ in stock" are buried in the About page in weak grammar
- Address (3833 Airline Drive, Metairie) appears only on the Contact page — not in the header, not in the footer
- Hours appear only on the Contact page
- No schema markup (`LocalBusiness`, `OpeningHoursSpecification`, `GeoCoordinates`) on any page

**Fix in rebuild:** Hero band with phone + address + hours baked in. Footer always shows full address + hours. Schema on every page.

---

## Gap 2: "Contact Us For Price" Is a Dead End

**What the brief says:** "Contact Us For Price" is acceptable in appliance retail, but the conversion UX has to compensate: one-click call, SMS/contact form, prefilled model inquiry, human response expectation.

**What the site does:** Every product card and product detail page shows "Contact Us For Price" as static text and a "Price Request" button. Clicking "Price Request" leads to... unclear. The contact form on `/en/contactus` has generic fields (First Name, Last Name, Email, Zip Code, Phone, Comments). No prefilled model number. No response time expectation set. No phone link on the product page.

**Specific failures:**
- "Price Request" button does not prefill model, SKU, or category in the form
- No phone number on product detail pages — user has to navigate to Contact to get the number
- No response time stated ("We'll call you back within 2 hours during store hours")
- No SMS/text option offered
- No "Call us now" tel: link on product pages
- CAPTCHA on contact form creates friction

**Fix in rebuild:** Product detail "Ask About This Model" modal pre-populates model number + category. One-click `tel:` link on every product. Response time stated. Optional SMS field.

---

## Gap 3: Clearance Center Is Nearly Empty

**What the brief says:** Clearance should be treated as a major local traffic asset. "Barto Clearance / Scratch & Dent / Floor Models" with big photography, exact condition notes, "only one available," and urgency mechanic.

**What the site does:** 1 product. One. A Vitara top-freezer refrigerator at $469.98 (was $699.99). No condition notes. No photography (only manufacturer stock photo). CTA is "Price Request" — not even a direct call button.

**Home page does have a "Scratch-N-Dent" section in the main slideshow** (confirming they have/had scratch-and-dent inventory) but it doesn't link to a live page.

**Specific failures:**
- 1 clearance product online vs. implied large physical inventory
- No condition notes (scratch, dent, floor model, etc.)
- No "only 1 available" urgency
- No local/real photography
- CTA is a form ("Price Request") — not a call or a direct buy
- No "mark as sold" workflow visible — item would stay up even if sold

**Fix in rebuild:** Admin clearance editor with: condition grade, photos, availability toggle, "call to claim" button as primary CTA.

---

## Gap 4: No "Why Shop Here" Proof Points on Product Pages

**What the brief says:** Product cards should show stock status, delivery/install note, rebate badge, and decision-enabling information.

**What the site does:** Product cards show model number, category, truncated description, brand logo, and "Price Request." Nothing else. No availability. No delivery window. No rebate badge (even when the product has a rebate — rebate appears as a separate filter/page, not on the card).

**Specific failures:**
- No "In Stock" / "Special Order" / "Call to Confirm" label
- No delivery availability note
- Rebate badge shown on some cards (e.g., FFHT1822UB has a Rebate link) — but it's a link, not a badge with dollar amount
- No dimensions on product cards — users have to click through to spec table
- No "Best For" descriptor

**Fix in rebuild:** Card redesign with: stock status chip, delivery note, rebate $-amount badge if applicable, key dimension (width), and 3 CTAs (Call / Request / Compare).

---

## Gap 5: No Address or Hours in the Global Header/Footer

**What the brief says:** The footer should be rebuilt as a local trust block: address, phone, hours, service areas.

**What the site does:** Footer has 3 links (About Us | Contact Us | Terms and Policies) and the logo. No address. No hours. No phone number. The phone number appears at the top of the page in small text (504-831-2734) but is not a `tel:` link on desktop — only mobile.

**Specific failures:**
- Phone number in header is not consistently a clickable `tel:` link
- Address not in footer
- Hours not in footer or header
- Service area ("metro New Orleans," "greater New Orleans") never stated on the site except in the About page
- No Google Maps embed on home page or footer

**Fix in rebuild:** Footer always shows: Barto Appliance | 3833 Airline Drive, Metairie, LA 70001 | (504) 831-2734 | Mon–Fri 9:30–6, Sat 10–3 | Service area list.

---

## Gap 6: Mobile Header Has No Phone-First UX

**What the brief says:** Phone-first mobile header: Call, Directions, Clearance, Search.

**What the site does:** Uses `maximum-scale=1.0` (prevents pinch-zoom — accessibility violation). The mobile header presumably collapses to a hamburger nav. Phone number exists in tiny top bar. No sticky call button. No "Directions" CTA.

**Fix in rebuild:** Mobile sticky header: [Call] [Directions] [Clearance] [Search] — four touch targets, full width.

---

## Gap 7: Reviews Are Siloed

**What the brief says:** The best reviews should be quoted on the washer/dryer page, the homepage, and an "Older Home Installation" landing page — not buried in a /reviews graveyard.

**What the site does:** 12 reviews live only at `/en/cp-reviews`. They are not referenced anywhere else on the site. The best review (Louis David, March 2024 — older home washer/dryer install, phone purchase, specialty installer) is not surfaced anywhere in the product flow.

**Fix in rebuild:** Review pull quotes component. Louis David's review on: washer/dryer category page, homepage "Why Barto" band, future "Older Home Installation" landing page.

---

## Gap 8: Brand Page Is a Logo Dump

**What the brief says:** Brand page should add positioning: "Speed Queen for long-life laundry," "Frigidaire for budget/value refrigeration," etc.

**What the site does:** 15 brand logos in a grid. No descriptions. No positioning. No "best for." Clicking a brand logo shows that brand's products filtered — which is fine functionally but loses the editorial opportunity.

**Fix in rebuild:** Brand tiles with 1-line positioning copy. Speed Queen gets featured placement (they have a homepage slide).

---

## Gap 9: No Local SEO Pages

**What the brief says:** Build pages for "apartment-size refrigerators Metairie," "washer dryer upstairs older home New Orleans," "room air conditioner Metairie," "clearance appliances New Orleans."

**What the site does:** Zero local SEO landing pages. The refrigerators category page is titled "Refrigerators at Barto Appliance" — no geo. Meta descriptions are empty on every page. og:url is incorrectly set to `https://www.google.com/` on catalog and product pages (Tailbase platform bug).

**Fix in rebuild:** Phase 3 local SEO pages targeting real purchase intent:
- Appliances for Older New Orleans Homes
- Room Air Conditioners — New Orleans + Metairie
- Washer & Dryer Replacement — Older Homes
- Rental Property Appliance Replacement
- Clearance / Scratch & Dent — Metairie
- Kitchen Appliance Packages — New Orleans
- Same-Week Appliance Delivery — Greater New Orleans

---

## Gap 10: Financing Page Is Underdeveloped

**What the brief says:** Financing should be a clear conversion path.

**What the site does:** One sentence about Wells Fargo 12-month 0% + a Acima QR code. No explanation of Acima. No "apply now" link. No financing calculator. No minimum payment examples.

**Fix in rebuild:** Financing page with: Wells Fargo explanation + apply link, Acima explanation (lease-to-own for buyers with credit challenges) + how it works, minimum purchase thresholds, contact CTA.

---

## Gap 11: No Product Inquiry System

**What the brief says:** Every "Call for price" button should also have "Ask about this model," prefilled with SKU/model, customer ZIP, phone, delivery need, and old-appliance haul-away question.

**What the site does:** Generic contact form with no product context. Users have to copy the model number manually, navigate to Contact Us, and re-enter all context.

**Fix in rebuild:** `InquiryModal` component that opens from any product page, pre-populates model + brand, asks: ZIP, phone preferred?, delivery needed?, haul-away?, notes. Sends lead to staff email + logs to `leads` table.

---

## Summary Priority Matrix

| Gap | Impact | Effort | Phase |
|-----|--------|--------|-------|
| No local identity on entry | HIGH | Medium | 1 |
| "Contact Us For Price" dead end | HIGH | Medium | 1 |
| No address/hours in footer | HIGH | Low | 1 |
| Mobile phone-first header missing | HIGH | Low | 1 |
| No stock/delivery on product cards | HIGH | Medium | 1 |
| Clearance nearly empty | HIGH | High (ops) | 1 |
| Reviews siloed | Medium | Low | 1 |
| Brand page is logo dump | Medium | Low | 2 |
| No local SEO pages | Medium | High | 3 |
| Financing underdeveloped | Medium | Low | 2 |
| No product inquiry system | HIGH | Medium | 1 |
| Schema markup missing | Medium | Low | 1 |
| Empty meta descriptions | Medium | Low | 1 |
