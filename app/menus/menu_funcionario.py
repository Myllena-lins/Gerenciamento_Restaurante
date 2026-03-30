from app.utils.inputs import ler_int
from app.menus.menu_cardapio import menu_cardapio
from app.menus.menu_reserva import menu_reservas
from app.menus.menu_pedidos import menu_pedidos


def menu_funcionario():
    while True:
        print("\n--- Menu do Funcionário ---")
        opcao = ler_int(
            "1 - Gerenciar cardápio\n"
            "2 - Gerenciar reservas\n"
            "3 - Gerenciar pedidos\n"
            "4 - Voltar\n\n"
            "Escolha: "
        )

        if opcao == 1:
            menu_cardapio()
        elif opcao == 2:
            menu_reservas()
        elif opcao == 3:
            menu_pedidos()
        elif opcao == 4:
            break
        else:
            print("\nOpção inválida. Escolha entre 1 à 4.")