import random

numero_secreto = random.randint(1, 10)
acertou = False
limite_tentativas = 5
tentativas = 0


while not acertou and tentativas < limite_tentativas:

    palpite = int(input("Tente adivinhar o número de 1 a 10: "))
    tentativas = tentativas + 1

    if palpite == numero_secreto:
        print("Acertou!")
        acertou = True
    elif palpite < numero_secreto:
        print("O numero secreto é maior")
    elif palpite > numero_secreto:
        print("O numero secreto é menor")
    else:
        print("Ainda não foi dessa vez!")

if acertou:
    print("Vc acertou em", tentativas, "tentativas")
else:
    print("Suas tentativas acabaram")
    print("O numero certo era", numero_secreto)






