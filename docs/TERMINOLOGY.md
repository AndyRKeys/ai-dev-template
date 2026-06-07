# Terminology

Canonical names for this project. Use these consistently in code, docs, commits, and conversation with AI assistants.

> **Template notice:** Replace all placeholder values. Consistency here prevents confusion across sessions.

---

## Environments

| Name | Description | URL / Location |
|---|---|---|
| `local` | Developer's own machine | `localhost` |
| `dev` / `staging` | <!-- TODO --> | <!-- TODO --> |
| `prod` / `production` | <!-- TODO --> | <!-- TODO --> |

---

## Branches

| Branch | Purpose |
|---|---|
| `main` | Production-ready code. Never commit directly here. |
| `dev` | Integration branch. All feature/fix branches merge here first. |
| `feature/issue-N-*` | New features |
| `fix/issue-N-*` | Bug fixes |
| `ops/issue-N-*` | Infrastructure, Docker, CI, deploy changes |
| `hotfix/issue-N-*` | Emergency fixes branched from `main` |

---

## Services / Components

<!-- TODO: List the named services in your project -->

| Name | What it is |
|---|---|
| <!-- e.g. `backend` --> | <!-- e.g. Node.js/Express API server --> |
| <!-- e.g. `db` --> | <!-- e.g. PostgreSQL database --> |

---

## Host / Infrastructure

<!-- TODO: Describe the host machine(s) -->

| Name | Description |
|---|---|
| <!-- e.g. `dev-server` --> | <!-- e.g. Ubuntu VM running dev environment --> |
| <!-- e.g. `prod-server` --> | <!-- e.g. Production host --> |

---

## Avoid These Ambiguous Terms

<!-- TODO: Add any terms that are easily confused in your project -->

| Avoid | Use instead | Reason |
|---|---|---|
| "the server" | `dev-server` or `prod-server` | Ambiguous |
| "the database" | `portfolio_dev` / `portfolio_prod` (or your DB name) | Be specific |
