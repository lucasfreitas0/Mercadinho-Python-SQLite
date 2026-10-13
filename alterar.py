def atualizar(conexao):
    cursor = conexao.cursor()

    atua = int(input(
        "1. Atualizar nome do produto.\n" \
        "2. Atualizar categoria do produto\n" \
        "3. Atualizar preço do produto\n" \
        "4. Apagar produto\n"
        "Escolha: "))

    if atua == 1:
        nome_antigo = input("Qual o nome do produto à ser alterado? ")
        nome_novo = input("Qual será o nome? ")
        cursor.execute("""
        UPDATE mercadinho SET nome = ? WHERE
        nome = ?
        """,(nome_novo, nome_antigo))
        conexao.commit()
        print("Nome atualizado com sucesso!")

    elif atua == 2:
            categoria_antiga = input("Qual categoria será alterada?")
            categoria_nova = input("Qual será a nova categoria?")
            cursor.execute("""
        UPDATE mercadinho SET categoria = ? WHERE 
        categoria = ?
        """,(categoria_nova, categoria_antiga))
            conexao.commit()
            print("Categoria atualizada com sucesso!")
            

    elif atua == 3:
            preco_antigo = float(input("Qual o preço à ser alterado?"))
            preco_novo = float(input("Qual será o novo preço?"))
            cursor.execute("""
        UPDATE mercadinho SET preco = ? WHERE
        preco = ?
        """,( preco_novo, preco_antigo))
            conexao.commit()
            print("Preço atualizado com sucesso!")

    elif atua == 4:
        identificador = int(input("Qual o id do produto á ser deletado?"))
        cursor.execute("""
        DELETE FROM mercadinho WHERE id = ?
""", (identificador,))
        conexao.commit()
        print("Produto deletado com sucesso!")

    else:
        print("Opção inválida, tente novamente.")
