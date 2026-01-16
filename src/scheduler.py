import time
from src.order_flow import criar_pedido
from src.restock import repor_estoque_se_necessario

def rodar_simulacao(pedidos_por_minuto=5):
    intervalo = 60 / pedidos_por_minuto
    contador = 0

    while True:
        criar_pedido()
        contador += 1

        # A cada 10 pedidos, verifica reposição
        if contador % 10 == 0:
            repor_estoque_se_necessario()

        time.sleep(intervalo)
