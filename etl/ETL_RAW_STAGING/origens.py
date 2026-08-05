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
            id_origem,
            UPPER(origem) AS origem
        FROM
            raw.origens
    """
)

origens = cursor_dw.fetchall()

print('Consulta realizada, mostrando dados retornados:')

for dados in origens:
    print(dados)

print('Iniciando carga...')

for dados in origens:
    cursor_dw.execute(
        """
            INSERT INTO staging.origens(
            id_origem,
            origem
            ) VALUES (
                %s,
                %s
            )
        """, dados
    )

conn_dw.commit()

print('Carga efetuada com sucesso!')