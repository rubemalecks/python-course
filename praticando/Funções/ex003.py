'''Faça um programa, com uma função que necessite de três argumentos, 
e que forneça a soma desses três argumentos.'''

def soma(x,y,z):
    return x + y + z
x = int(input('Digite um numero: '))
y = int(input('Digite um numero: '))
z = int(input('Digite um numero: '))
print(f'O resultado da soma entre {x, y, z} é: \n{soma(x, y, z)}')
