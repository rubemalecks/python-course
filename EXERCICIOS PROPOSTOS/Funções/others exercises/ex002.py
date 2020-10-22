'''Faça um programa para imprimir:
    1
    1   2
    1   2   3
    .....
    1   2   3   ...  n
para um n informado pelo usuário. Use uma função que receba 
um valor n inteiro imprima até a n-ésima linha.'''

def sequencia(numero):
    lista = []
    for c in range(1,numero+1):
        lista.append(c)
        print(*lista)
numero = int(input('Digite: '))
sequencia(numero)   
