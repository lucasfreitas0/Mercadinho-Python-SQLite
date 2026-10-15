## VERIFICA SE O PRODUTO EXISTE NO NA LISTA 
def produto_existe(cursor, nome):
    cursor.execute("""
    SELECT 1 FROM mercadinho WHERE nome = ? 
    LIMIT 1 
    """, (nome,),) #LIMITA A APENAS UMA LINHA RETORNADA

    resultado = cursor.fetchone()   # FETCHONE RETORNA APENAS UM RESULTADO 
    return resultado is not None # VOLTA O RESULTADO SE NÃO FOR VAZIO

# FUNÇÃO PRA INSERIR PRODUTOS NO NA LISTA
def cadastrar(conexao):
    cursor = conexao.cursor() # ABRE INTERAÇÃO COM O DB

    print("\n=== Cadastrar Produto ===\n")
    nome = input("Digite o nome do produto: ").strip()
    if not nome:
        print("\nERRO: O nome não pode ficar vazio!") # ERRO CASO O NOME SEJA DEIXADO EM BRANCO
        cursor.close()
        return

    categoria =(input("Digite a categoria do produto: ")).strip()
    if not categoria.replace(" ", "").isalpha(): # VERIFICA PRA CATEGORIA RECEBER APENAS LETRAS
        print("\nERRO: Digite uma categoria válida!")
        cursor.close() # FECHA INTERAÇÃO COM O DB
        return
    
    try:
        preco = float(input("Digite o preço do produto: ").replace(",", ".")) # ACEITA NÚMEROS COM VIRGULA OU PONTO
    except ValueError:
        print("\nERRO: Digite um preço válido!")
        cursor.close()
        return

    if preco < 0: #  ERRO SE O PREÇO DO PRODUTO FOR NEGATIVO
        print("\nERRO: O preço não pode ser negativo")
        cursor.close()
        return
    
    try:
        estoque = int(input("Digite a quantidade para o estoque: "))
    except ValueError:
        print("\nERRO: O estoque aceita apenas números, tente novamente!")
        cursor.close()
        return

    if estoque < 0: # ERRO SE O ESTOQUE DO PRODUTO FOR NEGATIVO
        print("ERRO: O estoque não pode ser negativo!")
        cursor.close()
        return
    
    if produto_existe(cursor,nome):
        print(f'\nERRO: O produto {nome} já existe no banco de dados!') # AQUI ELE PUXA A VERIFICAÇÃO FEITA PELA FUNÇÃO produto_existe
    else:
        cursor.execute("""
        INSERT INTO mercadinho
        (nome, categoria, preco, estoque)
        VALUES (?,?,?,?)
        """, (nome, categoria, preco, estoque),) # MUDA OS VALORES PELOS VALORES INSERIDOS

        conexao.commit() # SALVA A MODIFICAÇÃO
        print(f'\nProduto {nome} cadastrado com sucesso!\n')

    cursor.close() # FECHA A INTERAÇÃO COM O DB