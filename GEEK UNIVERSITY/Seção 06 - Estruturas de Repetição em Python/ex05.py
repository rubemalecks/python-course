print('''Faça um programa que peça ao usuário para digitar 10 valores e some-os.''')

cont_num, soma_num = 0,0
while cont_num < 10:
    num = int(input('Digite um numero: '))
    soma_num += num
    cont_num += 1

print(f'O resultado foi {soma_num}')