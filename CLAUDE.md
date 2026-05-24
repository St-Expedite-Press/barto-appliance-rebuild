# Web Design Workspace — Claude Code Instructions

This is a generalized web design agency workspace. Each client project lives in `projects/[slug]/`. Shared tooling, the Python environment, and the editorial persona live at the root.

See **`ONTOLOGY.md`** for the full taxonomy of entities in this repo.  
See **`PROCESSES.md`** for the dictionary of named work processes.

---

## Workspace Structure

```
(root)/
  CLAUDE.md           # This file — workspace-level instructions
  ONTOLOGY.md         # Entity taxonomy and relationship map
  PROCESSES.md        # Dictionary of named work processes
  README.md           # Workspace overview
  SANDBATCH.md        # C. Sandbatch editorial persona (shared, gitignored)
  projects/
    [slug]/           # One directory per client project
      CLAUDE.md       # Project-specific instructions
      PHASE-PLAN.md   # Phase tracking
      README.md       # Client-facing showcase
      audit/          # Audit artifacts, designs, screenshots
  tools/              # Shared MCP server implementations (gitignored)
  .venv/              # Shared Python environment (gitignored)
  .claude/            # Claude Code settings and slash commands
  .mcp.json           # MCP server configuration (gitignored)
  .env                # API keys and secrets (gitignored)
```

**When starting work on a project:** read `projects/[slug]/CLAUDE.md` first.

---

## Python Environment

Always use the workspace venv:

```
.venv\Scripts\python.exe   # Python interpreter
.venv\Scripts\pip.exe      # Package installer
.venv\Scripts\playwright   # Playwright CLI (Chromium installed)
```

Never use bare `python` or `pip`.

---

## Editorial Persona

**`SANDBATCH.md`** — C. Sandbatch persona. Invoke for any editorial, critique, copy, or voice-led work on any project. The persona is project-agnostic; each project's CLAUDE.md notes the relevant overlay section.

---

## Slash Commands (`.claude/commands/`)

| Command | Scope | What it does |
|---------|-------|-------------|
| `/screenshot-variant` | barto-appliance | Screenshots a local design variant |
| `/audit-page` | barto-appliance | Audits a live bartoappliances.com page |
| `/new-variant` | barto-appliance | Generates a new design variant |
| `/phase` | barto-appliance | Displays current phase status |
| `/sandbatch-review` | barto-appliance | Runs Sandbatch critique on variants |
| `/variant-improve` | barto-appliance | Applies a variant improvement brief |

---

## MCP Servers (`.mcp.json`)

| Server | Use for |
|--------|---------|
| `playwright` | Browser automation, DOM extraction |
| `playwright-ea` | API endpoint testing alongside browser |
| `screenshot-fast` | Full-page screenshots tiled at 1072×1072 (requires HTTP URL) |
| `firecrawl` | Clean content extraction, site crawls |
| `crawl4ai` | Local/keyless crawling, query extraction |
| `web-cloner` | Clone webpage sections |
| `design-copier` | Extract live CSS, convert to Tailwind |
| `claude-design` | Generate/iterate HTML+CSS designs |
| `page-design-guide` | 2024–2026 design trends and layout patterns |

---

## Keys & Secrets (in `.env`, gitignored)

| Key | Used by |
|-----|---------|
| `OPENAI_API_KEY` | crawl4ai smart extraction |
| `FIRECRAWL_API_KEY` | firecrawl MCP |
| `AWS_*` | AWS services |
| `GITHUB_PAT_WRITE` | GitHub repo ops |

---

## Adding a New Project

1. Create `projects/[client-slug]/`
2. Write `projects/[client-slug]/CLAUDE.md` — client info, live URL, stack, design system
3. Write `projects/[client-slug]/PHASE-PLAN.md` — phases and task tracking
4. Create `projects/[client-slug]/audit/` with subdirs: `designs/`, `screens/`, `scripts/`
5. Register project-scoped slash commands in `.claude/commands/` if needed
6. Update `.gitignore` for project-specific gitignored paths
