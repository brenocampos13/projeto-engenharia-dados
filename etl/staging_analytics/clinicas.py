from config import get_connect_dw


def extract_clinicas():
    conn = get_connect_dw()

    cursor = conn.cursor()

    cursor.execute(
        """
            TRUNCATE TABLE
                analytics.clinicas
        """
    )

    cursor.execute(
        """
            SELECT
                id_clinica,
                clinica,
                cnpj
            FROM
                staging.clinicas
        """
    )

    clinicas = cursor.fetchall()

    cursor.close()

    conn.close()

    return clinicas

def load_clinicas(clinicas):

    conn = get_connect_dw()

    cursor = conn.cursor()

    for linhas in clinicas:
        cursor.execute(
            """
                INSERT INTO analytics.clinicas(
                    id_clinica,
                    clinica,
                    cnpj
                ) VALUES (
                    %s,
                    %s,
                    %s
                )
            """, linhas
        )

    conn.commit()

    cursor.close()

    conn.close()

def pipeline_staging_analytics_clinicas():

    clinicas = extract_clinicas()

    load_clinicas(clinicas)