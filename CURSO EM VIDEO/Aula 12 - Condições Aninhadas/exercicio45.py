from random import randint
from time import sleep
itens = ("PEDRA", "PAPEL", "TESOURA")
computador = randint(0,2)
print('''
Suas Opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
''')
while True:
    jogador = int(input('Qual sua jogada? '))
    if jogador >= 0 and jogador <=2:
        break

    else:
        print("JOGADA INVALIDA")

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)

print('=*'*20)

if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')

print('O PC ESCOLHEU {} E O JOGADOR {}'.format(itens [computador],itens [jogador]))

print('=*'*20)