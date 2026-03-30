from app.utils.inputs import ler_int, ler_texto
from app.services.cardapio_service import listar_pratos
from app.services.pedidos_service import (
    criar_pedido,
    buscar_pedido_por_id,
    buscar_pedido_por_mesa,
    adicionar_prato_ao_pedido,
)
from app.services.reservas_service import (
    buscar_reserva_por_id,
    buscar_reserva_por_nome,
)
from app.utils.formatadores import formatar_prato, formatar_pedido, formatar_reserva


def menu_cliente():
    while True:
        print("\n--- Menu do Cliente ---")
        opcao = ler_int(
            "1 - Ver cardápio\n"
            "2 - Fazer pedido\n"
            "3 - Ver pedido por ID\n"
            "4 - Ver pedido por mesa\n"
            "5 - Ver reserva por ID\n"
            "6 - Ver reserva por nome\n"
            "7 - Voltar\n\n"
            "Escolha: "
        )

        if opcao == 1:
            pratos = listar_pratos()

            if not pratos:
                print("\nCardápio vazio.")
            else:
                print("\n--- Cardápio ---")
                for prato_id, prato in pratos.items():
                    print(formatar_prato(prato_id, prato))

        elif opcao == 2:
            numero_mesa = ler_int("Número da mesa: ")
            pratos = []

            print("\nDigite os pratos que deseja:")

            while True:
                prato_id = ler_texto("ID do prato (ou 0 para finalizar): ")

                if prato_id == "0":
                    break

                quantidade = ler_int("Quantidade: ")

                resultado = adicionar_prato_ao_pedido(pratos, prato_id, quantidade)

                if resultado is None:
                    print("\nPrato não encontrado.")
                else:
                    print("\nPrato adicionado!")

            if not pratos:
                print("\nPedido vazio. Cancelado.")
                continue

            observacoes = input("Observações (opcional): ").strip()

            pedido_id = criar_pedido(numero_mesa, pratos, observacoes)
            print(f"\nPedido realizado com sucesso! ID: {pedido_id}")

        elif opcao == 3:
            pedido_id = ler_texto("Digite o ID do pedido: ")
            pedido = buscar_pedido_por_id(pedido_id)

            if pedido:
                print(formatar_pedido(pedido_id, pedido))
            else:
                print("\nPedido não encontrado.")

        elif opcao == 4:
            numero_mesa = ler_int("Número da mesa: ")
            pedidos = buscar_pedido_por_mesa(numero_mesa)

            if pedidos:
                for pedido_id, pedido in pedidos:
                    print(formatar_pedido(pedido_id, pedido))
            else:
                print("\nNenhum pedido encontrado para essa mesa.")

        elif opcao == 5:
            reserva_id = ler_texto("Digite o ID da reserva: ")
            reserva = buscar_reserva_por_id(reserva_id)

            if reserva:
                print(formatar_reserva(reserva_id, reserva))
            else:
                print("\nReserva não encontrada.")

        elif opcao == 6:
            nome = ler_texto("Digite o nome do cliente: ")
            reservas = buscar_reserva_por_nome(nome)

            if reservas:
                for reserva_id, reserva in reservas:
                    print(formatar_reserva(reserva_id, reserva))
            else:
                print("\nNenhuma reserva encontrada.")

        elif opcao == 7:
            break

        else:
            print("\nOpção inválida. Escolha entre 1 à 7.")