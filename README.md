# ai-dev-template

A reusable scaffold for AI-led development. Clone or use as a GitHub template to bootstrap any new project with a consistent, battle-tested AI workflow.

---

## What's included

| File / Folder | Purpose |
|---|---|
| `CLAUDE.md` | Master AI context file — read by Claude Code at session start. Edit this first for every new project. |
| `docs/AI.md` | AI working rules: scope discipline, commit hygiene, PR expectations |
| `docs/STYLE_GUIDE.md` | Naming conventions, code patterns, button/component variants |
| `docs/CHANGELOG.md` | Keep-a-Changelog format. AI keeps this updated every PR. |
| `docs/TERMINOLOGY.md` | Canonical names for hosts, environments, services, branches |
| `.github/pull_request_template.md` | Structured PR template — AI fills this in for every PR |
| `.github/ISSUE_TEMPLATE/bug_report.md` | Bug report template |
| `.github/ISSUE_TEMPLATE/feature_request.md` | Feature request template |
| `.claude/settings.json` | Claude Code permissions — blocks direct `.env` reads |
| `.claude/redact-env-hook.py` | PreToolUse hook — intercepts `.env` reads and returns redacted version |
| `.markdownlint.json` | Markdown linting config |
| `.prettierrc` + `.prettierignore` | Code formatting config |
| `.gitignore` | Sensible defaults for Python + Node + common tools |

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
git checkout template/main -- CLAUDE.md docs/ .github/ .claude/ .markdownlint.json .prettierrc .prettierignore
git remote remove template
```

---

## First-time setup checklist

After cloning or applying this template, work through these in order:

- [ ] **Edit `CLAUDE.md`** — fill in Quick Orientation, tech stack, key files, common commands
- [ ] **Edit `docs/TERMINOLOGY.md`** — define your canonical names (host, envs, branches, services)
- [ ] **Edit `docs/AI.md`** — adjust scope rules and any project-specific working constraints
- [ ] **Edit `docs/STYLE_GUIDE.md`** — add your naming conventions and code patterns
- [ ] **Update `.claude/settings.json`** — add any path-specific `deny` rules for your `.env` locations
- [ ] **Update `.gitignore`** — extend for your language/framework if needed
- [ ] **Delete placeholder comments** from all `docs/` stubs once filled in
- [ ] **Mark this repo as a template** (Settings → check "Template repository") if you want GitHub to list it

---

## Branching convention (default)

```
main          ← production / stable
dev           ← integration branch
feature/issue-N-short-desc   ← AI working branches
fix/issue-N-short-desc
ops/issue-N-short-desc
```

AI always branches from `dev`, never directly from `main`.

---

## Commit message format

```
type: short imperative summary (≤50 chars)

Optional longer explanation of why, not what.

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>
```

Types: `feat` `fix` `refactor` `docs` `test` `ops` `chore`

---

## Derived from

[AndyRKeys/MyPortfolioSite](https://github.com/AndyRKeys/MyPortfolioSite) — a mature AI-assisted personal project that developed this workflow over time.
