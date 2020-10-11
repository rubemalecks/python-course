'''
Exercício Python 073: 
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela 
do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética. 
d) Em que posição está o time da Chapecoense.
'''
times = ('Corinthians','Cruzeiro','Palmeiras','Santos','Grêmio','Flamengo',
        'Vasco','Chapecoense','Atlético-MG','Botafogo','Athletico-PR',
        'Bahia','São Paulo','Fluminense','Sport','Vitória','Coritiba',
        'Avaí','Ponte Preta','Atlético-GO')
alfa = sorted(times)
print('-'*30)
print(f'{"CLASSIFICAÇÃO":^30}')
print('-'*30)

print(f'Os 5 Primeiros Colocados: {times[0:5]}')
print('-'*50)
print(f'OS 4 Ultimos Colocados: {times[-4:]}')
print('-'*50)
print(f'Em Ordem Alfabetica : {sorted(times)}')
print('-'*50)
print(f'A Chape ficou em {times.index("Chapecoense")+1}º Lugar')
print('-'*50)
print('---FIM---')
