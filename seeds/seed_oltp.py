from config import get_connect_dw

def seed_clinicas(cur):

    clinicas = [
        ("Clínica Alpha","11111111111111111"),
        ("Clínica Beta","22222222222222222"),
        ("Clínica Charlie","33333333333333333"),
        ("Clínica Delta","44444444444444444")
    ]

    cur.executemany(
        """
        INSERT INTO loja_oltp.clinicas
        (clinica, cnpj)
        VALUES (%s, %s)
        """,
        clinicas
    )

def seed_origens(cur):

    origens = [
        ("Instagram",),
        ("Facebook",),
        ("Google",),
        ("Indicação",)
    ]

    cur.executemany(
        """
        INSERT INTO loja_oltp.origens
        (origem)
        VALUES (%s)
        """,
        origens
    )

def seed_produtos(cur):

    produtos = [
        ("Botox", "Allergan", 1200.00),
        ("Preenchimento Labial", "Rennova", 900.00),
        ("Skinbooster", "Restylane", 700.00),
        ("Bioestimulador", "Galderma", 1500.00),
        ("Limpeza de Pele", "Próprio", 180.00)
    ]

    cur.executemany(
        """
        INSERT INTO loja_oltp.produtos
        (nome_produto, marca, valor)
        VALUES (%s, %s, %s)
        """,
        produtos
    )

def seed_clientes(cur):

    clientes = [
        ("1","Francisco","1968-11-09","12345678912","M","Engenheiro de Dados", "1111111111","4"),
        ("2","Maria","1999-09-13","12345678913","F","Cozinheiro", "2222222222","3"),
        ("3","João","1975-12-09","12345678914","M","Motorista", "3333333333","2"),
        ("4","Ana","1996-04-25","12345678915","F","Autonomo", "4444444444","1")
    ]

    cur.executemany(
        """
        INSERT INTO loja_oltp.clientes
        (id_clinica, nome_cliente, data_nasc, cpf, genero, profissao, telefone, origemid)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """,
        clientes
    )

def seed_vendas(cur):

    vendas = [
        (1, 1, 1, 1, 1200.00, "2026-01-10"),
        (1, 2, 2, 1, 900.00, "2026-02-15"),
        (2, 3, 3, 2, 1400.00, "2026-03-20"),
        (3, 4, 4, 1, 1500.00, "2026-04-05"),
        (2, 2, 4, 3, 540.00, "2026-05-12")
    ]

    cur.executemany(
        """
        INSERT INTO loja_oltp.vendas
        (id_clinica, id_cliente, id_produto, quantidade, valor_pago, data_venda)
        VALUES (%s, %s, %s, %s, %s, %s)
        """,
        vendas
    )

def main():
    conn = get_connect_dw()

    cur = conn.cursor()

    seed_clinicas(cur)
    seed_produtos(cur)
    seed_origens(cur)
    seed_clientes(cur)
    seed_vendas(cur)

    conn.commit()

    cur.close()
    conn.close()

    print("Seed executado com sucesso!")

if __name__ == "__main__":
    main()