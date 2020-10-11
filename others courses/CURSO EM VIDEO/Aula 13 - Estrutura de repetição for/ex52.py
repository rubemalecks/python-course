"""
DESAFIO 052: Números Primos
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
"""

p = 0
n = int(input('Digite um numero: '))
for c in range(1,n+1):
    if n % c == 0:
        p += 1
if p == 2:
    print('{} É UM NUMERO PRIMO!'.format(n))
else:
    print('{} NÃO É UM NUMERO PRIMO!'.format(n))
