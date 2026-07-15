numero_camisa = int(input("Digite o número da camisa: "))
valor_camisa = 12.50
valor_final = numero_camisa * valor_camisa
if numero_camisa <= 5:
    valor_final = valor_final * (1 - 3/100)  # Desconto de 3%
elif numero_camisa <= 10:
    valor_final = valor_final * (1 - 5/100)  # Desconto de 5%
else:
    valor_final = valor_final * (1 - 7/100)  # Desconto de 7%~
    print(f"O valor final da compra é: R${valor_final:.2f}")