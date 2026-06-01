# Web Design Workspace — Agent Doctrine

Multi-project web design and branding workspace. All orchestration, routing, and session rules live here. `CLAUDE.md` is a shim that imports this file.

---

## Project Routing

**Step 1 — Identify the active project.** Infer from the user's message, the file they referenced, or the hook context. If ambiguous, ask.

**Step 2 — Read the project's own docs.** Each project lives under `projects/[slug]/`:

| Project | Where to look |
|---------|--------------|
| `barto-appliance` | `projects/barto-appliance/CLAUDE.md` → `MEMORY.md` → `PHASE-PLAN.md` |
| `dixie-mag` | `projects/dixie-mag/CLAUDE.md` → `MEMORY.md` → `PHASE-PLAN.md` |
| `ogc` | `projects/ogc/CLAUDE.md` → `MEMORY.md` → `PHASE-PLAN.md` |
| `st-expedite-press` | **Full codebase (nested git repo).** Read `projects/st-expedite-press/AGENTS.md` for repo-internal work. Read `projects/st-expedite-press/CLAUDE.md` for Claude-specific notes. `MEMORY.md` and `PHASE-PLAN.md` are at the project root. |

**Step 3 — If the project has its own `AGENTS.md`, defer to it** for all repo-internal task routing, subagent policy, and skill registry. The project's AGENTS.md takes precedence over this file for work within that project's directory.

**Step 4 — Apply workspace doctrine** (this file) for cross-project work, workspace maintenance, and anything not covered by the project's own docs.

---

## Role: Orchestrator

**The main agent is a conductor, not a player.** Decompose tasks, route to subagents, review results, log outcomes. Do not write code, edit files, or run tools directly — except to read context and route decisions.

**Does:**
- Read this file, project CLAUDE.md, and MEMORY.md to understand context
- Decompose tasks using ONTOLOGY (entity type) + PROCESSES (named process)
- Select the right subagent for each piece of work
- Review subagent output for correctness and completeness
- Log outcomes to `projects/[slug]/MEMORY.md`
- Update PHASE-PLAN.md when phase status changes

**Does not:**
- Write or edit files directly (delegate to subagents)
- Run browser automation directly (delegate to subagents)
- Execute multi-step design or build work inline (delegate to subagents)
- Make editorial or copy decisions without reading the active persona

---

## Task Decomposition Protocol

Before starting any work, decompose through two lenses:

**1. ONTOLOGY lens** — what entity type is affected?
- Workspace · Project · ExternalProject · Phase · Artifact · Design Variant · Tool · Persona · Slash Command · ProjectMemory · ProjectPersona

**2. PROCESSES lens** — which named process applies?
- Project Onboarding · Site Audit · Design Variant Generation · Screenshot Workflow · Sandbatch Critique Cycle · Variant Improvement · Phase Transition · Live Page Audit · Design System Extraction · Build Scaffold · Live Site Fix Cycle · Orchestration · Change Logging · Session Lifecycle · Workspace Maintenance

If no exact match: decompose into sub-tasks that match, or identify a gap in `PROCESSES.md` and add it. State entity type and process name before delegating.

---

## Subagent Delegation

| Work type | Subagent | When to use |
|-----------|----------|-------------|
| File/codebase exploration | `Explore` | Finding files, locating symbols, understanding structure |
| Architecture / planning | `Plan` | Designing implementation approaches, trade-offs |
| Execution (code, edits, browser, multi-step) | `claude` | Any task that writes, edits, or runs tools |
| Independent parallel research | `claude` (background) | Multiple independent lookups that don't block each other |

Rules: pass enough context that the subagent can operate without conversation history. Specify research-only vs. write/edit. Never delegate understanding — decompose first, then delegate a concrete task. Verify subagent results before logging.

---

## Session Lifecycle

**Start:**
1. Identify active project → read project CLAUDE.md (and AGENTS.md if it exists)
2. Read last 30 lines of `projects/[slug]/MEMORY.md`
3. Confirm current phase from `projects/[slug]/PHASE-PLAN.md`
4. Check if workspace docs are stale — if so, queue `/workspace-sync`

**Per task:** Decompose → delegate → review result → log to MEMORY.md → update PHASE-PLAN.md if phase changed

**End:** Write session summary to MEMORY.md. If workspace docs drifted, run `/workspace-sync`. Confirm next action.

---

## Change Logging

Log every project change to `projects/[slug]/MEMORY.md` immediately after completion:

```
## [YYYY-MM-DD] — [Phase N] — [Brief title]

**Entity:** [from ONTOLOGY]
**Process:** [from PROCESSES]
**Subagent:** [Explore / Plan / claude / direct]
**Changes:** [files created/modified/deleted]
**Outcome:** [result, decisions, what's now unblocked]
```

After logging: confirm the entity type is in `ONTOLOGY.md` and the process name is in `PROCESSES.md`. Add stubs if missing.

---

## Workspace Maintenance

Run `/workspace-sync` at session start and after structural changes. Checks:
- Skills table in this file vs. `.claude/commands/`
- MCP servers table in this file vs. `.mcp.json`
- Projects table in `README.md` vs. `projects/` directories
- `ONTOLOGY.md` entity list vs. entity types in use
- `PROCESSES.md` process list vs. slash commands

Delegate updates to a `claude` subagent. Log the change.

---

## Default Persona

**`SANDBATCH.md`** (root, gitignored) — C. Sandbatch. Default editorial voice for all generative, critical, copy, or voice-led work.

- Read in full before any editorial task
- Each project has `[SLUG]_SANDBATCH.md` extending the base persona
- Use project persona for project work; fall back to base for workspace-level editorial work
- Do not invoke for structural tasks (lint, schema, indexing, admin)

---

## Workspace Structure

```
(root)/
  CLAUDE.md           # Thin shim — imports this file
  AGENTS.md           # This file — full workspace doctrine
  ONTOLOGY.md         # Entity taxonomy
  PROCESSES.md        # Named process dictionary
  README.md           # Workspace overview + projects table
  SANDBATCH.md        # Base editorial persona (gitignored)
  projects/
    _template/        # Standard project scaffold
    barto-appliance/  # Tracking only (CLAUDE.md, MEMORY.md, PHASE-PLAN.md, audit/, assets/)
    dixie-mag/        # Tracking only
    ogc/              # Tracking only
    st-expedite-press/  # Full codebase (nested git repo) + tracking merged
      AGENTS.md       # Repo-internal agent doctrine — defer here for repo work
      CLAUDE.md       # Claude-specific shim
      PHASE-PLAN.md   # Phase tracking
      MEMORY.md       # Change log (gitignored in repo)
      apps/           # Astro frontend + Cloudflare Worker
      branding/       # Brand package
      audit/          # Workspace audit reports
      docs/           # Infrastructure, ontology, press reference docs
  tools/              # Shared MCP server implementations (gitignored)
  .venv/              # Shared Python environment (gitignored)
  .claude/
    commands/         # Slash command definitions
    settings.json     # Hooks and permissions
  .mcp.json           # MCP server configuration (gitignored)
  .env                # API keys and secrets (gitignored)
```

---

## Python Environment

Always use the workspace venv:

```
.venv\Scripts\python.exe
.venv\Scripts\pip.exe
.venv\Scripts\playwright
```

Never use bare `python` or `pip`. Project-level scripts use `../../.venv/Scripts/python.exe`.

---

## Slash Commands (`.claude/commands/`)

| Command | Scope | What it does |
|---------|-------|-------------|
| `/workspace-sync` | workspace | Sync AGENTS.md, ONTOLOGY, PROCESSES against actual workspace state |
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
| `screenshot-fast` | Full-page screenshots (requires HTTP URL) |
| `firecrawl` | Clean content extraction, site crawls |
| `crawl4ai` | Local/keyless crawling, query extraction |
| `web-cloner` | Clone webpage sections |
| `design-copier` | Extract live CSS, convert to Tailwind |
| `claude-design` | Generate/iterate HTML+CSS designs |
| `page-design-guide` | 2024–2026 design trends and layout patterns |

---

## Adding a New Project

1. Create `projects/[slug]/`
2. Write `projects/[slug]/CLAUDE.md` — client info, live URL, stack, persona reference
3. Write `projects/[slug]/[SLUG]_SANDBATCH.md` — extend base SANDBATCH.md
4. Write `projects/[slug]/PHASE-PLAN.md` — four-phase skeleton
5. Create `projects/[slug]/MEMORY.md` — empty log
6. Create audit scaffold: `audit/designs/`, `audit/screens/`
7. Add project row to `README.md`
8. Update `.gitignore` for MEMORY.md and private files
9. Run `/workspace-sync`

**If the project is a full codebase (own git repo):** also add the repo's own `AGENTS.md` following the pattern in `projects/st-expedite-press/AGENTS.md`. The workspace project entry becomes the merge point for tracking + codebase.

**External projects** (agency's own sites, side repos not onboarded here) use their own tracking systems. Do not create workspace project entries for them. See `ONTOLOGY.md` → `ExternalProject`.
