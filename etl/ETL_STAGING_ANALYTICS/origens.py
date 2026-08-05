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
            analytics.origens
    """
)

cursor.execute(
    """
        SELECT
            id_origem,
            origem
        FROM
            staging.origens
    """
)

clientes = cursor.fetchall()

for linhas in clientes:
    cursor.execute(
        """
            INSERT INTO analytics.origens(
                id_origem,
                origem
            ) VALUES (
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
            analytics.origens
    """
)

dados = cursor.fetchall()

print(dados)