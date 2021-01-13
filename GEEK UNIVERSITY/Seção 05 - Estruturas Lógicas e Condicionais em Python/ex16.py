"""Usando switch, escreva um programa que leia um interiro entre 1 e 12
 e imprima o mês correspondente a este numero. Isto é, janeiro se 1, 
 fevereiro se 2, e assim por diante. """

while True:
    mes = input('digite um numero entre 1-12: ')
    print('-'*22)
    if mes.isnumeric() == False or int(mes) > 12 or int(mes) < 1:
        print('Valor Inválido! Tente Novamente!', '\n-'*22)
    else:
        mes = int(mes)
        break
if mes == 1:
    print(f'O {mes}º mês é Janeiro')

elif mes == 2:
    print(f'O {mes}º mês é Fevereiro')

elif mes == 3:
    print(f'O {mes}º mês é Março')

elif mes == 4:
    print(f'O {mes}º mês é Abril')

elif mes == 5:
    print(f'O {mes}º mês é Maio')

elif mes == 6:
    print(f'O {mes}º mês é Junho')

elif mes == 7:
    print(f'O {mes}º mês é Julho')

elif mes == 8:
    print(f'O {mes}º mês é Agosto')

elif mes == 9:
    print(f'O {mes}º mês é Setembro')

elif mes == 10:
    print(f'O {mes}º mês é Outubro')

elif mes == 11:
    print(f'O {mes}º mês é Novembro')

elif mes == 12:
    print(f'O {mes}º mês é Dezembro')
