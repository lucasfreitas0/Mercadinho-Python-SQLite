## VERIFICA SE O PRODUTO EXISTE NO DB
def produto_existe(cursor, nome):
    cursor.execute("""
    SELECT 1 FROM mercadinho WHERE nome = ? 
    LIMIT 1 
    """, (nome,),) #ASSIM QUE ACHAR 1 ELE PARA DE PROCURAR

    resultado = cursor.fetchone()   
    return resultado is not None # VOLTA O RESULTADO SE NÃO FOR VAZIO

# FUNÇÃO PRA INSERIR PRODUTOS NO DB
def inserir(conexao):
    cursor = conexao.cursor() # FAZ A CONEXÃO PARA EDITAR O DB

    print("=== Cadastrar Produto ===")
    nome = input("Digite o nome do produto: ")
    categoria = input("Digite a categoria do produto: ")
    preco = float(input("Digite o preço do produto: "))
    
    if produto_existe(cursor,nome):
        print(f'ERRO: O produto {nome} já existe no banco de dados!') # AQUI ELE PUXA A VERIFICAÇÃO FEITA PELA FUNÇÃO produto_existe
    else:
        cursor.execute("""
        INSERT INTO mercadinho
        (nome, categoria, preco)
        VALUES (?,?,?)
        """, (nome, categoria, preco),) # MUDA OS VALORES PELOS VALORES INSERIDOS

        conexao.commit() # SALVA A MODIFICAÇÃO
        print(f'Produto {nome} cadastrado com sucesso!\n')

    cursor.close() # FECHA A INTERAÇÃO COM O DB
