print('''

Leia uma data e determine se ela é válida. Ou seja, verifique se 
o mês está entre 1 e 12, e se o dia existe naquele mês. 
Note que fevereiro tem 29 dias em anos não bissextos.
-------------------------------------''')

data = input('DATA: (dd/mm/aaaa): ').split('/')
meses31 = (1, 3, 5, 7, 8, 10, 12)

dia, mes, ano = int(data[0]), int(data[1]), int(data[2])

if mes >= 1 and mes <= 12:
    data[1] = 'válido'
    if dia >= 1 and dia <= 31:
        if mes == 2:
            if ano % 400 == 0 and dia <= 29:
                data[0] = 'válido'
            elif ano / 4 == 0 and ano % 100 != 0 and dia <= 29:
                data[0] = 'válido'
            elif dia > 28:
                print('ano não bissexto')
            else:
                data[0] = 'válido'

if data[0] == data[1]:
    print('data válida')
