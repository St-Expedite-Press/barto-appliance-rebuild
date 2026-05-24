# Work Process Dictionary

Each entry defines a named, repeatable process used in this workspace. Entries include: trigger, inputs, steps, outputs, and which tools or personas are involved.

---

## Process: Project Onboarding

**When:** A new client engagement begins.  
**Trigger:** User asks to start a new project.

**Steps:**
1. Create `projects/[client-slug]/`
2. Write `projects/[client-slug]/CLAUDE.md` — client name, live URL, stack, business data, design constraints
3. Write `projects/[client-slug]/PHASE-PLAN.md` — four-phase skeleton (Audit / Design / Build / Launch)
4. Create directory tree: `audit/designs/`, `audit/screens/`, `audit/scripts/`
5. Add a row to root `README.md` projects table
6. Update `.gitignore` for any project-specific gitignored paths (e.g., `projects/[slug]/dump.md`)

**Outputs:** New project directory with CLAUDE.md, PHASE-PLAN.md, and audit scaffold.

---

## Process: Site Audit

**When:** Phase 1 of any project.  
**Trigger:** `/audit-page` command or manual audit request.  
**Tools:** `screenshot-fast`, `crawl4ai` or `firecrawl`, `playwright`

**Steps:**
1. Screenshot every key page with `screenshot-fast` — save tiled PNGs to `audit/screens/[page-name]/`
2. Extract content with `crawl4ai` or `firecrawl` — capture text, links, structural elements
3. Build `audit/content-inventory.md` — what content exists on the live site
4. Build `audit/design-inventory.md` — extract existing tokens (colors, fonts, spacing, logo)
5. Build `audit/conversion-gaps.md` — document specific failures against the brief
6. Tag each gap with: Impact (High/Medium/Low), Effort, and Phase assignment

**Outputs:** `content-inventory.md`, `design-inventory.md`, `conversion-gaps.md`  
**Gate:** Phase 1 is complete when all key pages are screenshotted and gaps are documented.

---

## Process: Design Variant Generation

**When:** Phase 2. Creating a new homepage mockup.  
**Trigger:** `/new-variant` command or direct request.  
**Tools:** `claude-design`, `page-design-guide`, `screenshot-fast`

**Steps:**
1. Read `audit/designs/design-system-docs.html` for locked tokens and component library
2. Read the baseline variant (`barto-homepage.html` or nearest analog) for content structure
3. Consult `page-design-guide` for trend-appropriate layout patterns if needed
4. Define the palette as CSS custom properties — document the three axes: body color, layout, typographic scale
5. Write the full standalone HTML file with all CSS embedded — no external stylesheets except Google Fonts
6. Include all required content blocks: topbar, header, hero, category grid, trust band, product grid, CTA band, footer
7. Include the floating variant navigator (`<div id="variant-nav">`) — do not omit
8. Save as `audit/designs/variant-[letter or slug].html`
9. Start HTTP server if not running: `.venv/Scripts/python.exe -m http.server 8765 --directory projects/[slug]/audit/designs`
10. Screenshot with `screenshot-fast`, save to `audit/designs/screenshots/`, display frame1

**Outputs:** New `variant-*.html` file, screenshot PNG  
**Constraint:** Brand palette, typography, and business data are locked. Vary only: body color, layout structure, typographic scale, border-radius system, section divider style.

---

## Process: Screenshot Workflow

**When:** Any time a local design mockup needs visual review.  
**Trigger:** `/screenshot-variant` command or inline screenshot request.  
**Tools:** `screenshot-fast` (requires HTTP URL)

**Steps:**
1. Check if HTTP server is running: `curl -s -o /dev/null -w "%{http_code}" http://localhost:8765/barto-homepage.html`
2. If not running, start it: `.venv/Scripts/python.exe -m http.server 8765 --directory projects/barto-appliance/audit/designs` (run in background)
3. Screenshot the file with `screenshot-fast`:
   - `url`: `http://localhost:8765/[filename]`
   - `directory`: absolute path to `projects/[slug]/audit/designs/screenshots/`
   - `waitUntil`: `load`
   - `waitForMS`: 1500
4. Read and display frame1 (and frame2 if page is long) so the user can see it
5. Screenshot multiple variants sequentially, not in parallel — avoids session-close errors

**Outputs:** Timestamped PNG tiles in `audit/designs/screenshots/`  
**Note:** Do not rename timestamp-named output files unless running a full batch cleanup with `audit/scripts/cleanup.py`.

---

## Process: Sandbatch Critique Cycle

**When:** Phase 2. Evaluating one or all design variants.  
**Trigger:** `/sandbatch-review` command or direct critique request.  
**Persona:** C. Sandbatch — read `SANDBATCH.md` in full, including the project overlay section.

**Steps:**
1. Read `SANDBATCH.md` — internalize the register and the project-specific overlay
2. Read `audit/sandbatch-critique.md` to load previously recorded critique for context
3. Screenshot the target variant (or all variants) using the Screenshot Workflow process
4. For each variant, write a critique in Sandbatch register:
   - What it does correctly (dimensional reduction, claim vs. descriptor, provenance mark)
   - What fails, and why — specific and imagistic, not generic
   - One concrete verdict sentence
5. Rank variants relative to one another — explicit ordering, not vague preference
6. Record the critique in `audit/sandbatch-critique.md`

**Voice constraints:**
- Compressed, declarative, imagistically precise
- `&` not `and` · em-dashes freely · no throat-clearing · no "perhaps"
- The Louis David quote is a load-bearing content asset — reference it when critiquing hero conversion
- "1947" is a provenance mark, not a style element — call out misuse

**Outputs:** Updated `audit/sandbatch-critique.md` with critique and ranking  
**Gate:** Critique is complete when all variants have a verdict sentence and a rank.

---

## Process: Variant Improvement

**When:** Phase 2. Applying a targeted improvement brief to raise a variant to 9/10.  
**Trigger:** `/variant-improve [letter]` command.  
**Persona:** C. Sandbatch (for quality judgment)  
**Tools:** `Edit`, `screenshot-fast`

**Steps:**
1. Read `SANDBATCH.md` project overlay — know what the brand actually owns
2. Read `audit/variant-improvement-briefs.md` — find the section for the requested variant
3. Read `audit/sandbatch-critique.md` — understand the diagnosis
4. Take a BEFORE screenshot — save, display labeled "BEFORE"
5. Read the HTML file in full
6. Apply all changes listed in the "Concrete changes" section of the brief:
   - Copy changes (headlines, subheads, body text)
   - CSS token changes (colors, sizes, spacing)
   - Structural HTML changes (remove/add elements)
   - Keep the variant navigator block intact
7. Take an AFTER screenshot — display labeled "AFTER"
8. Report: which changes were applied, any skipped (with reason), one-sentence verdict

**Constraints:**
- Brand palette is locked — do not introduce new colors
- Typography is locked — DM Sans + Playfair Display italic only
- Never remove the Louis David quote if present
- Never introduce glassmorphism, border-radius > 4px on structural elements, or gradients on A/C/D/E/I
- Phone number `(504) 831-2734` must appear in amber `#FFC20E` and be prominent

**Outputs:** Improved HTML file, before/after screenshot pair  

---

## Process: Phase Transition

**When:** All tasks in a phase are marked complete and the next phase is ready to begin.  
**Trigger:** `/phase` command or direct phase status request.

**Steps:**
1. Read `PHASE-PLAN.md` in full
2. Verify all tasks in the current phase are `✅ Done` — if not, surface what's pending
3. Summarize the phase's outputs and key decisions made
4. Identify the first 3 concrete tasks of the next phase, in order
5. Update `PHASE-PLAN.md` if any status rows need correction
6. Report: what changed, what's now unblocked, immediate next action

**Outputs:** Updated `PHASE-PLAN.md` if corrections needed; clear statement of next phase's entry point

---

## Process: Live Page Audit

**When:** Phase 1, or any time the live site needs a spot-check.  
**Trigger:** `/audit-page [path or keyword]` command.  
**Tools:** `screenshot-fast`, `crawl4ai` or `firecrawl`

**Steps:**
1. Resolve keyword to URL using the command's URL shortcut map
2. Screenshot the page with `screenshot-fast` at 1072px — save to `audit/screens/[page-name]/`
3. Scrape content with `crawl4ai` or `firecrawl` for text and structural analysis
4. Audit against the 11 gaps in `audit/conversion-gaps.md`:
   - Address/phone visible?
   - Stock status indicators?
   - Local identity signal?
   - "Contact Us For Price" as only CTA?
   - Schema markup present?
   - Meta description populated?
5. Report findings in the standard format (see `/audit-page` command)
6. Update `audit/conversion-gaps.md` only if new gaps are discovered

**Outputs:** New screenshots, findings report  
**Standard report format:**
```
## [Page] — Audit [date]
### What's on the page
### Gaps found
### New issues
### Verdict
```

---

## Process: Design System Extraction

**When:** Early Phase 2. Before any variant is built.  
**Tools:** `design-copier`, `crawl4ai`, `playwright`

**Steps:**
1. Use `design-copier` to extract live CSS from the client site — convert to Tailwind equivalents
2. Record existing palette (hex values), fonts, and spacing in `audit/design-inventory.md`
3. Make explicit decisions about what to keep, upgrade, or discard from the existing system
4. Lock the new design system: palette tokens, typography rules, required content blocks
5. Document the locked system in `audit/designs/design-system-docs.html`

**Decision framework:**
- Keep: any brand color worth retaining (evaluate for contrast, versatility)
- Upgrade: fonts (replace condensed/generic with DM Sans + Playfair Display)
- Discard: platform-imposed constraints that won't carry to the new build

**Outputs:** `audit/design-inventory.md`, `audit/designs/design-system-docs.html`

---

## Process: Build Scaffold (Phase 3)

**When:** Phase 3 begins. Design system is locked, variant is selected.  
**Tools:** Node.js, Next.js CLI, Drizzle ORM

**Steps:**
1. `npx create-next-app projects/[slug]/[site-dir]` with TypeScript + Tailwind
2. Configure `tailwind.config.ts` with design token variables from Phase 2
3. Set up Drizzle ORM + Postgres connection in `lib/db.ts`
4. Initialize Drizzle schema in `drizzle/schema.ts` — follow the schema design rules in PHASE-PLAN.md
5. Build core components (order: LocalTrustBar → ProductCard → PhoneCTA → FilterDrawer → InquiryModal)
6. Build page routes in priority order: P1 first (homepage, category, product, clearance, contact), then P2, then P3
7. For each page: build route → wire data → screenshot with playwright → verify golden path

**Schema design rule:** Manufacturer data is refreshable via import and must never overwrite local judgment (stock status, clearance flags, pricing notes). Keep them in separate tables.

**Outputs:** Production Next.js codebase in `projects/[slug]/[site-dir]/`
