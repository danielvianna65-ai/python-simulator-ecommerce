import random
from src.db import get_connection
from src.data_generators import (
    escolher_forma_pagamento,
    decidir_status_final,
    gerar_quantidade
)

def criar_pedido():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    try:
        # =========================
        # Cliente e endereço
        # =========================
        cursor.execute("SELECT id_cliente FROM clientes ORDER BY RAND() LIMIT 1")
        id_cliente = cursor.fetchone()["id_cliente"]

        cursor.execute("""
            SELECT id_endereco
            FROM enderecos
            WHERE id_cliente = %s
            ORDER BY RAND()
            LIMIT 1
        """, (id_cliente,))
        id_endereco = cursor.fetchone()["id_endereco"]

        # =========================
        # Quantidade de produtos diferentes
        # =========================
        qtd_produtos = random.randint(1, 5)

        # =========================
        # Buscar produtos distintos com estoque
        # =========================
        cursor.execute("""
            SELECT p.id_produto, p.preco, e.quantidade_disponivel
            FROM produtos p
            JOIN estoque e ON p.id_produto = e.id_produto
            WHERE e.quantidade_disponivel > 0
            ORDER BY RAND()
            LIMIT %s
        """, (qtd_produtos,))
        produtos = cursor.fetchall()

        if len(produtos) < qtd_produtos:
            raise Exception("Quantidade insuficiente de produtos com estoque")

        # =========================
        # Criar pedido (valor será atualizado)
        # =========================
        cursor.execute("""
            INSERT INTO pedidos (id_cliente, id_endereco, status_pedido, valor_total)
            VALUES (%s, %s, 'CRIADO', 0)
        """, (id_cliente, id_endereco))

        id_pedido = cursor.lastrowid

        # =========================
        # Inserir itens do pedido
        # =========================
        valor_total = 0

        for produto in produtos:
            quantidade = gerar_quantidade()

            if produto["quantidade_disponivel"] < quantidade:
                raise Exception(
                    f"Estoque insuficiente para produto {produto['id_produto']}"
                )

            subtotal = quantidade * produto["preco"]
            valor_total += subtotal

            cursor.execute("""
                INSERT INTO itens_pedido (
                    id_pedido,
                    id_produto,
                    quantidade,
                    preco_unitario
                )
                VALUES (%s, %s, %s, %s)
            """, (
                id_pedido,
                produto["id_produto"],
                quantidade,
                produto["preco"]
            ))

        # =========================
        # Atualizar valor total
        # =========================
        cursor.execute("""
            UPDATE pedidos
            SET valor_total = %s
            WHERE id_pedido = %s
        """, (valor_total, id_pedido))

        # =========================
        # Pagamento
        # =========================
        forma = escolher_forma_pagamento()
        status_final = decidir_status_final(forma)

        mapping = {
            "PAGO": "CONFIRMADO",
            "EM_PROCESSAMENTO": "PENDENTE",
            "CANCELADO": "CANCELADO"
        }

        if status_final not in mapping:
            raise ValueError(f"Status inesperado: {status_final}")

        status = mapping[status_final]

        cursor.execute("""
                       INSERT INTO pagamentos (id_pedido,
                                               forma_pagamento,
                                               status_pagamento,
                                               data_pagamento,
                                               valor_pago)
                       VALUES (%s, %s, %s, NOW(), %s)
                       """, (
                           id_pedido,
                           forma,
                           status,
                           valor_total
                       ))

        # =========================
        # Status final (TRIGGERS)
        # =========================
        cursor.execute("""
            UPDATE pedidos
            SET status_pedido = %s
            WHERE id_pedido = %s
        """, (status_final, id_pedido))

        conn.commit()
        print(
            f"Pedido {id_pedido} criado com "
            f"{qtd_produtos} produtos diferentes → {status_final} "
            f"valor total R$:{valor_total}"
        )

    except Exception as e:
        conn.rollback()
        print("Erro:", e)

    finally:
        cursor.close()
        conn.close()
