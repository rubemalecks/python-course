"""Faça um programa que receba 3 numeros e mostre-os em ondem crescente"""


num1 = int(input('Digite: '))
num2 = int(input('Digite: '))
num3 = int(input('Digite: '))

# Soted + descompactação de listas *

numeros = [num1, num2, num3]
print(*sorted(numeros))
