import random


def criar_baralho():
    naipes = ["Espadas", "Copas", "Paus", "Ouros"]
    valores = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    return [(valor, naipe) for valor in valores for naipe in naipes]


def valor_da_carta(carta):
    valor = carta[0]
    if valor.isdigit():
        return int(valor)
    if valor == "A":
        return 14
    if valor == "J":
        return 11
    if valor == "Q":
        return 12
    if valor == "K":
        return 13
    return 0


def calcular_pontuacao(mao):
    return sum(valor_da_carta(carta) for carta in mao)


def jogar():
    print("=== Jogo de Cartas Simplificado ===")
    nome = input("Digite o seu nome: ").strip() or "Jogador"

    baralho = criar_baralho()
    random.shuffle(baralho)

    mao_jogador = baralho[:5]
    mao_computador = baralho[5:10]

    pontuacao_jogador = calcular_pontuacao(mao_jogador)
    pontuacao_computador = calcular_pontuacao(mao_computador)

    print(f"\n{nome}, suas cartas: {mao_jogador}")
    print(f"Cartas do computador: {mao_computador}")
    print(f"Pontuação de {nome}: {pontuacao_jogador}")
    print(f"Pontuação do computador: {pontuacao_computador}")

    if pontuacao_jogador > pontuacao_computador:
        print(f"\nParabéns, {nome}! Você venceu!")
    elif pontuacao_jogador < pontuacao_computador:
        print("\nO computador venceu desta vez.")
    else:
        print("\nEmpate!")


if __name__ == "__main__":
    jogar()
