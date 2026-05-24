# Web Design Workspace

**Agency:** St. Expedite Press  
**Purpose:** Multi-project web design and rebuild workspace — audit, design system, and production build for client sites.

See `ONTOLOGY.md` for the full entity taxonomy. See `PROCESSES.md` for the dictionary of named work processes.

---

## Projects

| Slug | Client | Live URL | Stack | Phase |
|------|--------|----------|-------|-------|
| [barto-appliance](projects/barto-appliance/) | Barto Appliance · Metairie, LA | bartoappliances.com | Next.js · Drizzle · Postgres · Tailwind | Phase 3 pending |

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
    barto-appliance/
      CLAUDE.md
      PHASE-PLAN.md
      README.md
      audit/
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
