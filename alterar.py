def atualizar(conexao): # ABRE CONEXÃO COM O DB PARA ALTERAR INFORMAÇÕES DOS PRODUTOS
    cursor = conexao.cursor()

    atua = int(input( # MENU PRA SELECIONAR ALTERAÇÃO
        "1. Atualizar nome do produto.\n" \
        "2. Atualizar categoria do produto\n" \
        "3. Atualizar preço do produto\n" \
        "4. Apagar produto\n"
        "Escolha: "))

    if atua == 1: # ALTERAÇÃO DE NOME
        identificador = int(input("Qual o id do produto á ser alterado? "))
        nome_novo = input("Qual será o nome? ")
        cursor.execute("""
        UPDATE mercadinho SET nome = ?
        WHERE id = ?
        """,(nome_novo, identificador))
        conexao.commit()

        if cursor.rowcount > 0: # VERIFICA SE EXISTE O PRODUTO À SER ALTERADO
            print("Nome atualizado com sucesso!\n")
        else: 
            print("Produto não encontrado.")

    elif atua == 2: # ALTERAÇÃO DE CATEGORIA
            identificador = int(input("Qual o id do produto á ser alterado? "))
            categoria_nova = input("Qual será a nova categoria? ")
            cursor.execute("""
        UPDATE mercadinho SET categoria = ? 
        WHERE id = ?
        """,(categoria_nova, identificador))
            conexao.commit()

            if cursor.rowcount > 0:
                print("Categoria atualizada com sucesso!\n")
            else:
                print("Categoria não encontrada.")

    elif atua == 3: # ALTERAÇÃO DE PREÇO
            identificador = int(input("Qual o id do produto á ser alterado? "))
            preco_novo = float(input("Qual será o novo preço? "))
            cursor.execute("""
        UPDATE mercadinho SET preco = ? 
        WHERE id = ?
        """,( preco_novo, identificador))
            conexao.commit()

            if cursor.rowcount > 0:
                print("Preço atualizado com sucesso!\n")
            else:
                print("Preço não encontrado.")

    elif atua == 4: # APAGA O PRODUTO PELO ID
        identificador = int(input("Qual o id do produto á ser deletado?"))
        cursor.execute("""
        DELETE FROM mercadinho WHERE id = ?
""", (identificador,))
        conexao.commit()

        if cursor.rowcount > 0:
            print("Produto deletado com sucesso!\n")
        else:
            ("Produto não encontrado para deletar.")

    else:
        print("Opção inválida, tente novamente.")

    cursor.close()
