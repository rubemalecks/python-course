
"""
Cadastro de Jogador de Futebol
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o jogador do jogador
e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso
será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
"""

dados = dict()
gols = list()
dados['jogador'] = str(input('Nome do Jogador: ')).title()
partidas = int(input('Partidas jogadas: '))

for c in range(1,partidas+1):
    gols.append(int(input(f'Quantos gols na partida {c}: ')))
dados['gols'] = gols
dados['total'] = sum(gols)
print('='*42)

print(dados)

print('='*42)

for chave, valor in dados.items():
    print(f'O campo {chave} tem o valor {valor}')

print('='*42)

print(f'O jogador {dados["jogador"]} fez {partidas} partidas')

for j in range(partidas):
    print(f'=> Na {j+1}ª partida, fez {gols[j]} gols')
print(f'Foi um total de {dados["total"]} gols')