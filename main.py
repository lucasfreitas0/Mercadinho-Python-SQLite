from banco import conectar
from consultar import buscar
from inserir import inserir
from alterar import atualizar

conexao = conectar()

menu = (
"1. Cadastrar produto\n"
"2. Consultar produto\n"
"3. Alterar Produto\n"
"4. Sair"
)

while True:
    try:

        print(menu)
        escolha = int(input("Escolha: \n"))
        
        if escolha == 1:
            inserir(conexao)

        elif escolha == 2:
            buscar(conexao)

        elif escolha == 3:
            atualizar(conexao)

        elif escolha == 4:
            conexao.close()
            print("Programa encerrado!")
            break

        else:
            print("Opção inválida, tente novamente.")

    except ValueError:
        print("Escolha apenas com números.")
