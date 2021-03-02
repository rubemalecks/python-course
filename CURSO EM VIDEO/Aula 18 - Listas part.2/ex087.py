print('''
Aprimore o desafio anterior, mostrando no final:

(A) A soma de todos os valores pares digitados.
(B) A soma dos valores da terceira coluna.
(C) O maior valor da segunda linha.
''')

matriz = [[0,0,0],[0,0,0],[0,0,0]]
maior2linha = soma_pares = soma3coluna = 0

for linha in range(0, 3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha, coluna}]: '))
        if matriz[linha][coluna] % 2 == 0:
            soma_pares+= matriz[linha][coluna]
        if coluna == 2:
            soma3coluna+= matriz[linha][coluna]
        if linha == 1:
            if matriz[linha][coluna] > maior2linha:
                maior2linha = matriz[linha][coluna]
print('#'*42)
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
print('#'*42)
print(f'(A) A soma de todos os valores pares digitados: {soma_pares}')
print(f'(B) A soma dos valores da terceira coluna: {soma3coluna}')
print(f'(C) O maior valor da segunda linha: {maior2linha}')
