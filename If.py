nome = input("Digite seu nome: ")
if len(nome) > 5:  #len rtorna o número de caracteres da string
    print("Seu nome é grande")
    print(f"Seu nome é {nome} e possui {len(nome)} caracteres")
