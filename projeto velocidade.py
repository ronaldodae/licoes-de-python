velocidade = int(input('qual foi a sua velocidade? '))
velocidade_maxima = 80
if velocidade <= velocidade_maxima:
    print('nao houve multa')
elif velocidade > velocidade_maxima and velocidade <= velocidade_maxima + 10:
    print('multa leve')
elif velocidade > velocidade_maxima +11 and velocidade <= velocidade_maxima +20:
    print('multa grave')
elif velocidade >= velocidade_maxima +21 :
    print('perdeu a carta mané')
