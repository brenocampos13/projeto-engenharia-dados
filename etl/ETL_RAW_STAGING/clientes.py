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

print('Consulta realizada, mostrando dados retornados:')

for dados in clientes:
    print(dados)

print('Iniciando carga...')

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

conn_dw.commit()

print('Carga efetuada com sucesso!')