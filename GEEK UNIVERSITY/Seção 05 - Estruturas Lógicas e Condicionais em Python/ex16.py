"""Usando switch, escreva um programa que leia um interiro entre 1 e 12
 e imprima o mês correspondente a este numero. Isto é, janeiro se 1, 
 fevereiro se 2, e assim por diante. """

while True:
    mes = int(input('digite um numero entre 1-12: '))
    print('-'*22)
    if mes == 1:
        print(f'O {mes}º é Janeiro')
        break
    elif mes == 2:
        print(f'O {mes}º é Fevereiro')
        break
    elif mes == 3:
        print(f'O {mes}º é Março')
        break
    elif mes == 4:
        print(f'O {mes}º é Abril')
        break
    elif mes == 5:
        print(f'O {mes}º é Maio')
        break
    elif mes == 6:
        print(f'O {mes}º é Junho')
        break
    elif mes == 7:
        print(f'O {mes}º é Julho')
        break
    elif mes == 8:
        print(f'O {mes}º é Agosto')
        break
    elif mes == 9:
        print(f'O {mes}º é Setembro')
        break
    elif mes == 10:
        print(f'O {mes}º é Outubro')
        break
    elif mes == 11:
        print(f'O {mes}º é Novembro')
        break
    elif mes == 11:
        print(f'O {mes}º é Dezembro')
        break
    else:
        print('Valor Inválido! Tente Novamente!')
