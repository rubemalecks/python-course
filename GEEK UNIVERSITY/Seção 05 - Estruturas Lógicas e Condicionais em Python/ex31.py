"""Faça um programa que receba a altura e o peso de uma pessoa. De acordo com a tabela 
a seguir, verifique e mostre qual a classificação # olar ex31.py no pdf"""

altura = float(input('ALTURA: '))
peso = float(input('PESO: '))
classificacao = ''

if altura < 1.20:
    if peso < 60:
        classificacao = 'A'
    elif peso <= 90:
        classificacao = 'D'
    else:
        classificacao = 'G'
elif altura <= 1.70:
    if peso < 60:
        classificacao = 'B'
    elif peso <= 90:
        classificacao = 'E'
    else:
        classificacao = 'H'
else:
    if peso < 60:
        classificacao = 'C'
    elif peso <= 90:
        classificacao = 'F'
    else:
        classificacao = 'I'

print(f'CLASSIFICAÇÃO: {classificacao}')
