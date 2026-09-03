# Projeto Engenharia de Dados

## Sobre o Projeto

Este projeto foi desenvolvido com o objetivo de praticar conceitos fundamentais de Engenharia de Dados, incluindo modelagem de dados, construção de pipelines ETL, organização em camadas analíticas e consultas SQL para análise de negócio.

O projeto simula um ambiente de dados utilizando PostgreSQL como banco de dados e Python para o desenvolvimento dos processos ETL.

---

## Objetivos

Durante o desenvolvimento deste projeto foram praticados conceitos como:

- Modelagem de Dados
- SQL para Analytics
- Desenvolvimento de ETLs com Python
- Arquitetura de Data Warehouse
- Organização em camadas (OLTP, RAW, STAGING e ANALYTICS)
- Modularização de código
- Versionamento com Git e GitHub

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

### Banco de Dados

- PostgreSQL

### Linguagens

- SQL
- Python

### Bibliotecas

- psycopg2
- python-dotenv

### Ferramentas

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
│   ├── oltp_raw
│   │   ├── clientes.py
│   │   ├── clinicas.py
│   │   ├── origens.py
│   │   ├── produtos.py
│   │   └── vendas.py
│   │
│   ├── raw_staging
│   │   ├── clientes.py
│   │   ├── clinicas.py
│   │   ├── origens.py
│   │   ├── produtos.py
│   │   └── vendas.py
│   │
│   └── staging_analytics
│       ├── clientes.py
│       ├── clinicas.py
│       ├── origens.py
│       ├── produtos.py
│       └── vendas.py
│
├── sql
│   ├── ddl_oltp.sql
│   ├── ddl_raw.sql
│   ├── ddl_staging.sql
│   ├── ddl_analytics.sql
│   └── consultas.sql
│
├── config.py
├── main.py
├── requirements.txt
├── variaveis.env.example
├── README.md
└── .gitignore
```

---

## Organização dos ETLs

Cada pipeline foi estruturado seguindo o padrão:

- extract()
- load()
- pipeline()

O arquivo `main.py` atua como ponto central de execução, responsável por orquestrar todas as etapas do pipeline.

### Fluxo de Execução

```text
main.py
│
├── OLTP → RAW
│
├── RAW → STAGING
│
└── STAGING → ANALYTICS
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

Foi realizada validação da quantidade de registros entre as camadas para garantir a integridade dos dados.

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

### 2. Crescimento Mês contra Mês

Utilizando:

- LAG()
- CTEs
- Cálculo Percentual

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
git clone https://github.com/brenocampos13/projeto-engenharia-dados.git
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
HOST=localhost
PORT=5432
DATABASE=loja_oltp
DATABASE2=loja_dw
USER=postgres
PASSWORD=senha
```

### 4. Executar os Scripts SQL

Executar os arquivos:

```text
ddl_oltp.sql
ddl_raw.sql
ddl_staging.sql
ddl_analytics.sql
```

### 5. Executar o Pipeline

```bash
python main.py
```

---

## Aprendizados

Durante o desenvolvimento deste projeto foram praticados conceitos como:

- Arquitetura de Data Warehouse
- Modelagem OLTP e Analítica
- Desenvolvimento de ETLs em Python
- SQL Analítico
- Window Functions
- Modularização de Código
- Organização de Projetos de Dados
- Versionamento com Git
- Documentação Técnica

---

## Próximos Passos

Melhorias planejadas para futuras versões:

- Docker
- dbt
- Apache Airflow
- Data Quality Checks
- Integração com AWS S3
- Testes Automatizados

---

## Autor

**Breno Campos Franco**

Projeto desenvolvido como parte da formação prática em Engenharia de Dados, com foco na construção de pipelines ETL, modelagem de dados e arquitetura de Data Warehouse.
