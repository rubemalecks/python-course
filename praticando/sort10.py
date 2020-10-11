from time import sleep
from random import randint
lista = []

sorteado = int()
while len(lista) < 10:
    sorteado = randint(1, 10)
    lista.append(sorteado)
    for c in lista:
        if sorteado == c:
            if lista.count(c) > 1:
                lista.pop()

print('final: ', lista)
