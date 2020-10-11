"""
DESAFIO 065: Maior e Menor Valores
Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre
todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele
quer ou não continuar a digitar valores.
"""

s = 0
c = 0

r = 'S'
while r == 'S' :
    x = int(input('Digite algum numero: '))
    maior = menor = media = x
    if x < menor :
        menor = x
    if x > maior :
        maior = x
    c += 1
    s += x
    media = s / c
    r = input('Quer continuar ??\nR: ').upper()
print('A soma {}'.format(s))
print('A media {:.2f}'.format(media) )
print('O menor numero ', menor)
print('O maior numero ', maior)
