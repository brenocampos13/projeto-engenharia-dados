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
            id_produto,
            UPPER(nome_produto) AS nome_produto,
            UPPER(marca) AS marca,
            valor
        FROM
            raw.produtos
    """
)

produtos = cursor_dw.fetchall()

print('Consulta realizada, mostrando dados retornados:')

for dados in produtos:
    print(dados)

print('Iniciando carga...')

for dados in produtos:
    cursor_dw.execute(
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

conn_dw.commit()

print('Carga efetuada com sucesso!')