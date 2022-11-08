notas = [7.9 , 9.7 , 8.2]
lista = [26, 'Ronaldo', 3.1243124, False]
lista_de_listas = [10,[1, 2, 3]]

print(lista[1])
print(lista[2])
print(lista[0])

#slices

lista2 = [10, 40 ,30, 50, 15]

print(lista2[0:3])
print(lista2[2:5])
print(lista2[0:])
print(lista2[0:6:2])


# interacoes dom FOR

#-1 utilizando os proprios elementos da lista

for elemento in lista2:
    print(elemento)


#-2 utilizando os indices

print('comprimento da lista: ', len(lista2))

for i in range(len(lista2)):
    print(i)