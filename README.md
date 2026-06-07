# ai-dev-template

A reusable scaffold for AI-led development. Clone or use as a GitHub template to bootstrap any new
project with a consistent, battle-tested AI workflow.

---

## What's included

| File / Folder | Purpose |
| --- | --- |
| `CLAUDE.md` | Claude Code entry point — read at session start. Edit this first for every new project. |
| `AGENTS.md` | Canonical AI working rules for all assistants (Claude, Codex, Copilot Workspace, Gemini). |
| `CONTRIBUTING.md` | Contributor workflow for humans and AI assistants. |
| `SECURITY.md` | Vulnerability reporting policy. |
| `.env.example` | Safe example config shape with placeholder values only. |
| `docs/DECISIONS.md` | Architecture Decision Records — why key choices were made. |
| `docs/STYLE_GUIDE.md` | Naming conventions, code patterns, button/component variants. |
| `docs/CHANGELOG.md` | Keep-a-Changelog format. AI keeps this updated every PR. |
| `docs/TERMINOLOGY.md` | Canonical names for hosts, environments, services, branches. |
| `.github/pull_request_template.md` | Structured PR template — AI fills this in for every PR. |
| `.github/ISSUE_TEMPLATE/bug_report.md` | Bug report template. |
| `.github/ISSUE_TEMPLATE/feature_request.md` | Feature request template. |
| `.github/workflows/ci.yml` | Baseline CI checks for formatting, markdown, and template hygiene. |
| `.github/workflows/secret-scan.yml` | Secret scanning for pushes and pull requests. |
| `.claude/settings.json` | Claude Code permissions — blocks direct reads of common secret-bearing files. |
| `.claude/redact-sensitive-hook.py` | PreToolUse hook — intercepts reads of secret-bearing files and returns a redacted version. |
| `.markdownlint.json` | Markdown linting config. |
| `.prettierrc` + `.prettierignore` | Code formatting config. |
| `.gitignore` | Sensible defaults for Python + Node + common AI/dev tools. |

---

## How to use

### Option A — Use as a GitHub Template

1. Click **Use this template** at the top of this repo
2. Name your new repo and create it
3. Follow the checklist below

### Option B — Manual apply to an existing repo

```bash
# From your existing repo root:
git remote add template https://github.com/AndyRKeys/ai-dev-template.git
git fetch template
git checkout template/main -- CLAUDE.md AGENTS.md CONTRIBUTING.md SECURITY.md \
  .env.example docs/ .github/ .claude/ .markdownlint.json .prettierrc .prettierignore
git remote remove template
```

---

## First-time setup checklist

After cloning or applying this template, work through these in order:

- [ ] **Edit `CLAUDE.md`** — fill in Quick Orientation, tech stack, key files, common commands
- [ ] **Edit `AGENTS.md`** — remove sections that do not apply; add any project-specific rules
- [ ] **Edit `docs/TERMINOLOGY.md`** — define your canonical names (host, envs, branches, services)
- [ ] **Edit `docs/STYLE_GUIDE.md`** — add your naming conventions and code patterns
- [ ] **Add first entry to `docs/DECISIONS.md`** — record the key architectural choices made at project
  start
- [ ] **Add or adapt `.env.example`** — keep placeholders only, never real values
- [ ] **Update `.claude/settings.json`** — add deny rules for any project-specific secret-bearing files
  or directories
- [ ] **Review `.claude/redact-sensitive-hook.py`** — extend patterns for any project-specific secret
  names or config files
- [ ] **Update `.gitignore`** — extend for your language/framework if needed
- [ ] **Configure branch protection** in GitHub → Settings → Branches: protect `main` (require PR +
  review) and `dev` (require PR). AI never pushes directly to either.
- [ ] **Enable GitHub secret scanning** if available on your plan/org
- [ ] **Delete placeholder comments** from all stubs once filled in
- [ ] **Mark this repo as a template** (Settings → check "Template repository") if you want GitHub to
  list it

---

## Branching convention (default)

```text
main          ← production / stable
dev           ← integration branch
feature/issue-N-short-desc   ← AI working branches
fix/issue-N-short-desc
ops/issue-N-short-desc
```

AI always branches from `dev`, never directly from `main`.

---

## Commit message format

```text
type: short imperative summary (≤50 chars)

Optional longer explanation of why, not what.

Co-Authored-By: <AI Model Name> <noreply@example.com>
```

Update the `Co-Authored-By` line to match whichever model is in use on the project.

Types: `feat` `fix` `refactor` `docs` `test` `ops` `chore`
