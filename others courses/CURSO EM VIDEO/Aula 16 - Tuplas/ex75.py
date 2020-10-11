'''
Exercício Python 075: 
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
'''
import colorama
from time import sleep
colorama.init()
print('\033[7;35;40m Análise de dados em uma Tupla \033[m')
pares = 0
print()


v = int(input('Digite um valor: ')), int(input('Outro: ')), int(input('Outro: ')), int(input('Outro: '))
print()
print('Processando...')
sleep(2)
print(f'O Numero 9 apareceu {v.count(9)} vezes')
if 3 in v:
    print(f'O nº 3 apareceu primeiramente na {v.index(3)+1}ª posição ')
else:
    print('Não foi digitado o numero 3')
for numeros  in v:
    if numeros % 2 == 0:
        pares += 1
if pares == 0:
    print('Não houve numeros pares')
elif pares == 1:
    print(f'Só houve {pares} numero par ')
else:    
    print(f'Temos {pares} numeros pares ')



