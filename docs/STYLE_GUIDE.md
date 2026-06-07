# Style Guide

Naming conventions, code patterns, and component variants for this project.

> **Template notice:** Replace the placeholder sections below with project-specific conventions.

---

## Naming Conventions

<!-- TODO: Define your naming conventions -->

| Context | Convention | Example |
|---|---|---|
| JS/Python variables & functions | camelCase | `getUserData`, `parsedResult` |
| File names | kebab-case | `user-service.js`, `data-utils.py` |
| CSS classes / HTML IDs | kebab-case | `btn-primary`, `nav-header` |
| Database columns | snake_case | `user_id`, `created_at` |
| Constants | UPPER_SNAKE | `MAX_RETRIES`, `API_BASE_URL` |

---

## Code Patterns

<!-- TODO: Add project-specific patterns and anti-patterns -->

### Do

- Extract repeated logic into shared utilities — don't duplicate
- Use parameterised queries — never string-interpolated SQL
- Prefer explicit error messages with context over generic ones

### Don't

- String-concatenate SQL queries
- Swallow errors silently (always log + re-throw or return error state)
- Add logic to entry-point / orchestrator files — keep them thin

---

## Section Headers (inline code comments)

```js
// ── Section name
```

```python
# ── Section name
```

---

## Component / UI Variants

<!-- TODO: Define your UI component variants if applicable -->

| Variant | Class / Usage | Notes |
|---|---|---|
| Primary button | `.btn-primary` | Main CTA |
| Secondary button | `.btn-secondary` | Outlined |
| Danger action | `.btn-danger` | Destructive actions |

---

## File Structure

<!-- TODO: Describe the directory structure and what belongs where -->

```text
project-root/
├── src/           # Application source
├── tests/         # Test files mirroring src/ structure
├── docs/          # Project documentation
├── scripts/       # Dev, deploy, and utility scripts
└── .github/       # PR and issue templates
```
