"""
Workflow guide module for GitHub Achievement Lab.

Provides structured information about GitHub workflows,
best practices, and achievement progression guidance.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


class AchievementStatus(Enum):
    """Status of a GitHub achievement."""
    AVAILABLE = "🟢 Available"
    CONDITIONAL = "🟡 Conditional"
    HISTORICAL = "🔴 Historical (no longer earnable)"
    VERIFIED = "✅ Verified"


@dataclass
class Achievement:
    """Represents a single GitHub achievement."""
    name: str
    status: AchievementStatus
    requirement: str
    tier: Optional[str] = None
    notes: str = ""

    def display(self) -> str:
        """Return a formatted display string."""
        lines = [
            f"  Achievement : {self.name}",
            f"  Status      : {self.status.value}",
            f"  Requirement : {self.requirement}",
        ]
        if self.tier:
            lines.append(f"  Tier        : {self.tier}")
        if self.notes:
            lines.append(f"  Notes       : {self.notes}")
        return "\n".join(lines)


@dataclass
class WorkflowStep:
    """A single step in a GitHub workflow."""
    number: int
    title: str
    command: str
    description: str

    def display(self) -> str:
        """Return a formatted display string."""
        return (
            f"  Step {self.number}: {self.title}\n"
            f"    $ {self.command}\n"
            f"    → {self.description}"
        )


class WorkflowGuide:
    """
    Provides guidance on professional GitHub workflows and achievement paths.

    This class encapsulates structured knowledge about Git/GitHub best practices
    to help developers build genuine open-source collaboration skills.
    """

    ACHIEVEMENTS: list[Achievement] = [
        Achievement(
            name="Quickdraw",
            status=AchievementStatus.AVAILABLE,
            requirement="Close an issue or PR within 5 minutes of opening it",
            notes="Open a valid issue, realize it's a duplicate, close it quickly",
        ),
        Achievement(
            name="Pull Shark",
            status=AchievementStatus.AVAILABLE,
            requirement="Merge 2 pull requests (bronze tier)",
            tier="Bronze×2, Silver×16, Gold×128 merged PRs",
            notes="Each genuine merged PR counts; multiple tiers available",
        ),
        Achievement(
            name="Pair Extraordinaire",
            status=AchievementStatus.AVAILABLE,
            requirement="Co-author a merged pull request",
            tier="Bronze×1, Silver×10, Gold×100 co-authored PRs",
            notes="Requires a real second contributor added via Co-authored-by trailer",
        ),
        Achievement(
            name="Galaxy Brain",
            status=AchievementStatus.AVAILABLE,
            requirement="Have a discussion answer marked as 'Answered'",
            tier="Bronze×8, Silver×16, Gold×32 accepted answers",
            notes="Must be a genuine community answer accepted by the OP",
        ),
        Achievement(
            name="Starstruck",
            status=AchievementStatus.AVAILABLE,
            requirement="Create a repository that receives 16 stars (bronze tier)",
            tier="Bronze×16, Silver×128, Gold×512, Platinum×4096 stars",
            notes="Stars must be genuine — bots or purchased stars violate ToS",
        ),
        Achievement(
            name="YOLO",
            status=AchievementStatus.AVAILABLE,
            requirement="Merge a pull request without a code review",
            notes="Works on your own repos; not recommended for production",
        ),
        Achievement(
            name="Arctic Code Vault Contributor",
            status=AchievementStatus.HISTORICAL,
            requirement="Contributed code to the 2020 GitHub Archive Program snapshot",
            notes="No longer earnable — snapshot was taken Feb 2, 2020",
        ),
        Achievement(
            name="Mars 2020 Helicopter Contributor",
            status=AchievementStatus.HISTORICAL,
            requirement="Contributed to a repo used by the Mars 2020 mission",
            notes="No longer earnable — awarded for contributions before launch",
        ),
        Achievement(
            name="Public Sponsor",
            status=AchievementStatus.AVAILABLE,
            requirement="Sponsor an open-source developer via GitHub Sponsors",
            notes="Must be a genuine financial sponsorship",
        ),
    ]

    WORKFLOW_STEPS: list[WorkflowStep] = [
        WorkflowStep(1, "Create an Issue", "gh issue create", "Describe the problem or feature"),
        WorkflowStep(2, "Create a Branch", "git checkout -b feature/my-feature", "One branch per feature/fix"),
        WorkflowStep(3, "Make Changes", "git add . && git commit -m 'feat: ...'", "Conventional commit messages"),
        WorkflowStep(4, "Push Branch", "git push -u origin feature/my-feature", "Publish branch to remote"),
        WorkflowStep(5, "Open PR", "gh pr create --fill", "Reference the issue; describe changes"),
        WorkflowStep(6, "CI Runs", "(automatic)", "GitHub Actions validates the code"),
        WorkflowStep(7, "Code Review", "gh pr view --comments", "Address reviewer feedback"),
        WorkflowStep(8, "Merge PR", "gh pr merge --squash", "Squash for clean history"),
        WorkflowStep(9, "Close Issue", "(automatic via PR body)", "Use 'Closes #N' in the PR description"),
        WorkflowStep(10, "Tag Release", "git tag v1.0.0 && git push --tags", "Semantic versioning"),
    ]

    @classmethod
    def get_achievements(cls) -> list[Achievement]:
        """Return the full achievement list."""
        return cls.ACHIEVEMENTS

    @classmethod
    def get_available_achievements(cls) -> list[Achievement]:
        """Return only currently earnable achievements."""
        return [
            a for a in cls.ACHIEVEMENTS
            if a.status not in (AchievementStatus.HISTORICAL,)
        ]

    @classmethod
    def get_workflow_steps(cls) -> list[WorkflowStep]:
        """Return the standard PR workflow steps."""
        return cls.WORKFLOW_STEPS

    @classmethod
    def get_project_status(cls) -> dict[str, object]:
        """
        Return a summary of the current project status.

        Returns:
            A dict with project metadata and workflow statistics.
        """
        available = cls.get_available_achievements()
        historical = [
            a for a in cls.ACHIEVEMENTS
            if a.status == AchievementStatus.HISTORICAL
        ]
        return {
            "project": "GitHub Achievement Lab",
            "version": "1.0.0",
            "total_achievements": len(cls.ACHIEVEMENTS),
            "available_achievements": len(available),
            "historical_achievements": len(historical),
            "workflow_steps": len(cls.WORKFLOW_STEPS),
            "achievement_names": [a.name for a in available],
        }
