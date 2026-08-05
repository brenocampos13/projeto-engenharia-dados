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

conn_oltp = psycopg2.connect(
    host=os.getenv("host"),
    port=os.getenv("port"),
    database=os.getenv("database"),
    user=os.getenv("user"),
    password=os.getenv("password")
)

cursor1 = conn_oltp.cursor()

cursor1.execute(
    """
        SELECT
            *
        FROM
            loja_oltp.clientes
    """
)

clientes = cursor1.fetchall()

for dados in clientes:
    print(dados)

cursor1.close()

cursor2 = conn_dw.cursor()

cursor2.execute(
    """
        TRUNCATE TABLE raw.clientes
    """
)

for dados in clientes:
    cursor2.execute(
        """
            INSERT INTO raw.clientes(
                id_cliente,
                id_clinica,
                nome_cliente,
                data_nasc,
                cpf,
                genero,
                profissao,
                telefone,
                origemid
            )
            VALUES (
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
        """, dados
    )

conn_dw.commit()

cursor2.execute(
    """
        SELECT
            *
        FROM
            raw.clientes
    """
)

xdx = cursor2.fetchall()

for linhas in xdx:
    print(linhas)

cursor2.close()