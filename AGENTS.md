# AGENTS.md — AI Working Instructions

This file is the **canonical working rules document** for all AI assistants operating in this repository — including Claude Code, OpenAI Codex, GitHub Copilot Workspace, Gemini Code Assist, and any equivalent tool.

`CLAUDE.md` (Claude Code entry point) and any other tool-specific entry files all defer to this document for detail.

> **Model version note:** The `Co-Authored-By` footer in commits should reflect the model actually used. Update it when switching models (for example `Claude Sonnet 4.6`, `GPT-5`, `gemini-2.5-pro`).

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
  ```text
  Co-Authored-By: <AI Model Name> <noreply@example.com>
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

## Secrets & Sensitive Data

These rules apply to **any information that could cause harm if exposed** — not just `.env` files. This includes API keys, tokens, passwords, credentials, PII, private keys, connection strings, and any file or data store that holds them.

**Never read or expose sensitive data directly:**
- Do not read secret-bearing files directly into AI context
- Do not log, print, or include sensitive values in commit messages, PR bodies, comments, or documentation
- Do not pass raw secret values as function arguments in examples or test fixtures

**Examples of files that may contain secrets:**
- `.env*`
- `*.key`, `*.pem`, `*.p12`, `*.pfx`
- cloud credentials in `.aws/`, `.config/gcloud/`, `.azure/`
- Docker, Terraform, CI, or deploy config containing embedded credentials
- local override files such as `secrets.yml`, `appsettings.*.json`, `terraform.tfvars`, `.npmrc`, `.pypirc`

**Always use a redaction mechanism:**
- Every project that handles sensitive data must have a redaction layer — a hook, script, or pre-processing step that masks values before they reach AI context
- The mechanism should: intercept reads of secret-bearing files, replace sensitive values with `[redacted]`, and pass only the sanitised version forward
- Use regex patterns matching common secret key names (for example `SECRET`, `TOKEN`, `PASS`, `KEY`, `CREDENTIAL`, `PRIVATE`, `CERT`) as a baseline — extend for project-specific patterns
- Document the redaction mechanism in `CLAUDE.md` so AI tools know how to use it

**Safe patterns to follow:**
- Keep an `.env.example` or equivalent example config with placeholder values only — safe to read and commit
- Use variable names and config keys in code and docs; never inline actual values
- When an AI assistant needs to understand the shape of a config, point it to the example file or sanitised sample
- When a secret must be referenced in a PR, describe it by key name only

**If you discover a secret has been exposed:**
- Treat it as compromised immediately — rotate it before doing anything else
- Do not attempt to rewrite git history to remove it without also rotating; history rewrites alone are not sufficient
- Flag the exposure as a high-priority issue

---

## Debugging & Logging

- Build observability into every change — logging is part of the implementation
- Add structured log lines at: entry points, external-call outcomes, key branch decisions, failure paths
- Log the *why* of a failure: error message + relevant inputs + what was expected
- Never log secrets, tokens, JWTs, hashes, or any sensitive value
- A change isn't done until: "if this breaks in prod, how would we diagnose it from logs alone?" has an answer
- Fail loud, not silent — surface warnings as hard failures where appropriate

---

## PR Test Plans Must Include

- The **exact copy-paste command** for every step — no assumed knowledge
- A `# comment` above every command explaining what it verifies and why it matters for this PR
- The **expected output** after each command — reviewer knows pass vs fail at a glance
- Steps for both happy path and key edge cases
- Where a step requires waiting (for example token expiry), a DB or config command to simulate it instead

---

## Security Discipline

- Security and auth changes: one branch at a time, high test coverage, read the full auth file before editing
- Parameterised queries always — never string concatenation for SQL or shell commands
- Validate and sanitise all external input before use
- Principle of least privilege — request only the permissions a component actually needs

---

## Execution Safety (file system, shell, and destructive operations)

For any project where AI suggestions can result in file system changes, shell execution, or destructive operations:

- **Never suggest or generate commands that delete, overwrite, or move files without a dry-run flag** — always offer `--dry-run` or `-WhatIf` (PowerShell) as the default first step
- **Destructive actions require explicit human approval** — do not chain a dry-run directly into live execution
- **Quarantine before delete** — prefer moving items to a dated quarantine folder over permanent deletion
- **Scope writes to one root at a time** — never operate across multiple root directories in a single command
- **Log every proposed action to a file** before execution so there is a reviewable audit trail

---

## Merge Conflict Handling

- Prefer `git rebase` onto the latest target branch rather than merging the target branch into the feature branch
- If conflicts touch auth, secrets, migrations, infrastructure, or generated lockfiles, stop and request human review
- Never force-push to protected branches
- If a conflict resolution could change behaviour in a non-obvious way, document it in the PR notes and test plan

---

## What AI Should Not Do

- Merge PRs
- Push directly to `main` or `dev`
- Delete branches without instruction
- Modify secret files or credential stores
- Make broad refactors outside the current issue scope
- Skip the PR template
- Leave documentation out of date
- Execute destructive file operations without a preceding dry-run and explicit approval
- Read or relay sensitive data without passing it through the project’s redaction mechanism first
