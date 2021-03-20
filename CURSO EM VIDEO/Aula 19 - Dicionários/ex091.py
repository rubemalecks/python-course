  
"""
Jogo de Dados em Python
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um
dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
"""
from random import randint
from time import sleep
from operator import itemgetter
jogadores = {'jogador1' : randint(1,6),'jogador2' : randint(1,6), 'jogador3' : randint(1,6),'jogador4' : randint(1,6)}
rank = list()                        
print('Valores Sorteados ...')
for k, v in jogadores.items():
    print(f'Jogador {k} tirou {v}')
    sleep(0.7)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True) # COLOCA EM ORDEM DECRESCENTE (FALSE=ORDEM CRESCENTE)
print('='*42)
print('=== RANKING DE JOGADORES === ')
for indice, valor in enumerate(ranking):
    print(f'{indice+1}º lugar: {valor[0]} tirou {valor[1]} no dado')
    sleep(0.7)