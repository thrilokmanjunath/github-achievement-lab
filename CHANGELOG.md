# Changelog

All notable changes to **GitHub Achievement Lab** are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

---

## [1.0.0] — 2026-08-08

### Added

- **`achievement_lab.calculator`** — `Calculator` class with add, subtract, multiply, divide, and power
  operations; full input validation (type, NaN, Infinity); operation history tracking
- **`achievement_lab.workflows`** — `WorkflowGuide` with structured GitHub achievement data,
  workflow step documentation, and project status reporting
- **`achievement_lab.cli`** — Full CLI with subcommands:
  - `calculate [a] [b] [--operation OP]` — arithmetic with validation
  - `status` — project status report
  - `workflow` — standard GitHub PR workflow display
  - `achievements` — achievement guide and requirements
  - `about` — project information
- **GitHub Actions CI** — automated test pipeline on push and pull_request
- **Issue templates** — bug report and feature request forms
- **Pull request template** — structured PR checklist
- **`CONTRIBUTING.md`** — full contributor guide
- **`CODE_OF_CONDUCT.md`** — Contributor Covenant v2.1
- **`docs/github-workflow.md`** — detailed Git/GitHub workflow reference
- **`docs/achievement-guide.md`** — GitHub achievement legitimate route guide
- **`pyproject.toml`** — modern Python packaging with `[project.scripts]` entry-point

### Fixed

- Input validation for CLI numeric arguments prevents crashes on non-numeric input
- Division by zero is caught and reported with a clear error message

---

[Unreleased]: https://github.com/thrilokm/github-achievement-lab/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/thrilokm/github-achievement-lab/releases/tag/v1.0.0
