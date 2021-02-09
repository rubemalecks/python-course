print('''Faça um programa que leia um número inteiro positivo N e imprima todos os 
números naturais de 0 até N em ordem decrescente.\n''')

n = int(input('Digite um numero: '))

for c in range(n,-1,-1):
    print(c, end='...')
print('FIM')
