"""Tests for dftlab.core.element module."""

import pytest
from dftlab.core.element import Element


class TestElementCreation:
    """Test Element creation and basic functionality."""
    
    def test_element_creation(self):
        """Test creating an Element instance."""
        elem = Element("C", 6, 12.011)
        assert elem.symbol == "C"
        assert elem.atomic_number == 6
        assert elem.atomic_mass == 12.011
    
    def test_element_immutability(self):
        """Test that Element instances are immutable (frozen dataclass)."""
        elem = Element("H", 1, 1.008)
        with pytest.raises(AttributeError):
            elem.symbol = "He"
    
    def test_element_equality(self):
        """Test Element equality comparison."""
        elem1 = Element("O", 8, 15.999)
        elem2 = Element("O", 8, 15.999)
        elem3 = Element("N", 7, 14.007)
        
        assert elem1 == elem2
        assert elem1 != elem3
    
    def test_element_repr(self):
        """Test Element string representation."""
        elem = Element("N", 7, 14.007)
        repr_str = repr(elem)
        assert "Element" in repr_str
        assert "N" in repr_str
        assert "7" in repr_str


class TestElementWithFixture:
    """Test Element using pytest fixtures."""
    
    def test_fixture_hydrogen(self, sample_elements):
        """Test accessing hydrogen from fixture."""
        h = sample_elements["hydrogen"]
        assert h.symbol == "H"
        assert h.atomic_number == 1
    
    def test_fixture_carbon(self, sample_elements):
        """Test accessing carbon from fixture."""
        c = sample_elements["carbon"]
        assert c.symbol == "C"
        assert c.atomic_number == 6
