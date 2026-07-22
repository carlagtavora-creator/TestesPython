print("Calculadora")
print("Seleciona uma das operações do Menu")
print("[1] - Adição")
print("[2] - Subtração")
print("[3] - Multiplicação")
print("[4] - Divisão")
print("[5] - Potência")
print("[6] - Raiz Quadrada")
print("[7] - Porcentagem")
print("[8] - Fatorial")
print("[9] - Ajuda")
print("[0] - Sair")


        
while True: #condição de parada do loop
    opcao = input("Digite a opção desejada: ")

    if opcao == "1": #calcula a opção
        print("Adição")
        num1 = str(input("Digite o primeiro número: ")) #pede número
        lista_valor = list(num1.split(" ")) #cria lista dos valores
        soma = 0 #inicializa a soma com o elemento neutro
        for num1 in lista_valor: #percorre a lista
            soma += int(num1) #soma os valores da lista
        print(f"O resultado da adição é: {soma}")

    if opcao == "2":
        print("Subtração")
        num1 = str(input("Digite o primeiro número: "))
        lista_valor = list(num1.split(""))
        subtracao = int(lista_valor[0]) #inicializa a subtração com o primeiro elemento da lista
        for num1 in range(1, len(lista_valor)): #percorre a lista a partir do segundo elemento
            subtracao -= int(lista_valor[num1]) #subtrai os valores da lista
        print(f"O resultado da subtração é: {subtracao}")

    if opcao == "3":
        print("Multiplicação")
        num1 = str(input("Digite o primeiro número: "))
        lista_valor = list(num1.split(" "))
        multiplicacao = 1 
        for num1 in lista_valor: 
            multiplicacao *= int(num1)
        print(f"O resultado da multiplicação é: {multiplicacao}")

    if opcao == "4":
        print("Divisão")
        num1 = str(input("Digite o primeiro número: "))
        lista_valor = list(num1.split(" "))
        if (int(lista_valor[1]) == 0):
            print("Erro: Divisão por zero não é permitida.")
        else:
            divisao = int(lista_valor[0]) / int(lista_valor[1])
            resto = int(lista_valor[0]) % int(lista_valor[1])
            print(f"O resultado da divisão é: {divisao} e o resto é: {resto}")

    if opcao == "5":
        print("Potência")
        num1 = str(input("Digite o número base e expoente: "))
        lista_valor = list(num1.split(" "))
        potencia = int(lista_valor[0]) ** int(lista_valor[1])
        print(f"O resultado da potência é: {potencia}")
    
    if opcao == "6":
        print("Raiz Quadrada")
        num1 = str(input("Digite o número: "))
        lista_valor = list(num1.split(" "))
        lista_raizes = [] #cria lista vazia para armazenar os resultados das raízes quadradas
        for num1 in lista_valor: #integração dos novos numeros na lista
            lista_raizes.append(float(num1) ** (0.5)) #calcula a raiz quadrada e adiciona à lista   
        for i in range(len(lista_valor)): #integração dos resultados na lista
            print(f"O resultado da raiz quadrada é: {lista_raizes[i]}")
    
    if opcao == "7":
        print("Porcentagem")
        num1 = str(input("Digite o número e a porcentagem: "))
        lista_valor = list(num1.split(" "))
        porcentagem = (int(lista_valor[0]) * int(lista_valor[1])) / 100
        print(f"O resultado da porcentagem é: {porcentagem}")

    if opcao == "8":    
        print("Fatorial")
        num1 = str(input("Digite o número: "))
        def fatorial(num1): #tecnica para calcular o fatorial dele mesmo
            if num1<1:
                return 1
            else:
                return num1 * fatorial(num1 - 1) #EX: 4 * fatorial(3) = 4 * 3 * fatorial(2) = 4 * 3 * 2 * fatorial(1) = 4 * 3 * 2 * 1 = 24
        print(f"O resultado do fatorial é: {fatorial(int(num1))}")
    
    if opcao == "9":
        print("Ajuda")
        print("Para utilizar a calculadora, selecione uma das opções do menu e siga as instruções.")
        print("Certifique-se de digitar os números corretamente e evite divisões por zero.")
        print("Para sair da calculadora, selecione a opção [0].")

    if opcao == "0":
        print("Saindo da calculadora. Até logo!")
        break 

  


 