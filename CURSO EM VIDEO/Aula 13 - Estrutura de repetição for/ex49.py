"""
DESAFIO 049: Tabuada v2.0
Refaça o DESAFIO 009, mostrando a tabuada de um número que
o usuário escolher, só que agora utilizando um laço for.
"""
print('MOSTRANDO A TABUADA')
n = int(input('\nEscolha um numero: '))
for c in range(1, n + 1):
    print('-'*17)
    print('\nTABUADA DO {}'.format(c))
    print()
    for i in range(1, 11):
        r = c * i
        print('{:<2} x {:>2} = {}'.format(c, i, r))
print('-'*17)
