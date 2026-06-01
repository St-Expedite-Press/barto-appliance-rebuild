# Workspace Ontology

Workspace-level entity taxonomy. Project-specific entities live in each project's own `ONTOLOGY.md`.

---

## Workspace
The root git repository. Contains all projects, shared tooling, and shared personas.

**Attributes:** root path, agency name, git remote  
**Contains:** Projects (1..n), Tools, Persona, Python env, Claude settings

---

## Project
A discrete client engagement with its own git repo and self-contained agent system.

**Slug format:** `[client-kebab-case]`  
**Directory:** `projects/[slug]/`  
**Own agent docs:** `AGENTS.md` · `ONTOLOGY.md` · `PROCESSES.md` · `CLAUDE.md`  
**Own tracking:** `PHASE-PLAN.md` · `MEMORY.md`

For entity taxonomy within a project, read `projects/[slug]/ONTOLOGY.md`.

---

## Tool
A shared software component for automation, extraction, or generation. Workspace-scoped — serves any project.

| Type | Location | Examples |
|------|----------|---------|
| MCP server (local) | `tools/` | `mcp-web-clone`, `design-copier`, `WEB-SCRAPING-MCP` |
| MCP server (remote) | `.mcp.json` via npx | `playwright`, `screenshot-fast`, `firecrawl`, `claude-design` |
| Python package | `.venv/` | playwright, crawl4ai, http.server |
| Script | `projects/[slug]/audit/scripts/` | `cleanup.py`, `gen_logos.py` |

---

## Persona
A named editorial voice. Workspace-scoped base; extended per-project.

**Base:** C. Sandbatch (`SANDBATCH.md` — gitignored at workspace root)  
**Project overlays:** Each project has `[SLUG]_SANDBATCH.md` extending the base (gitignored in each project repo)  
**Invoked for:** design critique, copy, editorial framing, improvement briefs  
**Not invoked for:** structural tasks (lint, schema, indexing, admin)

---

## Slash Command
A Claude Code instruction registered in `.claude/commands/[name].md`. Some are workspace-scoped; most are scoped to a specific project.

| Command | Scope | What it does |
|---------|-------|-------------|
| `/workspace-sync` | workspace | Sync workspace docs against actual state |
| `/screenshot-variant` | barto-appliance | Screenshots a local design variant |
| `/audit-page` | barto-appliance | Audits a live bartoappliances.com page |
| `/new-variant` | barto-appliance | Generates a new design variant |
| `/phase` | barto-appliance | Displays current phase status |
| `/sandbatch-review` | barto-appliance | Runs Sandbatch critique on variants |
| `/variant-improve` | barto-appliance | Applies a variant improvement brief |

---

## Relationship Map

```
Workspace
  ├── Project (1..n)        → projects/[slug]/
  │     └── AGENTS.md · ONTOLOGY.md · PROCESSES.md · CLAUDE.md
  ├── Tool (shared)         → tools/ + .mcp.json
  ├── Persona (shared)      → SANDBATCH.md
  └── Slash Commands        → .claude/commands/
```

---

## Naming Conventions

| Thing | Convention | Example |
|-------|-----------|---------|
| Project slug | kebab-case | `barto-appliance` |
| Slash command | `[verb]-[noun]` | `screenshot-variant` |
| Phase task status | emoji prefix | `✅ Done` · `⏳ Pending` · `🔄 In Progress` |
