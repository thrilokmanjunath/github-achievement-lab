# Contributing to GitHub Achievement Lab

Thank you for your interest in contributing! This project exists to help developers
build genuine GitHub skills — every contribution is welcome.

---

## Table of Contents

1. [Code of Conduct](#code-of-conduct)
2. [Getting Started](#getting-started)
3. [Development Setup](#development-setup)
4. [Branching Strategy](#branching-strategy)
5. [Commit Messages](#commit-messages)
6. [Pull Request Process](#pull-request-process)
7. [Testing](#testing)
8. [Code Style](#code-style)
9. [Reporting Bugs](#reporting-bugs)
10. [Suggesting Features](#suggesting-features)

---

## Code of Conduct

This project adheres to the [Contributor Covenant Code of Conduct](CODE_OF_CONDUCT.md).
By participating you are expected to uphold this standard.

---

## Getting Started

1. **Fork** the repository on GitHub
2. **Clone** your fork locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/github-achievement-lab.git
   cd github-achievement-lab
   ```
3. **Add the upstream remote**:
   ```bash
   git remote add upstream https://github.com/thrilokm/github-achievement-lab.git
   ```
4. **Create a virtual environment and install dependencies**:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -e ".[dev]"
   ```

---

## Development Setup

```bash
# Verify your setup
python -m pytest
achievement-lab --version
```

---

## Branching Strategy

Use descriptive branch names with a category prefix:

| Prefix | Purpose | Example |
|---|---|---|
| `feature/` | New features | `feature/add-statistics-command` |
| `fix/` | Bug fixes | `fix/division-validation-error` |
| `docs/` | Documentation | `docs/update-workflow-guide` |
| `test/` | Tests only | `test/add-edge-case-coverage` |
| `chore/` | Maintenance | `chore/update-dependencies` |

Always branch from `main`:
```bash
git checkout main
git pull upstream main
git checkout -b feature/your-feature
```

---

## Commit Messages

We follow [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <short description>

[optional body]

[optional footer(s)]
```

**Types**: `feat`, `fix`, `docs`, `test`, `chore`, `refactor`, `perf`, `ci`

**Examples**:
```
feat(cli): add subtract command
fix(calculator): handle NaN input gracefully
docs(readme): add installation section
test(calculator): add edge case for large exponents
```

**Co-authored commits** (for pair programming):
```
feat(calculator): add statistics functions

Co-authored-by: Collaborator Name <collaborator@example.com>
```

---

## Pull Request Process

1. **Ensure tests pass**: `python -m pytest`
2. **Update documentation** if your change affects the public API or CLI
3. **Reference the issue** in your PR description: `Closes #N`
4. **Fill in the PR template** completely
5. **Request a review** from a maintainer
6. **Respond to feedback** — address all comments before merge

PRs are merged using **squash merge** to keep history clean.

---

## Testing

```bash
# Run all tests
python -m pytest

# Run with coverage report
python -m pytest --cov=achievement_lab --cov-report=term-missing

# Run a specific test file
python -m pytest tests/test_calculator.py -v
```

**Rules**:
- All new code must have tests
- Tests live in `tests/` and mirror the `src/` structure
- Test file names must start with `test_`
- Use descriptive test class and method names

---

## Code Style

- Follow **PEP 8**
- Use **type hints** on all function signatures
- Write **docstrings** for all public classes and functions
- Maximum line length: **100 characters**
- Use `from __future__ import annotations` at the top of each module

---

## Reporting Bugs

Use the [Bug Report issue template](.github/ISSUE_TEMPLATE/bug_report.md).

Include:
- Python version (`python3 --version`)
- OS and version
- Steps to reproduce
- Expected vs actual behaviour
- Error message / traceback

---

## Suggesting Features

Use the [Feature Request issue template](.github/ISSUE_TEMPLATE/feature_request.md).

Include:
- The problem you are trying to solve
- Your proposed solution
- Alternatives you considered
- Any additional context
