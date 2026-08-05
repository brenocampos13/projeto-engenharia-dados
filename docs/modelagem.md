# Modelagem

## Dimensão Clientes

| Coluna       | Descrição                |
| ------------ | ------------------------ |
| id_cliente   | Identificador do cliente |
| nome_cliente | Nome do cliente          |
| cpf          | CPF                      |
| genero       | Sexo do cliente          |
| profissao    | Profissão                |
| idade        | Idade calculada          |

---

## Dimensão Produtos

| Coluna       | Descrição        |
| ------------ | ---------------- |
| id_produto   | Identificador    |
| nome_produto | Nome do produto  |
| marca        | Marca            |
| valor        | Valor do produto |

---

## Dimensão Clínicas

| Coluna     | Descrição       |
| ---------- | --------------- |
| id_clinica | Identificador   |
| clinica    | Nome da clínica |

---

## Dimensão Origens

| Coluna    | Descrição          |
| --------- | ------------------ |
| id_origem | Identificador      |
| origem    | Canal de aquisição |

---

## Fato Vendas

| Coluna     | Descrição              |
| ---------- | ---------------------- |
| id_venda   | Identificador da venda |
| id_cliente | Cliente                |
| id_produto | Produto                |
| id_clinica | Clínica                |
| valor_pago | Valor pago             |
| data_venda | Data da venda          |
| ano_venda  | Ano extraído           |
| mes_venda  | Mês extraído           |
