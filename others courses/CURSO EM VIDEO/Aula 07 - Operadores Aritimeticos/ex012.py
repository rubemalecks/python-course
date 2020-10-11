'''Exercício Python 012: 
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, 
com 5% de desconto
'''

produto = float(input('Qual o preço do produto: R$ '))
desc = produto * (5/100)
valor_final = produto - desc
print(f'O item que valia R${produto:.2f} agora vale R${valor_final:.2f}')
print(f'5% de R${produto:.2f} equivale a R${desc:.2f}')
