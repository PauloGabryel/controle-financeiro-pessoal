#Bibliotecas
import time
import os

#Listas para armazenamento
valores_geral = []
categorias_geral = []
descrições_geral = []

#Limpar tela
def limpar_tela():
    if os.name == "nt": #verifica se for windowns
        os.system("cls")
    else: # Linux/macOS
        os.system("clear") 

#continuar
def continuar():
    continuar = input("\nAperte ENTER para continuar: ")

#Menu
traços = "—" * 29
vazio = " " * 29
def menu():
        print(f"|{traços}|\n| Controle Financeiro Pessoal |\n|{traços}|\n|{vazio}|\n| [1] Adicionar gasto         |\n| [2] Listar gastos           |")
        print(f"| [3] Mostrar total           |\n| [4] Mostrar por categoria   |\n| [5] Sair                    |\n|{traços}|\n")

while True:
    limpar_tela()
    menu()
    while True:
        try:
            resposta = int(input("Resposta: "))
            break
        except ValueError:
            print("Digite uma opção valida")
            time.sleep(1.5)
            limpar_tela()
            menu()

    #Verificando a resposta
    if resposta == 1:
        while True:
            try:
                valor = float(input("Valor: ").strip())
                break
            except ValueError: #Tratando erro de valor
                print("Digite um valor valido!")
                time.sleep(1.5)

        categoria = input("Categoria: ").strip().title() 
        while categoria.isspace() or categoria == "" or categoria.isnumeric(): #tratamento simples
            print("Insira uma categoria valida!")
            time.sleep(1.5)
            categoria = input("Categoria: ").strip().title()

        descrição = input("Descrição: ").strip().lower()
        while descrição.isspace() or descrição == "" or descrição.isnumeric():#tratamento simples
            print("Insira uma descrição valida!")
            time.sleep(1.5)
            descrição = input("Descrição: ").strip()

        valores_geral.append(valor)
        categorias_geral.append(categoria)
        descrições_geral.append(descrição)

        time.sleep(1)
        


    #Verificando a resposta
    elif resposta == 2:
        if valores_geral == []: #Verifica se a pessoa já inseriu um gasto
            print("\nNão possui gastos!")
            time.sleep(1.5)

        else: #Mostra todos os gastos
            for i in range(0,len(valores_geral)): 
                print(f"{i+1}° Gasto:")
                print(f"Valor: {valores_geral[i]:.2f}")
                print(f"Categoria: {categorias_geral[i]}")
                print(f"Descrição: {descrições_geral[i]}\n")

            time.sleep(1)
            continuar()


    #Verificando a resposta
    elif resposta == 3:
        if valores_geral == []: #Verifica se a pessoa já inseriu um gasto
            print("\nNão possui gastos!")
            time.sleep(1.5)

        else: #Mostra o total dos gastos
            total = 0
            for i in range(len(valores_geral)):
                total = total + valores_geral[i]
            print(f"Total gasto: {total:.2f}")

            time.sleep(1)
            continuar()


    #Verificando a resposta
    elif resposta == 4:
        if valores_geral == []: #Verifica se a pessoa já inseriu um gasto
            print("\nNão possui gastos!")
            time.sleep(1.5)
        
        else:
            organizado = [] #Cria uma lista para organizar em categoria e valor
            for i in range(len(valores_geral)):
                if categorias_geral[i] not in organizado:
                    organizado.append(categorias_geral[i])
                    organizado.append(valores_geral[i])

                else:
                    soma_dos_valores = organizado[(organizado.index(categorias_geral[i]))+1] + valores_geral[i]

                    organizado.pop(organizado.index(categorias_geral[i])+1) #Remove o valor anterior
                    organizado.insert(organizado.index(categorias_geral[i])+1, soma_dos_valores) #Adiciona a soma dos valores

            for i in range(len(organizado)-1):
                if i %2 == 0:
                    print(f"{organizado[i]}: {organizado[i+1]}") 

            time.sleep(1)
            continuar()


    #Verificando a resposta
    elif resposta == 5:
        print("Saindo, aguarde", end="", flush=True)
        for i in range(3):
            time.sleep(0.5)
            print(".", end="", flush=True)
        time.sleep(1.5)
        break 


    #Verificando a resposta
    else:
        print("Digite uma opção valida!")
        time.sleep(1.5)
