from datetime import date
print('='*22,'O ANO É BISSEXTO???','='*22)
ano = int(input('Informe o ano: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{} é um ano BISSEXTO!'.format(ano))
else:
    print('{} NÃO é BISSEXTO'.format(ano))
