import psycopg2
from dotenv import load_dotenv
from config import get_connect_dw
import os

load_dotenv("variaveis.env")

def extract_vendas():

    conn = get_connect_dw()

    cursor = conn.cursor()

    cursor.execute(
        """
            SELECT
                id_venda,
                id_clinica,
                id_cliente,
                id_produto,
                quantidade,
                valor_pago,
                data_venda
            FROM
                raw.vendas
        """
    )

    vendas = cursor.fetchall()

    return vendas

def load_vendas(vendas):

    conn = get_connect_dw()

    cursor = conn.cursor()

    for dados in vendas:
        cursor.execute(
            """
                INSERT INTO staging.vendas(
                id_venda,
                id_clinica,
                id_cliente,
                id_produto,
                quantidade,
                valor_pago,
                data_venda
                ) VALUES (
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

    cursor.close()

    conn.close()

def pipeline_raw_staging_vendas():

    vendas = extract_vendas()

    load_vendas(vendas)