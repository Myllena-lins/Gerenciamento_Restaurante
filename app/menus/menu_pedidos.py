from app.services.pedidos_service import (
    listar_pedidos,
    buscar_pedido_por_id,
    buscar_pedido_por_mesa,
    criar_pedido,
    adicionar_prato_ao_pedido,
)
from app.utils.inputs import ler_int, ler_texto
from app.utils.formatadores import formatar_pedido
from app.exceptions import (
    PedidoNaoEncontrado,
    PratoNaoEncontrado,
)


def menu_pedidos():
    while True:
        print("\n--- Gerenciamento de Pedidos ---")
        opcao = ler_int(
            "1 - Listar pedidos\n"
            "2 - Criar pedido\n"
            "3 - Buscar pedido por ID\n"
            "4 - Buscar pedido por mesa\n"
            "5 - Voltar\n\n"
            "Escolha: "
        )

        if opcao == 1:
            pedidos = listar_pedidos()

            if not pedidos:
                print("\nNenhum pedido encontrado.")
            else:
                for pedido_id, pedido in pedidos.items():
                    print(formatar_pedido(pedido_id, pedido))

        elif opcao == 2:
            numero_mesa = ler_int("Número da mesa: ")
            pratos = []

            print("\nDigite os pratos:")

            while True:
                prato_id = ler_texto("ID do prato (ou 0 para finalizar): ")

                if prato_id == "0":
                    break

                quantidade = ler_int("Quantidade: ")

                try:
                    adicionar_prato_ao_pedido(pratos, prato_id, quantidade)
                    print("\nPrato adicionado!")
                except PratoNaoEncontrado as e:
                    print(f"\nErro: {e}")

            if not pratos:
                print("\nPedido vazio. Cancelado.")
                continue

            observacoes = input("Observações (opcional): ").strip()

            try:
                pedido_id = criar_pedido(numero_mesa, pratos, observacoes)
                print(f"\nPedido criado com sucesso! ID: {pedido_id}")
            except ValueError as e:
                print(f"\nErro: {e}")

        elif opcao == 3:
            pedido_id = ler_texto("Digite o ID do pedido: ")

            try:
                pedido = buscar_pedido_por_id(pedido_id)
                print(formatar_pedido(pedido_id, pedido))
            except PedidoNaoEncontrado as e:
                print(f"\nErro: {e}")

        elif opcao == 4:
            numero_mesa = ler_int("Número da mesa: ")

            try:
                pedidos = buscar_pedido_por_mesa(numero_mesa)

                for pedido_id, pedido in pedidos:
                    print(formatar_pedido(pedido_id, pedido))

            except PedidoNaoEncontrado as e:
                print(f"\nErro: {e}")

        elif opcao == 5:
            break

        else:
            print("\nOpção inválida. Escolha entre 1 à 5.")