from dataclasses import dataclass, asdict


@dataclass
class Prato:
    nome: str
    descricao: str
    preco: float
    tipo: str

    def to_dict(self):
        return asdict(self)