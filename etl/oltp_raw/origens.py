import psycopg2
from dotenv import load_dotenv
from config import get_connect_dw, get_connect_oltp
import os

load_dotenv("variaveis.env")

def extract_origens():
    conn = get_connect_oltp()

    cursor = conn.cursor()

    cursor.execute(
        """
            SELECT
                *
            FROM
                loja_oltp.origens
        """
    )

    origens = cursor.fetchall()

    cursor.close()

    return origens

def load_origens(origens):
    conn = get_connect_dw()

    cursor = conn.cursor()

    cursor.execute(
        """
            TRUNCATE TABLE
                raw.origens
        """
    )

    for dados in origens:
        cursor.execute(
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

    conn.commit()

    cursor.close()

def pipeline_oltp_raw_origens():
    origens = extract_origens()

    load_origens(origens)