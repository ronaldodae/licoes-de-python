import random
valor_aleatorio = random.randint(1,10)
chute = int(input('chute um numero: '))
acertou = False
while acertou == False:
    chute = int(input('chute um numero: '))
    if chute > valor_aleatorio:
        print('chute foi maior que o esperado')
    elif chute < valor_aleatorio:
        print('chute foi menor que o esperado')
    elif chute == valor_aleatorio:
        acertou == True
        print('voce acertou')




