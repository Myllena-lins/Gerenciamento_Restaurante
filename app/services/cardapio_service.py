from app.models.prato import Prato
from app.repositories.json_repository import JsonRepository
from app.exceptions import PratoNaoEncontrado

REPOSITORIO_CARDAPIO = JsonRepository("data/cardapio.json")


def criar_prato(nome, descricao, preco, tipo):
    dados = REPOSITORIO_CARDAPIO.ler()
    novo_id = REPOSITORIO_CARDAPIO.gerar_novo_id(dados)

    prato = Prato(nome=nome, descricao=descricao, preco=preco, tipo=tipo)
    dados[novo_id] = prato.to_dict()

    REPOSITORIO_CARDAPIO.salvar(dados)
    return novo_id


def listar_pratos():
    return REPOSITORIO_CARDAPIO.ler()


def buscar_prato_por_id(prato_id):
    dados = REPOSITORIO_CARDAPIO.ler()

    if prato_id not in dados:
        raise PratoNaoEncontrado("Prato não encontrado pelo ID.")

    return dados[prato_id]


def buscar_prato_por_nome(nome):
    dados = REPOSITORIO_CARDAPIO.ler()

    resultados = [
        (prato_id, prato)
        for prato_id, prato in dados.items()
        if prato["nome"].lower() == nome.lower()
    ]

    if not resultados:
        raise PratoNaoEncontrado("Nenhum prato encontrado com esse nome.")

    return resultados


def atualizar_prato(prato_id, nome=None, descricao=None, preco=None, tipo=None):
    dados = REPOSITORIO_CARDAPIO.ler()

    if prato_id not in dados:
        raise PratoNaoEncontrado("Prato não encontrado para atualização.")

    if nome:
        dados[prato_id]["nome"] = nome
    if descricao:
        dados[prato_id]["descricao"] = descricao
    if preco is not None:
        dados[prato_id]["preco"] = preco
    if tipo:
        dados[prato_id]["tipo"] = tipo

    REPOSITORIO_CARDAPIO.salvar(dados)


def deletar_prato(prato_id):
    dados = REPOSITORIO_CARDAPIO.ler()

    if prato_id not in dados:
        raise PratoNaoEncontrado("Prato não encontrado para exclusão.")

    REPOSITORIO_CARDAPIO.deletar_e_reindexar(dados, prato_id)