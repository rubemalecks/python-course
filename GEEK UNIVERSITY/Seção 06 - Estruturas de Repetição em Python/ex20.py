print('''Ler uma sequência de números inteiros e determinar se eles são 
pares ou não. Deverá ser informado o número de dados lidos e o número de 
valores pares. O processo termina quando for digitado 1000\n''')

qtd_par, dados = 0, 0
while True:
    n = int(input('Digite um valor: '))
    if n == 1000:
        break
    if n % 2 == 0:
        print(f'{n} É PAR!')
        qtd_par+=1
    else:
        print(f'{n} NÃO É PAR ...')
    dados+=1
print(f'De {dados} lidos {qtd_par} pares achados!')