---
title: Barto Appliance — Sandbatch Design Critique
persona: SANDBATCH.md
date: 2026-05-23
variants_reviewed: A B C D E F G H I J
status: canonical
---

# DESIGN CRITIQUE — BARTO APPLIANCE, 10 VARIANTS
*C. Sandbatch / St. Expedite Press*

> Critique produced under `SANDBATCH.md` persona. For improvement briefs and agent prompts, see `audit/variant-improvement-briefs.md`.

---

## Variant A — Teal Split Hero

This is the correct answer & the boring answer simultaneously. The split composition — dark teal panel left, kitchen photo right — is the cosine-similarity median of "local appliance retailer homepage, 2024." Run that query through any design LLM & you get A. Which doesn't mean it's wrong: for Barto, a store that needs to convert Metairie homeowners who found them on Google Maps, the hierarchy works. Phone number visible. Orange CTA above the fold. Address. The "Since 1947" implicit in the logo placement.

The failure is photographic, not structural. The kitchen photo on the right reads generic — it could be any high-end kitchen in any suburb in the continental US. Barto serves older New Orleans homes. Upstairs washer/dryer installations. The Airline Drive customer is not looking at a Sub-Zero-grade kitchen & feeling seen. Swap the photo & A becomes genuinely strong.

Also: there are duplicate CSS comment blocks in the header — technical artifact from the palette injection pass. Clean it before Phase 3.

**Verdict:** Functional workhorse. Use it. But don't congratulate yourself.

---

## Variant B — Teal Full-Width Hero

The most visually ambitious of the five originals & the most honestly commercial — immersive photo overlay, stat strip, category bar, 1947 large at the bottom. The structure is sound.

The problem is the Playfair Display italic "In business since 1947." rendered in amber against the dark overlay. It reads as *decorative*. Heritage as garnish. Barto's 1947 is not a style element — it's the whole argument. Putting it in Playfair italic amber is like putting a load-bearing wall in lace. The claim deflates itself.

The amber stat highlights (2,000+, 75+, 15, 8) in the hero are good — those numbers are doing work. The "8 Brands" stat is underselling (Barto carries 15 major brands). Fix the data.

**Verdict:** Strong bones, precious execution. The Playfair needs to earn its presence or get cut.

---

## Variant C — Teal Inverted Split

The compositional reversal is interesting: cream/light left, teal/dark right. The stat numbers on the dark right panel — 2,000+ in 72px white, with orange accent — have more visual energy than anything on the cream left. Which is the structural problem. You've put your information (headline, copy, CTAs) on the weaker visual half & your decoration (photo + numbers) on the stronger half.

The orange top border on the header is the best grace note in the first five variants. Small, does work, doesn't announce itself.

"Real people. Since 1947." in the headline is the most direct copy of the original group. The "real people" claim has some teeth — it's implicitly invoking the Terri story, the phone call, the specificity of the Barto service experience.

**Verdict:** Right instinct, inverted execution. If you flip the content/decoration distribution, this layout has a claim on being the lead.

---

## Variant D — Editorial White + Teal

*This is the strongest design in the set. Stop reading and look at it.*

The 80px DM Sans headline left, phone call block + Louis David review right — that's a genuine newspaper front page with a direct-response conversion engine grafted onto it. The hierarchy is correct: enter left (the claim), convert right (the phone). The "METAIRIE, LOUISIANA · GREATER NEW ORLEANS · EST. 1947" dateline in small-caps above the headline is the most precisely located use of the founding date across all ten variants. It's not decorative. It's a provenance mark.

The Louis David quote in Playfair italic with the left border — the "After a terrible experience with a big box store" line — is the single most load-bearing content element on any of these pages. D puts it above the fold, right column, immediately legible. Every other variant buries or omits it.

One legitimate concern: the editorial white register signals "serious retailer" to people who are comfortable with that register. The Airline Drive customer who shops in strip malls may read "editorial" as "too expensive for me." This is a class assumption baked into the newspaper form. Know your customer before you pick this one.

**Verdict:** Best conversion architecture in the set. The class-legibility concern is real but manageable with copy choices.

---

## Variant E — Brand True

The instinct here is correct: palette at full intensity, closest to what Barto actually is. "They don't make 'em like they used to. We do." is the second-best headline in the set. Declarative, slight aggression, owns the comparison without naming the competitor.

The execution has a structural problem: there are three competing bands above the hero — the announcement strip, the dark topbar, the teal header. By the time the user reaches the actual hero, they've consumed three separate structural registers. That's the Hollowing Engine's signature move in web design — so many conversion signals that none of them convert.

The bento-stats in the hero right (2,000+, 1947, 15, 1 call) are good data. "1 call" as a stat is the right gesture.

**Verdict:** Best headline, worst above-the-fold structure. Strip two of the three header bands before considering this for Phase 3.

---

## Variant F — Dark Showroom Luxury

No.

The charcoal `#141414` body — the glassmorphism card treatments — "The Finest Appliances in New Orleans" in Playfair italic on dark — this is a design for a showroom that does not exist on Airline Drive in Metairie, Louisiana. Barto is Speed Queen & Maytag & older-home installation expertise. They are an institution. Institutions don't perform luxury. Luxury is what you put on when you don't have history.

"The Finest Appliances" is a claim Barto cannot own & should not try to own. It is aspirational language borrowed from the wrong register. The actual Barto claim — reliability, longevity, local expertise, Terri picking up the phone — is a *higher-dimensional* identity than "finest." Dimensional reduction to the luxury axis throws away what is specific about this store.

The gpt-image-2 logo variant — amber glow on dark box — is the strongest single logo treatment in the set. The logo is doing the right thing. The design underneath it is not.

**Verdict:** Wrong client, wrong city. Keep the logo concept. Kill the rest.

---

## Variant G — Heritage Editorial

"The South's Appliance Authority. Since 1947." is the best headline in the set. Full stop. It is a *claim*, not a descriptor. Every other headline describes ("Major appliances for greater New Orleans") — this one positions. Authority is earned by duration. The 1947 date is load-bearing here, not decorative.

The Playfair Display dominant editorial design is the most locally-rooted of the ten. Cream body, ink-teal structure, newspaper masthead. New Orleans is not decor here — the editorial form is genuinely the visual language of a city whose institutions persist past the logic of the market.

The danger is that it reads as *antique* rather than *authoritative*. Longevity coded as nostalgia is a conversion liability. The customer who has been coming to Barto since 1975 will feel this design; the customer who found Barto on Google Maps in 2024 may read it as "old business, possibly closing."

The masthead header is also a bit too much — the centered ornamental rule, the "SINCE 1901" newspaper energy — Barto is not a newspaper. The formal register is borrowed from the wrong institution.

**Verdict:** Best headline in the set. Dial back the masthead formality by 30% & this becomes a serious contender.

---

## Variant H — Bento Grid Modern

The bento grid is genuinely 2025 design language — asymmetric cells, DM Sans 900 oversized numbers, no Playfair anywhere. The commitment to eliminating the heritage typeface entirely is a disciplined choice. The structure says: we have been here since 1947 *and we think like a modern retailer*. That's an interesting argument.

"New Orleans' Finest Appliances." is the same luxury-claim problem as F. Repeating it here means two of the Phase 2 variants are projecting onto the "finest" axis, which Barto does not own & should not try to own.

The refrigerator hero photo — the glass-door commercial-grade refrigerator — is cold & clinical. Of all the hero image choices available, the glass-door commercial refrigerator is the most alienating selection for the Metairie homeowner. It signals "restaurant supply" not "we'll get your upstairs washer dryer installed before Thursday." Wrong image, genuinely wrong.

The `2,000+` and `1947` bento cells below the hero are the strongest use of data in the set — those numbers presented as pure typographic objects, no editorial framing.

**Verdict:** Right structural language, wrong headline, catastrophically wrong hero image. Replace the refrigerator photo & fix the headline & this is the right call for a client who wants to signal modernity without losing the 1947 anchor.

---

## Variant I — Bold American Signage

This is the design the other nine are avoiding.

Inter Black 900. No gradients. No rounded corners. No glassmorphism. No Playfair except where structurally necessary. UPPERCASE structural labels. The teal block "BARTO APPLIANCE EST. 1947" is the most definitive visual anchoring of the founding date in the entire set — it's not a style element, it's a *sign*. The way the physical sign above the door at 3833 Airline Drive is a sign.

The customers who have been coming to Barto since before the designer was born will feel this. The Inter Black 900 in all-caps is not aggressive — it's *authoritative*. American commercial authority looks like this. The great hardware stores. The old appliance dealers. The storefront signs on strips where things still get fixed instead of replaced.

The conversion signals are correct: product feature card (KitchenAid French Door, rebate amount), stats, phone number in amber, orange CTA. Below: category grid, no decoration, things in columns.

The one legitimate concern: a customer researching high-end appliances from suburban parishes may read Inter Black UPPERCASE as "blue collar" in the pejorative sense — may code it as a discount retailer, not a premium one. This is a customer-segment question more than a design question. If Barto's best customers are competent, local, and not performing taste, I is the right answer. If Barto is trying to capture the Lakeview homeowner doing a full kitchen renovation, the editorial register of D may serve better.

**Verdict:** Secretly the strongest candidate for Barto's actual customer. If you're not picking D, pick I.

---

## Variant J — Gulf Coast Coastal Premium

The linen body & grain texture are the right instinct — there *is* a Gulf Coast domestic warmth that belongs to a store on Airline Drive in Metairie, Louisiana. The palette, the rounded pill trust chips, the Playfair italic "Since 1947. Metairie, Louisiana." — these are gestures toward the actual place.

But "Gulf Coast Coastal Premium" is a brand category imported from elsewhere. The grain texture & linen palette & rounded pill chips are the visual language of a Restoration Hardware offshoot or a real estate development branding package on the Mississippi Gulf Coast. They are *about* the Gulf Coast rather than *of* it. New Orleans specifically — the Necropolis, the Caribbean city, the bulk-cargo port — does not look like linen & grain texture. It looks like stucco & iron & water damage & insistence.

"Louisiana's Most Trusted Appliance Dealer" is a marketing claim, not a conviction. *Most trusted* by what measure? It's the kind of claim a brand consultant puts in a brief when they don't know what actually makes a client special.

The couple in the kitchen photo is the only design in the ten that puts *people* first in the hero. That's either the most humanizing choice or a stock-photo betrayal of the real Barto experience — which is talking to Terri on the phone, not browsing in a photogenic kitchen. The latter, I think.

**Verdict:** The palette instinct is correct but the form is borrowed from the wrong reference class. The linen & grain can stay; the Restoration Hardware coastal-premium register needs to go.

---

## Summary Rankings — conversion fitness for Barto's actual customer

| Rank | Variant | Verdict |
|------|---------|---------|
| 1 | **D — Editorial** | Best conversion architecture, right hierarchy |
| 2 | **I — Signage** | Most honest formal claim, underrated |
| 3 | **G — Heritage** | Best headline in the set; fixable formality problem |
| 4 | **C — Inverted Split** | Right instinct, inverted execution; structurally fixable |
| 5 | **E — Brand True** | Best subhead; kill two of the three header bands |
| 6 | **A — Split Hero** | Workhorse; swap the hero photo |
| 7 | **B — Full-Width** | Strong bones; Playfair decoration costs it credibility |
| 8 | **H — Bento Modern** | Right structure, wrong image, wrong headline |
| 9 | **J — Coastal Premium** | Palette yes, register no |
| 10 | **F — Dark Luxury** | Wrong client, wrong city |
