import psycopg2
from dotenv import load_dotenv
from config import get_connect_dw
import os


load_dotenv("variaveis.env")

def extract_clinicas():
    conn = get_connect_dw()

    cursor = conn.cursor()

    cursor.execute(
        """
            SELECT
                id_clinica,
                UPPER(clinica) AS clinica,
                cnpj
            FROM
                raw.clinicas
        """
    )

    clinicas = cursor.fetchall()

    cursor.close()

    conn.close()

    return clinicas

def load_clinicas(clinicas):

    conn = get_connect_dw()

    cursor = conn.cursor()

    for dados in clinicas:
        cursor.execute(
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

    conn.commit()

    cursor.close()

    conn.close()

def pipeline_raw_staging_clinicas():

    clinicas = extract_clinicas()

    load_clinicas(clinicas)