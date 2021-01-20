print("""
Faça um programa que leia 3 numeros inteiros positivos e efetue o calculo de uma das seguintes médias de acordo com o valor numérico digitado pelo usuário:

Escolha:
a) Geometrica\nb) Ponderada\nc) Harmônica\nd) Aritmética\n""")


def geometrica(a, b, c):
    from math import pow
    x = pow((a * b * c), (1/3))
    return round(x)


def ponderada(a, b, c):
    x = ((a + 2) * (b + 3) * c)/6
    return (x)


def harmonica(a, b, c):
    x = 3 / ((1/a) + (1/b) + (1/c))
    return x


def aritmetica(a, b, c):
    x = (a + b + c)/3
    return x


r = ''
while r not in ('A', 'B', 'C', 'D'):
    r = input('R: ').upper()

print('-'*23)
a = int(input('Digite um numero: '))
b = int(input('Digite um numero: '))
c = int(input('Digite um numero: '))
print('-'*23)

if r == 'A':
    print(f'A média Geometrica de {a, b, c} é {geometrica(a, b, c):.2f}')

elif r == 'B':
    print(f'A média Ponderada de {a, b, c} é {ponderada(a, b, c):.2f}')

elif r == 'C':
    print(f'A média Harmônica de {a, b, c} é {harmonica(a, b, c):.2f}')

elif r == 'D':
    print(f'A média Aritmética de {a, b, c} é {aritmetica(a, b, c):.2f}')
