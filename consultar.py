def buscar(conexao): #FUNÇAO PARA BUSCAR UM PRODUTO OU TODOS
    cursor = conexao.cursor() # ABRE INTERAÇÃO COM O DB

    try: # MENU PRINCIPAL
        escolha = int(input(
            "\n=== Consultar Produtos ===\n"
            "\n1. Procurar produto\n"
            "2. Listar todos os produtos\n"
            "0. Voltar\n"
            "\nEscolha: "
            ))
    except ValueError: # ERRO CASO O INPUT NÃO ESTEJA NO MENU
        print("Opção inválida! Digite um número.")
        cursor.close()
        return
    
    if escolha == 1:
        try: # MENU SECUNDÁRIO
            menu = int(input(
                "\n === Procurar produto ===\n"
                "\n1. Procurar pelo ID\n"
                "2. Procurar pelo nome\n"
                "3. Procurar pela categoria\n"
                "4. Procurar produtos pelo menor preço\n"
                "0. Voltar\n"
                "\nEscolha: "
            ))
        except ValueError: # # ERRO CASO O INPUT NÃO ESTEJA NO MENU
            print("Opção inválida! Digite um número.")
            cursor.close()
            return

        if menu == 1: # PROCURAR PRODUTO PELO ID
            try:
                identificador = int(input("\nQual o ID do produto a ser procurado? "))
            except ValueError:
                print("ERRO: Digite um ID numérico válido")
                cursor.close()
                return

            if identificador <= 0:
                print("ERRO: O ID deve ser maior que zero!") # O ID PRECISA SER MAIOR QUE 0
                cursor.close()
                return

            # SELECIONA NA TABELA ONDE O ID FOR IGUAL AO INSERIDO
            cursor.execute("""
            SELECT * FROM mercadinho WHERE id = ? 
            """,(identificador,))

            # COMO O ID NÃO SE REPETE, O FETCHONE MOSTRA APENAS O ÚNICO ID
            resultado = cursor.fetchone()
            if resultado is not None:
                id, nome, categoria, preco, estoque = resultado
                print(f'\nId: {id} \nNome: {nome}\nCategoria: {categoria}\nPreço: {preco:.2f}\nEstoque: {estoque}\n') # TIRA OS DADOS DAS TUPLAS E DEIXA MAIS VISÍVEL
            else:
                print ("Produto não encontrado.")

        elif menu == 2: # PROCURAR PRODUTO PELO NOME
            nome = input("\nQual o nome do produto a ser procurado? ").strip() # STRIP TIRA OS ESPAÇOS DESNECESSÁRIOS

            if not nome:
                print("ERRO: O nome não pode ficar vazio!") # ERRO CASO O NOME SEJA DEIXADO EM BRANCO
                cursor.close()
                return

            cursor.execute("""
            SELECT * FROM mercadinho WHERE nome LIKE ?
            """, (f"%{nome}%",)) # PROCURA PELO NOME DO PRODUTO DIGITADO

            resultados = cursor.fetchall() # FETCHALL RETORNA TODOS OS REGISTROS QUE SE ENCAIXAM NA REGRA FORNECIDA

            if resultados:
                for i in resultados:
                    id, nome, categoria, preco, estoque = i
                    print(f'\nId: {id}\nNome: {nome}\nCategoria: {categoria}\nPreço: {preco:.2f}\nEstoque: {estoque}\n') # TIRA OS DADOS DAS TUPLAS E DEIXA MAIS VISÍVEL
            else:
                print("Produto não encontrado.")

        elif menu == 3: # PROCURAR PRODUTO PELA CATEGORIA
            categoria = input("\nQual categoria será procurada? ").strip()

            if not categoria or not categoria.replace(" ", "").isalpha(): # CHECAGEM PARA ACEITAR APENAS LETRAS E TIRAR OS ESPAÇOS DESNECESSÁRIOS
                print("ERRO: Digite uma categoria válida, usando apenas letras!") # ERRO CASO HAJA NÚMEROS DIGITADOS
                cursor.close()
                return

            cursor.execute("""
            SELECT * FROM mercadinho WHERE categoria like ?
            """,(f"%{categoria}%",)) # PROCURA PELA CATEGORIA DIGITADA
            resultados = cursor.fetchall()

            if resultados:
                for i in resultados:
                    id, nome, categoria, preco, estoque = i
                    print(f'\nId: {id}\nNome: {nome}\nCategoria: {categoria}\nPreço: {preco:.2f}\nEstoque: {estoque}\n') # TIRA OS DADOS DAS TUPLAS E DEIXA MAIS VISÍVEL
            else:
                print("Produto não encontrado.")

        elif menu == 4: # MOSTRA OS PRODUTOS ORDENADOS POR PREÇO CRESCENTE
            cursor.execute("""
            SELECT * FROM mercadinho ORDER BY preco ASC 
            """) # SELECIONA OS PRODUTOS POR PREÇO CRESCENTE
            resultados = cursor.fetchall() # SELECIONA TODOS OS PRODUTOS DA LISTA

            if resultados:
                for i in resultados:
                    id, nome, categoria, preco, estoque = i
                    print(f'\nId: {id}\nNome: {nome}\nCategoria: {categoria}\nPreço: {preco:.2f}\nEstoque: {estoque}\n') # TIRA OS DADOS DAS TUPLAS E DEIXA MAIS VISÍVEL
            else:
                print("Nenhum produto encontrado.")

        elif menu == 0: # VOLTAR PARA O MENU
            cursor.close()
            return

        else: # iNPUT INVÁLIDO PARA O MENU
            print("Opção inválida.")
            cursor.close()
            return

    elif escolha == 2: # SELECIONA TODOS OS PRODUTOS DA LISTA
        cursor.execute("SELECT * FROM mercadinho")
        resultados = cursor.fetchall() # FETCHALL RETORNA TODOS OS REGISTROS DA LISTA

        if resultados:
            for i in resultados:
                id, nome, categoria, preco, estoque = i
                print(f'\nId: {id}\nNome: {nome}\nCategoria: {categoria}\nPreço: {preco:.2f}\nEstoque: {estoque}\n') # TIRA OS DADOS DAS TUPLAS E DEIXA MAIS VISÍVEL
        else:
            print("Nenhum produto cadastrado.")

    elif escolha == 0:
        cursor.close()
        return
    else:
        print("Opção inválida.") # SE A OPÇÃO ESCOLHIDA NÃO ESTIVER NO MENU PRINCIPAL, CAI AQUI

    cursor.close() # FECHA A INTERAÇÃO COM O DB