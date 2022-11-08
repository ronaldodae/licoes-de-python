# funcoes

# 1. o que sao funcoes e como utiliza-las?

#funcoes que ja utilizamos anteriormente

'''print() # mostra a mensagem (int,float,str) no console, termimnal, cmd
input() # retorna um dado informado pelo usuario (entrada padrao) e pode receber uma string
len() # recebe uma lista e retorna o tamanho da lista
max() # retorna o maior valor de uma lista'''


# 2 criacao de funcoes

#funcao inicial

def saudacao():
    print('seja bem vindo!')
    print('ola é um prazer ter vc no curso')

saudacao()
saudacao()
saudacao()


#funcao com parametros


def saudacao(nome, curso):
    print(f'seja bem vindo, {nome}!')
    print(f'ola é um prazer ter vc no curso de {curso}')

saudacao('ronaldo', 'Python')


#funcao com parametros default

def saudacao(nome, curso='Python'):
    print(f'seja bem vindo, {nome}!')
    print(f'ola é um prazer ter vc no curso de {curso}')

saudacao('ronaldo')


#funcoes com retorno

def soma(num1, num2):
    return num1 + num2

resultado = soma(5, 7)

print('o resultado da soma é', resultado)


def calculadora(num1, num2, operacao='+'):
    if operacao =='+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2

resultado = calculadora(10,20, '-')

print(resultado)