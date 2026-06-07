# AGENTS.md — AI Working Instructions

This file is the **canonical working rules document** for all AI assistants operating in this repository — including Claude Code, OpenAI Codex, GitHub Copilot Workspace, Gemini Code Assist, and any equivalent tool.

`CLAUDE.md` (Claude Code entry point) and any other tool-specific entry files all defer to this document for detail.

> **Model version note:** The `Co-Authored-By` footer in commits should reflect the model actually used. Update it when switching models (e.g. `Claude Sonnet 4.6`, `gpt-4o`, `gemini-2.5-pro`).

---

## Scope Discipline

- Work on one issue at a time. Do not expand scope without explicit instruction.
- If you notice a related problem while working, **log it as a new issue** — don't fix it in the current branch.
- Prefer small, focused PRs over large ones. A PR that does one thing is easier to review and safer to merge.
- Never refactor code that isn't related to the current task — raise it as a separate issue.

---

## Commit Hygiene

- Imperative present tense: "fix", "add", "refactor" — not "fixed", "added", "refactored"
- Short summary (≤50 chars), blank line, optional body explaining *why* (not what — the diff shows what)
- Always include the `Co-Authored-By` footer, updated to match the model in use:
  ```
  Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>
  ```
- Commit logical units of work — don't bundle unrelated changes in one commit
- Atomic commits: each commit should leave the codebase in a working state

---

## PR Expectations

- PR creation is the **default** when work is complete — open it automatically, don't ask first
- Never merge a PR yourself — that is always the owner's action
- Fill in every section of `.github/pull_request_template.md` — no section left blank without a stated reason
- Include a squash commit message in the PR body — the repo squash-merges, so this becomes permanent history
- Recommend a `Closes #N` reference in the PR body
- After opening the PR, update the issue label from `in progress` → `awaiting review`

---

## Documentation Hygiene

**Docs move in lockstep with code.** Updating docs is part of the implementation, not a follow-up.

- If a script is added, renamed, or removed → update `README.md`
- If a workflow changes → update the relevant doc
- If an API, route, or env var changes → update the relevant doc
- If no doc update is needed, state explicitly why in the PR (`N/A: behaviour and operator docs already match`)
- When code and docs disagree, fix both in the same PR
- Prefer small, tied-to-behaviour doc edits over broad "docs tidy-up" PRs

**When NOT to add docs:**
- Generic "what this function does" explanations — prefer clear naming
- Obvious patterns that already match the existing style
- Implementation details that don't affect future work

---

## Debugging & Logging

- Build observability into every change — logging is part of the implementation
- Add structured log lines at: entry points, external-call outcomes, key branch decisions, failure paths
- Log the *why* of a failure: error message + relevant inputs + what was expected
- Never log secrets, tokens, JWTs, hashes, or `.env` values
- A change isn't done until: "if this breaks in prod, how would we diagnose it from logs alone?" has an answer
- Fail loud, not silent — surface warnings as hard failures where appropriate

---

## PR Test Plans Must Include

- The **exact copy-paste command** for every step — no assumed knowledge
- A `# comment` above every command explaining what it verifies and why it matters for this PR
- The **expected output** after each command — reviewer knows pass vs fail at a glance
- Steps for both happy path and key edge cases
- Where a step requires waiting (e.g. token expiry), a DB or config command to simulate it instead

---

## Security Discipline

- Never read `.env` files directly — use the redact hook or `.env.example` templates
- Never log or expose secrets, tokens, or credentials
- Security and auth changes: one branch at a time, high test coverage, read the full auth file before editing
- Parameterised queries always — never string concatenation for SQL or shell commands

---

## Execution Safety (file system, shell, and destructive operations)

For any project where AI suggestions can result in file system changes, shell execution, or destructive operations:

- **Never suggest or generate commands that delete, overwrite, or move files without a dry-run flag** — always offer `--dry-run` or `-WhatIf` (PowerShell) as the default first step
- **Destructive actions require explicit human approval** — do not chain a dry-run directly into live execution
- **Quarantine before delete** — prefer moving items to a dated quarantine folder over permanent deletion
- **Scope writes to one root at a time** — never operate across multiple root directories in a single command
- **Log every proposed action to a file** before execution so there is a reviewable audit trail

---

## What AI Should Not Do

- Merge PRs
- Push directly to `main` or `dev`
- Delete branches without instruction
- Modify `.env` files
- Make broad refactors outside the current issue scope
- Skip the PR template
- Leave documentation out of date
- Execute destructive file operations without a preceding dry-run and explicit approval
