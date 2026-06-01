# [CLIENT NAME] — Agent Doctrine

Self-contained agent system for the [slug] project. Read this file at session start before any project work.

---

## Session Start Checklist

1. Read this file
2. Read `CLAUDE.md` — client data, constraints, current status
3. Read last 30 lines of `MEMORY.md` — recent changes and open items
4. Confirm current phase from `PHASE-PLAN.md`
5. State: active project, current phase, last logged action

---

## Project Context

**Client:** [Client name · location]  
**Phase N:** [Status] · **Phase N+1:** [Status]  
**Gate:** [What's blocking the next phase]

**Entity types:** see `ONTOLOGY.md`  
**Named processes:** see `PROCESSES.md`

---

## Subagent Routing

| Work type | Subagent |
|-----------|----------|
| Find files, locate symbols | `Explore` |
| Architecture decisions, trade-offs | `Plan` |
| Write/edit, browser automation, multi-step | `claude` |
| Independent parallel lookups | `claude` (background) |

Pass enough context for the subagent to operate without conversation history. Specify read-only vs. write.

---

## Key Files

| File | Purpose |
|------|---------|
| `CLAUDE.md` | Client info, constraints, design system |
| `PHASE-PLAN.md` | Phase and task tracking |
| `ONTOLOGY.md` | Entity taxonomy for this project |
| `PROCESSES.md` | Named workflows for this project |
| `brand/` | Palette, typography, voice, logo spec |
| `audit/designs/` | HTML design variants |
| `assets/` | Logos, source images |

---

## Local Preview Server

```bash
# From workspace root
.venv/Scripts/python.exe -m http.server 876X --directory projects/[slug]/audit/designs
```

---

## Editorial Rules

- Read `../../SANDBATCH.md` + `[SLUG]_SANDBATCH.md` before any editorial, copy, or critique task
- Log every change to `MEMORY.md` immediately after completion
