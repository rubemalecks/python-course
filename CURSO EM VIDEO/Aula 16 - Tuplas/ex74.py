'''
Exercício Python 074: 
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 
Depois disso, mostre a listagem de números gerados e também indique o menor e 
o maior valor que estão na tupla.
'''
from random import randint
n = randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10)
print('Os valores sorteados foram: ')
for c in n:
    print(f'{c}', end = ' ')
print()
print(f'O maior numero foi {max(n)}')
print(f'O maior numero foi {min(n)}')
