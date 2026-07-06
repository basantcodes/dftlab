from dftlab.core.atom import Atom
class Structure:
    def __init__(self, name: str, fields: list[tuple[Atom, list]] = None):
        self.name = name
        self.fields = fields
    
    def add_atom(self, atom: Atom , position: list):
        self.fields.append((atom, position))

    def __repr__(self):
        return f"Structure(name={self.name}, fields={self.fields})"