import psycopg2
from dotenv import load_dotenv
from config import get_connect_dw
import os

load_dotenv("variaveis.env")

def extract_origens():

    conn = get_connect_dw()

    cursor = conn.cursor()

    cursor.execute(
        """
            SELECT
                id_origem,
                UPPER(origem) AS origem
            FROM
                raw.origens
        """
    )

    origens = cursor.fetchall()

    cursor.close()

    conn.close()

    return origens

def load_origens(origens):

    conn = get_connect_dw()

    cursor = conn.cursor()

    for dados in origens:
        cursor.execute(
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

    conn.commit()

    cursor.close()

    conn.close()

def pipeline_raw_staging_origens():

    origens = extract_origens()

    load_origens(origens)