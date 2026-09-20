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
FROM {{ ref('stg_clientes') }}