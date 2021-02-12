print('''Escreva um programa que leia um número inteiro e calcule a 
soma de todos os divisores desse número, com exceção dele próprio.
ex: a soma dos divisores do número 66 é 1 + 2 + 3 + 6 + 11 + 22 + 33
= 78\n ''')

numero = int(input('Digite um numero: '))
c, soma = 0, 0
for c in range(numero):
    if c > 0 and numero % c == 0:
        soma+=c

print(f'A soma dos divisores do número {numero} é {soma}.')