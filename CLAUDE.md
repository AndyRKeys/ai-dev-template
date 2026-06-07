# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

> **Template notice:** Lines marked `<!-- TODO -->` need filling in for this specific project. Delete the markers once done.

---

## Quick Orientation (2 minutes)

**What is this?** <!-- TODO: One sentence describing the project -->

**Tech stack:**

- <!-- TODO: Frontend framework / language -->
- <!-- TODO: Backend framework / language -->
- <!-- TODO: Database -->
- <!-- TODO: Infrastructure / hosting -->
- AI pair programmer: <!-- TODO: Model + provider used on this project -->

**Key files:**

- <!-- TODO: Entry point -->
- <!-- TODO: Routes / controllers -->
- <!-- TODO: Data / schema -->
- `AGENTS.md` — canonical working instructions for all AI assistants (scope, commits, documentation, code style)

---

## Before You Start

1. **Read the onboarding docs in this order:**
   - `README.md` — architecture, local setup, branching, deployment
   - `AGENTS.md` — working instructions, scope discipline, commit conventions
   - `docs/STYLE_GUIDE.md` — naming, code patterns
   - `docs/TERMINOLOGY.md` — canonical names (host, environments, services, branches)
   - `docs/DECISIONS.md` — architecture decisions and the reasoning behind them

2. **Project orientation:**
   - Branching: `main` (prod) ← `dev` (integration) ← `feature/issue-N-*` (your work)
   - Always branch from `dev`. Never commit directly to `main`.
   - One branch at a time for ops/infra or security work — finish, PR, merge before starting the next.

3. **Current state:** <!-- TODO: Brief note on what's working, what's in progress -->

---

## Common Commands

<!-- TODO: Fill in for your stack -->

### Local Development

```bash
# Start dev environment
# TODO

# Run tests
# TODO

# Stop / clean up
# TODO
```

### Git Workflow

```bash
# Start new work
git checkout dev
git pull origin dev
git checkout -b fix/issue-N-short-description

# Commit
git add <files>
git commit -m "fix: correct the thing

Why this change was needed and what it does.

Co-Authored-By: <AI Model Name> <noreply@example.com>"

# Push and open PR (default — do this automatically once work is complete)
git push -u origin fix/issue-N-short-description
# Then open PR to dev
```

**PR creation is the default.** Once the branch is pushed and the work is complete, open the PR to `dev` automatically — do not ask first. You still never merge it (owner reviews + merges). Skip only if work is explicitly incomplete/experimental.

**Every PR must fully fill in the template at `.github/pull_request_template.md`.**

**Issue labelling (AI-managed):**

- When starting work on an issue: apply `in progress`
- When opening a PR to `dev`: switch to `awaiting review`
- After merge to `dev` but before release: switch to `awaiting release`
- After deployed to production: switch to `released`

**Type labels (add all that apply):** `bug` · `feature` · `security` · `ops` · `documentation` · `workflow` · `high priority` · `regression` · `UI`

---

## Architecture & Key Concepts

<!-- TODO: Describe the architecture here. Include:
  - How requests flow through the system
  - Key directories and what lives in each
  - Any non-obvious design decisions
  - Auth model if applicable
-->

---

## Common Patterns & Conventions

<!-- TODO: Add project-specific patterns. Generic defaults below — keep what applies, replace the rest. -->

### Naming

- Camel case for variables and functions
- Kebab case for file names and CSS classes
- Underscore case for database columns

### Code style

- Prefer explicit over clever
- Extract repeated logic — don't duplicate validation, error handling, or config
- Parameterised queries always — never string concatenation for SQL

### Section headers (JS/Python comments)

```js
// ── Section name
```

### Commit messages

- Imperative present tense: "fix", "add", "refactor" — not "fixed", "added"
- Short summary (≤50 chars), blank line, optional explanation
- Always include `Co-Authored-By` footer matching the model in use (see `AGENTS.md`)

---

## Debugging & Logging

**Build observability into every change — it is part of the implementation, not a follow-up.**

- Add structured log lines at meaningful decision points (entry, external-call outcomes, branch taken, failure reasons)
- Log the *why* of a failure (error + relevant inputs + expectation), never secrets
- A change isn't done until you can answer: "if this breaks in prod, how would we diagnose it from logs alone?"
- Fail loud, not silent — surface warnings as hard failures, not silent skips

---

## Testing

<!-- TODO: Describe test strategy, how to run tests, what's covered -->

**PR test plan rules (every PR that touches application code):**

- Every step must include the exact copy-paste command
- Add a comment above every command explaining what it verifies
- State the expected output so the reviewer knows pass vs fail
- Where a step requires waiting (e.g. token expiry), provide a way to simulate it

---

## Documentation

**Docs must move in lockstep with code.**

**When to update docs (same PR):**

- Scripts are added, removed, or renamed
- Deploy / testing / operational workflows change
- Routes, APIs, or env vars are added or changed
- Any behaviour change that affects how someone develops, deploys, tests, or debugs

**What to update:**

- `README.md` — top-level workflow, commands, directory trees
- `AGENTS.md` — working rules for AI helpers
- `docs/CHANGELOG.md` — every PR gets a `[Unreleased]` entry
- `docs/DECISIONS.md` — add an ADR when a significant architectural choice is made
- Ops docs as applicable

**Treat the documentation checklist in the PR template as mandatory.** If no docs change is needed, explicitly state why.

---

## High-Risk Areas

Review these areas with extra care and slower-than-normal edits:

- Authentication, session, token, and permission logic
- Secret-bearing config, credential handling, and deployment settings
- Database schema and migration scripts
- File deletion, overwrite, move, sync, or bulk update logic
- Payment, billing, and externally visible automation

<!-- TODO: Add project-specific high-risk files and directories here -->

---

## Sensitive File Handling

- Never read secret-bearing files directly into AI context
- Use the project redaction mechanism when inspecting sensitive config
- Prefer example files or sanitised samples when reasoning about config shape
- Treat `.env*`, key material, deploy credentials, and local override files as sensitive by default

---

## Done Criteria

A task is only done when all of the following are true:

- Code changes are complete and scoped to the current issue
- Tests relevant to the change are run or explicitly documented as not applicable
- Logs / observability are good enough to diagnose failures
- Documentation is updated or the PR explains why no doc change is needed
- A PR to `dev` is opened with the template fully completed
