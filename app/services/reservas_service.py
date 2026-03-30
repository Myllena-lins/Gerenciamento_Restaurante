from app.models.reserva import Reserva
from app.repositories.json_repository import JsonRepository
from app.exceptions import ReservaNaoEncontrada

REPOSITORIO_RESERVAS = JsonRepository("data/reservas.json")


def criar_reserva(numero_mesa, nome_cliente, data, hora, numero_pessoas):
    dados = REPOSITORIO_RESERVAS.ler()
    novo_id = REPOSITORIO_RESERVAS.gerar_novo_id(dados)

    reserva = Reserva(
        numero_mesa=numero_mesa,
        nome_cliente=nome_cliente,
        data=data,
        hora=hora,
        numero_pessoas=numero_pessoas
    )

    dados[novo_id] = reserva.to_dict()
    REPOSITORIO_RESERVAS.salvar(dados)
    return novo_id


def listar_reservas():
    return REPOSITORIO_RESERVAS.ler()


def buscar_reserva_por_id(reserva_id):
    dados = REPOSITORIO_RESERVAS.ler()

    if reserva_id not in dados:
        raise ReservaNaoEncontrada("Reserva não encontrada pelo ID.")

    return dados[reserva_id]


def buscar_reserva_por_nome(nome):
    dados = REPOSITORIO_RESERVAS.ler()

    resultados = [
        (reserva_id, reserva)
        for reserva_id, reserva in dados.items()
        if reserva["nome_cliente"].lower() == nome.lower()
    ]

    if not resultados:
        raise ReservaNaoEncontrada("Nenhuma reserva encontrada com esse nome.")

    return resultados


def atualizar_reserva(
    reserva_id,
    numero_mesa=None,
    nome_cliente=None,
    data=None,
    hora=None,
    numero_pessoas=None
):
    dados = REPOSITORIO_RESERVAS.ler()

    if reserva_id not in dados:
        raise ReservaNaoEncontrada("Reserva não encontrada para atualização.")

    if numero_mesa is not None:
        dados[reserva_id]["numero_mesa"] = numero_mesa
    if nome_cliente:
        dados[reserva_id]["nome_cliente"] = nome_cliente
    if data:
        dados[reserva_id]["data"] = data
    if hora:
        dados[reserva_id]["hora"] = hora
    if numero_pessoas is not None:
        dados[reserva_id]["numero_pessoas"] = numero_pessoas

    REPOSITORIO_RESERVAS.salvar(dados)


def deletar_reserva(reserva_id):
    dados = REPOSITORIO_RESERVAS.ler()

    if reserva_id not in dados:
        raise ReservaNaoEncontrada("Reserva não encontrada para exclusão.")

    REPOSITORIO_RESERVAS.deletar_e_reindexar(dados, reserva_id)