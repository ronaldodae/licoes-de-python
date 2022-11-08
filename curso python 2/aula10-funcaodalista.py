# metodos de lista

lista = [1, 3, 12, 8, 2]

#append

print('antes do append: ', lista)

lista.append(2)

print('depois do append: ', lista)


# insert

lista.insert(2, 10)

print('lista depois do insert: ', lista)


#extend

lista2 = [11, 2423, 4234]

lista.extend(lista2)

print('depois do extend: ', lista)

#pop

lista.pop()

print('lista apos o pop: ', lista)

lista.pop(0)

print('lista apos o pop2: ', lista)

#remove - sempre tira o 1o que ele encontra

lista.remove(3) 
print('lista depois do remove1: ', lista)


#count - usa pra contar elementos


print('lista depois do count2: ', lista.count(2))


#index - o indice do elemento na lista * lembrar que ele sempre começa a contar do 0*

print('qual o indice do elemento 2: ', lista.index(12))


#sort - ordenar a lista

lista.sort()
print(lista)

lista.sort(reverse=True)
print(lista)


# funcoes para listas

# len

print(len(lista))

#sum

print(sum(lista))


#max

print('maior elemento da lista: ', max(lista))

#min

print('menor elemento da lista: ' ,min(lista))