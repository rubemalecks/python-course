print('''
Escreva um programa que, dado o valor da venda, imprima a comissão 
que deverá ser paga ao vendedor. Para calcular a comissão, considere 
a tabela abaixo:

VENDA                           |           COMISSÃO
> ou igual a R$ 100.000,00      |           R$ 700,00 + 16% das vendas
< R$ 100 mil e >ou =  R$80 mil  |           R$ 650,00 + 14% das vendas
< R$ 80 mil e > ou = R$ 60 mil  |           R$ 600,00 + 14% das vendas
< R$ 60 mil e>ou = a R$ 40 mil  |           R$ 550,00 + 14% das vendas
< R$ 40 mil e>ou = a R$ 20 mil  |           R$ 500,00 + 14% das vendas
< que R$ 20 mil                 |           R$ 400,00 + 14% das vendas
''')

venda = float(input('Valor Vendido: R$ '))
print('-'*23)
if venda < 20000:
    comissao = (venda * 0.14) + 400
elif venda < 40000:
    comissao = (venda * 0.14) + 500
elif venda < 60000:
    comissao = (venda * 0.14) + 550
elif venda < 80000:
    comissao = (venda * 0.14) + 600
elif venda < 100000:
    comissao = (venda * 0.14) + 650
else:
    comissao = (venda * 0.16) + 700

print(f'Venda: R$ {venda:.2f}\nComissão: R$ {comissao:.2f}')
