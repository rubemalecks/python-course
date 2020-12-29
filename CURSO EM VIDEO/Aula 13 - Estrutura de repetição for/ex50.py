"""
DESAFIO 050: Soma dos Pares
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas
daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
"""
s = 0
p = 0
for c in range(1, 7):
    n = int(input('Digite um numero: '))
    if n % 2 == 0 :
        s += n
        p += 1
if p == 1:
    print('VOCÊ DIGITOU SÓ {} NUMERO PAR'.format(p))
if p > 1:
    print('VOCÊ DIGITOU {} NUMEROS PARES'.format(p))
if p != 0:
    print('A SOMA DOS NUMEROS PARES É: {}'.format(s))

else:
    print('VOCÊ NÃO DIGITOU NENHUM NUMERO PAR')
