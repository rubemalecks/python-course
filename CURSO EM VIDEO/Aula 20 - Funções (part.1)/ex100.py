"""
Faça um programa que tenha uma lista chamada números e duas funções chamadas 
sorteia() e soma_par(). A primeira função vai sortear 5 números e vai colocá-los
dentro da lista e a segunda função vai mostrar a soma entre todos os valores 
pares sorteados pela função anterior.
"""

from random import randint

def sorteia(lista):
    for n in range(5):
        lista.append(randint(0,9))


numeros_sorteados = list()
sorteia(numeros_sorteados)
print(numeros_sorteados)

def soma_par(lista_numeros):
    soma = 0
    for num in lista_numeros:
        if num % 2 == 0:
            soma+= num
    return soma

print(soma_par(numeros_sorteados))