'''
DESAFIO 055: Maior e Menor da Sequencia

Faça um programa que leia o peso de 5 pessoas.
No fina, mostre qual foi o maior e o menor peso lido.

'''
maior = 0
menor = 100**99
for c in range(0,5):
    peso = float(input('Digite o peso: '))
    if peso > maior :
        maior = peso
    if peso < menor :
        menor = peso
print('O maior peso foi {}kg e o menor foi {}kg'.format(maior,menor))
