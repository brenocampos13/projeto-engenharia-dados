from config import get_connect_dw

def extract_produtos():

    conn = get_connect_dw()

    cursor = conn.cursor()

    cursor.execute(
        """
            TRUNCATE TABLE
                analytics.produtos
        """
    )

    cursor.execute(
        """
            SELECT
                id_produto,
                nome_produto,
                marca,
                valor
            FROM
                staging.produtos
        """
    )

    produtos = cursor.fetchall()

    cursor.close()

    conn.close()
    
    return produtos

def load_produtos(produtos):

    conn = get_connect_dw()

    cursor = conn.cursor()

    for linhas in produtos:
        cursor.execute(
            """
                INSERT INTO analytics.produtos(
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
            """, linhas
        )

    conn.commit()

    cursor.close()

    conn.close()

def pipeline_staging_analytics_produtos():

    produtos = extract_produtos()

    load_produtos(produtos)