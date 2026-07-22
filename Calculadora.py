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
            subtracao -= int(lista_valor[i]) #subtrai os valores da lista
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

    if opcao == "9":
        print("Ajuda")
        print("Para utilizar a calculadora, selecione uma das opções do menu e siga as instruções.")
        print("Certifique-se de digitar os números corretamente e evite divisões por zero.")
        print("Para sair da calculadora, selecione a opção [0].")

    if opcao == "0":
        print("Saindo da calculadora. Até logo!")
        break 

  


 