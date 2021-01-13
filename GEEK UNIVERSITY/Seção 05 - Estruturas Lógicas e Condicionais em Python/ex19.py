""" Faça um programa para verificar se um determinado número inteiro e divisível 
por 3 ou 5, mas não simultaneamente pelos dois"""

c = 1
while True:
    c += 1
    if c % 3 == 0 and c % 5 != 0 or c % 5 == 0 and c % 3 != 0:
        print(f'{c}')
    if c == 100:
        break
