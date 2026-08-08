"""
Tests for the project status reporting enhancement.

Covers: get_achievement_progress() return structure,
ordering, completeness, and CLI --verbose flag output.
These tests were added as part of feature/project-status (Issue #1 related).
"""

from __future__ import annotations

import io
import sys

import pytest

from achievement_lab.workflows import AchievementStatus, WorkflowGuide


# ─── get_achievement_progress structure ───────────────────────────────────────

class TestAchievementProgress:
    def test_returns_list(self) -> None:
        result = WorkflowGuide.get_achievement_progress()
        assert isinstance(result, list)

    def test_not_empty(self) -> None:
        assert len(WorkflowGuide.get_achievement_progress()) > 0

    def test_each_entry_has_required_keys(self) -> None:
        required = {"name", "status", "requirement", "tier", "notes"}
        for item in WorkflowGuide.get_achievement_progress():
            assert required.issubset(item.keys()), f"Missing keys in {item}"

    def test_all_names_are_strings(self) -> None:
        for item in WorkflowGuide.get_achievement_progress():
            assert isinstance(item["name"], str)
            assert len(item["name"]) > 0

    def test_historical_sorted_last(self) -> None:
        progress = WorkflowGuide.get_achievement_progress()
        historical_indices = [
            i for i, item in enumerate(progress)
            if AchievementStatus.HISTORICAL.value in str(item["status"])
        ]
        available_indices = [
            i for i, item in enumerate(progress)
            if AchievementStatus.AVAILABLE.value in str(item["status"])
        ]
        if historical_indices and available_indices:
            assert min(historical_indices) > max(available_indices)

    def test_count_matches_achievements(self) -> None:
        progress = WorkflowGuide.get_achievement_progress()
        all_achievements = WorkflowGuide.get_achievements()
        assert len(progress) == len(all_achievements)

    def test_tier_placeholder_for_no_tier(self) -> None:
        for item in WorkflowGuide.get_achievement_progress():
            # tier must be a non-empty string (either real tier or "—")
            assert isinstance(item["tier"], str)
            assert len(item["tier"]) > 0


# ─── CLI --verbose flag ───────────────────────────────────────────────────────

def run_status(*args: str) -> tuple[int, str]:
    """Run the status subcommand and capture stdout."""
    from achievement_lab.cli import main
    captured = io.StringIO()
    old_stdout = sys.stdout
    sys.stdout = captured
    try:
        code = main(["status", *args])
    except SystemExit as exc:
        code = int(exc.code) if exc.code is not None else 0
    finally:
        sys.stdout = old_stdout
    return code, captured.getvalue()


class TestStatusVerboseFlag:
    def test_status_exits_0(self) -> None:
        code, _ = run_status()
        assert code == 0

    def test_status_verbose_exits_0(self) -> None:
        code, _ = run_status("--verbose")
        assert code == 0

    def test_verbose_shows_achievement_table(self) -> None:
        _, output = run_status("--verbose")
        assert "Achievement Progress Table" in output

    def test_verbose_contains_pull_shark(self) -> None:
        _, output = run_status("--verbose")
        assert "Pull Shark" in output

    def test_verbose_contains_historical(self) -> None:
        _, output = run_status("--verbose")
        assert "Historical" in output or "🔴" in output

    def test_non_verbose_shows_tip(self) -> None:
        _, output = run_status()
        assert "--verbose" in output

    def test_non_verbose_shows_earnable_list(self) -> None:
        _, output = run_status()
        assert "Earnable Achievements" in output
