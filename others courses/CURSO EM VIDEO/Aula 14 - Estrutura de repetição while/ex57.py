"""
DESAFIO 057: Validação de Dados
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto.
"""
from time import sleep
s = str(input('Informe o Sexo(F/M): ')).upper().strip()[0]
while s != 'M' and s != 'F':
    print('Invalido! Tente Novamente!')
    s = str(input('Informe o Sexo(F/M): ')).upper().strip()[0]
print('Processando...')
sleep(1.5)
print('Okay')
