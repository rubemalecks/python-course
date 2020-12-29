"""
DESAFIO 051: Progressão Aritmética
Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.
"""
print('#' * 22)
print('TERMOS DE UMA P.A')
print('#' * 22)

pt = int(input('PRIMEIRO TERMO: '))
rz = int(input('RAZÃO: '))

for c in range(1,11):
    print(pt, end=' => ')
    pt+= rz
print('FIM')
