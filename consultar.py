

def buscar(conexao): #FUNÇAO PARA BUSCAR UM PRODUTO OU TODOS
    cursor = conexao.cursor() 

    escolha = int(input(
        "1. Procurar produto.\n"
        "2. Listar todos os produtos.\n"
        "Escolha: "
        ))
    
    if escolha == 1:
        nome = input("Qual produto deseja procurar? ")

        cursor.execute("""
        SELECT * FROM mercadinho WHERE nome = ?
        """, (nome,)) # PROCURA PELO NOME DO PRODUTO DIGITADO

        resultado = cursor.fetchone()   #FETCHONE RETORNA SOMENTE UM REGISTRO

        if resultado is not None:
            id, nome, categoria, preco = resultado
            print(f'\nId: {id}\nNome: {nome}\nCategoria: {categoria}\nPreço: {preco:.2f}\n') # DEIXA UMA IDENTAÇÃO MAIS BONITA NO PRINT
        else:
            print("Produto não encontrado.")

    elif escolha == 2:
        cursor.execute("SELECT * FROM mercadinho") # SELECIONA TODOS OSS DADOS DO DB
        resultados = cursor.fetchall() # FETCHALL RETORNA TODOS OS REGISTROS DO DB

        if resultados:
            for i in resultados:
                id, nome, categoria, preco = i
                print(f'\nId: {id}\nNome: {nome}\nCategoria: {categoria}\nPreço: {preco:.2f}\n') # IDENTAÇÃO MAIS LEGÍVEL
        else:
            print("Nenhum produto cadastrado.")

    else:
        print("Opção inválida.") # SE A OPÇÃO ESCOLHIDA NÃO ESTIVER NO MENU(ESCOLHA), CAI AQUI