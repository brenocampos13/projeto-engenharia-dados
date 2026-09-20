SELECT
    id_cliente,
    id_clinica,
    UPPER(nome_cliente) AS nome_cliente,
    data_nasc,
    cpf,
    UPPER(genero) AS genero,
    UPPER(profissao) AS profissao,
    telefone,
    origemid AS id_origem

FROM {{ source('raw', 'clientes') }}