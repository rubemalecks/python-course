'''Exercício Python 010: 
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira 
e mostre quantos dólares ela pode comprar.
'''
real = float(input('Quanto voce tem na carteira? R$ '))
dolar = real/3.27
print(f'Com R${real:.2f} voce pode comprar US${dolar:.2f}')
