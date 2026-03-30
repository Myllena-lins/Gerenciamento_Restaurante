from app.models.pedido import Pedido
from app.repositories.json_repository import JsonRepository
from app.exceptions import (
    PedidoNaoEncontrado,
    PratoNaoEncontrado,
)

REPOSITORIO_PEDIDOS = JsonRepository("data/pedidos.json")
REPOSITORIO_CARDAPIO = JsonRepository("data/cardapio.json")


def listar_pedidos():
    return REPOSITORIO_PEDIDOS.ler()


def buscar_pedido_por_id(pedido_id):
    dados = REPOSITORIO_PEDIDOS.ler()

    if pedido_id not in dados:
        raise PedidoNaoEncontrado("Pedido não encontrado pelo ID.")

    return dados[pedido_id]


def buscar_pedido_por_mesa(numero_mesa):
    dados = REPOSITORIO_PEDIDOS.ler()

    resultados = [
        (pedido_id, pedido)
        for pedido_id, pedido in dados.items()
        if pedido["numero_mesa"] == numero_mesa
    ]

    if not resultados:
        raise PedidoNaoEncontrado("Nenhum pedido encontrado para essa mesa.")

    return resultados


# 🔥 Função melhorada
def adicionar_prato_ao_pedido(lista_pratos, prato_id, quantidade):
    cardapio = REPOSITORIO_CARDAPIO.ler()

    if prato_id not in cardapio:
        raise PratoNaoEncontrado("Prato não encontrado no cardápio.")

    prato = cardapio[prato_id]

    preco_unitario = prato["preco"]
    preco_total = preco_unitario * quantidade

    item = {
        "id_prato": prato_id,
        "nome": prato["nome"],
        "quantidade": quantidade,
        "preco_unitario": preco_unitario,
        "preco_total": preco_total
    }

    lista_pratos.append(item)


def calcular_total(pratos):
    return sum(item["preco_total"] for item in pratos)


def criar_pedido(numero_mesa, pratos, observacoes=""):
    if not pratos:
        raise ValueError("Pedido não pode ser vazio.")

    dados = REPOSITORIO_PEDIDOS.ler()
    novo_id = REPOSITORIO_PEDIDOS.gerar_novo_id(dados)

    total = calcular_total(pratos)

    pedido = Pedido(
        numero_mesa=numero_mesa,
        pratos=pratos,
        observacoes=observacoes,
        total=total
    )

    dados[novo_id] = pedido.to_dict()
    REPOSITORIO_PEDIDOS.salvar(dados)

    return novo_id


def deletar_pedido(pedido_id):
    dados = REPOSITORIO_PEDIDOS.ler()

    if pedido_id not in dados:
        raise PedidoNaoEncontrado("Pedido não encontrado para exclusão.")

    REPOSITORIO_PEDIDOS.deletar_e_reindexar(dados, pedido_id)