""" 
Faça um programa que peça ao usuário para digitar um número inteiro, informe se
este número é par ou ímpar. Caso o usuário não digite um número inteiro, informe 
que não é um número inteiro.

"""

n = input('Digite um número inteiro: ')
if n.isdigit():
    n = int(n)
    if n % 2 == 0:
        print(f'{n} é um número PAR.')
    else:
        print(f'{n} é um número ÍMPAR.')
else:
    print(f'{n} NÃO é um número inteiro.')
    