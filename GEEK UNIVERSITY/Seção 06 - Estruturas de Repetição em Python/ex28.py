print("""Faça um programa que leia um valor N inteiro e positivo, calcule 
e mostre o valor E, conforme a fórmula a seguir.
h(n)= 1 + 1/2! 1/2! + 1/3! + 1/4! + ... 1/n!)\n""")
''
from math import factorial
n = 0
while n <= 0:
    n = int(input('Digite um numero positivo: '))
n_hrm = 0
for c in range(n+1):
    n_hrm += (1/factorial(c))
print(f'Resposta: {n_hrm}')