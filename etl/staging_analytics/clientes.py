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
            analytics.clientes    
    """
)

cursor.execute(
    """
        SELECT
            id_cliente,
            id_clinica,
            nome_cliente,
            data_nasc,
            EXTRACT(YEAR FROM AGE(NOW(), data_nasc)) AS idade,
            cpf,
            genero,
            profissao,
            telefone,
            id_origem
        FROM
            staging.clientes
    """
)

clientes = cursor.fetchall()

for linhas in clientes:
    cursor.execute(
        """
            INSERT INTO analytics.clientes(
                id_cliente,
                id_clinica,
                nome_cliente,
                data_nasc,
                idade,
                cpf,
                genero,
                profissao,
                telefone,
                id_origem
            ) VALUES (
                %s,
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
            analytics.clientes
    """
)

dados = cursor.fetchall()

print(dados)