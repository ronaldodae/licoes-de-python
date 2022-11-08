#condicionais

idade = int(input('digite sua idade: '))
if idade >= 18:
    print('boa, pode ser preso')
else:
    print('menor de idade')

nota_mensal = float(input('digite sua nota: '))
if nota_mensal >= 7:
    print('vc foi aprovado')
elif nota_mensal >= 5:
    print('vai pra recuperação')
else:
    print('vc foi reprovado')

media = 5
presenca = 100

if media >= 7 and presenca >= 70:
    print('aprovado')
else:
    print('reprovado')