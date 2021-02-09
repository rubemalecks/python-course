print('''Faça um programa que leia um número inteiro positivo N e calcule a soma 
dos N primeiros números naturais.\n''')


soma = 0
while True:
    n = int(input('Digite um inteiro positivo: '))
    if n > 0:
        break
for c in range(n+1):
    soma += c

print(f'O resultado da soma é {soma}')
