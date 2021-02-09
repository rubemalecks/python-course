print('''Faça um programa que leia um número inteiro positivo impar N e imprima 
todos os números impares de 1 até N em ordem decrescente.\n''')

while True:
    n = int(input('Digite um inteiro positivo ímpar: '))
    if n % 2 != 0 and n > 0:
        break
    else:
        print('Preciso de um numero inteiro positivo ímpar!')
for c in range(n,0,-2):
    print(c,end='...')
print('fim')
