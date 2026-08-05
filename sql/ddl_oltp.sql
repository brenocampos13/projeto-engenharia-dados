-- Cria schema loja_oltp
CREATE SCHEMA IF NOT EXISTS loja_oltp
;

-- Cria a tabela clinicas
CREATE TABLE IF NOT EXISTS loja_oltp.clinicas
(
    id_clinica integer NOT NULL DEFAULT nextval('loja_oltp.dim_clinicas_id_clinica_seq'::regclass),
    clinica character varying(50) COLLATE pg_catalog."default",
    cnpj character varying(20) COLLATE pg_catalog."default",
    CONSTRAINT dim_clinicas_pkey PRIMARY KEY (id_clinica),
    CONSTRAINT dim_clinicas_cnpj_key UNIQUE (cnpj)
)
;

-- Cria a tabela origens
CREATE TABLE IF NOT EXISTS loja_oltp.origens
(
    id_origem integer NOT NULL DEFAULT nextval('loja_oltp.dim_origem_id_origem_seq'::regclass),
    origem character varying(50) COLLATE pg_catalog."default",
    CONSTRAINT dim_origem_pkey PRIMARY KEY (id_origem)
)
;

-- Cria a tabela produtos
CREATE TABLE IF NOT EXISTS loja_oltp.produtos
(
    id_produto integer NOT NULL DEFAULT nextval('loja_oltp.dim_produtos_id_produto_seq'::regclass),
    nome_produto character varying(100) COLLATE pg_catalog."default" NOT NULL,
    marca character varying(50) COLLATE pg_catalog."default" NOT NULL,
    valor numeric(10,2) NOT NULL,
    CONSTRAINT dim_produtos_pkey PRIMARY KEY (id_produto)
)
;

-- Cria a tabela clientes
CREATE TABLE IF NOT EXISTS loja_oltp.clientes
(
    id_cliente integer NOT NULL DEFAULT nextval('loja_oltp.dim_clientes_id_cliente_seq'::regclass),
    id_clinica integer,
    nome_cliente character varying(100) COLLATE pg_catalog."default",
    data_nasc date NOT NULL,
    cpf character(11) COLLATE pg_catalog."default",
    genero character(1) COLLATE pg_catalog."default",
    profissao character varying(50) COLLATE pg_catalog."default",
    telefone character varying(20) COLLATE pg_catalog."default",
    origemid integer,
    CONSTRAINT dim_clientes_pkey PRIMARY KEY (id_cliente),
    CONSTRAINT dim_clientes_cpf_key UNIQUE (cpf),
    CONSTRAINT dim_clientes_id_clinica_fkey FOREIGN KEY (id_clinica)
        REFERENCES loja_oltp.clinicas (id_clinica) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT dim_clientes_origemid_fkey FOREIGN KEY (origemid)
        REFERENCES loja_oltp.origens (id_origem) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)
;

-- Cria a tabela vendas
CREATE TABLE IF NOT EXISTS loja_oltp.vendas
(
    id_venda integer NOT NULL DEFAULT nextval('loja_oltp.fato_vendas_id_venda_seq'::regclass),
    id_clinica integer,
    id_cliente integer,
    id_produto integer,
    quantidade integer NOT NULL,
    valor_pago numeric(10,2) NOT NULL,
    data_venda timestamp without time zone NOT NULL,
    data_carga timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fato_vendas_pkey PRIMARY KEY (id_venda),
    CONSTRAINT fato_vendas_id_cliente_fkey FOREIGN KEY (id_cliente)
        REFERENCES loja_oltp.clientes (id_cliente) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT fato_vendas_id_clinica_fkey FOREIGN KEY (id_clinica)
        REFERENCES loja_oltp.clinicas (id_clinica) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT fato_vendas_id_produto_fkey FOREIGN KEY (id_produto)
        REFERENCES loja_oltp.produtos (id_produto) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)
;