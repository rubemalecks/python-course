from math import sqrt
numero = int(input('Digite um numero: '))
if numero > 0:
    print(f'A a raiz qudrada é {sqrt(numero):.2f}')
else: 
    print(f'{numero} ao quadrado é {numero**2}')
    