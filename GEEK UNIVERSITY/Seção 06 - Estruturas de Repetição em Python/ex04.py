print('''Escreva um programa que declare um inteiro, inicialize-o com 0,
e incremente-o  de 1000 em 1000, até que seu valor seja 100mil.''')

from time import sleep
num = 0

while num<= 100000:
    sleep(0.08)
    print(num)
    num+= 1000