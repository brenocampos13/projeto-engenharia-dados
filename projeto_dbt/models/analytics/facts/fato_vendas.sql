SELECT
    vds.id_venda AS id_venda,
    cli.clinica AS clinica,
    clt.nome_cliente AS nome_cliente,
    pdt.nome_produto AS nome_produto,
    vds.quantidade AS quantidade,
    vds.valor_pago AS valor_pago,
    vds.data_venda AS data_venda,
    EXTRACT(YEAR FROM vds.data_venda) AS ano_venda,
    EXTRACT(MONTH FROM vds.data_venda) AS mes_venda
FROM {{ ref('stg_vendas') }} vds
LEFT JOIN {{ ref('stg_clientes') }} clt
    ON vds.id_cliente = clt.id_cliente
LEFT JOIN {{ ref('stg_produtos') }} pdt
    ON vds.id_produto = pdt.id_produto
LEFT JOIN {{ ref('stg_clinicas') }} cli
    ON vds.id_clinica = cli.id_clinica