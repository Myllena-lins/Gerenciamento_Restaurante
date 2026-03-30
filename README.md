# 🍽️ Sistema de Gerenciamento de Restaurante

## 📌 Descrição
Sistema desenvolvido em Python para gerenciamento de cardápio, reservas e pedidos, com interface via terminal (CLI).

## 🚀 Funcionalidades
- Gerenciamento de cardápio (CRUD)
- Gerenciamento de reservas (CRUD)
- Gerenciamento de pedidos (com cálculo automático)
- Consulta de pedidos e reservas
- Interface para cliente e funcionário

## 🧱 Arquitetura do Projeto
O projeto segue uma arquitetura modular:

- `menus/` → interface do usuário
- `services/` → regras de negócio
- `repositories/` → acesso a dados (JSON)
- `models/` → entidades
- `utils/` → funções auxiliares
- `data/` → armazenamento

## 🛠️ Tecnologias utilizadas
- Python 3
- JSON (persistência de dados)

## ▶️ Como executar

```bash
python3 -m app.main
```