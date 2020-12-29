'''ex018: Faça um programa que leia um ângulo qualquer a mostre na tela o 
valor do seno, cosseno e tangente desse ângulo.'''

from math import sin, cos, tan
from time import sleep
x = float(input('Digite o angulo: '))
sen = sin(x)
cos = cos(x)
tan = tan(x)
sleep(2)
print(f'O seno de {x} é {sen}')
sleep(2)
print(f'A tangente de {x} é {tan}')
sleep(2)
print(f'O cosseno de {x} é {cos}')
