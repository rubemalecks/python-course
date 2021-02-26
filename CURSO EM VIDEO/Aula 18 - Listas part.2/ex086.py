print('''
Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores 
lidos pelo teclado:
 ___ ___ ___
|___|___|___|
|___|___|___|
|___|___|___|

Ao final, mostre a matriz na tela, com a formatação correta.\n
''')
matriz = [[0,0,0],[0,0,0],[0,0,0]]

for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Digite p/ {linha,coluna}: '))
print('='*42)
print()
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()    