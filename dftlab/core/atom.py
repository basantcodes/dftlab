from __future__ import annotations

from dftlab.core.element import Element
"""Atom class for managing elements at certain distances."""


class Atom:
    """
    Represent an atom with elements at specified distances.
    
    This class stores atomic information and manages the positions of elements
    relative to a central atom at certain distances.
    """
    
    def __init__(self, symbol: str, element:Element, position: list = None):
        """
        Initialize an Atom.
        
        Args:
            symbol (str): Chemical symbol of the atom (e.g., 'C', 'H', 'O').
            position (list, optional): Cartesian coordinates [x, y, z]. Defaults to None.
        """
        self.symbol = symbol
        self.element = element
        self.position = position or [0.0, 0.0, 0.0]
        self.neighbors = []
    
    def add_neighbor(self, neighbor: 'Atom', distance: float):
        """
        Add a neighboring atom at a specified distance.
        
        Args:
            neighbor (Atom): The neighboring atom to add.
            distance (float): Distance to the neighbor atom.
        """
        self.neighbors.append({'atom': neighbor, 'distance': distance})
    
    def __repr__(self) -> str:
        """Return string representation of the atom."""
        return f"Atom({self.symbol}, position={self.position})"
