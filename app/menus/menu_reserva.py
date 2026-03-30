from app.services.reservas_service import (
    listar_reservas,
    criar_reserva,
    buscar_reserva_por_id,
    buscar_reserva_por_nome,
    atualizar_reserva,
    deletar_reserva,
)
from app.utils.inputs import ler_int, ler_texto
from app.utils.formatadores import formatar_reserva
from app.exceptions import ReservaNaoEncontrada


def menu_reservas():
    while True:
        print("\n--- Gerenciamento de Reservas ---")
        opcao = ler_int(
            "1 - Listar reservas\n"
            "2 - Criar reserva\n"
            "3 - Buscar reserva por ID\n"
            "4 - Buscar reserva por nome\n"
            "5 - Atualizar reserva\n"
            "6 - Deletar reserva\n"
            "7 - Voltar\n\n"
            "Escolha: "
        )

        if opcao == 1:
            reservas = listar_reservas()

            if not reservas:
                print("\nNenhuma reserva cadastrada.")
            else:
                print("\n--- Reservas ---")
                for reserva_id, reserva in reservas.items():
                    print(formatar_reserva(reserva_id, reserva))

        elif opcao == 2:
            numero_mesa = ler_int("Número da mesa: ")
            nome_cliente = ler_texto("Nome do cliente: ")
            data = ler_texto("Data (dd/mm/aaaa): ")
            hora = ler_texto("Hora: ")
            numero_pessoas = ler_int("Número de pessoas: ")

            reserva_id = criar_reserva(
                numero_mesa,
                nome_cliente,
                data,
                hora,
                numero_pessoas
            )

            print(f"\nReserva criada com sucesso! ID: {reserva_id}")

        elif opcao == 3:
            reserva_id = ler_texto("Digite o ID da reserva: ")

            try:
                reserva = buscar_reserva_por_id(reserva_id)
                print(formatar_reserva(reserva_id, reserva))
            except ReservaNaoEncontrada as e:
                print(f"\nErro: {e}")

        elif opcao == 4:
            nome = ler_texto("Digite o nome do cliente: ")

            try:
                reservas = buscar_reserva_por_nome(nome)

                for reserva_id, reserva in reservas:
                    print(formatar_reserva(reserva_id, reserva))

            except ReservaNaoEncontrada as e:
                print(f"\nErro: {e}")

        elif opcao == 5:
            reserva_id = ler_texto("Digite o ID da reserva: ")

            try:
                print("\nDeixe em branco para não alterar.")

                numero_mesa_input = input("Novo número da mesa: ").strip()
                nome_cliente = input("Novo nome do cliente: ").strip()
                data = input("Nova data: ").strip()
                hora = input("Nova hora: ").strip()
                numero_pessoas_input = input("Novo número de pessoas: ").strip()

                numero_mesa = None
                numero_pessoas = None

                if numero_mesa_input:
                    try:
                        numero_mesa = int(numero_mesa_input)
                    except ValueError:
                        print("\nNúmero da mesa inválido.")
                        continue

                if numero_pessoas_input:
                    try:
                        numero_pessoas = int(numero_pessoas_input)
                    except ValueError:
                        print("\nNúmero de pessoas inválido.")
                        continue

                atualizar_reserva(
                    reserva_id,
                    numero_mesa=numero_mesa,
                    nome_cliente=nome_cliente or None,
                    data=data or None,
                    hora=hora or None,
                    numero_pessoas=numero_pessoas
                )

                print("\nReserva atualizada com sucesso!")

            except ReservaNaoEncontrada as e:
                print(f"\nErro: {e}")

        elif opcao == 6:
            reserva_id = ler_texto("Digite o ID da reserva: ")

            try:
                deletar_reserva(reserva_id)
                print("\nReserva deletada com sucesso!")
            except ReservaNaoEncontrada as e:
                print(f"\nErro: {e}")

        elif opcao == 7:
            break

        else:
            print("\nOpção inválida. Escolha entre 1 à 7.")