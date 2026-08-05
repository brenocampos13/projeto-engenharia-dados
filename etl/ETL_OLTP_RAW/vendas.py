import psycopg2
from dotenv import load_dotenv
import os

load_dotenv("variaveis.env")

conn_oltp = psycopg2.connect(
    host=os.getenv("host"),
    port=os.getenv("port"),
    database=os.getenv("database"),
    user=os.getenv("user"),
    password=os.getenv("password")
)

conn_dw = psycopg2.connect(
    host=os.getenv("host"),
    port=os.getenv("port"),
    database=os.getenv("database2"),
    user=os.getenv("user"),
    password=os.getenv("password")
)

cursor_oltp = conn_oltp.cursor()

cursor_oltp.execute(
    """
        SELECT
            *
        FROM
            loja_oltp.vendas
    """
)

vendas = cursor_oltp.fetchall()

cursor_oltp.close()

cursor_dw = conn_dw.cursor()

cursor_dw.execute(
    """
        TRUNCATE TABLE
            raw.vendas
    """
)

print('Carregando...')

for dados in vendas:
    cursor_dw.execute(
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

conn_dw.commit()

print('Carga realizada!')

cursor_dw.close()