def validar_preco(preco):
    return preco > 0


def validar_quantidade(valor):
    return valor > 0


def validar_texto_obrigatorio(texto):
    return bool(texto and texto.strip())