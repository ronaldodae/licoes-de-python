#for para repeticao controlada, troca o numero do range (1o numero onde começa, 2o numero -1 e 3o numero pulando numeros)

for variavel in range(1,10,2):
    print(variavel)

soma = 0

for i in range(1,4):
    nota = float(input(f'informe sua nota{i}:'))

    soma = soma + nota

print(soma / 3)    


