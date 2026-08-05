-- QUERY 1
-- FATURAMENTO ACUMULADO POR MÊS
WITH faturamento_mes AS (
	SELECT
		DATE_TRUNC('month', data_venda) AS mes,
		SUM(valor_pago) AS faturamento
	FROM
		loja_oltp.vendas
	GROUP BY
		DATE_TRUNC('month', data_venda)
)
SELECT
	mes,
	faturamento,
	SUM(faturamento) OVER(
		ORDER BY mes ASC
	) AS faturamento_acumulado
FROM
	faturamento_mes
;

-- QUERY 2
-- CRESCIMENTO MÊS CONTRA MÊS
WITH faturamento_mes AS(
	SELECT
		DATE_TRUNC('month', data_venda) AS mes,
		SUM(valor_pago) AS faturamento_atual
	FROM loja_oltp.vendas
	GROUP BY
		DATE_TRUNC('month', data_venda)
), faturamento_mes_anterior AS(
	SELECT
		*,
		LAG(faturamento_atual) OVER(
			ORDER BY mes
		) AS faturamento_anterior
	FROM faturamento_mes
)
SELECT
    *,
    ROUND(
        (
            faturamento_atual - faturamento_anterior
        ) / faturamento_anterior * 100,
        2
    ) AS porcentagem_crescimento
FROM faturamento_mes_anterior
;

-- QUERY 3
-- PRODUTO CAMPEÃO DE FATURAMENTO POR MÊS
WITH produto_faturamento AS(
	SELECT
		DATE_TRUNC('month', vds.data_venda) AS mes,
		pdt.nome_produto AS nome_produto,
		SUM(vds.valor_pago) AS faturamento
	FROM
		loja_oltp.vendas vds
	JOIN
		loja_oltp.produtos pdt
	ON
		vds.id_produto = pdt.id_produto
	GROUP BY
		DATE_TRUNC('month', vds.data_venda), nome_produto
), ranking_produto AS(
	SELECT
		*,
		ROW_NUMBER() OVER(
			PARTITION BY mes
			ORDER BY faturamento DESC
		) AS ranking
	FROM
		produto_faturamento
)
SELECT
	*
FROM
	ranking_produto
WHERE
	ranking = 1
;
-- ROW_NUMBER foi utilizado para retornar apenas um campeão por mês.
-- Em cenários onde empates devem ser considerados,
-- DENSE_RANK pode ser utilizado.

-- =========================================
-- VALIDAÇÃO DAS CAMADAS

SELECT 'RAW' AS camada, COUNT(*)
FROM raw.vendas

UNION ALL

SELECT 'STAGING', COUNT(*)
FROM staging.vendas

UNION ALL

SELECT 'ANALYTICS', COUNT(*)
FROM analytics.vendas
;

-- =========================================
-- CONSULTA ANALYTICS

SELECT *
FROM analytics.vendas
LIMIT 10
;