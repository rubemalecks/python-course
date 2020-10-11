'''
faça um programa para imprimir:
    1
    2   2
    3   3   3
    .....
    n   n   n   n   n   n  ... n'''



def ordem(numero):
    x = 1
    for i in range(numero):
        print()
        for c in range(x):
            print(x, end=' ')
        x+=1
numero = int(input('Digite um numero: '))
ordem(numero)