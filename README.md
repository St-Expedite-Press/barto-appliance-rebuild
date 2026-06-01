# Web Design Workspace

**Agency:** St. Expedite Press  
**Purpose:** Multi-project web design and rebuild workspace — audit, design system, and production build for client sites.

See `ONTOLOGY.md` for the full entity taxonomy. See `PROCESSES.md` for the dictionary of named work processes.

---

## Projects

| Slug | Client | Live URL | Stack | Phase |
|------|--------|----------|-------|-------|
| [barto-appliance](projects/barto-appliance/) | Barto Appliance · Metairie, LA | bartoappliances.com | Next.js · Drizzle · Postgres · Tailwind | Phase 3 pending |
| [dixie-mag](projects/dixie-mag/) | The Dixie · New Orleans, LA | Not yet launched | TBD | Phase 2 — Identity |
| [st-expedite-press](projects/st-expedite-press/) | St. Expedite Press | stexpedite.press | Astro · Cloudflare Pages · D1 · Worker | Phase 2 — live, deploy-ready |
| [ogc](projects/ogc/) | OGC | Not yet launched | TBD | Phase 2 — Identity |

---

## Workspace Layout

```
(root)/
  CLAUDE.md         # Workspace-level Claude Code instructions
  ONTOLOGY.md       # Entity taxonomy and relationship map
  PROCESSES.md      # Dictionary of named work processes
  README.md         # This file
  SANDBATCH.md      # C. Sandbatch editorial persona (gitignored)
  projects/
    _template/      # Standard project scaffold (copy to start a new project)
    barto-appliance/
    dixie-mag/
    st-expedite-press/  # ← full codebase (nested git repo) + workspace tracking merged into one
    ogc/
    [slug]/         # Each project follows the same layout:
      CLAUDE.md           # Client info, stack, persona ref
      [SLUG]_SANDBATCH.md # Project persona extending ../../SANDBATCH.md
      PHASE-PLAN.md       # Phase and task tracking
      MEMORY.md           # Change log (gitignored)
      README.md           # Client-facing showcase
      brand/              # Brand system docs (palette, typography, voice)
      audit/              # Designs, screenshots, content inventory
      assets/             # Logos, source images, fonts
  tools/            # Shared MCP server implementations (gitignored)
  .venv/            # Shared Python environment (gitignored)
  .claude/          # Slash commands and Claude Code settings
```

---

## Shared Infrastructure

**Python env:** `.venv/` — Playwright, crawl4ai, web-cloner, utility scripts  
**MCP servers:** playwright · playwright-ea · screenshot-fast · firecrawl · crawl4ai · web-cloner · design-copier · claude-design · page-design-guide  
**Editorial persona:** C. Sandbatch — `SANDBATCH.md`

---

*Built by [St. Expedite Press](https://github.com/St-Expedite-Press)*
