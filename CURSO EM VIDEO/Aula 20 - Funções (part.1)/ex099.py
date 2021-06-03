"""
Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros
 com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual 
 deles é o maior.
"""
from time import sleep

def linha():
    print('-='*23)

def maior(*numeros):
    linha()
    print('analisando valores ...'), sleep(0.9)
    for c in numeros:
        print(c, end=' ')
        sleep(0.5)
    if len(numeros) > 0:
        m = numeros[0]
    else:
        m = 0
        print('NÃO FOI INFORMADO VALORES!')
        linha()
        return
    print(f'Foram informados {len(numeros)} valores ao todo')
    for x in numeros:
        if x > m:
            m = x
    print(f'O maior valor informado foi: {m}') 
    linha()

maior(1,2,3)


