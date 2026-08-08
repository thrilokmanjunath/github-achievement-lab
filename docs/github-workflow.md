# GitHub Workflow Guide

> A comprehensive reference for the standard GitHub collaborative development workflow.

---

## Overview

This guide documents the complete lifecycle of a code contribution — from identifying a
problem to shipping a merged, tested feature.

---

## 1. Issue Creation

Issues are the starting point for all work. They capture bugs, features, and discussions.

```bash
# Using GitHub CLI
gh issue create \
  --title "feat: add statistics command" \
  --body "Users need a way to view calculation history statistics." \
  --label "enhancement"

# Or open in browser
gh issue create --web
```

**Issue best practices:**
- Use a clear, descriptive title
- Describe the problem, not the solution
- Include reproduction steps for bugs
- Add labels to aid triage
- Assign to yourself when you begin work

---

## 2. Branch Creation

One branch per issue. Branch from a clean `main`.

```bash
# Sync main first
git checkout main
git pull origin main

# Create branch
git checkout -b feature/add-statistics-command

# Or with GitHub CLI
gh repo sync
git checkout -b feature/add-statistics-command
```

**Branch naming conventions:**

| Category | Pattern | Example |
|---|---|---|
| Feature | `feature/<slug>` | `feature/add-statistics-command` |
| Bug fix | `fix/<slug>` | `fix/division-validation` |
| Documentation | `docs/<slug>` | `docs/update-workflow-guide` |
| Tests | `test/<slug>` | `test/add-calculator-edge-cases` |

---

## 3. Commits

Use [Conventional Commits](https://www.conventionalcommits.org/) for all messages.

```bash
# Stage changes
git add src/achievement_lab/cli.py tests/test_cli.py

# Commit
git commit -m "feat(cli): add statistics subcommand"

# Commit with body
git commit -m "fix(calculator): handle NaN and Infinity inputs

Previously, passing float('nan') or float('inf') to any operation
would silently produce invalid results. Now raises ValidationError.

Closes #7"
```

**Commit types:**

| Type | Usage |
|---|---|
| `feat` | New feature |
| `fix` | Bug fix |
| `docs` | Documentation only |
| `test` | Tests only |
| `refactor` | Code restructure (no behaviour change) |
| `chore` | Maintenance, dependencies |
| `ci` | CI/CD configuration |
| `perf` | Performance improvement |

---

## 4. Co-authored Commits

When pair programming or acknowledging a collaborator's contribution:

```bash
git commit -m "feat(calculator): add modulo operation

Co-authored-by: Jane Smith <jane@example.com>
Co-authored-by: Bob Jones <bob@example.com>"
```

**Rules:**
- Only use real contributors who actually helped
- The co-author must have a real GitHub account associated with that email
- This is how the **Pair Extraordinaire** achievement is earned

---

## 5. Pushing a Branch

```bash
# First push (sets upstream tracking)
git push -u origin feature/add-statistics-command

# Subsequent pushes
git push
```

---

## 6. Pull Requests

```bash
# Create PR via CLI (uses PR template automatically)
gh pr create \
  --title "feat: add statistics subcommand" \
  --body "$(cat .github/PULL_REQUEST_TEMPLATE.md)"

# Or open the editor interactively
gh pr create --fill

# Or open in browser
gh pr create --web
```

**PR body must include:**
- Summary of changes
- Problem being solved
- How it was tested
- `Closes #<issue-number>` to auto-close the issue on merge

---

## 7. GitHub Actions CI

Every PR triggers the CI pipeline automatically.

```bash
# Check CI status
gh pr checks

# View run logs
gh run list
gh run view <run-id>
```

**All PRs must pass CI before merging.**

---

## 8. Code Review

```bash
# Request a review
gh pr edit --add-reviewer collaborator-username

# View PR comments
gh pr view --comments

# Check out a PR locally for review
gh pr checkout <pr-number>
```

**Review etiquette:**
- Be specific and constructive
- Distinguish blocking issues from suggestions
- Approve only when you are genuinely satisfied
- Respond to every comment before re-requesting review

---

## 9. Merging

```bash
# Squash merge (preferred — keeps history clean)
gh pr merge <pr-number> --squash

# Standard merge
gh pr merge <pr-number> --merge

# Rebase merge
gh pr merge <pr-number> --rebase
```

After merging:
```bash
git checkout main
git pull
git branch -d feature/add-statistics-command
```

---

## 10. Tagging Releases

```bash
# Create annotated tag
git tag -a v1.1.0 -m "Release v1.1.0: add statistics command"
git push origin v1.1.0

# Create GitHub release with notes
gh release create v1.1.0 \
  --title "v1.1.0 — Statistics Command" \
  --notes "## What's new
- Added \`achievement-lab statistics\` subcommand
- Fixed NaN/Infinity input validation
- Added 12 new unit tests"
```

---

## 11. GitHub Discussions

Discussions are for questions, ideas, and community conversations — not bug reports.

**Good discussion topics:**
- "How should small open-source projects structure Git workflows?"
- "Best practices for maintaining CI on Python projects?"
- "How to handle breaking changes gracefully?"

The **Galaxy Brain** achievement is earned when your answer in a discussion
is accepted as the official answer by the original poster.

---

## 12. Keeping Your Fork in Sync

```bash
# Add upstream remote
git remote add upstream https://github.com/thrilokm/github-achievement-lab.git

# Fetch and merge upstream changes
git fetch upstream
git checkout main
git merge upstream/main
git push origin main
```

---

## Quick Reference

```bash
gh issue create          # Open a new issue
gh issue list            # List open issues
gh pr create --fill      # Open a PR
gh pr list               # List open PRs
gh pr merge --squash     # Squash merge a PR
gh pr checks             # CI status for a PR
gh run list              # Recent CI runs
gh release create v1.0.0 # Create a release
gh repo view --web       # Open repo in browser
```
