print(''' 
O custo ao consumidor de um carro novo é a soma do custo de fábrica, da comissão
do distribuidor, e dos impostos. A comissão e os impostos são calculados sobre o 
custo da fábrica, de acordo com a tabela abaixo. Leia o custo de fábrica e escreva
o custo ao consumidor.

CUSTO DE FÁBRICA    |   % DO DISTRIBUIDOR   |       % DOS IMPOSTOS
até R$ 12.000,00    |           5           |       isento
entre 12mil e 25mil |           10          |       15
acima de 25 mil     |           15          |       20
''')

custo_fab = float(input('CUSTO DE FÁBRICA: '))

if custo_fab < 12000:
    porc_dist = 0.05
    imp = 0
elif custo_fab <= 25000:
    porc_dist = 0.10
    imp = 0.15
else:
    porc_dist = 15
    imp = 20

custo_final = (custo_fab * porc_dist) + (custo_fab * imp) + custo_fab

print(f'O preço final para consumidor é {custo_final}')