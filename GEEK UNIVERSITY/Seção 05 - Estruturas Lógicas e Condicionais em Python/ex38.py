print('''

Digite sua data de nascimento
-------------------------------------''')

data = input('DATA: (dd/mm/aaaa): ').split('/')
meses31 = (1, 3, 5, 7, 8, 10, 12)

dia, mes, ano = int(data[0]), int(data[1]), int(data[2])
final = ''

if mes >= 1 and mes <= 12 and ano != 0:
    final = 'DATA VÁLIDA'
    if mes == 2 and dia <= 29 :
        if ano % 400 == 0:
            final = 'DATA VÁLIDA'
        elif ano % 4 == 0 and ano % 100 != 0:
            final = 'DATA VÁLIDA'
        else:
            final = 'DATA INVÁLIDA'
    elif mes == 2 and dia > 29:
        final = 'DATA INVÁLIDA'
    
    elif mes not in meses31:
        final = 'DATA INVÁLIDA'
        
    elif dia == 0 or dia > 31:
        final = 'DATA INVÁLIDA'

else:
    final = 'DATA INVÁLIDA'

print(f'{dia:02d}/{mes:02d}/{ano} --- {final}')
