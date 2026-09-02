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

cursor_dw = conn_dw.cursor()

cursor_dw.execute(
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

vendas = cursor_dw.fetchall()

print('Consulta realizada, mostrando dados retornados:')

for dados in vendas:
    print(dados)

print('Iniciando carga...')

for dados in vendas:
    cursor_dw.execute(
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

conn_dw.commit()

print('Carga efetuada com sucesso!')