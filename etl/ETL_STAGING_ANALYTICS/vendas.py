import psycopg2
from dotenv import load_dotenv
import os

load_dotenv("variaveis.env")

conn_dw = psycopg2.connect(
    host=os.getenv("host"),
    port=os.getenv("port"),
    database=os.getenv("database2"),
    user=os.getenv("user"),
    password=os.getenv("password")
)

cursor = conn_dw.cursor()

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

clientes = cursor.fetchall()

for linhas in clientes:
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

conn_dw.commit()

cursor.execute(
    """SELECT
            *
        FROM
            analytics.vendas
    """
)

dados = cursor.fetchall()

print(dados)