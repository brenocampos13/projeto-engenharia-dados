# Fluxo dos Dados

Este documento descreve o fluxo dos dados ao longo das camadas do Data Warehouse, desde a origem transacional até a camada analítica.

---

# Clientes

```text
loja_oltp.clientes
        ↓
raw.clientes
        ↓
staging.stg_clientes
        ↓
analytics.dim_clientes
```

Transformações aplicadas:

- Padronização de `nome_cliente` com `UPPER()`
- Padronização de `profissao` com `UPPER()`
- Renomeação de `origemid` para `id_origem`
- Cálculo da idade do cliente

```sql
EXTRACT(YEAR FROM AGE(CURRENT_DATE, data_nasc))
```

---

# Vendas

```text
loja_oltp.vendas
        ↓
raw.vendas
        ↓
staging.stg_vendas
        ↓
analytics.fato_vendas
```

Transformações aplicadas:

- Extração do ano da venda

```sql
EXTRACT(YEAR FROM data_venda)
```

- Extração do mês da venda

```sql
EXTRACT(MONTH FROM data_venda)
```

- Consolidação das informações de:
  - clientes
  - produtos
  - clínicas

através de joins com as tabelas dimensionais da camada STAGING.

---

# Produtos

```text
loja_oltp.produtos
        ↓
raw.produtos
        ↓
staging.stg_produtos
        ↓
analytics.fato_vendas
```

Transformações aplicadas:

- Padronização da estrutura para consumo analítico
- Utilização como dimensão na construção da tabela fato de vendas

---

# Clínicas

```text
loja_oltp.clinicas
        ↓
raw.clinicas
        ↓
staging.stg_clinicas
        ↓
analytics.fato_vendas
```

Transformações aplicadas:

- Padronização da estrutura para consumo analítico
- Utilização como dimensão na construção da tabela fato de vendas

---

# Origens

```text
loja_oltp.origens
        ↓
raw.origens
        ↓
staging.stg_origens
        ↓
analytics.dim_clientes
```

Transformações aplicadas:

- Padronização da estrutura para consumo analítico
- Utilização para enriquecimento da dimensão de clientes

---

# Resumo do Fluxo

```text
CLIENTES
loja_oltp.clientes
    ↓
raw.clientes
    ↓
staging.stg_clientes
    ↓
analytics.dim_clientes


VENDAS
loja_oltp.vendas
    ↓
raw.vendas
    ↓
staging.stg_vendas
    ↓
analytics.fato_vendas


PRODUTOS
loja_oltp.produtos
    ↓
raw.produtos
    ↓
staging.stg_produtos
    ↓
analytics.fato_vendas


CLÍNICAS
loja_oltp.clinicas
    ↓
raw.clinicas
    ↓
staging.stg_clinicas
    ↓
analytics.fato_vendas


ORIGENS
loja_oltp.origens
    ↓
raw.origens
    ↓
staging.stg_origens
    ↓
analytics.dim_clientes
```
