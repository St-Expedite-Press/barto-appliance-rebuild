# [CLIENT NAME] — Process Dictionary

Project-specific processes. Workspace-level processes (Session Lifecycle, Orchestration, Change Logging, Workspace Maintenance, Project Onboarding, Phase Transition) live in root `PROCESSES.md`.

**Process index:**
- [Site Audit / Discovery](#process-site-audit--discovery)
- [Design Variant Generation](#process-design-variant-generation)
- [Sandbatch Critique](#process-sandbatch-critique)
- [Build Scaffold](#process-build-scaffold)

---

## Process: Site Audit / Discovery

**When:** Phase 1.  
**Tools:** `screenshot-fast`, `firecrawl`, `playwright`

**Steps:**
1. Screenshot all key pages — save to `audit/screens/[page]/`
2. Extract content with `firecrawl` — build `audit/content-inventory.md`
3. Document conversion gaps — `audit/conversion-gaps.md`
4. Extract design tokens from live site — `audit/design-inventory.md`

---

## Process: Design Variant Generation

**When:** Phase 2.  
**Tools:** `claude-design`, `page-design-guide`, `screenshot-fast`

**Steps:**
1. Read brand docs in `brand/` before generating
2. Write self-contained HTML — all CSS embedded
3. Save to `audit/designs/[name].html`
4. Start HTTP server: `.venv/Scripts/python.exe -m http.server 876X --directory projects/[slug]/audit/designs`
5. Screenshot and display

---

## Process: Sandbatch Critique

**When:** Phase 2. Evaluating design variants.  
**Persona:** C. Sandbatch — read `../../SANDBATCH.md` + `[SLUG]_SANDBATCH.md`

**Steps:**
1. Read both persona files
2. Screenshot target variant(s)
3. For each: what it does correctly · what fails · one verdict sentence
4. Rank explicitly

---

## Process: Build Scaffold

**When:** Phase 3. Design locked, variant selected.

**Steps:**
1. [Define stack-specific steps here]
2. Build core components first
3. Build page routes in priority order
4. Run check suite before each commit
