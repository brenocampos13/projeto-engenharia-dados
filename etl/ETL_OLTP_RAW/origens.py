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
            loja_oltp.origens
    """
)

origens = cursor_oltp.fetchall()

for linhas in origens:
    print(origens)

cursor_oltp.close()

cursor_dw = conn_dw.cursor()

cursor_dw.execute(
    """
        TRUNCATE TABLE
            raw.origens
    """
)

print('Carregando...')

for dados in origens:
    cursor_dw.execute(
        """
            INSERT INTO raw.origens(
                id_origem,
                origem
            )
            VALUES (
                %s,
                %s
            )
        """, dados
    )

conn_dw.commit()

print('Carga realizada!')

cursor_dw.close()

print('Carregado com sucesso!')