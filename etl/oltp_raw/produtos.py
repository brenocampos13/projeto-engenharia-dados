from config import get_connect_dw

def extract_produtos():
    conn = get_connect_dw()

    cursor = conn.cursor()

    cursor.execute(
        """
            SELECT
                *
            FROM
                loja_oltp.produtos
        """
    )

    produtos = cursor.fetchall()

    cursor.close()

    return produtos

def load_produtos(produtos):
    conn = get_connect_dw()
    
    cursor = conn.cursor()

    cursor.execute(
        """
            TRUNCATE TABLE
                raw.produtos
        """
    )

    for dados in produtos:
        cursor.execute(
            """
                INSERT INTO raw.produtos(
                    id_produto,
                    nome_produto,
                    marca,
                    valor
                )
                VALUES (
                    %s,
                    %s,
                    %s,
                    %s
                )
            """, dados
        )

    conn.commit()

    cursor.close()

def pipeline_oltp_raw_produtos():
    produtos = extract_produtos()

    load_produtos(produtos)