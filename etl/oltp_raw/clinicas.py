from config import get_connect_dw, get_connect_oltp

def extract_clinicas():
    conn = get_connect_oltp()
    cursor_oltp = conn.cursor()

    cursor_oltp.execute(
        """
            SELECT
                *
            FROM
                loja_oltp.clinicas
        """
    )

    clinicas = cursor_oltp.fetchall()

    cursor_oltp.close()

    return clinicas

def load_clinicas(clinicas):
    conn = get_connect_dw()
    cursor = conn.cursor()

    cursor.execute(
        """
            TRUNCATE TABLE
                raw.clinicas
        """
    )

    for dados in clinicas:
        cursor.execute(
            """
                INSERT INTO raw.clinicas(
                    id_clinica,
                    clinica,
                    cnpj
                )
                VALUES(
                    %s,
                    %s,
                    %s
                )
            """, dados
        )

    conn.commit()

    cursor.close()

def show_clinicas():
    conn = get_connect_dw()

    cursor = conn.cursor()

    cursor.execute(
        """
            SELECT
                *
            FROM
                raw.clinicas
            LIMIT
                1
        """
    )

    dados = cursor.fetchall()

    cursor.close()
    conn.close()

    return dados

def pipeline_oltp_raw_clinicas():
    clinicas = extract_clinicas()

    load_clinicas(clinicas)

    dados = show_clinicas()

    print("CLINICAS:")

    for linhas in dados:
        print(linhas)

    print("Carga efetuada com sucesso!")