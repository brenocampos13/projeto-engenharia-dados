# Projeto Engenharia de Dados

## Sobre o Projeto

Este projeto foi desenvolvido com o objetivo de praticar conceitos fundamentais de Engenharia de Dados, incluindo modelagem de dados, construção de pipelines ETL, organização em camadas analíticas e consultas SQL para análise de negócio.

O projeto simula um ambiente de dados utilizando PostgreSQL como banco de dados e Python para a construção dos processos ETL.

---

## Arquitetura

O projeto foi estruturado utilizando uma arquitetura em camadas:

```text
OLTP
 ↓
RAW
 ↓
STAGING
 ↓
ANALYTICS
```

### Camadas

#### OLTP

Camada transacional contendo os dados operacionais da loja.

#### RAW

Camada responsável por armazenar os dados brutos extraídos do sistema transacional.

#### STAGING

Camada de preparação dos dados, onde são realizadas padronizações e transformações intermediárias.

#### ANALYTICS

Camada analítica utilizada para consultas e geração de indicadores de negócio.

---

## Tecnologias Utilizadas

- PostgreSQL
- SQL
- Python
- Psycopg2
- Python Dotenv
- Git
- GitHub

---

## Estrutura do Projeto

```text
Projeto Engenharia de Dados
│
├── docs
│   ├── arquitetura.md
│   ├── fluxo.md
│   └── modelagem.md
│
├── etl
│   ├── ETL_OLTP_RAW
│   ├── ETL_RAW_STAGING
│   └── ETL_STAGING_ANALYTICS
│
├── sql
│   ├── ddl_oltp.sql
│   ├── ddl_raw.sql
│   ├── ddl_staging.sql
│   ├── ddl_analytics.sql
│   └── consultas.sql
│
├── .gitignore
├── README.md
├── requirements.txt
├── variaveis.env
└── variaveis.env.example
```

---

## Fluxo dos Dados

### ETL OLTP → RAW

Extração dos dados do banco transacional e carga na camada RAW.

Tabelas processadas:

- clientes
- clinicas
- origens
- produtos
- vendas

---

### ETL RAW → STAGING

Transformações realizadas:

- Padronização de texto utilizando UPPER()
- Renomeação de colunas para melhor legibilidade
- Tratamento e preparação dos dados

Exemplos:

```sql
UPPER(nome_cliente)
UPPER(genero)
UPPER(profissao)
```

---

### ETL STAGING → ANALYTICS

Transformações realizadas:

#### Clientes

Criação da coluna:

- idade

Utilizando:

```sql
EXTRACT(YEAR FROM AGE(NOW(), data_nasc))
```

#### Vendas

Criação das colunas:

- ano_venda
- mes_venda

Utilizando:

```sql
EXTRACT(YEAR FROM data_venda)
EXTRACT(MONTH FROM data_venda)
```

---

## Validação das Camadas

Foi realizada validação da quantidade de registros entre as camadas para garantir integridade dos dados.

Resultado:

| Camada    | Registros |
| --------- | --------: |
| RAW       |       912 |
| STAGING   |       912 |
| ANALYTICS |       912 |

Nenhum registro foi perdido durante as transformações.

---

## Consultas Analíticas

### 1. Faturamento Acumulado por Mês

Utilizando:

- SUM()
- Window Functions
- OVER()

---

### 2. Crescimento Mês contra Mês

Utilizando:

- LAG()
- CTEs
- Cálculo percentual

---

### 3. Produto Campeão de Faturamento por Mês

Utilizando:

- ROW_NUMBER()
- PARTITION BY
- CTEs
- Window Functions

Observação:

Em cenários com empates, a função DENSE_RANK() pode ser utilizada.

---

## Como Executar

### 1. Clonar o Repositório

```bash
git clone
```

### 2. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 3. Configurar Variáveis de Ambiente

Criar um arquivo:

```text
variaveis.env
```

Utilizando como base:

```text
variaveis.env.example
```

Exemplo:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=loja_dw
DB_USER=postgres
DB_PASSWORD=senha
```

### 4. Executar os Scripts SQL

Executar os arquivos:

```text
ddl_oltp.sql
ddl_raw.sql
ddl_staging.sql
ddl_analytics.sql
```

### 5. Executar os ETLs

Executar os scripts seguindo a ordem:

```text
ETL_OLTP_RAW
↓
ETL_RAW_STAGING
↓
ETL_STAGING_ANALYTICS
```

---

## Próximos Passos

Melhorias planejadas para futuras versões:

- Docker
- Airflow
- dbt
- Testes automatizados
- Data Quality Checks
- Integração com Cloud

---

## Autor

Projeto desenvolvido por Breno Campos Franco como parte da formação prática em Engenharia de Dados.
