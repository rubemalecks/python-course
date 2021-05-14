""" 
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito,
exiba a saudação apropriada. 
Ex:
bom dia 0-11, boa tarde, 12-17 e boa noite 18-23
"""

n = input('Digite um horário(0-23): ')

if n.isdigit():
    n = int(n)
    if n < 0 or n > 23:
        print(f'{n} É um valor inválido.')
    elif n <= 11:
        print('Bom Dia.')
    elif n <= 17:
        print('Boa Tarde.')
    else:
        print('Boa Noite.')
else:
    print(f'{n} não é um valor válido.')

