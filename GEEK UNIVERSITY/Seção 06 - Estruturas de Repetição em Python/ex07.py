print('''\nFaça um programa que leia 10 inteiros positivos, ignorando não positivos,
e imprima sua média''')


soma, num, = 0,0
for c in range(10):
    num = int(input('Digite um numero: '))
    if num >= 0:
        soma += num
media = soma/10

print(f' A média é {media}')
