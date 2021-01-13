"""Faça um programa que mostre ao usuário um menu com 4 opções de operações
matemáticas (as básicas, por exemplo). O usuário escolhe uma das opções e seu 
programa então pede dois valores numéricos e realiza a operação, mostrando o 
resultado e saindo"""

print("""\n[mini calculadora]""")

print("""
[1] - adição
[2] - subtração
[3] - multiplicação
[4] - divisão
""")
op = int(input('Escolha uma operação: '))
print('-'*22)
if op == 1:
    a = int(input('Digite um numero inteiro: '))
    b = int(input('Digite um outro inteiro: '))
    print(f'Resultado é {a + b}')

elif op == 2:
    a = int(input('Digite um numero inteiro: '))
    b = int(input('Digite um outro inteiro: '))
    print(f'Resultado é {a - b}')

elif op == 3:
    a = int(input('Digite um numero inteiro: '))
    b = int(input('Digite um outro inteiro: '))
    print(f'Resultado é {a * b}')

elif op == 4:
    a = int(input('Digite um numero inteiro: '))
    b = int(input('Digite um outro inteiro: '))
    print(f'Resultado é {a / b}')
