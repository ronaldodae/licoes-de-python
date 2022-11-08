# dicionarios

#criando um dicionario

dicionario = {}
dicionario = dict()

dicionario = {'nome': 'ronaldo', 'idade': 30, 'altura': 1.85}

print(dicionario)
print(dicionario['idade'])
print(dicionario['nome'])
print(dicionario['altura'])

#adicionando elementos no dicionario

dicionario['programador'] = True

print(dicionario)

dicionario['altura'] = 2

print(dicionario)

# iterando sobre um dicionario

for chave in dicionario:
    print(chave, dicionario[chave])


#testando se existe chave no dicionario


print('peso' in dicionario)
print('altura' in dicionario)
