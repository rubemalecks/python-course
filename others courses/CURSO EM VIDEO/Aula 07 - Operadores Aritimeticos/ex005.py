'''Exercício Python 005: 
Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.
'''
from time import sleep
numero = int(input('Digite um numero: '))
print('processando...')
sleep(3)
antecessor = numero - 1
sucessor = numero + 1
print(f'Analisando o valor {numero}, seu antecessor é {antecessor} e o sucessor é {sucessor}')
