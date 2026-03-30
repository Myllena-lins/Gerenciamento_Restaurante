from app.utils.inputs import ler_int
from app.menus.menu_cliente import menu_cliente
from app.menus.menu_funcionario import menu_funcionario


def menu_principal():
    while True:
        print("\n***** Bem-vindos ao Restaurante Maracujênios! *****\n")
        opcao = ler_int("Você deseja entrar como:\n1 - Cliente\n2 - Funcionário\n3 - Sair\n\nEscolha: ")

        if opcao == 1:
            menu_cliente()
        elif opcao == 2:
            menu_funcionario()
        elif opcao == 3:
            print("\nObrigada. Até a próxima!")
            break
        else:
            print("\nOpção inválida. Escolha entre 1 à 3.")