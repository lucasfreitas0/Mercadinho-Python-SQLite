# MENU RESPONSAVEL PELA INTERAÇÃO COM O USUÁRIO

from banco import conectar
from consultar import buscar
from inserir import cadastrar
from alterar import atualizar
from relatorios import relatorios

menu = ( # MENU PRINCIPAL
"=========================\n"
"      Mercadinho\n"
"=========================\n"
"\n1. Cadastrar produto\n"
"2. Consultar produto\n"
"3. Alterar oroduto\n"
"4. Relatórios\n"
"0. Sair\n"
)

# LOOP PARA AS ESCOLHAS DO MENU
conexao = conectar()

try:
    while True:
        print(menu)

        try:
            escolha = int(input("Escolha: "))

        except ValueError:
            print("Escolha apenas com números.\n")
            continue
        
        if escolha == 1:
            cadastrar(conexao)

        elif escolha == 2:
            buscar(conexao)

        elif escolha == 3:
            atualizar(conexao)

        elif escolha == 4:
            relatorios(conexao)

        elif escolha == 0:
            print("Programa encerrado!")
            break

        else:
            print("Opção inválida, tente novamente.\n")

finally:
    conexao.close()