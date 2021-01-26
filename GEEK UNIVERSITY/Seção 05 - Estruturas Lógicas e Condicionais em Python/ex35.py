print('''

Leia uma data e determine se ela é válida. Ou seja, verifique se 
o mês está entre 1 e 12, e se o dia existe naquele mês. 
Note que fevereiro tem 29 dias em anos não bissextos.
-------------------------------------''')

dia = int(input('DIA: '))
mes = int(input('MÊS: '))
ano = int(input('ANO: '))
print('-------------------------------------')
mesf = mes
diaf = dia

meses31 = 1, 3, 5, 7, 8, 10, 12

if ano % 400 == 0:
    bissexto = True
elif ano % 4 == 0 and ano % 100 != 0:
    bissexto = True
else:
    bissexto = False


# CONFERINDO MÊS
if mes > 0 and mes <= 12:
    pass
else:
    mes = None

# CONFERINDO DIA

if dia == 29 and mes == 2:
    if bissexto == True:
        pass
    else:
        dia = None
elif mes == 2 and dia > 29:
    dia = None

elif dia > 0 and dia <= 31:
    if dia == 31 and mes not in meses31:
        dia = None
    else:
        pass
else:
    dia = None


if dia != None and mes != None and ano != None:
    print(f'DATA VÁLIDA\n {dia} / {mes:02d} / {ano}')
else:
    print('DATA INVÁLIDA')
    print(f'{diaf}/{mesf:02d}/{ano}')
    if dia == None:
        print('dia inválido!')
    if mes == None:
        print('mês inválido')
