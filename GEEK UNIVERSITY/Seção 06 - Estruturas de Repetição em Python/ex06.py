print('''\nFaça um programa que leia 10 inteiros e imprima sua média\n''')
soma, num, = 0,0
for c in range(10):
    num = int(input('Digite um numero: '))
    soma += num
media = soma/10

print(f' A media é {media}')
