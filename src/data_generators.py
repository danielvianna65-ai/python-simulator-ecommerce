import random
from datetime import datetime

FORMAS_PAGAMENTO = ["PIX", "CARTAO_CREDITO", "BOLETO"]

def escolher_forma_pagamento():
    """
    Seleciona aleatoriamente uma forma de pagamento com pesos definidos.

    Probabilidades:
    - PIX: 50%
    - CARTAO_CREDITO: 35%
    - BOLETO: 15%

    Returns:
        str: Forma de pagamento selecionada.
    """
    return random.choices(
        FORMAS_PAGAMENTO,
        weights=[0.5, 0.35, 0.15]
    )[0]


def gerar_quantidade():
    """
    Gera a quantidade de itens de um pedido, variando de 1 a 5 unidades,
    com maior probabilidade para quantidades menores.

    Distribuição de probabilidade aproximada:
    1 unidade → 45%
    2 unidades → 25%
    3 unidades → 15%
    4 unidades → 10%
    5 unidades → 5%

    Returns:
        int: Quantidade de itens do pedido.
    """
    return random.choices(
        population=[1, 2, 3, 4, 5],
        weights=[45, 25, 15, 10, 5]
    )[0]


def decidir_status_final(forma):
    """
    Define o status final do pedido com base na forma de pagamento.

    Regras:
    - BOLETO:
        - PAGO: 60%
        - EM_PROCESSAMENTO: 40%
    - PIX e CARTAO_CREDITO:
        - PAGO: 90%
        - CANCELADO: 10%

    Args:
        forma (str): Forma de pagamento do pedido.

    Returns:
        str: Status final do pedido.
    """
    if forma == "BOLETO":
        return random.choices(
            ["PAGO", "EM_PROCESSAMENTO"],
            [0.6, 0.4]
        )[0]

    return random.choices(
        ["PAGO", "CANCELADO"],
        [0.9, 0.1]
    )[0]
