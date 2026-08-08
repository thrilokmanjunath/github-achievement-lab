"""
GitHub Achievement Lab — A CLI toolkit for learning GitHub workflows.

This package provides utilities for demonstrating professional Git/GitHub
practices including branching, CI/CD, code review, and collaboration.
"""

__version__ = "1.0.0"
__author__ = "Thrilok Manjunath"
__email__ = "ankushthrilok@gmail.com"
__license__ = "MIT"

from achievement_lab.calculator import Calculator
from achievement_lab.workflows import WorkflowGuide

__all__ = ["Calculator", "WorkflowGuide", "__version__"]
