print("""
Exercício Python 082: 
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores
ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
""")

num = list()
pares = list()
impares = list()
continuar = 'S'
while continuar == 'S':
    num.append(int(input('Digite um número: ')))
    continuar = str(input('Continuar [S/N]')).upper()
for i in num:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)
print('-='*30)
print(f'A lista completa é {num}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares {impares}')
