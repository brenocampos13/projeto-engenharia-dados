# Modelagem

## Visão Geral

A camada Analytics foi modelada utilizando conceitos de modelagem dimensional, contendo uma dimensão de clientes e uma tabela fato de vendas.

```text
dim_clientes
      │
      │
      ▼
fato_vendas
```

---

# Dimensão Clientes

Tabela: `analytics.dim_clientes`

Responsável por armazenar informações descritivas dos clientes utilizadas para análise.

| Coluna       | Descrição                |
| ------------ | ------------------------ |
| id_cliente   | Identificador do cliente |
| nome_cliente | Nome do cliente          |
| cpf          | CPF do cliente           |
| genero       | Gênero do cliente        |
| profissao    | Profissão do cliente     |
| data_nasc    | Data de nascimento       |
| id_origem    | Origem de aquisição      |
| idade        | Idade calculada pelo dbt |

Transformação aplicada:

```sql
EXTRACT(YEAR FROM AGE(CURRENT_DATE, data_nasc))
```

---

# Fato Vendas

Tabela: `analytics.fato_vendas`

Responsável por armazenar os eventos de venda realizados pela empresa.

| Coluna     | Descrição                 |
| ---------- | ------------------------- |
| id_venda   | Identificador da venda    |
| id_cliente | Cliente associado à venda |
| id_produto | Produto vendido           |
| id_clinica | Clínica responsável       |
| valor_pago | Valor pago na venda       |
| data_venda | Data da venda             |
| ano_venda  | Ano extraído da venda     |
| mes_venda  | Mês extraído da venda     |

Transformações aplicadas:

```sql
EXTRACT(YEAR FROM data_venda)
```

```sql
EXTRACT(MONTH FROM data_venda)
```

---

# Relacionamentos

A tabela fato é enriquecida através dos modelos da camada STAGING.

```text
stg_clientes
      │
      └──────────────┐
                     │
stg_produtos         │
      │              │
      └──────────┐   │
                 │   │
stg_clinicas     │   │
      │          │   │
      └──────┐   │   │
             ▼   ▼   ▼

        fato_vendas
```

Relacionamentos utilizados:

| Origem       | Destino     | Chave      |
| ------------ | ----------- | ---------- |
| stg_clientes | fato_vendas | id_cliente |
| stg_produtos | fato_vendas | id_produto |
| stg_clinicas | fato_vendas | id_clinica |

---

# Camada Staging

A camada STAGING é composta pelos seguintes modelos:

- stg_clientes
- stg_clinicas
- stg_origens
- stg_produtos
- stg_vendas

Esses modelos são utilizados para padronização dos dados antes da construção das tabelas analíticas.
