# barto-rebuild — Claude Code Workspace

Web development workspace for the Barto Appliance site rebuild.
**Live site:** bartoappliances.com (Tailbase/ColdFusion — full custom rebuild)
**Phase plan:** `PHASE-PLAN.md` — check here first for current status.

---

## Python Environment

Always use the project venv:

```
.venv\Scripts\python.exe   # Python interpreter
.venv\Scripts\pip.exe      # Package installer
.venv\Scripts\playwright   # Playwright CLI (Chromium installed)
```

Never use bare `python` or `pip`.

---

## Project Skills (Slash Commands)

| Command | What it does |
|---------|-------------|
| `/screenshot-variant` | Screenshots a local design variant for review |
| `/audit-page` | Audits a live bartoappliances.com page |
| `/new-variant` | Generates a new design variant |
| `/phase` | Displays current phase status |

---

## Repo Structure

```
barto-rebuild/
  audit/
    designs/            # All HTML mockups (5 variants + category + product)
      images/           # Barto logo + stock photos (Unsplash CDN)
      screenshots/      # Captured screenshots of designs
      design-system-docs.html
    screens/            # Live bartoappliances.com screenshots (audit baseline)
    content-inventory.md
    conversion-gaps.md  # 11 conversion gaps with fixes
    design-inventory.md
  CLAUDE.md             # This file
  PHASE-PLAN.md         # Full phase tracking
  README.md             # Client-facing project showcase
```

---

## Design System (Phase 2 complete)

**Shared brand palette (all variants):**
- Teal `#004A6E` — header / nav / structural
- Orange `#E8871A` — primary CTAs
- Amber `#FFC20E` — phone / accent highlights
- Red `#C8321E` — clearance / sale
- Cream `#FAF7F2` — body background

**Variants** (all in `audit/designs/`):
- `barto-homepage.html` — Variant A: Teal Split Hero
- `variant-b-navy-brass.html` — Variant B: Teal Full-Width Hero
- `variant-c-slate-rust.html` — Variant C: Teal Inverted Split
- `variant-d-editorial-white.html` — Variant D: Editorial White + Teal
- `variant-e-brand-true.html` — Variant E: Brand True (most expressive)
- `barto-category.html` — Category listing page
- `barto-product-detail.html` — Product detail page

**Typography (locked):**
- UI/body: DM Sans
- Heritage callouts only: Playfair Display italic ("Since 1947", pull quotes)

**Local preview server:**
```bash
.venv/Scripts/python.exe -m http.server 8765 --directory audit/designs
# http://localhost:8765/
```

---

## MCP Servers (`.claude/settings.json`)

| Server | Use for |
|--------|---------|
| `playwright` | Browser automation, DOM extraction (primary) |
| `playwright-ea` | API endpoint testing alongside browser |
| `screenshot-fast` | Full-page screenshots tiled at 1072×1072 (requires HTTP URL) |
| `firecrawl` | Clean content extraction, site crawls (needs `FIRECRAWL_API_KEY`) |
| `crawl4ai` | Local/keyless crawling, query extraction |
| `web-cloner` | Clone webpage sections |
| `design-copier` | Extract live CSS, convert to Tailwind |
| `claude-design` | Generate/iterate HTML+CSS designs |
| `page-design-guide` | 2024–2026 design trends and layout patterns |

---

## Workflow Patterns

### Preview a design
1. Start server: `.venv/Scripts/python.exe -m http.server 8765 --directory audit/designs`
2. Screenshot: `screenshot-fast` at `http://localhost:8765/[file].html`
3. Read frame1 tile to review

### Audit the live site
1. `screenshot-fast` on live URL
2. `crawl4ai` or `firecrawl` for content extraction
3. Update `audit/conversion-gaps.md`

### Start Phase 3 (Next.js)
1. Read `PHASE-PLAN.md` sections 3A–3F
2. Review `audit/designs/design-system-docs.html` for tokens/components
3. Target dir: `barto-site/` at repo root

---

## Keys & Secrets (in `.env`, gitignored)

| Key | Used by |
|-----|---------|
| `OPENAI_API_KEY` | crawl4ai smart extraction |
| `FIRECRAWL_API_KEY` | firecrawl MCP |
| `AWS_*` | AWS services |
| `GITHUB_PAT_WRITE` | GitHub repo ops |
