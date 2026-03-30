def formatar_moeda(valor):
    return f"R$ {valor:.2f}"


def formatar_prato(prato_id, prato):
    return (
        "\n----------------------------------------\n"
        f"ID: {prato_id}\n"
        f"Nome: {prato['nome']}\n"
        f"Descrição: {prato['descricao']}\n"
        f"Preço: {formatar_moeda(prato['preco'])}\n"
        f"Tipo: {prato['tipo']}\n"
        "----------------------------------------"
    )

def formatar_reserva(reserva_id, reserva):
    return (
        f"ID: {reserva_id} | "
        f"Cliente: {reserva['nome_cliente']} | "
        f"Mesa: {reserva['numero_mesa']} | "
        f"Data: {reserva['data']} | "
        f"Hora: {reserva['hora']}"
    )


def formatar_pedido(pedido_id, pedido):
    texto = (
        f"ID do Pedido: {pedido_id}\n"
        f"Mesa: {pedido['numero_mesa']}\n"
        "\n--- Itens ---\n"
    )

    for item in pedido["pratos"]:
        texto += (
            f"{item['nome']} | "
            f"Qtd: {item['quantidade']} | "
            f"Unitário: R$ {item['preco_unitario']:.2f} | "
            f"Total: R$ {item['preco_total']:.2f}\n"
        )

    texto += f"\nTOTAL DO PEDIDO: R$ {pedido['total']:.2f}\n"
    texto += "----------------------------------------"

    return texto