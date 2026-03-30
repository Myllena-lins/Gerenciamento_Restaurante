from dataclasses import dataclass, asdict, field


@dataclass
class Pedido:
    numero_mesa: int
    pratos: list = field(default_factory=list)
    observacoes: str = ""
    total: float = 0.0

    def to_dict(self):
        return asdict(self)