print('''\nFaça um programa que leia um número inteiro N e depois imprima os N
primeiros números naturais ímpares.''')

n = int(input('Digite um numero: '))

for c in range(n+1):
    if c % 2 != 0:
        print(c, end='...')
print('fim')