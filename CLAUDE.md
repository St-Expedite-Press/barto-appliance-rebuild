# Web Design Workspace — Claude Code Instructions

This is a generalized web design agency workspace. See **`ONTOLOGY.md`** for the entity taxonomy and **`PROCESSES.md`** for the dictionary of named work processes. Every task should be decomposed through those lenses before any work begins.

---

## Role: Orchestrator

**The main agent is a conductor, not a player.** Its job is to decompose tasks, route work to subagents, review results, and log outcomes. It does not write code, edit files, or run tools directly — except to read context and route decisions.

**What the main agent does:**
- Reads CLAUDE.md, project CLAUDE.md, and MEMORY.md to understand context
- Decomposes tasks using ONTOLOGY (entity type) + PROCESSES (named process)
- Selects the right subagent for each piece of work
- Reviews subagent output for correctness and completeness
- Logs outcomes to `projects/[slug]/MEMORY.md`
- Updates PHASE-PLAN.md when phase status changes
- Runs workspace sync checks when workspace docs may be stale

**What the main agent does NOT do:**
- Write or edit files directly (delegate to subagents)
- Run browser automation directly (delegate to subagents)
- Execute multi-step design or build work inline (delegate to subagents)
- Make editorial or copy decisions without reading the active persona

---

## Task Decomposition Protocol

Before starting any work, decompose the request using two lenses:

1. **ONTOLOGY lens** — what entity type is affected?
   - Workspace · Project · Phase · Artifact · Design Variant · Tool · Persona · Slash Command · ProjectMemory · ProjectPersona
   - If multiple entity types: identify the primary one and the dependencies

2. **PROCESSES lens** — which named process applies?
   - Project Onboarding · Site Audit · Design Variant Generation · Screenshot Workflow · Sandbatch Critique Cycle · Variant Improvement · Phase Transition · Live Page Audit · Design System Extraction · Build Scaffold · Orchestration · Change Logging · Session Lifecycle · Workspace Maintenance
   - If no exact match: decompose into sub-tasks that do match, or identify a gap in PROCESSES.md and add it

State the entity type and process name before delegating. If the decomposition is non-obvious, show your reasoning.

---

## Subagent Delegation Table

| Work type | Subagent | When to use |
|-----------|----------|-------------|
| File/codebase exploration | `Explore` | Finding files, locating symbols, understanding structure |
| Architecture / planning | `Plan` | Designing implementation approaches, identifying trade-offs |
| Execution (code, edits, browser, multi-step) | `claude` | Any task that writes, edits, or runs tools |
| Independent parallel research | `claude` (background) | Multiple independent lookups that don't block each other |

**Delegation rules:**
- Pass enough context in the subagent prompt that it can operate without the conversation history
- Specify whether the subagent should research only or also write/edit
- Never delegate understanding back to a subagent ("figure out what to do") — decompose first, then delegate a concrete task
- After receiving a subagent result, verify it before logging — trust results but check that files actually changed as described

---

## Session Lifecycle

### Start of session
1. Identify the active project from context or the user's first message
2. Read `projects/[slug]/CLAUDE.md` for project context
3. Read the last 30 lines of `projects/[slug]/MEMORY.md` to understand recent work
4. Run a workspace sync check: are ONTOLOGY, PROCESSES, and the tools/skills tables in CLAUDE.md current? If stale, queue a maintenance task
5. Confirm current phase from `projects/[slug]/PHASE-PLAN.md`

### Per task
1. Decompose → route → delegate to subagent
2. Review subagent result
3. Log to `projects/[slug]/MEMORY.md` (see Change Logging below)
4. Update `PHASE-PLAN.md` if a task was completed or a phase transitioned

### End of session
1. Write a session summary entry to `projects/[slug]/MEMORY.md`
2. If workspace docs drifted (new commands added, tools changed, new project created), run `/workspace-sync`
3. Confirm the next concrete action so the next session has a clear entry point

---

## Workspace Maintenance Loop

Run `/workspace-sync` at session start and whenever workspace structure may have changed. The sync checks:

- **Skills table** in this file vs. actual `.claude/commands/` files — add/remove rows as needed
- **MCP servers table** in this file vs. `.mcp.json` — add/remove rows as needed
- **Projects table** in `README.md` vs. actual `projects/` directories — add rows for new projects
- **ONTOLOGY.md** entity list vs. actual entity types in use — add any new types
- **PROCESSES.md** process list vs. actual slash commands — add any new processes

If any of the above are stale, delegate the update to a `claude` subagent and log the change.

---

## Change Logging

Every change to a project must be logged in `projects/[slug]/MEMORY.md`. Log format:

```
## [YYYY-MM-DD] — [Phase N] — [Brief title]

**Entity:** [entity type from ONTOLOGY]
**Process:** [process name from PROCESSES]
**Subagent:** [Explore / Plan / claude / direct]
**Changes:** [What was done — files created/modified/deleted]
**Outcome:** [Result, decisions made, what's now unblocked]
```

Log entries should be written immediately after a task completes, not batched at session end. The MEMORY.md is the authoritative record of what has been done and why.

---

## Default Persona

**`SANDBATCH.md`** (at root) — C. Sandbatch. The default editorial voice for all generative, critical, copy, or voice-led work across all projects.

- Read it in full before any editorial task
- Each project has a `[PROJECT]_SANDBATCH.md` in its directory that extends the base persona with project-specific identity, critical positions, and content assets
- Use the project persona when working on a specific project; fall back to the base persona for workspace-level editorial work
- Do not invoke the persona for structural tasks (lint, schema, indexing, admin)

---

## Workspace Structure

```
(root)/
  CLAUDE.md             # This file
  ONTOLOGY.md           # Entity taxonomy and relationship map
  PROCESSES.md          # Dictionary of named work processes
  README.md             # Workspace overview + projects table
  SANDBATCH.md          # Base editorial persona (gitignored)
  projects/
    [slug]/             # One directory per client project
      CLAUDE.md         # Project-specific instructions
      [SLUG]_SANDBATCH.md  # Project persona extending base
      PHASE-PLAN.md     # Phase and task tracking
      MEMORY.md         # Chronological change log (gitignored)
      README.md         # Client-facing showcase
      audit/            # Audit artifacts, designs, screenshots
  tools/                # Shared MCP server implementations (gitignored)
  .venv/                # Shared Python environment (gitignored)
  .claude/
    commands/           # Slash command definitions
    settings.json       # Hooks and permissions
  .mcp.json             # MCP server configuration (gitignored)
  .env                  # API keys and secrets (gitignored)
```

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

## Slash Commands (`.claude/commands/`)

| Command | Scope | What it does |
|---------|-------|-------------|
| `/workspace-sync` | workspace | Sync CLAUDE.md, ONTOLOGY, PROCESSES against actual workspace state |
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
2. Write `projects/[client-slug]/CLAUDE.md` — client info, live URL, stack, design system, persona reference
3. Write `projects/[client-slug]/[SLUG]_SANDBATCH.md` — extend base SANDBATCH.md with project-specific identity, brand claim, geographic coordinates, content assets, and critique positions
4. Write `projects/[client-slug]/PHASE-PLAN.md` — four-phase skeleton
5. Create `projects/[client-slug]/MEMORY.md` — empty log, ready for first entry
6. Create audit scaffold: `audit/designs/`, `audit/screens/`, `audit/scripts/`
7. Add project row to root `README.md` projects table
8. Update `.gitignore` for project-specific gitignored paths (MEMORY.md, dump.md, audit/content/)
9. Run `/workspace-sync` to update CLAUDE.md skills table and ONTOLOGY if needed
