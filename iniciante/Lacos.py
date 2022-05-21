import random

def jogar():

    resultado =  3 // 2
    print(resultado)

    print("Bem vindo no jogo de advinhação!")
    print("----------------------------------")

    numero_aleatorio = random.randrange(1,101)
    print(numero_aleatorio)

    print("Qual o nível de dificuldade?")
    print(" (1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    totalDeTentativas = 3

    if(nivel == 1):
        totalDeTentativas = 20
    elif(nivel == 2):
        totalDeTentativas = 10
    elif(nivel == 3):
        totalDeTentativas = 3


    numero_secreto = 42

    for rodada in range(1, totalDeTentativas + 1):
        print("Tentativa {} de {} ".format(rodada, totalDeTentativas))
        chute_str = input("Digite um número de 1 a 100: ")
        print("Você digitou: ", chute_str)
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("Você digitou um número fora do intervalo")
            continue

        acertou = chute == numero_aleatorio
        maior = chute > numero_aleatorio
        menor = chute < numero_aleatorio

        if(acertou):
            print("Você acertou na {} tentativa".format(rodada))
            break
        elif(maior):
            print("O número digitado é maior!")
        else:
            print("O número digitado é menor!")

    print("Fim de jogo")



