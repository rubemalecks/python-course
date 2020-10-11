
"""
DESAFIO 071: Simulador de Caixa Eletrônico
Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao
usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas
cédulas de cada valor serão entregues.
OBS: Considere que o caixa possui cédulas de R$ 50, R$ 20, R$ 10 e R$ 1.
"""
c50 = c20 = c10 = c01 = 0
banco = 'BANCO CEV'
print('='*27)
print()
print(banco.center(27))
print()
print('='*27)

valor = int(input('Valor Sacado: '))
while valor >= 50 :
    valor -= 50
    c50 += 1
while valor >= 20 :
    valor -= 20
    c20 += 1
while valor >= 10 :
    valor -= 10 
    c10 += 1
while valor >= 1 :
    valor -= 1
    c01 += 1
print(f'Total de {c50} cédulas de R$ 50,00')
print(f'Total de {c20} cédulas de R$ 20,00')
print(f'Total de {c10} cédulas de R$ 10,00')
print(f'Total de {c01} cédulas de R$ 1,00')



