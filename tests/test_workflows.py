"""
Tests for the WorkflowGuide and Achievement classes.

Covers: achievement data integrity, status filtering,
workflow step structure, and project status reporting.
"""

from __future__ import annotations

import pytest

from achievement_lab.workflows import Achievement, AchievementStatus, WorkflowGuide


# ─── Achievement data integrity ───────────────────────────────────────────────

class TestAchievementList:
    def test_achievements_not_empty(self) -> None:
        assert len(WorkflowGuide.get_achievements()) > 0

    def test_all_achievements_have_names(self) -> None:
        for a in WorkflowGuide.get_achievements():
            assert isinstance(a.name, str)
            assert len(a.name) > 0

    def test_all_achievements_have_requirements(self) -> None:
        for a in WorkflowGuide.get_achievements():
            assert isinstance(a.requirement, str)
            assert len(a.requirement) > 0

    def test_all_achievements_have_valid_status(self) -> None:
        valid_statuses = set(AchievementStatus)
        for a in WorkflowGuide.get_achievements():
            assert a.status in valid_statuses

    def test_achievement_names_are_unique(self) -> None:
        names = [a.name for a in WorkflowGuide.get_achievements()]
        assert len(names) == len(set(names))


# ─── Status filtering ─────────────────────────────────────────────────────────

class TestAchievementFiltering:
    def test_available_excludes_historical(self) -> None:
        available = WorkflowGuide.get_available_achievements()
        for a in available:
            assert a.status != AchievementStatus.HISTORICAL

    def test_available_includes_earnable(self) -> None:
        available = WorkflowGuide.get_available_achievements()
        statuses = {a.status for a in available}
        assert AchievementStatus.AVAILABLE in statuses

    def test_historical_achievements_exist(self) -> None:
        historical = [
            a for a in WorkflowGuide.get_achievements()
            if a.status == AchievementStatus.HISTORICAL
        ]
        assert len(historical) >= 1

    def test_pull_shark_is_available(self) -> None:
        available = WorkflowGuide.get_available_achievements()
        names = [a.name for a in available]
        assert "Pull Shark" in names


# ─── Achievement display ──────────────────────────────────────────────────────

class TestAchievementDisplay:
    def test_display_contains_name(self) -> None:
        a = Achievement(
            name="Test Achievement",
            status=AchievementStatus.AVAILABLE,
            requirement="Do something",
        )
        assert "Test Achievement" in a.display()

    def test_display_contains_requirement(self) -> None:
        a = Achievement(
            name="X",
            status=AchievementStatus.AVAILABLE,
            requirement="A specific requirement",
        )
        assert "A specific requirement" in a.display()

    def test_display_contains_tier_when_set(self) -> None:
        a = Achievement(
            name="X",
            status=AchievementStatus.AVAILABLE,
            requirement="...",
            tier="Bronze×2",
        )
        assert "Bronze×2" in a.display()

    def test_display_no_tier_field_when_absent(self) -> None:
        a = Achievement(
            name="X",
            status=AchievementStatus.AVAILABLE,
            requirement="...",
        )
        assert "Tier" not in a.display()


# ─── Workflow steps ───────────────────────────────────────────────────────────

class TestWorkflowSteps:
    def test_steps_not_empty(self) -> None:
        assert len(WorkflowGuide.get_workflow_steps()) > 0

    def test_steps_are_ordered(self) -> None:
        steps = WorkflowGuide.get_workflow_steps()
        numbers = [s.number for s in steps]
        assert numbers == sorted(numbers)

    def test_steps_start_at_one(self) -> None:
        steps = WorkflowGuide.get_workflow_steps()
        assert steps[0].number == 1

    def test_all_steps_have_commands(self) -> None:
        for step in WorkflowGuide.get_workflow_steps():
            assert isinstance(step.command, str)
            assert len(step.command) > 0

    def test_step_display_contains_number(self) -> None:
        steps = WorkflowGuide.get_workflow_steps()
        first = steps[0]
        assert str(first.number) in first.display()


# ─── Project status ───────────────────────────────────────────────────────────

class TestProjectStatus:
    def test_status_has_required_keys(self) -> None:
        status = WorkflowGuide.get_project_status()
        required = {
            "project", "version", "total_achievements",
            "available_achievements", "historical_achievements",
            "workflow_steps", "achievement_names",
        }
        assert required.issubset(status.keys())

    def test_counts_are_consistent(self) -> None:
        status = WorkflowGuide.get_project_status()
        total = status["total_achievements"]
        available = status["available_achievements"]
        historical = status["historical_achievements"]
        assert available + historical <= total  # conditional may not be counted

    def test_achievement_names_list(self) -> None:
        status = WorkflowGuide.get_project_status()
        names = status["achievement_names"]
        assert isinstance(names, list)
        assert len(names) > 0
        assert all(isinstance(n, str) for n in names)

    def test_version_format(self) -> None:
        status = WorkflowGuide.get_project_status()
        parts = str(status["version"]).split(".")
        assert len(parts) == 3
