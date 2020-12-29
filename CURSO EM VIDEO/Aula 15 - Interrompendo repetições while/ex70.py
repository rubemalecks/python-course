"""
DESAFIO 070: Estatísticas em Produtos
Crie um programa que leia o nome e o preço de vários produtos. O programa
deverá perguntar se o usuário vai continuar. No final, mostre:
A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$ 1000.
C) Qual é o nome do produto mais barato.
"""
print('-'*25)
loja = str('LOJÃO SUPER BARATO')
loja = loja.center(25)
cont = total = totmil = 0
menor = ''
print(loja)
print('-'*25)
while True:    
    produto = str(input('Nome do Produto: '))
    preço = float(input(' Preço: '))
    print('-'*25)
    cont+=1
    total += preço
    if preço >= 1000:
        totmil += 1
    if cont == 1 or preço < menor :
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':        
        resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
        print('-'*25)
    if resp == 'N':
        break
print(f'O total da compra foi de R$ {total:.2f}')
if totmil > 1:
    print(f'Temos {totmil} produtos custando + de R$ 1.000,00')
if totmil == 1:
    print(f'Temos só {totmil} produto custando + de R$ 1.000,00')
else:
    print('Não houve produtos custando + de R$ 1.000,00')
print(f'O produto mais barato foi o {barato} custando R${menor:.2f}')            
