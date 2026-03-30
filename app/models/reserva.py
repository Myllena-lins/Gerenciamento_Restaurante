from dataclasses import dataclass, asdict


@dataclass
class Reserva:
    numero_mesa: int
    nome_cliente: str
    data: str
    hora: str
    numero_pessoas: int

    def to_dict(self):
        return asdict(self)