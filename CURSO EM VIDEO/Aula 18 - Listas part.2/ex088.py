print('''
Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai 
perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada 
jogo, cadastrando tudo em uma lista composta.
''')

numero_sorteado = list()
jogo_sorteado = list()
from time import sleep
from random import randint
q_jogos = int(input('Quantidade de Jogos: '))
print('Sorteando...', end=''), sleep(2)
print()
for c in range(0, q_jogos):
    for i in range(0,6):
        numero_sorteado.append(randint(1,60))
        if numero_sorteado not in jogo_sorteado:
            jogo_sorteado.append(numero_sorteado[:])
            numero_sorteado.clear()
        else:
            while True:
                if numero_sorteado in jogo_sorteado:
                    numero_sorteado.clear()
                    numero_sorteado.append(randint(1,60)) 
                else:
                    break                 
            jogo_sorteado.append(numero_sorteado[:])
            numero_sorteado.clear()
    jogo_sorteado.sort()
    print(f'Jogo {c+1} : {jogo_sorteado}')
    sleep(1)
    jogo_sorteado.clear()


    
