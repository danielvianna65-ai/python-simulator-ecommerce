from src.db import get_connection

ESTOQUE_MINIMO = 20
QTDE_REPOSICAO = 500

def repor_estoque_se_necessario():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    try:
        # Buscar produtos com estoque baixo
        cursor.execute("""
            SELECT id_produto, quantidade_disponivel
            FROM estoque
            WHERE quantidade_disponivel < %s
            FOR UPDATE
        """, (ESTOQUE_MINIMO,))

        produtos = cursor.fetchall()

        for p in produtos:
            cursor.execute("""
                UPDATE estoque
                SET quantidade_disponivel = quantidade_disponivel + %s
                WHERE id_produto = %s
            """, (QTDE_REPOSICAO, p["id_produto"]))

            print(
                f"[REPOSIÇÃO] Produto {p['id_produto']} "
                f"estoque {p['quantidade_disponivel']} → "
                f"{p['quantidade_disponivel'] + QTDE_REPOSICAO}"
            )

        conn.commit()

    except Exception as e:
        conn.rollback()
        print("Erro na reposição:", e)

    finally:
        cursor.close()
        conn.close()
