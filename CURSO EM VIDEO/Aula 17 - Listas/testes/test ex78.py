"""
Exercício Python 078:
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas
respectivas posições na lista.
"""

for c in range(0,5):
    numeros = [input('Digite um numero:')]
    if c <= 1:
        menor = maior = numeros
    if numeros < menor :
        menor = numeros
    if numeros > maior :
        maior = numeros
print(f'O maior numero é {maior}')
print(f'O menor numero é {menor}')
