"""
Exercício Python 078:
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas
respectivas posições na lista.
"""
listanum = []
for c in range(0,5):
    listanum.append(int(input(f'Digite um valor para posição {c}: ')))
    if c == 0:
        maior = menor = listanum[c]
    else:
        if listanum[c] > maior :
            maior = listanum[c]
        if listanum[c] < menor :
            menor = listanum[c]
print('*'*33)
print(f'Você digitou os valores{listanum}')
print(f'O maior numero foi {maior} na posição', end='')
for i, v in enumerate(listanum):
    if v == maior:
        print(f' {i}... ', end='')
print()
print(f'O menor numero foi {menor} na posição', end='')
for i, v in enumerate(listanum):
    if v == menor:
        print(f' {i}... ', end='')
print()
