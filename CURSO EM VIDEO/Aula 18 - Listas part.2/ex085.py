print('''
Crie um programa onde o usuário possa digitar 7 valores numéricos e cadastre-os
em uma lista única que mantenha separados os valores pares e ímpares. No final,
mostre os valores pares e ímpares em uma ordem crescente.
''')
#[[2,4,6][1,3,5,7]]

n = int()
impar = list()
par = list()
lista_num = list()

c = 1
while c <= 7:
    n = int(input(f'Digite o {c}º número: '))
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    c+=1
par.sort()
impar.sort()
lista_num.append(par)
lista_num.append(impar)
print(f'Os números pares são: {lista_num[0]}')
print(f'Os números impares são: {lista_num[1]}')
