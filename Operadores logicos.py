numero1 = int (input("Digite o número 1: "))
numero2 = int (input("Digite o número 2: "))
numero3 = int (input("Digite o número 3: "))    
if numero1 == numero2 or numero2 == numero3 or numero1 == numero3:
    exit()
if numero1 > numero2 and numero1 > numero3:
    print("O primeiro número é maior")
if numero2 > numero1 and numero2 > numero3:
    print("O segundo número é maior")
if numero3 > numero1 and numero3 > numero2:
    print("O terceiro número é maior")
