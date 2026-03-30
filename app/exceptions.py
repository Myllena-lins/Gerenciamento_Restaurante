class PratoNaoEncontrado(Exception):
    def __init__(self, mensagem="Prato não encontrado."):
        super().__init__(mensagem)


class PratoJaExiste(Exception):
    def __init__(self, mensagem="Prato já existe no cardápio."):
        super().__init__(mensagem)
        
class ReservaNaoEncontrada(Exception):
    def __init__(self, mensagem="Reserva não encontrada."):
        super().__init__(mensagem)

class PedidoNaoEncontrado(Exception):
    def __init__(self, mensagem="Pedido não encontrado."):
        super().__init__(mensagem)