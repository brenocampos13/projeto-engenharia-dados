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
            id_clinica,
            UPPER(clinica) AS clinica,
            cnpj
        FROM
            raw.clinicas
    """
)

clinicas = cursor_dw.fetchall()

print('Consulta realizada, mostrando dados retornados:')

for dados in clinicas:
    print(dados)

print('Iniciando carga...')

for dados in clinicas:
    cursor_dw.execute(
        """
            INSERT INTO staging.clinicas(
            id_clinica,
            clinica,
            cnpj
            ) VALUES (
                %s,
                %s,
                %s
            )
        """, dados
    )

conn_dw.commit()

print('Carga efetuada com sucesso!')