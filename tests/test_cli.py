"""
Tests for the CLI entry-point (cmd_calculate validation improvements).

Covers: per-argument error messages, exit codes, valid operations.
These tests were added as part of fix/cli-validation (Issue #2).
"""

from __future__ import annotations

import pytest

from achievement_lab.cli import build_parser, cmd_calculate, main


# ─── Helpers ─────────────────────────────────────────────────────────────────

def run_calculate(*args: str) -> tuple[int, str]:
    """Run the calculate subcommand and return (exit_code, stderr_output)."""
    import io
    import sys

    captured = io.StringIO()
    old_stderr = sys.stderr
    sys.stderr = captured

    try:
        code = main(["calculate", *args])
    except SystemExit as exc:
        code = int(exc.code) if exc.code is not None else 0
    finally:
        sys.stderr = old_stderr

    return code, captured.getvalue()


# ─── Valid operations ─────────────────────────────────────────────────────────

class TestValidCalculations:
    def test_add_default(self) -> None:
        code, _ = run_calculate("10", "20")
        assert code == 0

    def test_subtract(self) -> None:
        code, _ = run_calculate("10", "3", "--operation", "subtract")
        assert code == 0

    def test_multiply(self) -> None:
        code, _ = run_calculate("4", "5", "--operation", "multiply")
        assert code == 0

    def test_divide(self) -> None:
        code, _ = run_calculate("20", "4", "--operation", "divide")
        assert code == 0

    def test_power(self) -> None:
        code, _ = run_calculate("2", "8", "--operation", "power")
        assert code == 0


# ─── Validation: invalid first argument ──────────────────────────────────────

class TestFirstArgumentValidation:
    def test_string_first_arg_exits_2(self) -> None:
        code, stderr = run_calculate("abc", "20")
        assert code == 2

    def test_string_first_arg_mentions_first(self) -> None:
        code, stderr = run_calculate("abc", "20")
        assert "first" in stderr.lower()

    def test_string_first_arg_echoes_bad_value(self) -> None:
        code, stderr = run_calculate("not_a_number", "20")
        assert "not_a_number" in stderr

    def test_first_arg_error_includes_usage_hint(self) -> None:
        code, stderr = run_calculate("bad", "20")
        assert "Usage" in stderr or "usage" in stderr


# ─── Validation: invalid second argument ─────────────────────────────────────

class TestSecondArgumentValidation:
    def test_string_second_arg_exits_2(self) -> None:
        code, stderr = run_calculate("10", "xyz")
        assert code == 2

    def test_string_second_arg_mentions_second(self) -> None:
        code, stderr = run_calculate("10", "xyz")
        assert "second" in stderr.lower()

    def test_string_second_arg_echoes_bad_value(self) -> None:
        code, stderr = run_calculate("10", "bad_value")
        assert "bad_value" in stderr

    def test_second_arg_error_includes_usage_hint(self) -> None:
        code, stderr = run_calculate("10", "bad")
        assert "Usage" in stderr or "usage" in stderr


# ─── Division by zero ─────────────────────────────────────────────────────────

class TestDivisionByZero:
    def test_divide_by_zero_exits_1(self) -> None:
        code, _ = run_calculate("10", "0", "--operation", "divide")
        assert code == 1


# ─── Unknown operation ────────────────────────────────────────────────────────

class TestUnknownOperation:
    def test_unknown_op_exits_2(self) -> None:
        code, _ = run_calculate("10", "20", "--operation", "modulo")
        assert code == 2
