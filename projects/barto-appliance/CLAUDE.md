# barto-appliance — Project Instructions

**Persona:** Read `BARTO_SANDBATCH.md` (this directory) before any editorial, critique, or copy task. It extends `../../SANDBATCH.md` — read both, project overlay last.  
**Change log:** All changes to this project must be logged in `MEMORY.md` (this directory) immediately after completion.  
**Orchestration:** The main agent routes work to subagents. See root `CLAUDE.md` for delegation table and session lifecycle.

**Client:** Barto Appliance · 3833 Airline Drive, Metairie, LA 70001  
**Live site:** bartoappliances.com (Tailbase/ColdFusion — full custom rebuild)  
**Stack:** Next.js · Drizzle · Postgres · Tailwind  
**Hosting target:** Replit Reserved VM → custom domain  
**Phase plan:** `PHASE-PLAN.md` — check here first for current status.

---

## Python Environment

Use the workspace venv (at repo root):

```
../../.venv/Scripts/python.exe   # Python interpreter
../../.venv/Scripts/pip.exe      # Package installer
../../.venv/Scripts/playwright   # Playwright CLI
```

Or from the workspace root: `.venv\Scripts\python.exe`

---

## Editorial & Critique Persona

**`BARTO_SANDBATCH.md`** (this directory) — project-specific persona extending `../../SANDBATCH.md`. Read both before any editorial, critique, or copy task. The base persona establishes voice and doctrine; the project overlay grounds it in Barto's identity, geography, and content assets.

- Critique records: `audit/sandbatch-critique.md`
- Improvement briefs (variants → 9/10): `audit/variant-improvement-briefs.md`

---

## Design System (Phase 2 complete)

**Shared brand palette (all variants):**
- Teal `#004A6E` — header / nav / structural
- Orange `#E8871A` — primary CTAs
- Amber `#FFC20E` — phone / accent highlights
- Red `#C8321E` — clearance / sale
- Cream `#FAF7F2` — body background

**Typography (locked):**
- UI/body: DM Sans
- Heritage callouts only: Playfair Display italic ("Since 1947", pull quotes)

---

## Variants (all in `audit/designs/`)

| File | Variant | Description | Critique rank |
|------|---------|-------------|---------------|
| `barto-homepage.html` | A | Teal Split Hero | — |
| `variant-b-navy-brass.html` | B | Teal Full-Width + Amber | — |
| `variant-c-slate-rust.html` | C | Teal Inverted Split | — |
| `variant-d-editorial-white.html` | D | Editorial White + Teal | #1 |
| `variant-e-brand-true.html` | E | Brand True (most expressive) | — |
| `variant-f-dark-luxury.html` | F | Dark Showroom Luxury | #10 (pivot required) |
| `variant-g-heritage-editorial.html` | G | New Orleans Heritage Editorial | best headline |
| `variant-h-bento-modern.html` | H | Bento Grid Modern | — |
| `variant-i-bold-signage.html` | I | Bold American Signage | #2 |
| `variant-j-coastal-premium.html` | J | Gulf Coast Coastal Premium | — |
| `barto-category.html` | — | Category listing page | — |
| `barto-product-detail.html` | — | Product detail page | — |

**Logo variants** (`audit/designs/images/`): `logo-variant-[a-j].png` — gpt-image-2 generated per variant aesthetic.

---

## Local Preview Server

Start from the workspace root:

```bash
.venv/Scripts/python.exe -m http.server 8765 --directory projects/barto-appliance/audit/designs
# http://localhost:8765/
```

---

## Project Structure

```
projects/barto-appliance/
  CLAUDE.md                     # This file
  PHASE-PLAN.md                 # Full phase tracking (Phases 1–4)
  README.md                     # Client-facing project showcase
  dump.md                       # Raw brief / discovery notes (gitignored)
  audit/
    content-inventory.md
    conversion-gaps.md          # 11 gaps with fixes
    design-directory.md
    design-inventory.md
    sandbatch-critique.md       # Recorded Sandbatch critique (gitignored)
    variant-improvement-briefs.md
    content/                    # Raw content dumps (gitignored)
    designs/                    # HTML mockups
      images/                   # Logo + stock photos
      screenshots/              # Captured screenshots
      design-system-docs.html
    screens/                    # Live site screenshots (audit baseline)
    scripts/                    # Python utility scripts
```

---

## Key Business Data

```
Name:     Barto Appliance
Address:  3833 Airline Drive, Metairie, LA 70001
Phone:    (504) 831-2734
Hours:    Mon–Fri 9:30 AM–6:00 PM (Fri closes 5:30 PM) · Sat 10:00 AM–3:00 PM · Sun Closed
Geo:      29.9756398, -90.1685747
Since:    1947
Stock:    2,000+ appliances and air conditioners
Areas:    Metairie · New Orleans · Kenner · Jefferson Parish · Greater New Orleans
```

**Brands:** Amana · Avanti · Comfort-Aire · Electrolux · Frigidaire · Frigidaire Gallery · Frigidaire Professional · KitchenAid · Maytag · Maytag Commercial Laundry · Sharp · Speed Queen · Thor Kitchen · Vitara · Whirlpool

**Hero review (use site-wide):**
> "After a terrible experience with getting an unnamed big box store to install a washer/dryer upstairs in an older home, I called Barto and Terri took care of it all! I bought the washer dryer over the phone, and she connected me with a specialty installer."
> — Louis David, March 2024 · Google Review
