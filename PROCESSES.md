# Workspace Process Dictionary

Workspace-level processes only. Project-specific processes live in `projects/[slug]/PROCESSES.md`.

**Process index:**
- [Session Lifecycle](#process-session-lifecycle)
- [Orchestration](#process-orchestration)
- [Change Logging](#process-change-logging)
- [Workspace Maintenance](#process-workspace-maintenance)
- [Project Onboarding](#process-project-onboarding)
- [Phase Transition](#process-phase-transition)

---

## Process: Session Lifecycle

**When:** Every work session, automatically.  
**Trigger:** User sends the first message of a session.

**Start of session:**
1. Identify the active project from user context or first message
2. Read `projects/[slug]/CLAUDE.md` — project instructions and constraints
3. Read `projects/[slug]/AGENTS.md` — task routing for this project
4. Read the last 30 lines of `projects/[slug]/MEMORY.md` — recent work context
5. Confirm the current phase from `projects/[slug]/PHASE-PLAN.md`
6. State active project, current phase, and last logged action before proceeding

**Per task:**
1. Decompose using the project's `ONTOLOGY.md` (entity type) + `PROCESSES.md` (process name)
2. Route to the appropriate subagent (see Orchestration)
3. Review subagent result for correctness
4. Log to `projects/[slug]/MEMORY.md` immediately
5. Update `PHASE-PLAN.md` if phase status changed

**End of session:**
1. Write a session summary entry to `projects/[slug]/MEMORY.md`
2. If workspace docs drifted, run `/workspace-sync`
3. State the next concrete action

---

## Process: Orchestration

**When:** Any time a task is assigned.  
**Role:** Main agent only — does not execute, only routes.

**Steps:**
1. Identify the entity type from `projects/[slug]/ONTOLOGY.md`
2. Identify the named process from `projects/[slug]/PROCESSES.md`
3. Select the subagent type:

| Work category | Subagent | Notes |
|---------------|----------|-------|
| File/codebase exploration, symbol lookup | `Explore` | Read-only; fast |
| Architecture, design decisions | `Plan` | Returns a plan; review before delegating execution |
| Code, file editing, browser automation | `claude` | Worktree isolation for risky edits |
| Independent parallel research | `claude` (background) | Multiple simultaneous lookups |

4. Write a self-contained subagent prompt — include goal, file paths, entity type, process, read vs. write
5. Review result: did the subagent do what was asked?
6. Log via Change Logging

**Anti-patterns:** delegating understanding · doing execution inline · accepting unverified results

---

## Process: Change Logging

**When:** After every completed task that modifies any project artifact.  
**Role:** Orchestrator writes the log entry directly.

**Format:**
```
## [YYYY-MM-DD] — Phase [N] — [Brief title]

**Entity:** [entity type from project ONTOLOGY.md]
**Process:** [process name from project PROCESSES.md]
**Subagent:** [Explore / Plan / claude / direct]
**Changes:** [Specific files created/modified/deleted]
**Outcome:** [Result, decisions, what's unblocked, next action]
```

**Rules:**
- Log immediately — do not batch at session end
- Be specific about files changed
- One entry per discrete task
- Log failures and abandoned tasks too, with reason

**After each entry:** confirm the entity type is in `projects/[slug]/ONTOLOGY.md` and the process name is in `projects/[slug]/PROCESSES.md`. Add stubs if missing.

---

## Process: Workspace Maintenance

**When:** Start of session, or after any structural change.  
**Trigger:** `/workspace-sync` command.

**Checks:**
1. **Skills table** (in root `AGENTS.md`) vs. actual `.claude/commands/` files
2. **MCP servers table** (in root `AGENTS.md`) vs. `.mcp.json`
3. **Projects table** (in root `README.md`) vs. actual `projects/` directories
4. **Each project** has `AGENTS.md`, `ONTOLOGY.md`, `PROCESSES.md`, `MEMORY.md`, `[SLUG]_SANDBATCH.md`
5. **Root `ONTOLOGY.md`** covers only workspace entities; project-specific entities are in project docs
6. **Root `PROCESSES.md`** covers only workspace processes; project-specific processes are in project docs

Delegate reads to `Explore`, writes to `claude`.

---

## Process: Project Onboarding

**When:** A new client engagement begins.

**Steps:**
1. Create `projects/[slug]/` (copy from `projects/_template/`)
2. Write `CLAUDE.md` — client name, live URL, stack, constraints, persona reference
3. Write `AGENTS.md` — agent routing, subagent policy, session start checklist
4. Write `ONTOLOGY.md` — entity taxonomy specific to this project
5. Write `PROCESSES.md` — named workflows for this project's phase model
6. Write `PHASE-PLAN.md` — four-phase skeleton
7. Write `[SLUG]_SANDBATCH.md` — project persona extending `../../SANDBATCH.md`
8. Create `MEMORY.md` — empty log with standard header
9. Create audit scaffold: `audit/designs/`, `audit/screens/`, `audit/scripts/`
10. Add project row to root `README.md`
11. Update root `.gitignore` — add `projects/[slug]/` as an ignored directory (it has its own repo)
12. `git init` the project dir, create private GitHub repo, push
13. Run `/workspace-sync`

**If the project is a full codebase:** also write a repo-internal `AGENTS.md` following `projects/st-expedite-press/AGENTS.md` as the pattern.

---

## Process: Phase Transition

**When:** All tasks in a phase are marked complete and the next phase is ready to begin.

**Steps:**
1. Read `PHASE-PLAN.md` in full
2. Verify all tasks in the current phase are `✅ Done` — surface anything pending
3. Summarize the phase's outputs and key decisions
4. Identify the first 3 concrete tasks of the next phase, in order
5. Update `PHASE-PLAN.md` status rows if corrections needed
6. Log the transition to `MEMORY.md`
7. Report: what changed, what's unblocked, immediate next action
