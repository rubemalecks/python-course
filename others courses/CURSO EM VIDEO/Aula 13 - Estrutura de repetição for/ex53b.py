"""
DESAFIO 053: Detector de Palíndromo
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
"""
frase =  str(input('Digite uma frase: ')).upper()
frase0 = frase.replace(' ','')
inverso = ''
for letra in range(len(frase0)-1, -1, -1) :
    inverso += frase0[letra]
if inverso == frase0 :
    print('TEMOS UM PALINDROMO!')
    print('O contrario de {} é {}!'.format(frase0, inverso))
else:
    print('Não é um palindromo!')
    print('\nO contrario de {} é {}!'.format(frase0, inverso))
