from app.services.cardapio_service import (
    listar_pratos,
    criar_prato,
    buscar_prato_por_id,
    buscar_prato_por_nome,
    atualizar_prato,
    deletar_prato,
)
from app.utils.inputs import ler_int, ler_float, ler_texto
from app.utils.formatadores import formatar_prato
from app.exceptions import PratoNaoEncontrado


def menu_cardapio():
    while True:
        print("\n--- Gerenciamento de Cardápio ---")
        opcao = ler_int(
            "1 - Listar pratos\n"
            "2 - Adicionar prato\n"
            "3 - Buscar prato por ID\n"
            "4 - Buscar prato por nome\n"
            "5 - Atualizar prato\n"
            "6 - Deletar prato\n"
            "7 - Voltar\n\n"
            "Escolha: "
        )

        if opcao == 1:
            pratos = listar_pratos()

            if not pratos:
                print("\nNenhum prato cadastrado.")
            else:
                print("\n--- Cardápio ---")
                for prato_id, prato in pratos.items():
                    print(formatar_prato(prato_id, prato))

        elif opcao == 2:
            nome = ler_texto("Nome do prato: ")
            descricao = ler_texto("Descrição: ")
            preco = ler_float("Preço: ")
            tipo = ler_texto("Tipo do prato: ")

            prato_id = criar_prato(nome, descricao, preco, tipo)
            print(f"\nPrato cadastrado com sucesso! ID: {prato_id}")

        elif opcao == 3:
            prato_id = ler_texto("Digite o ID do prato: ")

            try:
                prato = buscar_prato_por_id(prato_id)
                print("\nPrato encontrado:")
                print(formatar_prato(prato_id, prato))
            except PratoNaoEncontrado as e:
                print(f"\nErro: {e}")

        elif opcao == 4:
            nome = ler_texto("Digite o nome do prato: ")

            try:
                pratos = buscar_prato_por_nome(nome)

                print("\nPratos encontrados:")
                for prato_id, prato in pratos:
                    print(formatar_prato(prato_id, prato))

            except PratoNaoEncontrado as e:
                print(f"\nErro: {e}")

        elif opcao == 5:
            prato_id = ler_texto("Digite o ID do prato que deseja atualizar: ")

            try:
                print("\nDeixe em branco se não quiser alterar um campo.")

                nome = input("Novo nome: ").strip()
                descricao = input("Nova descrição: ").strip()
                preco_input = input("Novo preço: ").strip()
                tipo = input("Novo tipo: ").strip()

                preco = None
                if preco_input:
                    try:
                        preco = float(preco_input.replace(",", "."))
                    except ValueError:
                        print("\nPreço inválido.")
                        continue

                atualizar_prato(
                    prato_id,
                    nome=nome or None,
                    descricao=descricao or None,
                    preco=preco,
                    tipo=tipo or None,
                )

                print("\nPrato atualizado com sucesso!")

            except PratoNaoEncontrado as e:
                print(f"\nErro: {e}")

        elif opcao == 6:
            prato_id = ler_texto("Digite o ID do prato que deseja deletar: ")

            try:
                deletar_prato(prato_id)
                print("\nPrato deletado com sucesso!")
            except PratoNaoEncontrado as e:
                print(f"\nErro: {e}")

        elif opcao == 7:
            break

        else:
            print("\n\nOpção inválida. Escolha entre 1 à 7.")