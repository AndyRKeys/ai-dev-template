## Summary

<!-- One or two sentences describing what this PR does and why -->

Closes #<!-- issue number -->

## Changes

<!-- Bullet list of files/areas changed and what changed -->

- <!-- describe change 1 -->
- <!-- describe change 2 -->

## Test Plan

<!-- Specific steps to verify this works. Be precise — exact commands, actions, expected results. -->

### Happy path

1. <!-- step 1 -->
2. <!-- step 2 -->
3. <!-- step 3 -->

### Edge cases

- [ ] <!-- e.g. Empty state / no data -->
- [ ] <!-- e.g. Error handling (bad input, network failure) -->
- [ ] <!-- e.g. Mobile / small screen -->

### Regression checks

<!-- Features that could have been affected and should be verified still work -->

- [ ] <!-- feature 1 still works -->
- [ ] <!-- feature 2 still works -->

### Setup required before testing

<!-- Any seed data, env vars, or manual steps needed -->

- None

## Smoke Test

<!-- Tick what applies -->

- [ ] Manual smoke test run against dev environment
- [ ] Automated test suite run and passing
- [ ] N/A — no testable behaviour changes in this PR

## Documentation

<!-- Tick all that apply. If a box is not relevant, mark N/A. -->

- [ ] `docs/CHANGELOG.md` updated with an entry under `[Unreleased]`
- [ ] `AGENTS.md` / `docs/STYLE_GUIDE.md` updated if working rules or patterns changed
- [ ] `README.md` updated if commands, setup steps, or directory structure changed
- [ ] N/A — behaviour and operator docs already match the change (no updates needed)

## Risk / Impact

<!-- For security/infra/ops changes, briefly note risk, impact, or threat mitigated. -->

- <!-- describe risk or impact, or state: Low — no application behaviour changes -->

## Squash Commit Message

<!-- Mandatory — repo squash-merges, so this becomes the permanent history entry.
     Format: short imperative summary (≤50 chars), blank line, short why/what body
     (focus on WHY, not what — the diff shows what), then Co-Authored-By footer. -->

```text
<summary>

<body>

Co-Authored-By: <AI Model Name> <noreply@example.com>
```

## Notes for Reviewer

<!-- Anything unusual, a known limitation, or a decision that warrants explanation. -->

<!-- ⚠️ Full file rewrite — please check diff carefully for unintended changes -->
<!-- (uncomment the line above if any file was fully rewritten) -->
