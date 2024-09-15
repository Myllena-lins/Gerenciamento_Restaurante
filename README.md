# Gerenciamento de Restaurante
Este é um sistema de gerenciamento de restaurante desenvolvido em Python que permite a administração de cardápios, reservas e pedidos, feito em grupo com cinco pessoas que contribuiram para o desenvolvimento do projeto, da disciplina de Fundamentos da Programação. O sistema utiliza arquivos JSON para armazenamento dos dados e fornece uma interface de linha de comando para interação com as funcionalidades.

## Funcionalidades
### Gerenciamento do Cardápio
- Adicionar Prato: Adiciona novos pratos ao cardápio com informações como nome, descrição, preço e tipo.
- Visualizar Pratos: Lista todos os pratos disponíveis no cardápio.
- Atualizar Prato: Permite alterar as informações de pratos existentes.
- Excluir Prato: Remove um prato do cardápio.
- Buscar Prato por Nome ou ID: Procura pratos no cardápio pelo nome ou ID.
### Gerenciamento de Reservas
- Criar Reserva: Adiciona novas reservas com informações como número da mesa, nome, data, hora e número de pessoas.
- Visualizar Reservas: Lista todas as reservas existentes.
- Atualizar Reserva: Permite alterar os detalhes de uma reserva existente.
- Excluir Reserva: Remove uma reserva do sistema.
- Buscar Reserva por Nome ou ID: Procura reservas pelo nome do cliente ou ID.
### Gerenciamento de Pedidos
- Criar Pedido: Adiciona novos pedidos com o número da mesa, pratos escolhidos, quantidades, observações e valor total.
- Visualizar Pedidos: Lista todos os pedidos realizados.
- Atualizar Pedido: Permite alterar os detalhes de um pedido existente.
- Excluir Pedido: Remove um pedido do sistema.
- Buscar Pedido por ID ou Mesa: Procura pedidos pelo ID ou número da mesa.

## Estrutura de Dados
- cardapio.json: Armazena informações sobre os pratos do cardápio.
- reservas.json: Armazena informações sobre as reservas feitas.
- pedidos.json: Armazena informações sobre os pedidos realizados.

## Tecnologias Utilizadas
- Python (módulos padrão: json, os)

## Observações Finais
A criação desse sistema foi uma solução simples e aplicável em qualquer sistema de gerenciamento de restaurantes. Qualquer sugestão para melhoria do mesmo será bem-vinda!
