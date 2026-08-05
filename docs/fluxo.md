# Fluxo dos Dados

## Clientes

loja_oltp.clientes
↓
raw.clientes
↓
staging.clientes
↓
analytics.clientes

Transformações:

- nome_cliente em maiúsculo
- profissao em maiúsculo
- origemid renomeado para id_origem
- cálculo da idade

---

## Vendas

loja_oltp.vendas
↓
raw.vendas
↓
staging.vendas
↓
analytics.vendas

Transformações:

- criação da coluna ano_venda
- criação da coluna mes_venda

---

## Produtos

loja_oltp.produtos
↓
raw.produtos
↓
staging.produtos
↓
analytics.produtos

---

## Clínicas

loja_oltp.clinicas
↓
raw.clinicas
↓
staging.clinicas
↓
analytics.clinicas

---

## Origens

loja_oltp.origem
↓
raw.origem
↓
staging.origem
↓
analytics.origem
