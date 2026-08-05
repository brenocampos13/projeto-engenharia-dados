# Arquitetura

## Objetivo

Este projeto tem como objetivo demonstrar a construção de um Data Warehouse utilizando PostgreSQL e Python, aplicando conceitos de Engenharia de Dados como ETL, modelagem dimensional e organização em camadas.

## Arquitetura de Dados

O projeto foi desenvolvido utilizando a seguinte arquitetura:

OLTP
↓
RAW
↓
STAGING
↓
ANALYTICS

### OLTP

Banco transacional que simula o sistema operacional da empresa.

Tabelas:

- clientes
- clinicas
- origem
- produtos
- vendas

### RAW

Camada responsável por armazenar uma cópia fiel dos dados extraídos da origem.

Objetivo:

- Preservar os dados originais
- Garantir rastreabilidade

### STAGING

Camada responsável por padronizar e preparar os dados para análise.

Transformações aplicadas:

- Padronização de textos com UPPER()
- Renomeação de colunas
- Organização dos dados

### ANALYTICS

Camada voltada para consumo analítico.

Transformações aplicadas:

- Cálculo da idade dos clientes
- Extração do ano da venda
- Extração do mês da venda
