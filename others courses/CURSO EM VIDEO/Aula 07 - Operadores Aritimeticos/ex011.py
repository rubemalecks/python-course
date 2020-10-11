'''Exercício Python 011: 
Faça um programa que leia a largura e altura de uma parede em metros, 
calcule a sua área e a quantidade de tintas necessárias para pintá-la, 
sabendo que cada litro de tinta, pinta uma área de 2m² 
'''

Largura = float(input('Largura da Parede: '))
Altura = float(input('Altura da parede: '))
Area = Largura * Altura
print(f'A parede tem a dimenção de {Largura}x{Altura}')
print(f'Sua area é de {Area}m²')
print(f'Para pintar a parede será necessario {Area/2:.2f}lt de tinta.')
