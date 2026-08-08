"""
Calculator module for GitHub Achievement Lab.

Provides arithmetic operations with robust input validation,
demonstrating proper Python error handling and type hints.
"""

from __future__ import annotations

from typing import Union

Number = Union[int, float]


class ValidationError(ValueError):
    """Raised when invalid numeric input is provided."""
    pass


class Calculator:
    """
    A clean, well-tested arithmetic calculator.

    Demonstrates Python best practices: type hints, docstrings,
    custom exceptions, and comprehensive input validation.

    Examples:
        >>> calc = Calculator()
        >>> calc.add(10, 20)
        30
        >>> calc.divide(10, 0)
        Traceback (most recent call last):
            ...
        ZeroDivisionError: Cannot divide by zero
    """

    def __init__(self) -> None:
        self._history: list[dict[str, object]] = []

    @staticmethod
    def _validate(value: object, name: str = "value") -> Number:
        """
        Validate that a value is a real number (int or float), not NaN or Inf.

        Args:
            value: The value to validate.
            name: Label used in error messages.

        Returns:
            The validated number.

        Raises:
            ValidationError: If the value is not a valid finite number.
        """
        if not isinstance(value, (int, float)):
            raise ValidationError(
                f"'{name}' must be a number, got {type(value).__name__!r}: {value!r}"
            )
        import math
        if math.isnan(value):
            raise ValidationError(f"'{name}' must not be NaN")
        if math.isinf(value):
            raise ValidationError(f"'{name}' must be a finite number, got infinity")
        return value

    def _record(self, operation: str, result: Number) -> None:
        """Record a completed operation in the history log."""
        self._history.append({"operation": operation, "result": result})

    @property
    def history(self) -> list[dict[str, object]]:
        """Return a copy of the operation history."""
        return list(self._history)

    def add(self, a: Number, b: Number) -> Number:
        """
        Add two numbers.

        Args:
            a: The first operand.
            b: The second operand.

        Returns:
            The sum of a and b.

        Raises:
            ValidationError: If either argument is not a valid finite number.
        """
        a = self._validate(a, "a")
        b = self._validate(b, "b")
        result = a + b
        self._record(f"{a} + {b}", result)
        return result

    def subtract(self, a: Number, b: Number) -> Number:
        """
        Subtract b from a.

        Args:
            a: The minuend.
            b: The subtrahend.

        Returns:
            The difference a − b.

        Raises:
            ValidationError: If either argument is not a valid finite number.
        """
        a = self._validate(a, "a")
        b = self._validate(b, "b")
        result = a - b
        self._record(f"{a} - {b}", result)
        return result

    def multiply(self, a: Number, b: Number) -> Number:
        """
        Multiply two numbers.

        Args:
            a: The first factor.
            b: The second factor.

        Returns:
            The product of a and b.

        Raises:
            ValidationError: If either argument is not a valid finite number.
        """
        a = self._validate(a, "a")
        b = self._validate(b, "b")
        result = a * b
        self._record(f"{a} × {b}", result)
        return result

    def divide(self, a: Number, b: Number) -> float:
        """
        Divide a by b.

        Args:
            a: The dividend.
            b: The divisor (must not be zero).

        Returns:
            The quotient a / b as a float.

        Raises:
            ValidationError: If either argument is not a valid finite number.
            ZeroDivisionError: If b is zero.
        """
        a = self._validate(a, "a")
        b = self._validate(b, "b")
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        result = a / b
        self._record(f"{a} ÷ {b}", result)
        return result

    def power(self, base: Number, exponent: Number) -> Number:
        """
        Raise base to the power of exponent.

        Args:
            base: The base value.
            exponent: The exponent.

        Returns:
            base ** exponent.

        Raises:
            ValidationError: If either argument is not a valid finite number.
        """
        base = self._validate(base, "base")
        exponent = self._validate(exponent, "exponent")
        result = base ** exponent
        self._record(f"{base} ^ {exponent}", result)
        return result

    def clear_history(self) -> None:
        """Clear the operation history."""
        self._history.clear()
