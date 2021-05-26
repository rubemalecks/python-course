"""
Faça um programa que tenha uma função chamada area(), que receba dimensões de 
um terreno retangular (largura e comprimento) e mostre a área do terreno.
"""

def area(x, y):
    print(f'A area do terreno é: {x*y}m²')

largura = float(input('Largura: '))
comprimento = float(input('Comprimento: '))

area(largura, comprimento)
