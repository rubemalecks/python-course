"""Escreva o menu de opções abaixo. Leia a opção do usuário e execute a
operação escolhida. Escreva uma mensagem  de erro se a opção for inválida.

[1] SOMA DE 2 NÚMEROS
[2] DIFERENÇA ENTRE 2 NÚMEROS (MAIOR PELO MENOR)
[3] PRODUTO ENTRE 2 NÚMEROS
[4] DIVISÃO ENTRE 2 NÚMEROS (DENOMINADOR NÃO PODE SER ZERO)

OPÇÃO:
"""
opcoes = 1, 2, 3, 4
while True:
    op = int(input(
        '''
    [1] SOMA DE 2 NÚMEROS
    [2] DIFERENÇA ENTRE 2 NÚMEROS (MAIOR PELO MENOR)
    [3] PRODUTO ENTRE 2 NÚMEROS
    [4] DIVISÃO ENTRE 2 NÚMEROS (DENOMINADOR NÃO PODE SER ZERO)

    OPÇÃO: '''))
    print('-'*27)

    if op not in opcoes:
        print('[OPÇÃO INVÁLIDA]')
    else:
        break

# CRIANDO AS FUNÇÕES


def soma(a, b):  # 1 = SOMA
    return f'A SOMA entre {a} + {b} = {a+b}'


def dif(a, b):  # 2 = DIFERENÇA
    if a > b:
        return f'A diferença entre {a} e {b} é {a-b}'
    elif b > a:
        return f'A diferença entre {b} e {a} é {b-a}'
    else:
        return f'{a} e {b} são IGUAIS!'


def prod(a, b):  # 3 = PRODUTO ENTRE 2 NUMEROS
    return f'{a} * {b} = {a*b}'


def div(a, b):  # 4 = DIVISÃO ENTRE 2 NUMEROS
    if a == 0 and b == 0:
        return '[NUMERADOR NÃO PODE SER ZERO] \n[DENOMINADOR NÃO PODE SER ZERO]'
    elif b == 0:
        return '[DENOMINADOR NÃO PODE SER ZERO]'
    elif a == 0:
        return '[NUMERADOR NÃO PODE SER ZERO]'
    return f'{a} / {b} = {a/b}'


# ENTRADA DO USUÁRIO
x = int(input('Digite um número: '))
y = int(input('Digite outro número: '))

print('-'*27)

if op == 1:
    print(soma(x, y))

elif op == 2:
    print(dif(x, y))

elif op == 3:
    print(prod(x, y))

elif op == 4:
    print(div(x, y))
