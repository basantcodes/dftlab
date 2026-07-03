"""dftlab.core.element
======================

Lightweight Element class used across dftlab.

This module provides a simple, well-documented Element value type that
stores a chemical element's symbol, atomic number and standard atomic mass.

The documentation strings follow Sphinx/reStructuredText conventions so they
can be included in the project API docs.

Example
-------
>>> from dftlab.core.element import Element
>>> Element("C", 6, 12.011)
Element(symbol='C', atomic_number=6, atomic_mass=12.011)
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class Element:
    """Representation of a chemical element.

    Parameters
    ----------
    symbol:
        The element symbol, e.g. ``"H"``, ``"He"``. Must be a non-empty
        string starting with an uppercase letter.
    atomic_number:
        The element's atomic number (Z). Must be a positive integer.
    atomic_mass:
        Standard atomic mass in atomic mass units (u). A positive float.

    Attributes
    ----------
    symbol, atomic_number, atomic_mass

    Notes
    -----
    This class is intentionally minimal. Validation is performed on
    construction to catch obvious errors early.
    """

    symbol: str = field()
    atomic_number: int = field()
    atomic_mass: float = field()

    def __post_init__(self) -> None:  # type: ignore[override]
        # Validate symbol
        if not isinstance(self.symbol, str) or not self.symbol:
            raise TypeError("symbol must be a non-empty string")
        if not self.symbol[0].isupper():
            raise ValueError("symbol must start with an uppercase letter")

        # Validate atomic_number
        if not isinstance(self.atomic_number, int) or self.atomic_number <= 0:
            raise TypeError("atomic_number must be a positive integer")

        # Validate atomic_mass
        if not isinstance(self.atomic_mass, (int, float)) or self.atomic_mass <= 0:
            raise TypeError("atomic_mass must be a positive number")

    def to_dict(self) -> dict[str, Any]:
        """Return a plain dict representation of the element.

        Returns
        -------
        dict
            Dictionary with keys ``symbol``, ``atomic_number`` and
            ``atomic_mass``.
        """
        return {
            "symbol": self.symbol,
            "atomic_number": self.atomic_number,
            "atomic_mass": float(self.atomic_mass),
        }

    def __repr__(self) -> str:  # pragma: no cover - trivial
        return f"Element(symbol={self.symbol!r}, atomic_number={self.atomic_number!r}, atomic_mass={self.atomic_mass!r})"

    def __eq__(self, other: object) -> bool:  # pragma: no cover - dataclass would provide, but be explicit
        if not isinstance(other, Element):
            return NotImplemented
        return (
            self.symbol == other.symbol
            and self.atomic_number == other.atomic_number
            and float(self.atomic_mass) == float(other.atomic_mass)
        )
