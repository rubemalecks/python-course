print('''\nEscreva um programa que leia 10 numeros e escreva o menor valor lido 
e o maior valor lido.''')

maior, menor = None, None
for x in range(10):
    num = int(input('Digite um numero: '))
    if maior == None:
        maior, menor = num, num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
print(f'Menor numero: {menor}')
print(f'Maior numero: {maior}')
