"""CALCULAR RAIZES DE 2º GRAU"""


def raizes(a, b, c):
    d = (b**2 - 4 * a * c)
    x1 = (-b + d**(1/2)) / (2*a)
    x2 = (-b - d**(1/2)) / (2*a)
    if d < 0:
        print('NÃO EXISTE RAIZ!')
    elif d == 0:
        print('Raiz Unica', x1)
    else:
        print(x1, x2)


r = 'S'
while r == 'S':
    print('-'*23)
    a = int(input('A: '))
    b = int(input('B: '))
    c = int(input('C: '))
    print('-'*23)
    print(f'R: ')
    raizes(a, b, c)
    print('-'*23)
    r = str(input('Deseja continuar? [S/N]\nR:'))[0].upper()
    if r == 'N':
        break
