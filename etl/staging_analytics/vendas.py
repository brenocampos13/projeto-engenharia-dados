from config import get_connect_dw

def extract_vendas():

    conn = get_connect_dw()

    cursor = conn.cursor()

    cursor.execute(
        """
            TRUNCATE TABLE
                analytics.vendas
        """
    )

    cursor.execute(
        """
            SELECT
                id_venda,
                id_clinica,
                id_cliente,
                id_produto,
                quantidade,
                valor_pago,
                data_venda,
                EXTRACT(YEAR FROM data_venda) AS ano_venda,
                EXTRACT(MONTH FROM data_venda) AS mes_venda
            FROM
                staging.vendas
        """
    )

    vendas = cursor.fetchall()

    cursor.close()

    conn.close()

    return vendas

def load_vendas(vendas):

    conn = get_connect_dw()

    cursor = conn.cursor()

    for linhas in vendas:
        cursor.execute(
            """
                INSERT INTO analytics.vendas(
                    id_venda,
                    id_clinica,
                    id_cliente,
                    id_produto,
                    quantidade,
                    valor_pago,
                    data_venda,
                    ano_venda,
                    mes_venda
                ) VALUES (
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
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

def pipeline_staging_analytics_vendas():

    vendas = extract_vendas()

    load_vendas(vendas)