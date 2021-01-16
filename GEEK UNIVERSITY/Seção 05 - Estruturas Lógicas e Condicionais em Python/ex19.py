""" Faça um programa para verificar se um determinado número inteiro é divisível 
por 3 ou 5, mas não simultaneamente pelos dois"""


num = int(input('Digite um numero inteiro: '))

if num % 3 == 0 and num % 5 == 0:
    print('[ERROR] o numero deve ser divisível por 3 [OU] 5')
elif num % 3 == 0:
    print(f'{num} é divisível por 3')
elif num % 5 == 0:
    print(f'{num} é divisível por 5')
else:
    print(f'{num} não é divisível por 3 nem por 5')
