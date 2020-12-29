"""
DESAFIO 058: Jogo da Adivinhação v2.0
Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos
palpites foram necessários para vencer.
"""
from time import sleep
c = 1
x = ''
from random import randint
print('Pensando em um numero ...')
sleep(2)
pc = randint(0,10)
while pc != x:
    x = int(input('Tente adivinhar o numero: '))
    if x == pc:
        print('Parabéns você ACERTOU!')
    else:
        print('Errou!!!')
        c += 1
if c == 1:
    print('Só precisou de {} tentativa'.format(c))
else:
    print('Precisou de {} tentativas'.format(c))
