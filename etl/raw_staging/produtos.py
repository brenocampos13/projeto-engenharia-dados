from config import get_connect_dw

def extract_produtos():

    conn = get_connect_dw()
    
    cursor = conn.cursor()

    cursor.execute(
        """
            SELECT
                id_produto,
                UPPER(nome_produto) AS nome_produto,
                UPPER(marca) AS marca,
                valor
            FROM
                raw.produtos
        """
    )

    produtos = cursor.fetchall()

    cursor.close()

    conn.close()

    return produtos

def load_produtos(produtos):

    conn = get_connect_dw()

    cursor = conn.cursor()

    for dados in produtos:
        cursor.execute(
            """
                INSERT INTO staging.produtos(
                id_produto,
                nome_produto,
                marca,
                valor
                ) VALUES (
                    %s,
                    %s,
                    %s,
                    %s
                )
            """, dados
        )

    conn.commit()

    cursor.close()

    conn.close()

def pipeline_raw_staging_produtos():

    produtos = extract_produtos()

    load_produtos(produtos)