"""
DESAFIO 063: Sequência de Fibonacci v1.0
Escreva um programa que leia um número n inteiro qualquer e mostre
na tela os n primeiros elementos de uma Sequência de Fibonacci.
Ex: 0 → 1 → 1 → 2 → 3 → 5 → 8
"""
print('-'*23)
print('Sequencia de Fibonacci')
print('-'*23)
n = int(input('Digite quantos numeros mostrar: '))
t1 = 0
t2 = 1
print('~'*23)
print('{} -> {}'.format(t1, t2),end=' -> ')
cont = 3 
while cont <= n :
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    print('{}'.format(t3),end=' -> ')
    cont += 1
print('FIM')
print('~'*23)