from config import get_connect_dw

def extract_origens():

    conn = get_connect_dw()

    cursor = conn.cursor()

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

    origens = cursor.fetchall()

    cursor.close()

    conn.close()
    
    return origens

def load_origens(origens):

    conn = get_connect_dw()

    cursor = conn.cursor()

    for linhas in origens:
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

    conn.commit()

    cursor.close()

    conn.close()

def pipeline_staging_analytics_origens():

    origens = extract_origens()

    load_origens(origens)