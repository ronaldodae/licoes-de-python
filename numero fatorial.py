numero = int(input('digite um numero: '))
if numero <= 0:
    print('apenas numeros positivos e inteiros')
if numero > 0:
    fatorial = 1
    for item in range(1,numero + 1):
        fatorial = fatorial * item
    print(fatorial)


