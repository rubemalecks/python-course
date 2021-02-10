print('''Escreva um algoritmo que leia um número inteiro entre 100 e 999
 e imprima na saida cada um dos algarismos que compõem o número.\n''')

while True:
    n = int(input('Digite um número entre 100 - 999: \nR: '))
    if n >= 100 and n <= 999:
        break
    else:
        print('[entrada inválida]')
for x, c in enumerate(str(n)):
    print(c)