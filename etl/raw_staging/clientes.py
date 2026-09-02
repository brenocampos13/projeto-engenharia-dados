import psycopg2
from dotenv import load_dotenv
from config import get_connect_dw
import os

load_dotenv("variaveis.env")

def extract_clientes():

    conn_dw = get_connect_dw()

    cursor_dw = conn_dw.cursor()

    cursor_dw.execute(
        """
            SELECT
                id_cliente,
                id_clinica,
                UPPER(nome_cliente) AS nome_cliente,
                data_nasc,
                cpf,
                UPPER(genero) AS genero,
                UPPER(profissao) AS profissao,
                telefone,
                origemid as id_origem
            FROM
                raw.clientes
        """
    )

    clientes = cursor_dw.fetchall()

    cursor_dw.close()

    conn_dw.close()

    return clientes

def load_clientes(clientes):

    conn = get_connect_dw()

    cursor_dw = conn.cursor()

    for dados in clientes:
        cursor_dw.execute(
            """
                INSERT INTO staging.clientes(
                    id_cliente,
                    id_clinica,
                    nome_cliente,
                    data_nasc,
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
                    %s
                )
            """, dados
        )

    conn.commit()
    conn.close()

def pipeline_raw_staging_clientes():

    clientes = extract_clientes()

    load_clientes(clientes)