print(f'''Faça um algoritmo que leia um número positivo e imprima 
seus divisores.\n''')

divisores = []
n = 0
while n <= 0:
    n = int(input('Digite um número (positivo): '))

for c in range(n+1):
    if c >= 1 and n % c == 0:
        divisores.append(c)

print(f'Os divisores de n são {divisores}')