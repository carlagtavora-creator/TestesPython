while True:
    n1 = int(input("Digite um número: "))
    n2 = int(input("Digite outro número: "))
    if n2 == 0:
        print("Não é possível dividir por zero. Tente novamente.")
        break #parar de pedir numeros até sair o print de cima
    print(f"A divisão de {n1} por {n2} é: {n1 / n2}")