print('='*22, 'Qual o maior e o menor numero???', '='*22)
x = int(input('Digite um numero: '))
y = int(input('Digite outro numero: '))
z = int(input('Digite mais um numero: '))
maior = x
if y > x and x > z:
    maior = y
if z > y and z > x:
    maior = z
if x < y and x < z:
    menor = x
if y < x and y < z:
    menor = y
if z < y and z < x:
    menor = z
print('O menor numero foi {}'.format(menor))
print('O maior numero foi {}'.format(maior))
