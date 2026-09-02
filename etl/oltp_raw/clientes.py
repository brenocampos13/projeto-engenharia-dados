from config import get_connect_dw, get_connect_oltp

def extract_clientes():
    conn = get_connect_oltp()
    cursor = conn.cursor()
    cursor.execute(
        """
            SELECT
                *
            FROM
                loja_oltp.clientes
        """
    )

    clientes = cursor.fetchall()

    cursor.close()
    conn.close()

    return clientes

def load_clientes(clientes):
    conn = get_connect_dw()

    cursor = conn.cursor()

    cursor.execute(
        """
            TRUNCATE TABLE raw.clientes
        """
    )

    for dados in clientes:
        cursor.execute(
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

    conn.commit()
    conn.close()

def show_clientes():
    conn = get_connect_dw()

    cursor = conn.cursor()

    cursor.execute(
        """
            SELECT
                *
            FROM
                raw.clientes
            LIMIT
                1
        """
    )

    dados = cursor.fetchall()

    cursor.close()
    conn.close()

    return dados

def pipeline_oltp_raw_clientes():
    clientes = extract_clientes()

    load_clientes(clientes)

    dados = show_clientes()

    print("CLIENTES:")

    for linhas in dados:
        print(linhas)

    print("Carga efetuada com sucesso!")