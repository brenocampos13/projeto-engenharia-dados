SELECT
    id_origem,
    UPPER(origem) AS origem
FROM {{ source('raw', 'origens') }}