from math import sqrt
numero = int(input('Digite um numero: '))
if numero > 0 :
    print(f'A raiz de {numero} é {sqrt(numero):.2f}')
else: 
    print('Numero invalido')

