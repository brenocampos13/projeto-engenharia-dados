# Projeto Engenharia de Dados

## Sobre o Projeto

Este projeto foi desenvolvido com o objetivo de praticar conceitos fundamentais de Engenharia de Dados, simulando a construção de um pipeline moderno de dados utilizando PostgreSQL, Python, Docker e dbt.

O projeto foi inicialmente desenvolvido com todas as transformações realizadas em Python. Após a introdução do dbt, as camadas de transformação foram refatoradas para uma arquitetura ELT, centralizando as regras de negócio, testes e documentação na ferramenta.

---

## Objetivos

Durante o desenvolvimento deste projeto foram praticados conceitos como:

- Modelagem de Dados
- SQL para Analytics
- Desenvolvimento de ETLs com Python
- Arquitetura de Data Warehouse
- Arquitetura ELT
- Transformações com dbt
- Data Quality
- Data Lineage
- Documentação automática
- Containerização com Docker
- Versionamento com Git e GitHub

---

## Arquitetura

O projeto utiliza uma arquitetura em camadas:

```text
OLTP
 ↓
Python
 ↓
RAW
 ↓
dbt
 ↓
STAGING
 ↓
dbt
 ↓
ANALYTICS
```

### OLTP

Camada transacional contendo os dados operacionais da empresa.

### RAW

Camada responsável por armazenar os dados brutos extraídos do sistema transacional.

### STAGING

Camada intermediária onde são realizadas padronizações, renomeações e transformações iniciais.

### ANALYTICS

Camada analítica utilizada para construção de indicadores, dimensões e fatos para consumo por ferramentas de BI.

---

## Tecnologias Utilizadas

### Banco de Dados

- PostgreSQL

### Linguagens

- SQL
- Python

### Ferramentas

- Docker
- dbt
- Git
- GitHub

### Bibliotecas

- psycopg2
- python-dotenv
- dbt-postgres

---

## Estrutura do Projeto

```text
Projeto Engenharia de Dados
│
├── docs
│
├── etl
│   ├── oltp_raw
│   │
│   └── legado
│       ├── raw_staging
│       └── staging_analytics
│
├── projeto_dbt
│   ├── models
│   │   ├── staging
│   │   └── analytics
│   │
│   ├── tests
│   ├── macros
│   ├── snapshots
│   ├── target
│   └── dbt_project.yml
│
├── sql
│   ├── ddl_oltp.sql
│   ├── ddl_raw.sql
│   └── legado
│
├── docker-compose.yml
│
├── config.py
├── requirements.txt
├── variaveis.env.example
├── README.md
└── .gitignore
```

---

## Pipeline de Dados

### Ingestão

O Python é responsável exclusivamente pela ingestão dos dados:

```text
OLTP
 ↓
RAW
```

Os pipelines realizam:

- Extração dos dados do sistema transacional
- Carregamento dos dados na camada RAW

Tabelas processadas:

- clientes
- clinicas
- origens
- produtos
- vendas

---

## Transformações com dbt

Após a ingestão, todas as transformações são realizadas pelo dbt.

### Camada Staging

Models:

- stg_clientes
- stg_clinicas
- stg_origens
- stg_produtos
- stg_vendas

Transformações realizadas:

- Padronização de textos com UPPER()
- Renomeação de colunas
- Organização dos dados para consumo analítico

### Camada Analytics

Models:

- dim_clientes
- fato_vendas

Transformações realizadas:

#### dim_clientes

Criação da coluna:

- idade

Utilizando:

```sql
EXTRACT(YEAR FROM AGE(CURRENT_DATE, data_nasc))
```

#### fato_vendas

Criação das colunas:

- ano_venda
- mes_venda

Utilizando:

```sql
EXTRACT(YEAR FROM data_venda)
EXTRACT(MONTH FROM data_venda)
```

Além disso, a fato consolida informações de:

- clientes
- produtos
- clínicas

por meio de joins entre os models da camada staging.

---

## Qualidade dos Dados

O projeto utiliza testes nativos do dbt para garantir a integridade dos dados.

Testes implementados:

### not_null

Garantia de preenchimento obrigatório.

Exemplos:

- id_cliente
- cpf
- genero
- id_venda

### unique

Garantia de unicidade.

Exemplos:

- id_cliente
- cpf

### accepted_values

Validação de domínio.

Exemplo:

```text
M
F
```

### relationships

Validação de relacionamentos entre tabelas.

Exemplos:

- vendas → clientes
- vendas → produtos
- vendas → clinicas

---

## Documentação e Data Lineage

O dbt gera automaticamente a documentação do projeto.

Comandos:

```bash
dbt docs generate
dbt docs serve
```

A documentação permite visualizar:

- Models
- Sources
- Dependências
- Data Lineage
- Descrições das tabelas
- Descrições das colunas

---

## Fluxo de Execução

```text
Docker Compose
 ↓
PostgreSQL
 ↓
DDL OLTP + RAW
 ↓
Seed OLTP
 ↓
Python ETL
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

---

## Como Executar

### 1. Clonar o Repositório

```bash
git clone https://github.com/brenocampos13/projeto-engenharia-dados.git
```

### 2. Configurar Variáveis de Ambiente

Criar um arquivo:

```text
variaveis.env
```

Utilizando como base:

```text
variaveis.env.example
```

### 3. Subir o Banco

```bash
docker compose up -d
```

O comando irá:

- Criar o PostgreSQL
- Executar as DDLs
- Popular o banco OLTP com dados de exemplo

### 4. Executar Ingestão

```bash
python etl/oltp_raw/main_oltp_raw.py
```

### 5. Executar Transformações

```bash
dbt run
```

### 6. Executar Testes

```bash
dbt test
```

### 7. Gerar Documentação

```bash
dbt docs generate
dbt docs serve
```

---

## Evolução do Projeto

### Versão 1

Transformações realizadas em Python:

```text
RAW
 ↓
Python
 ↓
STAGING

STAGING
 ↓
Python
 ↓
ANALYTICS
```

### Versão 2

Migração das transformações para dbt:

```text
RAW
 ↓
dbt
 ↓
STAGING

STAGING
 ↓
dbt
 ↓
ANALYTICS
```

Benefícios obtidos:

- Menos código Python
- Transformações centralizadas
- Testes automatizados
- Documentação automática
- Data Lineage
- Maior manutenibilidade

---

## Próximos Passos

Evoluções planejadas:

- Dockerização do dbt
- Apache Airflow
- AWS S3
- AWS RDS
- Spark / PySpark
- Databricks

---

## Autor

**Breno Campos Franco**

Projeto desenvolvido como parte da formação prática em Engenharia de Dados, com foco na construção de pipelines modernos, modelagem de dados, arquitetura ELT e Data Warehousing.
