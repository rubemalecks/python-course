"""
Faça um programa que tenha uma lista chamada números e duas funções chamadas 
sorteia() e soma_par(). A primeira função vai sortear 5 números e vai colocá-los
dentro da lista e a segunda função vai mostrar a soma entre todos os valores 
pares sorteados pela função anterior.
"""

from random import randint
from time import sleep
def sorteia(lista):
    print('Sorteando 5 números: ', end='')
    for n in range(5):
        aleatorio = (randint(0,9))
        print(f'{aleatorio}', end=' ')
        sleep(0.9)
        lista.append(aleatorio)
    print()


numeros_sorteados = list()
sorteia(numeros_sorteados)


def soma_par(lista_numeros):
    soma = 0
    for num in lista_numeros:
        if num % 2 == 0:
            soma+= num
    print(f'Somando os valores pares entre: {lista_numeros}, é {soma}')

soma_par(numeros_sorteados)