"""
Exercício Python 009: 
Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua 
tabuada.
"""


while True:
    numero = int(input('Digite um numero: '))
    for c in range(1,10) :
        print(f'{numero} x {c} = {numero*c:2}')
    r = input('Quer continuar?(S/N)').capitalize()
    if 'N' in r :
        break
