SELECT
    id_produto,
    UPPER(nome_produto) AS nome_produto,
    UPPER(marca) AS marca,
    valor
FROM {{ source('raw', 'produtos') }}