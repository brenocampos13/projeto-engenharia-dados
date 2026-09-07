from config import get_connect_dw

def extract_vendas():
    conn = get_connect_dw()

    cursor = conn.cursor()

    cursor.execute(
        """
            SELECT
                *
            FROM
                loja_oltp.vendas
        """
    )

    vendas = cursor.fetchall()

    cursor.close()

    conn.close()

    return vendas

def load_vendas(vendas):
    conn = get_connect_dw()

    cursor = conn.cursor()

    cursor.execute(
        """
            TRUNCATE TABLE
                raw.vendas
        """
    )

    for dados in vendas:
        cursor.execute(
            """
                INSERT INTO raw.vendas(
                    id_venda,
                    id_clinica,
                    id_cliente,
                    id_produto,
                    quantidade,
                    valor_pago,
                    data_venda,
                    data_carga
                )
                VALUES (
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s
                )
            """, dados
        )

    conn.commit()

    print('Carga realizada!')

    cursor.close()

    conn.close()

def pipeline_oltp_raw_vendas():
    vendas = extract_vendas()

    load_vendas(vendas)