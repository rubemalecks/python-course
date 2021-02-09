print('''Faça um programa que leia um número positivo par N e imprima todos os 
números pares de 0 até N em ordem crescente.\n''')

while True:
    n = int(input('Digite um inteiro positivo par: '))
    if n % 2 == 0 and n > 0:
        break
for c in range(n,0-1,-1):
    if c % 2 == 0:
        print(c, end='...')
print('fim')

