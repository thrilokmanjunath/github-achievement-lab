"""
Tests for the `history` CLI subcommand (Issue #1).

Covers: empty-state message, populated history display,
session calculator sharing between commands.
"""

from __future__ import annotations

import io
import sys

import pytest

import achievement_lab.cli as cli_module
from achievement_lab.calculator import Calculator
from achievement_lab.cli import main


# ─── Helpers ─────────────────────────────────────────────────────────────────

def run_cmd(*argv: str) -> tuple[int, str]:
    """Run a CLI subcommand and capture stdout."""
    captured = io.StringIO()
    old_stdout = sys.stdout
    sys.stdout = captured
    try:
        code = main(list(argv))
    except SystemExit as exc:
        code = int(exc.code) if exc.code is not None else 0
    finally:
        sys.stdout = old_stdout
    return code, captured.getvalue()


# ─── Empty history ─────────────────────────────────────────────────────────────

class TestHistoryEmpty:
    def setup_method(self) -> None:
        """Reset the shared session calculator before each test."""
        cli_module._SESSION_CALC.clear_history()

    def test_history_exits_0_when_empty(self) -> None:
        code, _ = run_cmd("history")
        assert code == 0

    def test_history_shows_empty_message(self) -> None:
        _, output = run_cmd("history")
        assert "No calculations" in output or "no calculation" in output.lower()

    def test_history_suggests_calculate(self) -> None:
        _, output = run_cmd("history")
        assert "calculate" in output.lower()


# ─── Populated history ────────────────────────────────────────────────────────

class TestHistoryPopulated:
    def setup_method(self) -> None:
        """Reset and pre-populate the session calculator."""
        cli_module._SESSION_CALC.clear_history()
        cli_module._SESSION_CALC.add(10, 20)
        cli_module._SESSION_CALC.multiply(3, 4)
        cli_module._SESSION_CALC.divide(100, 4)

    def test_history_exits_0(self) -> None:
        code, _ = run_cmd("history")
        assert code == 0

    def test_history_shows_correct_count(self) -> None:
        _, output = run_cmd("history")
        assert "3 operation" in output

    def test_history_shows_first_result(self) -> None:
        _, output = run_cmd("history")
        assert "30" in output

    def test_history_shows_multiply_result(self) -> None:
        _, output = run_cmd("history")
        assert "12" in output

    def test_history_shows_divide_result(self) -> None:
        _, output = run_cmd("history")
        assert "25" in output

    def test_history_shows_numbered_entries(self) -> None:
        _, output = run_cmd("history")
        assert "1." in output
        assert "2." in output
        assert "3." in output


# ─── Session calculator sharing ───────────────────────────────────────────────

class TestSessionCalculatorSharing:
    def setup_method(self) -> None:
        cli_module._SESSION_CALC.clear_history()

    def test_session_calc_is_calculator_instance(self) -> None:
        assert isinstance(cli_module._SESSION_CALC, Calculator)

    def test_clear_history_resets_correctly(self) -> None:
        cli_module._SESSION_CALC.add(1, 1)
        cli_module._SESSION_CALC.clear_history()
        assert cli_module._SESSION_CALC.history == []

    def test_session_calc_accumulates(self) -> None:
        cli_module._SESSION_CALC.add(5, 5)
        cli_module._SESSION_CALC.subtract(10, 3)
        assert len(cli_module._SESSION_CALC.history) == 2
