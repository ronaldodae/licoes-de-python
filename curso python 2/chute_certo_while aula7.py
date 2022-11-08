import random

numero_sorteado = int(random.randint(1,10))

numero_escolhido = int(input('Escolha um numero entre 1 e 10 agora serio: '))

while numero_escolhido !=  numero_sorteado:
    print('voce errou o numero, tente novamente! ')

    numero_escolhido = int(input('Escolha um numero entre 1 e 10 agora serio: '))

if numero_escolhido == numero_sorteado:
    print('acertou miseravi')

# chute certo com numero random :)
