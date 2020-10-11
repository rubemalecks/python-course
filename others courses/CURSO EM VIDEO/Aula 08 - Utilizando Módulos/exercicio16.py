'''ex016: Crie um programa que leia um número Real qualquer pelo teclado 
e mostre na tela a sua porção Inteira.
Ex: Digite um número: 6.127
      O número 6.127 tem a parte Inteira 6'''

from math import trunc
x = float(input('Digite um numero: '))
print(trunc(x))
