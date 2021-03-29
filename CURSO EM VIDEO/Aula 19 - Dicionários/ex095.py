"""
Aprimorando os Dicionários
Aprimore o DESAFIO 093 para que ele funcione com vários jogador, incluindo
um sistema de visualização de detalhes do aproveitamento de cada jogador.
"""

time = list()
jogador = dict()
gols = list()

while True:
    print('-'*42)
    
    gols.clear()
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: ')).title()
    jogador['partidas'] = int(input('Patidas Jogadas: '))
    for c in range(1, jogador['partidas']+1):
        gols.append(int(input(f' - Quantos gols fez na partida {c}: ')))
    jogador['gols'] = gols.copy()
    jogador['total_gols'] = sum(gols)
    time.append(jogador.copy())
    continuar = (input(str('Continuar[S/N]? '))).upper()
    if 'N' in continuar:
        break

print('=-'*21)

print('cod  ', end='')

for k in jogador.keys():
    print(f'{k:<15}', end='')
print()

print('--'*42)
for index, dado_jogador in enumerate(time):
    print(f'{index:<5}', end='')
    for dado in dado_jogador.values():
        print(f'{str(dado):<15}', end='')
    print()

while True:
    print('='*42)    
    select_jogador = int(input('Mostrar dados de qual jogador? (999 para parar) ')) 
    if select_jogador == 999:
        break
    elif select_jogador >= len(time):
        print(f'ERRO!! NÃO EXISTE JOGADOR COM CODIGO {select_jogador}!!')
    else:
        print(f'--- LEVANTAMENTO DE {time[select_jogador]["nome"]} ---')
        for part, gols in enumerate((time[select_jogador]['gols'])):
            print(f' ~ Na {part+1}ª partida ele fez {gols} gols')

print('<< VOLTE SEMPRE >>')
