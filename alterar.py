def atualizar(conexao): # ABRE CONEXÃO COM O DB PARA ALTERAR INFORMAÇÕES DOS PRODUTOS
    cursor = conexao.cursor() # ABRE INTERAÇÃO COM O DB
    try:
        atua = int(input( 
            # MENU PRA SELECIONAR ALTERAÇÃO
            "\n1. Atualizar nome do produto\n"
            "2. Atualizar categoria do produto\n"
            "3. Atualizar preço do produto\n"
            "4. Atualizar estoque\n"
            "5. Apagar produto\n"
            "0. Voltar\n"
            "Escolha: "))
    except ValueError: # ERRO PARA ALGO DIGITADO ALÉM DAS OPÇOES DADAS PELO MENU
        print("ERRO: Digite uma opção numérica!")
        cursor.close()
        return

    if atua == 1:
        # ALTERAÇÃO DE NOME
        try:
            identificador = int(input("Qual o ID do produto a ser alterado? "))
        except ValueError:
            print("ERRO: Digite um ID numérico válido!") # VERIFICA SE O ID FORNECIDO É NUMÉRICO
            cursor.close()
            return

        if identificador <= 0:
            print("ERRO: O ID deve ser maior que zero!") # O ID PRECISA SER MAIOR QUE 0
            cursor.close()
            return
    
        nome_novo = input("Qual será o nome? ").strip() # STRIP TIRA OS ESPAÇOS ANTES E DEPOIS DAS PALAVRAS

        if not nome_novo:
            print("ERRO: O nome não pode ficar vazio!") # VERIFICA SE O CAMPO NOME FICOU VAZIO
            cursor.close()
            return

        cursor.execute("""
        UPDATE mercadinho SET nome = ?
        WHERE id = ?
        """,(nome_novo, identificador))
        conexao.commit() # FAZ A ALTERAÇÃO DO NOME NA LISTA

        if cursor.rowcount > 0: # VERIFICA SE EXISTE O PRODUTO À SER ALTERADO
            print("Nome atualizado com sucesso!\n")
        else: 
            print("Produto não encontrado.")

    elif atua == 2:
        # ALTERAÇÃO DE CATEGORIA
        try:
            identificador = int(input("Qual o ID do produto a ser alterado?"))
        except ValueError:
            print("ERRO: Digite um ID numérico válido!") # # VERIFICA SE O ID FORNECIDO É NUMÉRICO
            cursor.close()
            return

        if identificador <= 0:
            print("ERRO: O ID deve ser maior que zero!") # # O ID PRECISA SER MAIOR QUE 0
            cursor.close()
            return

        categoria_nova =input("Qual será a nova categoria? ").strip() # STRIP TIRA ESPAÇOS

        if not categoria_nova or not categoria_nova.replace(" ", "").isalpha(): # CHECAGEM PARA ACEITAR APENAS LETRAS
            print("ERRO: Digite uma categoria válida, usando apenas letras!")
            cursor.close()
            return

        cursor.execute("""
            UPDATE mercadinho SET categoria = ? 
            WHERE id = ?
        """,(categoria_nova, identificador))
        conexao.commit()

        if cursor.rowcount > 0:
            print("Categoria atualizada com sucesso!\n")
        else:
            print("Produto não encontrado.")

    elif atua == 3: 
        # ALTERAÇÃO DE PREÇO
        try:
            identificador = int(input("Qual o ID do produto a ser alterado? "))
        except ValueError:
            print("ERRO: Digite um ID numérico válido!")
            cursor.close()
            return

        if identificador <= 0:
            print("ERRO: O ID deve ser maior que zero")
            cursor.close()
            return


        try:
            preco_novo = float(input("Qual será o novo preço? ").replace(",", ".")) # O PREÇO PODE SER DIGITADO COM , OU .
        except ValueError: 
            print("ERRO: Digite um preço numérico válido")
            cursor.close()
            return

        if preco_novo < 0:
            print("ERRO: O preço não pode ser negativo!")
            cursor.close()
            return
        
        cursor.execute("""
            UPDATE mercadinho SET preco = ? 
            WHERE id = ?
        """,( preco_novo, identificador))
        conexao.commit()

        if cursor.rowcount > 0:
            print("Preço atualizado com sucesso!\n")
        else:
            print("Produto não encontrado.")

    elif atua == 4: 
        # ALTERAÇÃO DE ESTOQUE
        try:
            identificador = int(input("Qual o ID do produto a ser alterado? "))
        except ValueError:
            print("ERRO: Digite um ID numérico válido!")
            cursor.close()
            return

        if identificador <= 0:
            print("ERRO: O ID deve ser maior que zero!")
            cursor.close()
            return
        
        try:
            estoque_novo = int(input("Qual a nova quantidade em estoque? "))
        except ValueError:
            print("ERRO: O estoque deve ser um número inteiro!")
            cursor.close()
            return

        if estoque_novo < 0:
            print("ERRO: O estoque não pode ser negativo!")
            cursor.close()
            return

        cursor.execute("""
            UPDATE mercadinho SET estoque = ? 
            WHERE id = ?
        """,( estoque_novo, identificador))
        conexao.commit()

        if cursor.rowcount > 0:
            print("Estoque atualizado com sucesso!\n")
        else:
            print("Produto não encontrado.")           

    elif atua == 5: 
        # APAGA O PRODUTO PELO ID
        try:
            identificador = int(input("Qual o ID do produto a ser deletado? "))
        except ValueError:
            print("ERRO: Digite um ID numérico válido!")
            cursor.close()
            return

        if identificador <= 0:
            print("ERRO: O ID deve ser maior que zero!")
            cursor.close()
            return
        
        cursor.execute("""
            DELETE FROM mercadinho 
            WHERE id = ?
        """, (identificador,))
        conexao.commit()

        if cursor.rowcount > 0:
            print("Produto deletado com sucesso!\n")
        else:
            print("Produto não encontrado para deletar.")

    elif atua == 0: # VOLTA PRO MENU PRINCIPAL
        cursor.close()
        return

    else: # SE FOI DIGITADO ALGO ALÉM DOS NÚMEROS CORRESPONDENTES, ELE CAI AQUI E SAI
        print("Opção inválida, tente novamente.")

    cursor.close() # FECHA INTERAÇÃO COM O DB