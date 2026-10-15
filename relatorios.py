def relatorios(conexao):
    cursor = conexao.cursor() # CRIA INTERAÇÃO COM O DB

    try:
        escolha = int(input( # MENU DE RELATÓRIOS
        "1. Relatório geral\n"
        "2. Relatório por categoria\n"
        "Escolha: "
        ))
    except ValueError:
        print("Opção inválida! Digite um número.")
        cursor.close()
        return

    if escolha == 1: # RELATÓRIO GERAL
        cursor.execute("""
        SELECT COUNT(*) AS quantidade,
        MIN(preco) AS menor_preco,
        MAX(preco) AS maior_preco,
        AVG(preco) AS preco_medio
        FROM mercadinho
        """)
        resultado = cursor.fetchone()
        if resultado[0] == 0:
            print("\nNenhum produto cadastrado")
            cursor.close()
            return
    
        quantidade, menor_preco, maior_preco, preco_medio = resultado

        print(f'\nQuantidade de produtos: {quantidade} \nMenor preço: R$ {menor_preco:.2f} \nMaior preço: R${maior_preco:.2f} \nPreço médio: R${preco_medio:.2f}\n')

    elif escolha == 2: # RELATÓRIO POR CATEGORIA
        cursor.execute("""
        SELECT categoria, COUNT(*) AS quantidade, AVG(preco) AS preco_medio
        FROM mercadinho
        GROUP BY categoria
        """)
        resultado = cursor.fetchall()
        if not resultado:
            print("\nNenhum produto cadastrado")
            cursor.close()
            return

        for i in resultado:
            categoria, quantidade, preco_medio = i
            print(f'\nCategoria: {categoria} \nQuantidade: {quantidade} \nPreço médio: R${preco_medio}\n')

    else:
        print("Opção inválida!")

    cursor.close()