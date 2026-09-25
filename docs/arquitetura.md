# Arquitetura

## Objetivo

Este projeto tem como objetivo demonstrar a construção de um pipeline moderno de Engenharia de Dados utilizando PostgreSQL, Python, Docker, dbt e Apache Airflow.

A solução foi desenvolvida para simular um ambiente de Data Warehouse completo, contemplando ingestão de dados, transformações, testes de qualidade, documentação e orquestração de pipelines.

---

# Arquitetura da Solução

A arquitetura de dados do projeto segue o modelo:

```text
OLTP
 ↓
ETL Container
 ↓
RAW
 ↓
dbt Models
 ↓
STAGING
 ↓
ANALYTICS
```

A execução do pipeline é orquestrada pelo Apache Airflow através do DockerOperator.

```text
Airflow
 ├── ETL Container
 └── dbt Container
```

---

# Camadas do Data Warehouse

## OLTP

Banco transacional responsável por simular o sistema operacional da empresa.

Tabelas:

- clientes
- clinicas
- origens
- produtos
- vendas

Objetivo:

- Representar os dados operacionais
- Servir como fonte para os processos de ingestão

---

## RAW

Camada responsável por armazenar os dados extraídos do sistema transacional sem aplicação de regras de negócio.

Objetivos:

- Preservar os dados originais
- Garantir rastreabilidade
- Permitir reprocessamentos quando necessário

---

## STAGING

Camada intermediária responsável pela preparação dos dados para consumo analítico.

Transformações aplicadas:

- Padronização de textos utilizando `UPPER()`
- Renomeação de colunas
- Organização dos dados
- Padronização de nomenclaturas

As tabelas desta camada são materializadas como Views através do dbt.

Models:

- stg_clientes
- stg_clinicas
- stg_origens
- stg_produtos
- stg_vendas

---

## ANALYTICS

Camada destinada ao consumo analítico e construção de indicadores.

Models:

### dim_clientes

Transformações aplicadas:

- Cálculo da idade dos clientes

```sql
EXTRACT(YEAR FROM AGE(CURRENT_DATE, data_nasc))
```

---

### fato_vendas

Transformações aplicadas:

- Extração do ano da venda

```sql
EXTRACT(YEAR FROM data_venda)
```

- Extração do mês da venda

```sql
EXTRACT(MONTH FROM data_venda)
```

Além disso, a tabela fato consolida informações de:

- clientes
- produtos
- clinicas

através de joins realizados entre os modelos da camada STAGING.

---

# Fluxo de Execução

O pipeline completo segue a seguinte ordem:

```text
PostgreSQL
    ↓
Seed OLTP
    ↓
ETL Container
    ↓
RAW
    ↓
dbt run
    ↓
STAGING
    ↓
ANALYTICS
    ↓
dbt test
```

Quando executado pelo Apache Airflow:

```text
Airflow
    ↓
ETL Container
    ↓
dbt Container (dbt run)
    ↓
dbt Container (dbt test)
```

---

# Tecnologias Utilizadas

- PostgreSQL
- Python
- SQL
- Docker
- Apache Airflow
- dbt
- Git
- GitHub
