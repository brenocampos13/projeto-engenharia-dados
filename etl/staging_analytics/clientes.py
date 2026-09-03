from config import get_connect_dw

def extract_clientes():

    conn = get_connect_dw()

    cursor = conn.cursor()

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

    cursor.close()

    conn.close()

    return clientes

def load_clientes(clientes):

    conn = get_connect_dw()

    cursor = conn.cursor()

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

    conn.commit()

    cursor.close()

    conn.close()

def pipeline_staging_analytics_clientes():

    clientes = extract_clientes()

    load_clientes(clientes)