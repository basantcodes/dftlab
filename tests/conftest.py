"""Pytest configuration and shared fixtures."""

import pytest


@pytest.fixture
def sample_elements():
    """Provide sample element data for tests."""
    from dftlab.core.element import Element
    
    return {
        "hydrogen": Element("H", 1, 1.008),
        "carbon": Element("C", 6, 12.011),
        "oxygen": Element("O", 8, 15.999),
    }
