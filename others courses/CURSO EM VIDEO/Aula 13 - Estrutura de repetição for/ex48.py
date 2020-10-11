"""
DESAFIO 048: Soma Ímpares Múltiplos de Três
Faça um programa que calcule a soma entre todos os números ímpares que
são múltiplos de 3 e que se encontram no intervalo de 1 até 500.
"""
s = 0
print('Todos os números ímpares que são múltiplos de 3 e estão entre 1 e 500:')

for c in range(1,500 + 1, 2):
    if c % 3 == 0:
        print(c,end=', ')
        s += c
print('\nA SOMA TOTAL É: {}'.format(s))
