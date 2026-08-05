-- Cria o schema staging:
CREATE SCHEMA IF NOT EXISTS staging;

-- Cria a tabela clientes:
CREATE TABLE IF NOT EXISTS staging.clientes
(
    id_cliente integer NOT NULL,
    id_clinica integer,
    nome_cliente character varying(100) COLLATE pg_catalog."default",
    data_nasc date NOT NULL,
    cpf character(11) COLLATE pg_catalog."default",
    genero character(1) COLLATE pg_catalog."default",
    profissao character varying(50) COLLATE pg_catalog."default",
    telefone character varying(20) COLLATE pg_catalog."default",
    id_origem integer
)
;

-- Cria a tabela clinicas:
CREATE TABLE IF NOT EXISTS staging.clinicas
(
    id_clinica integer NOT NULL,
    clinica character varying(50) COLLATE pg_catalog."default",
    cnpj character varying(20) COLLATE pg_catalog."default"
)
;

-- Cria a tabela origens:
CREATE TABLE IF NOT EXISTS staging.origens
(
    id_origem integer NOT NULL,
    origem character varying(50) COLLATE pg_catalog."default"
)
;

-- Cria a tabela produtos:
CREATE TABLE IF NOT EXISTS staging.produtos
(
    id_produto integer NOT NULL,
    nome_produto character varying(100) COLLATE pg_catalog."default",
    marca character varying(50) COLLATE pg_catalog."default",
    valor numeric(10,2)
)
;

-- Cria a tabela vendas:
CREATE TABLE IF NOT EXISTS staging.vendas
(
    id_venda integer NOT NULL,
    id_clinica integer,
    id_cliente integer,
    id_produto integer,
    quantidade integer NOT NULL,
    valor_pago numeric(10,2) NOT NULL,
    data_venda timestamp without time zone NOT NULL
)
;