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
            loja_oltp.clinicas
    """
)

clinicas = cursor_oltp.fetchall()

for linha in clinicas:
    print(linha)

cursor_oltp.close()

print('Carregando...')

cursor_dw = conn_dw.cursor()

cursor_dw.execute(
    """
        TRUNCATE TABLE
            raw.clinicas
    """
)

for dados in clinicas:
    cursor_dw.execute(
        """
            INSERT INTO raw.clinicas(
                id_clinica,
                clinica,
                cnpj
            )
            VALUES(
                %s,
                %s,
                %s
            )
        """, dados
    )

conn_dw.commit()

cursor_dw.close()

print('Carregado com sucesso.')