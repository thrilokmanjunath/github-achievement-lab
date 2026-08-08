# GitHub Achievement Lab

> **Learn professional GitHub workflows through a real, working Python project.**

[![CI](https://github.com/thrilokm/github-achievement-lab/actions/workflows/ci.yml/badge.svg)](https://github.com/thrilokm/github-achievement-lab/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

---

## 1. Overview

GitHub Achievement Lab is a production-quality open-source Python project designed to help developers
learn and practise professional GitHub workflows — branching, pull requests, CI/CD, code review, and collaboration —
through genuine, hands-on contribution to a real codebase.

The project is also a sandbox for legitimately earning GitHub profile achievements through authentic Git activity.

---

## 2. Features

| Feature | Description |
|---|---|
| 🧮 **Arithmetic CLI** | Clean command-line calculator with full validation |
| 🔄 **Workflow Guide** | Interactive display of the standard GitHub PR workflow |
| 🏆 **Achievement Guide** | Structured reference for all current GitHub achievements |
| 📊 **Status Report** | Project-level summary of achievements and workflow |
| ✅ **Unit Tests** | Comprehensive test suite with pytest |
| 🤖 **CI/CD** | GitHub Actions workflow for automated testing |
| 📄 **Full Documentation** | Issue templates, PR templates, contributing guide |

---

## 3. Installation

### Prerequisites

- Python 3.10 or higher
- Git

### Clone and install

```bash
# Clone the repository
git clone https://github.com/thrilokm/github-achievement-lab.git
cd github-achievement-lab

# Create a virtual environment
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# Install in editable mode with dev dependencies
pip install -e ".[dev]"
```

---

## 4. Usage

```bash
# Basic arithmetic
achievement-lab calculate 10 20
achievement-lab calculate 100 4 --operation divide
achievement-lab calculate 2 10 --operation power

# Available operations: add | subtract | multiply | divide | power

# Show project status
achievement-lab status

# Show the GitHub PR workflow
achievement-lab workflow

# Show achievement guide
achievement-lab achievements

# About this project
achievement-lab about

# Version
achievement-lab --version
```

### Example output

```
achievement-lab calculate 10 20
  10.0 + 20.0 = 30.0

achievement-lab calculate 10 0 --operation divide
✗ Math error: Cannot divide by zero
```

---

## 5. Project Architecture

```
github-achievement-lab/
├── src/
│   └── achievement_lab/
│       ├── __init__.py       # Package metadata and public API
│       ├── cli.py            # CLI entry-point (argparse)
│       ├── calculator.py     # Arithmetic engine with validation
│       └── workflows.py      # Achievement and workflow data
├── tests/
│   ├── test_calculator.py    # Calculator unit tests
│   └── test_workflows.py     # Workflow/achievement unit tests
├── docs/
│   ├── github-workflow.md    # Detailed GitHub workflow guide
│   └── achievement-guide.md  # Achievement reference
├── .github/
│   ├── ISSUE_TEMPLATE/       # Structured issue forms
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── workflows/
│       └── ci.yml            # GitHub Actions CI pipeline
├── pyproject.toml            # Modern Python packaging
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
└── CHANGELOG.md
```

---

## 6. Development Workflow

```bash
# 1. Fork and clone
git clone https://github.com/thrilokm/github-achievement-lab.git
cd github-achievement-lab

# 2. Create a feature branch
git checkout -b feature/your-feature-name

# 3. Make changes, add tests
# ... edit code ...

# 4. Run the test suite
python -m pytest

# 5. Commit with conventional style
git commit -m "feat: add your feature description"

# 6. Push and open a PR
git push -u origin feature/your-feature-name
gh pr create --fill
```

---

## 7. GitHub Workflow

See [`docs/github-workflow.md`](docs/github-workflow.md) for a detailed walkthrough of:

- Creating issues
- Branching strategies
- Pull request lifecycle
- Code review etiquette
- Squash merging
- Tagging releases
- Co-authored commits

---

## 8. Contributing

Please read [`CONTRIBUTING.md`](CONTRIBUTING.md) before submitting a pull request.

We follow:
- [Conventional Commits](https://www.conventionalcommits.org/)
- [Semantic Versioning](https://semver.org/)
- [Contributor Covenant Code of Conduct](CODE_OF_CONDUCT.md)

---

## 9. Testing

```bash
# Run all tests
python -m pytest

# Run with coverage
python -m pytest --cov=achievement_lab --cov-report=term-missing

# Run a specific test file
python -m pytest tests/test_calculator.py -v

# Compile check
python -m compileall src
```

---

## 10. CI/CD

Every push and pull request triggers the GitHub Actions CI pipeline (`.github/workflows/ci.yml`) which:

1. Checks out the code
2. Sets up Python 3.13
3. Installs the project with dev dependencies
4. Runs `python -m compileall src`
5. Runs `python -m pytest`

All PRs must pass CI before merging.

---

## 11. GitHub Achievement Learning Path

See [`docs/achievement-guide.md`](docs/achievement-guide.md) for a complete reference.

| Achievement | How to earn it legitimately |
|---|---|
| **Pull Shark** | Open and merge genuine pull requests |
| **Quickdraw** | Close an issue or PR within 5 minutes of opening |
| **Pair Extraordinaire** | Co-author a merged PR with a real contributor |
| **Galaxy Brain** | Have a discussion answer accepted as the answer |
| **Starstruck** | Earn 16+ genuine stars on a repository |
| **YOLO** | Merge a PR without a code review |
| **Public Sponsor** | Sponsor a developer via GitHub Sponsors |

> ⚠️ Do not use bots, fake accounts, or any method that violates GitHub's Terms of Service.

---

## 12. License

This project is licensed under the [MIT License](LICENSE).

---

*Built with ❤️ to help developers grow their GitHub skills authentically.*
