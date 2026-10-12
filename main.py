from inserir import inserir 
from consultar import buscar

menu = (
"1. Cadastrar produto\n"
"2. Consultar produto"
)
print(menu)

escolha = int(input("Escolha: "))
if escolha == 1:
    inserir()
elif escolha == 2:
    buscar()
else:
    print("Até logo!")
