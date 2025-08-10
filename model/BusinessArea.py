from dataclasses import dataclass
from openpyxl.styles import PatternFill


@dataclass
class BusinessArea:
    id: str
    nome: str
    colore: str

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return self.id == other.id

    def __lt__(self, other):
        return self.id < other.id

    def __str__(self):
        return f"{self.id} - {self.nome}"

    def __repr__(self):
        return str(self)

    def colora_area(self):
        colore = PatternFill(start_color=self.colore[1:], # per rimuovere il carattere '#'
                             end_color=self.colore[1:],
                             fill_type="solid")
        return colore