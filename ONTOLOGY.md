# Workspace Ontology

This document defines the entity types, their attributes, and their relationships within this web design workspace. It is the authoritative reference for how work is organized.

---

## Entity Types

### Workspace
The root git repository. Contains all projects, shared tooling, and shared personas.

**Attributes:** root path, agency name, git remote  
**Contains:** Projects (1..n), Tools, Persona, Python env, Claude settings

---

### Project
A discrete client engagement with its own audit trail, design system, and build target.

**Slug format:** `[client-kebab-case]` (e.g., `barto-appliance`)  
**Directory:** `projects/[slug]/`  
**Attributes:** client name, live URL, tech stack, current phase  
**Contains:** Phases, Artifacts, CLAUDE.md, PHASE-PLAN.md, README.md

**Key files:**
```
projects/[slug]/
  CLAUDE.md           # Project-specific Claude Code instructions
  PHASE-PLAN.md       # Authoritative phase and task tracker
  README.md           # Client-facing project showcase
  dump.md             # Raw discovery/brief notes (gitignored)
  audit/              # All audit-phase and design-phase artifacts
```

---

### Phase
A named, sequential stage of project work. Phases are tracked in `PHASE-PLAN.md`.

**Types:**
| Phase | Name | Produces |
|-------|------|----------|
| 1 | Audit | Screens, content inventory, conversion gaps, design inventory |
| 2 | Design System | HTML variants, design-system-docs, critique, improvement briefs |
| 3 | Build | Production codebase (Next.js or equivalent) |
| 4 | Launch / Post-Launch | Deployment, enhanced features, CRM, analytics |

**Statuses:** `⏳ Pending` · `🔄 In Progress` · `✅ Complete` · `❌ Blocked`

---

### Artifact
A concrete output produced during a phase. Artifacts live in `projects/[slug]/audit/`.

**Artifact types:**

| Type | Directory | Description |
|------|-----------|-------------|
| `screen` | `audit/screens/[page]/` | Screenshot of a live site page (tiled PNGs) |
| `design-variant` | `audit/designs/` | Standalone HTML mockup of a homepage or page |
| `supporting-page` | `audit/designs/` | Category, product, or utility page mockup |
| `design-system-doc` | `audit/designs/` | Full token/component documentation page |
| `content-inventory` | `audit/` | Structured list of all content on the live site |
| `conversion-gap` | `audit/` | Documented gap between current site and desired outcome |
| `design-inventory` | `audit/` | Existing design tokens extracted from the live site |
| `design-directory` | `audit/` | Full element inventory, logo brief, modernization guide |
| `sandbatch-critique` | `audit/` | Ranked critique of all variants in Sandbatch register |
| `improvement-brief` | `audit/` | Per-variant agent prompt to reach 9/10 quality |
| `screenshot` | `audit/designs/screenshots/` | Captured screenshot of a local design variant |

---

### Design Variant
A specific homepage layout approach, implemented as a self-contained HTML file.

**Attributes:** letter (a–j), palette, layout approach, critique rank, improvement-brief status  
**File:** `audit/designs/[variant-filename].html`  
**Screenshot:** `audit/designs/screenshots/variant-[letter]-[slug].png`  
**Logo:** `audit/designs/images/logo-variant-[letter].png`

**Variant identity is defined by three axes:**
1. **Body color** — cream, white, dark, linen
2. **Layout structure** — split hero, full-width, editorial, bento grid, signage
3. **Typographic scale** — DM Sans dominant vs. Playfair Display callouts

All variants share the brand palette and content structure. What differs is how those are applied.

---

### Tool
A shared software component used for automation, extraction, or generation. Not project-specific.

**Types:**
| Type | Location | Examples |
|------|----------|---------|
| MCP server (local) | `tools/` | `mcp-web-clone`, `design-copier`, `WEB-SCRAPING-MCP` |
| MCP server (remote) | `.mcp.json` via npx | `playwright`, `screenshot-fast`, `firecrawl`, `claude-design` |
| Python package | `.venv/` | playwright, crawl4ai, http.server |
| Script | `projects/[slug]/audit/scripts/` | `cleanup.py`, `gen_logos.py` |

**Tools are workspace-scoped** — they serve any project, not one specific project.

---

### Persona
A named editorial voice used for critique, copy, and voice-led work.

**Current persona:** C. Sandbatch (see `SANDBATCH.md`)  
**Used for:** design critique, headline copy, editorial framing, improvement briefs  
**Project overlay:** Each project's CLAUDE.md notes the relevant brand/identity context to apply over the base persona.

**Persona is workspace-scoped** — it applies to any project's editorial work.

---

### Slash Command
A reusable Claude Code instruction registered in `.claude/commands/[name].md`.

**Attributes:** name, project scope, description, argument types  
**Current commands:**

| Command | Project scope | Arguments |
|---------|--------------|-----------|
| `/audit-page` | barto-appliance | page path or keyword |
| `/screenshot-variant` | barto-appliance | variant letter (a–j), page name, or blank |
| `/new-variant` | barto-appliance | palette/mood description |
| `/phase` | barto-appliance | phase number (optional) |
| `/sandbatch-review` | barto-appliance | variant letter or blank |
| `/variant-improve` | barto-appliance | variant letter |

Commands scoped to a specific project use that project's artifact paths. Commands intended for reuse across projects are noted as workspace-scoped.

---

## Relationship Map

```
Workspace
  ├── Project (1..n)
  │     ├── Phase (1..4)
  │     │     └── Artifact (0..n)
  │     │           └── Design Variant → Screenshot
  │     │                             → Logo Variant
  │     └── CLAUDE.md · PHASE-PLAN.md · README.md
  ├── Tool (shared)
  │     ├── MCP server (local) → tools/
  │     └── MCP server (remote) → .mcp.json
  ├── Persona (shared) → SANDBATCH.md
  ├── Python env (shared) → .venv/
  └── Slash Commands → .claude/commands/
        └── scoped-to → Project
```

---

## Directory Semantics

| Path | What lives here |
|------|----------------|
| `projects/` | One subdirectory per client project |
| `projects/[slug]/audit/designs/` | HTML mockups — all self-contained, no build step |
| `projects/[slug]/audit/designs/images/` | Project brand assets + stock photos |
| `projects/[slug]/audit/designs/screenshots/` | Captured screenshots of local mockups |
| `projects/[slug]/audit/screens/` | Live-site screenshots organized by page |
| `projects/[slug]/audit/scripts/` | Project-specific Python utility scripts |
| `tools/` | MCP server source code (local servers only) |
| `.venv/` | Shared Python environment for all tools and scripts |
| `.claude/commands/` | Slash command definitions |

---

## Naming Conventions

| Thing | Convention | Example |
|-------|-----------|---------|
| Project slug | kebab-case, client + disambiguator if needed | `barto-appliance` |
| Design variant file | `variant-[letter]-[adjective-noun].html` | `variant-d-editorial-white.html` |
| Screenshot | `variant-[letter]-[slug].png` | `variant-d-editorial.png` |
| Logo variant | `logo-variant-[letter].png` | `logo-variant-d.png` |
| Slash command | `[verb]-[noun]` | `screenshot-variant`, `audit-page` |
| Phase task status | emoji prefix | `✅ Done` · `⏳ Pending` · `🔄 In Progress` |
