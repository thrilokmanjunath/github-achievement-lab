"""
Tests for the Calculator class.

Covers: arithmetic operations, input validation, history tracking,
division by zero, and edge cases with NaN/Infinity.
"""

from __future__ import annotations

import math
import pytest

from achievement_lab.calculator import Calculator, ValidationError


# ─── Fixtures ────────────────────────────────────────────────────────────────

@pytest.fixture
def calc() -> Calculator:
    """Return a fresh Calculator instance for each test."""
    return Calculator()


# ─── Addition ─────────────────────────────────────────────────────────────────

class TestAdd:
    def test_integers(self, calc: Calculator) -> None:
        assert calc.add(10, 20) == 30

    def test_floats(self, calc: Calculator) -> None:
        assert math.isclose(calc.add(1.5, 2.5), 4.0)

    def test_negative(self, calc: Calculator) -> None:
        assert calc.add(-5, 3) == -2

    def test_zero(self, calc: Calculator) -> None:
        assert calc.add(0, 0) == 0


# ─── Subtraction ─────────────────────────────────────────────────────────────

class TestSubtract:
    def test_basic(self, calc: Calculator) -> None:
        assert calc.subtract(10, 4) == 6

    def test_negative_result(self, calc: Calculator) -> None:
        assert calc.subtract(3, 10) == -7

    def test_floats(self, calc: Calculator) -> None:
        assert math.isclose(calc.subtract(5.5, 2.2), 3.3)


# ─── Multiplication ──────────────────────────────────────────────────────────

class TestMultiply:
    def test_basic(self, calc: Calculator) -> None:
        assert calc.multiply(4, 5) == 20

    def test_by_zero(self, calc: Calculator) -> None:
        assert calc.multiply(99, 0) == 0

    def test_floats(self, calc: Calculator) -> None:
        assert math.isclose(calc.multiply(2.5, 4.0), 10.0)

    def test_negative(self, calc: Calculator) -> None:
        assert calc.multiply(-3, -4) == 12


# ─── Division ─────────────────────────────────────────────────────────────────

class TestDivide:
    def test_basic(self, calc: Calculator) -> None:
        assert calc.divide(10, 2) == 5.0

    def test_float_result(self, calc: Calculator) -> None:
        assert math.isclose(calc.divide(1, 3), 0.3333333333333333)

    def test_divide_by_zero(self, calc: Calculator) -> None:
        with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
            calc.divide(10, 0)

    def test_negative_dividend(self, calc: Calculator) -> None:
        assert calc.divide(-10, 2) == -5.0


# ─── Power ────────────────────────────────────────────────────────────────────

class TestPower:
    def test_square(self, calc: Calculator) -> None:
        assert calc.power(3, 2) == 9

    def test_zero_exponent(self, calc: Calculator) -> None:
        assert calc.power(100, 0) == 1

    def test_fractional_exponent(self, calc: Calculator) -> None:
        assert math.isclose(calc.power(4, 0.5), 2.0)


# ─── Validation ───────────────────────────────────────────────────────────────

class TestValidation:
    def test_string_input_a(self, calc: Calculator) -> None:
        with pytest.raises(ValidationError, match="must be a number"):
            calc.add("abc", 5)  # type: ignore[arg-type]

    def test_string_input_b(self, calc: Calculator) -> None:
        with pytest.raises(ValidationError, match="must be a number"):
            calc.add(5, "xyz")  # type: ignore[arg-type]

    def test_none_input(self, calc: Calculator) -> None:
        with pytest.raises(ValidationError, match="must be a number"):
            calc.multiply(None, 3)  # type: ignore[arg-type]

    def test_nan_input(self, calc: Calculator) -> None:
        with pytest.raises(ValidationError, match="NaN"):
            calc.add(float("nan"), 1)

    def test_inf_input(self, calc: Calculator) -> None:
        with pytest.raises(ValidationError, match="finite"):
            calc.add(float("inf"), 1)

    def test_negative_inf_input(self, calc: Calculator) -> None:
        with pytest.raises(ValidationError, match="finite"):
            calc.subtract(1, float("-inf"))

    def test_list_input(self, calc: Calculator) -> None:
        with pytest.raises(ValidationError):
            calc.divide([1, 2], 3)  # type: ignore[arg-type]


# ─── History ──────────────────────────────────────────────────────────────────

class TestHistory:
    def test_records_operation(self, calc: Calculator) -> None:
        calc.add(1, 2)
        assert len(calc.history) == 1
        assert calc.history[0]["result"] == 3

    def test_multiple_operations(self, calc: Calculator) -> None:
        calc.add(1, 1)
        calc.multiply(3, 3)
        calc.divide(10, 2)
        assert len(calc.history) == 3

    def test_history_is_copy(self, calc: Calculator) -> None:
        calc.add(1, 1)
        h = calc.history
        h.clear()
        assert len(calc.history) == 1

    def test_clear_history(self, calc: Calculator) -> None:
        calc.add(1, 1)
        calc.clear_history()
        assert calc.history == []
