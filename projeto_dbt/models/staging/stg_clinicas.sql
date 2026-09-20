SELECT
    id_clinica,
    UPPER(clinica) AS clinica,
    cnpj
FROM {{ source('raw', 'clinicas') }}