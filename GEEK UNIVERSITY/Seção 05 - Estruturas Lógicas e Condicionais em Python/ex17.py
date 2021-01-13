"""Faça um programa que calcule a area de um trapézio"""

base_maior = float(input('base maior: '))
base_menor = float(input('base menor: '))
altura = float(input('altura: '))
area = ((base_maior + base_menor) * altura)/2
print(f'A área do trapézio é {area}')
