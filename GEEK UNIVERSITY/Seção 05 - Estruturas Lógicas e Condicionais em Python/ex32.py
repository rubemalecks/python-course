"""Escreva um programa que leia o código do produto escolhido do cardápio de uma 
lanchonete e a quantidade. O programa deve calcular o valor a ser pago por aquele 
lanche. Considere que cada execução somente será calculado um pedido. 
[O cardápio da Lanchonete está no pdf]"""

print('*'*23)

print('''
CARDÁPIO 

PRODUTO           | CÓDIGO  | PREÇO
CACHORRO QUENTE   |   100   | 1,20
BAURU SIMPLES     |   101   | 1,30
BAURU COM OVO     |   102   | 1,50
HAMBURGUER        |   103   | 1,20
CHEESEBURGUER     |   104   | 1,70
SUCO              |   105   | 2,20
REFRIGERANTE      |   106   | 1,00
''')

escolha = int(input('Codigo do Produto: '))
quantidade = int(input('Quantos? '))

if escolha == 100:
    a_pagar = quantidade * 1.20
    print(f'Total a Pagar R$ {a_pagar:.2f}')
elif escolha == 101:
    a_pagar = quantidade * 1.30
    print(f'Total a Pagar R$ {a_pagar:.2f}')
elif escolha == 102:
    a_pagar = quantidade * 1.50
    print(f'Total a Pagar R$ {a_pagar:.2f}')
elif escolha == 103:
    a_pagar = quantidade * 1.20
    print(f'Total a Pagar R$ {a_pagar:.2f}')
elif escolha == 104:
    a_pagar = quantidade * 1.70
    print(f'Total a Pagar R$ {a_pagar:.2f}')
elif escolha == 105:
    a_pagar = quantidade * 2.20
    print(f'Total a Pagar R$ {a_pagar:.2f}')
elif escolha == 106:
    a_pagar = quantidade * 1.00
    print(f'Total a Pagar R$ {a_pagar:.2f}')
